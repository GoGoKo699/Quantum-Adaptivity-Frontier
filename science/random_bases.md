# Three bases with uniformly small cross submatrices

The communication construction needs one fixed triple of bases that works for every allowed input subset. Bounding a typical subset is insufficient. This page proves the required uniform existence statement directly, using Haar measure and finite nets. The probabilistic tools are standard; the communication application and attribution are discussed in [related work](../references/RELATED_WORK.md).

Read the [operational model](model.md) for the resource and error conventions. The resulting bases feed into the [exact quantum protocol](quantum_construction.md), which supplies the lower construction in the [joint frontier](frontier.md).

## Uniform basis lemma

For every integer $`R\ge 1024`$, put

```math
m=\left\lfloor\frac{R}{1024}\right\rfloor.
```

There are three orthonormal bases of $`\mathbb C^R`$, represented by unitary matrices $`U_1,U_2,U_3`$, such that

```math
\left\|
  U_a[:,I]^\dagger U_b[:,J]
\right\|_{\mathrm{op}}
\lt
\frac14
```

for every distinct $`a,b\in\{1,2,3\}`$ and every pair of index subsets $`I,J\subseteq[R]`$ satisfying $`|I|+|J|\le m`$. The norm of a matrix with an empty row or column set is zero.

The same triple works simultaneously for all those pairs of subsets. Its matrices may be chosen to have rational real and imaginary parts. This is an existence statement with finite exact descriptions, not an efficient synthesis or search algorithm.

## A complex Haar coordinate

Let $`U`$ be Haar distributed on $`U(R)`$, and let $`x,y\in\mathbb C^R`$ be fixed unit vectors. Unitary invariance makes $`Uy`$ uniform on the complex unit sphere, so $`|x^\dagger Uy|`$ has the distribution of the absolute value of its first coordinate. For $`0\le t\lt 1`$,

```math
\Pr\!\left\{
  |x^\dagger Uy|\ge t
\right\}
=
(1-t^2)^{R-1}.
```

For completeness, take independent standard complex Gaussian variables $`g_1,\ldots,g_R`$. Their squared magnitudes are independent mean-one exponential variables, and $`g/\left\|g\right\|_2`$ is uniform on the sphere. If

```math
X=|g_1|^2,
\qquad
Y=\sum_{j=2}^R|g_j|^2,
```

then, with $`u=t^2`$,

```math
\begin{aligned}
\Pr\!\left\{\frac{X}{X+Y}\ge u\right\}
&=
\mathbb E\exp\!\left(-\frac{u}{1-u}Y\right)\\
&=
\left(1+\frac{u}{1-u}\right)^{-(R-1)}
=
(1-u)^{R-1}.
\end{aligned}
```

Only the displayed scalar tail is used below.

## Finite nets control each submatrix

The unit sphere in $`\mathbb C^s`$, regarded as a subset of $`\mathbb R^{2s}`$, has a $`\delta`$-net of cardinality at most $`(1+2/\delta)^{2s}`$. One proof takes a maximal $`\delta`$-separated set on the sphere. The open balls of radius $`\delta/2`$ around its points are disjoint and lie in the ball of radius $`1+\delta/2`$. Comparing their real $`2s`$-dimensional volumes bounds their number, and maximality supplies the covering property.

Fix supports $`I,J`$ with $`p=|I|>0`$, $`q=|J|>0`$, and write $`A=U[I,J]`$. Choose $`1/8`$-nets on their unit spheres. For unit vectors $`v,w`$ attaining $`|v^\dagger Aw|=\left\|A\right\|_{\mathrm{op}}`$, choose net points $`v_0,w_0`$ within $`1/8`$. Since all four vectors have norm one,

```math
\begin{aligned}
|v_0^\dagger Aw_0|
&\ge
|v^\dagger Aw|
-
|(v-v_0)^\dagger Aw|
-
|v_0^\dagger A(w-w_0)|\\
&\ge
\frac34\left\|A\right\|_{\mathrm{op}}.
\end{aligned}
```

