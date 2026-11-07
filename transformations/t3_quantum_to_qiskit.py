import sys
import os
import glob
import importlib
import shutil

# 1. Path configuration
current_dir = os.path.dirname(os.path.abspath(__file__))
generated_dir = os.path.join(current_dir, 'generated')
sys.path.append(generated_dir)

try:
    from quantum_instance import qc
except ImportError:
    print("❌ Error: 'quantum_instance.py' not found in generated/. Run T2 first.")
    sys.exit(1)

from besser.generators.qiskit import QiskitGenerator

def generate_t3_qiskit_script():
    print(f"🚀 Launching T3 (M2T) for circuit: {qc.name}")
    
    original_cwd = os.getcwd()
    os.chdir(generated_dir)
    
    # 2. BESSER Generation
    generator = QiskitGenerator(model=qc)
    generator.generate()
    
    # 3. Clean up the 'output/' folder
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

    # 4. Retrieve variable names from T1
    t1_files = glob.glob('t1-result-*.py')
    latest_t1_file = max(t1_files, key=os.path.getctime)
    module_name = os.path.basename(latest_t1_file).replace('.py', '')
    
    t1_module = importlib.import_module(module_name)
    bin_vars = sorted([v for v in t1_module.object_model.objects if v.classifier.name == "BinaryVariable"], key=lambda x: x.name)
    var_names = [v.name for v in bin_vars]
    
    # 5. Decoding & Validation Python Code (Injected)
    decoding_script = f"""
# ==========================================
# DOMAIN TERMS DECODING & VALIDATION (T3)
# ==========================================
print("\\n--- Domain Validation and Probability Analysis ---")

qubo_vars = {var_names}
total_shots = sum(counts.values())

# Aggregate counts by decoded domain solution (ignoring slack variables)
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
                
    solution_str = ', '.join(selected_items) if selected_items else 'None'
    
    # Sum the counts for identical domain solutions
    if solution_str in aggregated_results:
        aggregated_results[solution_str] += count
    else:
        aggregated_results[solution_str] = count

# Sort results by descending probability
sorted_solutions = sorted(aggregated_results.items(), key=lambda item: item[1], reverse=True)

print(f"Top 5 Domain Solutions measured over {{total_shots}} shots:")
for solution_str, count in sorted_solutions[:5]:
    prob = (count / total_shots) * 100
    print(f"  -> Solution [{{solution_str}}] : {{prob:.2f}}% probability (measured {{count}} times)")

print("\\nNote for the report: Compare these aggregated probabilities with the optimal classical baseline.")
"""

    # 6. Injection into the final script
    with open(target_file, "a", encoding="utf-8") as f:
        f.write(decoding_script)
        
    os.chdir(original_cwd)
    print(f"✅ Step T3 successful! The final script is located at: transformations/generated/{target_file}")

if __name__ == "__main__":
    generate_t3_qiskit_script()