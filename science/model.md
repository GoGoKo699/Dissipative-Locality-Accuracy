# Model and accuracy theorem

How accurately can autonomous dissipation stabilize a specified pure quantum state when each reservoir acts only on an allowed subsystem? We allow arbitrary coherent control on the whole system and optimize the dissipators themselves. The answer is controlled, within a factor of two, by the smallest eigenvalue of an allowed target marginal. If the stationary output must also be pure, that eigenvalue gives the exact optimum.

This page fixes the model and all optimization quantifiers. The [converse](converse.md) proves the error bounds and the geometric pure-state optimum. The [construction](construction.md) supplies an explicit generator and proves global attraction.

## Admissible generators

Fix a finite physical Hilbert space

```math
\mathcal H=\bigotimes_{i=1}^{n}\mathcal H_i,
\qquad 2\le \dim\mathcal H_i<\infty.
```

Let $`\mathcal N`$ be a nonempty family of nonempty subsets of $`\{1,\ldots,n\}`$. The family need not be translation invariant, geometrically local, or closed under taking subsets. It specifies the permitted supports of individual dissipative channels. A full-system support is allowed formally, although it makes the obstruction below vanish.

An admissible generator is a linear map that **admits at least one** finite Lindblad representation

```math
\mathcal L(\rho)
=-i[H,\rho]+\sum_{a=1}^{m}\mathcal D[J_a](\rho),
\qquad
\mathcal D[J](\rho)
=J\rho J^\dagger-\frac12\{J^\dagger J,\rho\},
```

```math
H=H^\dagger,
\qquad
J_a=A_{a,S_a}\otimes I_{S_a^c},
\qquad S_a\in\mathcal N.
```

The Hamiltonian is an arbitrary finite Hermitian operator on $`\mathcal H`$. There is no restriction on its interaction support. The finite number of jumps, their allowed support choices, and their strengths are free; positive rates can be absorbed into the matrices $`A_{a,S_a}`$. An operator supported on a smaller set is permitted whenever it can be written as an operator on some allowed $`S_a`$ tensored with the identity outside that set.

The existence quantifier over representations matters. Unitary mixing of Lindblad channels can turn a local representation into one whose displayed jumps have larger supports. Admissibility requires a representation of the stated form, not locality of every equivalent representation. All converse proofs choose one admissible representation and apply to the generator it defines.

The physical Hilbert space is fixed throughout. The generator is time independent, and no auxiliary register or additional local level is supplied. Locality concerns the effective Lindblad jumps. Local microscopic system–bath couplings alone do not guarantee this condition after an effective generator is derived. In particular, a collective jump written as a sum of operators on different subsystems is not automatically a channel on either individual subsystem; membership in the class requires an admissible representation of the full generator.

## The target invariant

Fix a normalized pure target $`|\psi\rangle`$, and write

```math
\psi=|\psi\rangle\langle\psi|,
\qquad
\psi_S=\operatorname{Tr}_{S^c}\psi.
```

Define

```math
\boxed{
\mu_{\mathcal N}(\psi)
=\min_{S\in\mathcal N}\lambda_{\min}(\psi_S).
}
```

The minimum eigenvalue is taken on the **entire** local Hilbert space $`\mathcal H_S`$, including zero eigenvalues. It is not the smallest nonzero Schmidt weight. In particular,

```math
0\le\mu_{\mathcal N}(\psi)\le\frac12.
```

The upper bound follows because every allowed subsystem has dimension at least two and each marginal has unit trace. The invariant is positive precisely when every allowed marginal is full rank. If an allowed subsystem has dimension larger than its complement, its pure-state marginal is necessarily rank deficient, and the invariant vanishes.

