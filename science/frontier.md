# The dimension and precision frontier

[Model](model.md) · [Random bases](random_bases.md) · [Quantum construction](quantum_construction.md) · [Classical exclusion](classical_exclusion.md) · [Interpretation](interpretation.md)

The target sends a single ternary message and has receiver dimension at most $`R`$. Let $`M_*(R,\varepsilon)`$ be the supremal nonadaptive simulation alphabet defined in the [model](model.md#error-and-optimal-alphabet). The supremum includes every finite input and output set; the simulator's nonadaptive quantum resources and shared randomness are unrestricted.

## Main theorem

For every integer $`R\ge1`$ and $`0\lt \varepsilon\le1/2`$,

```math
\frac1{4096}\min\!\left\{R,\ln\frac1\varepsilon\right\}
\le M_*(R,\varepsilon)
\le
\min\!\left\{
3R,
1+\left\lceil\frac{\ln(1/\varepsilon)}{\ln(3/2)}\right\rceil
\right\}
\le6\min\!\left\{R,\ln\frac1\varepsilon\right\}.
```

Thus the constants are uniform when $`R`$ and $`\varepsilon`$ vary together:

```math
M_*(R,\varepsilon)
=\Theta\!\left(\min\!\left\{R,\ln\frac1\varepsilon\right\}\right).
```

Exact simulation instead satisfies

```math
\frac R{2048}\le M_*(R,0)\le3R,
```

so $`M_*(R,0)=\Theta(R)`$.

The finite lower bound is more informative before universal constants are absorbed. For $`R\ge2048`$, put

```math
m=\left\lfloor\frac R{1024}\right\rfloor,
\qquad
\lambda=\ln12288.
```

Then

```math
m+1\le M_*(R,0)\le3R,
```

and, for $`0\lt \varepsilon\le1/2`$,

```math
M_*(R,\varepsilon)
\ge
\max\!\left\{1,
\min\!\left\{\frac m2,
\frac{\ln(1/\varepsilon)}{\lambda}\right\}\right\}.
```

The bounds count alphabet symbols. Fixed-length binary communication is obtained by applying $`\lceil\log_2(\cdot)\rceil`$; see the [resource interpretation](interpretation.md).

## What is inherited and what is added

The upper bounds are [Tavakoli's](../references/RELATED_WORK.md#tavakoli-2026). The exact dimension bound uses the [Frenkel–Weiner theorem](../references/RELATED_WORK.md#frenkel-weiner), and the bounded-error bound uses message guessing followed by selection. The lower construction uses Tavakoli's split-Gram POVM with [three bases controlling every small coordinate submatrix](random_bases.md). Its constant-density forbidden sets give the matching lower orders through the [known guessing inequality and its classical minimax form](classical_exclusion.md).

## Inherited exact dimension upper bound

Condition on shared randomness. Alice prepares the subnormalized receiver states

```math
\tau_{a|x}=\operatorname{tr}_A
\!\left[(A_{a|x}\otimes I)\rho_{AB}\right],
\qquad
\tau_{a|x}\succeq0,
\qquad
\sum_a\operatorname{tr}\tau_{a|x}=1.
```

Use a direct sum on at most $`3R`$ dimensions:

```math
\widetilde\tau_x=\bigoplus_{a=1}^{3}\tau_{a|x},
\qquad
\widetilde B_b=\bigoplus_{a=1}^{3}B_{b|a}.
```

The $`\widetilde\tau_x`$ are density operators, the $`\widetilde B_b`$ form one POVM, and

```math
p(b|x)=\operatorname{tr}
\left(\widetilde\tau_x\widetilde B_b\right).
```

Frenkel–Weiner states that every finite conditional distribution obtained from states on $`D`$ dimensions and one fixed POVM belongs to the shared-random classical $`D`$-message polytope. Applying it with $`D=3R`$ gives exact simulation. Shared-random mixtures remain in that polytope, proving

```math
M_\varepsilon(p)\le M_0(p)\le3R.
```

The invoked theorem concerns the complete finite matrix of probabilities. It does not assert classical reproduction of an unknown quantum state or permit Bob to choose an independent measurement-setting input.

## Inherited bounded-error upper bound

Take $`N`$ independent target-state copies. On copy $`i`$, shared randomness guesses $`g_i\in\{1,2,3\}`$ uniformly; Bob measures $`B_{b|g_i}`$ before receiving a message. Alice obtains $`a_i`$ and sends the first index with $`a_i=g_i`$, or a failure symbol. On failure Bob samples a fixed distribution $`u`$.

For every input, the matching probability per copy is $`1/3`$, and

```math
\Pr(a_i=g_i,\ b_i=b\mid x)=\frac13p(b|x).
```

Independence across copies gives the complete output law

```math
q_N(b|x)=
\left[1-\left(\frac23\right)^N\right]p(b|x)
+\left(\frac23\right)^Nu(b).
```

Consequently

```math
d_{\mathrm{TV}}(p,q_N)\le\left(\frac23\right)^N,
\qquad
N=\left\lceil\frac{\ln(1/\varepsilon)}{\ln(3/2)}\right\rceil
```

uses $`N+1`$ message values. Bob's product measurement is independent of the selected index. Additional copies are allowed because only the target receiver dimension is bounded.

## The lower-bound target

For every $`R\ge2048`$, the [random-basis lemma](random_bases.md) supplies three orthonormal bases of $`\mathbb C^R`$ such that every cross-basis submatrix with total coordinate support at most $`m=\lfloor R/1024\rfloor`$ has operator norm at most $`1/4`$.

Label their vectors by a universe $`\mathcal U=\{1,2,3\}\times\{1,\ldots,R\}`$ of size $`3R`$. Inputs are all $`m`$-subsets $`S\subset\mathcal U`$. The [split-Gram construction](quantum_construction.md) gives an adaptive ternary-message protocol, using a maximally entangled state of Schmidt rank $`R`$, with

```math
p_R(S|S)=0\qquad\text{for every }S.
```

These are finite input and output sets for each $`R`$, and $`p_R\in\mathcal A_3(R)`$. The same correlation $`p_R`$ supplies the lower bound for every error tolerance; the bases need not change with $`\varepsilon`$.

## Lower bound for positive error

Let $`q`$ be any $`K`$-symbol simulator of $`p_R`$ with error at most $`\varepsilon>0`$. The [classical exclusion theorem](classical_exclusion.md#transfer-to-full-distribution-simulation) gives, when $`1\le K\le m`$,

```math
\varepsilon\ge d_{\mathrm{TV}}(p_R,q)
\ge\frac{\binom mK}{\binom{3R}K}.
```

If $`K\le m/2`$, the [finite binomial estimate](classical_exclusion.md#the-finite-estimate-used-in-the-frontier) yields

```math
\varepsilon\ge12288^{-K},
\qquad
K\ge\frac{\ln(1/\varepsilon)}{\lambda}.
```

If $`K>m/2`$, its alphabet already exceeds the other alternative. Every admissible alphabet is a positive integer, so in both cases

```math
K\ge\max\!\left\{1,
\min\!\left\{\frac m2,
\frac{\ln(1/\varepsilon)}{\lambda}\right\}\right\}.
```

This real-valued inequality makes no claim that $`m/2`$ or $`\ln(1/\varepsilon)/\lambda`$ is an attainable integer alphabet. It is a necessary bound for every simulator, hence for $`M_\varepsilon(p_R)`$ and its supremum.

For $`R\ge2048`$, $`m\ge R/2048`$. Also $`\lambda\lt 4096`$. With $`L=\ln(1/\varepsilon)`$,

```math
M_*(R,\varepsilon)
\ge\min\!\left\{\frac R{4096},\frac L\lambda\right\}
\ge\frac1{4096}\min\{R,L\}.
```

For $`1\le R\lt 2048`$, the trivial bound $`M_*\ge1`$ is at least $`\min\{R,L\}/4096`$. Thus the stated lower bound also covers every smaller dimension.

For the final upper simplification, $`L\ge\ln2`$ implies

```math
1+\left\lceil\frac L{\ln(3/2)}\right\rceil
\le2+\frac L{\ln(3/2)}
\le6L.
```

Combining this with $`3R\le6R`$ proves the uniform positive-error theorem.

## Exact error zero

For $`R\ge2048`$, every $`K\le m`$ has

```math
\frac{\binom mK}{\binom{3R}K}>0.
```

Thus exact simulation of $`p_R`$ needs at least $`m+1`$ symbols. This uses only a lower bound from the exclusion task; it does not assert that $`m+1`$ symbols reproduce the full correlation. Since $`m+1>R/1024`$, it in particular exceeds $`R/2048`$. For $`R\lt 2048`$, $`M_*\ge1>R/2048`$. The inherited exact upper bound $`3R`$ completes the zero-error result.

## Consequence and scope

The worst-case alphabet grows linearly with receiver dimension at exact accuracy. Under nonzero error it saturates at logarithmic order in inverse error, and this saturation is attainable within the same exclusion family. Therefore the dimension cutoff and precision cutoff are simultaneously optimal up to universal constants.

The result is an information-theoretic statement about classical conditional distributions. It provides no new channel-capacity separation, efficient gate compilation, minimum entanglement entropy or constant-error advantage growing without bound. The [interpretation](interpretation.md) explains the distinction between these statements and the sharp communication frontier.
