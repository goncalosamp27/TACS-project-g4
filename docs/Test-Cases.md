# Test Cases

> The following test cases are based on published 0/1 Knapsack benchmark instances. In the context of the portfolio or project selection problem, each item is interpreted as project and their weight and value as cost and benefit respectively.

## 1: Small Instance

- Source(s): [KNAPSACK_01 Data for the 01 Knapsack Problem (P02) (John Burkardt)](https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html)
- Number of projects: 5
- Available budget: 26

| Project | Cost | Benefit |
|-|-|-|
| A | 12 | 24 |
| B | 7 | 13 |
| C | 11 | 23 |
| D | 8 | 15 |
| E | 9 | 16 |

Optimal solution: [B, C, D]
Total cost: 26
Total benefit: 51

## 2: Medium Instance

- Source(s): [KNAPSACK_01 Data for the 01 Knapsack Problem (P04) (John Burkardt)](https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html)
- Number of projects: 7
- Available budget: 50

| Project | Cost | Benefit |
|-|-|-|
| A | 31 | 70 |
| B | 10 | 20 |
| C | 20 | 39 |
| D | 19 | 37 |
| E | 4 | 7 |
| F | 3 | 5 |
| G | 6 | 10 |

Optimal solution: [A, D]
Total cost: 50
Total benefit: 107

## 3: Large Instance

- Source(s): [Hands-on Optimization with OR-Tools in Python Chapter 8: The Knapsack Problem](https://kunlei.github.io/python-ortools-notes/ip-knapsack.html), [Knapsack_problem_0-1](https://github.com/Lolik-Bolik/Knapsack_problem_0-1)
- Number of projects: 10
- Available budget: 269

| Project | Cost | Benefit |
|-|-|-|
| A | 55 | 95 |
| B | 10 | 4 |
| C | 47 | 60 |
| D | 5 | 32 |
| E | 4 | 23 |
| F | 50 | 72 |
| G | 8 | 80 |
| H | 61 | 62 |
| I | 85 | 65 |
| J | 87 | 46 |

Optimal solution: [A, B, C, D, E, F, G, I]
Total cost: 264
Total benefit: 431