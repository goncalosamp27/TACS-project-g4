# Problem DSL Concepts

## Purpose

This Domain Specific Language will allow users to model portfolio selection problems by specifying a set of available projects, their costs, their benefits and a maximum budget that can be spent in the selection.

## Realization

> To be defined 

## Content (Concept List)

| Concept | Intrinsic Properties | Extrinsic Properties |
|-|-|-|
| SelectionProblem | budget: Integer | Contains at least one project and zero or more SelectionResults |
| Project | id: String; cost: Integer; benefit: Integer | Belongs to one Selection Problem and is a candidate to its solution |
| SelectionResult | totalCost: Integer; totalBenefit: Integer | Belongs to one SelectionProblem and references zero or more Projects |

- SelectionProblem: the project selection problem (0/1 Knapsack) defined by a list of available projects and a budget
- Project: a candidate project, identified by its id and containing a cost and a benefit.
- SelectionResult: a feasible selection of Projects that solve a specific SelectionProblem and includes its total cost and benefit.

## Domain Rules

- R1: The budget of the problem must be a non-negative integer
- R2: Each project's cost must be a non-negative integer
- R3: Each project's benefit must be a non-negative integer
- R4: In the same SelectionProblem, each Project must have an unique id
- R5: A SelectionProblem must have at least one candidate project
- R6: All Projects referenced by a SelectionResult must belong to the same SelectionProblem the SelectionResult belongs to
- R7: The sum of the benefits of the Projects that belong in a SelectionResult must equal its totalBenefit
- R8: The sum of the costs of the Projects that belong in a SelectionResult must equal its totalCost
- R9: The total cost of a SelectionResult must not exceed the SelecionProblem's budget