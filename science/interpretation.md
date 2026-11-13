# What the dimension–precision frontier means

An adaptive receiver keeps a quantum system until the sender's classical message arrives. The message selects which measurement to perform. A nonadaptive receiver chooses the quantum measurement before learning the message and uses the message only to process its classical outcome. The comparison concerns the correlations these two arrangements can generate.

Here Bob has **no independent input**. Alice sends one of three symbols, and Bob's share of the resource has Hilbert-space dimension at most $`R`$. A competing nonadaptive simulator may use unlimited shared randomness and an entirely different entangled state of arbitrary dimension. In this setting its correlations are equivalent to a classical protocol with shared randomness. The [model](model.md) specifies these quantifiers and the worst-input total-variation error.

## Two resources control the strongest possible advantage

Let $`M_*(R,\varepsilon)`$ be the supremum, over the allowed finite adaptive correlations, of the smallest nonadaptive message alphabet needed for error at most $`\varepsilon`$. The [frontier theorem](frontier.md) gives

```math
M_*(R,\varepsilon)
=\Theta\!\left(\min\{R,1+\ln(1/\varepsilon)\}\right),
\qquad 0\lt \varepsilon\leq\tfrac12,
```

with universal comparison constants. At zero error, $`M_*(R,0)=\Theta(R)`$. These are statements about the worst correlation in the specified class; they do not say that every adaptive protocol is difficult to simulate.

One [constructed family](quantum_construction.md) witnesses both parameter dependencies. Its inputs are all subsets of $`m=\lfloor R/1024\rfloor`$ labels from a universe of $`3R`$ labels. The adaptive output never belongs to Alice's subset. Three bases with uniformly small cross-submatrix norms make this possible at a constant excluded fraction. The [random-basis proof](random_bases.md) establishes existence simultaneously for every input subset.

For a classical simulator with an alphabet of size $`K\leq m`$, the [exclusion converse](classical_exclusion.md), a restatement of the established [subset-guessing inequality](../references/RELATED_WORK.md#frenkel-weiner), forces some input to have forbidden-output probability at least

```math
\frac{\binom mK}{\binom{3R}K}.
```

At constant excluded fraction this decreases exponentially in $`K`$ until the dimension scale is reached. Since a forbidden output also witnesses total-variation error, the construction meets the two universal simulation limits in order. The exact minimax value of the exclusion **game** supplies a simulation lower bound; its attaining classical game strategy need not reproduce the full quantum output distribution.

The universal upper bounds and the original unbounded separation are due to [Tavakoli](../references/RELATED_WORK.md#tavakoli-2026). The new conclusion is their joint order-level optimality under finite dimension and finite error.

## An alphabet size is different from a number of bits

The charged communication resource is the number of possible message values. An alphabet of size $`K`$ can be represented using $`\lceil\log_2K\rceil`$ fixed-length bits. Thus the growing simulation cost has bit scaling

```math
\log_2\!\left(\min\{R,1+\ln(1/\varepsilon)\}\right)+O(1).
```

In particular, logarithmic growth in inverse error for the alphabet means double-logarithmic growth for fixed-length bits before dimension saturation. The adaptive protocol uses one trit, representable by two fixed-length binary bits. Expected-length coding is a different optimization.

At any fixed positive error the required nonadaptive alphabet is bounded independently of $`R`$. To force a growing alphabet $`K`$, the dimension must be at least proportional to $`K`$, and the error must be exponentially small in $`K`$, up to constants. Increasing the entanglement dimension alone cannot produce an unbounded advantage at constant error.

## Exact simulation after uniform output replacement

The same family has a sharp consequence for a specific noisy correlation. Write $`n=3R`$ and let $`u(b)=1/n`$. Replace Bob's completed output by an independent uniform label with probability $`t`$:

```math
p_{R,t}(b\mid S)=(1-t)p_R(b\mid S)+t\,u(b).
```

For $`R\geq2048`$ and $`0\lt t\leq1/2`$, its minimum **exact** nonadaptive simulation alphabet obeys

```math
M_0(p_{R,t})
=\Theta\!\left(\min\{R,1+\ln(1/t)\}\right).
```

To see the lower bound, the forbidden-output mass of the target is exactly $`tm/(3R)`$ on every input. Any exact $`K`$-symbol simulator with $`K\leq m`$ must therefore satisfy

```math
\frac{\binom mK}{\binom{3R}K}\leq\frac{tm}{3R}.
```

For $`K\leq m/2`$, the left side is at least $`12288^{-K}`$. Consequently either $`K`$ is already proportional to $`R`$, or it must grow proportionally to $`1+\ln(1/t)`$. The exact noisy-output simulation bound in [Tavakoli's work](../references/RELATED_WORK.md#tavakoli-2026), combined with the dimension upper bound, gives the reverse order. This is a corollary of the same lower construction.

Output replacement is the specified noise model. It is not an equivalence to local noise on the entangled resource, basis miscalibration, detector errors, or continuous decoherence during storage. Those mechanisms can produce different input-dependent disturbances.

## Resource and implementation boundary

| Resource | Status in this result |
|---|---|
| Forward communication | One adaptive trit; the nonadaptive alphabet is optimized. |
| Receiver dimension | Bounded by $`R`$ for the adaptive source. |
| Entanglement supplied to the witness | A maximally entangled pair of rank $`R`$, using $`\log_2R`$ ebits. |
| Simulator's entanglement and shared randomness | Unrestricted. |
| Input and output alphabets | Finite, but may grow; the witness has $`\binom{3R}m`$ sender settings and $`3R`$ output labels. |
| Local computation, resource preparation, measurement synthesis and numerical precision | Not optimized or included in the communication cost. |

The maximally entangled resource shows that $`\log_2R`$ ebits suffice for this family. A lower bound on Hilbert-space dimension is not a lower bound on entanglement entropy for arbitrary resource states; no entropy-optimal tradeoff is established.

The bases are proved to exist, and each input POVM is specified by finite matrix formulas. This does not supply an efficient uniform circuit compiler for all those measurements. The theorem is a communication-correlation frontier, rather than an end-to-end hardware advantage, a capacity theorem, or a matching law when Bob has an independent input.

See [related work](../references/RELATED_WORK.md) for the inherited mechanisms and the precise quantitative addition.
