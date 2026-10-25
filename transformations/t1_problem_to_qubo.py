"""
References for rules:
    - Part I README: Project Selection / 0-1 Knapsack QUBO formulation.
    - TACS assignment, Annex A, class A: QUBO and quadratic penalties.
    - Glover, Kochenberger & Du (2019), QUBO formulations (assignment ref).
"""

import sys
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path

from besser.BUML.metamodel.object import ObjectModel

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "code"))

from problem_DSL_object_diagram import object_model as problem_model
from solution_DSL_class_diagram import (
    QuboModel, BinaryVariable, LinearTerm, QuadraticTerm,
)


@dataclass(frozen=True)
class QuboConfig:
    # None = automatically compute a conservative penalty from the input model.
    # A supplied penalty must be a positive integer; smaller values may fail
    # to enforce the budget constraint.
    penalty: int | None = None


def objects_of_type(model, class_name):
    """Identify BESSER objects by their classifier (not their Python type)."""
    return sorted(
        (obj for obj in model.objects if obj.classifier.name == class_name),
        key=lambda obj: obj.name_,
    )


def linked_objects(obj, end_name):
    """Navigate BESSER associations without depending on the editor's end names."""
    return sorted(
        {end.object for end in obj.link_ends()
         if end.association_end.name == end_name},
        key=lambda target: target.name_,
    )


def rule_t1_1_create_qubo():
    """SelectionProblem -> QuboModel; constant filled by T1.6."""
    return QuboModel("qubo_1").attributes(constant=0).build()


def rule_t1_2_project_variables(projects):
    """Each ProjectClass -> one BinaryVariable (x_projectId)."""
    variables = []
    trace = {}
    for index, project in enumerate(projects, start=1):
        name = f"x_{project.id}"
        var = BinaryVariable(f"decision_{index}").attributes(name=name).build()
        variables.append(var)
        trace[name] = project.id
    return variables, trace


def rule_t1_3_slack_variables(budget):
    """Represent unused budget by powers-of-two slack bits."""
    variables = []
    weights = {}
    for index in range(budget.bit_length()):
        name = f"s_{index + 1}"
        var = BinaryVariable(f"slack_{index + 1}").attributes(name=name).build()
        variables.append(var)
        weights[name] = 2 ** index
    return variables, weights


def choose_penalty(projects, config):
    """For non-negative integer benefits, sum(benefits)+1 is a safe bound.

    Any infeasible binary selection has an integer constraint violation of
    magnitude >= 1, costing at least penalty, more than all possible benefits.
    A feasible selection (e.g. the empty selection) can attain penalty zero.
    """
    if config.penalty is None:
        return 1 + sum(project.benefit for project in projects)
    if type(config.penalty) is not int or config.penalty <= 0:
        raise ValueError("The configured QUBO penalty must be a positive integer")
    return config.penalty


def rule_t1_4_linear_terms(variables, weights, benefits, budget, penalty):
    """Expand -benefit*x + penalty*(sum(weights*x)-budget)^2.

    Reference: assignment Annex A, class A; Glover et al. (2019).
    x^2 = x for binary variables, so a_i = -benefit_i + penalty*(w_i^2-2*B*w_i).
    """
    terms = []
    for variable in variables:
        w = weights[variable.name]
        coefficient = -benefits.get(variable.name, 0) + penalty * (w*w - 2*budget*w)
        if coefficient == 0:  # Metamodel's nonzero-coefficient constraint.
            continue
        term = LinearTerm(f"linear_{variable.name}").attributes(
            coefficient=coefficient,
        ).build()
        term.linearVariable = variable
        terms.append(term)
    return terms


def rule_t1_5_quadratic_terms(variables, weights, penalty):
    """For i<j, b_ij = 2*penalty*w_i*w_j (symmetric pairs counted once).

    Reference: assignment Annex A, class A; Glover et al. (2019).
    """
    terms = []
    for left, right in combinations(variables, 2):
        coefficient = 2 * penalty * weights[left.name] * weights[right.name]
        if coefficient == 0:
            continue
        term = QuadraticTerm(f"quadratic_{left.name}_{right.name}").attributes(
            coefficient=coefficient,
        ).build()
        term.variables = {left, right}
        terms.append(term)
    return terms


def rule_t1_6_constant(qubo, budget, penalty):
    """Constant c = penalty*budget^2 from the squared budget constraint.

    Reference: assignment Annex A, class A; Glover et al. (2019).
    """
    qubo.constant = penalty * budget * budget


