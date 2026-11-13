# Learn Quantum Adaptivity Frontier

Alice sends Bob a short classical message. They also share an entangled state prepared in advance. Bob can preserve his quantum share until the message arrives, then choose how to measure it. This project asks how much extra communication is needed if he must measure first and use the message only to interpret a classical record.

Bob has no independent input. The adaptive target sends one of three symbols, and Bob's quantum share has dimension at most $`R`$. A competing nonadaptive simulator can use a different entangled state of arbitrary dimension and unlimited input-independent shared randomness. Its task is to reproduce the complete conditional output distribution, with a worst-input total-variation error at most $`\varepsilon`$.

The worst target's required nonadaptive alphabet has order

```math
\min\!\left\{R,1+\ln\frac1\varepsilon\right\}
\qquad(0<\varepsilon\le1/2),
```

and order $`R`$ at exact accuracy. Here the alphabet counts possible message values. The fixed-length binary cost is its base-two logarithm rounded up. The [scientific theorem](../science/frontier.md) gives precise uniform constants and assumptions.

## One anchor and a route into the proof

The selected educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. The [author's official page](https://cs.uwaterloo.ca/~watrous/TQI/) provides the January-2018 pre-publication manuscript used here, in standard layout. The source is available for personal use; this repository links to it and does not redistribute the book.

| Start here | What it provides |
|---|---|
| [Watrous bridge](WATROUS_BRIDGE.md) | Relevant source sections, a notation dictionary, remote preparation, and a complete two-qubit example |
| [Thirty-milestone map](MILESTONES.md) | The connected understanding route, from background objects to the full dimension–precision frontier |
| [Scientific overview](../science/README.md) | The complete chain of models, constructions, lower bounds and upper bounds |
| [Related work](../references/RELATED_WORK.md) | Attribution for imported theorems and the specific contribution beyond earlier adaptivity results |
| [Verification](../verification/README.md) | Finite calculations and the limits of their evidence |

The map contains exactly **M01–M30** in two phases: background/preliminaries and narrative/innovation. Each phase moves from individual objects to their combined operational meaning. The bridge supplies an entry point; the map identifies the project-specific understanding targets and their dependencies. Reading the whole textbook is unnecessary before following the example.

## Follow the scientific story

Begin with a measurement outcome as both a classical message and a way to condition Bob's state. Then understand why a receiver who measures before receiving the message has only a shared-random classical record in this no-receiver-input setting. The bridge's six-output example makes those operations explicit, while the [model](../science/model.md) fixes their general meaning.

The contribution combines three ingredients. [Uniformly controlled random bases](../science/random_bases.md) allow an input-dependent three-outcome sender measurement to exclude a constant fraction of output labels for every input subset, using the same three receiver bases. The [quantum construction](../science/quantum_construction.md) realizes the exact conditional probabilities. The [classical exclusion bound](../science/classical_exclusion.md) turns a forbidden output into a necessary simulation error; the [frontier theorem](../science/frontier.md) matches that lower bound with inherited universal upper bounds.

Keep the game score and the complete distribution separate. A classical strategy that avoids forbidden labels with optimal probability need not reproduce the quantum probabilities on the remaining labels. Also keep receiver dimension, entanglement entropy, message alphabet and transmitted bits separate. The [interpretation](../science/interpretation.md) explains these distinctions and the exact uniform-output-replacement corollary.

The result charges communication and bounds the target's receiver dimension. It establishes the existence of the required bases and POVMs with finite mathematical descriptions; it does not bound the time to find, compute or implement them. At any fixed positive error, increasing dimension alone does not give an unbounded communication advantage.
