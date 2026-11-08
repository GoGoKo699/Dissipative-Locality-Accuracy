# Reproducible finite checks

Run from the repository root with Python 3.12 and the pinned dependencies:

```bash
python -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
  python verification/verify.py
```

The script exits unsuccessfully if any check fails and writes [results.json](results.json) only after all checks pass. To run the same checks without changing the saved output:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
  python verification/verify.py --no-write
```

An alternative output location can be supplied with `--output PATH`. The saved results record the Python, NumPy, and SciPy versions, target and probe seeds, tolerances, every checked marginal spectrum, and each generator's residuals and spectral gap. Floating-point values may differ slightly across numerical-library builds; the checks use explicit tolerances rather than requiring identical decimal output.

## What is checked

The suite uses five structured examples and seven concrete generators. The largest physical Hilbert space used for a generator has dimension 16, so its Lindblad matrix is only 256 by 256.

| Check | Purpose |
| --- | --- |
| Complex product target | Exercises the zero-eigenvalue endpoint with complex amplitudes. |
| Bell target | Checks a maximally mixed local marginal and truncation error $`1/2`$. |
| Four-qubit GHZ, single-site supports | Checks $`\mu=1/2`$ for single-site dissipation. |
| Four-qubit GHZ, pair supports | Checks exact stabilization when a pair marginal is rank deficient, even though the support and complement have equal dimension. |
| Seeded complex target on dimensions $`2\times4\times2`$ | Checks a full-rank marginal on the separated support consisting of the first and third factors. |
| Seeded complex target on dimensions $`2\times3\times2`$ | Checks $`\mu=0`$ when that separated support has dimension four and its complement has dimension three. |
| Single qubit with full-system support | Checks the formal $`D=2`$ endpoint, where the Hamiltonian chain is empty and one reset suffices. |
| Five-qubit ring graph state | Checks all ten two-site marginals with exact integer Gram matrices and all 32 stabilizer supports. |

For the separated-support cases, the allowed family contains the first factor, the third factor, and their union. The union must be selected as the minimizing support. This checks support selection as well as a tensor permutation that is absent from a simple bipartite example. Code and JSON use **zero-based site indices**; the prose examples use conventional site labels starting at one.

The partial trace and the supported reset are compared with independent matrix-element calculations using explicit physical basis indices. These reference calculations do not use the transpose-and-reshape implementation being checked. A complex Hermitian probe compares the vectorized generator with direct operator multiplication, testing the distinction between transpose and adjoint.

For each generator, the script checks the following construction identities:

```math
L\phi=H\phi=0,\qquad
L^\dagger L=A,\qquad
B^\dagger B=I,\qquad
BB^\dagger+|\phi\rangle\langle\phi|=I.
```

Here $`B`$ contains the Jacobi-chain basis. The script also checks that $`B^\dagger A B`$ is diagonal, a necessary feature of the construction's row-propagation proof. It verifies stationarity, trace preservation, Hermiticity preservation, $`\|L\|=1`$, $`\|H\|=2\cos(\pi/D)<2`$ at numerical tolerance, and

```math
1-|\langle\psi|\phi\rangle|^2=\mu.
```

Every finite Lindblad matrix must have exactly one eigenvalue within $`10^{-8}`$ of zero, with every other eigenvalue's real part below $`-10^{-9}`$. Algebraic residuals must be below $`10^{-10}`$. The observed spectral gaps are instance-specific diagnostics at the construction's unit jump strength and unit Hamiltonian coupling.

## Exact checks for the ring state

The five-qubit graph state has amplitudes $`s_x/\sqrt{32}`$, where $`s_x\in\{-1,1\}`$. For each pair of sites, the corresponding amplitude matrix has four rows and eight columns. The script verifies with integer arithmetic that

```math
M_SM_S^{\mathsf T}=8I_4.
```

Thus its reduced state is exactly $`I_4/4`$. It also verifies the five stabilizer generators and obtains the weight distribution

```math
1+10z^3+15z^4+6z^5.
```

These are exact finite statements about this explicitly specified graph state. No Lindblad matrix for the 32-dimensional graph-state system is diagonalized.

## Interpretation

The checks validate the implementation and the stated finite examples. The [analytic proof](../science/model.md) establishes the universal lower bound and global attraction, and the [construction](../science/construction.md) explains the generator being implemented. A finite set of successful spectra does not prove the theorem, optimize the mixed stationary output, establish the best constants, or provide a dimension-uniform mixing-time bound. In particular, the construction reaches the pure-output optimum $`\mu`$; it is not a numerical search for $`\epsilon_{\mathrm{opt}}`$ over mixed outputs.

## The external rigorous Gibbs certificate

The [Gibbs application](../science/gibbs-corollary.md) uses the authoritative five-qubit input and rigorous certificate in [Gibbs Cancellation Obstruction at the linked revision](https://github.com/GoGoKo699/Gibbs-Cancellation-Obstruction/tree/7261788af6b88ba30222dc5e5fafb93337d09876/verification/ground-thermal). Its [coefficient file](https://github.com/GoGoKo699/Gibbs-Cancellation-Obstruction/blob/7261788af6b88ba30222dc5e5fafb93337d09876/verification/data/hamiltonian.json) has SHA256 `4356bc7a4090a83426c93d2a4142bbc83a39fa8f9707208a268e2cb057bf8b2d`. The certificate reconstructs that exact Gaussian-integer Hamiltonian and uses 256-bit Arb/Acb Rump enclosures for its complete energy spectrum, normalized ground vector and all nine allowed marginal spectra. Interval LDL* certifies the four negative ground-population forms, while enclosed Boltzmann sums certify the thermal deficit and inherited error floor.

From a checkout of that exact companion revision, run:

```bash
python -m pip install -r verification/requirements.txt
python verification/ground-thermal/certify_ground_thermal.py --output /tmp/ground_thermal_certificate.json
```

The companion's [verification guide](https://github.com/GoGoKo699/Gibbs-Cancellation-Obstruction/blob/7261788af6b88ba30222dc5e5fafb93337d09876/verification/ground-thermal/README.md) explains rational enclosures, input identity, all positive LDL* pivots and the analytic monotone extension to every real $`\beta\ge12/5`$. The high-temperature positive reservoir interval and local-superoperator evaluation rank have different certificates and retain separate logical roles.

`verification/verify.py` in this repository checks its finite constructions and structured states; it does **not** run the companion's thermal certificate. No duplicate Hamiltonian, program or certificate JSON is maintained here. The [thermal trace-distance floor](../science/gibbs-corollary.md#a-direct-corollary-of-the-inherited-stationary-bound) follows analytically from this repository's existing pure-target theorem, and the companion supplies the explicit rigorous inputs and stronger exact-feasibility witness.

## Actual hosted mathematics

The [hosted rendering check](hosted/README.md) compares the actual public GitHub mathematics with an exact source commit at wide and narrow viewport widths. Its read-only pull-request job retains MathML comparisons and screenshots. This check is separate from the generator suite and the external rigorous Gibbs certificate; neither scientific computation establishes displayed readability.
