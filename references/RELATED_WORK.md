# Related work and attribution

[Scientific model](../science/model.md) · [Converse](../science/converse.md) · [Construction](../science/construction.md) · [Consequences](../science/consequences.md) · [Bibliography](references.bib)

The result developed here is a quantitative stationary-accuracy law for arbitrary pure targets under individually supported Lindblad jumps and unrestricted global coherent control:

```math
\frac{\mu_{\mathcal N}(\psi)}2
\le\epsilon_{\mathrm{opt}}(\psi,\mathcal N)
\le\epsilon_{\mathrm{pure,opt}}(\psi,\mathcal N)
=\mu_{\mathcal N}(\psi),
\qquad
\mu_{\mathcal N}(\psi)
=\min_{S\in\mathcal N}\lambda_{\min}(\psi_S).
```

The exact pure-state locality obstruction, spectral population balance and general Hamiltonian-assisted attraction are established ingredients. The additional statement controls ordinary fidelity to an arbitrary target even when the stationary state is mixed and its dominant eigenvector differs from the target. It compares that mixed optimum with an attainable pure approximation, uniformly in dimension and the support family. The [resource account](../science/resources.md) specifies the physical assumptions.

## Where the main ingredients enter

| Ingredient or comparison | Source | Role here |
|---|---|---|
| A quantitative local-cooling ceiling for a two-qubit singlet | [Žnidarič 2015](#znidaric2015) | Closest concrete optimized fidelity benchmark; stronger constants for its special target |
| Full-rank neighborhood marginals obstruct exact DQLS preparation | [Karuvade et al. 2018](#karuvade2018) | Exact rank obstruction underlying the pure-state geometry |
| Diagonal stationarity in a density-matrix eigenvector | [Linowski et al. 2023](#linowski2023) | Inherited population-balance mechanism in the mixed-state converse |
| Constant Hamiltonian control can make a suitable invariant subspace attractive | [Ticozzi and Viola 2009](#ticozzi2009) | Established existence principle realized explicitly after Schmidt truncation |
| Concentration of extremal marginal eigenvalues | [Hayden et al. 2006](#hayden2006) | Inherited estimate used in the Haar-target consequence |

<a id="znidaric2015"></a>
## Optimized local cooling of a singlet

**Marko Žnidarič, “Geometry of local quantum dissipation and fundamental limits to local cooling,” Physical Review A 91, 052107 (2015).** [Published article](https://doi.org/10.1103/PhysRevA.91.052107) · [arXiv:1501.03453v2](https://arxiv.org/pdf/1501.03453v2).

Section III optimizes a two-qubit singlet's stationary fidelity over arbitrary two-qubit Hamiltonians and dissipation acting on one qubit. It reports the optimal value, approached as a limit,

```math
F_{\mathrm{singlet}}^{\mathrm{sup}}
=\frac{3+\sqrt5}{8}\simeq0.6545.
```

Section IV already interprets this ceiling as a restriction on local cooling and as a way to infer nonlocal dissipation from sufficiently high stationary singlet fidelity. The present work does not introduce those physical ideas.

For this target and a one-qubit allowed support, $`\mu=1/2`$, so our universal converse yields only $`F\le3/4`$. It does not improve that special-case optimum. Its different contribution is the general target-dependent characterization through local marginal spectra, together with a pure upper construction and the factor-two comparison between mixed and pure approximations.

<a id="karuvade2018"></a>
## Exact dissipative quasi-local stabilization

**Salini Karuvade, Peter D. Johnson, Francesco Ticozzi and Lorenza Viola, “Generic pure quantum states as steady states of quasi-local dissipative dynamics,” Journal of Physics A: Mathematical and Theoretical 51, 145304 (2018).** [Published article](https://doi.org/10.1088/1751-8121/aaad1a) · [arXiv:1711.11142](https://arxiv.org/pdf/1711.11142).

Theorem 4.1 establishes an exact generic-state DQLS obstruction when each neighborhood is no larger in Hilbert-space dimension than its complement. Remark 4.2 applies the obstruction to every pure target with full-rank neighborhood marginals. Section 4.2 obtains arbitrarily accurate approximations in settings where DQLS states instead have full measure.

These are exact structural foundations. The present optimization allows arbitrary global Hamiltonians and mixed stationary outputs. Its error floor quantifies the full-rank-marginal obstruction in ordinary target infidelity. A rank-deficient marginal is sufficient for exact stabilization in this enlarged coherent-control model; it need not be sufficient for purely dissipative QL stabilization.

<a id="linowski2023"></a>
## Spectral stabilizability and population balance

**Tomasz Linowski, Łukasz Rudnicki and Clemens Gneiting, “Spectral stabilizability,” Physical Review A 107, 042218 (2023).** [Published article](https://doi.org/10.1103/PhysRevA.107.042218) · [arXiv:2212.12245v2](https://arxiv.org/pdf/2212.12245v2).

Section II, Proposition 1, gives necessary and sufficient spectral conditions for stabilizability; Eq. (5) supplies a counteracting global Hamiltonian, with antecedents credited there. For a simple target spectrum this reduces to zero dissipative energy diagonal. Section III, Eqs. (31)–(33), uses diagonal dissipative balance to constrain the population of a chosen pure constituent of a stationary mixture. Equations (45)–(47) explicitly distinguish a target retained as an eigenvector from a fidelity-optimal mixed state whose eigenvectors rotate.

Our [converse](../science/converse.md) inherits that balance condition and applies it at the actual dominant stationary eigenvector. Local marginal eigenvalue bounds force at least one active marginal of that eigenvector to have a small eigenvalue. A binary measurement then relates this marginal to the prescribed target. This step controls ordinary target fidelity without assuming that the target is a stationary eigenvector.

<a id="ticozzi2009"></a>
## Hamiltonian-assisted global attraction

**Francesco Ticozzi and Lorenza Viola, “Analysis and synthesis of attractive quantum Markovian dynamics,” Automatica 45, 2002–2009 (2009).** [Published article](https://doi.org/10.1016/j.automatica.2009.05.005) · [arXiv:0809.0613v1](https://arxiv.org/pdf/0809.0613v1).

Section 4.1, Theorem 2, characterizes when an invariant target subspace can be made attractive by arbitrary constant Hamiltonian control: its full orthogonal complement must not be invariant. The principle is also restated as Theorem 2 in [Ticozzi, Lucchese, Cappellaro and Viola (2012)](https://doi.org/10.1109/TAC.2012.2195858), with an [author-hosted full text](https://web.mit.edu/pcappell/www/pubs/Ticozzi12.pdf).

After truncation, our target $`\phi`$ satisfies $`L\phi=0`$ and $`L^\dagger\phi\ne0`$. The latter supplies a nonzero transition into the target, so the complementary subspace is not invariant. The established theorem therefore supplies Hamiltonian-assisted attraction. The [construction](../science/construction.md) gives an explicit Jacobi-chain realization and a self-contained positivity-and-convergence proof. General Hamiltonian-assisted attraction is an inherited result.

<a id="hayden2006"></a>
## Concentration of random marginals

**Patrick Hayden, Debbie W. Leung and Andreas Winter, “Aspects of generic entanglement,” Communications in Mathematical Physics 265, 95–117 (2006).** [Published article](https://doi.org/10.1007/s00220-006-1535-6) · [arXiv:quant-ph/0407049v2](https://arxiv.org/pdf/quant-ph/0407049v2).

Lemma III.4 supplies the extremal-eigenvalue estimate used in the [Haar-target consequence](../science/consequences.md). That page states the full-rank regime, converts the source's base-two exponential convention, and derives a simultaneous support-family bound. The concentration estimate itself is not new.

<a id="pocklington2024"></a>
## Collective local-sum jumps and relaxation

**Andrew Pocklington and Aashish A. Clerk, “Universal Time-Entanglement Trade-off in Open Quantum Systems,” PRX Quantum 5, 040305 (2024).** [Published article](https://doi.org/10.1103/PRXQuantum.5.040305) · [arXiv:2404.03625v2](https://arxiv.org/pdf/2404.03625v2).

Section II, Eq. (6), permits collective jumps $`A\otimes I+I\otimes B`$. The paper relates pure steady-state entanglement to relaxation times and identifies an obstruction at maximal entanglement. Such a collective jump generally acts on both factors, and cancellation between its two terms can support entangled dark states.

The present theorem instead constrains each jump's individual support and bounds stationary infidelity. It neither implies the collective-jump time–entanglement law nor establishes a relaxation-time bound.

<a id="zhan2026"></a>
## Strict support and quasilocal ground-state preparation

**Yongtao Zhan, Zhiyan Ding, Jakob Huhn, Johnnie Gray, John Preskill, Garnet Kin-Lic Chan and Lin Lin, “Rapid Quantum Ground State Preparation via Dissipative Dynamics,” Physical Review X 16, 011004 (2026).** [Published article](https://doi.org/10.1103/wzb3-dbg9) · [arXiv:2503.15827v3](https://arxiv.org/pdf/2503.15827v3).

Section II, under “Quasilocality of the jump operator,” recalls the exact pure-state restrictions imposed by strictly local jumps and explains how filtered quasilocal jumps allow a broader class of targets. This distinction is important here: exponentially decaying tails are not strict support on a prescribed finite region. The present feasibility law is compatible with those preparation results and does not replace their mixing-time analysis.

**Qicheng Tang, Ruhanshi Barad and Xueda Wen, “Locality in Dissipative Ground-State Preparation,” arXiv:2610.40628 (2026).** [Primary abstract](https://arxiv.org/abs/2610.40628). Its stated setting uses free-fermion targets, quadratic Lindbladians and exponentially local linear jumps for exact preparation. The locality notion and jump class differ from the arbitrary finite-dimensional, strictly supported model considered here.

<a id="rivas2012"></a>
## Dynamical maps and microscopic assumptions

**Ángel Rivas and Susana F. Huelga, “Open Quantum Systems: An Introduction,” SpringerBriefs in Physics, first edition (2012).** [Publisher](https://doi.org/10.1007/978-3-642-23354-8) · [Author preprint, arXiv:1104.5242v2](https://arxiv.org/pdf/1104.5242v2).

Sections 4–5 of this fixed preprint discuss quantum dynamical maps, Markovian generators and steady states. Section 6.2, especially Sec. 6.2.1, explains the weak-coupling energy-transition decomposition used in our [microscopic scope discussion](../science/resources.md#microscopic-bath-couplings-and-effective-jumps). Local microscopic couplings and local effective jumps are separate assumptions.

<a id="autonomous-noise-floor"></a>
## Relation to a public stationary-noise analysis

The public scientific account [Autonomous Entanglement Noise Floor](https://github.com/GoGoKo699/Autonomous-Entanglement-Noise-Floor/tree/04754e635f2f3f30051f9d01dcd2251af4372e09) treats collective local-sum jumps, a fixed engineered dissipative-strength budget and compulsory local dephasing near a maximally entangled target. Its [mixed-state rigidity proof](https://github.com/GoGoKo699/Autonomous-Entanglement-Noise-Floor/blob/04754e635f2f3f30051f9d01dcd2251af4372e09/science/rigidity.md) uses the same leading-eigenvector and spectral-balance starting point, explicitly credited there to Linowski et al.

The common argument is credited as shared. The resulting laws concern different physical questions: a noise-versus-strength optimum for collective local-sum reservoirs there, and a target-marginal-spectrum optimum for individually supported reservoirs here. The present theorem introduces neither a mandatory noise channel nor a strength budget, and the collective local-sum theorem does not supply its all-target characterization.

<a id="gibbs-cancellation"></a>
## Gibbs approximation and coherent-control locality

The sister account [Gibbs Cancellation Obstruction](https://github.com/GoGoKo699/Gibbs-Cancellation-Obstruction/tree/5666fe5ede05e8d5ea4d8caf1f9641c2170341f8) studies strict single-site/adjacent-pair generators on an open five-qubit chain. Its original cancellation theorem restricts both coherent terms and individual jumps to those supports. For each fixed positive inverse temperature it identifies a generic nearest-neighbor Hamiltonian family whose stationary local-superoperator kernel contains only the Hamiltonian commutator. Its explicit integer witness has the stated obstruction at every positive algebraic inverse temperature. These quantifiers are separate from its continuous high-temperature positive-reservoir certificate.

The [Gibbs corollary](../science/gibbs-corollary.md) uses this repository's existing pure-target stationary bound to obtain half-trace-distance error at least $`[\mu(g)/2-\delta_\beta]_+`$. That bound remains inherited from this project's [converse](../science/converse.md), rather than becoming a second all-target theorem in the companion. Keeping the prescribed Gibbs ground eigenvector also avoids the moving-eigenvector step and permits stronger exact-target population tests.

The companion is the authoritative home of the [explicit thermal certificate and full proof](https://github.com/GoGoKo699/Gibbs-Cancellation-Obstruction/blob/5666fe5ede05e8d5ea4d8caf1f9641c2170341f8/science/finite-temperature-feasibility.md): all nine ground marginals are full rank; four negative ground-population forms exclude genuine dissipation for every real $`\beta\ge12/5`$ even under global coherent control. Its inherited positive secular reservoir, completed by the established [Linowski et al. construction](#linowski2023), admits exact attractive Gibbs preparation for $`0\le\beta\le1/100`$ with global coherent control and the same individual jump support. The reservoir itself and its weak-coupling population-balance ingredients remain credited there. The added consequence is a certified finite-system feasibility comparison. It does not introduce local-cooling temperature floors, already discussed by [Žnidarič](#znidaric2015), or spectral coherent completion.

The local-$`K`$ obstruction and global-$`K`$ construction have different admissible coherent resources. Their distinction is essential at $`\beta=3/1000`$ and $`1/100`$, where the same target and jump supports yield an exact separation. The interval $`1/100<\beta<12/5`$ remains unresolved; neither witness monotonicity nor the inherited fidelity bound determines an exact crossover or monotone feasible set. Larger supports, other system sizes and additional physical degrees of freedom are not covered by this finite example.

## Contribution boundary

The supported addition is the factor-two stationary-infidelity law and its comparison with the exact pure optimum. The uniform-marginal and Haar consequences follow from that law with their stated spectral assumptions. The thermal trace-distance floor is another direct corollary; the companion owns its explicit certificate and full finite-temperature feasibility comparison. Neither sharper special-case cooling constants, general Hamiltonian-assisted stabilization, random-state concentration, nor an efficient implementation of the attaining Hamiltonian is claimed as a new result.
