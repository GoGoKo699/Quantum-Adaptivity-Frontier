# From Watrous to the adaptivity frontier

[Learning route](README.md) · [Thirty milestones](MILESTONES.md) · [Scientific overview](../science/README.md)

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
| A vector $`u`$ and its adjoint $`u^*`$ | $`|u\rangle`$ and $`\langle u|`$; $`uu^*`$ becomes $`|u\rangle\langle u|`$ |
| $`\operatorname{Pos}(\mathcal X)`$ | Positive semidefinite operators, written $`A\succeq0`$ |
| $`\operatorname D(\mathcal X)`$ | Density operators: positive operators with trace one |
| A measurement $`\mu:\Sigma\to\operatorname{Pos}(\mathcal X)`$ | Effects $`\{A_a\}_a`$ with $`\sum_a A_a=I`$ |
| $`\langle A,B\rangle=\operatorname{Tr}(A^*B)`$ | The Born probability $`\operatorname{Tr}(A\rho)`$ for effect $`A`$ and state $`\rho`$ |
| An ensemble $`\eta(a)`$ | A subnormalized state $`\tau_a`$: its trace is outcome probability, and $`\tau_a/\operatorname{Tr}\tau_a`$ is the conditional state |

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
\operatorname{Tr}_A
\left[(A_a^{\mathsf T}\otimes I)|\Phi_R\rangle\langle\Phi_R|\right]
=\frac{A_a}{R}.
```

Its trace is Alice's outcome probability. Conditional on receiving $`a`$, Bob measures a basis $`\{|u_{j|a}\rangle\}_j`$. The full joint probability is therefore

```math
p(a,j\mid S)
=\operatorname{Tr}\!\left(
\frac{A_{a|S}}R|u_{j|a}\rangle\langle u_{j|a}|
\right)
=\frac1R\langle u_{j|a}|A_{a|S}|u_{j|a}\rangle.
```

Thus putting a forbidden vector in the kernel of the corresponding effect makes its output probability zero. This statement uses unconditional probabilities: every Alice outcome is retained and sent. The [quantum proof](../science/quantum_construction.md) builds effects with all the required kernels simultaneously.

## A complete two-qubit example

Take $`R=2`$ and let the parties share one Bell pair,

```math
|\Phi_2\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}.
```

Bob has three possible measurement bases. Their output labels include the basis name, so the six labels remain distinct even when two outcomes have the same numerical probability.

| Sent symbol $`a`$ | Basis outcome $`j=0`$ | Basis outcome $`j=1`$ |
|---|---|---|
| 1 | $`|0\rangle`$ | $`|1\rangle`$ |
| 2 | $`|+\rangle=(|0\rangle+|1\rangle)/\sqrt2`$ | $`|-\rangle=(|0\rangle-|1\rangle)/\sqrt2`$ |
| 3 | $`|+i\rangle=(|0\rangle+i|1\rangle)/\sqrt2`$ | $`|-i\rangle=(|0\rangle-i|1\rangle)/\sqrt2`$ |

Alice's allowed inputs are the six singleton forbidden sets. First consider $`S=\{(1,0)\}`$: Bob must avoid the computational-basis label $`(1,0)`$. Set

```math
A_1=\begin{pmatrix}0&0\\0&1/3\end{pmatrix},
\qquad
A_2=A_3=
\begin{pmatrix}1/2&0\\0&1/3\end{pmatrix}.
```

All three matrices are positive and their sum is $`I_2`$. They are real, so their transposes equal themselves. Alice measures this three-outcome POVM and sends the outcome. The remote-preparation identity gives the following complete branch description:

| Alice's message | Probability | Bob's normalized conditional state | Bob's conditional basis probabilities |
|---|---:|---|---|
| 1 | $`1/6`$ | $`|1\rangle\langle1|`$ | In basis1: $`(0,1)`$ |
| 2 | $`5/12`$ | $`\operatorname{diag}(3/5,2/5)`$ | In basis2: $`(1/2,1/2)`$ |
| 3 | $`5/12`$ | $`\operatorname{diag}(3/5,2/5)`$ | In basis3: $`(1/2,1/2)`$ |

For example, $`\operatorname{Tr}(A_2)/2=5/12`$ and $`A_2/\operatorname{Tr}(A_2)=\operatorname{diag}(3/5,2/5)`$. Each vector in basis2 or3 has equal squared overlap with $`|0\rangle`$ and $`|1\rangle`$, which explains the equal conditional outcomes in those branches. Multiplying each branch probability by its conditional measurement probabilities yields the entire output distribution:

| Output label | $`(1,0)`$ | $`(1,1)`$ | $`(2,0)`$ | $`(2,1)`$ | $`(3,0)`$ | $`(3,1)`$ |
|---|---:|---:|---:|---:|---:|---:|
| Probability given $`S=\{(1,0)\}`$ | 0 | $`1/6`$ | $`5/24`$ | $`5/24`$ | $`5/24`$ | $`5/24`$ |

These six probabilities sum to one. The forbidden label has probability zero, while all three messages have positive probability.

The protocol also specifies every other allowed input. If $`S=\{(a_0,j_0)\}`$, put $`P=|u_{j_0|a_0}\rangle\langle u_{j_0|a_0}|`$ and choose

```math
A_{a_0|S}=\frac{I_2-P}{3},
\qquad
A_{a|S}=\frac P2+\frac{I_2-P}{3}
\quad(a\ne a_0).
```

Alice measures their transposes. Positivity, completeness and $`A_{a_0|S}|u_{j_0|a_0}\rangle=0`$ hold for all six inputs, so Bob always avoids Alice's forbidden label. For this triple of mutually unbiased qubit bases, the forbidden label has probability zero, its partner in the same basis has probability $`1/6`$, and the four labels in the other bases each have probability $`5/24`$.

This example uses one ebit and a three-valued classical message; it makes the conditioning and basis choice visible. It is a small exclusion protocol, **not a witness of an unbounded advantage**. For the singleton exclusion game, two fixed candidate labels already give a classical zero-failure strategy: Alice indicates one that is not forbidden. That game strategy is not asserted to reproduce the complete probability table above.

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
