# Test Cases

> The following test cases are based on published 0/1 Knapsack benchmark instances. In the context of the porfolio or project selection problem, each item is interpreted as project and their weight and value as cost and benefit respectively.

## 1: Small Instance

- Source(s): [KNAPSACK_01 Data for the 01 Knapsack Problem (P02) (John Burkardt)](https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html)
- Number of projects: 5
- Available budget: 26

| Project | Cost | Benefit |
|-|-|-|
| 1 | 12 | 24 |
| 2 | 7 | 13 |
| 3 | 11 | 23 |
| 4 | 8 | 15 |
| 5 | 9 | 16 |

Optimal solution: [2, 3, 4]
Total cost: 26
Total benefit: 51

## 2: Medium Instance

- Source(s): [KNAPSACK_01 Data for the 01 Knapsack Problem (P04) (John Burkardt)](https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html)
- Number of projects: 7
- Available budget: 50

| Project | Cost | Benefit |
|-|-|-|
| 1 | 31 | 70 |
| 2 | 10 | 20 |
| 3 | 20 | 39 |
| 4 | 19 | 37 |
| 5 | 4 | 7 |
| 6 | 3 | 5 |
| 7 | 6 | 10 |

Optimal solution: [1, 4]
Total cost: 50
Total benefit: 107

## 3: Large Instance

- Source(s): [Hands-on Optimization with OR-Tools in Python Chapter 8: The Knapsack Problem](https://kunlei.github.io/python-ortools-notes/ip-knapsack.html), [Knapsack_problem_0-1](https://github.com/Lolik-Bolik/Knapsack_problem_0-1)
- Number of projects: 10
- Available budget: 269

| Project | Cost | Benefit |
|-|-|-|
| 1 | 55 | 95 |
| 2 | 10 | 4 |
| 3 | 47 | 60 |
| 4 | 5 | 32 |
| 5 | 4 | 23 |
| 6 | 50 | 72 |
| 7 | 8 | 80 |
| 8 | 61 | 62 |
| 9 | 85 | 65 |
| 10 | 87 | 46 |

Optimal solution: [2, 3, 4, 8, 9, 10]
Total cost: 269
Total benefit: 295