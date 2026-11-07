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

qc.append(RZGate(-32587.740595686922), [q[4]])

qc.append(RZGate(-27975.88258021711), [q[9]])

qc.append(RZGate(-32605.804753445067), [q[7]])

qc.append(RZGate(-13873.273158252527), [q[2]])

qc.append(RZGate(-3685.0881826608274), [q[0]])

qc.append(RZGate(-34702.032451552855), [q[5]])

qc.append(RZGate(-25446.115095913927), [q[8]])

qc.append(RZGate(-25434.334123462966), [q[3]])

qc.append(RZGate(-22771.048951382218), [q[6]])

qc.append(RZGate(-7225.663103256524), [q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[4]])

qc.append(RZGate(17486.104709880787), [q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[5]])

qc.append(RZGate(19075.750592597225), [q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[5]])

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

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[5]])

qc.append(RZGate(15607.432303034093), [q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[2]])

qc.append(RZGate(4046.3713378236534), [q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[2]])

qc.append(RZGate(4624.424386084175), [q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[6]])

qc.append(RZGate(11127.521179015048), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[1]])

qc.append(RZGate(2312.2121930420876), [q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[1]])

qc.append(RZGate(3468.3182895631317), [q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[4]])

qc.append(RZGate(12717.167061731483), [q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[7]])

qc.append(RZGate(14306.812944447918), [q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[2]])

qc.append(RZGate(4624.424386084175), [q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[3]])

qc.append(RZGate(13873.273158252527), [q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[1]])

qc.append(RZGate(2601.2387171723485), [q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[1]])

qc.append(RZGate(3179.2917654328708), [q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[3]])

qc.append(RZGate(12717.167061731483), [q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[6]])

qc.append(RZGate(11127.521179015048), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[3]])

qc.append(RZGate(10404.954868689394), [q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[3]])

qc.append(RZGate(12717.167061731483), [q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[5]])

qc.append(RZGate(12139.11401347096), [q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[0]])

qc.append(RZGate(289.02652413026095), [q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[6]])

qc.append(RZGate(9104.335510103221), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[8]])

qc.append(RZGate(10404.954868689394), [q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[8]])

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

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[7]])

qc.append(RZGate(12717.167061731483), [q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[1]])

qc.append(RZGate(3179.2917654328708), [q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[2]])

qc.append(RZGate(6936.636579126263), [q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[0]])

qc.append(RZGate(1300.6193585861743), [q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[4]])

qc.append(RZGate(14306.812944447918), [q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[0]])

qc.append(RZGate(1589.6458827164354), [q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[0]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[2]])

qc.append(RZGate(6358.5835308657415), [q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[5]])

qc.append(RZGate(19075.750592597225), [q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[2]])

qc.append(RZGate(5202.477434344697), [q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[2]])

qc.append(RZGate(6358.5835308657415), [q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[6]])

qc.append(RZGate(8092.742675647307), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[6]])

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

# Aggregate counts by decoded domain solution (ignoring slack variables)
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
                
    solution_str = ', '.join(selected_items) if selected_items else 'None'
    
    # Sum the counts for identical domain solutions
    if solution_str in aggregated_results:
        aggregated_results[solution_str] += count
    else:
        aggregated_results[solution_str] = count

# Sort results by descending probability
sorted_solutions = sorted(aggregated_results.items(), key=lambda item: item[1], reverse=True)

print(f"Top 5 Domain Solutions measured over {total_shots} shots:")
for solution_str, count in sorted_solutions[:5]:
    prob = (count / total_shots) * 100
    print(f"  -> Solution [{solution_str}] : {prob:.2f}% probability (measured {count} times)")
