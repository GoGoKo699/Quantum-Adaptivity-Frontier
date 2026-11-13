# Scientific account

An adaptive receiver can wait for a short classical message before choosing how to measure shared entanglement. A nonadaptive receiver must measure first and use the later message only to decode its classical record. With no independent receiver input, every nonadaptive strategy reduces to shared-random classical communication.

The question is quantitative: for one adaptive trit and receiver dimension at most $`R`$, how large must a nonadaptive alphabet be to reproduce the full conditional distribution to worst-input total-variation error $`\varepsilon`$?

## One connected argument

1. The [model](model.md) defines the finite correlation task, target dimension, simulator resources and error convention.
2. The [frontier theorem](frontier.md) states uniform finite bounds and explains the inherited exact-dimension and approximate simulation upper bounds.
3. The [random-basis lemma](random_bases.md) produces three fixed bases whose small cross submatrices are uniformly controlled over every input subset.
4. The [quantum construction](quantum_construction.md) inserts those bases into the inherited positive Gram-matrix decomposition. A ternary message then excludes every allowed constant-density input subset with zero error.
5. The [classical exclusion account](classical_exclusion.md) re-proves the established subset-guessing inequality and its minimax form. Its forbidden-output event lower-bounds total-variation simulation error.
6. The [interpretation](interpretation.md) derives the joint resource consequence, separates alphabet size from bits and Hilbert dimension from entanglement entropy, and proves the output-replacement-noise corollary.

The lower construction and inherited upper bounds yield

```math
M_*(R,\varepsilon)
=\Theta\!\left(\min\!\left\{R,\ln\frac1\varepsilon\right\}\right)
\quad(0<\varepsilon\le1/2),
\qquad
M_*(R,0)=\Theta(R).
```

One target family supplies the lower bound for every error tolerance. No efficient local compilation or growing constant-error advantage is asserted.

## Attribution and verification

The original unbounded adaptive advantage, split-Gram measurement and universal upper bounds are prior work. The new contribution is the constant-density realization and the resulting sharp joint frontier. Standard probability and classical guessing ingredients are credited in [related work](../references/RELATED_WORK.md).

The [verification guide](../verification/README.md) documents finite diagnostics and their limits. The [repository overview](../README.md) provides direct routes for inspecting a specific claim; the full proof remains in these topic-based files.

For a source-guided route into the same argument, use the [Watrous bridge](../learning/WATROUS_BRIDGE.md) and the [30 milestones](../learning/MILESTONES.md). The bridge's small complete experiment illustrates the measurement sequence without claiming the asymptotic separation.
