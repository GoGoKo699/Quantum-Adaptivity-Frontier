# Exact classical exclusion error

[Model](model.md) · [Quantum realization](quantum_construction.md) · [Frontier theorem](frontier.md)

The lower bound uses a distributed exclusion task. Alice is told a forbidden subset. Bob must return a label outside it. The exact classical value is useful because it converts a zero-probability event in the quantum distribution into a quantitative obstruction to approximation.

The converse below is the known guessing inequality of Frenkel–Weiner, presented in [Doolittle–Chitambar, Appendix D.1, Eq. (D2)](../references/RELATED_WORK.md#doolittle-chitambar-2021). Their parameters are $`n'=n`$, $`k=n-m`$ and $`d=K`$: the allowed set is the complement of the forbidden set. Dividing their total success bound by $`\binom nm`$ gives the failure bound $`\binom mK/\binom nK`$. We re-prove that bound directly and use permutation symmetrization to obtain the worst-input minimax equality. This is an inherited classical ingredient, not a new classical theorem.

## The task

Let $`\mathcal U`$ be a universe of size $`n`$, with $`1\le m\lt n`$. Alice's input is any $`m`$-element subset $`S\subset\mathcal U`$. Bob has no input and returns one label $`b\in\mathcal U`$. A protocol fails when $`b\in S`$.

The parties share arbitrary input-independent randomness and Alice sends one of $`K`$ symbols. Write the minimum worst-input failure probability as

```math
e_{n,m}(K)=
\inf_{q\ \mathrm{classical},\ K\ \mathrm{symbols}}
\ \max_{\substack{S\subset\mathcal U\\ |S|=m}}
q(S|S),
\qquad
q(S|S):=\sum_{b\in S}q(b|S).
```

By the [nonadaptive-to-classical reduction](model.md#why-arbitrary-nonadaptive-entanglement-reduces-to-shared-randomness), the same value holds if the simulator has arbitrary nonadaptive shared quantum resources.

## Exact minimax value

**Known guessing bound and its minimax form.** For every positive integer $`K`$,

```math
e_{n,m}(K)=
\begin{cases}
\displaystyle\frac{\binom mK}{\binom nK},&1\le K\le m,\\[6pt]
0,&K\ge m+1.
\end{cases}
```

The equality is for success in the exclusion task. It does not identify the communication cost of reproducing a particular complete quantum distribution.

### Converse with arbitrary randomness

Fix all random seeds of a classical protocol, including private seeds. The remaining encoder and decoder are deterministic. Bob's possible decoded outputs form a set

```math
T=\{h(1),\ldots,h(K)\},
\qquad s:=|T|\le K.
```

If $`T\subseteq S`$, every possible message makes Bob fail. Choose $`S`$ uniformly from all $`m`$-subsets. For $`K\le m`$,

```math
\Pr_S[T\subseteq S]
=\frac{\binom{n-s}{m-s}}{\binom nm}
=\frac{\binom ms}{\binom ns}
\ge\frac{\binom mK}{\binom nK}.
```

The last inequality holds because consecutive ratios are related by

```math
\frac{\binom m{s+1}/\binom n{s+1}}
{\binom ms/\binom ns}
=\frac{m-s}{n-s}\lt 1.
```

Averaging over the fixed seeds preserves the lower bound on average-input failure. The worst-input failure is at least that average. Randomness depending on the input would invalidate this argument; such preshared randomness is excluded by the model.

### Matching protocol

For $`K\le m`$, use shared randomness to choose a uniformly random $`K`$-subset $`T`$ of $`\mathcal U`$. Both parties know its fixed ordering. Alice sends the index of an element in $`T\setminus S`$ whenever one exists. If $`T\subseteq S`$, she sends any index and failure is unavoidable. For every fixed $`S`$,

```math
\Pr_T[T\subseteq S]
=\frac{\binom mK}{\binom nK}.
```

For $`K\ge m+1`$, agree on $`m+1`$ distinct labels. At least one lies outside every forbidden $`m`$-subset, so the same index protocol succeeds deterministically. Thus the exact zero-error threshold is $`K=m+1`$.

For example, at $`n=9`$, $`m=4`$ and $`K=3`$, the optimal worst-input failure is $`\binom43/\binom93=1/21`$. Five symbols permit zero failure. These values concern the exclusion score, without selecting any particular target distribution on the allowed labels.

## Transfer to full-distribution simulation

Suppose an adaptive target correlation satisfies

```math
p(S|S)=0
\qquad\text{for every }S.
```

For any simulator $`q`$, the event characterization of total variation gives

```math
\frac12\sum_{b\in\mathcal U}|p(b|S)-q(b|S)|
\ge |p(S|S)-q(S|S)|
=q(S|S).
```

Therefore every $`K`$-symbol nonadaptive simulator obeys

```math
d_{\mathrm{TV}}(p,q)
\ge e_{n,m}(K).
```

This is a necessary condition for reproducing $`p`$. The matching exclusion protocol above need not match $`p`$ on allowed outputs, so it supplies no converse equality for $`M_\varepsilon(p)`$.

## The finite estimate used in the frontier

The [quantum construction](quantum_construction.md) takes

```math
n=3R,\qquad
m=\left\lfloor\frac R{1024}\right\rfloor,
\qquad R\ge2048.
```

In this range $`m\ge R/2048`$. If $`1\le K\le m/2`$, then

```math
\begin{aligned}
\frac{\binom mK}{\binom{3R}K}
&=\prod_{i=0}^{K-1}\frac{m-i}{3R-i}\\
&\ge\left(\frac{m}{6R}\right)^K\\
&\ge 12288^{-K}.
\end{aligned}
```

Indeed $`i\le K-1\lt m/2`$, so $`m-i\ge m/2`$, while $`3R-i\le3R`$. The estimate is deliberately conservative; the exact binomial expression remains available for finite parameters.

With $`\lambda:=\ln12288`$, a simulator of error at most $`\varepsilon>0`$ and alphabet $`K\le m/2`$ must consequently satisfy

```math
\varepsilon\ge e^{-\lambda K},
\qquad
K\ge\frac{\ln(1/\varepsilon)}{\lambda}.
```

An alphabet larger than $`m/2`$ already has order $`R`$. The [frontier proof](frontier.md#lower-bound-for-positive-error) combines these two alternatives without treating an integer threshold as an equality.
