# Resources and physical scope

[Model and theorem](model.md) · [Converse](converse.md) · [Construction](construction.md) · [Consequences](consequences.md)

The accuracy law isolates one restriction: every dissipative jump must act on one allowed region of a fixed physical tensor decomposition. The coherent Hamiltonian and the choice of those local dissipators are otherwise unrestricted. This makes the result a stationary feasibility theorem. Its construction does not establish an efficient many-body preparation algorithm.

## What is fixed and what is optimized

| Quantity | Assumption |
|---|---|
| Physical system | A fixed finite tensor product; no additional retained degrees of freedom |
| Target | A specified normalized pure state; the generator may depend on its full description |
| Allowed dissipative supports | A nonempty family of nonempty regions, each with Hilbert-space dimension at least two; proper supports are the intended locality regime |
| Effective jumps | An admissible representation with each jump supported on one allowed region |
| Coherent control | An arbitrary finite, time-independent global Hermitian Hamiltonian |
| Dissipative strengths and number | Arbitrary finite choices; positive rates are absorbed into the jump matrices |
| Main optimized output | A unique globally attractive stationary state, possibly mixed |
| Error | $`1-\langle\psi\vert\rho_*\vert\psi\rangle`$ |
| Preparation time | Not optimized or bounded by the accuracy theorem |

The [converse](converse.md) also holds for every stationary state of a generator with at least one nonscalar admissible jump. It does not need uniqueness, attraction or a bound on the Hamiltonian. Scalar-only jumps must be excluded from that stronger statement: purely Hamiltonian dynamics can have an arbitrary prescribed pure eigenstate stationary, but cannot attract all initial states to it.

The formal theorem also allows a full-system support. Its marginal is the pure target itself, so its smallest eigenvalue is zero and exact stabilization is available. A positive locality obstruction therefore requires every allowed marginal to be full rank.

## Locality is a property of the generator

The admissible class consists of generators that **admit** a representation

```math
\mathcal L(\rho)
=-i[H,\rho]+\sum_a\mathcal D[J_a](\rho),
\qquad
J_a=A_{a,S_a}\otimes I_{S_a^c},
\quad S_a\in\mathcal N,
```

where

```math
\mathcal D[J](\rho)
=J\rho J^\dagger-\tfrac12\{J^\dagger J,\rho\}.
```

Lindblad representations are not unique. Unitarily mixing jump labels can give an equivalent representation whose displayed jumps have larger support. That change does not remove an already existing supported representation. Scalar centering, as used in the converse, preserves each supported tensor form and changes only an allowed Hamiltonian term. The bound therefore does not depend on assigning a norm cost to a particular gauge.

In contrast, a genuinely collective jump

```math
J=A\otimes I+I\otimes B
```

