# Quantum Adaptivity Frontier

**How much classical communication can a receiver save by choosing a quantum measurement after receiving the message?** This project determines the joint limits imposed by receiver dimension and simulation accuracy when the adaptive protocol sends one ternary message and the receiver has no independent input.

Let $`M_*(R,\varepsilon)`$ be the largest, over all such finite quantum correlations with receiver dimension at most $`R`$, of the smallest nonadaptive simulation alphabet at worst-input total-variation error $`\varepsilon`$. Nonadaptive simulators may use unrestricted shared entanglement and shared randomness. In this setting they are equivalent to classical protocols with shared randomness.

For every integer $`R\ge1`$ and $`0<\varepsilon\le1/2`$,

```math
M_*(R,\varepsilon)
=\Theta\!\left(\min\!\left\{R,\ln\frac1\varepsilon\right\}\right),
\qquad
M_*(R,0)=\Theta(R).
```

The constants are universal, including when dimension and error vary together. Communication is measured in possible message values; its fixed-length binary cost is their base-two logarithm rounded up. The adaptive target uses three values, or two fixed-length binary bits.

| Resource boundary | Result |
|---|---|
| Finite receiver dimension, exact simulation | Worst-case alphabet grows linearly with $`R`$ |
| Nonzero simulation error | Worst-case alphabet is capped at logarithmic order in $`1/\varepsilon`$ |
| Both limits together | One exclusion family attains the smaller order |
| Uniform input-independent output replacement noise | The same family has exact simulation cost of order $`\min\{R,\ln(1/t)\}`$ for $`0<t\le1/2`$ |

[Tavakoli's earlier work](https://arxiv.org/abs/2611.11333) established the unbounded adaptive advantage, the exact exclusion measurement, and universal simulation upper bounds. The contribution here is a constant-density quantum exclusion construction that makes the dimension and precision bounds simultaneously tight in order. It uses standard Haar-matrix estimates and the established classical subset-guessing inequality. The [related-work account](references/RELATED_WORK.md) separates these ingredients and compares the previous construction's weaker quantitative consequence.

## Read the science

The [scientific overview](science/README.md) connects the operational question, construction, converse, and meaning.

| Question | Authoritative account |
|---|---|
| Which inputs, dimensions, simulators and error conventions are allowed? | [Model](science/model.md) |
| What are the exact finite bounds and joint asymptotic law? | [Frontier theorem](science/frontier.md) |
| How can one triple of bases work for every input subset? | [Uniform random-basis lemma](science/random_bases.md) |
| How does Alice's measurement exclude a constant fraction of output labels? | [Quantum construction](science/quantum_construction.md) |
| Why can unlimited shared randomness not evade the converse? | [Classical exclusion](science/classical_exclusion.md) |
| What do the bounds mean in bits, dimension and output noise? | [Interpretation](science/interpretation.md) |
| What is inherited, and what was checked? | [Related work](references/RELATED_WORK.md), [bibliography](references/references.bib), and [verification](verification/README.md) |

The [reading guide](llms.txt) maps specific questions to the complete proof files.

## Learn the argument

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, using the author's January 2018 standard-layout manuscript. The [source-to-project bridge](learning/WATROUS_BRIDGE.md) identifies the relevant sections, translates notation, and begins with a complete two-qubit experiment. It separates textbook foundations from imported research theorems and the new frontier proof.

The [30-milestone map](learning/MILESTONES.md) follows the project's story through 12 background milestones and 18 narrative milestones. Its two phases connect individual objects to the full model, then the construction and converse to the joint resource law. Start with the [learning guide](learning/README.md); specialists can continue directly to the scientific accounts above.

## Reproduce the checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python3 verification/check_science.py --output /tmp/adaptivity-checks.json
```

The checks cover finite quantum measurements, an independent bipartite Born-probability calculation, small classical minimax linear programs, exact-rational integer bounds, and the scalar probability estimate. The general theorem follows from the written proofs; finite checks do not establish asymptotic validity or literature priority. See the [verification guide](verification/README.md) for the exact tested scope and saved results.

## Scope

The receiver has no independent input. The dimension bound applies to the adaptive target's quantum share; simulator quantum resources are unrestricted. The attaining target uses a maximally entangled state with $`\log_2R`$ ebits, without establishing a necessary entanglement-entropy law for arbitrary states.

Local computation, measurement descriptions, finding the bases and implementing the POVMs are uncharged. The result is an information-theoretic communication frontier, with no efficient-circuit, laboratory-runtime or channel-capacity claim. Output replacement noise is a specified mixture of classical output distributions, not a general model of local apparatus noise.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
