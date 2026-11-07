"""
T1: transforms a BESSER Problem DSL ObjectModel into a QUBO Solution DSL (.py).

Use from the project root:
    python transformations/t1_problem_to_qubo.py
    python transformations/t1_problem_to_qubo.py code/object/problem_DSL_object_diagram.py [or orther valid object diagram]

Optional arguments:
    --solution-metamodel code/solution_DSL_class_diagram.py
    --output-dir transformations/generated
    --slack-encoding bounded # or binary

The generated file defines the Solution DSL structural
metamodel and a concrete BESSER ObjectModel.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime
from itertools import combinations
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = ROOT / "code/object/small_problem_DSL_object_diagram.py"
DEFAULT_METAMODEL = ROOT / "code/solution_DSL_class_diagram.py"
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parent / "generated"


@dataclass(frozen=True)
class ProjectInput:
    identifier: str
    cost: int
    benefit: int
# Represents a Project from the original model


@dataclass(frozen=True)
class ProblemInput:
    budget: int
    projects: tuple[ProjectInput, ...]
# Represents the Problem itself, budget + available projects


@dataclass(frozen=True)
class Qubo:
    names: tuple[str, ...]
    slack_weights: tuple[int, ...]
    penalty: int
    constant: int
    linear: dict[int, int]
    quadratic: dict[tuple[int, int], int]
# mathematical result of the transformation 


def object_attribute(obj, name: str):
    """Retrieve the underlying Python value from a BESSER AttributeLink slot."""
    found = [slot.value.value for slot in obj.slots if slot.attribute.name == name]
    if len(found) != 1:
        raise ValueError(f"Expected one attribute {name!r} on object {obj.name!r}")
    return found[0]
# Reads attributes from BESSER's objects


def is_associated_project(project, problem) -> bool:
    """Check the BESSER association, not just membership in object_model.objects."""
    for link in project.links:
        if link.association.name != "ProjectClass_SelectionProblem":
            continue
        endpoints = [end.object for end in link.connections]
        if any(obj is project for obj in endpoints) and any(obj is problem for obj in endpoints):
            return True
    return False
# verifies if the associations in the Problem Object Model are the same as in the metamodel


def load_problem(input_file: Path) -> ProblemInput:
    namespace = runpy.run_path(str(input_file))
    object_model = namespace.get("object_model")

    if object_model is None:
        raise ValueError(f"{input_file} does not define 'object_model'")

    # Retrieve the problem instance and its candidate projects according to their classes in the Problem DSL.
    problems = [obj for obj in object_model.objects
                if obj.classifier.name == "SelectionProblem"]
    candidates = [obj for obj in object_model.objects
                  if obj.classifier.name == "ProjectClass"]
    
    if len(problems) != 1:
        raise ValueError(f"Expected one SelectionProblem, found {len(problems)}")
    
    problem = problems[0]
    budget = object_attribute(problem, "budget")

    if type(budget) is not int or budget < 0:
        raise ValueError("SelectionProblem.budget must be a non-negative integer")

    projects: list[ProjectInput] = []
    for obj in candidates:
        if not is_associated_project(obj, problem):
            raise ValueError(f"Project {obj.name!r} is not linked to SelectionProblem")
        identifier = object_attribute(obj, "id")
        cost = object_attribute(obj, "cost")
        benefit = object_attribute(obj, "benefit")
        if not isinstance(identifier, str) or not identifier:
            raise ValueError("Project.id must be a non-empty string")
        if type(cost) is not int or cost < 0:
            raise ValueError(f"Project {identifier!r} has an invalid cost")
        if type(benefit) is not int or benefit < 0:
            raise ValueError(f"Project {identifier!r} has an invalid benefit")
        projects.append(ProjectInput(identifier, cost, benefit))

    projects.sort(key=lambda p: p.identifier)
    if not projects:
        raise ValueError("A SelectionProblem must contain at least one ProjectClass")
    if len({p.identifier for p in projects}) != len(projects):
        raise ValueError("Projects must have unique ids")
    return ProblemInput(budget=budget, projects=tuple(projects))


def slack_weights(budget: int, encoding: str = "bounded") -> tuple[int, ...]:
    """Binary encode unused budget s >= 0 (and up to budget for 'bounded').

    With the bounded encoding, B=26 -> (1, 2, 4, 8, 11), as in the supplied
    handwritten example's linear coefficients. With standard binary:
    B=26 -> (1, 2, 4, 8, 16). Both cover every s in [0, B].
    """
    if budget < 0:
        raise ValueError("budget must be non-negative")
    if encoding not in {"bounded", "binary"}:
        raise ValueError(f"Unknown slack encoding: {encoding}")
    if budget == 0:
        return ()
    if encoding == "binary":
        return tuple(1 << k for k in range(budget.bit_length()))
    # Minimum number of bits. The first m-1 are ordinary binary weights;
    # the final weight fills the remaining capacity. For B=269, this is
    # [1,2,4,8,16,32,64,128,14] (all values 0..269 are representable).
    bit_count = budget.bit_length()
    weights = [1 << k for k in range(bit_count - 1)]
    weights.append(budget - sum(weights))
    return tuple(weights)


def transform(problem: ProblemInput, encoding: str = "bounded") -> Qubo:
    """Expand the knapsack-to-QUBO formula into factorized coefficients"""
    weights = slack_weights(problem.budget, encoding)
    penalty = 1 + sum(p.benefit for p in problem.projects)
    names = tuple(f"x_{p.identifier}" for p in problem.projects) + tuple(
        f"s_{k}" for k in range(1, len(weights) + 1)
    )
    costs = tuple(p.cost for p in problem.projects) + weights
    benefits = tuple(p.benefit for p in problem.projects) + (0,) * len(weights)
    B = problem.budget
    linear = {
        i: penalty * (a * a - 2 * B * a) - benefits[i]
        for i, a in enumerate(costs)
        if penalty * (a * a - 2 * B * a) - benefits[i] != 0
    }
    quadratic = {
        (i, j): 2 * penalty * costs[i] * costs[j]
        for i, j in combinations(range(len(costs)), 2)
        if costs[i] and costs[j]
    }
    return Qubo(names=names, slack_weights=weights, penalty=penalty,
                constant=penalty * B * B, linear=linear, quadratic=quadratic)


def generate_python(qubo: Qubo, metamodel_file: Path, source_file: Path) -> str:
    """Write BESSER objects using exactly the classes/associations in Solution DSL."""
    text = metamodel_file.read_text(encoding="utf-8")
    marker = "# PROJECT DEFINITION #"
    if marker not in text:
        raise ValueError(f"Could not identify structural model in {metamodel_file}")
    # Keep the class diagram source intact, stopping before its Project wrapper.
    structural = text[:text.rfind("######################", 0, text.index(marker))].rstrip()
    lines = [
        "# Generated by T1: Problem ObjectModel -> QUBO Solution ObjectModel",
        f"# Source problem file: {source_file.name}",
        "# References: Lucas (2014), Ising formulations of many NP problems;",
        "#             Glover, Kochenberger and Du (2019), Quantum Bridge Analytics I.",
        f"# Automatically calculated penalty: {qubo.penalty}",
        f"# Slack variable weights: {list(qubo.slack_weights)}",
        "# This file is a BESSER object model, NOT a quantum circuit or a solved selection.",
        "",
        structural,
        "",
        "################",
        "# OBJECT MODEL #",
        "################",
        "",
        "from besser.BUML.metamodel.object import ObjectModel",
        "",
        "# --- Concrete QUBO Object Model ---",
        f"qubomodel_1_obj = QuboModel('quboModel_1').attributes(constant={qubo.constant}).build()",
        "",
        "# Binary decision variables followed by slack variables",
    ]
    object_vars: list[str] = ["qubomodel_1_obj"]
    binary_vars = []
    for i, name in enumerate(qubo.names):
        variable = f"binaryvariable_{i}_obj"
        binary_vars.append(variable)
        object_vars.append(variable)
        lines.append(f"{variable} = BinaryVariable({('binaryVariable_' + str(i))!r}).attributes(name={name!r}).build()")

    lines += ["", "# Linear terms: coefficients have already been factorized"]
    for i, coeff in sorted(qubo.linear.items()):
        variable = f"linearterm_{i}_obj"
        object_vars.append(variable)
        lines.append(f"{variable} = LinearTerm({('linearTerm_' + str(i))!r}).attributes(coefficient={coeff}).build()")
        lines.append(f"{variable}.linearVariable = {binary_vars[i]}")
        lines.append(f"{variable}.qubomodel_lt = qubomodel_1_obj")

    lines += ["", "# Quadratic terms: one unique term per unordered pair"]
    for (i, j), coeff in sorted(qubo.quadratic.items()):
        variable = f"quadraticterm_{i}_{j}_obj"
        object_vars.append(variable)
        lines.append(f"{variable} = QuadraticTerm({('quadraticTerm_' + str(i) + '_' + str(j))!r}).attributes(coefficient={coeff}).build()")
        lines.append(f"{variable}.variables = {{{binary_vars[i]}, {binary_vars[j]}}}")
        lines.append(f"{variable}.qubomodel_qt = qubomodel_1_obj")

    lines += [
        "",
        "# All binary variables belong to the QUBO object",
        "qubomodel_1_obj.binaryVariables = {" + ", ".join(binary_vars) + "}",
        "",
        "object_model: ObjectModel = ObjectModel(",
        "    name='T1_Generated_QUBO',",
        "    objects={" + ", ".join(object_vars) + "}",
        ")",
        "",
        "######################",
        "# PROJECT DEFINITION #",
        "######################",
        "",
        "from besser.BUML.metamodel.project import Project",
        "",
        "# Reusable BESSER Project with both the class and object models",
        "project = Project(",
        "    name='Solution_DSL',",
        "    models=[domain_model, object_model],",
        "    owner='TACS Group 4',",
        "    metadata=Metadata(description='QUBO solution model generated by T1')",
        ")",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("problem_file", nargs="?", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--solution-metamodel", type=Path, default=DEFAULT_METAMODEL)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--slack-encoding", choices=("bounded", "binary"), default="bounded")
    args = parser.parse_args()

    problem_file = args.problem_file.resolve()
    model_file = args.solution_metamodel.resolve()
    problem = load_problem(problem_file)
    qubo = transform(problem, encoding=args.slack_encoding)

    generated = generate_python(qubo, model_file, problem_file)
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"t1-result-{datetime.now().strftime('%Y%m%d-%H%M%S-%f')}.py"
    output_file.write_text(generated, encoding="utf-8")

    print(f"Input: {problem_file}")
    print(f"Projects: {len(problem.projects)} | Budget: {problem.budget}")
    print(f"QUBO: {len(qubo.names)} variables, {len(qubo.linear)} linear terms, "
          f"{len(qubo.quadratic)} quadratic terms")
    print(f"Penalty: {qubo.penalty} | Slack weights: {list(qubo.slack_weights)}")
    print(f"Generated: {output_file}")


if __name__ == "__main__":
    main()
