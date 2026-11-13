# A complete two-qubit example

[Watrous bridge and source locators](WATROUS_BRIDGE.md) · [Learning route](README.md) · [Thirty milestones](MILESTONES.md)

Alice receives a forbidden output label and sends one of three classical symbols. Bob has no independent input; he uses the received symbol to choose his measurement basis. They share the Bell pair specified below, and every outcome is retained.

For this Bell pair, measuring the transpose of an effect on Alice's share prepares that effect divided by two as Bob's unnormalized conditional state. Its trace gives the message probability. Transpose means ordinary matrix transpose in the computational zero/one basis. The [bridge derives the general identity](WATROUS_BRIDGE.md#remote-preparation-is-the-operational-link) and connects it to the selected Watrous 2018 source.

Take $`R=2`$ and let the parties share one Bell pair,

```math
|\Phi_2\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}.
```

Bob has three possible measurement bases. Their output labels include the basis name, so the six labels remain distinct even when two outcomes have the same numerical probability.

| Sent symbol $`a`$ | Basis outcome $`j=0`$ | Basis outcome $`j=1`$ |
|---|---|---|
| 1 | $`\vert 0\rangle`$ | $`\vert 1\rangle`$ |
| 2 | $`\vert +\rangle=(\vert 0\rangle+\vert 1\rangle)/\sqrt2`$ | $`\vert -\rangle=(\vert 0\rangle-\vert 1\rangle)/\sqrt2`$ |
| 3 | $`\vert +i\rangle=(\vert 0\rangle+i\vert 1\rangle)/\sqrt2`$ | $`\vert -i\rangle=(\vert 0\rangle-i\vert 1\rangle)/\sqrt2`$ |

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
| 1 | $`1/6`$ | $`\vert 1\rangle\langle1\vert `$ | In basis1: $`(0,1)`$ |
| 2 | $`5/12`$ | $`\mathrm{diag}(3/5,2/5)`$ | In basis2: $`(1/2,1/2)`$ |
| 3 | $`5/12`$ | $`\mathrm{diag}(3/5,2/5)`$ | In basis3: $`(1/2,1/2)`$ |

For example, $`\mathrm{Tr}(A_2)/2=5/12`$ and $`A_2/\mathrm{Tr}(A_2)=\mathrm{diag}(3/5,2/5)`$. Each vector in basis2 or3 has equal squared overlap with $`|0\rangle`$ and $`|1\rangle`$, which explains the equal conditional outcomes in those branches. Multiplying each branch probability by its conditional measurement probabilities yields the entire output distribution:

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

Continue with [the bridge's proof roadmap](WATROUS_BRIDGE.md#from-the-example-to-the-project-theorem), or return to the [scientific quantum construction](../science/quantum_construction.md).
