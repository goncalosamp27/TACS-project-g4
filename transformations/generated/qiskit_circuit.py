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

qc.append(RZGate(-27975.88258021711), [q[9]])

qc.append(RZGate(-32587.740595686922), [q[4]])

qc.append(RZGate(-32605.804753445067), [q[7]])

qc.append(RZGate(-13873.273158252527), [q[2]])

qc.append(RZGate(-3685.0881826608274), [q[0]])

qc.append(RZGate(-34702.032451552855), [q[5]])

qc.append(RZGate(-25446.115095913927), [q[8]])

qc.append(RZGate(-25434.334123462966), [q[3]])

qc.append(RZGate(-7225.663103256524), [q[1]])

qc.append(RZGate(-22771.048951382218), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[6]])

qc.append(RZGate(8092.742675647307), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[9]])

qc.append(RZGate(14306.812944447918), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[4]])

qc.append(RZGate(17486.104709880787), [q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[5]])

qc.append(RZGate(19075.750592597225), [q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[2]])

qc.append(RZGate(6358.5835308657415), [q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[0]])

qc.append(RZGate(578.0530482605219), [q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[0]])

qc.append(RZGate(1011.5928344559134), [q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[0]])

qc.append(RZGate(1156.1060965210438), [q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[0]])

qc.append(RZGate(1589.6458827164354), [q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[9]])

qc.append(RZGate(15607.432303034093), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[2]])

qc.append(RZGate(4046.3713378236534), [q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[2]])

qc.append(RZGate(4624.424386084175), [q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[1]])

qc.append(RZGate(2312.2121930420876), [q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[6]])

qc.append(RZGate(11127.521179015048), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[1]])

qc.append(RZGate(3468.3182895631317), [q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[4]])

qc.append(RZGate(12717.167061731483), [q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[9]])

qc.append(RZGate(14306.812944447918), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[2]])

qc.append(RZGate(4624.424386084175), [q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[3]])

qc.append(RZGate(13873.273158252527), [q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[9]])

qc.append(RZGate(2601.2387171723485), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[1]])

qc.append(RZGate(3179.2917654328708), [q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[3]])

qc.append(RZGate(12717.167061731483), [q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[6]])

qc.append(RZGate(11127.521179015048), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[9]])

qc.append(RZGate(10404.954868689394), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[3]])

qc.append(RZGate(12717.167061731483), [q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[6]])

qc.append(RZGate(12139.11401347096), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[9]])

qc.append(RZGate(9104.335510103221), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[9]])

qc.append(RZGate(5202.477434344697), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[0]])

qc.append(RZGate(289.02652413026095), [q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[9]])

qc.append(RZGate(10404.954868689394), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[5]])

qc.append(RZGate(13873.273158252527), [q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[0]])

qc.append(RZGate(1156.1060965210438), [q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[1]])

qc.append(RZGate(2023.1856689118267), [q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[1]])

qc.append(RZGate(2312.2121930420876), [q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[1]])

qc.append(RZGate(1156.1060965210438), [q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[3]])

qc.append(RZGate(8092.742675647307), [q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[0]])

qc.append(RZGate(1734.1591447815658), [q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[3]])

qc.append(RZGate(9248.84877216835), [q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[1]])

qc.append(RZGate(3179.2917654328708), [q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[7]])

qc.append(RZGate(12717.167061731483), [q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[2]])

qc.append(RZGate(6936.636579126263), [q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[9]])

qc.append(RZGate(1300.6193585861743), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[0]])

qc.append(RZGate(1589.6458827164354), [q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[2]])

qc.append(RZGate(6358.5835308657415), [q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[5]])

qc.append(RZGate(19075.750592597225), [q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[5]])

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

# ==========================================
# DOMAIN TERMS DECODING & VALIDATION (T3)
# ==========================================
print("\n--- Domain Validation and Probability Analysis ---")

qubo_vars = ['s_1', 's_2', 's_3', 's_4', 's_5', 'x_A', 'x_B', 'x_C', 'x_D', 'x_E']
total_shots = sum(counts.values())

# --- DYNAMIC PROBLEM DATA ---
# Injected directly from the MDE Problem Model (problem_DSL_object_diagram.py)
projects_data = {
    'A': {'cost': 12, 'benefit': 24},
    'B': {'cost': 7, 'benefit': 13},
    'C': {'cost': 11, 'benefit': 23},
    'D': {'cost': 8, 'benefit': 15},
    'E': {'cost': 9, 'benefit': 16},
}
max_budget = 26

# Aggregate counts by decoded domain solution
aggregated_results = {}

for bitstring, count in counts.items():
    # Read Little Endian
    reversed_bitstring = bitstring[::-1]
    
    selected_items = []
    for i, bit in enumerate(reversed_bitstring):
        if bit == '1' and i < len(qubo_vars):
            var_name = qubo_vars[i]
            if var_name.startswith('x_'):
                selected_items.append(var_name.split('_')[1])
            elif not var_name.startswith('s_'):
                selected_items.append(var_name)
                
    # Sort items to correctly group identical combinations (e.g. 'C, B' and 'B, C')
    selected_items.sort()
    solution_tuple = tuple(selected_items)
    
    if solution_tuple in aggregated_results:
        aggregated_results[solution_tuple] += count
    else:
        aggregated_results[solution_tuple] = count

# Evaluate all unique solutions found by the quantum circuit
evaluated_solutions = []
for solution, count in aggregated_results.items():
    total_cost = sum(projects_data.get(item, {'cost': 0})['cost'] for item in solution)
    total_benefit = sum(projects_data.get(item, {'benefit': 0})['benefit'] for item in solution)
    
    is_valid = total_cost <= max_budget
    prob = (count / total_shots) * 100
    
    evaluated_solutions.append({
        'items': solution,
        'cost': total_cost,
        'benefit': total_benefit,
        'is_valid': is_valid,
        'count': count,
        'prob': prob
    })

# ---------------------------------------------------------
# HIGHLIGHT THE TRUE OPTIMAL SOLUTION (CLASSICAL BASELINE)
# ---------------------------------------------------------
# Filter valid solutions and find the one with the absolute maximum benefit
valid_solutions = [s for s in evaluated_solutions if s['is_valid']]

if valid_solutions:
    best_valid = max(valid_solutions, key=lambda x: x['benefit'])
    sol_str = ', '.join(best_valid['items']) if best_valid['items'] else 'None'
    
    print(f"\n🏆 TRUE OPTIMAL SOLUTION MEASURED:")
    print(f"  -> Items selected: [{sol_str}]")
    print(f"  -> Cost: {best_valid['cost']} (Max: {max_budget}) | Benefit: {best_valid['benefit']}")
    print(f"  -> Quantum Probability: {best_valid['prob']:.2f}% (measured {best_valid['count']} times)")
else:
    print("\n❌ No valid solutions were measured by the quantum circuit.")

# ---------------------------------------------------------
# SHOW MOST FREQUENT QUANTUM STATES
# ---------------------------------------------------------
# Sort by highest quantum probability (count) to see what the circuit favored
evaluated_solutions.sort(key=lambda x: x['count'], reverse=True)

print(f"\n--- Top 5 Most Frequent Quantum States ---")
for s in evaluated_solutions[:5]:
    status = "✅ Valid" if s['is_valid'] else "❌ INVALID (Overweight)"
    sol_str = ', '.join(s['items']) if s['items'] else 'None'
    print(f"  -> [{sol_str}] : {s['prob']:.2f}% | {status} | Cost: {s['cost']}, Benefit: {s['benefit']}")
