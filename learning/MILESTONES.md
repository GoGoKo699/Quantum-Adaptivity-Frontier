# Thirty milestones for the adaptivity frontier

[Learning guide](README.md) · [Watrous bridge](WATROUS_BRIDGE.md) · [Scientific account](../science/README.md)

This map follows the project's argument, from individual states and measurements to a uniform law for the strongest possible communication advantage. Its single educational anchor is John Watrous, *The Theory of Quantum Information* (2018), using the author's January-2018 pre-publication manuscript. Section, equation and exercise identifiers below refer to that manuscript; page numbers are its printed page numbers, not PDF-page indices.

The allocation is **12 background/preliminary milestones and 18 narrative/innovation milestones**. The background joins quantum measurements, classical randomization, approximation and matrix geometry into one operational framework. The narrative then joins the two inherited upper bounds, the constant-density quantum construction and the classical converse into the complete dimension–precision frontier. Both phases end by assembling their components.

Watrous supplies the foundations. The project proof pages supply its particular Haar-tail/net argument, exclusion construction, resource frontier and attribution. A pointer to Watrous is a prerequisite connection, not a claim that the new frontier theorem appears in the book. Primary-paper comparisons in the scientific account remain scientific references rather than additional educational anchors.

## Background/preliminaries — M01–M12

### M01 — Inputs, outputs and conditional experiments

**Phase:** Background/preliminaries.

**Central question:** What does a table of conditional probabilities describe in this communication experiment?

**Understanding target:** Identify Alice's input, the communicated symbol and Bob's output as distinct labels. Explain why a correlation specifies one output distribution for every input, rather than a single success probability averaged over a supplied prior.

**Dependencies and story role:** None. Establishes the classical experiment before adding quantum resources.

**Conceptual connection:** Finite register alphabets become the input and output sets over which the final supremum is taken.

