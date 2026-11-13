# Exact adaptive exclusion with one ternary message

This page turns the [uniform basis lemma](random_bases.md) into a quantum correlation that excludes every allowed input subset with zero error. The Gram-matrix measurement and its positivity mechanism are inherited from Tavakoli, *Unbounded advantage of adaptivity in entanglement-assisted communication*, [arXiv:2611.11333v1, Eqs. (4)–(7)](https://arxiv.org/html/2611.11333v1). The present application uses a constant-density family of excluded sets supplied by the different basis estimate.

The [model](model.md) fixes the communication resource. The [classical converse](classical_exclusion.md) and [joint frontier](frontier.md) explain what this correlation forces a nonadaptive simulator to spend. See [related work](../references/RELATED_WORK.md) for the full attribution.

## Task and fixed resources

Fix an integer $`R\ge1024`$ and put $`m=\lfloor R/1024\rfloor`$. Choose a triple of bases from the uniform basis lemma and write its vectors as

```math
|u_{j|a}\rangle=U_a|j\rangle,
\qquad
a\in\{1,2,3\},\quad j\in[R].
```

The output alphabet consists of the $`3R`$ labels $`(a,j)`$. Alice receives any $`m`$-element subset $`S`$ of this alphabet. Bob has no independent input. Their goal is to output a label outside $`S`$.

They share the fixed maximally entangled state

```math
|\Phi_R\rangle
=
\frac1{\sqrt R}\sum_{r=1}^R|r\rangle_A|r\rangle_B.
```

Each local share has dimension $`R`$. Its entanglement is $`\log_2 R`$ ebits; dimension and ebit count are different resources. Alice will send only one message from $`\{1,2,3\}`$. A fixed-length binary encoding uses two bits. No quantum message, abort event, or discarded branch is used.

## Collect the excluded vectors

For each basis label $`a`$, let $`s_a`$ be the number of labels from that basis in $`S`$. Let $`V_a`$ be the $`R\times s_a`$ matrix of the corresponding basis vectors, in any fixed order. Thus,

```math
s_1+s_2+s_3=m,
\qquad
T=[\,V_1\ V_2\ V_3\,],
\qquad
G=T^\dagger T.
```

In blocks,

```math
G=
\begin{pmatrix}
I_{s_1}&G_{12}&G_{13}\\
G_{21}&I_{s_2}&G_{23}\\
G_{31}&G_{32}&I_{s_3}
\end{pmatrix},
\qquad
G_{ab}=V_a^\dagger V_b.
```

Every cross block has norm less than $`1/4`$, because $`s_a+s_b\le m`$. Empty blocks have their natural zero-dimensional meaning.

The matrix $`G`$ is uniformly invertible. To verify this, write a vector in its three blocks as $`z=(z_1,z_2,z_3)`$ and put $`r_a=\|z_a\|_2`$. Then

```math
\begin{aligned}
|z^\dagger(G-I_m)z|
&\le
2\sum_{a<b}\|G_{ab}\|_{\mathrm{op}}r_ar_b\\
&\le
\frac12\sum_{a<b}r_ar_b\\
&\le
\frac12\sum_a r_a^2.
\end{aligned}
```

The last step follows from $`r_1r_2+r_1r_3+r_2r_3\le r_1^2+r_2^2+r_3^2`$. Hence

```math
\frac12 I_m\preceq G\preceq\frac32 I_m.
```

In particular, the columns of $`T`$ are linearly independent.

## A positive split of the Gram matrix

Define $`C_a`$ by setting its block row and column $`a`$ to zero, putting $`I/2`$ on each of the other two diagonal blocks, and retaining the cross block between those other two blocks. For example,

```math
C_1=
\begin{pmatrix}
0&0&0\\
0&\tfrac12 I_{s_2}&G_{23}\\
0&G_{32}&\tfrac12 I_{s_3}
\end{pmatrix}.
```

Each $`C_a`$ is positive semidefinite. On its two potentially nonzero blocks, a matrix of the form

```math
\begin{pmatrix}
\tfrac12 I&B\\
B^\dagger&\tfrac12 I
\end{pmatrix}
```

is bounded below by $`(\tfrac12-\|B\|_{\mathrm{op}})I`$. Here that lower bound is at least $`I/4`$. If one or both blocks are empty, positivity is immediate.

Each diagonal block of $`G`$ appears twice with weight $`1/2`$, and each cross block appears in exactly one $`C_a`$. Therefore,

```math
C_1+C_2+C_3=G.
```

For a standard coordinate vector $`e_\ell`$ corresponding to a column of $`V_a`$, the zero block column gives $`C_ae_\ell=0`$.

## The input-dependent POVM

Let

```math
P=TG^{-1}T^\dagger
```

be the orthogonal projector onto the span of the excluded vectors. Define

```math
A_{a|S}
=
TG^{-1}C_aG^{-1}T^\dagger
+
\frac{I_R-P}{3},
\qquad a\in\{1,2,3\}.
```

Both terms are positive semidefinite. Using the positive split,

```math
\sum_a A_{a|S}
=
TG^{-1}GG^{-1}T^\dagger+(I_R-P)
=
I_R.
```

Thus the three effects form a POVM.

Every excluded vector from basis $`a`$ lies in the kernel of its own effect. Indeed, if $`(a,j)\in S`$, write $`|u_{j|a}\rangle=Te_\ell`$ for its coordinate in block $`a`$. Since $`G^{-1}T^\dagger T=I_m`$,

```math
\begin{aligned}
A_{a|S}|u_{j|a}\rangle
&=
TG^{-1}C_ae_\ell
+
\frac{I_R-P}{3}Te_\ell\\
&=0.
\end{aligned}
```

If $`s_a=0`$, there is no kernel condition for that outcome. The same formula still defines a valid effect; no separate case or extra message is necessary.

## Protocol and exact output distribution

Alice measures the POVM $`\{A_{a|S}^{\mathsf T}\}_a`$, where transpose refers to the computational basis defining $`|\Phi_R\rangle`$. Transpose preserves positivity and the identity sum. She sends the outcome $`a`$. Bob then measures in basis $`a`$ and outputs $`(a,j)`$.

The joint Born probability is

```math
\begin{aligned}
p(a,j\mid S)
&=
\langle\Phi_R|
A_{a|S}^{\mathsf T}
\otimes|u_{j|a}\rangle\langle u_{j|a}|
|\Phi_R\rangle\\
&=
\frac1R
\langle u_{j|a}|A_{a|S}|u_{j|a}\rangle.
\end{aligned}
```

Equivalently, Alice remotely prepares the unnormalized conditional state $`A_{a|S}/R`$ on Bob's share. Summing the displayed probabilities gives

```math
\sum_{a,j}p(a,j\mid S)
=
\frac1R\sum_a\operatorname{Tr}A_{a|S}
=
1.
```

The kernel identity proves

```math
p(a,j\mid S)=0
\quad\text{whenever }(a,j)\in S.
```

This holds for every one of Alice's allowed input subsets, using the same entangled state and the same three Bob bases. Only Alice's POVM depends on $`S`$.

The resulting distribution need not be uniform over the allowed labels. The [classical game optimum](classical_exclusion.md) concerns the probability of landing in $`S`$; it is not an assertion that a game-optimal classical strategy reproduces this entire distribution. Its simulation lower bound uses only the necessary condition that a small total-variation error cannot assign substantial probability to an event of target probability zero.

## Exact specification and physical scope

The [basis lemma](random_bases.md) permits bases with entries in $`\mathbb Q(i)`$. Their submatrices, Gram inverse, projector, and effects above then also have entries in $`\mathbb Q(i)`$. The maximally entangled amplitude $`1/\sqrt R`$ is algebraic. Consequently the ideal state and POVMs admit finite exact mathematical descriptions.

This does not establish efficient local synthesis or a practical communication experiment. The theorem counts communication alphabet size and target entanglement dimension, with arbitrary local processing as specified in the model. Finding and certifying the bases, storing their descriptions, computing Alice's input-dependent POVM, and implementing it are not bounded by a claimed algorithmic runtime here.

The uniform positivity margins support the exact existence proof. They do not by themselves turn an imperfect physical implementation into a zero-error protocol. Any implementation errors contribute to the allowed operational error; the [interpretation](interpretation.md) keeps this distinction explicit.

