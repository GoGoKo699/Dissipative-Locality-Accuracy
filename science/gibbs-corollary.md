# Gibbs approximation from the pure-target accuracy bound

[Model and theorem](model.md) · [Stationary converse](converse.md) · [Consequences](consequences.md) · [Coherent-control resources](resources.md#local-and-global-coherent-control-for-gibbs-targets)

A low-temperature Gibbs state approaches a ground-state projector. The pure-target stationary bound therefore gives a finite-temperature approximation floor whenever every allowed ground-state marginal is full rank. This page derives that corollary and applies it to the rigorously certified five-qubit witness in [Gibbs Cancellation Obstruction](https://github.com/GoGoKo699/Gibbs-Cancellation-Obstruction). The complete explicit certificate, stronger exact-target proof and positive thermal construction have their [authoritative home there](https://github.com/GoGoKo699/Gibbs-Cancellation-Obstruction/blob/5666fe5ede05e8d5ea4d8caf1f9641c2170341f8/science/finite-temperature-feasibility.md).

## Model and accuracy conventions

Fix a finite physical tensor product and a nonempty family $`\mathcal N`$ of allowed jump supports. Consider a time-independent generator

```math
\mathcal L(A)=-i[K,A]+\sum_a\mathcal D[J_a](A),
\qquad
J_a=A_{a,S_a}\otimes I_{S_a^c},\quad S_a\in\mathcal N,
```

with $`\mathcal D[J](A)=JAJ^\dagger-\tfrac12\{J^\dagger J,A\}`$. The coherent Hamiltonian $`K`$ may act globally and need not equal the target energy Hamiltonian $`H_0`$. No retained ancilla is supplied. For the all-stationary converse below, require at least one nonscalar jump in an admissible supported representation. Every generator with a unique globally attractive state satisfies this condition. Purely Hamiltonian dynamics can leave a Gibbs state stationary and is excluded from the dissipative converse.

Suppose $`H_0`$ has a unique normalized ground vector $`|g\rangle`$ with energy $`E_0`$. Write

```math
\rho_\beta=\frac{e^{-\beta H_0}}{\mathrm{Tr}e^{-\beta H_0}},
\qquad
\delta_\beta=1-\langle g|\rho_\beta|g\rangle,
\qquad
\mu=\min_{S\in\mathcal N}\lambda_{\min}(g_S),
```

where $`g_S=\mathrm{Tr}_{S^c}|g\rangle\langle g|`$ and the minimum eigenvalue includes zeros. The pure-target infidelity is $`1-\langle g|\sigma|g\rangle`$, while thermal approximation error is the half trace distance $`D_{\mathrm{tr}}(\sigma,\rho_\beta)=\tfrac12\|\sigma-\rho_\beta\|_1`$. They are distinct quantities.

## A direct corollary of the inherited stationary bound

The [stationary-state converse](converse.md#the-mixed-state-error-bound) already proves, for every stationary output $`\sigma`$ in the dissipative class above,

```math
1-\langle g|\sigma|g\rangle\ge\frac\mu2.
```

The ground-projector measurement is an effect, so the variational characterization of half trace distance gives

```math
\begin{aligned}
D_{\mathrm{tr}}(\sigma,\rho_\beta)
&\ge\left|\langle g|(\sigma-\rho_\beta)|g\rangle\right|\\
&\ge \frac\mu2-\delta_\beta.
\end{aligned}
```

Combining this with nonnegativity yields

```math
\boxed{
D_{\mathrm{tr}}(\sigma,\rho_\beta)
\ge\left[\frac\mu2-\delta_\beta\right]_+,
\qquad [x]_+=\max\{x,0\}.
}
```

No square root or additional factor of two appears: the comparison uses one projector's probability difference directly. In particular, $`\delta_\beta<\mu/2`$ excludes exact Gibbs stationarity with genuine dissipation, even under unrestricted coherent control. This is a corollary of this repository's existing pure-target theorem, rather than a second discovery of that theorem. Local-cooling temperature floors are also an [established physical phenomenon](../references/RELATED_WORK.md#znidaric2015).

## Certified five-qubit example

Take the original five-qubit open chain and let $`\mathcal N`$ contain its five single sites and four adjacent pairs. The integer Pauli Hamiltonian $`H_0`$ is fixed by the [authoritative coefficient file](https://github.com/GoGoKo699/Gibbs-Cancellation-Obstruction/blob/5666fe5ede05e8d5ea4d8caf1f9641c2170341f8/verification/data/hamiltonian.json). The [256-bit Arb/Acb certificate](https://github.com/GoGoKo699/Gibbs-Cancellation-Obstruction/blob/5666fe5ede05e8d5ea4d8caf1f9641c2170341f8/verification/ground-thermal/ground_thermal_certificate.json) isolates all 32 energies, certifies the normalized ground vector, and encloses the complete spectra of all nine allowed marginals. Every one of those marginals is positive definite. It proves

```math
0.000071696775227<\mu<0.000071696775228,
```

with the minimum uniquely attained on bond $`(1,2)`$, and

```math
3.005072939810<E_1-E_0<3.005072939811.
```

The exact thermal deficit is evaluated from those certified energies:

```math
\delta_\beta
=\frac{\sum_{j=1}^{31}e^{-\beta(E_j-E_0)}}
{1+\sum_{j=1}^{31}e^{-\beta(E_j-E_0)}}.
```

At $`\beta=4`$ the certificate gives

```math
0.000006066710605253<\delta_4<0.000006066710605254,
```

and, for every stationary output $`\sigma`$ with a nonscalar allowed jump,

```math
\boxed{D_{\mathrm{tr}}(\sigma,\rho_4)>0.000029781677008303.}
```

The [certificate guide and command](../verification/README.md#the-external-rigorous-gibbs-certificate) distinguish these outward interval bounds from this repository's finite floating-point generator checks. The sufficient test $`\delta_\beta<\mu/2`$ has its crossing between $`3.41147195216`$ and $`3.41147195217`$ for this fixed Hamiltonian. That crossing is not the exact physical feasibility boundary.

## Keeping the Gibbs ground eigenvector gives stronger exact-target tests

For exact stationarity of $`\rho_\beta`$, the ground vector is already a stationary-state eigenvector. Thus the target-to-moving-eigenvector part of the ordinary-fidelity proof is unnecessary. Write $`\rho_\beta=p_0|g\rangle\langle g|+R`$, with $`R|g\rangle=0`$, and center each jump by $`L_a=J_a-\langle g|J_a|g\rangle I`$. The inherited [population balance](converse.md#stationary-population-balance) reads

```math
p_0\sum_a\|L_ag\|^2
=\sum_a\langle g|L_aRL_a^\dagger|g\rangle.
```

The coherent commutator has zero ground diagonal for every $`K`$, independent of its support or strength. The existing marginal argument with $`R\preceq\delta_\beta I`$ gives the necessary condition $`\delta_\beta\ge\mu`$. Keeping the largest excited Gibbs population $`p_1`$ instead yields

```math
p_0\sum_a\|L_ag\|^2
\le p_1\sum_a\|L_a^\dagger g\|^2.
```

For a support $`S`$, write $`\alpha_S=\lambda_{\min}(g_S)`$ and $`b_S=\lambda_{\max}(g_S)`$. The squared norms are bounded below by $`\alpha_S\|L_{a,S}\|_F^2`$ and above by $`b_S\|L_{a,S}\|_F^2`$, respectively. Since at least one centered local matrix is nonzero, exact dissipative stationarity requires

```math
\boxed{
e^{-\beta(E_1-E_0)}=\frac{p_1}{p_0}
\ge r,\qquad r=\min_{S\in\mathcal N}\frac{\alpha_S}{b_S}.
}
```

For the explicit witness, the certificate encloses $`r`$ between $`0.000072889471412`$ and $`0.000072889471413`$. The ratio test excludes inverse temperatures above $`\log(1/r)/(E_1-E_0)`$, whose certified interval is $`(3.170161438761,3.170161438762)`$. These are sharper applications of inherited fixed-eigenvector balance; their failure to exclude a temperature supplies no feasible generator.

The companion's stronger [energy-resolved ground-population forms](https://github.com/GoGoKo699/Gibbs-Cancellation-Obstruction/blob/5666fe5ede05e8d5ea4d8caf1f9641c2170341f8/science/finite-temperature-feasibility.md) use all excited weights. Four rigorously negative bond forms at $`\beta=12/5`$, with analytic monotone continuation, exclude every nonscalar on-site/adjacent-pair jump for every real $`\beta\ge12/5`$. That exact-target certificate is distinct from the robust trace-distance floor derived above; its full proof and program are retained in the companion repository.

## Local and global coherent control give different feasible regions

The same companion supplies a positive pair-supported dissipator $`\mathcal D_\beta`$ with exact energy-population balance throughout $`0\le\beta\le1/100`$. For $`\beta>0`$ the Gibbs spectrum is simple. If $`B=\mathcal D_\beta(\rho_\beta)`$, then its energy diagonal is zero, and the standard [spectral stabilizability construction](../references/RELATED_WORK.md#linowski2023) chooses

```math
K_{mn}=-i\frac{B_{mn}}{p_n-p_m}\quad(m\ne n),
\qquad K_{mm}\in\mathbb R.
```

This Hermitian global $`K`$ satisfies $`-i[K,\rho_\beta]=-B`$. The companion's dissipative coercivity proves uniqueness and global attraction of the exact Gibbs state. At $`\beta=0`$ local depolarization suffices directly. This is the established coherent-completion mechanism applied to the companion's inherited secular reservoir; it is not the pure-output construction of this repository.

| Coherent control on the five physical qubits | Certified result with the same individual jump support |
|---|---|
| Unrestricted global $`K`$ | Exact unique attractive Gibbs preparation for $`0\le\beta\le1/100`$; no genuine dissipative stationary realization for every real $`\beta\ge12/5`$ |
| $`K`$ is a sum of single-site and adjacent-pair terms | For this explicit $`H_0`$, the inherited cancellation theorem excludes genuine dissipation at every positive algebraic $`\beta`$, including $`3/1000`$ and $`1/100`$ |

The companion's generic local-$`K`$ theorem fixes $`\beta>0`$ before selecting generic nearest-neighbor Hamiltonians. It is not a common generic-Hamiltonian assertion at every temperature. Its continuous reservoir interval is not a continuous evaluation-rank certificate. At $`\beta=3/1000`$ and $`\beta=1/100`$, the two constructions give a direct separation between local and unrestricted coherent control.

For global $`K`$, the intermediate interval $`1/100<\beta<12/5`$ remains unresolved. The endpoint $`12/5`$ is a sufficient exclusion certificate, not an exact crossover. No monotonicity or connectedness of the full feasible set follows from the monotonicity of the negative population witness.

These claims concern autonomous stabilization on the original finite system under strict effective jump support. They supply neither an efficient synthesis of the generally global $`K`$ nor a rate at a prescribed total-strength budget. Rescaling the entire finite generator preserves its stationary state and rescales its gap. Larger neighborhoods, quasi-local tails, retained auxiliaries and time-dependent protocols require different statements.
