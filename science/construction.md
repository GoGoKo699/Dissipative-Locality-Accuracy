# One local reset and an explicit global Hamiltonian

The [accuracy theorem](model.md#accuracy-theorem) has an upper bound that is attained by a finite, time-independent generator. This page constructs that generator and proves that its stationary state is unique and globally attractive. The construction works at $`\mu_{\mathcal N}(\psi)=0`$ as well as at positive $`\mu_{\mathcal N}(\psi)`$.

For a dissipator that leaves a desired subspace invariant, a suitable global Hamiltonian can make that subspace attractive when its full orthogonal complement is not invariant; see [Hamiltonian-assisted Markovian stabilization](../references/RELATED_WORK.md#ticozzi2009). In the construction below, the relevant conditions are a dark target, $`J\phi=0`$, and a nonzero incoming block, $`J^\dagger\phi\ne0`$. The Hamiltonian is given explicitly, and positivity supplies a self-contained uniqueness and attraction proof.

## Remove one local eigencomponent

Write $`\mu=\mu_{\mathcal N}(\psi)`$. Choose an allowed support $`S`$ attaining the minimum and a local unit eigenvector $`|u\rangle`$ satisfying

```math
\psi_S|u\rangle=\mu|u\rangle.
```

Let

```math
A=|u\rangle\langle u|_S\otimes I_{S^c},
\qquad
|\phi\rangle=\frac{(I-A)|\psi\rangle}{\sqrt{1-\mu}}.
\tag{1}
```

Since $`\mu\le1/2`$, the normalization is well defined. Directly,

```math
A\phi=0,
\qquad
\langle\psi|\phi\rangle=\sqrt{1-\mu},
\qquad
1-|\langle\psi|\phi\rangle|^2=\mu.
\tag{2}
```

If $`\mu=0`$, then $`A\psi=0`$ and $`\phi=\psi`$. Thus (1) also covers a target whose allowed marginal is already rank deficient. It does not require a full-rank Schmidt decomposition or a complement dimension at least as large as $`\dim\mathcal H_S`$.

Choose a unit eigenvector $`|b\rangle`$ of $`\psi_S`$, orthogonal to $`u`$, with positive eigenvalue $`\nu>0`$. Such a choice always exists. If $`\mu>0`$, every eigenvalue is positive and the subsystem has dimension at least two. If $`\mu=0`$, unit trace supplies a positive eigenvalue in the orthogonal complement of the kernel vector.

Use the single local reset jump

```math
J=|b\rangle\langle u|_S\otimes I_{S^c}.
\tag{3}
```

Its local matrix has rank one, and

```math
J^\dagger J=A,
\qquad J\phi=0,
\qquad \|J\|=1.
```

Define

```math
v=J^\dagger\phi.
```

The retained component along $`b`$ ensures

```math
Av=v,
\qquad
\|v\|^2=\frac{\nu}{1-\mu}>0.
\tag{4}
```

The nonzero vector $`v`$ is the channel through which population can enter the desired state.

## Choose the Hamiltonian

Set

```math
P=|\phi\rangle\langle\phi|,
\qquad Q=I-P,
\qquad D=\dim\mathcal H.
```

Because $`A\phi=0`$, the orthogonal complement $`Q\mathcal H`$ is invariant under the projector $`A`$. Choose an orthonormal basis

```math
e_1=\frac{v}{\|v\|},\quad e_2,\ldots,e_{D-1}
```

of $`Q\mathcal H`$ consisting entirely of eigenvectors of $`A`$:

```math
Ae_j=a_je_j,
\qquad a_j\in\{0,1\}.
\tag{5}
```

Such a completion exists because $`Av=v`$. The eigenbasis requirement in (5) is part of the construction; an arbitrary orthonormal completion is not what the proof below uses.

For any fixed $`h>0`$, define

```math
H=h\sum_{j=1}^{D-2}
\left(|e_j\rangle\langle e_{j+1}|
+|e_{j+1}\rangle\langle e_j|\right),
\qquad H\phi=0.
\tag{6}
```

This is a path Hamiltonian on the orthogonal complement of $`\phi`$. Its norm is

```math
\|H\|=2h\cos\left(\frac\pi D\right)<2h.
```

For $`D=2`$, the sum is empty and $`H=0`$, consistent with this formula. The generator is

```math
\mathcal L(\rho)=-i[H,\rho]+\mathcal D[J](\rho).
\tag{7}
```

Equations (2), (3), and (6) give $`J\phi=A\phi=H\phi=0`$, so $`P`$ is stationary. The remaining task is to show that every other state converges to it.

## Uniqueness by positivity

Let $`\rho`$ be any stationary density operator. Its population balance at $`\phi`$ gives

```math
0=\langle\phi|\mathcal L(\rho)|\phi\rangle
=\langle\phi|J\rho J^\dagger|\phi\rangle
=\langle v|\rho|v\rangle.
```

For a positive semidefinite operator, a vanishing quadratic form at a vector implies that the operator annihilates that vector. Therefore

```math
\rho e_1=0.
\tag{8}
```

We propagate (8) along the path. Suppose $`\rho e_j=0`$ and, for $`j>1`$, $`\rho e_{j-1}=0`$. The diagonal stationary equation at $`e_j`$ reduces to

```math
0=\langle e_j|J\rho J^\dagger|e_j\rangle.
```

Indeed, the commutator and anticommutator diagonal entries vanish whenever $`\rho e_j=0`$. Since $`J\rho J^\dagger`$ is positive semidefinite, its entire $`e_j`$-row and column vanish as well. The whole $`e_j`$-row of the stationary equation then becomes

```math
0=\langle e_j|\mathcal L(\rho)
=-i\langle e_j|H\rho.
```

Here $`\langle e_j|\rho H=0`$; both anticommutator rows vanish because $`A`$ is diagonal in the chosen basis. From the path form of $`H`$ and the already vanishing preceding row, for $`j<D-1`$ we obtain

```math
0=-ih\langle e_{j+1}|\rho.
```

Thus $`\rho e_{j+1}=0`$. Induction eliminates all of $`Q\mathcal H`$. Hermiticity then eliminates the corresponding rows, so positivity and unit trace force

```math
\rho=P.
```

This proves uniqueness. The case $`D=2`$ is already complete after (8).

## Global attraction

For an arbitrary initial density operator, let $`\rho(t)=e^{t\mathcal L}(\rho_0)`$. Its desired-state population obeys

```math
p(t)=\mathrm{Tr}(P\rho(t)),
\qquad
\frac{dp}{dt}=\langle v|\rho(t)|v\rangle\ge0.
\tag{9}
```

Since $`0\le p(t)\le1`$, it has a limit $`p_\infty`$. Consider the Cesàro averages

```math
\overline\rho_T=\frac1T\int_0^T\rho(t)\,dt.
```

The finite-dimensional state space is compact, so a sequence with $`T\to\infty`$ has a convergent subsequence. Every subsequential limit is stationary, because

```math
\mathcal L(\overline\rho_T)
=\frac{\rho(T)-\rho(0)}{T}
\longrightarrow0.
```

The uniqueness result therefore forces every such limit to equal $`P`$. On the other hand,

```math
\mathrm{Tr}(P\overline\rho_T)
=\frac1T\int_0^T p(t)\,dt
\longrightarrow p_\infty.
```

It follows that $`p_\infty=1`$. The pure-state trace-distance bound now gives

```math
\|\rho(t)-P\|_1
\le2\sqrt{1-p(t)}
\longrightarrow0.
```

Thus $`P`$ is globally attractive. Equation (9) also gives stability near $`P`$: a small initial population deficit cannot grow, and it bounds the trace distance at every later time. No unproved implication from uniqueness alone is needed.

## Attained accuracy and the exact boundary

The constructed output has infidelity $`\mu`$ by (2), so

```math
\epsilon_{\mathrm{opt}}(\psi,\mathcal N)
\le\mu,
\qquad
\epsilon_{\mathrm{pure,opt}}(\psi,\mathcal N)
\le\mu.
```

The [pure-state lower bound](converse.md#the-exact-pure-state-optimum) makes the second inequality an equality. At $`\mu=0`$, the construction has $`\phi=\psi`$ and stabilizes the original target exactly. Conversely, if every allowed target marginal is full rank, the pure-state converse forbids exact stabilization by any nontrivial admissible dissipator.

More generally, take any pure state with a rank-deficient marginal on an allowed support and use it as the target in this construction. Its invariant is zero, so it becomes the exact globally attractive stationary state of a generator of the form (7). This proves that, with unrestricted global coherent control, the rank-deficient set used in the geometric proof is exactly the set of pure attractive stationary outputs.

## What the construction costs

The jump acts on one allowed subsystem and has a rank-one local matrix. The Hamiltonian in (6) acts on a basis of the full orthogonal complement of the desired state. Although its operator norm is bounded independently of $`D`$ for fixed $`h`$, specifying that basis and implementing those matrix elements can require global control and an exponentially large description in the number of sites.

The construction establishes a stationary-accuracy optimum. It does not establish an efficient preparation algorithm, a local Hamiltonian realization, or a dimension-independent relaxation rate. Those distinctions are part of the [resource interpretation](resources.md). The [verification route](../verification/README.md) provides finite examples that check the construction algebra and spectra; the positivity and convergence arguments above establish the universal result.
