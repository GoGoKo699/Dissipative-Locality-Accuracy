# From open-system dynamics to a locality–accuracy law

[30-milestone map](MILESTONES.md) · [Exact model and theorem](../science/model.md) · [Converse](../science/converse.md) · [Attracting construction](../science/construction.md) · [Research attribution](../references/RELATED_WORK.md)

A reset operation can drive one qubit to its ground state regardless of how that qubit started. Preparing an entangled state is more demanding: a reservoir acting on one part must preserve the correlations with the rest. This project asks how accurately autonomous dynamics can stabilize a specified pure state when every dissipative channel has a prescribed support, even though the Hamiltonian can act on the entire system.

The quantity that controls the answer is the smallest eigenvalue of an allowed reduced density matrix. This page connects open-system foundations to that statement, explains the additional reasoning, and gives a complete two-qubit construction. The [milestone map](MILESTONES.md) organizes the full conceptual route; the linked science pages contain the authoritative assumptions and proofs.

## Selected source and focused routes

The educational anchor is **Ángel Rivas and Susana F. Huelga, _Open Quantum Systems: An Introduction_, first edition, SpringerBriefs in Physics (2012)**. Use the fixed [author preprint, arXiv:1104.5242v2, dated 9 February 2012](https://arxiv.org/pdf/1104.5242v2). The [publisher record](https://doi.org/10.1007/978-3-642-23354-8) identifies the book. Every section and equation number below refers to that fixed preprint.

The following routes use selected sections rather than the whole text.

| Project question | Fixed-source route | Connection to this repository |
|---|---|---|
| What are states, reduced states and their local weights? | §4 opening, Eq. (29); §4.1, proof of Theorem 4.1, Eq. (33) | Partial trace and Schmidt weights lead to the [target invariant](../science/model.md#the-target-invariant). |
| How does a differential equation define a physical evolution? | §§2.1–2.3; §§4.2–4.3; §4.5 | Operator exponentials, quantum channels and composition lead to the [admissible generators](../science/model.md#admissible-generators). |
| What are the Hamiltonian and dissipative terms? | §5.2, Theorem 5.1 and Eq. (46) | Specialize the generator to constant coefficients and impose support on its jump operators. |
| When is a stationary state the final state from every initial condition? | §5.4, Definition 5.3 and Theorems 5.3–5.4 | Relate stationary solutions and relaxation to the [explicit attraction proof](../science/construction.md#global-attraction). |
| How does a pure-target accuracy floor constrain a Gibbs state? | §§5.2 and 5.4; §§6.2.1 and 6.2.8 | Stationarity, an energy eigenbasis and thermal populations support the [Gibbs bridge](#from-pure-target-fidelity-to-gibbs-accuracy). |
| Does a local bath coupling yield a local effective jump? | §6.2.1, then §6.4.1 | Compare microscopic couplings with the [effective-support assumption](../science/resources.md#microscopic-bath-couplings-and-effective-jumps). |

The marginal-spectrum bound, the ordinary-fidelity geometry and the explicit construction below are supplied by the project. The source establishes the open-system language; the [research dependencies](#textbook-background-and-research-dependencies) identify the separate scientific ingredients.

## Notation and conventions

A density operator describes both pure and mixed states. A pure vector $`|\psi\rangle`$ determines the density operator $`\psi=|\psi\rangle\langle\psi|`$. The partial trace $`\psi_S=\mathrm{Tr}_{S^c}\psi`$ contains all measurement probabilities accessible on subsystem $`S`$. Its nonzero eigenvalues are the squared nonzero Schmidt coefficients across the split between $`S`$ and its complement. Additional zero eigenvalues remain part of its spectrum on the full local Hilbert space.

| Source notation or concept | Convention used here |
|---|---|
| Dynamical map $`\mathcal E_{(t,t_0)}`$; homogeneous map $`\mathcal E_\tau`$ | For one time-independent generator, $`\rho(t)=e^{t\mathcal L}(\rho_0)`$. The exponential acts on density operators. |
| Generator $`\mathcal L_t`$ in Eq. (45) | The project uses a fixed $`\mathcal L`$, with no time-dependent control. |
| Eq. (46): rate $`\gamma_k`$ and operator $`V_k`$ | Write $`J_k=\sqrt{\gamma_k}V_k`$ and absorb the rate into the jump. Thus $`\gamma_k\mathcal D[V_k]=\mathcal D[J_k]`$. |
| Hamiltonian commutator | Use $`\hbar=1`$: $`H`$ is expressed in frequency units. If a physical Hamiltonian is given in energy units, replace it by $`H_{\rm phys}/\hbar`$. |
| Trace norm $`\lVert X\rVert_1`$ | The convergence criterion uses the unhalved norm. When discussing trace distance, use $`D_{\rm tr}(\rho,\sigma)=\tfrac12\lVert\rho-\sigma\rVert_1`$. |
| A steady state $`\rho_{\rm ss}`$ and a relaxing semigroup | Write $`\rho_*`$ for a stationary state. Global attraction means convergence to it from every initial density operator. |
| Target accuracy, added here | $`F_\psi(\rho)=\langle\psi\vert\rho\vert\psi\rangle`$ and $`\epsilon_\psi(\rho)=1-F_\psi(\rho)`$. This is squared Uhlmann fidelity when one argument is pure. |

For two pure states, infidelity equals the square of the half trace distance:

```math
1-|\langle\psi|\phi\rangle|^2
=D_{\rm tr}(\psi,\phi)^2.
```

For a mixed $`\rho`$ and a pure $`\psi`$, the equality is replaced by bounds; the construction uses $`D_{\rm tr}(\rho,\psi)\le\sqrt{1-F_\psi(\rho)}`$. These accuracy conventions are stated explicitly because neither an overlap amplitude nor its square should be silently substituted for the other.

## From a Lindblad equation to the accuracy question

The generator has the form

```math
\begin{aligned}
\mathcal L(\rho)
&=-i[H,\rho]
+\sum_a\left(
J_a\rho J_a^\dagger-\frac12\{J_a^\dagger J_a,\rho\}
\right),\\
J_a&=A_{a,S_a}\otimes I_{S_a^c}.
\end{aligned}
```

The operator $`A_{a,S_a}`$ acts on an allowed subsystem $`S_a\in\mathcal N`$. The identity on its complement makes the support restriction precise. The Hamiltonian $`H`$ may act globally. The number, strengths and forms of the supported jumps are optimized, and the physical Hilbert space is fixed.

A stationary state solves $`\mathcal L(\rho_*)=0`$. The optimization requires it to be the unique globally attractive stationary state, so its fidelity describes an output obtainable from any initial state. Define

```math
\mu=\mu_{\mathcal N}(\psi)
=\min_{S\in\mathcal N}\lambda_{\min}(\psi_S).
```

The minimum includes zero eigenvalues on the entire local Hilbert space. A positive $`\mu`$ therefore means that every allowed target marginal is full rank. The [theorem](../science/model.md#accuracy-theorem) is

```math
\boxed{
\frac{\mu}{2}
\le\epsilon_{\mathrm{opt}}(\psi,\mathcal N)
\le\mu
=\epsilon_{\mathrm{pure,opt}}(\psi,\mathcal N).
}
```

Here the first optimization permits mixed stationary outputs; the second requires a pure output. The theorem determines the pure optimum exactly and places the mixed optimum within a factor of two. It does not assert that either endpoint is the exact mixed optimum for every target.

### Why the smallest local eigenvalue appears

For a local matrix $`B`$, partial trace gives

```math
\|(B\otimes I)|\psi\rangle\|^2
=\mathrm{Tr}(\psi_S B^\dagger B)
\ge\lambda_{\min}(\psi_S)\mathrm{Tr}(B^\dagger B).
```

Thus a full-rank marginal prevents a nonzero local operator from annihilating the target. Every local direction carries some weight. For a pure stationary state, each jump must act as a scalar on its state vector; subtracting that scalar converts the condition into local annihilation. If all allowed marginals are full rank, every such centered jump must vanish. A generator containing only scalar jumps has no dissipative mechanism for global attraction.

There is also a geometric interpretation. Choose an allowed marginal and a normalized vector $`u`$ with the least possible weight $`\mu`$. With

```math
A=|u\rangle\langle u|_S\otimes I_{S^c},
\qquad
|\phi\rangle=\frac{(I-A)|\psi\rangle}{\sqrt{1-\mu}},
```

the state $`\phi`$ has an empty local direction, and

```math
1-|\langle\psi|\phi\rangle|^2=\mu.
```

No pure state with an empty direction on any allowed support can be closer. Consequently $`\mu`$ is exactly the pure-state infidelity distance to the rank-deficient set $`\mathcal Z_{\mathcal N}`$. The [pure-state proof](../science/converse.md#the-exact-pure-state-optimum) establishes this distance, and the [construction](../science/construction.md) shows that every state in this set can be made globally attractive with the permitted global control.

### Why a mixed stationary output cannot remove the error floor

The stationary output need not have the prescribed target as an eigenvector. The converse therefore starts at its actual dominant eigenvector $`\phi`$:

```math
\rho_*=(1-\delta)|\phi\rangle\langle\phi|+R,
\qquad
R\ge0,\quad R\phi=0,\quad\mathrm{Tr}R=\delta.
```

Only the case $`1-\delta>1/2`$ needs the detailed argument. Center each jump at $`\phi`$ by setting $`L_a=J_a-\langle\phi|J_a|\phi\rangle I`$. The diagonal Hamiltonian contribution vanishes because $`\phi`$ is an eigenvector of $`\rho_*`$. Stationarity then gives the [population balance](../science/converse.md#stationary-population-balance)

```math
\begin{aligned}
(1-\delta)\sum_a\|L_a\phi\|^2
&=\sum_a\langle\phi|L_aRL_a^\dagger|\phi\rangle\\
&\le\delta\sum_a\|L_a^\dagger\phi\|^2.
\end{aligned}
```

The left side is loss from the dominant component. The right side bounds how much the remaining population can replenish it. Local marginal eigenvalues bound both terms, forcing at least one active support to satisfy $`\lambda_{\min}(\phi_S)\le\delta`$. Increasing the Hamiltonian strength does not alter this diagonal balance.

The last step must relate $`\phi`$ to the original $`\psi`$. A projector onto that small local direction has probability at least $`\mu`$ in $`\psi`$ and at most $`\delta`$ in $`\phi`$. For $`\delta<\mu`$, splitting the overlap into the two measurement outcomes and applying Cauchy–Schwarz gives

```math
|\langle\psi|\phi\rangle|
\le\sqrt{\mu\delta}+\sqrt{(1-\mu)(1-\delta)}.
```

Writing $`c=|\langle\psi|\phi\rangle|`$, the residual state also obeys

```math
F_\psi(\rho_*)
\le(1-\delta)c^2+\delta(1-c^2).
```

Combining these inequalities yields the error floor $`\mu/2`$, as shown in the [mixed-state bound](../science/converse.md#the-mixed-state-error-bound). If $`\delta\ge\mu`$, the simpler inequality $`F_\psi(\rho_*)\le1-\delta`$ already suffices. This argument explains the role of the moving stationary eigenvector; replacing it by the target would omit a necessary step.

## Worked example: one reset channel and a global Hamiltonian

Consider two qubits, labelled first and second, with dissipation allowed only on the first. Choose

```math
|\psi\rangle
=\frac{\sqrt3}{2}|00\rangle+\frac12|11\rangle,
\qquad
\psi_{\{1\}}
=\begin{pmatrix}3/4&0\\0&1/4\end{pmatrix}.
```

The invariant is $`\mu=1/4`$. Hence every admissible attractive stationary output has infidelity at least $`1/8`$, while the optimal pure output has infidelity exactly $`1/4`$.

Discarding the smaller local component gives $`|\phi\rangle=|00\rangle`$. Take

```math
\begin{aligned}
J&=|0\rangle\langle1|\otimes I,\\
H&=h\left(|10\rangle\langle11|+|11\rangle\langle10|\right)\\
&\quad+h\left(|11\rangle\langle01|+|01\rangle\langle11|\right),
\qquad h>0.
\end{aligned}
```

The jump resets the first qubit. It sends $`|10\rangle`$ to $`|00\rangle`$ and $`|11\rangle`$ to $`|01\rangle`$. The Hamiltonian connects the three unwanted basis states along the path $`|10\rangle,\ |11\rangle,\ |01\rangle`$ and leaves $`|00\rangle`$ unchanged. It is a permitted two-qubit Hamiltonian, with norm $`\sqrt2\,h`$.

Both $`J|00\rangle=0`$ and $`H|00\rangle=0`$, so $`P=|00\rangle\langle00|`$ is stationary. With $`H=0`$ the second qubit would retain its initial state, leaving many stationary outputs. The couplings above remove that freedom.

To see uniqueness directly, stationarity of the $`|00\rangle`$ population gives

```math
0=\langle10|\rho_*|10\rangle.
```

Positivity forces the entire $`|10\rangle`$ row and column to vanish. The $`|10\rangle`$ row of the stationary equation then forces the $`|11\rangle`$ row to vanish; the next row forces the $`|01\rangle`$ row to vanish. The jump-gain term has vanishing rows at these steps because it is itself positive, and $`J^\dagger J=|1\rangle\langle1|\otimes I`$ is diagonal in this basis. Unit trace leaves only $`\rho_*=P`$.

For convergence, the desired population satisfies

```math
\frac{d}{dt}\langle00|\rho(t)|00\rangle
=\langle10|\rho(t)|10\rangle\ge0.
```

Time averages have stationary subsequential limits in the finite-dimensional state space. Uniqueness makes every such limit equal to $`P`$. Since the desired population is monotone, it must tend to one, and the pure-state trace-distance bound gives $`\|\rho(t)-P\|_1\to0`$. This is the finite example of the [general convergence argument](../science/construction.md#global-attraction).

The attainable output has

```math
F_\psi(P)=|\langle\psi|00\rangle|^2=\frac34,
\qquad
\epsilon_\psi(P)=\frac14.
```

Operationally, $`F_\psi(P)`$ is the success probability of the projector measurement onto the desired target. The theorem permits an optimized mixed output to improve this value, but requires $`F_\psi(\rho_*)\le7/8`$. This example does not determine the exact mixed optimum.

## From pure-target fidelity to Gibbs accuracy

The same source supports a thermal application without changing the educational anchor. RH §5.2 gives the GKLS equation, and §5.4 separates a stationary solution from a relaxing semigroup. RH §§6.2.1 and 6.2.8 provide the energy-basis and thermal-population language. These background sections do not contain this project's marginal-spectrum theorem or the companion's finite certificate.

Let $`H_0`$ denote a target energy Hamiltonian with unique ground vector $`|g\rangle`$, while $`K`$ denotes the independently controlled coherent term. The Gibbs state has ground probability $`1-\delta_\beta`$. This repository's existing theorem bounds the stationary ground infidelity below by $`\mu(g)/2`$ for any supported representation with a nonscalar jump. A ground-projector measurement turns the probability difference directly into

```math
D_{\mathrm{tr}}(\sigma,\rho_\beta)
\ge[\mu(g)/2-\delta_\beta]_+.
```

The [self-contained corollary](../science/gibbs-corollary.md) derives that step and supplies the exact conventions. It is a trace-distance statement about a mixed thermal target obtained from the inherited pure-target theorem. The [companion certificate](https://github.com/GoGoKo699/Gibbs-Cancellation-Obstruction/tree/7261788af6b88ba30222dc5e5fafb93337d09876/verification/ground-thermal) rigorously supplies the ground marginal weights and thermal deficit for an interacting five-qubit example; those numerical inputs and its stronger ground-population forms are project-specific material beyond RH.

At exact Gibbs stationarity, $`|g\rangle`$ is already a stationary density-matrix eigenvector. Its diagonal commutator vanishes for any $`K`$, so population balance gives stronger exact-target tests without an estimate of coherent strength. Conversely, a positive local dissipator with zero energy-population drift can have its off-diagonal drift cancelled by a generally global $`K`$ when the Gibbs spectrum is simple. This is the established [spectral stabilizability construction](../references/RELATED_WORK.md#linowski2023). The companion's positive reservoir and coercivity make that completion attractive at high temperature; its local-$`K`$ theorem excludes that resource choice.

The example therefore connects one inherited fidelity law to a robust cold approximation floor and a separately certified high/cold exact-feasibility comparison. It does not infer an exact transition or efficient implementation. The [resource account](../science/resources.md#local-and-global-coherent-control-for-gibbs-targets) retains the distinction between stationary accuracy, physical coherent support and the cost of implementing $`K`$.

## Textbook background and research dependencies

The selected source supplies channels, semigroups, generators and the distinction between stationarity and relaxation. The additional research citations below attribute the mathematical ingredients used to reach this project's result; they do not introduce further educational anchors.

| Ingredient | Provenance and its precise role |
|---|---|
| Exact full-rank marginal obstruction | [Karuvade et al. (2018), Theorem 4.1 and Remark 4.2](../references/RELATED_WORK.md#karuvade2018) supply the relevant exact DQLS obstruction. The present pure-state argument and its enlarged global-Hamiltonian setting are made explicit in the [converse](../science/converse.md#the-exact-pure-state-optimum). |
| Stationary population balance | [Linowski et al. (2023), §III, Eqs. (31)–(33)](../references/RELATED_WORK.md#linowski2023) provide the inherited spectral mechanism. The local marginal estimate and the comparison with a possibly different target complete the present fidelity bound. |
| Hamiltonian-assisted attraction | [Ticozzi and Viola (2009), §4.1, Theorem 2](../references/RELATED_WORK.md#ticozzi2009) give the general existence principle. The project supplies a particular path Hamiltonian and proves its uniqueness and attraction directly. |
| Random marginal concentration | [Hayden, Leung and Winter (2006), Lemma III.4](../references/RELATED_WORK.md#hayden2006) supplies the probability estimate used in the [Haar consequence](../science/consequences.md#haar-random-targets-a-finite-probability-bound). It is separate from the open-system foundation. |
| Existing local-cooling benchmark | [Žnidarič (2015), §§III–IV](../references/RELATED_WORK.md#znidaric2015) already establishes a stronger optimized ceiling for its two-qubit singlet setting. The universal theorem here does not improve every special-case constant. |

The source-to-result gap is therefore explicit: the open-system framework must be combined with locality in the physical tensor product, extremal marginal eigenvalues, ordinary target fidelity and a constructive attraction argument. The [complete attribution account](../references/RELATED_WORK.md) records which claims are inherited and which statements are proved here.

## Scope that matters for interpreting the result

The support constraint concerns the **effective jump operators**. An admissible generator must have at least one representation with each jump supported on an allowed subsystem. Mixing equivalent jump operators can change their displayed supports, so the condition is an existence statement about a representation. A collective jump $`A\otimes I+I\otimes B`$ generally has a larger support than either term separately.

The microscopic discussion in source §6.2.1 resolves bath couplings into energy-transition operators. Those operators can involve global energy projectors. Consequently local microscopic coupling does not, by itself, establish the effective-support assumption used here; see the [resource discussion](../science/resources.md#microscopic-bath-couplings-and-effective-jumps).

Global coherent control is an essential resource in the upper construction. The path basis depends on the full target state. A bounded Hamiltonian norm does not imply a short description, geometric locality or efficient implementation. The proof establishes asymptotic attraction and stationary accuracy, without a uniform relaxation-time guarantee.

The physical Hilbert space is fixed and the generator is time independent. Reservoir degrees of freedom have already been eliminated; a retained auxiliary register or additional local levels changes the optimization. Full-system jump support is formally allowed, but then a pure target's full-system marginal has a kernel and $`\mu=0`$. Proper supports are the regime in which a nonzero locality obstruction can arise.

For the resulting support-size laws, including uniform marginals and typical Haar states, continue to [Consequences](../science/consequences.md). For the precise resource and implementation boundaries, use [Resources and physical scope](../science/resources.md). The [verification guide](../verification/README.md) gives reproducible finite examples alongside the universal proofs.
