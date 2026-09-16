# Exact registered mathematical scopes

These are source-scope reviews for the exact compiled and replayed targets in verification.json. They do not assert stronger variants, first authorship, official acceptance, or a prize award. The machine-readable metadata and checksummed logs contain all source and process evidence.

## JSP-000810 — Erdős 977

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos977.lean)

The target proves that the greatest prime factor of two to the n minus one, divided by n, tends to positive infinity along all natural exponents. The greatest-prime-factor definition uses the maximum of the number’s actual prime factors, with a harmless convention for the small values zero and one. The final theorem is unconditional: it applies a uniform Fermat-quotient estimate proved within the source with a specified numerical constant. It is therefore stronger in logical form than the nearby transfer lemmas that assume Stewart’s or Yamada’s estimates, and it establishes the complete limit rather than only a subsequence or limsup.

This covers the displayed Mersenne-number question. It does not settle the separate n!+1 question mentioned in the page commentary, and the selected target does not assert Stewart’s precise stronger quantitative bound.

Exact target conjunction: `Erdos977.erdos_977`.

All 1 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-000821 — Erdős 988

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos988.lean)

The target proves that the infimum of spherical-cap discrepancies over all sets of exactly n distinct points on the unit two-sphere tends to positive infinity as n grows. Discrepancy is the supremum of absolute differences between the cap point count and n times normalized cap area. The source constructs probability-normalized surface measure from ambient Euclidean volume and proves the required cap-area identity, rather than leaving this identification as a hypothesis. Its proof supplies the uniform inequality that the number of points is at most 512 times the fourth power of discrepancy, which yields the requested divergence.

The registered question concerns the two-sphere. Do not extend this target to Schmidt’s higher-dimensional generalization or claim an optimal discrepancy constant. The code uses supremum and infimum formulations; these directly establish the original uniform divergence question.

Exact target conjunction: `Erdos988.erdos_988`.

All 1 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-000825 — Erdős 992

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos992.lean)

There is one strictly increasing integer sequence and one constant c>0 such that, for Lebesgue-almost every α in [0,1], its interval discrepancy is at least c sqrt(N log N) for infinitely many N tending to infinity. The sequence is fixed before α is quantified; the theorem does not choose a different sequence for each α. This is the counterexample result attributed to Berkes and Philipp and refutes both proposed smaller almost-everywhere growth bounds. It does not assert the lower bound at every large N or for every α.

Existing attributed proof reproduction; no priority or award claim.

Exact target conjunction: `Erdos992.not_erdos_992`.

All 1 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-000838 — Erdős 1006

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1006.lean)

The target constructs a finite simple graph with no triangles or quadrilaterals that admits no acyclic orientation remaining acyclic after every single-edge reversal. The definitions require exactly one directed arc for each undirected edge and no additional arcs; reversal deletes that arc and inserts its opposite. Directed acyclicity forbids every positive-length directed closed walk. A proved finite construction supplies a graph in which every vertex ordering contains a monotone five-cycle, and the orientation argument converts this into the required counterexample. This answers the original universal question negatively, without assuming the ordered-cycle construction as an external mathematical hypothesis.

The source proves the girth-greater-than-four counterexample sufficient for the original question. It does not establish the stronger Nešetřil–Rödl theorem for every prescribed girth. Source-scope review is separate from actual compilation and kernel replay.

Exact target conjunction: `Erdos1006.not_erdos_1006`.

All 4 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-000845 — Erdős 1015

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1015.lean)

The selected targets resolve the intended question for sufficiently large host order, using vertex-disjoint monochromatic complete graphs in either color. For each t at least three, the exact optimum under the inclusive remaining-at-most convention is R minus one plus the residue of n minus (R minus one) modulo t, where R is the Ramsey number R(t,t-1). The optimal eventual bound independent of the host residue is R plus t minus two. Separate selected theorems prove that this optimal bound is not O(t) and that its t-th roots do not converge to one, addressing both asymptotic questions.

The webpage mixes an inclusive wording with a formula for the strict threshold. The source explicitly separates them: Erdos1015.erdos1015_strict_exact proves the printed R+residue formula for remaining<b. Full coverage here uses the webpage’s stated intended sufficiently-large-n interpretation, not an optimal bound for every small host order. All four selected targets must be checked if all four conclusions are registered.

Exact target conjunction: `Erdos1015.erdos_1015`, `Erdos1015.erdos1015_eventual_uniform`, `Erdos1015.uniformRemainder_not_isBigO_id`, `Erdos1015.uniformRoot_not_tendsto_one`.

