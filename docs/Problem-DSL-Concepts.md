# Problem DSL Concepts

## Purpose

This Domain Specific Language will allow users to model portfolio selection problems by specifying a set of available projects, their costs, their benefits and a maximum budget that can be spent in the selection.



## Content (Concept List)

| Concept | Intrinsic Properties | Extrinsic Properties |
|-|-|-|
| SelectionProblem | budget: Integer | Contains at least one project and zero or more SelectionResults |
| Project | id: String; cost: Integer; benefit: Integer | Belongs to one Selection Problem and is a candidate to its solution |
| SelectionResult | totalCost: Integer; totalBenefit: Integer | Belongs to one SelectionProblem and references zero or more Projects |

- SelectionProblem: the project selection problem (0/1 Knapsack) defined by a list of available projects and a budget
- Project: a candidate project, identified by its id and containing a cost and a benefit.
- SelectionResult: a feasible selection of Projects that solve a specific SelectionProblem and includes its total cost and benefit.

