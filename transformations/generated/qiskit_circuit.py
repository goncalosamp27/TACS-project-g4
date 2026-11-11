import sys
import os
sys.path = [p.strip() for p in sys.path if p]
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.circuit import Instruction

from qiskit_aer import AerSimulator

from qiskit.circuit.library import *
from qiskit.circuit.library.standard_gates import GlobalPhaseGate
import numpy as np










# Function Gate Definitions



# Initialize Registers

q = QuantumRegister(10, 'q')


c = ClassicalRegister(10, 'c')


# Initialize Circuit
qc = QuantumCircuit(q, c)

# Operations

qc.append(HGate(), [q[0]])

qc.append(HGate(), [q[1]])

qc.append(HGate(), [q[2]])

qc.append(HGate(), [q[3]])

qc.append(HGate(), [q[4]])

qc.append(HGate(), [q[5]])

qc.append(HGate(), [q[6]])

qc.append(HGate(), [q[7]])

qc.append(HGate(), [q[8]])

qc.append(HGate(), [q[9]])

qc.append(RZGate(-0.7853981633974483), [q[0]])

qc.append(RZGate(-0.45818284048630936), [q[1]])

qc.append(RZGate(-0.7199144046098631), [q[2]])

qc.append(RZGate(-0.5236326874360967), [q[3]])

qc.append(RZGate(-0.5891164462236819), [q[4]])

qc.append(RZGate(-0.065517670625383), [q[5]])

qc.append(RZGate(-0.131035341250766), [q[6]])

qc.append(RZGate(-0.262070682501532), [q[7]])

qc.append(RZGate(-0.524141365003064), [q[8]])

qc.append(RZGate(-0.7206943768792129), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[1]])

qc.append(RZGate(0.262070682501532), [q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[2]])

qc.append(RZGate(0.41182535821669314), [q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[3]])

qc.append(RZGate(0.29950935143032226), [q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[4]])

qc.append(RZGate(0.33694802035911253), [q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[5]])

qc.append(RZGate(0.03743866892879028), [q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[6]])

qc.append(RZGate(0.07487733785758056), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[7]])

qc.append(RZGate(0.14975467571516113), [q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[8]])

qc.append(RZGate(0.29950935143032226), [q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[9]])

qc.append(RZGate(0.41182535821669314), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[2]])

qc.append(RZGate(0.24023145895973766), [q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[3]])

qc.append(RZGate(0.17471378833435464), [q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[4]])

qc.append(RZGate(0.196553011876149), [q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[5]])

qc.append(RZGate(0.02183922354179433), [q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[6]])

qc.append(RZGate(0.04367844708358866), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[7]])

qc.append(RZGate(0.08735689416717732), [q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[8]])

qc.append(RZGate(0.17471378833435464), [q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[9]])

qc.append(RZGate(0.24023145895973766), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[3]])

qc.append(RZGate(0.2745502388111287), [q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[4]])

qc.append(RZGate(0.3088690186625198), [q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[5]])

qc.append(RZGate(0.03431877985139109), [q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[6]])

qc.append(RZGate(0.06863755970278218), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[7]])

qc.append(RZGate(0.13727511940556436), [q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[8]])

qc.append(RZGate(0.2745502388111287), [q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[9]])

qc.append(RZGate(0.37750657836530194), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[4]])

qc.append(RZGate(0.22463201357274168), [q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[5]])

qc.append(RZGate(0.024959112619193518), [q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[6]])

qc.append(RZGate(0.049918225238387036), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[7]])

qc.append(RZGate(0.09983645047677407), [q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[8]])

qc.append(RZGate(0.19967290095354814), [q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[9]])

qc.append(RZGate(0.2745502388111287), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[5]])

qc.append(RZGate(0.02807900169659271), [q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[6]])

qc.append(RZGate(0.05615800339318542), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[7]])

qc.append(RZGate(0.11231600678637084), [q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[8]])

qc.append(RZGate(0.22463201357274168), [q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[9]])

qc.append(RZGate(0.3088690186625198), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[6]])

