"""T2: transform a BESSER QUBO Solution ObjectModel into a BESSER quantum circuit.

Run from the project root (after T1):
    python transformations/t2_solution_to_quantum.py
    python transformations/t2_solution_to_quantum.py --qubo-file transformations/generated/t1-result-....py
    python transformations/t2_solution_to_quantum.py --depth 2 --gammas 0.1 0.2 --betas 0.3 0.4

Solver parameters are read from transformations/solver_config.json by default.
Explicit CLI arguments override the corresponding JSON settings.
T2 only generates a quantum MODEL; it never executes Qiskit or finds a solution.

References next to the rules: Lucas (2014) for QUBO/Ising and Farhi et al.
(2014) for the QAOA cost/mixer construction; Nielsen & Chuang (2010) for
implementing ZZ rotations with CX-RZ-CX.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
import math
from pathlib import Path
import runpy


GENERATED_DIR = Path(__file__).resolve().parent / "generated"
DEFAULT_CONFIG = Path(__file__).resolve().parent / "solver_config.json"


@dataclass(frozen=True)
class QuboData:
    names: tuple[str, ...]  # In the exact q[0], q[1], ... register order
    constant: float
    linear: dict[int, float]
    quadratic: dict[tuple[int, int], float]


@dataclass(frozen=True)
class IsingData:
    constant: float
    linear_z: dict[int, float]  # Coefficient of Z_i
    quadratic_zz: dict[tuple[int, int], float]  # Coefficient of Z_i Z_j


def object_attribute(obj, name: str):
    """Read the semantic attribute value of a BESSER object, not obj.name."""
    matches = [slot.value.value for slot in obj.slots if slot.attribute.name == name]
    if len(matches) != 1:
        raise ValueError(f"Expected one attribute {name!r} on {obj.name!r}")
    return matches[0]


def variable_order(name: str):
    """Keep project choices before budget-slack bits, in a reproducible order."""
    if name.startswith("x_"):
        return (0, name[2:])
    if name.startswith("s_") and name[2:].isdigit():
        return (1, int(name[2:]))
    return (2, name)


def read_qubo_model(model) -> QuboData:
    """Extract the mathematical QUBO solely from the Solution DSL ObjectModel."""
    of_type = lambda name: [o for o in model.objects if o.classifier.name == name]
    qubo_objects = of_type("QuboModel")
    if len(qubo_objects) != 1:
        raise ValueError(f"Expected one QuboModel; found {len(qubo_objects)}")

    variables = of_type("BinaryVariable")
    variables.sort(key=lambda obj: variable_order(object_attribute(obj, "name")))
    names = tuple(str(object_attribute(v, "name")) for v in variables)
    if not names or len(set(names)) != len(names):
        raise ValueError("The QUBO must have binary variables with distinct semantic names")
    index = {v: i for i, v in enumerate(variables)}

    linear: dict[int, float] = {}
    for term in of_type("LinearTerm"):
        i = index[term.linearVariable]
        if i in linear:
            raise ValueError(f"Duplicate linear coefficient for {names[i]}")
        linear[i] = float(object_attribute(term, "coefficient"))

    quadratic: dict[tuple[int, int], float] = {}
    for term in of_type("QuadraticTerm"):
        endpoints = list(term.variables)
        if len(endpoints) != 2:
            raise ValueError(f"Quadratic term {term.name} must reference exactly two variables")
        i, j = sorted((index[endpoints[0]], index[endpoints[1]]))
        if i == j or (i, j) in quadratic:
            raise ValueError(f"Repeated variable or quadratic term ({names[i]}, {names[j]})")
        quadratic[(i, j)] = float(object_attribute(term, "coefficient"))

    constant = float(object_attribute(qubo_objects[0], "constant"))
    if not all(math.isfinite(v) for v in (constant, *linear.values(), *quadratic.values())):
        raise ValueError("QUBO coefficients must be finite")
    return QuboData(names, constant, linear, quadratic)


def qubo_to_ising(qubo: QuboData) -> IsingData:
    """Lucas (2014): x_i = (1-Z_i)/2 and x_i*x_j = (1-Z_i-Z_j+Z_i*Z_j)/4.

    f(x) = c + sum_i a_i*x_i + sum_{i<j} b_ij*x_i*x_j
         = C + sum_i h_i*Z_i + sum_{i<j} J_ij*Z_i*Z_j.

    C = c + sum(a_i)/2 + sum(b_ij)/4
    h_i = -a_i/2 - sum_{j != i}(b_ij)/4
    J_ij = b_ij/4.
    """
    c = qubo.constant
    h = {i: 0.0 for i in range(len(qubo.names))}
    for i, a in qubo.linear.items():
        c += a / 2.0
        h[i] -= a / 2.0
    j_coefficients = {}
    for (i, j), b in qubo.quadratic.items():
        c += b / 4.0
        h[i] -= b / 4.0
        h[j] -= b / 4.0
        j_coefficients[(i, j)] = b / 4.0
    return IsingData(c, h, j_coefficients)


def make_solver_config(depth: int, gammas: list[float], betas: list[float], cost_scale: str) -> dict:
    """Validate the explicit QAOA solver settings supplied by the command line."""
    if type(depth) is not int or depth <= 0:
        raise ValueError("Solver 'depth' must be a positive integer")
    for key, angles in (("gammas", gammas), ("betas", betas)):
        if not isinstance(angles, list) or len(angles) != depth:
            raise ValueError(f"Solver '{key}' must have {depth} angles")
        if any(type(angle) not in (int, float) or not math.isfinite(angle) for angle in angles):
            raise ValueError(f"Solver '{key}' must contain finite numbers")
    if cost_scale not in ("none", "max_abs"):
        raise ValueError("Solver 'cost_scale' must be 'none' or 'max_abs'")
    return {"depth": depth, "gammas": gammas, "betas": betas, "cost_scale": cost_scale}


def read_solver_config(path: Path) -> dict:
    """Validate the JSON solver configuration before generating any circuit."""
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Missing solver configuration: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(config, dict):
        raise ValueError("Solver configuration must be a JSON object")
    expected = {"depth", "gammas", "betas", "cost_scale", "shots"}
    if set(config) != expected:
        raise ValueError(
            f"Solver configuration must contain exactly {sorted(expected)}; "
            f"missing={sorted(expected - set(config))}, extra={sorted(set(config) - expected)}"
        )
    validated = make_solver_config(
        config["depth"], config["gammas"], config["betas"], config["cost_scale"]
    )
    shots = config["shots"]
    if type(shots) is not int or shots <= 0:
        raise ValueError("Solver 'shots' must be a positive integer")
    return {**validated, "shots": shots}


def emit_quantum_model(qubo: QuboData, ising: IsingData, config: dict, source_file: Path) -> str:
    """Emit Python defining a BESSER quantum ObjectModel, without running a simulator."""
    n = len(qubo.names)
    coeffs = [abs(v) for v in (*ising.linear_z.values(), *ising.quadratic_zz.values())]
    scale = max([1.0, *coeffs]) if config["cost_scale"] == "max_abs" else 1.0
    depth = config["depth"]
    operations = [
        "from besser.BUML.metamodel.quantum import (",
        "    QuantumCircuit, QuantumRegister, ClassicalRegister,",
        "    HadamardGate, PauliXGate, RZGate, RXGate, Measurement",
        ")",
        "",
        "# T2 traceability: Lucas (2014); Farhi et al. (2014); Nielsen & Chuang (2010).",
        f"qubo_variable_names = {list(qubo.names)!r}",
        f"source_qubo_file = {source_file.name!r}",
        f"qaoa_depth = {depth}",
        f"solver_shots = {config['shots']}",
        f"ising_energy_scale = {scale!r}",
        "# The constant Ising term contributes only a global phase and can be omitted.",
        f"ising_constant = {ising.constant!r}",
        "",
        "qc = QuantumCircuit('Knapsack_QAOA')",
        f"q_reg = QuantumRegister('q', {n})",
        f"c_reg = ClassicalRegister('c', {n})",
        "qc.add_qreg(q_reg)",
        "qc.add_creg(c_reg)",
        "",
        "# Rule 1 (Farhi et al., 2014): uniform initial superposition",
    ]
    for i in range(n):
        operations.append(f"qc.add_operation(HadamardGate(target_qubit={i}))")

    for layer in range(depth):
        gamma = config["gammas"][layer]
        beta = config["betas"][layer]
        operations += [
            "",
            f"# Rule 2 (Lucas, 2014): QAOA cost layer {layer + 1}/{depth}",
            f"# Effective gamma = gamma[{layer}] / energy_scale = {gamma / scale!r}",
            "# RZ(theta) = exp(-i*theta*Z/2); theta = 2*gamma*h_i/scale",
        ]
        for i, h_i in sorted(ising.linear_z.items()):
            if h_i != 0:
                theta = 2 * gamma * h_i / scale
                operations.append(f"qc.add_operation(RZGate(target_qubit={i}, theta={theta!r}))")
        operations += [
            "# Rule 3 (Nielsen & Chuang, 2010): exp(-i*gamma*J_ij*Z_i*Z_j/scale)",
            "# Implement each ZZ rotation as CX(i,j) - RZ(j, 2*gamma*J_ij/scale) - CX(i,j)",
        ]
        for (i, j), j_ij in sorted(ising.quadratic_zz.items()):
            if j_ij != 0:
                theta = 2 * gamma * j_ij / scale
                operations.append(f"qc.add_operation(PauliXGate(target_qubit={j}, control_qubits=[{i}]))")
                operations.append(f"qc.add_operation(RZGate(target_qubit={j}, theta={theta!r}))")
                operations.append(f"qc.add_operation(PauliXGate(target_qubit={j}, control_qubits=[{i}]))")
        operations += ["# Rule 4 (Farhi et al., 2014): mixer exp(-i*beta*sum(X_i))"]
        for i in range(n):
            operations.append(f"qc.add_operation(RXGate(target_qubit={i}, theta={2 * beta!r}))")

    operations += ["", "# Rule 5: measurement (bit i corresponds to qubo_variable_names[i])"]
    for i in range(n):
        operations.append(f"qc.add_operation(Measurement(target_qubit={i}, output_bit={i}))")
    return "\n".join(operations) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--qubo-file", type=Path, help="Explicit T1-generated .py input (recommended)")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG,
                        help="Path to JSON solver configuration")
    parser.add_argument("--depth", type=int, help="Override QAOA depth from JSON")
    parser.add_argument("--gammas", type=float, nargs="+", help="One gamma per QAOA layer")
    parser.add_argument("--betas", type=float, nargs="+", help="One beta per QAOA layer")
    parser.add_argument("--cost-scale", choices=("none", "max_abs"),
                        help="Override cost scale from JSON")
    parser.add_argument("--output", type=Path, default=GENERATED_DIR / "quantum_instance.py")
    args = parser.parse_args()

    source = args.qubo_file
    if source is None:
        candidates = list(GENERATED_DIR.glob("t1-result-*.py"))
        if not candidates:
            parser.error("No T1 result in transformations/generated/. Run T1 first")
        source = max(candidates, key=lambda p: p.stat().st_mtime_ns)
    source = source.resolve()
    if not source.is_file():
        parser.error(f"Cannot read {source}")

    # runpy loads the actual BESSER Solution DSL ObjectModel. This is not a
    # replacement QUBO parser: the transformation reads the model's objects.
    model = runpy.run_path(str(source)).get("object_model")
    if model is None:
        raise ValueError(f"No BESSER object_model exported by {source}")
    qubo = read_qubo_model(model)
    ising = qubo_to_ising(qubo)
    try:
        json_config = read_solver_config(args.config)
        depth = args.depth if args.depth is not None else json_config["depth"]
        gammas = args.gammas if args.gammas is not None else json_config["gammas"]
        betas = args.betas if args.betas is not None else json_config["betas"]
        cost_scale = args.cost_scale if args.cost_scale is not None else json_config["cost_scale"]
        config = {
            **make_solver_config(depth, gammas, betas, cost_scale),
            "shots": json_config["shots"],
        }
    except ValueError as exc:
        parser.error(str(exc))
    generated = emit_quantum_model(qubo, ising, config, source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(generated, encoding="utf-8")
    print(f"T2: {len(qubo.names)} qubits, p={config['depth']}, {len(ising.quadratic_zz)} ZZ terms")
    print(f"Solver config: {args.config.resolve()} | shots={config['shots']}")
    print(f"Qubit order: {', '.join(qubo.names)}")
    print(f"Generated BESSER quantum model: {args.output.resolve()}")


if __name__ == "__main__":
    main()
