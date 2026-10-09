# 0/1 Knapsack 

This problem consists of selecting a subset of items out of a given list inside a knapsack with a fixed maximum weight, so that the subset maximizes the total value without exceeding the capacity of the bag. 

Each item has a fixed weight and value. In this version of the problem, we can not divide items into fractions (for example: we are not allowed to select half an item) and each item must only be selected once (therefore each item can be selected (1) or not (0)).

List of inputs:
- set of items
- each item's value
- each item's weight
- maximum sack capacity

Objective:
- maximize the sum of the value of the selected items

Constraints:
- the total weight of the selected items must not exceed the knapsack's maximum capacity
- each item can only be selected once
- items can not be devided into fractions

Output:
- final subset of selected items
- total weight of the selected items
- total value of the selected items

# Application to Problem A4

The 0/1 Knapsack problem can also represent portfolio or project selection under a limited budget.

In this context:
- Each item represents a project
- Each item's weight represents the project's cost
- Each item's value represents the project's benefit
- The knapsack's maximum capacity represents the available budget

We want to select the subset of projects that maximize the benefit while keeping the total cost of the projects lower than the available budget.