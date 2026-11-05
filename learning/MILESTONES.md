# Thirty milestones for dissipative locality and stationary accuracy

[Scientific model](../science/model.md) · [Educational anchor and bridge](ANCHOR.md) · [Converse](../science/converse.md) · [Construction](../science/construction.md) · [Consequences](../science/consequences.md)

A reservoir may act on a small part of a quantum device while the Hamiltonian couples the whole device. This map connects that physical setting to the project's central result: the smallest eigenvalue of an allowed target marginal determines the optimal pure stationary approximation exactly, and the optimal mixed stationary approximation within a factor of two.

The map contains exactly **M01–M30**, organized by the science rather than by a reader's prior experience. The first **11 milestones** build the objects, dynamics, accuracy convention and physical assumptions into a complete optimization problem. The remaining **19 milestones** connect the pure-state geometry, mixed-state converse, explicit attractive construction and many-body consequences. The larger second phase reflects the work needed to join these distinct arguments into one stationary-accuracy law. M11 and M30 synthesize their respective phases.

| Phase | Milestones | Progression |
| --- | --- | --- |
| Background/preliminaries | M01–M11 | States and subsystem spectra, then dynamics and accuracy, then the complete physical model |
| Narrative/innovation | M12–M30 | A local spectral invariant, then converse and construction, then consequences, scope and synthesis |

## Source convention and limits

