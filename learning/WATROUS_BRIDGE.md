# From Watrous to the adaptivity frontier

[Learning route](README.md) · [Complete worked example](WORKED_EXAMPLE.md) · [Thirty milestones](MILESTONES.md) · [Scientific overview](../science/README.md)

Alice knows which output labels are forbidden. Bob must produce a label after receiving one short message. Their shared entanglement lets Alice's measurement condition Bob's quantum state; the message tells him which measurement to use. The project determines the strongest possible communication saving when Bob has no independent input, his share has finite dimension, and a nonadaptive simulator is allowed a prescribed error.

## Selected source and useful locations

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. Use the January-2018 pre-publication manuscript linked from the [author's official book page](https://cs.uwaterloo.ca/~watrous/TQI/), choosing its **standard layout**. Section, equation and exercise identifiers below refer to that manuscript; the page numbers are its printed page labels.

| Needed idea | Anchor location | Connection to this project |
|---|---|---|
| Positive operators | §1.1.2, Eq.1.95, p17 | Each POVM effect must be positive semidefinite. |
| Operator norms and matrix decompositions | §1.1.3, p24 | Cross-submatrix norms control the Gram construction. |
| Convex combinations and finite decompositions | §1.2.1, p35; Theorems1.9 and1.10, p45 | Shared randomness mixes deterministic classical strategies. |
| States, ensembles, reductions and purifications | §§2.1.2–2.1.3, pp61–67 | The parties share a state; conditioning on Alice's outcome gives an ensemble on Bob. |
| POVMs and conditioned states | §§2.3.1–2.3.2, pp100–106; Eq2.226 on p106 | Alice's three effects generate the message-conditioned states. |
| Convex measurement/ensemble structure | §2.3.3, p113 | Mixtures and extremal descriptions clarify finite classical and quantum strategy sets. |
| Remote realization of an ensemble | Exercise2.2, p120 | A measurement on a purification can realize a chosen decomposition of its reduced state. |
| Entanglement with classical communication | §6.1.2, p324; §6.3.1, p359 | Local operations can depend on the received classical message. |
| Random bases | §7.2.1, p408; §7.3.1, p430 | Haar measure and concentration motivate uniform control over many submatrices. |

The [frontmatter and contents](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf) verify the manuscript version and navigation. Direct chapter links are [1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), [2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), [6](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), and [7](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf). These are source pointers, not additional educational anchors or a requirement to study entire chapters.

## Translate the notation

| Watrous notation | Repository notation and meaning |
|---|---|
| A complex Euclidean space $`\mathcal X`$ | A finite-dimensional quantum register, often $`\mathbb C^R`$ |
| A vector $`u`$ and its adjoint $`u^*`$ | $`\vert u\rangle`$ and $`\langle u\vert `$; $`uu^*`$ becomes $`\vert u\rangle\langle u\vert `$ |
| $`\mathrm{Pos}(\mathcal X)`$ | Positive semidefinite operators, written $`A\succeq0`$ |
| $`\mathrm{D}(\mathcal X)`$ | Density operators: positive operators with trace one |
| A measurement $`\mu:\Sigma\to\mathrm{Pos}(\mathcal X)`$ | Effects $`\{A_a\}_a`$ with $`\sum_a A_a=I`$ |
| $`\langle A,B\rangle=\mathrm{Tr}(A^*B)`$ | The Born probability $`\mathrm{Tr}(A\rho)`$ for effect $`A`$ and state $`\rho`$ |
| An ensemble $`\eta(a)`$ | A subnormalized state $`\tau_a`$: its trace is outcome probability, and $`\tau_a/\mathrm{Tr}\tau_a`$ is the conditional state |

The project uses $`a\in\{1,2,3\}`$ for Alice's sent symbol. In the exclusion construction Bob outputs a pair $`b=(a,j)`$, where $`j`$ is his basis outcome; Alice's input $`S`$ is a set of forbidden pairs. The integer $`R`$ is Bob's target quantum dimension, while $`M`$ or $`K`$ counts a simulator's message values. The set size $`m=|S|`$ is a different quantity.

For classical distributions $`p,q`$, total variation is $`\tfrac12\sum_b|p(b)-q(b)|`$. The project takes its maximum over Alice's inputs. This concerns classical output probabilities, without replacing them by an error measure on the retained quantum state.

## Remote preparation is the operational link

A POVM specifies positive effects whose sum is the identity. The trace of an effect against a state gives the probability of its outcome. For a joint state, the same calculation also gives the state of the other register conditioned on that outcome. Watrous's Eq2.226 and Exercise2.2 develop these facts and their ensemble interpretation.

For this project, the maximally entangled state has the form

```math
|\Phi_R\rangle
=\frac1{\sqrt R}\sum_{r=1}^{R}|r\rangle_A|r\rangle_B.
```

The computational basis in this expression defines transpose, denoted $`\mathsf T`$. If Alice measures effects $`\{A_a^{\mathsf T}\}_a`$, then Bob's unnormalized conditional state is

```math
\tau_a=
\mathrm{Tr}_A
\left[(A_a^{\mathsf T}\otimes I)|\Phi_R\rangle\langle\Phi_R|\right]
=\frac{A_a}{R}.
```

Its trace is Alice's outcome probability. Conditional on receiving $`a`$, Bob measures a basis $`\{|u_{j|a}\rangle\}_j`$. The full joint probability is therefore

```math
p(a,j\mid S)
=\mathrm{Tr}\!\left(
\frac{A_{a|S}}R|u_{j|a}\rangle\langle u_{j|a}|
\right)
=\frac1R\langle u_{j|a}|A_{a|S}|u_{j|a}\rangle.
```

Thus putting a forbidden vector in the kernel of the corresponding effect makes its output probability zero. This statement uses unconditional probabilities: every Alice outcome is retained and sent. The [quantum proof](../science/quantum_construction.md) builds effects with all the required kernels simultaneously.

## See the complete experiment

The [complete two-qubit worked example](WORKED_EXAMPLE.md) shows all three sender outcomes, the receiver's selected bases, every output probability, and all six allowed forbidden inputs. Read it alongside the remote-preparation identity above, then return to the proof roadmap below.

## From the example to the project theorem

The general construction uses three bases in dimension $`R`$ and inputs containing $`m=\lfloor R/1024\rfloor`$ forbidden labels. Many kernel conditions must now hold at once. Collect their vectors as columns of a matrix $`T`$; its Gram matrix is $`G=T^\dagger T`$. Small cross-basis submatrix norms make $`G`$ invertible and permit a positive three-part split. [Tavakoli's inherited POVM construction](../references/RELATED_WORK.md#tavakoli-2026) turns that split into the effects with the required kernels.

The new input to that construction is a triple of bases working uniformly for every allowed forbidden set with $`m`$ proportional to $`R`$. The [basis proof](../science/random_bases.md) uses an explicit complex-Haar coordinate tail, finite sphere nets and a union bound. Watrous's Haar/concentration chapters support the background; the specific uniform estimate and its constants are established in the project's proof, using standard probability tools.

For the classical lower bound, fixing every random seed leaves at most $`K`$ candidate output labels. Some forbidden inputs contain all of them. Averaging over the forbidden sets forces a failure probability at least

```math
\frac{\binom mK}{\binom{3R}K}
\qquad(1\le K\le m).
```

Shared randomness cannot remove that average obstruction. The [classical proof](../science/classical_exclusion.md) derives the inherited subset-guessing inequality and its minimax form directly. Since the quantum target never enters the forbidden set, its simulator's probability of doing so is also a lower bound on total-variation error. This implication concerns the whole output distribution; the game score alone does not characterize that distribution.

For the matching upper bounds, two distinct research ingredients are used. The exact $`3R`$ bound imports the **Frenkel–Weiner fixed-POVM simulation theorem**, applied to a direct-sum encoding. The logarithmic bounded-error upper uses **Tavakoli's guessing-and-selection protocol**. Neither is replaced by a textbook convexity fact. The [frontier proof](../science/frontier.md) combines these imported results with the constant-density construction and keeps all parameters uniform.

## Keep the source and contribution boundaries visible

| Role | Material |
|---|---|
| Textbook foundations | Finite states and measurements, ensembles and purification, convexity, LOCC, Haar measure and concentration |
| Imported research mechanisms | Tavakoli's adaptive separation, split-Gram POVM and universal upper bounds; Frenkel–Weiner's simulation theorem and subset-guessing inequality; established Haar-submatrix tools |
| This project's added conclusion | A constant-density adaptive exclusion realization and the joint, uniform dimension–precision frontier |
| Explained consequence | The corresponding exact simulation law after the specified uniform output replacement |

The [related-work account](../references/RELATED_WORK.md) gives the precise primary comparisons. It remains part of the proof route even though Watrous is the one educational anchor.

The final parameter $`R`$ measures the target receiver's Hilbert-space dimension. The construction supplies $`\log_2R`$ ebits but establishes no necessary entanglement-entropy law. The simulator's quantum resources are unrestricted. Communication is counted by alphabet size, local computation and measurement implementation are uncharged, and fixed positive error prevents an unbounded advantage from growing with $`R`$ alone. These conditions travel with the [main theorem](../science/frontier.md) and its [interpretation](../science/interpretation.md).