qc.append(RZGate(0.0062397781547983795), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[7]])

qc.append(RZGate(0.012479556309596759), [q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[8]])

qc.append(RZGate(0.024959112619193518), [q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[9]])

qc.append(RZGate(0.03431877985139109), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[7]])

qc.append(RZGate(0.024959112619193518), [q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[8]])

qc.append(RZGate(0.049918225238387036), [q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[9]])

qc.append(RZGate(0.06863755970278218), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[8]])

qc.append(RZGate(0.09983645047677407), [q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[9]])

qc.append(RZGate(0.13727511940556436), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[9]])

qc.append(RZGate(0.2745502388111287), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[9]])

qc.append(RXGate(1.5707963267948966), [q[0]])

qc.append(RXGate(1.5707963267948966), [q[1]])

qc.append(RXGate(1.5707963267948966), [q[2]])

qc.append(RXGate(1.5707963267948966), [q[3]])

qc.append(RXGate(1.5707963267948966), [q[4]])

qc.append(RXGate(1.5707963267948966), [q[5]])

qc.append(RXGate(1.5707963267948966), [q[6]])

qc.append(RXGate(1.5707963267948966), [q[7]])

qc.append(RXGate(1.5707963267948966), [q[8]])

qc.append(RXGate(1.5707963267948966), [q[9]])

qc.measure(q[0], c[0])

qc.measure(q[1], c[1])

qc.measure(q[2], c[2])

qc.measure(q[3], c[3])

qc.measure(q[4], c[4])

qc.measure(q[5], c[5])

qc.measure(q[6], c[6])

qc.measure(q[7], c[7])

qc.measure(q[8], c[8])

qc.measure(q[9], c[9])


# Draw
print(qc.draw())


# Execution (Local Aer Simulator)
print("Simulating circuit with Aer Simulator...")
simulator = AerSimulator()
transpiled_qc = transpile(qc, simulator)
result = simulator.run(transpiled_qc, shots=1024).result()
counts = result.get_counts()
print("Counts:", counts)


# ================================================================
# GENERATED T3 DOMAIN DECODING + INDEPENDENT CLASSICAL BASELINE
# ================================================================
from itertools import combinations as _tacs_combinations
_tacs_qubo_vars = ['x_A', 'x_B', 'x_C', 'x_D', 'x_E', 's_1', 's_2', 's_3', 's_4', 's_5']
_tacs_projects = {'A': {'cost': 12, 'benefit': 24}, 'B': {'cost': 7, 'benefit': 13}, 'C': {'cost': 11, 'benefit': 23}, 'D': {'cost': 8, 'benefit': 15}, 'E': {'cost': 9, 'benefit': 16}}
_tacs_budget = 26
_tacs_slack_weights = [1, 2, 4, 8, 11]

_tacs_project_ids = tuple(sorted(_tacs_projects))
_tacs_total_shots = sum(counts.values())
if _tacs_total_shots <= 0:
    raise ValueError("Aer returned no measurement counts")

# Classical exhaustive search. Independent of any measured bitstring.
_tacs_optimum = -1
_tacs_optimal_selections = set()
for _r in range(len(_tacs_project_ids) + 1):
    for _choice in _tacs_combinations(_tacs_project_ids, _r):
        _cost = sum(_tacs_projects[_p]["cost"] for _p in _choice)
        if _cost > _tacs_budget:
            continue
        _benefit = sum(_tacs_projects[_p]["benefit"] for _p in _choice)
        if _benefit > _tacs_optimum:
            _tacs_optimum = _benefit
            _tacs_optimal_selections = {_choice}
        elif _benefit == _tacs_optimum:
            _tacs_optimal_selections.add(_choice)
assert _tacs_optimum >= 0

