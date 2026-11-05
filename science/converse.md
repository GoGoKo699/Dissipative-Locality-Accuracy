# Stationary-state converse and the pure-state optimum

Use the finite-dimensional model and fidelity convention in [model](model.md). Write $`\mu=\mu_{\mathcal N}(\psi)`$. This page proves two lower bounds:

```math
1-\langle\psi|\rho_*|\psi\rangle\ge\frac\mu2
\quad\text{for every stationary state},
```

```math
1-|\langle\psi|\phi\rangle|^2\ge\mu
\quad\text{for every pure stationary state }|\phi\rangle\langle\phi|.
```

In both statements, choose an admissible local Lindblad representation containing at least one nonscalar jump. Every generator with a unique globally attractive state satisfies this nontriviality condition. The Hamiltonian is arbitrary throughout.

## Stationary population balance

The diagonal balance equation below is an established ingredient of [spectral stabilizability](../references/RELATED_WORK.md#linowski2023). We derive it here to make the dependence on the actual stationary eigenvector explicit.

Let $`\rho_*`$ be stationary and suppose its largest eigenvalue exceeds one half. Write

```math
\rho_*=(1-\delta)|\phi\rangle\langle\phi|+R,
\qquad 0\le\delta<\frac12,
```

```math
R\ge0,
\qquad R|\phi\rangle=0,
\qquad \mathrm{Tr}R=\delta.
```

The leading eigenvector is unique up to phase. For each jump define

```math
a_a=\langle\phi|J_a|\phi\rangle,
\qquad L_a=J_a-a_aI.
```

Subtracting a scalar preserves the allowed support. In an eigenvector of $`\rho_*`$,

```math
\langle\phi|[H,\rho_*]|\phi\rangle=0.
```

Moreover, $`R|\phi\rangle=0`$ gives

```math
\langle\phi|\mathcal D[J_a](\rho_*)|\phi\rangle
=\langle\phi|L_aRL_a^\dagger|\phi\rangle
-(1-\delta)\|L_a\phi\|^2.
```

Thus stationarity implies the exact identity and its positive-operator estimate

```math
\begin{aligned}
&(1-\delta)\sum_a\|L_a\phi\|^2
=\sum_a\langle\phi|L_aRL_a^\dagger|\phi\rangle
\le\delta\sum_a\|L_a^\dagger\phi\|^2.
\end{aligned}
\tag{1}
```

The inequality uses $`R\le\delta I`$. It places no bound on $`H`$ and does not require any individual dissipator to preserve $`\rho_*`$. The centered jumps are used only to express this identity; no assumption about a preferred Lindblad representation is introduced.

## A small eigenvalue in an active local marginal

For each allowed support, define the extremal eigenvalues of the marginal of the **stationary eigenvector**:

```math
\alpha_S=\lambda_{\min}(\phi_S),
\qquad
\beta_S=\lambda_{\max}(\phi_S),
\qquad
\phi_S=\mathrm{Tr}_{S^c}|\phi\rangle\langle\phi|.
```

Because $`\dim\mathcal H_S\ge2`$ and $`\mathrm{Tr}\phi_S=1`$,

```math
\beta_S\le1-\alpha_S.
```

Write $`L_a=L_{a,S_a}\otimes I_{S_a^c}`$. With $`\|\cdot\|_F`$ denoting the Frobenius norm of the local matrix,

```math
\begin{aligned}
\|L_a\phi\|^2
&=\mathrm{Tr}(\phi_{S_a}L_{a,S_a}^\dagger L_{a,S_a})
\ge\alpha_{S_a}\|L_{a,S_a}\|_F^2,\\
\|L_a^\dagger\phi\|^2
&=\mathrm{Tr}(\phi_{S_a}L_{a,S_a}L_{a,S_a}^\dagger)
\le\beta_{S_a}\|L_{a,S_a}\|_F^2.
\end{aligned}
\tag{2}
```

At least one centered local matrix is nonzero, since the chosen representation contains a nonscalar jump. Equations (1) and (2) imply that at least one support carrying a nonzero centered jump satisfies

```math
\boxed{\alpha_S\le\delta.}
\tag{3}
```

To see this, suppose instead that every active support had $`\alpha_S>\delta`$. For each such support,

```math
(1-\delta)\alpha_S
>\delta(1-\alpha_S)
\ge\delta\beta_S.
```

Multiplication by the nonzero squared Frobenius norms and summation contradict (1). The conclusion is insensitive to the channel strengths and to the number of channels.

## From the stationary eigenvector to the target overlap

Assume now that $`0\le\delta<\mu`$. Choose a support satisfying (3), and choose a unit eigenvector $`|u\rangle\in\mathcal H_S`$ with eigenvalue $`\alpha_S`$. The projector

```math
M=|u\rangle\langle u|_S\otimes I_{S^c}
```

has probabilities

```math
p=\langle\psi|M|\psi\rangle\ge\mu,
\qquad
q=\langle\phi|M|\phi\rangle=\alpha_S\le\delta.
```

Splitting the overlap into the two orthogonal measurement sectors and applying Cauchy–Schwarz yields

```math
\begin{aligned}
c:=|\langle\psi|\phi\rangle|
&\le\sqrt{pq}+\sqrt{(1-p)(1-q)}\\
&\le\sqrt{\mu\delta}+\sqrt{(1-\mu)(1-\delta)}.
\end{aligned}
\tag{4}
```

For the second inequality, write $`p=\sin^2 x`$ and $`q=\sin^2 y`$, with angles in $`[0,\pi/2]`$. Under $`p\ge\mu>\delta\ge q`$, the nonnegative angle difference $`x-y`$ is smallest at $`p=\mu,q=\delta`$. The binary overlap is $`\cos(x-y)`$, so it is largest there. This step controls ordinary target fidelity even when the target is not an eigenvector of the stationary state.

## The mixed-state error bound

If $`\mu=0`$, the desired lower bound is immediate. Suppose $`0<\mu\le1/2`$, and put

```math
F=\langle\psi|\rho_*|\psi\rangle,
\qquad \epsilon=1-F.
```

If $`F\le1/2`$, then $`\epsilon\ge1/2\ge\mu/2`$. Otherwise $`\lambda_{\max}(\rho_*)\ge F>1/2`$, so the preceding decomposition and balance argument apply. Positivity gives

```math
R\le\delta\bigl(I-|\phi\rangle\langle\phi|\bigr),
```

and hence

```math
\begin{aligned}
&F\le(1-\delta)c^2+\delta(1-c^2).
\end{aligned}
\tag{5}
```

If $`\delta\ge\mu`$, then $`F\le1-\delta`$ already gives the stronger inequality $`\epsilon\ge\mu`$. It remains to consider $`\delta<\mu`$. Set

```math
\mu=\sin^2 a,
\qquad \delta=\sin^2 b,
\qquad 0\le b\lt a\le\frac\pi4.
```

Equation (4) says $`c\le\cos(a-b)`$. Since $`1-2\delta>0`$, (5) implies

```math
\begin{aligned}
\epsilon
&\ge\sin^2 b+\cos(2b)\sin^2(a-b)\\
&=\frac{1-\cos(2b)\cos(2a-2b)}2.
\end{aligned}
```

The product-to-sum identity supplies the final bound:

```math
\begin{aligned}
\cos(2b)\cos(2a-2b)
&=\frac{\cos(2a)+\cos(4b-2a)}2\\
&\le\frac{1+\cos(2a)}2
=1-\mu.
\end{aligned}
```

Therefore every stationary state in the stated nontrivial dissipative class satisfies

```math
\boxed{1-\langle\psi|\rho_*|\psi\rangle\ge\frac\mu2.}
```

The proof allows arbitrary Hamiltonian terms, arbitrary stationary-state rank, and cancellation among all channels in the stationary equation. Its use of the actual leading stationary eigenvector is what permits a bound on the target overlap rather than only on a designated stationary eigenvalue.

## The exact pure-state optimum

The pure-output statement has a direct geometric proof. It also identifies precisely which pure states can be stabilized with the available support family and unrestricted global coherent control.

### Necessary rank deficiency

Let $`|\phi\rangle\langle\phi|`$ be stationary. Its diagonal stationarity equation is

```math
0
=-\sum_a\left(
\langle\phi|J_a^\dagger J_a|\phi\rangle
-|\langle\phi|J_a|\phi\rangle|^2
\right)
=-\sum_a\|L_a\phi\|^2.
```

Every term vanishes, so every jump has $`\phi`$ as an eigenvector. Choose a nonscalar jump, for which the centered local matrix $`L_{a,S_a}`$ is nonzero. Then

```math
0=\|L_a\phi\|^2
=\mathrm{Tr}(\phi_{S_a}L_{a,S_a}^\dagger L_{a,S_a})
```

forces $`\phi_{S_a}`$ to be rank deficient. A positive definite marginal would give a strictly positive trace. This is the local rank obstruction familiar from [quasi-local pure-state stabilization](../references/RELATED_WORK.md#karuvade2018); the common-eigenvector and invariant-subspace conditions also belong to [Hamiltonian-assisted stabilization theory](../references/RELATED_WORK.md#ticozzi2009).

### Distance to the rank-deficient set

Define the set of normalized pure vectors

```math
\mathcal Z_{\mathcal N}
=\left\{|\phi\rangle:
\lambda_{\min}(\phi_S)=0
\text{ for at least one }S\in\mathcal N\right\}.
```

For any $`\phi\in\mathcal Z_{\mathcal N}`$, choose an allowed support $`S`$ and a local unit vector $`u\in\ker\phi_S`$. With $`M=|u\rangle\langle u|_S\otimes I`$, positivity gives $`M|\phi\rangle=0`$. Consequently,

```math
\begin{aligned}
|\langle\psi|\phi\rangle|^2
&=|\langle\psi|(I-M)|\phi\rangle|^2\\
&\le\|(I-M)\psi\|^2\\
&=1-\langle u|\psi_S|u\rangle\\
&\le1-\lambda_{\min}(\psi_S)
\le1-\mu.
\end{aligned}
```

Conversely, choose a support $`S`$ attaining $`\mu`$ and a local unit eigenvector $`u`$ with eigenvalue $`\mu`$. Define

```math
M=|u\rangle\langle u|_S\otimes I,
\qquad
|\phi\rangle=\frac{(I-M)|\psi\rangle}{\sqrt{1-\mu}}.
```

The denominator is nonzero because $`\mu\le1/2`$. This vector belongs to $`\mathcal Z_{\mathcal N}`$ and obeys $`|\langle\psi|\phi\rangle|^2=1-\mu`$. Hence

```math
\boxed{
\min_{\phi\in\mathcal Z_{\mathcal N}}
\left(1-|\langle\psi|\phi\rangle|^2\right)
=\mu_{\mathcal N}(\psi).
}
```

### From geometry to an attained stabilization optimum

The necessary rank condition puts every pure attractive stationary output in $`\mathcal Z_{\mathcal N}`$. The [explicit construction](construction.md) stabilizes every member of this set using one allowed reset channel and a suitable global Hamiltonian. Applied to the vector just constructed, it attains the geometric minimum. Therefore

```math
\boxed{\epsilon_{\mathrm{pure,opt}}(\psi,\mathcal N)
=\mu_{\mathcal N}(\psi).}
```

In particular, exact pure-state stabilization is possible if and only if at least one allowed target marginal is rank deficient. If $`\mu=0`$, the geometric minimizer is the target itself, and the same construction stabilizes it exactly. This endpoint does not require a limit of approximate states or of vanishing dissipative rates.
