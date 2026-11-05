# Accuracy, dissipative support and typical targets

[Model and theorem](model.md) · [Converse](converse.md) · [Attaining construction](construction.md) · [Resource boundaries](resources.md)

The stationary accuracy law turns local marginal spectra into a constraint on dissipative support. For a normalized pure target $`\psi`$ and an allowed support family $`\mathcal N`$, write

```math
\mu_{\mathcal N}(\psi)
=\min_{S\in\mathcal N}\lambda_{\min}(\psi_S),
\qquad
\psi_S=\operatorname{Tr}_{S^c}|\psi\rangle\langle\psi|.
```

The minimum includes zero eigenvalues. The [main theorem](model.md) gives

```math
\frac{\mu_{\mathcal N}(\psi)}2
\le \epsilon_{\mathrm{opt}}(\psi,\mathcal N)
\le \epsilon_{\mathrm{pure,opt}}(\psi,\mathcal N)
=\mu_{\mathcal N}(\psi).
```

Here the optimization permits arbitrary global, time-independent Hamiltonians and arbitrary supported jump design on the fixed physical Hilbert space. The optimized outputs are globally attractive stationary states, and $`\epsilon=1-\langle\psi|\rho_*|\psi\rangle`$ is ordinary target infidelity. These assumptions are retained in every consequence below.

## Pure and mixed stationary approximations

