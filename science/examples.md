# Examples of the locality–accuracy law

The invariant

```math
\mu_{\mathcal N}(\psi)
=\min_{S\in\mathcal N}\lambda_{\min}(\psi_S)
```

depends on the target and the allowed dissipative supports. Zero eigenvalues are included. Under the [model](model.md)—separately supported effective Lindblad jumps, arbitrary global time-independent Hamiltonian, and no additional retained degrees of freedom—the optimal stationary infidelity satisfies

```math
\frac{\mu_{\mathcal N}(\psi)}2
\le\epsilon_{\mathrm{opt}}(\psi,\mathcal N)
\le\mu_{\mathcal N}(\psi).
```

The optimum restricted to pure attractive stationary outputs is exactly $`\mu_{\mathcal N}(\psi)`$. The [single-reset construction](construction.md) attains that value. The examples below distinguish the mixed-output interval from this exact pure-output optimum.

| Target | Allowed supports | $`\mu`$ | Mixed-output infidelity guaranteed by the theorem | Pure-output optimum |
| --- | --- | --- | --- | --- |
| Product state | Any nonempty family of supports of dimension at least two | $`0`$ | $`0`$ | $`0`$ |
| Two-qubit Bell state | One or both single sites | $`1/2`$ | $`[1/4,1/2]`$ | $`1/2`$ |
| $`n`$-qubit GHZ, $`n\ge3`$ | Single sites only | $`1/2`$ | $`[1/4,1/2]`$ | $`1/2`$ |
| $`n`$-qubit GHZ, $`n\ge3`$ | A family containing a pair | $`0`$ | $`0`$ | $`0`$ |
| Five-qubit ring graph state | Single sites only | $`1/2`$ | $`[1/4,1/2]`$ | $`1/2`$ |
| Five-qubit ring graph state | Supports of size at most two, including a pair | $`1/4`$ | $`[1/8,1/4]`$ | $`1/4`$ |

The intervals are bounds on the optimum, not claims that every value in the interval is attained. All achievability statements in this page permit the globally supported Hamiltonian in the model.

## Product targets

For $`|\psi\rangle=\bigotimes_j|a_j\rangle`$, every nonempty reduced state is pure. Whenever its Hilbert-space dimension is at least two, its minimum eigenvalue is zero. Therefore $`\mu=0`$, and exact stabilization is available.

For example, independent local resets prepare a product target if the allowed supports contain all single sites. If only one support is allowed, the general construction instead uses that support's reset together with a global Hamiltonian. The invariant does not require the dissipative supports themselves to cover the system, because the Hamiltonian is unrestricted.

## Bell targets: the bound need not be sharp

For

```math
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},
```

each one-qubit marginal is $`I_2/2`$. The theorem therefore excludes stationary infidelity below $`1/4`$ and supplies a pure attractive output of infidelity $`1/2`$. Such a pure output is a product state obtained by discarding one Schmidt component.

There is a sharper known result in the specific setting where **only one of the two qubits is coupled to the dissipator**. Optimizing the local dissipator and arbitrary two-qubit Hamiltonian gives a singlet-fidelity supremum of $`(3+\sqrt5)/8`$, corresponding to infidelity

```math
\frac{5-\sqrt5}{8}\simeq0.34549.
```