def transform(source, config=None):
    """Transform a BESSER problem ObjectModel into a QUBO ObjectModel.

    Returns: (target_model, trace variableName->projectId, slack_weights).
    """
    if config is None:
        config = QuboConfig()

    problems = objects_of_type(source, "SelectionProblem")
    if len(problems) != 1:
        raise ValueError("Expected exactly one SelectionProblem")
    problem = problems[0]

    projects = sorted(linked_objects(problem, "projects"), key=lambda p: p.id)
    if not projects:
        raise ValueError("At least one project is required")
    budget = problem.budget
    if type(budget) is not int or budget < 0:
        raise ValueError("Budget must be a non-negative integer")
    ids = [project.id for project in projects]
    if len(set(ids)) != len(ids):
        raise ValueError("Project IDs must be unique")
    for project in projects:
        if any(type(v) is not int or v < 0 for v in (project.cost, project.benefit)):
            raise ValueError("Costs and benefits must be non-negative integers")

    penalty = choose_penalty(projects, config)
    qubo = rule_t1_1_create_qubo()
    project_vars, trace = rule_t1_2_project_variables(projects)
    slack_vars, slack_weights = rule_t1_3_slack_variables(budget)
    variables = project_vars + slack_vars

    weights = {f"x_{p.id}": p.cost for p in projects}
    weights.update(slack_weights)
    benefits = {f"x_{p.id}": p.benefit for p in projects}

    linear_terms = rule_t1_4_linear_terms(
        variables, weights, benefits, budget, penalty,
    )
    quadratic_terms = rule_t1_5_quadratic_terms(variables, weights, penalty)
    rule_t1_6_constant(qubo, budget, penalty)

    # BESSER associations, as defined in solution_DSL_class_diagram.py.
    qubo.binaryVariables = set(variables)
    qubo.linearTerms = set(linear_terms)
    qubo.quadraticTerms = set(quadratic_terms)
    target = ObjectModel(
        name="Generated_QUBO",
        objects={qubo, *variables, *linear_terms, *quadratic_terms},
    )
    return target, trace, slack_weights


def qubo_energy(target, assignment):
    """Read the generated BESSER model to calculate f(assignment)."""
    qubo = objects_of_type(target, "QuboModel")[0]
    energy = qubo.constant
    for term in objects_of_type(target, "LinearTerm"):
        var, = linked_objects(term, "linearVariable")
        energy += term.coefficient * assignment[var.name]
    for term in objects_of_type(target, "QuadraticTerm"):
        first, second = linked_objects(term, "variables")
        energy += term.coefficient * assignment[first.name] * assignment[second.name]
    return energy


def check_small_instance(target, trace, slack_weights, source):
    """Independent exhaustive check for the Part I five-project example."""
    problem = objects_of_type(source, "SelectionProblem")[0]
    projects = {p.id: p for p in linked_objects(problem, "projects")}
    names = [v.name for v in objects_of_type(target, "BinaryVariable")]
    assert len(names) == 10
    assert len(objects_of_type(target, "LinearTerm")) == 10
    assert len(objects_of_type(target, "QuadraticTerm")) == 45

    penalty = 1 + sum(p.benefit for p in projects.values())
    best_energy = None
    best_assignment = None
    for bits in product((0, 1), repeat=len(names)):
        assignment = dict(zip(names, bits))
        total_cost = sum(projects[project_id].cost * assignment[name]
                         for name, project_id in trace.items())
        total_benefit = sum(projects[project_id].benefit * assignment[name]
                            for name, project_id in trace.items())
        unused_budget = sum(weight * assignment[name]
                            for name, weight in slack_weights.items())
        expected = -total_benefit + penalty * (total_cost + unused_budget - problem.budget)**2
        actual = qubo_energy(target, assignment)
        assert actual == expected, (assignment, actual, expected)
        if best_energy is None or actual < best_energy:
            best_energy = actual
            best_assignment = assignment

    selected = sorted(project_id for name, project_id in trace.items()
                      if best_assignment[name] == 1)
    assert selected == ["B", "C", "D"]
    assert best_energy == -51
    print("OK: all 1024 QUBO assignments match the mathematical formula")
    print("Best selection:", selected)
    print("Minimum QUBO energy:", best_energy)


if __name__ == "__main__":
    target, trace, slack_weights = transform(problem_model)
    qubo = objects_of_type(target, "QuboModel")[0]
    print("Generated QUBO:")
    print("  Variables:", len(objects_of_type(target, "BinaryVariable")))
    print("  Linear terms:", len(objects_of_type(target, "LinearTerm")))
    print("  Quadratic terms:", len(objects_of_type(target, "QuadraticTerm")))
    print("  Constant:", qubo.constant)
    print("  Project trace:", trace)
    print("  Slack weights:", slack_weights)
    check_small_instance(target, trace, slack_weights, problem_model)