All 3 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-000851 — Erdős 1021

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1021.lean)

For every fixed natural k at least three, the target proves a positive power saving below n to the three-halves power for the extremal number of the one-subdivision of the complete graph on k vertices. The graph is defined by the incidence relation between the original k vertices and their two-element subsets, matching the graph in the question. The final theorem supplies the positive saving itself, using Janzer’s value one divided by (four k minus six), and proves the required asymptotic upper bound for this actual graph. Both the exponent and implicit constant may depend on k.

Covers every fixed k at least three, not just the six-cycle case k=3. It does not claim the optimal saving, a matching lower bound, or an implicit constant uniform in k.

Exact target conjunction: `Erdos1021.erdos_1021`.

All 3 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-000857 — Erdős 1031

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1031.lean)

The target supplies absolute constants c > 0 and n0 such that every finite graph on n >= n0 vertices, whose largest clique or independent set has size strictly less than 10 log n, contains a large induced regular subgraph. Its vertex set S has at least c log n vertices, and its regular degree d satisfies 0 < d and d+1 < |S|. These inequalities ensure that the induced graph is neither empty nor complete. Both constants are selected before n and the graph, so the conclusion is uniform. The scope is the primary regular-subgraph assertion under the specified Ramsey-type hypothesis.

Keep sufficiently large n, the strict homogeneous-set bound with the fixed coefficient 10, and constants chosen before n and G. The registered terminal statement is the primary nontrivial regular induced-subgraph conclusion. Do not expand it into the general induced-universality refinement mentioned on the source page.

Exact target conjunction: `Erdos1031.erdos_1031`.

All 1 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-000868 — Erdős 1046

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1046.lean)

For every monic complex polynomial, if its open unit lemniscate is connected then that lemniscate is contained in an open disk of radius 2. The proof uses the centroid of its roots. This is Pommerenke’s affirmative radius-two result; the separate diameter/width questions mentioned in the problem discussion are outside the submitted target.

Existing attributed proof reproduction; no priority or award claim.

Exact target conjunction: `Erdos1046.erdos_1046`.

All 2 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-000870 — Erdős 1050

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1050.lean)

The target states that the real infinite series sum_{n>=1} 1/(2^n-3) is irrational. The definition indexes precisely the positive natural numbers, retaining the initial negative term and every subsequent term. Separate lemmas establish summability, identify this sum with the shifted natural-index series, and prove the exact relation to the generalized Lambert series used in the argument. The terminal irrationality theorem has no hypothesis assuming the irrationality of that auxiliary value: its proof supplies the needed result through integer linear forms. This is an attributed registration of the specific Erdős 1050 series, including its convergent infinite-sum interpretation.

This target concerns exactly the series indexed by positive natural numbers with denominator 2^n-3. Do not omit the n=1 term, substitute a finite sum, or advertise a general parameterized Lambert-series or transcendence theorem. The closure also contains ErdosProblems/Erdos250/Erdos250Core.lean, whose attribution and license must be retained.

Exact target conjunction: `Erdos1050.erdos_1050`.

All 2 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-000896 — Erdős 1078

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1078.lean)

The target proves Haxell's transversal-clique conclusion for every r >= 2 and n > 0. Vertices are represented by Fin r x Fin n, with adjacency forbidden within each first-coordinate part. Every vertex must satisfy the exact strict bound 2(r-1)((r-1)n-deg(v)) < rn. Under this condition, the graph contains a clique selecting one vertex from each of the r parts. Equivalently, the minimum degree exceeds (r-3/2-1/(2(r-1)))n; the displayed error tends to zero as r increases. This records an existing finite theorem with explicit parameters and covers the primary asymptotic question, without asserting the later sharp ceiling threshold.

Keep the strict integer degree inequality and r >= 2, n > 0. The error term 1/(2(r-1)) tends to zero with r, not with n at fixed r. Do not describe this target as the later Haxell–Szabó sharp ceiling threshold. The explicit Fin r x Fin n model represents equal-sized labelled parts.

Exact target conjunction: `Erdos1078.erdos_1078`.

All 1 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-000897 — Erdős 1079

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1079.lean)

For every r ≥ 4 and n ≥ 2, any n-vertex graph with at least ex(n,K_r) edges has a maximum-degree vertex of degree d ≥ n/2 whose open neighbourhood contains at least ex(d,K_(r−1)) edges. The tested target is the non-strict threshold result. Mathematical attribution: Bollobás and Thomason; the source also credits Bondy for the separate strict strengthening.

