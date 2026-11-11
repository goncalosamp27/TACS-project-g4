"""T3: BESSER Quantum DSL -> generated Qiskit + domain-result decoding.

Run after T1 and T2, from the project root:
    python transformations/t3_quantum_to_qiskit.py

T3 uses the exact QUBO file recorded in quantum_instance.py, then follows
T1's source-problem metadata to select the matching Problem ObjectModel.
Simulation shots are read from transformations/solver_config.json.

The BESSER generator produces the circuit/simulation script. T3 adds a
reproducible, automatically generated result-analysis section; it does not
manually edit the generated script. A separate brute-force calculation is
used as a classical baseline (not inferred from measured quantum states).
"""
from __future__ import annotations

import argparse
import json
import ast
import os
from pathlib import Path
import re
import runpy
import tempfile
from textwrap import dedent

ROOT = Path(__file__).resolve().parent.parent
GENERATED_DIR = Path(__file__).resolve().parent / "generated"
OBJECT_DIR = ROOT / "code" / "object"
DEFAULT_CONFIG = Path(__file__).resolve().parent / "solver_config.json"


def read_attribute(obj, name: str):
    """Read a semantic attribute from BESSER object slots."""
    vals = [slot.value.value for slot in obj.slots if slot.attribute.name == name]
    if len(vals) != 1:
        raise ValueError(f"Expected exactly one attribute {name!r} on {obj.name!r}")
    return vals[0]


def find_source_problem(qubo_path: Path) -> tuple[Path, list[int]]:
    """Follow metadata emitted by T1, without selecting a hard-coded instance."""
    text = qubo_path.read_text(encoding="utf-8")
    match = re.search(r"^# Source problem file:\s*(\S+)\s*$", text, re.MULTILINE)
    if match is None:
        raise ValueError(f"No T1 source problem metadata in {qubo_path}")
    source_name = match.group(1)
    if Path(source_name).name != source_name or not source_name.endswith(".py"):
        raise ValueError(f"Invalid source model name in T1 output: {source_name!r}")
    source_path = OBJECT_DIR / source_name
    if not source_path.is_file():
        raise FileNotFoundError(f"Problem model referenced by T1 is missing: {source_path}")

    slack_match = re.search(r"^# Slack variable weights:\s*(\[.*\])\s*$", text, re.MULTILINE)
    if slack_match is None:
        raise ValueError(f"No slack-weight metadata in {qubo_path}")
    slack_weights = ast.literal_eval(slack_match.group(1))
    if not isinstance(slack_weights, list) or any(type(w) is not int or w <= 0 for w in slack_weights):
        raise ValueError("Invalid slack weights in T1 output")
    return source_path, slack_weights


def read_problem(problem_path: Path) -> tuple[dict[str, dict[str, int]], int]:
    """Read projects, costs, benefits and budget from the Problem ObjectModel."""
    problem_model = runpy.run_path(str(problem_path)).get("object_model")
    if problem_model is None:
        raise ValueError(f"Missing BESSER object_model in {problem_path}")
    problems = [o for o in problem_model.objects if o.classifier.name == "SelectionProblem"]
    if len(problems) != 1:
        raise ValueError("Expected exactly one SelectionProblem")
    budget = read_attribute(problems[0], "budget")
    if type(budget) is not int or budget < 0:
        raise ValueError("Invalid SelectionProblem.budget")

    projects: dict[str, dict[str, int]] = {}
    for obj in problem_model.objects:
        if obj.classifier.name != "ProjectClass":
            continue
        identifier = read_attribute(obj, "id")
        cost = read_attribute(obj, "cost")
        benefit = read_attribute(obj, "benefit")
        if (not isinstance(identifier, str) or not identifier
                or type(cost) is not int or cost < 0
                or type(benefit) is not int or benefit < 0):
            raise ValueError(f"Invalid project in {obj.name}")
        if identifier in projects:
            raise ValueError(f"Duplicate ProjectClass.id: {identifier!r}")
        projects[identifier] = {"cost": cost, "benefit": benefit}
    if not projects:
        raise ValueError("Problem model has no projects")
    return dict(sorted(projects.items())), budget


def validate_matching_models(variable_names: list[str], projects: dict, slack_weights: list[int]) -> None:
    if len(variable_names) != len(set(variable_names)):
        raise ValueError("Repeated variable names in T2 output")
    project_vars = {f"x_{name}" for name in projects}
    slack_vars = {f"s_{index}" for index in range(1, len(slack_weights) + 1)}
    if set(variable_names) != project_vars | slack_vars:
        raise ValueError(
            "T2 QUBO variables do not match the associated Problem Model: "
            f"expected {sorted(project_vars | slack_vars)}, got {sorted(variable_names)}"
        )