generally acts on the union of its two factors. Its dissipator includes interference terms and is not obtained by adding $`\mathcal D[A\otimes I]`$ and $`\mathcal D[I\otimes B]`$. It may fail to admit a representation supported separately on the two factors. The results for such collective local-sum jumps in [Pocklington and Clerk](../references/RELATED_WORK.md#pocklington2024) concern a different admissible class.

The support family can be geometrically disconnected or omit some sites entirely. The upper construction still works because its unrestricted Hamiltonian can couple the remaining degrees of freedom. Imposing spatial locality or a fixed native interaction set on the Hamiltonian would require a new achievability analysis; the current converse would continue to apply to that smaller class.

## Microscopic bath couplings and effective jumps

A local microscopic system–bath coupling does not, by itself, imply that the effective Lindblad jumps have the required support. In a weak-coupling derivation, a coupling operator $`A`$ is decomposed into energy-transition components of the system Hamiltonian:

```math
A(\omega)
=\sum_{E'-E=\omega}\Pi_E A\Pi_{E'}.
```

For an interacting global Hamiltonian, its spectral projectors $`\Pi_E`$ need not preserve the original support of $`A`$. The weak-coupling construction and this decomposition are explained in [Rivas and Huelga, Sec. 6.2, especially Sec. 6.2.1](../references/RELATED_WORK.md#rivas2012).

The theorem must therefore be applied to a justified effective generator. It does not assert that every reservoir attached to a small physical region faces the same stationary error floor. Filtered quasilocal jumps used in [Zhan et al.](../references/RELATED_WORK.md#zhan2026) also lie outside a strict finite-support assumption when their tails extend beyond the allowed region.

## Rates and coherent strength

No rate normalization is needed for a stationary optimum. Rescaling a generator by any $`c>0`$ changes its speed while preserving its stationary states:

```math
\mathcal L\longmapsto c\mathcal L,
\qquad
H\longmapsto cH,
\qquad
J_a\longmapsto\sqrt c\,J_a.
```

The converse is also uniform over independent choices of relative rates and coherent strengths. Its population-balance argument removes the Hamiltonian and compares nonnegative jump contributions. Making nonzero dissipation arbitrarily weak cannot improve the bound. At exactly zero dissipation, global attraction is lost and the stronger stationary-state statement no longer has its required nonscalar jump.

The [upper construction](construction.md) can use a single jump

```math
J=\sqrt\gamma\,
\bigl(|0\rangle\langle d|_S\otimes I_{S^c}\bigr),
\qquad \gamma>0,
```

whose local matrix has rank one and satisfies $`\|J\|_{\mathrm{op}}^2=\gamma`$. The full jump need not have rank one, since it includes the identity on the complement. On the $`(D-1)`$-dimensional space orthogonal to the desired stationary vector, the construction takes a path Hamiltonian with nearest-neighbor matrix elements $`h>0`$. It has

```math
\|H\|_{\mathrm{op}}<2h.
```

Both $`h`$ and $`\gamma`$ may be fixed positive constants. The accuracy witness therefore does not require an operator norm growing with the system dimension. Global attraction holds for each finite constructed generator, but this norm statement provides no dimension-uniform convergence rate.

## Local and global coherent control for Gibbs targets

The [Gibbs application](gibbs-corollary.md) uses $`H_0`$ for the target energy Hamiltonian and $`K`$ for the controlled coherent term. The stationary converse remains valid if $`K`$ is further restricted to local terms. Its pure-output attaining construction uses unrestricted $`K`$, so it provides no corresponding local-$`K`$ upper bound.

[Gibbs Cancellation Obstruction](https://github.com/GoGoKo699/Gibbs-Cancellation-Obstruction/blob/7261788af6b88ba30222dc5e5fafb93337d09876/science/finite-temperature-feasibility.md) distinguishes those models for the same explicit five-qubit Gibbs target. Its local-$`K`$ cancellation obstruction is compatible with exact high-temperature preparation obtained by cancelling an inherited secular reservoir's off-diagonal drift with generally global $`K`$. At sufficiently low temperature its certified negative ground-population forms exclude genuine dissipation even for global $`K`$. Strict jump support is retained throughout; changing coherent support alone changes the high-temperature feasibility conclusion.

For each fixed temperature in the feasible interval, the completed global-$`K`$ generator is finite and can be rescaled to any positive full-generator norm budget. Such rescaling preserves exact stationarity and scales the positive gap. The unscaled dissipative coercivity is not an explicit rate at that budget without a bound on the complete generator norm. Neither a small norm nor formal exact coherent completion supplies an efficient specification or implementation of $`K`$.

## A bounded operator norm does not price implementation

The path basis is built from the full target state and a local Schmidt decomposition. Its vectors generally extend across the entire physical system. Nearest-neighbor hopping in that abstract basis is not nearest-neighbor coupling between physical sites.

For $`n`$ qubits, $`D=2^n`$, so the construction uses a basis of $`D-1`$ orthogonal directions. An explicit dense description of the resulting Hamiltonian can be exponentially large. The theorem does not supply an efficient classical specification, native-gate decomposition, calibration scheme or bounded-degree physical realization. Nor does it bound the cost of obtaining the full description of an unknown target.

These facts distinguish the attained stationary error from a complete preparation cost. The globally supported Hamiltonian is a permitted resource in the optimization and a substantive condition of the matching upper bound.

## State space, autonomy and approximation

Adding an ancilla or an extra local level changes the physical Hilbert space. For example, extending a target to $`|\psi\rangle\otimes|0\rangle_A`$ gives a rank-deficient marginal on a resettable ancilla. A theorem applied to that enlarged target must use the enlarged tensor decomposition and support family. It cannot be used to infer the same positive error floor on the original system after tracing out the ancilla.

Time-dependent preparation, measurements, postselection and controllers with retained memory can similarly change the admissible dynamics. An unconditional feedback construction that happens to produce a time-independent Lindblad generator in the stated class still obeys the theorem; the effective mathematical model is decisive.

The proof concerns exact stationary states of each fixed finite generator. It is not an estimate for approximately stationary states in terms of $`\|\mathcal L(\rho)\|`$, and it does not bound finite-time transients. It also assumes strict support. An extension to small nonlocal tails would need to quantify their strength and the relevant stationary-state response.

Finally, the factor-two interval does not identify the exact mixed optimum or prove optimality of the universal constant. Some targets have arbitrarily small $`\mu_{\mathcal N}(\psi)`$. Large entanglement entropy alone does not supply a lower bound on this smallest eigenvalue; the [uniform-marginal and Haar consequences](consequences.md) state the spectral hypotheses explicitly.