Thus $`\left\|A\right\|_{\mathrm{op}}\ge1/4`$ forces at least one net bilinear form to have magnitude at least $`3/16`$. After embedding the net vectors on their fixed supports into $`\mathbb C^R`$, the Haar-coordinate formula applies to each pair. There are at most $`17^{2(p+q)}`$ pairs. Consequently,

```math
\Pr\!\left\{
  \left\|U[I,J]\right\|_{\mathrm{op}}\ge\frac14
\right\}
\le
17^{2(p+q)}
\left(\frac{247}{256}\right)^{R-1}.
```

Empty supports never violate the desired bound.

## One union bound covers all inputs

It suffices to control supports of total size exactly $`m`$. Any pair with smaller total size can be enlarged to such a pair, because $`m\lt R`$. A submatrix's operator norm cannot decrease when rows or columns are added.

The number of ordered support pairs with total size $`m`$ is

```math
\sum_{p=0}^m
\binom Rp\binom R{m-p}
=
\binom{2R}{m}.
```

Choose $`U_1=I_R`$ and choose $`U_2,U_3`$ independently from Haar measure. Each of $`U_1^\dagger U_2`$, $`U_1^\dagger U_3`$, and $`U_2^\dagger U_3`$ is marginally Haar. These three matrices are dependent; a union bound requires no independence between their bad events. Reversing a pair only takes an adjoint and preserves its submatrix norm.

The probability that any required cross submatrix fails is therefore at most

```math
B_R
=
3\binom{2R}{m}\,
17^{2m}
\left(\frac{247}{256}\right)^{R-1}.
```

This bound is strictly less than one for every $`R\ge1024`$. Indeed, $`\binom{2R}{m}\le(2eR/m)^m`$, and the function $`s\mapsto s\ln(2eR/s)`$ increases on $`0\lt s\lt 2R`$. Using $`m\le R/1024`$ and $`\ln(1-u)\le-u`$ gives

```math
\ln B_R
\le
\ln3+
\frac{R}{1024}
\bigl[\ln(2048e)+2\ln17\bigr]
-\frac{9(R-1)}{256}.
```

The elementary bounds $`\ln3\lt 2`$, $`\ln2048\lt 8`$, and $`\ln17\lt 3`$ imply

```math
\ln B_R
\lt
2+\frac{36}{1024}
-\frac{21R}{1024}
\lt
0
\qquad
(R\ge1024).
```

A triple outside all bad events proves the lemma, with strict slack below $`1/4`$.

## Finite exact descriptions

The probabilistic proof need not leave the protocol dependent on infinitely specified real numbers. For fixed $`R`$, only finitely many support pairs occur. Their submatrix norms depend continuously on the two chosen unitary matrices. A successful triple with strict slack consequently has an open neighborhood of successful triples.

Unitary matrices with rational real and imaginary parts are dense in $`U(R)`$. To see this, first approximate a given unitary by one with no eigenvalue $`-1`$. Such a unitary has the Cayley representation

```math
U=(I+iH)(I-iH)^{-1},
\qquad H=H^\dagger.
```

Approximate $`H`$ by Hermitian matrices whose entries have rational real and imaginary parts. Their Cayley transforms are exactly unitary, have entries in $`\mathbb Q(i)`$, and converge to $`U`$. Choosing such transforms inside the successful neighborhood preserves all the strict norm bounds. The fixed first basis $`U_1=I_R`$ already has rational entries.

The [Gram construction](quantum_construction.md) then uses finite rational matrix operations to specify its POVM effects. This observation establishes finite mathematical descriptions only. It supplies no polynomial bound on finding, certifying, or implementing the bases, and it does not charge those operations as communication.

## Consequence and limits

These bases allow exclusion sets containing $`\Theta(R)`$ labeled vectors while retaining the positivity margin required by the quantum measurement. The earlier mutually unbiased basis construction used a Frobenius-norm estimate with a quadratic relation between entanglement dimension and excluded-set size. The exact measurement construction itself is inherited; replacing that estimate by uniform cross-submatrix control is the step used here.

The [classical exclusion converse](classical_exclusion.md) converts this constant-density family into a simulation lower bound. The [frontier theorem](frontier.md) combines it with the inherited universal upper bounds. The [interpretation](interpretation.md) separates alphabet size, bits, dimension, and the uncharged local processing.