Existing attributed proof reproduction; no priority or award claim.

Exact target conjunction: `Erdos1079.erdos_problem_1079`.

All 1 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-000906 — Erdős 1089

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1089.lean)

For every fixed n ≥ 2, the genuine minimal forcing number g_d(n) for distinct distances in Euclidean d-space lies between binomial(d+1,n−1)+1 and binomial(d+n−1,n−1)+1. Its quotient by d^(n−1) tends to 1/(n−1)! as d tends to infinity. This is the fixed-n asymptotic question, not an exact formula for every d,n. The lower construction is attributed to Aletheia and the upper bound to Bannai, Bannai and Stanton.

Existing attributed proof reproduction; no priority or award claim.

Exact target conjunction: `Erdos1089.erdos_1089`.

All 1 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-000912 — Erdős 1099

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1099.lean)

For every real alpha > 1, the target provides a finite nonnegative constant C, depending on alpha, such that h_alpha(n) <= C for arbitrarily large natural numbers n and the liminf of h_alpha is at most C. Here h_alpha sums the alpha-th powers of consecutive relative gaps in the complete increasing list of positive divisors, using (d_{i+1}/d_i-1)^alpha. The proof supplies an explicit cofinal Vose sequence, rather than relying on finitely many examples or a merely assumed sequence. This is the primary bounded-liminf assertion; it does not identify the separate factorial or least-common-multiple sequences as successful witnesses.

The bound depends on alpha > 1 and holds for arbitrarily large n, not eventually for every n. The theorem establishes the main bounded-liminf question via its explicit Vose sequence. It does not resolve the page's separate questions for n!, lcm(1,...,n), or the alpha=1 logarithmic variant. The seven-file source closure and its notices must be preserved.

Exact target conjunction: `Erdos1099.erdos_1099`.

All 7 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-000925 — Erdős 1114

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1114.lean)

The target treats every nonzero real polynomial of degree N+1, with N > 0, whose N+1 roots are the arithmetic progression a+d*j for 0 <= j <= N and d > 0. For any derivative roots b_k specified inside the consecutive open root intervals, it proves that consecutive derivative gaps are nondecreasing from the midpoint toward the right endpoint, together with reflection symmetry giving the corresponding left-hand conclusion. The statement uses the actual roots-and-degree hypotheses, deriving the needed scalar factorization internally. Thus the registered result covers arbitrary translation, positive spacing, and nonzero leading coefficient, with the corrected nonvacuous root indexing.

Use the corrected nonvacuous indexing: degree N+1, roots j=0,...,N, and N derivative roots. The page's degree/root indexing is inconsistent as written. The target assumes the derivative-root selector lies in the appropriate open intervals and satisfies derivative zero; it does not separately construct that selector. The gap inequalities are non-strict. This registration is for the corrected intended statement, not the literally inconsistent wording.

Exact target conjunction: `Erdos1114.erdos_1114`.

All 1 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-000935 — Erdős 1127

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1127.lean)

The target proves an equivalence between the continuum hypothesis and the following all-dimensional statement: for every natural number n, Euclidean n-space admits a coloring by natural numbers such that each color class has distinct distances between different unordered pairs of distinct points. Equality of two distances within a color class forces equality of the endpoint pairs up to reversal. Both the CH-to-coloring construction and the reverse implication are terminal proved directions; the real-line equivalence is also provided separately. The use of EuclideanSpace fixes the Euclidean metric. This records the exact conditional-equivalence resolution, without asserting an unconditional coloring or a formal metatheoretic consistency proof.

The positive answer is equivalent to CH; it is not asserted unconditionally. Distances refer to different unordered nondegenerate pairs, so reversal is identified and diagonal pairs are excluded. Use EuclideanSpace, not the sup metric on coordinate functions. Both directions are proved, but this is not a formal metatheoretic consistency/independence proof for ZFC.

Exact target conjunction: `Erdos1127.erdos_1127`, `Erdos1127.erdos_1127_real_line`.

All 1 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-000984 — Erdős 1179

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1179.lean)

For every fixed epsilon strictly between zero and one, the theorem gives an explicit subset size asymptotic to log base two of the group order and proves that a uniformly chosen subset of this size is balanced with probability tending to one along every growing sequence of finite abelian groups. Balancedness simultaneously bounds every subset-sum representation count by the required relative error. A separate universal lower bound proves that any balanced subset has at least logarithmic size. The sample space consists of genuine finite subsets, with distinct elements; the proof explicitly transfers from independent tuples and handles eventual nonemptiness.

