#!/usr/bin/env python3
"""Reproduce finite checks of the local-dissipation stabilization construction.

The analytic proof supplies the universal theorem. These checks address tensor
ordering, complex conjugation, rank-deficient marginals, and the spectrum of
seven concrete generators. No optimization over generators is performed.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import eigvals


SEED = 1126
ALGEBRA_TOL = 1e-10
ZERO_EIGENVALUE_TOL = 1e-8
DECAY_TOL = 1e-9


def require(condition: bool, message: str) -> None:
    """Keep checks active even when Python is invoked with -O."""
    if not condition:
        raise AssertionError(message)


def support_order(dims: tuple[int, ...], support: tuple[int, ...]):
    require(len(set(support)) == len(support), "Repeated support index")
    require(0 < len(support) <= len(dims), "Support must be nonempty")
    require(all(0 <= i < len(dims) for i in support), "Invalid support index")
    support = tuple(sorted(support))
    complement = tuple(i for i in range(len(dims)) if i not in support)
    order = support + complement
    ds = int(np.prod([dims[i] for i in support]))
    dr = int(np.prod([dims[i] for i in complement]))
    require(ds >= 2, "Supported Hilbert-space dimension must be at least two")
    return support, complement, order, ds, dr


def reduced_state(psi, dims, support):
    """Physical basis uses C order: the first tensor factor varies slowest."""
    _, _, order, ds, dr = support_order(dims, support)
    matrix = psi.reshape(dims).transpose(order).reshape(ds, dr)
    marginal = matrix @ matrix.conj().T
    return (marginal + marginal.conj().T) / 2


def reference_reduced_state(psi, dims, support):
    """Independent index-loop partial trace, without tensor transposition."""
    support = tuple(sorted(support))
    complement = tuple(i for i in range(len(dims)) if i not in support)
    local_dims = tuple(dims[i] for i in support)
    coordinates = list(np.ndindex(dims))
    local_indices = [
        np.ravel_multi_index(tuple(c[i] for i in support), local_dims)
        for c in coordinates
    ]
    ds = int(np.prod(local_dims))
    marginal = np.zeros((ds, ds), dtype=complex)
    for i, ci in enumerate(coordinates):
        for j, cj in enumerate(coordinates):
            if all(ci[k] == cj[k] for k in complement):
                marginal[local_indices[i], local_indices[j]] += (
                    psi[i] * psi[j].conjugate()
                )
    return marginal


def embed_supported(local_operator, dims, support):
    """Embed A_S tensor I, including supports whose sites are not adjacent."""
    _, _, order, ds, dr = support_order(dims, support)
    require(local_operator.shape == (ds, ds), "Wrong local operator dimension")
    dim = ds * dr
    indices = np.arange(dim).reshape(dims).transpose(order).reshape(-1)
    embedded = np.empty((dim, dim), dtype=complex)
    embedded[np.ix_(indices, indices)] = np.kron(local_operator, np.eye(dr))
    return embedded


def reference_supported(local_operator, dims, support):
    """Independent matrix-element definition of a supported operator."""
    support = tuple(sorted(support))
    complement = tuple(i for i in range(len(dims)) if i not in support)
    local_dims = tuple(dims[i] for i in support)
    coordinates = list(np.ndindex(dims))
    local_indices = [
        np.ravel_multi_index(tuple(c[i] for i in support), local_dims)
        for c in coordinates
    ]
    dim = int(np.prod(dims))
    result = np.zeros((dim, dim), dtype=complex)
    for i, ci in enumerate(coordinates):
        for j, cj in enumerate(coordinates):
            if all(ci[k] == cj[k] for k in complement):
                result[i, j] = local_operator[local_indices[i], local_indices[j]]
    return result


def fix_phase(vector):
    pivot = vector[int(np.argmax(np.abs(vector)))]
    return vector * pivot.conjugate() / abs(pivot)


def orthonormal_columns(candidates, count):
    """Fixed-order, twice-reorthogonalized Gram-Schmidt in a known subspace."""
    columns = []
    for candidate in candidates:
        vector = np.asarray(candidate, dtype=complex).copy()
        for _ in range(2):
            for column in columns:
                vector -= column * np.vdot(column, vector)
        norm = np.linalg.norm(vector)
        if norm > ALGEBRA_TOL:
            columns.append(vector / norm)
        if len(columns) == count:
            return np.column_stack(columns)
    raise AssertionError("Candidates did not span the required subspace")


def construct(psi, dims, supports):
    """Schmidt truncation, one supported reset, and a global Jacobi chain."""
    require(len(dims) > 0 and all(d >= 2 for d in dims), "Invalid physical dimensions")
    require(len(supports) > 0, "Allowed support family is empty")
    dim = int(np.prod(dims))
    require(psi.shape == (dim,), "Wrong target dimension")
    require(abs(np.vdot(psi, psi).real - 1) < ALGEBRA_TOL, "Target not normalized")
    spectra = []
    for support in supports:
        values, vectors = np.linalg.eigh(reduced_state(psi, dims, support))
        spectra.append((float(values[0]), tuple(support), values, vectors))
    raw_mu, support, values, vectors = min(spectra, key=lambda item: item[0])
    require(raw_mu > -ALGEBRA_TOL, "Marginal has a significantly negative eigenvalue")
    mu = max(0.0, raw_mu)
    _, _, _, ds, dr = support_order(dims, support)

    discarded = fix_phase(vectors[:, 0])
    retained = fix_phase(vectors[:, -1])
    local_jump = np.outer(retained, discarded.conj())
    jump = embed_supported(local_jump, dims, support)
    projector = embed_supported(np.outer(discarded, discarded.conj()), dims, support)
    phi = psi - projector @ psi
    phi /= np.linalg.norm(phi)
    first = jump.conj().T @ phi
    require(np.linalg.norm(first) > ALGEBRA_TOL, "Reset has no influx into target")
    first /= np.linalg.norm(first)

    identity = np.eye(dim)
    # Every chain vector must be an eigenvector of L^dagger L. The active
    # subspace starts with first; the dark subspace starts with phi, which is
    # omitted from the chain. Projector columns make the choice deterministic.
    active = orthonormal_columns([first, *projector.T], dr)
    dark = orthonormal_columns([phi, *(identity - projector).T], dim - dr)
    basis = np.column_stack([active, dark[:, 1:]])
    chain = np.diag(np.ones(dim - 2), 1) + np.diag(np.ones(dim - 2), -1)
    hamiltonian = basis @ chain @ basis.conj().T
    return {
        "support": support,
        "ds": ds,
        "dr": dr,
        "mu": mu,
        "raw_mu": raw_mu,
        "marginal_eigenvalues": values,
        "phi": phi,
        "local_jump": local_jump,
        "jump": jump,
        "projector": projector,
        "basis": basis,
        "hamiltonian": hamiltonian,
    }


def lindblad_matrix(hamiltonian, jump):
    """Column-major vectorization: vec(A rho B)=(B^T tensor A) vec(rho)."""
    identity = np.eye(hamiltonian.shape[0])
    loss = jump.conj().T @ jump
    return (
        -1j * (np.kron(identity, hamiltonian) - np.kron(hamiltonian.T, identity))
        + np.kron(jump.conj(), jump)
        - (np.kron(identity, loss) + np.kron(loss.T, identity)) / 2
    )


def verify_construction(name, psi, dims, supports, expected_rank, probe_seed):
    built = construct(psi, dims, supports)
    phi, jump = built["phi"], built["jump"]
    projector, basis = built["projector"], built["basis"]
    hamiltonian = built["hamiltonian"]
    dim, dr = len(psi), built["dr"]
    fixed_point = np.outer(phi, phi.conj())
    generator = lindblad_matrix(hamiltonian, jump)

    rng = np.random.default_rng(probe_seed)
    matrix = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
    probe = (matrix + matrix.conj().T) / 2
    probe /= np.linalg.norm(probe)
    loss = jump.conj().T @ jump
    direct = (
        -1j * (hamiltonian @ probe - probe @ hamiltonian)
        + jump @ probe @ jump.conj().T
        - (loss @ probe + probe @ loss) / 2
    )
    vectorized = (generator @ probe.reshape(-1, order="F")).reshape(
        (dim, dim), order="F"
    )
    diagonal = np.diag([1.0] * dr + [0.0] * (dim - dr - 1))
    residuals = {
        "partial_trace_reference": float(np.linalg.norm(
            reduced_state(psi, dims, built["support"])
            - reference_reduced_state(psi, dims, built["support"])
        )),
        "supported_jump_reference": float(np.linalg.norm(
            jump - reference_supported(built["local_jump"], dims, built["support"])
        )),
        "jump_loss_projector": float(np.linalg.norm(loss - projector)),
        "basis_orthonormality": float(np.linalg.norm(basis.conj().T @ basis - np.eye(dim - 1))),
        "basis_completeness": float(np.linalg.norm(basis @ basis.conj().T + fixed_point - np.eye(dim))),
        "basis_projector_diagonal": float(np.linalg.norm(basis.conj().T @ projector @ basis - diagonal)),
        "dark_jump": float(np.linalg.norm(jump @ phi)),
        "dark_hamiltonian": float(np.linalg.norm(hamiltonian @ phi)),
        "hamiltonian_hermiticity": float(np.linalg.norm(hamiltonian - hamiltonian.conj().T)),
        "stationarity": float(np.linalg.norm(generator @ fixed_point.reshape(-1, order="F"))),
        "trace_preservation": float(np.linalg.norm(np.eye(dim).reshape(-1, order="F") @ generator)),
        "vectorization_reference": float(np.linalg.norm(vectorized - direct)),
        "hermiticity_preservation": float(np.linalg.norm(vectorized - vectorized.conj().T)),
    }
    for label, residual in residuals.items():
        require(residual < ALGEBRA_TOL, f"{name}: {label} residual {residual}")

    infidelity = float(1 - abs(np.vdot(psi, phi)) ** 2)
    require(abs(infidelity - built["mu"]) < ALGEBRA_TOL, f"{name}: wrong infidelity")
    marginal_rank = int(np.count_nonzero(built["marginal_eigenvalues"] > ALGEBRA_TOL))
    require(marginal_rank == expected_rank, f"{name}: wrong marginal rank")
    h_norm = float(np.linalg.norm(hamiltonian, 2))
    jump_norm = float(np.linalg.norm(jump, 2))
    require(h_norm < 2 + ALGEBRA_TOL, f"{name}: Hamiltonian norm exceeds two")
    require(abs(h_norm - 2 * np.cos(np.pi / dim)) < ALGEBRA_TOL,
            f"{name}: wrong path-Hamiltonian norm")
    require(abs(jump_norm - 1) < ALGEBRA_TOL, f"{name}: jump norm is not one")

    eigenvalues = eigvals(generator, check_finite=True)
    zero = abs(eigenvalues) < ZERO_EIGENVALUE_TOL
    require(int(zero.sum()) == 1, f"{name}: expected exactly one zero eigenvalue")
    largest_other_real = float(np.max(eigenvalues[~zero].real))
    require(largest_other_real < -DECAY_TOL, f"{name}: nondecaying nonzero mode")
    if expected_rank < built["ds"]:
        require(np.linalg.norm(fixed_point - np.outer(psi, psi.conj())) < ALGEBRA_TOL,
                f"{name}: rank-deficient target was not stabilized exactly")

    return {
        "name": name,
        "dimensions": list(dims),
        "allowed_supports_zero_based": [list(s) for s in supports],
        "selected_support_zero_based": list(built["support"]),
        "support_dimension": built["ds"],
        "complement_dimension": built["dr"],
        "selected_marginal_rank": marginal_rank,
        "mu_numeric": built["mu"],
        "mu_before_roundoff_clipping": built["raw_mu"],
        "constructed_infidelity": infidelity,
        "hamiltonian_norm": h_norm,
        "jump_norm": jump_norm,
        "generator_dimension": dim * dim,
        "zero_eigenvalue_count": int(zero.sum()),
        "zero_eigenvalue_modulus": float(np.max(abs(eigenvalues[zero]))),
        "spectral_gap_numeric": -largest_other_real,
        "residuals": residuals,
    }


def verify_marginal_example(name, psi, dims, supports, expected_spectrum):
    records = []
    maximum_error = 0.0
    for support in supports:
        marginal = reduced_state(psi, dims, support)
        reference = reference_reduced_state(psi, dims, support)
        require(np.linalg.norm(marginal - reference) < ALGEBRA_TOL,
                f"{name}: partial trace disagrees with independent reference")
        spectrum = np.linalg.eigvalsh(marginal)
        error = float(np.max(abs(spectrum - expected_spectrum)))
        maximum_error = max(maximum_error, error)
        require(error < ALGEBRA_TOL, f"{name}: wrong marginal spectrum")
        records.append({"support_zero_based": list(support), "spectrum": spectrum.tolist()})
    mu = float(min(expected_spectrum))
    return {
        "name": name,
        "dimensions": list(dims),
        "mu_exact": mu,
        "stationary_infidelity_interval": [mu / 2, mu],
        "pure_output_optimum": mu,
        "maximum_spectrum_error": maximum_error,
        "marginals": records,
    }


def cycle_five_state_and_exact_checks():
    """Exact integer checks of the ring graph state; no floating-point verdict."""
    n = 5
    dims = (2,) * n
    coordinates = list(np.ndindex(dims))
    signs = np.array([
        (-1) ** sum(bits[i] * bits[(i + 1) % n] for i in range(n))
        for bits in coordinates
    ], dtype=np.int64)
    pairs = list(itertools.combinations(range(n), 2))
    for support in pairs:
        _, _, order, ds, dr = support_order(dims, support)
        matrix = signs.reshape(dims).transpose(order).reshape(ds, dr)
        require(np.array_equal(matrix @ matrix.T, dr * np.eye(ds, dtype=np.int64)),
                f"C5: nonuniform exact marginal on {support}")

    for vertex in range(n):
        for index, bits in enumerate(coordinates):
            flipped = list(bits)
            flipped[vertex] ^= 1
            destination = np.ravel_multi_index(tuple(flipped), dims)
            phase = (-1) ** (bits[(vertex - 1) % n] + bits[(vertex + 1) % n])
            require(signs[destination] == phase * signs[index], "C5: wrong stabilizer sign")

    weights = {weight: 0 for weight in range(n + 1)}
    for mask in range(1 << n):
        x = [(mask >> j) & 1 for j in range(n)]
        z = [x[(j - 1) % n] ^ x[(j + 1) % n] for j in range(n)]
        weight = sum(bool(xj or zj) for xj, zj in zip(x, z))
        weights[weight] += 1
    require(weights == {0: 1, 1: 0, 2: 0, 3: 10, 4: 15, 5: 6},
            "C5: unexpected stabilizer weight distribution")
    return signs.astype(complex) / np.sqrt(2**n), {
        "arithmetic": "int64; all values are small integers",
        "two_site_gram_matrices_checked": len(pairs),
        "stabilizer_generators_checked": n,
        "stabilizer_weight_distribution": {str(k): v for k, v in weights.items()},
        "minimum_nonidentity_stabilizer_weight": 3,
        "all_two_site_marginals_equal_identity_over_four": True,
    }


def random_complex_state(dims, seed):
    rng = np.random.default_rng(seed)
    dim = int(np.prod(dims))
    vector = rng.normal(size=dim) + 1j * rng.normal(size=dim)
    return vector / np.linalg.norm(vector)


def run():
    product = np.kron(np.kron(
        np.array([1, 1j]) / np.sqrt(2),
        np.array([np.sqrt(0.7), np.exp(0.4j) * np.sqrt(0.3)]),
    ), np.array([np.cos(0.31), np.exp(0.71j) * np.sin(0.31)]))
    bell = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    ghz = np.zeros(16, dtype=complex)
    ghz[[0, -1]] = 1 / np.sqrt(2)
    cycle, exact_cycle = cycle_five_state_and_exact_checks()
    singles = lambda n: [(j,) for j in range(n)]
    pairs = lambda n: list(itertools.combinations(range(n), 2))

    examples = [
        verify_marginal_example("product_3_qubits", product, (2, 2, 2), singles(3), [0, 1]),
        verify_marginal_example("bell_2_qubits", bell, (2, 2), singles(2), [0.5, 0.5]),
        verify_marginal_example("ghz_4_single_sites", ghz, (2,) * 4, singles(4), [0.5, 0.5]),
        verify_marginal_example("ghz_4_pairs", ghz, (2,) * 4, pairs(4), [0, 0, 0.5, 0.5]),
        verify_marginal_example("cycle_5_pairs", cycle, (2,) * 5, pairs(5), [0.25] * 4),
    ]

    full_dims = (2, 4, 2)
    deficient_dims = (2, 3, 2)
    full = random_complex_state(full_dims, SEED)
    deficient = random_complex_state(deficient_dims, SEED + 1)
    separated_family = [(0,), (2,), (0, 2)]
    specifications = [
        ("product_3_qubits", product, (2, 2, 2), singles(3), 1),
        ("bell_2_qubits", bell, (2, 2), singles(2), 2),
        ("ghz_4_single_sites", ghz, (2,) * 4, singles(4), 2),
        ("ghz_4_pairs", ghz, (2,) * 4, pairs(4), 2),
        ("complex_full_rank_separated_support", full, full_dims, separated_family, 4),
        ("complex_rank_deficient_larger_support", deficient, deficient_dims, separated_family, 3),
        ("single_qubit_full_support", np.array([1, 1j]) / np.sqrt(2), (2,), [(0,)], 1),
    ]
    constructions = []
    for index, specification in enumerate(specifications):
        result = verify_construction(*specification, probe_seed=SEED + 100 + index)
        if specification[0].startswith("complex_"):
            require(result["selected_support_zero_based"] == [0, 2],
                    "Separated support did not minimize the target marginal eigenvalue")
        constructions.append(result)

    return {
        "schema_version": 1,
        "status": "passed",
        "scope": "Finite construction checks and exact structured examples; not a proof or an optimization of the universal bound.",
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
        "seeds": {"full_rank_target": SEED, "rank_deficient_target": SEED + 1,
                  "operator_probes": [SEED + 100 + i for i in range(len(specifications))]},
        "tolerances": {"algebra": ALGEBRA_TOL, "zero_eigenvalue": ZERO_EIGENVALUE_TOL,
                       "strict_decay": DECAY_TOL},
        "structured_examples": examples,
        "cycle_5_exact_checks": exact_cycle,
        "construction_checks": constructions,
        "summary": {
            "structured_example_count": len(examples),
            "construction_count": len(constructions),
            "maximum_generator_dimension": max(c["generator_dimension"] for c in constructions),
            "maximum_algebra_residual": max(max(c["residuals"].values()) for c in constructions),
            "smallest_observed_spectral_gap": min(c["spectral_gap_numeric"] for c in constructions),
            "all_zero_modes_unique_and_other_modes_decaying": True,
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    parser.add_argument("--no-write", action="store_true", help="Run checks without changing results.json")
    args = parser.parse_args()
    results = run()
    if not args.no_write:
        args.output.write_text(json.dumps(results, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": results["status"], **results["summary"]}, indent=2))


if __name__ == "__main__":
    main()