The [pure-state geometry](converse.md#the-exact-pure-state-optimum) gives a useful interpretation: $`\mu_{\mathcal N}(\psi)`$ is the least pure-target infidelity needed to reach a pure state with a rank-deficient marginal on at least one allowed support.

## The stationary optimization

A stationary state satisfies $`\mathcal L(\rho_*)=0`$. It is globally attractive if every initial density operator converges to it in trace norm:

```math
\lim_{t\to\infty}
\left\|e^{t\mathcal L}(\rho_0)-\rho_*\right\|_1=0
\qquad\text{for every density operator }\rho_0.
```

A globally attractive stationary state is necessarily unique. We nevertheless state uniqueness explicitly when describing the optimization and construction. The target fidelity convention is

```math
F_\psi(\rho)=\langle\psi|\rho|\psi\rangle,
\qquad
\epsilon_\psi(\rho)=1-F_\psi(\rho).
```

Thus $`F_\psi`$ is the squared Uhlmann fidelity when one argument is pure. The target need not be an eigenvector of $`\rho`$.

Let $`\mathfrak G_{\mathcal N}^{\mathrm{att}}`$ denote the admissible generators having a unique globally attractive stationary state $`\rho_{\mathcal L}`$. Define

```math
\epsilon_{\mathrm{opt}}(\psi,\mathcal N)
=\inf_{\mathcal L\in\mathfrak G_{\mathcal N}^{\mathrm{att}}}
\left[1-\langle\psi|\rho_{\mathcal L}|\psi\rangle\right].
```

Restricting the same optimization to pure stationary outputs defines

```math
\epsilon_{\mathrm{pure,opt}}(\psi,\mathcal N)
=\inf_{\substack{\mathcal L\in\mathfrak G_{\mathcal N}^{\mathrm{att}}\\
\operatorname{rank}\rho_{\mathcal L}=1}}
\left[1-\langle\psi|\rho_{\mathcal L}|\psi\rangle\right].
```

Both classes are nonempty: the construction below gives a pure attractive output for every target and every allowed family in this model.

## Accuracy theorem

For every target and allowed family as above,

```math
\boxed{
\frac12\mu_{\mathcal N}(\psi)
\le\epsilon_{\mathrm{opt}}(\psi,\mathcal N)
\le\mu_{\mathcal N}(\psi)
=\epsilon_{\mathrm{pure,opt}}(\psi,\mathcal N).
}
```

The individual assertions have different strengths:

1. **Converse for all stationary states.** If an admissible representation contains at least one nonscalar jump, every stationary density operator has infidelity at least $`\mu_{\mathcal N}(\psi)/2`$. This statement does not require uniqueness or attraction. The nonscalar condition is essential here: a purely Hamiltonian generator can have an arbitrary pure eigenstate as a stationary state. Such a generator cannot have a globally attractive state on the nontrivial Hilbert space considered here.

2. **Exact pure-output optimum.** Every pure stationary output of a generator with a nonscalar admissible jump has infidelity at least $`\mu_{\mathcal N}(\psi)`$. A pure globally attractive output attains this value.

3. **Explicit attainment of the upper bound.** One supported local reset jump with operator norm one and an explicit global Hamiltonian with $`\|H\|<2h`$, for any chosen $`h>0`$, suffice to attain infidelity $`\mu_{\mathcal N}(\psi)`$. No limiting sequence of control strengths is needed.

4. **Exact-stabilization boundary.** The target itself is an admissible pure globally attractive stationary state if and only if $`\mu_{\mathcal N}(\psi)=0`$. The same construction covers this endpoint without adding an ancilla.

The [converse proof](converse.md) establishes the first two statements and the necessary part of the fourth. The [construction and attraction proof](construction.md) establish the remaining assertions. In particular, for $`\mu_{\mathcal N}(\psi)>0`$, allowing mixed outputs can improve the optimum over pure outputs by at most a factor of two.

## Meaning and scope of the optimum

The theorem quantifies stationary accuracy under unrestricted coherent control. The converse therefore remains valid when the Hamiltonian is further restricted. The matching upper bound specifically uses the full freedom to choose a global, target-dependent Hamiltonian; it does not establish attainability with a local Hamiltonian.

No rate budget is needed for the stationary error bound. Multiplying a generator by a positive constant changes its time scale and leaves its stationary states unchanged. The model does not optimize preparation time, and the explicit Hamiltonian can require an exponentially large description in the number of physical sites. Its bounded operator norm is not a statement of efficient implementation. These resource distinctions are developed in [resources](resources.md).

The factor-two interval is a uniform characterization, not a claim that its lower constant is sharp. In particular, exact two-qubit local-cooling optima can be stricter; see [Žnidarič's analysis](../references/RELATED_WORK.md#znidaric2015). The [consequences](consequences.md) translate the invariant into precision laws for uniform and Haar-random targets.

The proof uses established [spectral population-balance conditions](../references/RELATED_WORK.md#linowski2023), the [local marginal rank obstruction](../references/RELATED_WORK.md#karuvade2018), and the setting of [Hamiltonian-assisted stabilization](../references/RELATED_WORK.md#ticozzi2009). The ordinary-fidelity bound, geometric optimum, and explicit construction are proved in full in the following pages, with the imported ingredients identified where they enter.
