"""Run the SAME T1 transformation against all three BESSER problem models.

From the project root (with your virtual environment activated):
    python tests/test_t1_instances.py

No pytest dependency is required.
"""

import sys
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from instances.problem_instances import INSTANCE_DATA, build_problem_model
from transformations.t1_problem_to_qubo import (
    transform,
    objects_of_type,
    linked_objects,
    qubo_energy,
)


# Verified by independent exhaustive search over PROJECT selections.
# Note: docs/Test-Cases.md currently has an incorrect large-instance optimum.
EXPECTED = {
    "small":  (("B", "C", "D"), 26, 51, 18),
    "medium": (("A", "D"), 50, 107, 71),
    "large":  (("A", "B", "C", "D", "E", "F", "G", "I"), 264, 431, 799),
}


def all_project_subsets(projects):
    """Brute-force classical baseline: all subsets of domain projects."""
    for size in range(len(projects) + 1):
        yield from combinations(projects, size)


def best_classical_selection(projects, budget):
    """Maximize benefit, breaking benefit ties by choosing lower cost."""
    best = None
    feasible_count = 0
    for subset in all_project_subsets(projects):
        cost = sum(p.cost for p in subset)
        if cost > budget:
            continue
        feasible_count += 1
        benefit = sum(p.benefit for p in subset)
        selected = tuple(sorted(p.id for p in subset))
        candidate = (benefit, -cost, selected)
        if best is None or candidate[:2] > best[:2]:
            best = candidate
    assert best is not None
    benefit, negative_cost, selected = best
    return selected, -negative_cost, benefit, feasible_count


def test_instance(name):
    # INPUT: a real BESSER ObjectModel conforming to your Problem DSL.
    source = build_problem_model(name)
    source_problem, = objects_of_type(source, "SelectionProblem")
    projects = sorted(linked_objects(source_problem, "projects"), key=lambda p: p.id)
    budget = source_problem.budget

    assert [(p.id, p.cost, p.benefit) for p in projects] == INSTANCE_DATA[name]["projects"]
    assert budget == INSTANCE_DATA[name]["budget"]

    # M2M T1: same function, without any changes or hard-coded cases.
    target, trace, slack_weights = transform(source)
    qubo, = objects_of_type(target, "QuboModel")
    vars_ = objects_of_type(target, "BinaryVariable")
    linear = objects_of_type(target, "LinearTerm")
    quadratic = objects_of_type(target, "QuadraticTerm")
    count = len(projects) + budget.bit_length()
    penalty = 1 + sum(project.benefit for project in projects)

    assert len(vars_) == count
    assert len(linear) == count
    assert len(quadratic) == count * (count - 1) // 2
    assert qubo.constant == penalty * budget * budget
    assert len(linked_objects(qubo, "binaryVariables")) == count
    assert len(trace) == len(projects)
    assert len(slack_weights) == budget.bit_length()

    # Check the generated model's coefficients against the independently
    # expanded QUBO formula (not just the output of a solver).
    variable_weights = {f"x_{p.id}": p.cost for p in projects}
    variable_weights.update(slack_weights)
    variable_benefits = {f"x_{p.id}": p.benefit for p in projects}

    for term in linear:
        var, = linked_objects(term, "linearVariable")
        w = variable_weights[var.name]
        expected_coefficient = (
            -variable_benefits.get(var.name, 0)
            + penalty * (w * w - 2 * budget * w)
        )
        assert term.coefficient == expected_coefficient, (name, var.name)
    for term in quadratic:
        left, right = linked_objects(term, "variables")
        expected_coefficient = (
            2 * penalty * variable_weights[left.name] * variable_weights[right.name]
        )
        assert term.coefficient == expected_coefficient, (name, left.name, right.name)

    # Independent classical optimum, computed from the projects (5/7/10 bits),
    # not from the QUBO solver or any hand-written best selection.
    classical = best_classical_selection(projects, budget)
    assert classical == EXPECTED[name], (name, classical, EXPECTED[name])
    selected_ids, best_cost, best_benefit, feasible_count = classical

    # Test QUBO energy for EVERY subset of projects. Each is completed with
    # the optimal non-negative slack encoding. This avoids an unnecessary
    # 2^19 full enumeration of the large instance's slack assignments.
    minimum_energy = None
    minimum_selected = None
    for subset in all_project_subsets(projects):
        cost = sum(p.cost for p in subset)
        benefit = sum(p.benefit for p in subset)
        slack = max(0, budget - cost)
        chosen_ids = {p.id for p in subset}
        assignment = {f"x_{p.id}": int(p.id in chosen_ids) for p in projects}
        for bit_index, slack_name in enumerate(slack_weights):
            assignment[slack_name] = (slack >> bit_index) & 1
        actual = qubo_energy(target, assignment)
        expected_energy = -benefit + penalty * (cost + slack - budget) ** 2
        assert actual == expected_energy, (name, chosen_ids, actual, expected_energy)
        if minimum_energy is None or actual < minimum_energy:
            minimum_energy = actual
            minimum_selected = tuple(sorted(chosen_ids))

    assert minimum_energy == -best_benefit
    assert minimum_selected == selected_ids
    print(
        f"{name.upper():6} OK | projects={len(projects):2} budget={budget:3} "
        f"qubits={count:2} linear={len(linear):2} quadratic={len(quadratic):3} "
        f"feasible={feasible_count:3} | best={','.join(selected_ids)} "
        f"cost={best_cost} benefit={best_benefit}"
    )


if __name__ == "__main__":
    for instance_name in ("small", "medium", "large"):
        test_instance(instance_name)
    print("SUCCESS: T1 validated against all three Part I test instances.")