def build_analysis_source(variable_names: list[str], projects: dict, budget: int,
                          slack_weights: list[int]) -> str:
    """Create the M2T results/decode template using source-model data."""
    header = (
        "\n\n# ================================================================\n"
        "# GENERATED T3 DOMAIN DECODING + INDEPENDENT CLASSICAL BASELINE\n"
        "# ================================================================\n"
        "from itertools import combinations as _tacs_combinations\n"
        f"_tacs_qubo_vars = {variable_names!r}\n"
        f"_tacs_projects = {projects!r}\n"
        f"_tacs_budget = {budget!r}\n"
        f"_tacs_slack_weights = {slack_weights!r}\n"
    )
    code = dedent('''
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

        print("\\n=== Classical baseline (exact brute force) ===")
        print(f"Budget: {_tacs_budget}")
        print(f"Optimal benefit: {_tacs_optimum}")
        print(f"Optimal project selections: {sorted(_tacs_optimal_selections)}")
        print("\\n=== QAOA measurement validation ===")
        print(f"Shots: {_tacs_total_shots}")
        print(f"Best feasible selection measured: {_tacs_best_measured}")
        print(f"Best measured benefit: {_tacs_best_measured_benefit}")
        print(f"Approximation ratio (best measured / optimum): {_tacs_ratio:.4f}")
        print(f"Domain-feasible observations: {100*_tacs_domain_feasible/_tacs_total_shots:.2f}%")
        print(f"QUBO-feasible observations (consistent slack): {100*_tacs_full_qubo_feasible/_tacs_total_shots:.2f}%")
        print(f"Optimal project selections measured: {100*_tacs_optimal_domain/_tacs_total_shots:.2f}%")
        print(f"Optimal full QUBO states measured: {100*_tacs_optimal_full_qubo/_tacs_total_shots:.2f}%")
        print("\\nTop 5 measured project selections (slack aggregated):")
        for _selection, _count in sorted(
            _tacs_domain_counts.items(), key=lambda kv: (-kv[1], kv[0])
        )[:5]:
            _cost = sum(_tacs_projects[_p]['cost'] for _p in _selection)
            _benefit = sum(_tacs_projects[_p]['benefit'] for _p in _selection)
            print(f"  {_selection}: {_count/_tacs_total_shots:.2%}, cost={_cost}, "
                  f"benefit={_benefit}, feasible={_cost <= _tacs_budget}")
    ''')
    return header + code


def read_shots(path: Path) -> int:
    """Read the sample count from the same solver model used by T2."""
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Missing solver configuration: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(config, dict):
        raise ValueError("Solver configuration must be a JSON object")
    shots = config.get("shots")
    if type(shots) is not int or shots <= 0:
        raise ValueError("Solver 'shots' must be a positive integer")
    return shots


def configure_generated_shots(source: str, shots: int) -> str:
    """M2T postprocessing: apply configured shot count to BESSER output.

    The generated Qiskit script is never edited manually. Fail clearly if
    a future BESSER generator version changes its simulator call layout.
    """
    pattern = r"(simulator\.run\(\s*transpiled_qc\s*,\s*shots\s*=\s*)\d+(\s*\))"
    patched, count = re.subn(pattern, lambda match: f"{match.group(1)}{shots}{match.group(2)}", source)
    if count != 1:
        raise ValueError(
            "Could not locate exactly one Aer simulator.run(..., shots=...) "
            "call in BESSER output; adapt the M2T generation rule"
        )
    return patched


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quantum-file", type=Path, default=GENERATED_DIR / "quantum_instance.py")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--shots", type=int, help="Override shots from JSON")
    parser.add_argument("--output", type=Path, default=GENERATED_DIR / "qiskit_circuit.py")
    args = parser.parse_args()
    shots = args.shots if args.shots is not None else read_shots(args.config)
    if type(shots) is not int or shots <= 0:
        parser.error("--shots must be a positive integer")

    quantum_path = args.quantum_file.resolve()
    if not quantum_path.is_file():
        parser.error(f"Missing T2 quantum model: {quantum_path}")
    namespace = runpy.run_path(str(quantum_path))
    qc = namespace.get("qc")
    variables = namespace.get("qubo_variable_names")
    source_qubo_file = namespace.get("source_qubo_file")
    if qc is None or not isinstance(variables, list) or not isinstance(source_qubo_file, str):
        raise ValueError("T2 output lacks qc, qubo_variable_names, or source_qubo_file")
    if Path(source_qubo_file).name != source_qubo_file:
        raise ValueError(f"Invalid QUBO filename recorded by T2: {source_qubo_file!r}")

    qubo_path = GENERATED_DIR / source_qubo_file
    if not qubo_path.is_file():
        raise FileNotFoundError(f"T1 QUBO referenced by T2 is missing: {qubo_path}")
    problem_path, slack_weights = find_source_problem(qubo_path)
    projects, budget = read_problem(problem_path)
    validate_matching_models(variables, projects, slack_weights)

    from besser.generators.qiskit import QiskitGenerator

    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    # Generate in a clean temporary directory so an older output cannot
    # accidentally be mistaken for the result of this run.
    with tempfile.TemporaryDirectory(prefix=".t3-build-", dir=GENERATED_DIR) as build_dir:
        old_cwd = Path.cwd()
        try:
            os.chdir(build_dir)
            QiskitGenerator(model=qc).generate()
        finally:
            os.chdir(old_cwd)
        generated = Path(build_dir) / "output" / "qiskit_circuit.py"
        if not generated.is_file():
            raise FileNotFoundError(f"BESSER generator did not produce {generated}")
        generated_text = generated.read_text(encoding="utf-8")
    generated_text = configure_generated_shots(generated_text, shots)
    if "counts" not in generated_text:
        raise ValueError("Generated BESSER script does not define measurement counts")
    analysis_code = build_analysis_source(variables, projects, budget, slack_weights)
    result = generated_text + analysis_code
    compile(result, str(args.output), "exec")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(result, encoding="utf-8")
    print(f"T3 input: {quantum_path.name}; T1 source: {qubo_path.name}")
    print(f"Problem: {problem_path.name}; {len(projects)} projects; budget={budget}")
    print(f"Generated: {args.output.resolve()}")
    print(f"Simulation shots: {shots} (solver configuration)")


if __name__ == "__main__":
    main()
