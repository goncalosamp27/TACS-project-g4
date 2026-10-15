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

