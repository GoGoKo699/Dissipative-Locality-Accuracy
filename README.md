# Dissipative Locality and Accuracy

**How accurately can local reservoirs stabilize a quantum state when coherent control is unrestricted?** This project characterizes the best stationary approximation to an arbitrary pure target through the spectra of its local reduced states.

Fix a pure target $`|\psi\rangle`$ and a nonempty family $`\mathcal N`$ of allowed reservoir supports. Every effective Lindblad jump must act within one allowed support. The dynamics are time independent, the Hamiltonian may act globally, and no additional ancillas are supplied. Define

```math
\mu_{\mathcal N}(\psi)
=\min_{S\in\mathcal N}\lambda_{\min}(\psi_S),
\qquad
\psi_S=\operatorname{Tr}_{S^c}|\psi\rangle\langle\psi|.
```

The eigenvalue minimum includes zeros. For ordinary target infidelity $`\epsilon=1-\langle\psi|\rho_*|\psi\rangle`$, optimize over generators with a unique globally attractive stationary state. Then

```math
\boxed{
\frac{\mu_{\mathcal N}(\psi)}2
\le\epsilon_{\mathrm{opt}}(\psi,\mathcal N)
\le\mu_{\mathcal N}(\psi)
=\epsilon_{\mathrm{pure,opt}}(\psi,\mathcal N).
}
```

Allowing a mixed steady state can improve infidelity over the best pure steady state by at most a factor of two. The pure optimum is attained by removing one least-weight Schmidt component and using one supported reset channel with an explicit global Hamiltonian. The original target is exactly stabilizable in this model precisely when at least one allowed marginal has a zero eigenvalue.

| Result | Meaning |
|---|---|
| Universal stationary error bound | The converse allows arbitrary coherent strength, arbitrary channel strengths and a mixed stationary output whose eigenvectors may differ from the target. |
| Exact pure-output optimum | The least achievable pure-output error equals the distance to the set of pure states with a rank-deficient allowed marginal. |
| Explicit attractive construction | One local reset and a global path Hamiltonian attain the pure optimum; positivity proves uniqueness and convergence. |
| Finite-accuracy support law | For qubit targets with maximally mixed allowed marginals and largest support size $`k`$, the optimal error lies between $`2^{-k-1}`$ and $`2^{-k}`$. A corresponding Haar statement holds well below half-system support. |

Exact local-rank obstructions, spectral population balance and Hamiltonian-assisted attraction are [established ingredients](references/RELATED_WORK.md). The contribution is the quantitative target-dependent characterization of ordinary stationary fidelity, including the comparison between pure and mixed outputs. The general lower bound is not claimed to give the exact optimal coefficient for every target.

## Read the science

Begin with the [model, conventions and exact theorem](science/model.md), then follow the [stationary-state converse](science/converse.md) and the [attaining construction](science/construction.md). The examples and consequences connect the mathematical invariant to reservoir support and finite accuracy.

| To inspect | Read |
|---|---|
| Allowed dynamics, representations, attraction and fidelity convention | [Model and accuracy theorem](science/model.md) |
| Population balance, moving stationary eigenvectors and the pure-state distance | [Converse and geometry](science/converse.md) |
| One reset, an explicit Hamiltonian, uniqueness and global attraction | [Construction](science/construction.md) |
| Product, Bell, GHZ and graph-state boundaries | [Examples](science/examples.md) |
| Uniform marginals, the Haar probability estimate and accuracy requirements | [Consequences](science/consequences.md) |
| Hamiltonian control, effective jump locality and preparation resources | [Resource interpretation](science/resources.md) |
| Closest results and inherited proof ingredients | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Reproducible checks and the scope of numerical evidence | [Verification](verification/README.md) |

The [LLM reading guide](llms.txt) maps questions to these authoritative files.

## Reproduce the finite checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/verify.py
```

The suite checks finite construction instances and structured marginal examples. The written proofs establish the universal converse, exact pure optimum and global-attraction theorem; finite spectra do not establish an asymptotic mixing law.

## Scope and interpretation

The converse remains valid when the Hamiltonian is restricted further. The attaining construction uses a target-dependent global Hamiltonian whose description can be exponentially large, and no efficient synthesis or useful general preparation-time bound is established. A small Hamiltonian operator norm does not remove those costs.

The support assumption concerns the actual effective jump operators. Microscopic local bath couplings, collective sums, auxiliary reset systems and jumps with decaying spatial tails can produce different admissible dynamics. The theorem concerns stabilization on the specified physical system under the [stated model](science/model.md).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
