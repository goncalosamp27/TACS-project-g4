import sys
import os
import glob
import importlib
import shutil

# 1. Path configuration
current_dir = os.path.dirname(os.path.abspath(__file__))
generated_dir = os.path.join(current_dir, 'generated')
sys.path.append(generated_dir)

# Import Solution Model & Circuit (T2 Output)
try:
    from quantum_instance import qc
except ImportError:
    print("❌ Error: 'quantum_instance.py' not found in generated/. Run T2 first.")
    sys.exit(1)

from besser.generators.qiskit import QiskitGenerator

# 2. Import Problem Model (To extract dynamic costs, benefits, and budget)
object_dir = os.path.abspath(os.path.join(current_dir, '..', 'code', 'object'))
sys.path.append(object_dir)
try:
    from small_problem_DSL_object_diagram import object_model as problem_model
except ImportError:
    print("❌ Error: 'problem_DSL_object_diagram.py' not found. Cannot extract dynamic problem data.")
    sys.exit(1)


def extract_problem_data():
    """Extracts costs, benefits, and budget dynamically from the source Problem Model."""
    projects_data = {}
    max_budget = 0
    
    # Helper function to safely read BESSER attributes (slots) and unwrap DataValues
    def get_attr(obj, attr_name, default):
        if hasattr(obj, 'slots'):
            for slot in obj.slots:
                if slot.attribute.name == attr_name:
                    val = slot.value
                    # BESSER wraps primitives in DataValue objects. Extract the real Python value.
                    if hasattr(val, 'value'):
                        return val.value
                    return val
                    
        # Fallback
        val = getattr(obj, attr_name, default)
        if hasattr(val, 'value'):
            return val.value
        return val

    # Iterate through all objects in the Problem DSL
    for obj in problem_model.objects:
        cls_name = obj.classifier.name
        
        if cls_name == "ProjectClass": 
            item_id = get_attr(obj, 'id', obj.name)
            item_cost = get_attr(obj, 'cost', 0)
            item_benefit = get_attr(obj, 'benefit', 0)
            
            projects_data[item_id] = {'cost': item_cost, 'benefit': item_benefit}
            
        elif cls_name == "SelectionProblem":
            max_budget = get_attr(obj, 'budget', 0)
            
    return projects_data, max_budget

def generate_t3_qiskit_script():
    print(f"🚀 Launching T3 (M2T) for circuit: {qc.name}")
    
    # Extract dynamic data from the problem instance
    projects_data, max_budget = extract_problem_data()
    
    # Format the dynamic Python dictionary string to inject into Qiskit
    projects_data_str = "{\n"
    for item, data in projects_data.items():
        projects_data_str += f"    '{item}': {{'cost': {data['cost']}, 'benefit': {data['benefit']}}},\n"
    projects_data_str += "}"
    
    original_cwd = os.getcwd()
    os.chdir(generated_dir)
    
    # 3. BESSER Generation
    generator = QiskitGenerator(model=qc)
    generator.generate()
    
    # 4. Clean up the 'output/' folder
    besser_output_path = os.path.join("output", "qiskit_circuit.py")
    target_file = "qiskit_circuit.py"
    
    if os.path.exists(besser_output_path):
        shutil.move(besser_output_path, target_file)
        try:
            os.rmdir("output")
        except OSError:
            pass

    if not os.path.exists(target_file):
        print("❌ Error: The Qiskit file could not be retrieved.")
        os.chdir(original_cwd)
        return

    # 5. Retrieve variable names from T1 (Solution Model)
    t1_files = glob.glob('t1-result-*.py')
    latest_t1_file = max(t1_files, key=os.path.getctime)
    module_name = os.path.basename(latest_t1_file).replace('.py', '')
    
    t1_module = importlib.import_module(module_name)
    bin_vars = sorted([v for v in t1_module.object_model.objects if v.classifier.name == "BinaryVariable"], key=lambda x: x.name)
    var_names = [v.name for v in bin_vars]
    
    # 6. Decoding, Evaluation & Validation Python Code (Injected)
    decoding_script = f"""
# ==========================================
# DOMAIN TERMS DECODING & VALIDATION (T3)
# ==========================================
print("\\n--- Domain Validation and Probability Analysis ---")

qubo_vars = {var_names}
total_shots = sum(counts.values())

# --- DYNAMIC PROBLEM DATA ---
# Injected directly from the MDE Problem Model (problem_DSL_object_diagram.py)
projects_data = {projects_data_str}
max_budget = {max_budget}

# Aggregate counts by decoded domain solution
aggregated_results = {{}}

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
    total_cost = sum(projects_data.get(item, {{'cost': 0}})['cost'] for item in solution)
    total_benefit = sum(projects_data.get(item, {{'benefit': 0}})['benefit'] for item in solution)
    
    is_valid = total_cost <= max_budget
    prob = (count / total_shots) * 100
    
    evaluated_solutions.append({{
        'items': solution,
        'cost': total_cost,
        'benefit': total_benefit,
        'is_valid': is_valid,
        'count': count,
        'prob': prob
    }})

# ---------------------------------------------------------
# HIGHLIGHT THE TRUE OPTIMAL SOLUTION (CLASSICAL BASELINE)
# ---------------------------------------------------------
# Filter valid solutions and find the one with the absolute maximum benefit
valid_solutions = [s for s in evaluated_solutions if s['is_valid']]

if valid_solutions:
    best_valid = max(valid_solutions, key=lambda x: x['benefit'])
    sol_str = ', '.join(best_valid['items']) if best_valid['items'] else 'None'
    
    print(f"\\n🏆 TRUE OPTIMAL SOLUTION MEASURED:")
    print(f"  -> Items selected: [{{sol_str}}]")
    print(f"  -> Cost: {{best_valid['cost']}} (Max: {{max_budget}}) | Benefit: {{best_valid['benefit']}}")
    print(f"  -> Quantum Probability: {{best_valid['prob']:.2f}}% (measured {{best_valid['count']}} times)")
else:
    print("\\n❌ No valid solutions were measured by the quantum circuit.")

# ---------------------------------------------------------
# SHOW MOST FREQUENT QUANTUM STATES
# ---------------------------------------------------------
# Sort by highest quantum probability (count) to see what the circuit favored
evaluated_solutions.sort(key=lambda x: x['count'], reverse=True)

print(f"\\n--- Top 5 Most Frequent Quantum States ---")
for s in evaluated_solutions[:5]:
    status = "✅ Valid" if s['is_valid'] else "❌ INVALID (Overweight)"
    sol_str = ', '.join(s['items']) if s['items'] else 'None'
    print(f"  -> [{{sol_str}}] : {{s['prob']:.2f}}% | {{status}} | Cost: {{s['cost']}}, Benefit: {{s['benefit']}}")
"""

    # 7. Injection into the final script
    with open(target_file, "a", encoding="utf-8") as f:
        f.write(decoding_script)
        
    os.chdir(original_cwd)
    print(f"✅ Step T3 successful! The final script is located at: transformations/generated/{target_file}")

if __name__ == "__main__":
    generate_t3_qiskit_script()