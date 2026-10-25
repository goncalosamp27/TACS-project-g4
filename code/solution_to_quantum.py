from qiskit import QuantumCircuit
from besser.BUML.metamodel.object import ObjectModel
from solution_DSL_object_diagram import object_model

def transform_t2_solution_to_qaoa(object_model: ObjectModel, p_depth: int = 1, gamma: list = [0.5], beta: list = [0.5]):
    """
    Transformation T2: Converts the Solution Model (QUBO) into a Quantum Model (Qiskit QAOA Circuit).
    Ref: Farhi et al. (2014) - A Quantum Approximate Optimization Algorithm.
    """
    
    # 1. Extract objects from the BESSER ObjectModel
    # Filter objects by their type (Class)
    binary_vars = [obj for obj in object_model.objects if obj.classifier.name == "BinaryVariable"]
    linear_terms = [obj for obj in object_model.objects if obj.classifier.name == "LinearTerm"]
    quadratic_terms = [obj for obj in object_model.objects if obj.classifier.name == "QuadraticTerm"]

    # 2. Map binary variables to Qubits
    # Sort to ensure the qubit order remains deterministic across executions
    binary_vars.sort(key=lambda v: v.name) 
    
    var_to_qubit = {}
    for idx, var in enumerate(binary_vars):
        var_to_qubit[var] = idx  # Map the BinaryVariable object instance to an integer index

    num_qubits = len(binary_vars)
    
    # Initialize the quantum circuit with num_qubits
    qc = QuantumCircuit(num_qubits)
    
    # --- STEP A: Initialization ---
    # Rule: Initial equal superposition (Hadamard gates)
    for i in range(num_qubits):
        qc.h(i)
    
    qc.barrier()
    
    # --- STEP B: QAOA Loop (p layers) ---
    for layer in range(p_depth):
        g = gamma[layer]
        b = beta[layer]
        
        # B.1: Cost Hamiltonian (H_C) based on the QUBO formulation
        
        # Rule T2.1: Linear Terms -> RZ Gates
        # Ref: Lucas 2014, Ising formulations of many NP problems
        # A term c*x_i translates to a Z rotation by an angle proportional to the coefficient
        for lt in linear_terms:
            # Retrieve the linked variable via the 'linearVariable' association link
            var_obj = lt.linearVariable 
            qubit_idx = var_to_qubit[var_obj]
            
            # Retrieve the coefficient attribute value
            coeff = lt.coefficient
            
            angle = 2 * g * coeff
            qc.rz(angle, qubit_idx)
            
        # Rule T2.2: Quadratic Terms -> RZZ Entanglement Gates
        # A term c*x_i*x_j translates to a ZZ interaction between qubits i and j
        for qt in quadratic_terms:
            # Retrieve both linked variables via the 'variables' association link
            vars_set = list(qt.variables)
            q1 = var_to_qubit[vars_set[0]]
            q2 = var_to_qubit[vars_set[1]]
            
            coeff = qt.coefficient
            angle = 2 * g * coeff
            
            # Standard implementation of RZZ(angle) using CNOTs and RZ
            qc.cx(q1, q2)
            qc.rz(angle, q2)
            qc.cx(q1, q2)
            
        qc.barrier()
        
        # B.2: Mixer Hamiltonian (H_M)
        # Rule T2.3: Standard mixer -> RX gates on all qubits
        for i in range(num_qubits):
            qc.rx(2 * b, i)
            
        qc.barrier()
        
    # --- STEP C: Measurement ---
    # Add classical registers and measurement instructions
    qc.measure_all()
    
    # Return both the circuit AND the mapping dictionary for future automatic decoding
    return qc, var_to_qubit

# ==========================================
# SCRIPT EXECUTION (Generated via M2T)
# ==========================================

# Call the transformation function with your 'object_model'
# p_depth=1 (1 QAOA iteration), with example gamma and beta angles
quantum_circuit, qubit_mapping = transform_t2_solution_to_qaoa(
    object_model=object_model, 
    p_depth=1, 
    gamma=[0.5], 
    beta=[0.5]
)

# Display decoding information
print("--- Qubit <-> Variable Mapping ---")
for var_obj, q_idx in qubit_mapping.items():
    print(f"Qubit {q_idx} represents the variable: {var_obj.name}")

# Display the generated circuit in the console
print("\n--- Generated Quantum Circuit ---")
print(quantum_circuit.draw('text'))