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

> This Object Diagram was exported to B-UML Python code: [problem_DSL_class_diagram.py](./code/problem_DSL_object_diagram.py)
