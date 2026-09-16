# JSP-000769 / Erdős 926: statement review

The [original problem](https://www.erdosproblems.com/926) asks, for every fixed k ≥ 4, whether ex(n; H_k) is O_k(n^(3/2)). Its H_k has one center x, k vertices y_i adjacent to x, and one distinct vertex for each unordered pair of y vertices, adjacent to both members of that pair.

The exact source uses `Unit ⊕ (Fin k ⊕ PairIndex k)`, where PairIndex contains ordered representatives i < j of unordered pairs. `HAdj` has exactly the center–branch and pair–branch edges. `SimpleGraph.extremalNumber` and graph freeness use Mathlib's ordinary non-induced extremal graph convention.

The terminal theorem `Erdos926.erdos_926` quantifies over every k ≥ 4, with n tending to infinity. The real exponent is 3/2, and the Big-O bound may depend on k. The proof obtains an explicit finite-graph bound, transfers it to the extremal number, and then supplies the claimed Big-O theorem. This closes the stated question. The mathematically credited author in the unchanged header is Zoltán Füredi; its formal authors are Codex and GPT-5.6 Sol.

The original page also describes later stronger dependence on k. This packet does not assert that it formalizes the optimal constant, all later improvements, or the matching lower bound. Its advertised scope is precisely the fixed-k upper estimate.

The observed source compilation, final theorem/axiom harness, and target-module checker all exited 0. `verified-run/verification.json` records the actual run. The terminal axiom list is exactly propext, Classical.choice, Quot.sound. Imported Mathlib caches were trusted; the checker is the same Lean kernel and is not an independent implementation or a full dependency replay.
