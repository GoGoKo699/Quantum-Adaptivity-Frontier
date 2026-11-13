# Related work and attribution

The result concerns one-way communication correlations with a fixed adaptive trit, no independent receiver input, receiver dimension at most $`R`$, and worst-input total-variation error $`\varepsilon`$. It does not compare quantum-channel capacities or general distributed computations with a receiver input. The [model](../science/model.md) fixes the operational conventions.

## Tavakoli 2026

<a id="tavakoli-2026"></a>

Armin Tavakoli, [*Unbounded advantage of adaptivity in entanglement-assisted communication*, arXiv:2611.11333v1](https://arxiv.org/html/2611.11333v1).

This work establishes unbounded adaptive advantage with a trit through subset exclusion, constructs the split-Gram POVM used here, and proves the universal bounds $`M_0\leq3R`$ without a receiver input and $`M_\varepsilon\leq1+\lceil\ln(1/\varepsilon)/\ln(3/2)\rceil`$. Its original witness uses dimension $`R=m^2+1`$ for excluded-set size $`m`$. It explicitly leaves logarithmic approximate-simulation tightness open after Eq. (11), and also gives exact simulation under input-independent output replacement noise.

The present addition is a constant-density exclusion realization, $`m=\Theta(R)`$, and its matching joint dimension–precision frontier. Unboundedness, the Gram construction, and the upper bounds are inherited.

### What the original family already implies

Combining that earlier family with the elementary classical exclusion-error calculation gives the routine lower bound $`\Omega(\min\{\sqrt R,L/\ln L\})`$ in the large-$`L`$ regime, where $`L=\ln(1/\varepsilon)`$. For example, choose an excluded-set size proportional to the candidate classical alphabet; the forced error is $`\exp[-O(K\ln K)]`$. The new bases replace this by $`\exp[-O(K)]`$ while allowing $`K=\Theta(R)`$, closing both gaps.

## Frenkel–Weiner

<a id="frenkel-weiner"></a>

Péter E. Frenkel and Mihály Weiner, [*Classical information storage in an n-level quantum system*, arXiv:1304.5723v3](https://arxiv.org/html/1304.5723v3), *Communications in Mathematical Physics* **340**, 563–574 (2015), [DOI](https://doi.org/10.1007/s00220-015-2463-0).

Their Theorem 3 equates the convex sets of prepare-and-measure correlations from an $`n`$-level quantum system and an $`n`$-symbol classical system with shared randomness. Applying it to the adaptive protocol's $`3R`$-dimensional block encoding supplies the exact dimension upper bound. Section 3, Eq. (3.6), gives the subset-guessing inequality underlying the classical exclusion score below. Both ingredients are inherited and restated with the needed conventions. The simulation theorem uses one fixed measurement scenario; it does not remove quantum advantages when the receiver has an input.

## Signaling-dimension witnesses

<a id="doolittle-chitambar-2021"></a>

Brian Doolittle and Eric Chitambar, [*Certifying the classical simulation cost of a quantum channel*](https://doi.org/10.1103/PhysRevResearch.3.043073), *Physical Review Research* **3**, 043073 (2021); [arXiv:2102.12543v1](https://arxiv.org/abs/2102.12543v1).

Appendix D.1, Eqs. (D2)–(D4), writes the established subset-guessing bound as a signaling-dimension witness and credits Frenkel–Weiner. Taking $`n-m`$ allowed answers among $`n`$ outputs and an alphabet of size $`K`$ gives normalized average failure $`\binom mK/\binom nK`$. Symmetry turns this into the exact minimax exclusion value reproduced here. Neither that classical bound nor their general witness framework supplies the constant-density adaptive trit realization or the joint $`R,\varepsilon`$ frontier. Their partial-replacer-channel analysis concerns a different physical channel class.

## Haar submatrix estimates and uncertainty

<a id="adamczak-et-al"></a>

Radosław Adamczak, Rafał Latała, Zbigniew Puchała and Karol Życzkowski, [*Asymptotic entropic uncertainty relations*, arXiv:1412.7065v2](https://arxiv.org/html/1412.7065v2), *Journal of Mathematical Physics* **57**, 032204 (2016), [DOI](https://doi.org/10.1063/1.4944425).

Their Theorem 7 bounds the maximum norm of prescribed-size submatrices of a Haar unitary, and Appendix A.2 supplies its proof. Such uniform small-submatrix estimates are established uncertainty tools. The [random-basis lemma](../science/random_bases.md) gives a self-contained tail-and-net proof with conservative constants for this application. Its role is to feed the inherited POVM construction; a new general random-matrix theorem is not claimed.

## Contribution boundary

The advance is the sharp worst-case alphabet law

```math
\Theta\!\left(\min\{R,1+\ln(1/\varepsilon)\}\right)
```

and the corresponding exact $`\Theta(R)`$ dimension law in the stated adaptive-trit model. The [interpretation](../science/interpretation.md) distinguishes alphabet size from transmitted bits, gives the uniform-output-noise corollary, and states the implementation resources left unoptimized. This attribution and comparison support a bounded novelty claim; they are not an exhaustive priority certificate.

Machine-readable entries are in [references.bib](references.bib).
