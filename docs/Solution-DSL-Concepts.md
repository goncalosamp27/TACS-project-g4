# Problem DSL Concepts

## Purpose

This Domain Specific Language will convert the Problem-DSL into a model of a mathematic optimisation problem without constraints representing a cost function with binary variables, linear coefficients (projects costs) and quadratic coefficients (budget constraints). 

## Realization

> To be defined 

## Content (Concept List)

| Concept | Intrinsic Properties | Extrinsic Properties |
|-|-|-|
| QuboModel | constant: Integer | Contains the BinaryVariables, LinearTerms, QuadraticTerms |
| BinaryVariable | name: String; | Belongs to one QuboModel |
| LinearTerm | coefficient: Integer | Belongs to one BinaryVariable |
| QuadraticTerm | coefficient: Integer | Belongs to two BinaryVariable |

## Domain Rules

- R1: In the same QuboModel, each BinaryVariable must have an unique name
- R2:  

- R1: The budget of the problem must be a non-negative integer
- R2: Each project's cost must be a non-negative integer
- R3: Each project's benefit must be a non-negative integer
- R4: In the same SelectionProblem, each Project must have an unique id
- R5: A SelectionProblem must have at least one candidate project
- R6: All Projects referenced by a SelectionResult must belong to the same SelectionProblem the SelectionResult belongs to
- R7: The sum of the benefits of the Projects that belong in a SelectionResult must equal its totalBenefit
- R8: The sum of the costs of the Projects that belong in a SelectionResult must equal its totalCost
- R9: The total cost of a SelectionResult must not exceed the SelecionProblem's budget