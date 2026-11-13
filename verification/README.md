# Reproduce the scientific checks

From the repository root, use Python 3.10 or later with the dependencies in
[`requirements.txt`](requirements.txt):

```bash
python3 -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python3 verification/check_science.py
```

The checker exits unsuccessfully if a required numerical or exact-arithmetic
comparison fails. Its default output is
[`results/science_checks.json`](results/science_checks.json). To save a separate
report, pass `--output /path/to/report.json`. The report records the checker
SHA-256, package versions, fixed seeds, inputs, residuals, and checked scope.
It does not contain a claimed source commit or proof certificate.

## What is checked

| Calculation | Inputs and extent | What it tests |
| --- | --- | --- |
| Uniform small-support geometry | One fixed-seed triple of bases in dimension 512; every cross-basis submatrix with total support at most three | The exact finite maximum follows from all top-two row and column squared masses. This tests a concrete basis triple, rather than a sample of support sets. |
| Split-Gram POVMs | Fifty excluded sets, covering all ten ways to divide three selected labels among three bases | Gram invertibility, positivity, completeness, forbidden-output probabilities, and normalization of the complete output distribution. Empty blocks and the three-nonempty-block case are included. |
| Independent bipartite probabilities | One dimension-16 example; all 48 output labels | The explicit tensor-product trace on a maximally entangled state agrees with the independently evaluated Born formula, including the transpose on Alice's POVM. |
| Classical exclusion minimax error | 110 finite instances with universe sizes three through eight | An LP over every possible fixed-size output set agrees with `binom(m,K)/binom(n,K)`. The uniform shared-random strategy has the same error for every excluded set. |
| Random-basis union bound | The analytical scalar envelope and several finite dimensions | The envelope is negative at dimension 1024 and has negative slope, as required by the written random-basis proof. |
| Finite integer frontier bounds | Twelve dimension/error pairs; exact integers and rational arithmetic | The elementary lower bound, exact exclusion-game alphabet, and inherited correlation-simulation upper bound have the required order. The exponential error inequality is also checked at each applicable integer. |

The finite basis example uses three excluded labels in dimension 512. It is a
specific valid example; it does not replace the conservative general existence
bound with excluded-set size `floor(R/1024)`.

## Mathematical and numerical boundaries

The written proofs establish the universal statements. The finite matrix
calculations detect transpose, normalization, support, and implementation
errors. They do not enumerate all excluded sets in the POVM calculation, prove
the general random-basis theorem, establish experimental feasibility, or
certify literature priority. Tiny negative eigenvalues and probabilities in
the report are floating-point residuals, tested against explicit tolerances.

The classical LP concerns exclusion-game failure. Its optimum supplies a lower
bound on the cost of simulating the full quantum output distribution. The
game-optimal classical strategy is not claimed to simulate that distribution
in total variation. The extension from deterministic output lists to arbitrary
shared-random protocols is supplied by the analytical converse.

The scalar union-bound diagnostic evaluates

```math
3\binom{2R}{m}17^{2m}
\left(\frac{247}{256}\right)^{R-1},
\qquad m=\lfloor R/1024\rfloor.
```

The script checks the negative-slope linear envelope used in the proof and
compares selected finite values with it. These logarithms use floating-point
arithmetic. The finite integer frontier diagnostics use exact rational
arithmetic and keep the exclusion-game lower bound distinct from the
correlation-simulation upper bound.

## Recorded run

The accompanying JSON is produced directly by this checker. It records the
actual Python, NumPy, and SciPy versions used for that run; rerunning overwrites
the report with the new observations. The requirements describe compatible
dependencies rather than a hardware-specific environment lock.