Local unitary changes of basis transfer this benchmark to $`|\Phi^+\rangle`$. It lies strictly between $`1/4`$ and $`1/2`$, illustrating both the non-sharpness of the universal interval and an improvement from allowing mixed stationary outputs. The cited benchmark has a single dissipative support; it is not asserted here as the optimum when separate dissipators on both qubits are allowed. See [Žnidarič (2015)](../references/RELATED_WORK.md#znidaric2015) for the precise optimization and limiting construction.

## GHZ targets: a local kernel changes feasibility

Let

```math
|\mathrm{GHZ}_n\rangle
=\frac{|0\rangle^{\otimes n}+|1\rangle^{\otimes n}}{\sqrt2},
\qquad n\ge3.
```

Every single-site marginal is $`I_2/2`$, so restricting the dissipators to single sites gives $`\mu=1/2`$. The resulting stationary error floor persists even if the Hamiltonian is global and arbitrarily chosen.

Every pair marginal is

```math
\psi_{ij}
=\frac12|00\rangle\langle00|
+\frac12|11\rangle\langle11|,
```

with spectrum $`(1/2,1/2,0,0)`$. Allowing even one pair as a dissipative support therefore makes $`\mu=0`$. Exact stabilization then follows from the general construction. This conclusion does not claim a local Hamiltonian or a favorable preparation time.

The verification uses four qubits. In that case a pair and its complement both have dimension four, so the kernel reflects the structure of GHZ rather than an automatic dimension imbalance.

## Five-qubit ring graph state: a two-body error floor

Number the sites modulo five and define

```math
|C_5\rangle
=\left(\prod_{j=1}^5\mathrm{CZ}_{j,j+1}\right)|+\rangle^{\otimes5}
=\frac1{\sqrt{32}}\sum_{x\in\{0,1\}^5}
(-1)^{\sum_jx_jx_{j+1}}|x\rangle.
```

Its stabilizer generators are

```math
K_j=X_jZ_{j-1}Z_{j+1}.
```

A product of generators indexed by a vertex set $`T`$ has binary Pauli labels $`x=1_T`$ and $`z=A_{C_5}1_T\pmod2`$. Its support contains $`T`$. Thus a product of at least three generators has weight at least three. A single generator has weight three, while a product of two distinct generators has weight four, both for adjacent vertices and for vertices at distance two. No nonidentity stabilizer is supported on one or two sites.

In the stabilizer expansion of the pure-state density matrix, partial trace removes every term whose support is not contained in the retained region. Hence, for every pair $`S`$,

```math
(C_5)_S=\frac{I_4}{4}.
```

Every single-site marginal is consequently $`I_2/2`$. If allowed supports have size at most two and include at least one pair, then

```math
\mu=\frac14,\qquad
\frac18\le\epsilon_{\mathrm{opt}}\le\frac14,
\qquad
\epsilon_{\mathrm{pure,opt}}=\frac14.
```

This example has a nonzero obstruction even though pair-supported dissipation suffices for exact GHZ stabilization under the same freedom in coherent control. The distinction is the presence or absence of a kernel in the target's allowed marginals.

The verification independently checks all ten pair marginals with exact integer Gram matrices. It also enumerates the stabilizer weight distribution $`1+10z^3+15z^4+6z^5`$. These finite exact checks establish the stated property of this explicit graph state; they do not replace the general stabilization proof.

## General complex targets and unequal subsystem dimensions

The theorem does not require real amplitudes, qubits, contiguous supports, or a Schmidt basis aligned with the physical coordinates. Two fixed seeded complex vectors in the verification exercise these features:

| Physical dimensions | Allowed supports, with sites numbered from one | Selected support dimension | Complement dimension | Selected marginal rank |
| --- | --- | --- | --- | --- |
| $`2\times4\times2`$ | $`\{1\},\{3\},\{1,3\}`$ | $`4`$ | $`4`$ | $`4`$ |
| $`2\times3\times2`$ | $`\{1\},\{3\},\{1,3\}`$ | $`4`$ | $`3`$ | $`3`$ |

In the first case, the selected marginal is full rank. For the saved target seed 1126, its smallest eigenvalue is approximately $`1.88644564\times10^{-3}`$, and the constructed pure stationary infidelity agrees with that value to floating-point precision. In the second, the marginal necessarily has a kernel because its rank cannot exceed the complement dimension. The construction stabilizes that target exactly. Choosing the first and third physical factors tests an actual subsystem permutation rather than treating the input as an already grouped bipartite state.

These are reproducible finite examples, not an empirical claim about a distribution of random states. [verification/results.json](../verification/results.json) records the numerical values, while [verification/README.md](../verification/README.md) explains the checks and tolerances. The analytic theorem supplies the general statement.