Let $`\mathcal Z_{\mathcal N}`$ be the set of normalized pure states with a rank-deficient marginal on at least one allowed support. The [pure-output geometric argument](converse.md#the-exact-pure-state-optimum) establishes

```math
\min_{\phi\in\mathcal Z_{\mathcal N}}
\left(1-|\langle\psi|\phi\rangle|^2\right)
=\mu_{\mathcal N}(\psi).
```

The [construction](construction.md) makes every such $`\phi`$ globally attractive using one allowed reset and a suitable global Hamiltonian. Thus the pure optimum is exactly this geometric distance. Allowing a mixed stationary output can reduce the optimal infidelity by at most a factor of two. For two pure states, infidelity equals the square of their half-trace distance, $`D(\phi,\psi)=\tfrac12\||\phi\rangle\langle\phi|-|\psi\rangle\langle\psi|\|_1`$. No equality between mixed-state trace distances is asserted.

When $`\mu_{\mathcal N}(\psi)=0`$, the target itself can be stabilized exactly. When $`\mu_{\mathcal N}(\psi)>0`$, the converse gives a positive error floor even for mixed stationary states and arbitrarily strong coherent control. The exact rank obstruction is established background; its quantitative extension to ordinary stationary fidelity is described in [related work](../references/RELATED_WORK.md).

## A deterministic support requirement

Consider $`n`$ physical qubits and supports satisfying $`1\le |S|\le k`$. Suppose that, for some $`0<c\le1`$,

```math
\psi_S\succeq \frac{c}{2^{|S|}}I_S
\qquad\text{for every }S\in\mathcal N.
```

Then

```math
\mu_{\mathcal N}(\psi)\ge c\,2^{-k},
\qquad
\epsilon_{\mathrm{opt}}(\psi,\mathcal N)\ge c\,2^{-k-1}.
```

Consequently, an attractive stationary output with infidelity at most $`\varepsilon>0`$ requires

```math
k\ge \log_2\frac{c}{2\varepsilon}.
```

For integer $`k`$, take the ceiling when the right-hand side is positive. If the family contains at least one support of size $`k`$, normalization gives the complementary deterministic bound

```math
\mu_{\mathcal N}(\psi)\le 2^{-k},
\qquad
\epsilon_{\mathrm{opt}}(\psi,\mathcal N)\le 2^{-k}.
```

The upper bound is an existence statement with the unrestricted Hamiltonian of the [construction](construction.md).

### Uniform local marginals

A pure $`n`$-qubit state is called *$`k`$-uniform* here when every $`k`$-qubit marginal is maximally mixed. Taking partial traces shows the same property for all smaller marginals. If the target is $`k`$-uniform and the allowed family has largest support size $`k`$, then

```math
\boxed{
\mu_{\mathcal N}(\psi)=2^{-k},
\qquad
2^{-k-1}\le\epsilon_{\mathrm{opt}}(\psi,\mathcal N)\le2^{-k}.
}
```

For each such target and family, accuracy $`\varepsilon`$ therefore requires $`k\ge\lceil\log_2(1/\varepsilon)-1\rceil`$. The condition $`k\ge\lceil\log_2(1/\varepsilon)\rceil`$ suffices under the stated coherent-control model, provided the corresponding support is allowed. These implications are conditional on the target's uniformity; they do not assert the existence of $`k`$-uniform states for arbitrary $`n,k`$.

For illustration, exact uniformity through support sizes one, two and three gives infidelity intervals $`[1/4,1/2]`$, $`[1/8,1/4]`$ and $`[1/16,1/8]`$, respectively. The theorem does not determine the exact mixed optimum within those intervals.

## Haar-random targets: a finite probability bound

Let $`|\psi\rangle`$ be Haar-random on $`n`$ qubits, and take

```math
1\le k\le\lfloor n/2\rfloor,
\qquad
d=2^k,
\qquad
r=2^{n-k}.
```

For any fixed $`k`$-subset $`T`$, the marginal $`\psi_T`$ is full rank almost surely because $`d\le r`$. [Hayden, Leung and Winter, Lemma III.4](../references/RELATED_WORK.md#hayden2006) gives, for $`0<\eta<1`$,

```math
\Pr\!\left[
\lambda_{\min}(\psi_T)<\frac{1-\eta}{d}
\right]
\le
\left(\frac{10d}{\eta}\right)^{2d}
\exp\!\left(-\frac{r\eta^2}{14}\right).
\tag{1}
```

In this page $`\exp`$ denotes the natural exponential and $`\ln`$ the natural logarithm. The cited paper uses base-two $`\exp`$ and writes its exponent as $`-r\eta^2/(14\ln2)`$; equation (1) is the same bound after conversion. Its lemma refers to the smallest nonzero eigenvalue. Full rank in the stated $`d\le r`$ regime makes it the smallest eigenvalue needed here.

A union bound over all $`\binom nk`$ supports gives the failure probability

```math
\Delta_{n,k}(\eta)
:=
\min\!\left\{
1,\,
\binom nk
\left(\frac{10\,2^k}{\eta}\right)^{2^{k+1}}
\exp\!\left(-\frac{2^{n-k}\eta^2}{14}\right)
\right\}.
\tag{2}
```

No independence of the marginals is required. With probability at least $`1-\Delta_{n,k}(\eta)`$, every $`k`$-subset satisfies $`\psi_T\succeq(1-\eta)I_T/2^k`$. For a smaller subset $`S\subset T`$, positivity of the partial trace then gives

```math
\psi_S
=\operatorname{Tr}_{T\setminus S}\psi_T
\succeq
\frac{1-\eta}{2^{|S|}}I_S.
\tag{3}
```

On this single event, **every** allowed family whose largest support has size $`k`$ obeys

```math
(1-\eta)2^{-k}
\le\mu_{\mathcal N}(\psi)\le2^{-k},
```

and hence

```math
\boxed{
(1-\eta)2^{-k-1}
\le\epsilon_{\mathrm{opt}}(\psi,\mathcal N)
\le2^{-k}.
}
\tag{4}
```

The concentration inequality is inherited. Equations (2)–(4) combine it with a union bound, marginalization and the stationary accuracy theorem. An entropy or average-purity estimate alone would not establish the lower spectral bound used here.

### An asymptotic regime away from half the system

Fix $`0<\alpha<1/2`$ and let $`k=k_n`$ satisfy

```math
1\le k\le(1/2-\alpha)n.
```

Choose $`\eta_n=2^{-\alpha n/2}`$. The logarithm of the untruncated expression in (2) is

```math
\ln\binom nk
+2^{k+1}\ln\!\left(\frac{10\,2^k}{\eta_n}\right)
-\frac{2^{n-k}\eta_n^2}{14}.
\tag{5}
```

The first positive term is at most $`n\ln2`$. The second is $`O(n2^k)`$, while

```math
\frac{2^{n-k}\eta_n^2}{n2^k}
=\frac{2^{n-2k-\alpha n}}{n}
\ge\frac{2^{\alpha n}}{n}\longrightarrow\infty.
```

Thus $`\Delta_{n,k}(\eta_n)\to0`$. With probability tending to one, uniformly over the support families just specified,

```math
\frac{1-o(1)}2\,2^{-k}
\le\epsilon_{\mathrm{opt}}(\psi,\mathcal N)
\le2^{-k}.
```

In this regime the optimum is $`\Theta(2^{-k})`$. This includes fixed $`k`$ as $`n`$ grows. The argument does not provide a uniform asymptotic characterization in the half-system window; there the marginal spectrum requires separate analysis.

## Interpretation

For targets with nearly uniform allowed marginals, achieving error below the stated support-dependent floor requires increasing the number of qubits acted on coherently by at least one dissipative jump. Increasing the Hamiltonian strength, the number of independently supported channels or their rates cannot remove the lower bound. Error can still improve at fixed support within the permitted interval. Conversely, one allowed jump suffices to attain the same order of error with a suitable global Hamiltonian.

This is a statement about the support of the effective jumps and stationary feasibility. It does not bound the locality of microscopic bath couplings, the cost of learning an unknown target, or a preparation time. Those distinctions are made explicit in [resources and physical scope](resources.md).