**RH** means the single educational anchor, Ángel Rivas and Susana F. Huelga, *Open Quantum Systems: An Introduction* (2012), specifically [arXiv:1104.5242v2](https://arxiv.org/pdf/1104.5242v2), dated 9 February 2012. Section and theorem numbers below refer to that fixed preprint. The section links open its relevant PDF pages; they do not require reading the source from beginning to end. [ANCHOR.md](ANCHOR.md) supplies the notation and source-to-project bridge.

The main background route uses RH §§2.1, 2.2, 2.3, 3, the opening of §4, §§4.1, 4.2, 4.3, 4.5, 5.2 and 5.4. Sections 6.2.1 and 6.4.1 explain the microscopic-locality boundary. The remaining microscopic and non-Markovian chapters are not prerequisites for this map.

An **anchor context** pointer identifies the relevant foundation, not a claim that RH proves the milestone's project-specific conclusion. In particular:

- RH uses density operators and Schmidt decomposition; the project bridge supplies the conventions needed here. RH §4.3 treats trace-norm contraction, while the project's fidelity convention and binary-overlap argument are stated and derived in the project sources.
- The invariant, distance to the rank-deficient set, factor-two converse and explicit reset-plus-Hamiltonian construction have their authoritative derivations in `science/`.
- Graph-state calculations, the extremal-eigenvalue concentration estimate and its simultaneous-support consequence are outside the anchor's teaching route. Their project derivations and primary research attribution are linked where needed. Primary research citations do not introduce additional educational anchors.
- The map covers the connected understanding of the result. Specialist calculations, full proof details and implementation checks remain in their canonical sources.

## Phase I — Background/preliminaries

This phase starts with individual states and operations, then combines them into an autonomous preparation problem with a fixed tensor decomposition, explicit accuracy objective and precise resource assumptions.

<a id="m01"></a>
### M01 — States and observable probabilities

- **Phase:** Background/preliminaries.
- **Central question:** What mathematical object describes the state that a preparation process is meant to produce?
- **Understanding target:** Interpret a density operator as a positive operator of unit trace, distinguish a pure state from a mixed state, and connect a projector's expectation to the probability of its outcome. Identify the target vector and the actual output state as different objects.
- **Dependencies and story role:** None within this map. This supplies the state and probability language used by every later milestone.
- **Conceptual connection:** The stationary accuracy objective ultimately asks how much probability the output assigns to the prescribed pure target.
- **Sources:** [RH §3][rh-3] uses pure and mixed states in their evolution equations; the definitions and accuracy convention are supplied in the project [target invariant](../science/model.md#the-target-invariant), [stationary optimization](../science/model.md#the-stationary-optimization) and [anchor bridge](ANCHOR.md).

<a id="m02"></a>
### M02 — Subsystems, marginal states and operator support

- **Phase:** Background/preliminaries.
- **Central question:** How does a statement about a few physical sites become an operator statement on the entire device?
- **Understanding target:** Relate the tensor decomposition to partial trace, explain why a marginal predicts all measurements on its subsystem, and interpret $`A_S\otimes I_{S^c}`$ as an operator acting trivially outside its support. A support may contain separated sites and need not cover the system together with the other supports.
- **Dependencies and story role:** [M01](#m01). This gives physical meaning to the local regions that will constrain the dissipation.
- **Conceptual connection:** The same tensor decomposition determines both the admissible jumps and the target marginals entering the accuracy law.
- **Sources:** [RH §4, opening discussion and Eqs. (29)–(30)][rh-4]; project [admissible generators](../science/model.md#admissible-generators) and [locality of the generator](../science/resources.md#locality-is-a-property-of-the-generator).

<a id="m03"></a>
### M03 — Marginal spectra, Schmidt weights and kernels

- **Phase:** Background/preliminaries.
- **Central question:** What can a local spectrum reveal about a globally pure state?
- **Understanding target:** Connect the nonzero marginal eigenvalues to squared Schmidt coefficients, distinguish full rank from a kernel, and count zero eigenvalues on the entire subsystem Hilbert space. Explain why a support larger than its complement necessarily has a rank-deficient pure-state marginal.
- **Dependencies and story role:** [M02](#m02). This moves from the existence of a marginal to the spectral information that the theorem will use.
- **Conceptual connection:** A smallest eigenvalue measures the probability weight in a least-populated local direction; it is not interchangeable with entropy or with the smallest nonzero Schmidt weight.
- **Sources:** [RH §4.1, proof of Theorem 4.1, Eq. (33)][rh-4-1]; project [target invariant](../science/model.md#the-target-invariant) and [unequal subsystem dimensions](../science/examples.md#general-complex-targets-and-unequal-subsystem-dimensions).

<a id="m04"></a>
### M04 — Positivity as a quantitative tool

- **Phase:** Background/preliminaries.
- **Central question:** How do positive operators turn spectral information into bounds on transitions and overlaps?
- **Understanding target:** Distinguish operator, trace and Frobenius norms; interpret an operator inequality through quadratic forms; and understand why a zero quadratic form of a positive operator implies a kernel vector. Relate extremal eigenvalues to bounds on traces against a positive operator.
- **Dependencies and story role:** [M01](#m01), [M03](#m03). These are the shared linear-algebra tools for both the converse and the attraction proof.
- **Conceptual connection:** Positivity will prevent dissipative loss terms from canceling in a pure stationary state and will later propagate vanishing populations through the constructed Hamiltonian path.
- **Sources:** Anchor context: [RH §2.1][rh-2-1] and the Hilbert–Schmidt operator basis in [§5.2][rh-5-2]. Project derivations: [local spectral inequalities](../science/converse.md#a-small-eigenvalue-in-an-active-local-marginal) and [uniqueness by positivity](../science/construction.md#uniqueness-by-positivity).

<a id="m05"></a>
### M05 — Physical evolution maps

- **Phase:** Background/preliminaries.
- **Central question:** What makes an open-system evolution a physical map on every initial state?
- **Understanding target:** Explain trace preservation and complete positivity, and distinguish a channel defined for arbitrary system states from a reduced evolution tied to a particular initial system–environment correlation. Understand the role of a mathematical reference system in complete positivity.
- **Dependencies and story role:** [M02](#m02), [M04](#m04). The map now connects the state space to permissible dynamical transformations.
- **Conceptual connection:** The project optimizes autonomous generators on one fixed physical system. Complete positivity does not itself supply an additional retained register as a preparation resource.
- **Sources:** [RH §§4.1–4.2][rh-4-1], especially [§4.2][rh-4-2]; project [admissible generators](../science/model.md#admissible-generators) and [state space and autonomy](../science/resources.md#state-space-autonomy-and-approximation).

<a id="m06"></a>
### M06 — Autonomous evolution and its generator

- **Phase:** Background/preliminaries.
- **Central question:** How does one time-independent rule specify the evolution at every later time?
- **Understanding target:** Relate the master equation to $`e^{t\mathcal L}`$, understand the semigroup composition law, and distinguish a fixed generator from a time-dependent preparation schedule. Recognize that the exponential acts on density operators rather than only on state vectors.
- **Dependencies and story role:** [M04](#m04), [M05](#m05). This turns a family of physical maps into the autonomous dynamics studied by the project.
- **Conceptual connection:** Stationarity, convergence and rescaling of time can all be formulated directly in terms of the generator.
- **Sources:** [RH §2.2][rh-2-2], [§2.3][rh-2-3] and [§4.5][rh-4-5]; project [stationary optimization](../science/model.md#the-stationary-optimization) and [rates and coherent strength](../science/resources.md#rates-and-coherent-strength).

<a id="m07"></a>
### M07 — Hamiltonian terms, jumps and representation freedom

- **Phase:** Background/preliminaries.
- **Central question:** Which parts of a Lindblad generator describe coherent motion and dissipative transitions?
- **Understanding target:** Read the Hamiltonian commutator and a jump dissipator, understand absorption of a positive rate into its jump, and distinguish the generator from a particular list of jump operators. Explain why scalar centering preserves a supported tensor form while general mixing of jump labels may obscure a local representation.
- **Dependencies and story role:** [M06](#m06), with the support definition from [M02](#m02). This identifies the control variables of the optimization.
- **Conceptual connection:** Admissibility requires the existence of a supported Lindblad representation; the theorem does not assign a physical cost to one arbitrary gauge choice.
- **Sources:** [RH §5.2, Theorem 5.1 and Eq. (46)][rh-5-2]; the project supplies the support and gauge interpretation in [admissible generators](../science/model.md#admissible-generators) and [locality of the generator](../science/resources.md#locality-is-a-property-of-the-generator).

<a id="m08"></a>
### M08 — Stationarity, attraction and spectral decay

- **Phase:** Background/preliminaries.
- **Central question:** What distinguishes a state that remains unchanged from a state reached from every initial condition?
- **Understanding target:** Separate stationarity, uniqueness and global attraction; relate a stationary state to a zero generator mode; and interpret the relaxation criterion involving the remaining eigenvalues. Keep stationary accuracy distinct from how long convergence takes.
- **Dependencies and story role:** [M06](#m06), [M07](#m07). This defines the required output behavior and the stronger class covered by the converse.
- **Conceptual connection:** A pure Hamiltonian eigenstate may be stationary without being attractive. The project needs a nontrivial dissipator for its stationary-state converse and a convergence proof for its attaining construction.
- **Sources:** [RH §5.4, Theorems 5.3–5.4][rh-5-4]; project [stationary optimization](../science/model.md#the-stationary-optimization), [accuracy theorem](../science/model.md#accuracy-theorem) and [verification interpretation](../verification/README.md#interpretation).

<a id="m09"></a>
### M09 — The accuracy being optimized

- **Phase:** Background/preliminaries.
- **Central question:** How is closeness to a prescribed pure target measured when the output may be mixed?
- **Understanding target:** Interpret $`F_\psi(\rho)=\langle\psi\vert\rho\vert\psi\rangle`$ and infidelity $`1-F_\psi(\rho)`$. Distinguish this overlap from an eigenvalue assigned to the target, and distinguish infidelity from trace distance while recognizing the relation for pure states.
- **Dependencies and story role:** [M01](#m01), [M03](#m03), [M04](#m04). This supplies the performance metric after the dynamical requirements have been defined.
- **Conceptual connection:** A stationary mixture can have substantial target overlap even when its leading eigenvector differs from the target; the mixed-state proof must control both effects.
- **Sources:** Anchor context: [RH §4.3][rh-4-3] treats trace-norm contraction. The fidelity convention and required geometric relations come from the project [stationary optimization](../science/model.md#the-stationary-optimization) and [pure and mixed approximations](../science/consequences.md#pure-and-mixed-stationary-approximations).

<a id="m10"></a>
### M10 — Microscopic coupling and effective dissipative locality

- **Phase:** Background/preliminaries.
- **Central question:** Does attaching a reservoir to a small physical region guarantee a jump with that same support?
- **Understanding target:** Explain how energy-transition components of a coupling operator depend on the system Hamiltonian's spectral projectors. Distinguish strict effective support from microscopic coupling locality, quasilocal tails and a coherent sum of operators on separate regions.
- **Dependencies and story role:** [M02](#m02), [M07](#m07). This places the mathematical locality assumption inside a physical modeling problem.
- **Conceptual connection:** The theorem applies after an effective generator is justified; a global interacting Hamiltonian can alter the support of jumps arising from a microscopic derivation.
- **Sources:** [RH §6.2.1][rh-6-2-1] and [§6.4.1][rh-6-4-1]; project [microscopic couplings and effective jumps](../science/resources.md#microscopic-bath-couplings-and-effective-jumps) and [strict versus quasilocal support](../references/RELATED_WORK.md#zhan2026).

<a id="m11"></a>
### M11 — Background synthesis: the preparation problem

- **Phase:** Background/preliminaries.
- **Central question:** What precisely is fixed, what can be designed, and what must the resulting dynamics achieve?
- **Understanding target:** Specify the physical tensor factors, target, allowed support family, arbitrary global Hamiltonian, freely designed supported channels and rates, and globally attractive stationary output as one optimization problem. State the fidelity convention and distinguish this optimization from the stronger converse over all stationary states with a nonscalar jump.
- **Dependencies and story role:** [M05](#m05), [M08](#m08), [M09](#m09), [M10](#m10), together with their dependencies. This is the phase synthesis: local objects and dynamical assumptions now define a complete scientific question.
- **Conceptual connection:** The model deliberately permits extensive coherent control while retaining one explicit constraint on each dissipative channel and one fixed physical state space.
- **Sources:** Anchor synthesis: [RH §§4.5][rh-4-5], [5.2][rh-5-2], [5.4][rh-5-4] and [6.2.1][rh-6-2-1]. Canonical project sources: [model](../science/model.md) and [what is fixed and optimized](../science/resources.md#what-is-fixed-and-what-is-optimized).

## Phase II — Narrative/innovation

This phase begins with one local spectral quantity. It first builds a converse for arbitrary stationary outputs, then turns the closest pure approximation into an attractive state. The final milestones connect the theorem to target families, dissipative support, physical resources and the limits of its evidence.

<a id="m12"></a>
### M12 — The target's least local eigenvalue

- **Phase:** Narrative/innovation.
- **Central question:** Which feature of the target identifies the least costly local direction to remove?
- **Understanding target:** Interpret $`\mu_{\mathcal N}(\psi)=\min_{S\in\mathcal N}\lambda_{\min}(\psi_S)`$, including its minimization over the allowed family and all zero eigenvalues. Explain the bounds $`0\le\mu\le1/2`$ and distinguish one rank-deficient allowed marginal from full rank on every allowed marginal.
- **Dependencies and story role:** [M03](#m03), [M09](#m09), [M11](#m11). This introduces the proposed controlling quantity before assigning it an operational meaning.
- **Conceptual connection:** A local spectral minimum will become a distance to feasible pure outputs and a lower bound on arbitrary stationary infidelity.
- **Sources:** Anchor context: [RH §4.1, Eq. (33)][rh-4-1]. The invariant and its quantifiers are defined in the project [target invariant](../science/model.md#the-target-invariant).

<a id="m13"></a>
### M13 — The exact rank obstruction for pure outputs

- **Phase:** Narrative/innovation.
- **Central question:** Why can a nontrivial supported jump not preserve a pure state with a full-rank marginal on its support?
- **Understanding target:** Connect pure-state stationarity to a sum of nonnegative jump variances, then to a common-eigenvector condition. Explain why a nonzero centered local jump requires a kernel in the corresponding pure output marginal.
- **Dependencies and story role:** [M04](#m04), [M07](#m07), [M12](#m12). This identifies a necessary geometric property of every feasible pure stationary output.
- **Conceptual connection:** The established exact locality obstruction becomes the starting point for quantifying approximation error rather than only deciding exact feasibility.
- **Sources:** Anchor context: [RH §§4.1][rh-4-1] and [5.2][rh-5-2]. Project proof: [necessary rank deficiency](../science/converse.md#necessary-rank-deficiency); research attribution: [exact dissipative stabilization](../references/RELATED_WORK.md#karuvade2018).

<a id="m14"></a>
### M14 — Distance to a local rank defect

- **Phase:** Narrative/innovation.
- **Central question:** How close can a pure target be to a pure state with a kernel on at least one allowed marginal?
- **Understanding target:** Relate projection away from a local direction to lost target probability. Explain why deleting a minimum-weight local eigencomponent attains pure infidelity $`\mu`$, while every pure state with an allowed marginal kernel has at least that error.
- **Dependencies and story role:** [M03](#m03), [M04](#m04), [M09](#m09), [M13](#m13). This establishes a geometric optimum before its dynamical attainability is proved.
- **Conceptual connection:** Schmidt truncation supplies the candidate output, and the same local projector proves that no closer rank-deficient pure candidate exists.
- **Sources:** Anchor context: [RH §4.1, Eq. (33)][rh-4-1]. Project proof: [distance to the rank-deficient set](../science/converse.md#distance-to-the-rank-deficient-set).

<a id="m15"></a>
### M15 — A mixed output's actual leading eigenvector

- **Phase:** Narrative/innovation.
- **Central question:** What must replace the pure-output rank argument when the stationary output is mixed?
- **Understanding target:** Decompose the output into a dominant pure component of weight $`1-\delta`$ and a positive orthogonal remainder of trace $`\delta`$. Explain when this leading vector is unique and why it must be distinguished from the desired target.
- **Dependencies and story role:** [M08](#m08), [M09](#m09), [M14](#m14). This opens the mixed-state branch by identifying the state on which stationarity gives useful diagonal information.
- **Conceptual connection:** Approximation can come from both spectral mixing and rotation of the leading eigenvector. Ordinary target fidelity requires controlling them together.
- **Sources:** Anchor context: [RH §5.4][rh-5-4]. Project sources: [stationary population balance](../science/converse.md#stationary-population-balance), [mixed-state bound](../science/converse.md#the-mixed-state-error-bound) and [spectral-stabilizability comparison](../references/RELATED_WORK.md#linowski2023).

<a id="m16"></a>
### M16 — Population balance removes the Hamiltonian

- **Phase:** Narrative/innovation.
- **Central question:** Why can a converse allow an arbitrary global Hamiltonian without estimating its strength?
- **Understanding target:** Explain why a Hamiltonian commutator has zero diagonal expectation in a stationary density-matrix eigenvector. Use centered jumps to interpret the remaining equality as dissipative loss from the leading component balanced by influx from the remainder.
- **Dependencies and story role:** [M07](#m07), [M15](#m15). This isolates the inherited balance mechanism on which the mixed converse rests.
- **Conceptual connection:** The stationary equation permits cancellation among different channels, yet its diagonal balance compares nonnegative transition contributions and eliminates coherent strength from the bound.
- **Sources:** Anchor context: [RH §3, Eq. (19)][rh-3] and [§5.2][rh-5-2]. Project derivation: [stationary population balance, Eq. (1)](../science/converse.md#stationary-population-balance); attribution: [Linowski et al.](../references/RELATED_WORK.md#linowski2023).

<a id="m17"></a>
### M17 — Stationarity forces a small local eigenvalue

- **Phase:** Narrative/innovation.
- **Central question:** How does locality convert population balance into a constraint on the dominant eigenvector's marginals?
- **Understanding target:** Relate a supported jump's loss and influx norms to the minimum and maximum eigenvalues of the corresponding marginal. Explain why summing the resulting inequalities forces at least one active support to satisfy $`\lambda_{\min}(\phi_S)\le\delta`$.
- **Dependencies and story role:** [M04](#m04), [M12](#m12), [M16](#m16). This is the local spectral step that turns general stationarity into a locality-sensitive obstruction.
- **Conceptual connection:** The relevant marginal belongs to the actual leading stationary vector. Arbitrary channel counts and strengths cannot invalidate a contradiction obtained by summing nonnegative local terms.
- **Sources:** Anchor context: [RH §2.1][rh-2-1] and the operator inner product in [§5.2][rh-5-2]. Project proof: [small eigenvalue in an active marginal, Eqs. (2)–(3)](../science/converse.md#a-small-eigenvalue-in-an-active-local-marginal).

<a id="m18"></a>
### M18 — A binary local measurement controls global overlap

- **Phase:** Narrative/innovation.
- **Central question:** How can one locally distinguishable direction bound overlap between two global pure states?
- **Understanding target:** Choose the projector associated with the small marginal eigenvalue from M17. Relate its target probability $`p\ge\mu`$ and stationary-vector probability $`q\le\delta`$ to a bound on global overlap by splitting the two measurement sectors and applying Cauchy–Schwarz.
- **Dependencies and story role:** [M02](#m02), [M09](#m09), [M17](#m17). This bridges the stationary vector's local defect to the prescribed target, rather than silently identifying the two vectors.
- **Conceptual connection:** A probability separation visible on one allowed region limits coherence of the full-state overlap. No informationally complete measurement is needed.
- **Sources:** Anchor context: [RH §4, Eqs. (29)–(30)][rh-4]. The binary-overlap inequality is derived in the project [stationary-vector to target-overlap argument, Eq. (4)](../science/converse.md#from-the-stationary-eigenvector-to-the-target-overlap).

<a id="m19"></a>
### M19 — The factor-two mixed-state converse

- **Phase:** Narrative/innovation.
- **Central question:** How much can mixing and eigenvector rotation jointly improve the stationary approximation?
- **Understanding target:** Combine the dominant-component fidelity estimate with M18's overlap bound. Identify the easy branches and the remaining tradeoff in $`\delta`$ that gives $`1-F\ge\mu/2`$. Distinguish this universal inequality from a claim that the constant is attained for every target.
- **Dependencies and story role:** [M15](#m15), [M18](#m18). This completes the mixed-state lower bound by connecting local spectral loss to global ordinary fidelity.
- **Conceptual connection:** The same argument covers arbitrary output rank and does not require the target to be a stationary eigenvector, uniqueness, or a Hamiltonian norm bound.
- **Sources:** Anchor context: [RH §5.4][rh-5-4] supplies the stationary-state framework. The quantitative argument and all case conditions are in the project [mixed-state error bound](../science/converse.md#the-mixed-state-error-bound).

<a id="m20"></a>
### M20 — One reset with a dark output and nonzero influx

- **Phase:** Narrative/innovation.
- **Central question:** How can the closest pure candidate be made compatible with an allowed dissipative channel?
- **Understanding target:** Construct a rank-one local reset from the removed eigenvector to a retained positive-weight eigenvector. Explain the different roles of $`L\phi=0`$ and $`L^\dagger\phi\ne0`$: the candidate is dark, while population can still enter it from its complement.
- **Dependencies and story role:** [M07](#m07), [M14](#m14). This begins the dynamical upper bound with a single local operation.
- **Conceptual connection:** The geometrically removed component supplies a physical reset direction without adding a register or local level. The construction includes $`\mu=0`$ directly.
- **Sources:** Anchor context: [RH §4.1][rh-4-1] and [§5.2][rh-5-2]. Project recipe: [remove one local eigencomponent](../science/construction.md#remove-one-local-eigencomponent); inherited attraction principle: [Ticozzi and Viola](../references/RELATED_WORK.md#ticozzi2009).

<a id="m21"></a>
### M21 — A global Hamiltonian connects the remaining directions

- **Phase:** Narrative/innovation.
- **Central question:** How can coherent motion connect every unwanted direction to the reset's incoming channel?
- **Understanding target:** Build a path Hamiltonian in the output's orthogonal complement, beginning at the normalized vector $`L^\dagger\phi`$. Explain why the path basis must diagonalize the projector $`A=L^\dagger L`$, and distinguish adjacency in that basis from adjacency of physical sites.
- **Dependencies and story role:** [M04](#m04), [M20](#m20). This extends one local reset into a globally connected dynamical design while preserving the dark output.
- **Conceptual connection:** The permitted global Hamiltonian makes a rank-deficient marginal sufficient for stabilization. Its bounded operator norm does not imply a local or efficient physical implementation.
- **Sources:** Anchor context: [RH §2.1][rh-2-1] and [§3][rh-3]. Project construction: [choose the Hamiltonian](../science/construction.md#choose-the-hamiltonian); resource interpretation: [bounded norm and implementation](../science/resources.md#a-bounded-operator-norm-does-not-price-implementation).

<a id="m22"></a>
### M22 — Positivity excludes other stationary states

- **Phase:** Narrative/innovation.
- **Central question:** Why can no stationary population remain trapped along the constructed path?
- **Understanding target:** Follow the implication from zero stationary influx into the dark output to a kernel vector of the density matrix. Explain how positivity and the diagonal form of $`A`$ then propagate zero rows and columns along the irreducible path, leaving only the desired pure state.
- **Dependencies and story role:** [M08](#m08), [M21](#m21), using [M04](#m04). This proves uniqueness for the explicit generator.
- **Conceptual connection:** The basis choice in M21 prevents dissipative anticommutator terms from canceling the Hamiltonian recurrence. Uniqueness follows for every finite dimension, not from inspection of a few spectra.
- **Sources:** Anchor context: [RH §5.4][rh-5-4]. Project proof: [uniqueness by positivity](../science/construction.md#uniqueness-by-positivity).

<a id="m23"></a>
### M23 — From uniqueness to global convergence in this construction

- **Phase:** Narrative/innovation.
- **Central question:** What ensures that every trajectory actually approaches the unique constructed stationary state?
- **Understanding target:** Connect the nondecreasing target population to stationary subsequential limits of time-averaged states. Use uniqueness to identify their target population and the pure-state trace-distance bound to conclude convergence of the trajectory itself.
- **Dependencies and story role:** [M06](#m06), [M09](#m09), [M22](#m22). This completes the attraction argument required by the optimization.
- **Conceptual connection:** The proof uses finite-dimensional compactness and the generator equation, with no assumed diagonalizability or dimension-uniform mixing rate.
- **Sources:** Anchor context: [RH §2.3][rh-2-3] and [§5.4, especially the existence and relaxation discussion][rh-5-4]. The construction-specific monotonicity and Cesàro argument are in [global attraction](../science/construction.md#global-attraction).

<a id="m24"></a>
### M24 — Assemble the accuracy theorem and exact boundary

- **Phase:** Narrative/innovation.
- **Central question:** What operational theorem follows when the converse and attractive construction are combined?
- **Understanding target:** State $`\mu/2\le\epsilon_{\mathrm{opt}}\le\mu`$ and $`\epsilon_{\mathrm{pure,opt}}=\mu`$ with their different quantifiers. Explain why the pure optimum is attained, why $`\mu=0`$ is equivalent to exact stabilization, and why mixed outputs can improve the optimal error by at most a factor of two.
- **Dependencies and story role:** [M12](#m12), [M14](#m14), [M19](#m19), [M23](#m23). This combines the two proof branches into the project's complete accuracy statement.
- **Conceptual connection:** The geometric rank-deficient set is now identified with the set of pure attractive outputs under unrestricted coherent control.
- **Sources:** Anchor context: [RH §5.4][rh-5-4]. Canonical project statements: [accuracy theorem](../science/model.md#accuracy-theorem), [geometry to an attained optimum](../science/converse.md#from-geometry-to-an-attained-stabilization-optimum) and [exact boundary](../science/construction.md#attained-accuracy-and-the-exact-boundary).

<a id="m25"></a>
### M25 — Structured targets expose the controlling distinction

- **Phase:** Narrative/innovation.
- **Central question:** Why do the same allowed support sizes impose different constraints on Bell, GHZ and ring-graph targets?
- **Understanding target:** Connect product-state kernels, Bell single-site spectra, GHZ pair kernels and the five-qubit ring's maximally mixed pair marginals to their respective values of $`\mu`$. Use the sharper one-qubit-bath Bell benchmark to interpret the universal interval's non-sharpness.
- **Dependencies and story role:** [M03](#m03), [M24](#m24). This gives concrete physical meaning to the theorem before moving to general support-size laws.
- **Conceptual connection:** Entanglement alone does not decide feasibility. The decisive distinction is the full spectrum on the specific allowed supports.
- **Sources:** Anchor context: [RH §4.1][rh-4-1]. Project [structured examples](../science/examples.md), especially [GHZ](../science/examples.md#ghz-targets-a-local-kernel-changes-feasibility) and [the ring graph state](../science/examples.md#five-qubit-ring-graph-state-a-two-body-error-floor); benchmark attribution: [Žnidarič](../references/RELATED_WORK.md#znidaric2015).

<a id="m26"></a>
### M26 — Accuracy as a requirement on dissipative support

- **Phase:** Narrative/innovation.
- **Central question:** When does a marginal spectral bound become a lower bound on the number of sites a jump must act on?
- **Understanding target:** For qubit targets, translate $`\psi_S\succeq cI_S/2^{\lvert S\rvert}`$ on supports of size at most $`k`$ into a stationary error floor. Explain the special case $`\mu=2^{-k}`$ for uniform marginals when the family includes a size-$`k`$ support, and interpret the logarithmic support requirement for a specified accuracy.
- **Dependencies and story role:** [M12](#m12), [M24](#m24), [M25](#m25). This turns the invariant into an architectural statement conditioned on a target property.
- **Conceptual connection:** More independent small-support channels or stronger coherent control do not remove the spectral floor; the conclusion does not assume that uniform targets exist for arbitrary system sizes.
- **Sources:** Anchor context: [RH §4, partial trace][rh-4] and [§4.1][rh-4-1]. Project [deterministic support requirement](../science/consequences.md#a-deterministic-support-requirement) and [uniform local marginals](../science/consequences.md#uniform-local-marginals).

<a id="m27"></a>
### M27 — What a typical target needs from concentration

- **Phase:** Narrative/innovation.
- **Central question:** Which random-state estimate can justify a nonzero error floor for a fixed local region?
- **Understanding target:** Identify the full-rank regime for a Haar-random qubit target across a fixed cut, and distinguish concentration of the smallest marginal eigenvalue from high entropy or small average purity. Read the inherited finite probability bound with its dimension and parameter conditions.
- **Dependencies and story role:** [M03](#m03), [M12](#m12), [M26](#m26). This extends the deterministic spectral hypothesis to a probabilistic target class, initially for one region.
- **Conceptual connection:** The theorem needs a lower bound on every local eigenvalue. A generic entanglement statement without that spectral control is insufficient.
- **Sources:** Anchor context only: [RH §4.1, Eq. (33)][rh-4-1]. Random-state concentration is outside RH's route: use the project [fixed-cut probability bound](../science/consequences.md#haar-random-targets-a-finite-probability-bound) and its primary source, [Hayden et al., Lemma III.4](../references/RELATED_WORK.md#hayden2006).

<a id="m28"></a>
### M28 — From one region to simultaneous support families

- **Phase:** Narrative/innovation.
- **Central question:** How does a fixed-cut estimate control every allowed family of bounded-size supports?
- **Understanding target:** Explain the union bound over all size-$`k`$ regions, extension to smaller regions by partial trace, and the absence of an independence assumption. For families whose largest allowed support has size $`k`$, connect the finite failure bound to $`\Theta(2^{-k})`$ accuracy away from the half-system window, retaining both conditions.
- **Dependencies and story role:** [M02](#m02), [M26](#m26), [M27](#m27). This is the probabilistic local-to-global step and completes the many-body consequence.
- **Conceptual connection:** A single event about all marginals controls every permitted support family of the stated sizes, including a family selected after the target is known.
- **Sources:** Anchor context: [RH §4, Eq. (29)][rh-4]. The union-bound and asymptotic arguments are supplied in the project [simultaneous marginal bound](../science/consequences.md#haar-random-targets-a-finite-probability-bound) and [regime away from half the system](../science/consequences.md#an-asymptotic-regime-away-from-half-the-system).

<a id="m29"></a>
### M29 — Stationary feasibility, implementation and verification

- **Phase:** Narrative/innovation.
- **Central question:** What does an attained stationary error establish about a realizable preparation process?
- **Understanding target:** Separate bounded operator norms from the cost of describing and implementing a global Hamiltonian. Explain how time rescaling preserves stationary accuracy, and interpret finite algebra and spectrum checks as evidence about specified generators and their implementation, without inferring a general preparation-time law.
- **Dependencies and story role:** [M08](#m08), [M10](#m10), [M21](#m21), [M23](#m23), [M28](#m28). This connects the theorem's global consequences back to its physical resources and evidence.
- **Conceptual connection:** The same construction can establish an accuracy optimum while leaving its scalable implementation and dimension-dependent relaxation behavior unresolved.
- **Sources:** [RH §2.1][rh-2-1], [§2.2][rh-2-2] and [§5.4, Theorem 5.4][rh-5-4]. Project [rates](../science/resources.md#rates-and-coherent-strength), [implementation cost](../science/resources.md#a-bounded-operator-norm-does-not-price-implementation) and [verification](../verification/README.md).

<a id="m30"></a>
### M30 — Narrative synthesis: one law, its mechanism and its domain

- **Phase:** Narrative/innovation.
- **Central question:** What complete scientific statement do the geometry, converse, construction and consequences jointly establish?
- **Understanding target:** Connect the least allowed marginal eigenvalue to pure-output geometry, the factor-two mixed-output bound and an attained autonomous generator. Explain the uniform and typical-target consequences with their assumptions, identify the inherited ingredients, and retain the boundaries imposed by strict effective support, fixed state space and unrestricted coherent control.
- **Dependencies and story role:** [M24](#m24), [M25](#m25), [M28](#m28), [M29](#m29), together with their dependencies. This is the final phase synthesis and completes the connected account.
- **Conceptual connection:** The contribution is a target-dependent stationary-accuracy characterization. Its meaning includes both what local reservoir design cannot overcome and what one allowed reset can attain with a suitable global Hamiltonian.
- **Sources:** Anchor synthesis: [RH §5.2][rh-5-2], [§5.4][rh-5-4] and [§6.2.1][rh-6-2-1]. Project [accuracy theorem](../science/model.md#accuracy-theorem), [consequences](../science/consequences.md), [resource boundaries](../science/resources.md) and [contribution boundary and attribution](../references/RELATED_WORK.md#contribution-boundary).

[rh-2-1]: https://arxiv.org/pdf/1104.5242v2#page=4
[rh-2-2]: https://arxiv.org/pdf/1104.5242v2#page=6
[rh-2-3]: https://arxiv.org/pdf/1104.5242v2#page=8
[rh-3]: https://arxiv.org/pdf/1104.5242v2#page=18
[rh-4]: https://arxiv.org/pdf/1104.5242v2#page=21
[rh-4-1]: https://arxiv.org/pdf/1104.5242v2#page=23
[rh-4-2]: https://arxiv.org/pdf/1104.5242v2#page=26
[rh-4-3]: https://arxiv.org/pdf/1104.5242v2#page=29
[rh-4-5]: https://arxiv.org/pdf/1104.5242v2#page=33
[rh-5-2]: https://arxiv.org/pdf/1104.5242v2#page=37
[rh-5-4]: https://arxiv.org/pdf/1104.5242v2#page=45
[rh-6-2-1]: https://arxiv.org/pdf/1104.5242v2#page=57
[rh-6-4-1]: https://arxiv.org/pdf/1104.5242v2#page=77