Covers the original leading asymptotic question. It does not define or compute an exact finite-order minimum g_epsilon(N), or claim the best lower-order error. No unresolved definition bridge was found at the inspected endpoints.

Exact target conjunction: `Erdos1179.erdos_1179`.

All 3 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-000985 — Erdős 1180

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1180.lean)

For every ε>0 there is a constant C depending only on ε such that, for every prime p, every residue modulo p is a sum of at most C inverses of admissible positive integers n≤p^ε. The source excludes denominators divisible by p and handles small primes too. This registers the uniform existence assertion, without claiming the optimal dependence of C on ε. The historical affirmative result is attributed to Shparlinski, with the later Glibichuk method used in the source.

Existing attributed proof reproduction; no priority or award claim.

Exact target conjunction: `Erdos1180.erdos_1180`.

All 1 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-000990 — Erdős 1185

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1185.lean)

The uniform arithmetic-progression assertion is false already at density δ=1/200 and length k=3: for every proposed lower bound m on the size of B and every threshold N₀, the source constructs N≥N₀ and subsets A,B of {1,…,N}, with |A|≥δN and |B|≥m, having no nontrivial three-term progression in A whose step belongs to B−B. The historical negative result is attributed to Furstenberg.

Existing attributed proof reproduction; no priority or award claim.

Exact target conjunction: `Erdos1185.not_erdos_1185`.

All 1 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-001000 — Erdős 1195

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1195.lean)

For every nonnegative nondecreasing real function F on [1,∞) tending to infinity, there is a measurable set S of infinite measure with no integer ratio between distinct members and |S∩(0,x)|≥F(x) for all sufficiently large x if and only if the integral of F(x)/x² on [1,∞) is finite. The growth bound is eventual, not asserted for all x≥1. This is the sharp criterion attributed in the linked discussion to Ho Boon Suan and GPT, building on Haight and Szemerédi.

Existing attributed proof reproduction; no priority or award claim.

Exact target conjunction: `Erdos1195.erdos_1195`.

All 1 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-001003 — Erdős 1198

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1198.lean)

There exists a two-coloring of the positive integers with no infinite strictly increasing positive sequence for which every nontrivial sum of products over disjoint nonempty finite index blocks has one common color. Only a single one-element block is excluded as trivial. The source proves the negative answer attributed to Smith; this is the full sum/product assertion, not just the finite-sums special case.

Existing attributed proof reproduction; no priority or award claim.

Exact target conjunction: `Erdos1198.not_erdos_1198`.

All 1 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-001010 — Erdős 1205

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1205.lean)

Choose one residue class modulo each positive n≤x and maximize the number of these classes that cover every integer in {1,…,x}. The source defines this genuine optimal common coverage and proves it is asymptotic to log x. The submitted theorem asserts the leading asymptotic, without claiming the sharper secondary error term mentioned in the problem discussion. Provenance remains with the linked Erdős problem discussion and source header.

Existing attributed proof reproduction; no priority or award claim.

Exact target conjunction: `Erdos1205.erdos_1205`.

All 1 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-001018 — Erdős 1213

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1213.lean)

For all positive integers a and K there is a bound f(a,K) such that every finite strictly increasing integer sequence starting at a, with successive gaps at most K and last term greater than that bound, has two distinct nonempty index intervals with equal sums. This is Hegyvári’s affirmative bounded-gap result. The registered terminal statement is existence of the bound; no optimal dependence on K is claimed.

Existing attributed proof reproduction; no priority or award claim.

Exact target conjunction: `Erdos1213.erdos_1213`.

All 1 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.

## JSP-001020 — Erdős 1215

[Pinned main source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1215.lean)

There is no uniform real bound on the length of an escape path for all positive-degree complex polynomials P with P(0)=1 and every root on the unit circle. Paths are continuous, start at 0, end on the unit circle, and satisfy |P(γ(t))|<1 at every noninitial point; length is total variation. Exempting the initial point is essential because |P(0)|=1. The source constructs polynomial labyrinth barriers, following the negative result attributed to Mac Lane.

Existing attributed proof reproduction; no priority or award claim.

Exact target conjunction: `Erdos1215.not_erdos_1215`.

All 6 local source modules compiled and replayed; the independent importing-file axiom report covers every listed target. This uses the same Lean kernel and is not an independent verifier implementation.