**Source pointers:** Watrous [§2.1.1, pp. 58–60][W2] and [§1.2.2, starting p. 47][W1]; [project model: adaptive target correlations](../science/model.md#adaptive-target-correlations).

### M02 — A quantum state and its dimension

**Phase:** Background/preliminaries.

**Central question:** What resource is bounded when the receiver's quantum share has dimension $`R`$?

**Understanding target:** Read a density operator on $`\mathbb C^R`$ as a state of an $`R`$-dimensional register. Distinguish the number of available basis labels from the number of classical input settings and from the number of transmitted bits.

**Dependencies and story role:** M01. Introduces the quantum object whose size will control one side of the frontier.

**Conceptual connection:** The bound concerns the target receiver's Hilbert space, while the competing simulator's quantum resources are unrestricted.

**Source pointers:** Watrous [§1.1.1, starting p. 1][W1] and [§2.1.2, starting p. 61][W2]; [model: alphabet, bits and quantum dimension](../science/model.md#alphabet-bits-and-quantum-dimension).

### M03 — Positive measurement effects and probabilities

**Phase:** Background/preliminaries.

**Central question:** What makes a list of operators a valid measurement?

**Understanding target:** Explain the two requirements of a POVM: each effect is positive semidefinite and their sum is the identity. Connect these requirements to nonnegative Born probabilities summing to one, and recognize a basis measurement as a special case.

**Dependencies and story role:** M02. Supplies the physical validity conditions that the later Gram construction must meet.

**Conceptual connection:** A matrix formula becomes a protocol only after its positivity and normalization have been proved.

**Source pointers:** Watrous [§2.3.1, starting p. 100][W2]; [quantum construction: the input-dependent POVM](../science/quantum_construction.md#the-input-dependent-povm).

### M04 — Local shares and reduced states

**Phase:** Background/preliminaries.

**Central question:** How can one shared state describe two laboratories while each laboratory has its own state?

**Understanding target:** Interpret a bipartite state, its tensor-product space and its reduced receiver state. Explain why averaging over an uncommunicated local measurement outcome leaves the receiver's marginal fixed.

**Dependencies and story role:** M02, M03. Moves from one register to the shared resource used by both parties.

**Conceptual connection:** The fixed receiver marginal is the constraint behind remote ensemble preparation and the reduction of a fixed receiver measurement to shared randomness.

**Source pointers:** Watrous [§2.1.3, starting p. 67][W2] and [§2.3.2, Eq. (2.226)][W2]; [model: nonadaptive simulators](../science/model.md#nonadaptive-simulators).

### M05 — Conditional states from a maximally entangled pair

**Phase:** Background/preliminaries.

**Central question:** How does Alice's measurement select an ensemble for Bob without changing his average state?

**Understanding target:** Interpret an unnormalized conditional state: its trace gives the outcome probability and its normalized version gives the state in that branch. Understand the project identity that measuring $`A^{\mathsf T}`$ on one half of a rank-$`R`$ maximally entangled pair prepares $`A/R`$ on the other half.

**Dependencies and story role:** M03, M04. Connects measurement effects to remotely prepared receiver states.

**Conceptual connection:** A kernel of an Alice effect will later become an exactly forbidden Bob output.

**Source pointers:** Watrous [§2.3.2, Eq. (2.226), and Exercise 2.2, p. 120][W2]; [quantum construction: protocol and exact output distribution](../science/quantum_construction.md#protocol-and-exact-output-distribution).

### M06 — What the message is allowed to change

**Phase:** Background/preliminaries.

**Central question:** Where does adaptivity enter a one-way entanglement-assisted protocol?

**Understanding target:** Distinguish a message that selects a quantum measurement from a message that only processes an existing classical record. Identify the order of operations and explain why Bob's absence of an independent input is a material restriction.

**Dependencies and story role:** M01, M03, M05. Organizes the local objects into the two competing causal arrangements.

**Conceptual connection:** Keeping the receiver's quantum share until the message arrives is the capability whose simulation cost is studied.

**Source pointers:** Watrous [§6.1.2, starting p. 324, and §6.3.1, starting p. 359][W6]; [model: adaptive targets and nonadaptive simulators](../science/model.md#adaptive-target-correlations).

### M07 — Shared randomness as a convex mixture

**Phase:** Background/preliminaries.

**Central question:** Why can arbitrary randomized classical protocols be studied through deterministic encoders and decoders?

**Understanding target:** View input-independent randomization as a convex combination of deterministic conditional-probability tables. Explain why fixing all seeds leaves at most one decoded output per possible message, without assuming that one fixed seed works well on every input.

**Dependencies and story role:** M01, M06. Supplies the classical geometry needed for the converse while retaining arbitrary shared randomness.

**Conceptual connection:** Averaging a bound over fixed seeds will be valid; selecting a bad input separately for every seed will not establish the required worst-input randomized bound.

**Source pointers:** Watrous [§1.2.1, Theorems 1.9–1.10, p. 45][W1]; [model: why nonadaptive entanglement reduces to shared randomness](../science/model.md#why-arbitrary-nonadaptive-entanglement-reduces-to-shared-randomness).

### M08 — Approximation judged by observable events

**Phase:** Background/preliminaries.

**Central question:** How can one event certify that two complete output distributions are different?

**Understanding target:** Read worst-input total-variation error and its half-$`\ell_1`$ normalization. Explain why assigning probability to a target-impossible event gives a lower bound on that error, even when the probabilities on every other output are unknown.

**Dependencies and story role:** M01, M03. Introduces the operational metric connecting a task score to full-distribution simulation.

**Conceptual connection:** The classical exclusion failure will become a necessary error bound rather than an assertion that a game-optimal protocol simulates the whole target.

**Source pointers:** Watrous [§1.2.2, starting p. 47][W1] for probability notation; [model: error and optimal alphabet](../science/model.md#error-and-optimal-alphabet) and [the local event-to-TV argument](../science/classical_exclusion.md#transfer-to-full-distribution-simulation). The project pages supply the required event inequality.

### M09 — Gram matrices and overlap geometry

**Phase:** Background/preliminaries.

**Central question:** What does a Gram matrix retain about a collection of selected vectors?

**Understanding target:** Connect the entries of $`T^\dagger T`$ to pairwise overlaps, its quadratic form to $`\|Tz\|^2`$, and its eigenvalue bounds to linear independence. Interpret cross-basis submatrix norms as bounds applying to arbitrary superpositions on their selected coordinates.

**Dependencies and story role:** M02, M03. Introduces the geometry that controls the constructed measurement globally rather than entry by entry.

**Conceptual connection:** Uniform overlap control provides both an invertible selected Gram matrix and the positivity margin for its decomposition.

**Source pointers:** Watrous [§1.1.2, starting p. 8, and §1.1.3, starting p. 24][W1]; [quantum construction: collect the excluded vectors](../science/quantum_construction.md#collect-the-excluded-vectors).

### M10 — Positivity, kernels and projectors

**Phase:** Background/preliminaries.

**Central question:** How can an operator be positive and still forbid selected vectors exactly?

**Understanding target:** Distinguish positive semidefiniteness from strict positivity, identify a kernel, and interpret an orthogonal projector as the identity on a span and zero on its orthogonal complement. Understand why adding a positive term on that complement can complete a measurement without disturbing the prescribed kernels.

**Dependencies and story role:** M03, M09. Assembles the matrix tools used to turn overlap geometry into exact exclusion.

**Conceptual connection:** The two terms of the final POVM handle the selected span and its complement separately while their sum covers the full receiver space.

**Source pointers:** Watrous [§1.1.2 and §1.1.3][W1]; [quantum construction: a positive split](../science/quantum_construction.md#a-positive-split-of-the-gram-matrix) and [the POVM formula](../science/quantum_construction.md#the-input-dependent-povm).

### M11 — Random bases and simultaneous guarantees

**Phase:** Background/preliminaries.

**Central question:** How can randomness establish one apparatus that works for every permitted input?

**Understanding target:** Distinguish choosing a random basis once from drawing a new basis for each input. Identify the role of Haar invariance and of a union bound over bad events; explain why a probability below one for any failure proves the existence of one uniformly successful fixed choice.

**Dependencies and story role:** M07, M09. Joins probability to matrix geometry without yet using the project's quantitative estimate.

**Conceptual connection:** The bases are selected before Alice's input, so a typical-input or average-subset guarantee would not prove the protocol required by the theorem.

**Source pointers:** Watrous [§1.2.2][W1] and [§7.2.1, starting p. 408][W7]; [random-basis lemma and its quantifiers](../science/random_bases.md#uniform-basis-lemma).

### M12 — Assemble the complete simulation question

**Phase:** Background/preliminaries.

**Central question:** Which resources, quantifiers and error convention must remain together when comparing the two protocols?

**Understanding target:** State the target and simulator classes, the supremum over finite input/output sets, the worst-input tolerance and the positive-integer alphabet cost. Keep quantum dimension, shared randomness, transmitted bits and uncharged local processing separate in one account.

**Dependencies and story role:** M02, M06, M07, M08, M11. Integrates the background into the precise question answered by the narrative.

**Conceptual connection:** Neither large entanglement dimension alone nor a favorable score for one input establishes the claimed worst-case frontier.

**Source pointers:** Watrous [§2.1.1–§2.1.3][W2] and [§6.1.2][W6]; [complete project model](../science/model.md) and [bridge](WATROUS_BRIDGE.md).

## Narrative/innovation — M13–M30

### M13 — The inherited exact dimension ceiling

**Phase:** Narrative/innovation.

**Central question:** Why can every allowed target be simulated exactly using at most $`3R`$ classical symbols?

**Understanding target:** Form the three-block state from Alice's conditional ensembles and the matching block-diagonal Bob POVM. Explain how the inherited Frenkel–Weiner correlation theorem applies on that $`3R`$-dimensional space, and why it requires the absence of an independent receiver input.

**Dependencies and story role:** M05, M07, M12. Establishes the first universal ceiling before constructing a hard target.

**Conceptual connection:** Remote conditional states become an ordinary fixed-measurement correlation table; classical simulation concerns that table, not reproduction of an unknown quantum state.

**Source pointers:** Watrous [§2.3.2, Eq. (2.226)][W2] and [§1.2.1][W1]; [frontier: inherited exact dimension upper bound](../science/frontier.md#inherited-exact-dimension-upper-bound), including its primary-source attribution.

### M14 — The inherited precision ceiling

**Phase:** Narrative/innovation.

**Central question:** How does guessing the message before measurement give a universal approximate simulator?

**Understanding target:** Explain the independent trials, the first correct guess and the fallback output. Account for the unconditional mixture with failure weight $`(2/3)^N`$, its total-variation error and its $`N+1`$ message values. Recognize that the simulator may use more entanglement than the target.

**Dependencies and story role:** M06, M08, M12. Adds the second universal ceiling and identifies the precision dependence that a matching construction must attain.

**Conceptual connection:** Selecting a previously measured copy is classical decoding and therefore respects nonadaptivity.

**Source pointers:** Watrous [§1.2.2][W1] and [§2.3.2][W2]; [frontier: inherited bounded-error upper bound](../science/frontier.md#inherited-bounded-error-upper-bound).

### M15 — The established classical exclusion value

**Phase:** Narrative/innovation.

**Central question:** How much can a shared-random $`K`$-symbol protocol avoid every forbidden $`m`$-subset of an $`n`$-label universe?

**Understanding target:** Reconstruct the deterministic output-list converse under a uniform input subset, then average over seeds. Explain how a uniformly random $`K`$-subset attains worst-input failure $`\binom mK/\binom nK`$ for $`K\le m`$, while $`m+1`$ labels permit zero failure.

**Dependencies and story role:** M01, M07, M12. Supplies the inherited quantitative classical obstruction, including its matching game strategy.

**Conceptual connection:** Permutation symmetry connects the average-input guessing inequality to an exact worst-input game value.

**Source pointers:** Watrous [§1.2.1–§1.2.2][W1]; [classical exclusion: exact minimax value and attribution](../science/classical_exclusion.md#exact-minimax-value).

### M16 — A game lower bound for complete correlations

**Phase:** Narrative/innovation.

**Central question:** What does zero forbidden-output probability imply for a simulator of the full quantum distribution?

**Understanding target:** Apply the event-to-TV inequality separately on every input and then take the worst input. Keep the valid simulation lower bound distinct from an unsupported equality between game complexity and complete-distribution simulation complexity.

**Dependencies and story role:** M08, M15. Turns a classical task bound into the metric obstruction needed by the frontier.

**Conceptual connection:** The proof needs an exactly absent target event; it does not need the target to be uniform on its allowed outputs.

**Source pointers:** Watrous [§1.2.2][W1] for probability foundations; [classical exclusion: transfer to full-distribution simulation](../science/classical_exclusion.md#transfer-to-full-distribution-simulation).

### M17 — Why the forbidden fraction must stay positive

**Phase:** Narrative/innovation.

**Central question:** Which change to the earlier exclusion family can make both universal ceilings sharp?

**Understanding target:** Compare a forbidden-set size growing only as $`\sqrt R`$ with one proportional to $`R`$. Explain why constant forbidden density lets the binomial obstruction decrease exponentially in the classical alphabet while retaining a dimension-scale zero-error threshold.

**Dependencies and story role:** M13, M14, M15, M16. Identifies the scientific gap and the target property of the new realization before entering its proof.

**Conceptual connection:** The goal is a stronger uniform quantum realization of the known exclusion task, rather than a new classical guessing inequality or another universal upper bound.

**Source pointers:** Watrous [§1.1.3 and §1.2.2][W1]; [related work: what the original family already implies](../references/RELATED_WORK.md#what-the-original-family-already-implies) and [random bases: consequence and limits](../science/random_bases.md#consequence-and-limits).

### M18 — The scalar Haar tail

**Phase:** Narrative/innovation.

**Central question:** Why is a fixed overlap unlikely to be large in a high-dimensional random basis?

**Understanding target:** Use unitary invariance to reduce $`|x^\dagger Uy|`$ to one coordinate of a uniform complex unit vector. Follow the normalized-complex-Gaussian calculation of its exact tail $`(1-t^2)^{R-1}`$ and identify which vectors are fixed before the Haar draw.

**Dependencies and story role:** M09, M11, M17. Provides the local probabilistic estimate that will control all submatrices.

**Conceptual connection:** Exponential decay in dimension will pay for a finite collection of possible supports and directions.

**Source pointers:** Watrous [§7.2.1, starting p. 408][W7]; [random bases: a complex Haar coordinate](../science/random_bases.md#a-complex-haar-coordinate), which supplies the exact calculation used here.

### M19 — From finitely many directions to an operator norm

**Phase:** Narrative/innovation.

**Central question:** How can a finite net control every superposition on selected coordinates?

**Understanding target:** Explain the sphere-covering bound and the two replacement errors in a bilinear form. With $`1/8`$-nets, connect a submatrix norm of at least $`1/4`$ to a tested overlap of at least $`3/16`$, including the net cardinality cost.

**Dependencies and story role:** M09, M10, M18. Converts a scalar tail into a support-wise norm guarantee.

**Conceptual connection:** The argument controls a whole continuous family of directions by deterministic approximation followed by a probability bound.

**Source pointers:** Watrous [§1.1.3 and §1.2.1][W1] for norms and finite-dimensional geometry, and [§7.3.1, starting p. 430][W7] for concentration context; [the project's finite-net proof](../science/random_bases.md#finite-nets-control-each-submatrix). No application of Lévy's lemma is required.

### M20 — One triple of bases for every input

**Phase:** Narrative/innovation.

**Central question:** Why does the uniform estimate survive all choices of a constant-density excluded subset?

**Understanding target:** Count support pairs by $`\binom{2R}m`$, use monotonicity under support enlargement, and combine the net count with the Haar tail. Explain why the three relative unitaries need only be marginally Haar, and why a union-bound failure probability below one proves a fixed successful triple.

**Dependencies and story role:** M11, M18, M19. Assembles the local probability estimates into the required global basis property.

**Conceptual connection:** The choice $`m=\lfloor R/1024\rfloor`$ makes the exponentially small tail dominate every permitted support choice simultaneously.

**Source pointers:** Watrous [§1.2.2][W1] and [§7.2.1][W7]; [random bases: one union bound covers all inputs](../science/random_bases.md#one-union-bound-covers-all-inputs).

### M21 — A selected Gram matrix stays invertible

**Phase:** Narrative/innovation.

**Central question:** What does the uniform basis property imply for the vectors named by one input subset?

**Understanding target:** Assemble $`T=[V_1\ V_2\ V_3]`$ and its three-block Gram matrix. Derive the spectrum interval $`[1/2,3/2]`$ from the cross-block norm bound, including inputs with empty blocks.

**Dependencies and story role:** M09, M10, M20. Transfers the global basis guarantee to the input-dependent matrix from which the protocol is built.

**Conceptual connection:** Controlling coherent superpositions across all selected blocks supplies a valid inverse and a stable selected span.

**Source pointers:** Watrous [§1.1.2–§1.1.3][W1]; [quantum construction: collect the excluded vectors](../science/quantum_construction.md#collect-the-excluded-vectors).

### M22 — Split the Gram matrix into positive pieces

**Phase:** Narrative/innovation.

**Central question:** How can three positive matrices sum to the Gram matrix while each ignores one basis block?

**Understanding target:** Explain the half-identity diagonal blocks, the retained cross block and the zero block row/column in each $`C_a`$. Verify both positivity and $`\sum_aC_a=G`$, rather than treating a formal decomposition as sufficient.

**Dependencies and story role:** M03, M10, M21. Supplies the inherited measurement mechanism with the positivity margin provided by the new bases.

**Conceptual connection:** Each piece preserves the overlap data needed for normalization while creating the kernel needed for one message value.

**Source pointers:** Watrous [§1.1.2–§1.1.3][W1] and [§2.3.1][W2]; [quantum construction: a positive split of the Gram matrix](../science/quantum_construction.md#a-positive-split-of-the-gram-matrix), with its primary-source attribution.

### M23 — Complete the measurement and retain its kernels

**Phase:** Narrative/innovation.

**Central question:** Why does the input-dependent formula define a POVM on the whole receiver space?

**Understanding target:** Track the congruence transformation of each positive $`C_a`$ and the complement term $`(I-P)/3`$. Establish positivity, the identity sum and annihilation of every excluded vector in its own basis block.

**Dependencies and story role:** M03, M10, M21, M22. Converts the matrix decomposition into a complete physical measurement, including the unselected subspace.

**Conceptual connection:** Exact kernels and unconditional normalization must hold together; an exclusion condition alone does not specify a protocol.

**Source pointers:** Watrous [§2.3.1][W2] and [§1.1.2][W1]; [quantum construction: the input-dependent POVM](../science/quantum_construction.md#the-input-dependent-povm).

### M24 — Run the adaptive ternary protocol

**Phase:** Narrative/innovation.

**Central question:** How do the constructed kernels become zero-probability output events in two laboratories?

**Understanding target:** Follow Alice's transposed POVM, her ternary message and Bob's selected basis measurement. Derive the full unconditional law, its normalization and zero mass on every forbidden subset, while keeping all outcomes and using the same shared state and Bob bases for every input.

**Dependencies and story role:** M05, M06, M23. Assembles the local matrix identities into the complete target correlation.

**Conceptual connection:** The message chooses a quantum measurement on Bob's still-available share; remote conditioning is the operational link from the POVM proof to exclusion.

**Source pointers:** Watrous [§2.3.2, Eq. (2.226), and Exercise 2.2][W2], plus [§6.1.2][W6]; [quantum construction: protocol and exact output distribution](../science/quantum_construction.md#protocol-and-exact-output-distribution).

### M25 — Exact descriptions and the implementation boundary

**Phase:** Narrative/innovation.

**Central question:** What does the existential construction specify, and which implementation costs remain outside its theorem?

**Understanding target:** Explain how strict slack and continuity permit bases with rational real and imaginary parts, and how the Cayley representation supplies a dense exact-description family. Distinguish finite mathematical specifications from efficient search, certification, compilation or physical zero-error performance.

**Dependencies and story role:** M10, M20, M24. Closes the description issue before extracting a resource law from the ideal protocol.

**Conceptual connection:** Robustness of matrix inequalities establishes an exact existence statement without supplying a gate-efficient apparatus or removing experimental error.

**Source pointers:** Watrous [§1.1.2 and §1.2.1][W1]; [random bases: finite exact descriptions](../science/random_bases.md#finite-exact-descriptions) and [quantum construction: exact specification and physical scope](../science/quantum_construction.md#exact-specification-and-physical-scope).

### M26 — From binomial failure to an exponential obstruction

**Phase:** Narrative/innovation.

**Central question:** How does a constant forbidden fraction force an alphabet logarithmic in inverse error?

**Understanding target:** Apply the exact classical value to the constructed universe of $`3R`$ labels. For $`K\le m/2`$ and $`R\ge2048`$, explain the product bound $`\binom mK/\binom{3R}K\ge12288^{-K}`$ and the alternative that $`K>m/2`$ already has dimension-scale cost.

**Dependencies and story role:** M15, M16, M20, M24. Connects the quantum existence proof to the finite quantitative simulation lower bound.

**Conceptual connection:** The lower law arises from constant density, the classical guessing obstruction and an operational error witness, with their parameter conditions aligned.

**Source pointers:** Watrous [§1.2.2][W1]; [classical exclusion: the finite estimate used in the frontier](../science/classical_exclusion.md#the-finite-estimate-used-in-the-frontier).

### M27 — Match both ceilings in every regime

**Phase:** Narrative/innovation.

**Central question:** How do the bounds become one uniform dimension–precision theorem?

**Understanding target:** Combine the lower alternatives with the exact and approximate upper bounds. Explain the dimension-limited and precision-limited regimes, the treatment of positive integer alphabets and small dimensions, and the separate exact-error statement $`M_*(R,0)=\Theta(R)`$.

**Dependencies and story role:** M13, M14, M16, M25, M26. Integrates the proof components into the central theorem rather than inferring a matching law from unmatched limits.

**Conceptual connection:** Universal constants allow dimension and error to vary together; the same hard correlation family witnesses every tolerance.

**Source pointers:** Watrous [§1.1.3 and §1.2.1–§1.2.2][W1] as mathematical foundations; [frontier: main theorem, positive-error proof and zero-error proof](../science/frontier.md).

### M28 — Exact simulation with specified output noise

**Phase:** Narrative/innovation.

**Central question:** What changes if Bob's completed output is independently replaced by a uniform label?

**Understanding target:** Compute the forbidden mass $`tm/(3R)`$ of the noisy target and apply the same classical obstruction to an exact simulator. Connect the matching upper bound to the guessing construction, and distinguish this precise noise model from local entanglement noise or basis miscalibration.

**Dependencies and story role:** M08, M14, M16, M26, M27. Demonstrates an operational consequence of the same framework without changing the resource model.

**Conceptual connection:** A nonzero noise parameter can set the cost of exact correlation simulation while preserving the dimension cutoff.

**Source pointers:** Watrous [§2.2.1, replacement channels on p. 73][W2], and [§1.2.2][W1]; [interpretation: uniform output replacement](../science/interpretation.md#exact-simulation-after-uniform-output-replacement).

### M29 — Read the result in the correct resource units

**Phase:** Narrative/innovation.

**Central question:** What growing advantage does the theorem establish, and which stronger claims do its resource bounds not imply?

**Understanding target:** Convert alphabet bounds to fixed-length bit bounds. Explain why dimension alone cannot give unbounded advantage at fixed positive error; separate sufficient entanglement of the witness from a necessary entanglement-entropy claim, and identify the local processing and input descriptions left unoptimized.

**Dependencies and story role:** M02, M06, M12, M25, M27, M28. Reconciles the mathematical law with the complete operational accounting.

**Conceptual connection:** The frontier measures communication correlations; it is not a channel-capacity theorem, an efficient circuit result or a growing constant-error separation.

**Source pointers:** Watrous [§2.1.1–§2.1.3][W2] and [§6.3.1][W6]; [interpretation: bits and resource boundary](../science/interpretation.md#an-alphabet-size-is-different-from-a-number-of-bits).

### M30 — The complete causal and quantitative picture

**Phase:** Narrative/innovation.

**Central question:** How do local quantum geometry, classical information and global approximation jointly determine the strongest adaptive advantage?

**Understanding target:** Explain the whole chain: uniform random bases give positive Gram measurements; steering turns their kernels into exact exclusions; the established classical guessing bound witnesses simulation error; inherited universal simulators close the joint frontier. Identify the new constant-density realization, the inherited components, and the scope of both the zero-error and finite-error conclusions.

**Dependencies and story role:** M12, M17, M20, M24, M27, M28, M29. Synthesizes the narrative into the project's full contribution and its limitations.

**Conceptual connection:** One apparatus family and two resource ceilings explain both the ideal unbounded separation and the finite precision required to expose a large alphabet advantage.

**Source pointers:** Watrous [§1.2.1][W1], [§2.3.2][W2] and [§7.2.1][W7] for the connected foundations; [scientific account](../science/README.md), [frontier theorem](../science/frontier.md), [interpretation](../science/interpretation.md), [related work](../references/RELATED_WORK.md), and [Watrous bridge](WATROUS_BRIDGE.md).

[W1]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf
[W2]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf
[W6]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf
[W7]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf
