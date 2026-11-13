# Model and communication resource

[Scientific overview](README.md) · [Frontier theorem](frontier.md) · [Interpretation](interpretation.md)

Alice receives a classical input. Bob has no independent input and must produce a classical output after one message from Alice. The question is how much communication is needed when Bob must choose his quantum measurement before learning that message.

The charged resource is the number of values in the message alphabet. The target protocol sends one of three symbols. Its receiver has a quantum system of dimension at most $`R`$. A simulator may use a different shared state of unrestricted finite dimension, unrestricted shared randomness and arbitrary local operations. Thus the comparison does not require the simulator to reproduce the target apparatus or preserve its shared state.

## Adaptive target correlations

Fix finite, nonempty input and output sets $`\mathcal X`$ and $`\mathcal B`$, and an integer $`R\ge1`$. A target protocol consists of a finite-dimensional shared state $`\rho_{AB}`$ with $`\dim B\le R`$, Alice's three-outcome POVMs $`\{A_{a|x}\}_{a=1}^3`$, and Bob's POVMs $`\{B_{b|a}\}_{b\in\mathcal B}`$. It produces

```math
p(b|x)=\sum_{a=1}^{3}
\mathrm{tr}\!\left[\rho_{AB}
\left(A_{a|x}\otimes B_{b|a}\right)\right].
```

Alice sends her outcome $`a`$. Bob may choose his POVM using that outcome. Protocols with fewer than three message values are included by adding zero effects. Private randomization and local processing can be absorbed into the POVMs.

Input-independent shared classical randomness is also allowed. The formula above then holds conditioned on its value and is averaged over that value. The bound $`\dim B\le R`$ applies to the quantum share in each conditioned branch; a free shared classical label is not counted as a quantum Hilbert-space register. Denote the resulting set of conditional distributions by $`\mathcal A_3(R;\mathcal X,\mathcal B)`$.

The sets $`\mathcal X`$ and $`\mathcal B`$ may grow with $`R`$. They are finite for each individual target. No input prior is supplied: all error guarantees are worst case over $`x`$.

## Nonadaptive simulators

A nonadaptive simulator uses an $`M`$-valued message $`m`$. Bob first measures a shared quantum state with a POVM $`\{F_c\}`$ independent of $`m`$, and then decodes classically using $`m`$ and $`c`$. Without displaying shared classical randomization, its correlations have the form

```math
q(b|x)=\sum_{m=1}^{M}\sum_c
\mathrm{tr}\!\left[\sigma_{A'B'}
\left(E_{m|x}\otimes F_c\right)\right]
r(b|m,c).
```

There is no bound relating $`\dim B'`$ to $`R`$. The shared state, its dimension, the measurement outcome set and the decoder may all differ from those of the target. Shared randomness remains independent of $`x`$. A simulator is chosen for the complete target correlation, and must work for every input in its specified input set.

### Why arbitrary nonadaptive entanglement reduces to shared randomness

There is only one Bob measurement because he has no independent input. Put

```math
\pi(c)=\mathrm{tr}\!\left[\sigma_{A'B'}(I\otimes F_c)\right],
\qquad
e(m|x,c)=
\frac{\mathrm{tr}[\sigma_{A'B'}(E_{m|x}\otimes F_c)]}
{\pi(c)}
```

when $`\pi(c)>0`$. Completeness gives

```math
\sum_m e(m|x,c)=1,
\qquad
q(b|x)=\sum_c\pi(c)\sum_{m=1}^{M}
e(m|x,c)r(b|m,c).
```

The distribution $`\pi`$ is independent of $`x`$. The parties can therefore sample $`c`$ as shared randomness, after which Alice samples $`m`$ and Bob uses the same decoder. Zero-probability values are discarded. The same argument uses integrals if a measurement has continuous outcomes. Conversely, every shared-random classical protocol is a nonadaptive protocol with a trivial quantum state.

Consequently the admissible nonadaptive correlations are exactly the classical $`M`$-message correlations with shared randomness. For finite $`\mathcal X`$ and $`\mathcal B`$, these form the convex hull of deterministic encoder/decoder pairs

```math
f:\mathcal X\longrightarrow\{1,\ldots,M\},
\qquad
h:\{1,\ldots,M\}\longrightarrow\mathcal B.
```

There are finitely many such pairs, so arbitrary shared randomness gives the same closed polytope as a finite mixture. This equivalence is the no-receiver-input specialization used in [Tavakoli's adaptive communication model](../references/RELATED_WORK.md#tavakoli-2026). It does not apply when Bob has an independent measurement-setting input.

## Error and optimal alphabet

For two correlations with the same input and output sets, define

```math
d_{\mathrm{TV}}(p,q)=
\max_{x\in\mathcal X}\frac12
\sum_{b\in\mathcal B}|p(b|x)-q(b|x)|.
```

For $`0\le\varepsilon\lt 1`$, let $`M_\varepsilon(p)`$ be the smallest positive integer $`M`$ for which an admissible nonadaptive simulator satisfies $`d_{\mathrm{TV}}(p,q)\le\varepsilon`$. Equality is required when $`\varepsilon=0`$. The [exact dimension upper bound](frontier.md#inherited-exact-dimension-upper-bound) ensures this minimum is finite.

The quantity studied here is

```math
M_*(R,\varepsilon)=
\sup_{\substack{\mathcal X,\mathcal B\ \mathrm{finite}\\
p\in\mathcal A_3(R;\mathcal X,\mathcal B)}}
M_\varepsilon(p).
```

The supremum ranges over all finite input and output sets as well as all permitted target correlations. The same simulator is not required to simulate every target simultaneously. Both the target and its chosen simulator can depend on $`R`$ and on the error tolerance.

## Alphabet, bits and quantum dimension

An alphabet of size $`M`$ can be transmitted using $`\lceil\log_2 M\rceil`$ fixed-length binary bits. Bounds linear in an alphabet size must therefore not be read as bounds linear in the bit count. The target alphabet is three, so its fixed-length binary implementation uses two bits.

The parameter $`R`$ bounds the receiver's quantum Hilbert-space dimension in the target protocol. It is not a bound on the entanglement entropy. The [attaining construction](quantum_construction.md) uses a maximally entangled state of Schmidt rank $`R`$, whose entanglement entropy is $`\log_2R`$ ebits. No matching necessary entanglement-entropy bound for arbitrary shared states is claimed.

## Resource scope

The model charges one classical message alphabet and specifies the target's receiver dimension. It allows unrestricted local computation, matrix descriptions, POVMs and shared randomness. Shared entanglement is supplied before the message; its preparation time, energy and gate cost are not part of the communication score. The random-basis construction establishes the existence of finite-dimensional protocols, not an efficient uniform circuit family.

There is no additional communication, postselection or aborted output in the task. Every input produces an output with its unconditional distribution. The result concerns reproduction of conditional distributions, rather than reliable transmission of an arbitrary classical message at an asymptotic channel capacity. See [interpretation](interpretation.md) for the operational consequence and its limits.
