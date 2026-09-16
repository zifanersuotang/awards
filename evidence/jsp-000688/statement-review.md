# JSP-000688 / Erdős 832: statement review

The [original question](https://www.erdosproblems.com/832) universally quantifies over r ≥ 3, permits the lower threshold K to depend on r, and asks for the binomial edge lower bound in every r-uniform hypergraph of exact chromatic number k ≥ K, together with a complete-hypergraph equality clause.

The selected terminal statement negates exactly that universal eventual assertion. Its `FiniteHypergraph` retains the ambient vertex set (including isolated vertices), uses sets of vertices as edges, and defines proper coloring by non-monochromaticity of each edge. `HasChromaticNumber` supplies both a k-coloring and the nonexistence of colorings with fewer colors; it is not merely a lower bound on chromatic number.

The proof fixes r = 4 and, for every proposed K, constructs a sufficiently large k = 2^(K+9). A spanning edge subhypergraph realizes exact chromatic number k while its edge count stays strictly below the proposed binomial lower bound. Therefore the disproof does not rely on an isolated-vertex ambiguity in the equality clause. The strict edge-count failure alone refutes the conjunction.

This covers the original universal question. It does not settle the r = 3 specialization, construct counterexamples for every r ≥ 4, or prove the full general extremal formula or its later asymptotics. The original page explicitly records r = 3 as open. The header credits Noga Alon for the mathematical disproof and Codex/GPT-5.6 Sol for the selected formal proof; the retained copyright block also acknowledges Aristotle/OpenAI Codex.

Compilation and checker success are asserted only by the actual `verified-run/verification.json` and associated logs, when present. This statement review by itself is not a kernel verification.
