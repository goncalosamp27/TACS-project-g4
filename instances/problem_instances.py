"""Three TACS Project Selection problem instances, as BESSER ObjectModels.

The small instance is the original Part I object model.
The medium and large instances use exactly the same Problem DSL metamodel.
Data source: project/docs/Test-Cases.md (Part I submission).
"""

import sys
from pathlib import Path

from besser.BUML.metamodel.object import ObjectModel

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

# Use the actual metamodel classes, not a parallel Python data structure.
from problem_DSL_class_diagram import ProjectClass, SelectionProblem
from problem_DSL_object_diagram import object_model as small_object_model


# Each tuple is (project ID, cost, benefit), copied from docs/Test-Cases.md.
INSTANCE_DATA = {
    "small": {
        "budget": 26,
        "projects": [
            ("A", 12, 24),
            ("B", 7, 13),
            ("C", 11, 23),
            ("D", 8, 15),
            ("E", 9, 16),
        ],
    },
    "medium": {
        "budget": 50,
        "projects": [
            ("A", 31, 70),
            ("B", 10, 20),
            ("C", 20, 39),
            ("D", 19, 37),
            ("E", 4, 7),
            ("F", 3, 5),
            ("G", 6, 10),
        ],
    },
    "large": {
        "budget": 269,
        "projects": [
            ("A", 55, 95),
            ("B", 10, 4),
            ("C", 47, 60),
            ("D", 5, 32),
            ("E", 4, 23),
            ("F", 50, 72),
            ("G", 8, 80),
            ("H", 61, 62),
            ("I", 85, 65),
            ("J", 87, 46),
        ],
    },
}


def build_problem_model(instance_name):
    """Return a fresh BESSER ObjectModel for the named instance.

    Important: a selection problem model is not itself a solution.
    SelectionResult objects will be generated after solving/decoding.
    """
    if instance_name not in INSTANCE_DATA:
        raise ValueError(f"Unknown instance {instance_name!r}; choose small, medium or large")

    if instance_name == "small":
        # Reuse the hand-built object model submitted in Part I.
        return small_object_model

    data = INSTANCE_DATA[instance_name]
    problem = SelectionProblem(f"problem_{instance_name}").attributes(
        budget=data["budget"]
    ).build()

    projects = []
    for project_id, cost, benefit in data["projects"]:
        project = ProjectClass(f"project_{instance_name}_{project_id}").attributes(
            id=project_id, cost=cost, benefit=benefit
        ).build()
        # Same association used by the Part I BESSER object-model export.
        project.selectionproblem = problem
        projects.append(project)

    return ObjectModel(
        name=f"SelectionProblem_{instance_name}",
        objects={problem, *projects},
    )
