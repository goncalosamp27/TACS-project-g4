# TACS Project Group 4
## Project Selection Problem (0/1 Knapsack)
The **0/1 Knapsack problem** consists of **selecting a subset of items** out of a given list inside a **knapsack with a fixed maximum weight**, so that the subset **maximizes the total value without exceeding the capacity** of the bag. Each item has a **fixed weight and value**, can only be **selected once** and **cannot be divided into a fraction** (e.g. selecting half an item is not allowed).

In the context of **Project Selection**, the 0/1 Knapsack problem can be applied to selecting a subset of projects under a limited budget (the knapsack's maximum capacity), where each project has a cost (weight) and a benefit (value). The goal is to maximize the total benefit of the selection without exceeding the available budget.

## Problem DSL
A **Domain Specific Language** was designed to allow users to model portfolio selection problems by specifying a set of available projects, their costs and benefits and a maximum budget that can be spent in the selection. The DSL was developed using **BESSER** where a UML Class Diagram was created to define its concepts, attributes, constraints and relationships. 

| Concept | Intrinsic Properties | Extrinsic Properties |
|-|-|-|
| SelectionProblem | budget: Integer | Contains at least one project and zero or more SelectionResults |
| Project | id: String; cost: Integer; benefit: Integer | Belongs to one Selection Problem and is a candidate to its solution |
| SelectionResult | totalCost: Integer; totalBenefit: Integer | Belongs to one SelectionProblem and references zero or more Projects |
*Table 1: Problem DSL Concept List*

![Problem DSL Class Diagram](diagrams/problemDSLclass.png)
*Figure 1: Problem DSL Class Diagram*

- **SelectionProblem** represents the project selection problem (0/1 Knapsack) defined by a list of available projects and a budget, grouping all candidate projects and defining the budget that can be spent.
- **Project** represents a candidate project, identified by an unique id and containing a cost and a benefit that represent, respectively, the weight and value of an item in the original problem.
- **SelectionResult** represents a feasible selection of Projects for a specific SelectionProblem and includes its total cost and benefit and was created to separate the problem definition from its possible results, allowing the Problem to exist with 0 or more feasible selections. 

> The Class Diagram was exported to B-UML Python code: [problem_DSL_class_diagram.py](./code/problem_DSL_class_diagram.py)

### Domain Rules
Several domain rules were introduced to ensure the consistency and validity of the problem instances and OCL constraints were used to enforce conditions that cannot be fully expressed through the metamodel's attributes and associations:
- R1: The budget of the problem must be a non-negative integer
- R2: Each project's cost must be a non-negative integer
- R3: Each project's benefit must be a non-negative integer
- R4: In the same SelectionProblem, each Project must have an unique id
- R5: A SelectionProblem must have at least one candidate project
- R6: All Projects referenced by a SelectionResult must belong to the same SelectionProblem the SelectionResult belongs to
- R7: The sum of the benefits of the Projects that belong in a SelectionResult must equal its totalBenefit
- R8: The sum of the costs of the Projects that belong in a SelectionResult must equal its totalCost
- R9: The total cost of a SelectionResult must not exceed the SelecionProblem's budget

### Example Object Model
Three test cases were selected to demonstrate the application of the DSL, as documented in [Test-Cases.md](./docs/Test-Cases.md). The first test case was used to create an Object Diagram in BESSER that represents a problem with five candidate projects and a budget of 26 where each project is represented as an instance of the Project class, associated to a single SelectionProblem instance:

![Problem DSL Object Diagram](diagrams/problemDSLobject.png)
*Figure 2: Problem DSL Object Diagram for Test Case 1.*

> This Object Diagram was exported to B-UML Python code: [problem_DSL_object_diagram.py](./code/problem_DSL_object_diagram.py)


## Solution DSL Design
A Domain Specific Language was designed to implement the mathematical optimisaition equation. It represents a cost function thanks to binary variables, linear and quadratic coefficients. The DSL was developed using **BESSER** where a UML Class Diagram was created to define its concepts, attributes and relationships. 

| Concept | Intrinsic Properties | Extrinsic Properties |
|-|-|-|
| QuboModel | constant: Integer | Contains the BinaryVariables, LinearTerms, QuadraticTerms |
| BinaryVariable | name: String; | Belongs to one QuboModel |
| LinearTerm | coefficient: Integer | Belongs to one BinaryVariable |
| QuadraticTerm | coefficient: Integer | Belongs to two BinaryVariable |

![Solution DSL Class Diagram](diagrams/solutionDSLclass.png)
*Figure 3: Solution DSL Class Diagram*

- **QuboModel** represents a Quadratic Unconstrained Binary Optimization formulation, defined by the value of the constant. It groups all decision variables, linear and quadratic terms which create the cost equation. 
- **BinaryVariable** represents a binary decision variables (0/1). Identified by a name and representing either a project selection variable or a slack variable used to uncode constraints (maximum size of the knapsack). 
- **LinearTerm** represents first order terms in the polynomial equation. Defined by an integer coefficient associated with a single BinaryVariable to model the contribution of this specific project to the result. 
- **QuadraticTerm** represents second order terms in the polynomial equation. Defined by an integer coefficient associated with two BinaryVariable to model the constraint of maximum weight.

### Domain Rules
Several domain rules were introduced to ensure the consistency and validity of the solution instances and OCL constraints were used to enforce conditions that cannot be fully expressed through the metamodel's attributes and associations:
- R1: Each BinaryVariables must habe a unique name 
- R2: Each LinearTerm must be different than 0
- R3: Each QuadraticTerm must be different than 0
- R4: Each QuadraticTerm must be associated with two different BinaryVariable
- R5: Each BinaryVariable must be associated with a unique LinearTerm
- R6: Each pair of BinaryVariable must be associated with a unique QuadraticTerm
- R7: LinearTerm must be factorized as much as possible 
- R8: QuadraticTerm must be factorized as much as possible

## LLM usage log
| Goal | Tool | Validation |
|-|-|-|
| corrections in OCL syntax | gemini | Quality Check of the class diagram in Besser |
| creating the solution object code based on the solution class code. Create the object by hand in the GUI of besser would have been difficult because of the high number of links between objects | gemini | manually step throught the code to look at the object instance and links + Quality Check of the object diagram in Besser |

