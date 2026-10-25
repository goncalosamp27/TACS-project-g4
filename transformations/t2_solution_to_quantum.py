import sys
import os

# Ajoute le dossier parent au chemin de recherche Python pour localiser solution_DSL_object_diagram
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code')))

import math
from solution_DSL_object_diagram import object_model

# Importing the existing quantum metamodel classes from BESSER
from besser.BUML.metamodel.quantum import (
    QuantumCircuit,
    QuantumRegister,
    ClassicalRegister,
    HadamardGate,
    CXGate,
    RZGate,
    RXGate,
    Measurement
)

def transform_t2_solution_to_quantum(qubo_model, p_depth=1, gamma=math.pi / 8, beta=math.pi / 4):
    """
    Transformation T2 (M2M): Converts the Solution Model (QUBO) into instances 
    of the BESSER Quantum Model.
    """
    
    # 1. Extract objects from the input QUBO model
    binary_vars = [obj for obj in qubo_model.objects if obj.classifier.name == "BinaryVariable"]
    linear_terms = [obj for obj in qubo_model.objects if obj.classifier.name == "LinearTerm"]
    quadratic_terms = [obj for obj in qubo_model.objects if obj.classifier.name == "QuadraticTerm"]
    
    # Sort variables to guarantee a deterministic qubit order
    binary_vars.sort(key=lambda v: v.name)
    num_qubits = len(binary_vars)
    
    # 2. Create registers and the quantum circuit
    node_reg = QuantumRegister(size=num_qubits, name="nodes")
    cls_reg = ClassicalRegister(size=num_qubits, name="result")
    qc = QuantumCircuit(name="Knapsack_QAOA")
    
    # Mapping: Associate each BinaryVariable with its Qubit in the register
    var_to_qubit = {}
    for i, var in enumerate(binary_vars):
        var_to_qubit[var] = node_reg.qubits[i]
        
    quantum_gates = []

    # 3. Apply quantum gates (QAOA Algorithm)
    
    # Step A: Initial Superposition (Hadamard)
    for i in range(num_qubits):
        h_gate = HadamardGate(node_reg.qubits[i])
        quantum_gates.append(h_gate)
        
    # Step B: QAOA Optimization Layers
    for layer in range(p_depth):
        
        # Cost Hamiltonian: Linear terms (RZ Gates)
        for lt in linear_terms:
            target_q = var_to_qubit[lt.linearVariable]
            angle = 2 * gamma * lt.coefficient
            
            rz_gate = RZGate(angle, target_q)
            quantum_gates.append(rz_gate)
            
        # Cost Hamiltonian: Quadratic terms (CX-RZ-CX Entanglement)
        for qt in quadratic_terms:
            vars_set = list(qt.variables)
            q1 = var_to_qubit[vars_set[0]]
            q2 = var_to_qubit[vars_set[1]]
            angle = 2 * gamma * qt.coefficient
            
            cx1 = CXGate(q1, q2)
            rz = RZGate(angle, q2)
            cx2 = CXGate(q1, q2)
            quantum_gates.extend([cx1, rz, cx2])
            
        # Mixer Hamiltonian: RX Gates
        for i in range(num_qubits):
            rx_gate = RXGate(2 * beta, node_reg.qubits[i])
            quantum_gates.append(rx_gate)
            
    # Step C: Final Measurements
    for i in range(num_qubits):
        meas = Measurement(node_reg.qubits[i], i)
        quantum_gates.append(meas)
        
    # 4. Attach elements to the circuit
    qc.registers = [node_reg, cls_reg]
    qc.gates = quantum_gates
        
    return qc

# ==========================================
# T2 EXECUTION
# ==========================================

# Execute the T2 transformation with the object model (QUBO)
my_quantum_circuit = transform_t2_solution_to_quantum(qubo_model=object_model, p_depth=1)

# Console verification
print(f"Success: Quantum model instantiated successfully.")
print(f"Circuit Name: {my_quantum_circuit.name}")