# Counts in Qiskit are big-endian display strings; bit i is counted
# from the RIGHT. T2 measures qubit i into classical bit i.
_tacs_domain_counts = {}
_tacs_domain_feasible = 0
_tacs_full_qubo_feasible = 0
_tacs_optimal_domain = 0
_tacs_optimal_full_qubo = 0
for _display_bits, _frequency in counts.items():
    _bits = ''.join(_ch for _ch in _display_bits if _ch in '01')
    if len(_bits) != len(_tacs_qubo_vars):
        raise ValueError(f"Unexpected Qiskit bitstring: {_display_bits!r}")
    _chosen = []
    _unused_budget = 0
    for _i, _bit in enumerate(reversed(_bits)):
        if _bit == '0':
            continue
        _name = _tacs_qubo_vars[_i]
        if _name.startswith('x_'):
            _chosen.append(_name[2:])
        elif _name.startswith('s_'):
            _index = int(_name[2:]) - 1
            _unused_budget += _tacs_slack_weights[_index]
        else:
            raise ValueError(f"Unexpected QUBO variable: {_name!r}")
    _selection = tuple(sorted(_chosen))
    _cost = sum(_tacs_projects[_p]['cost'] for _p in _selection)
    _is_domain_feasible = _cost <= _tacs_budget
    _is_qubo_feasible = _cost + _unused_budget == _tacs_budget
    _tacs_domain_counts[_selection] = _tacs_domain_counts.get(_selection, 0) + _frequency
    if _is_domain_feasible:
        _tacs_domain_feasible += _frequency
    if _is_qubo_feasible:
        _tacs_full_qubo_feasible += _frequency
    if _selection in _tacs_optimal_selections:
        _tacs_optimal_domain += _frequency
        if _is_qubo_feasible:
            _tacs_optimal_full_qubo += _frequency

_tacs_measured_feasible = [
    _selection for _selection in _tacs_domain_counts
    if sum(_tacs_projects[_p]['cost'] for _p in _selection) <= _tacs_budget
]
_tacs_best_measured = max(
    _tacs_measured_feasible,
    key=lambda _sel: (sum(_tacs_projects[_p]['benefit'] for _p in _sel),
                      -sum(_tacs_projects[_p]['cost'] for _p in _sel)),
    default=None,
)
_tacs_best_measured_benefit = (
    sum(_tacs_projects[_p]['benefit'] for _p in _tacs_best_measured)
    if _tacs_best_measured is not None else None
)
_tacs_ratio = (
    (_tacs_best_measured_benefit / _tacs_optimum if _tacs_optimum > 0 else 1.0)
    if _tacs_best_measured_benefit is not None else 0.0
)

print("\n=== Classical baseline (exact brute force) ===")
print(f"Budget: {_tacs_budget}")
print(f"Optimal benefit: {_tacs_optimum}")
print(f"Optimal project selections: {sorted(_tacs_optimal_selections)}")
print("\n=== QAOA measurement validation ===")
print(f"Shots: {_tacs_total_shots}")
print(f"Best feasible selection measured: {_tacs_best_measured}")
print(f"Best measured benefit: {_tacs_best_measured_benefit}")
print(f"Approximation ratio (best measured / optimum): {_tacs_ratio:.4f}")
print(f"Domain-feasible observations: {100*_tacs_domain_feasible/_tacs_total_shots:.2f}%")
print(f"QUBO-feasible observations (consistent slack): {100*_tacs_full_qubo_feasible/_tacs_total_shots:.2f}%")
print(f"Optimal project selections measured: {100*_tacs_optimal_domain/_tacs_total_shots:.2f}%")
print(f"Optimal full QUBO states measured: {100*_tacs_optimal_full_qubo/_tacs_total_shots:.2f}%")
print("\nTop 5 measured project selections (slack aggregated):")
for _selection, _count in sorted(
    _tacs_domain_counts.items(), key=lambda kv: (-kv[1], kv[0])
)[:5]:
    _cost = sum(_tacs_projects[_p]['cost'] for _p in _selection)
    _benefit = sum(_tacs_projects[_p]['benefit'] for _p in _selection)
    print(f"  {_selection}: {_count/_tacs_total_shots:.2%}, cost={_cost}, "
          f"benefit={_benefit}, feasible={_cost <= _tacs_budget}")
