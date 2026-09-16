# Statement review — JSP-000663 / Erdős 806

The catalog and original question ask whether every `A ⊆ {1,…,n}` of size at most `sqrt n` has a sumset basis `B ⊆ ℤ` of size `o(sqrt n)`. The source formalizes the uniform little-o assertion: for every real `ε>0`, all sufficiently large `n` work for **every** such `A`, with a suitable finite integer `B` satisfying `A⊆B+B` and `|B|≤ε sqrt n`. The threshold depends only on `ε`, not on `A`. Thus the statement is not weakened by exchanging uniformity quantifiers.

Natural elements of `A` are mapped injectively to integers by `Nat.castEmbedding`; `B+B` is the ordinary pointwise sumset, allowing two equal summands. `B` need not consist of positive integers, matching the original `B⊆ℤ`. The source's terminal theorem exposes all these conditions directly.

The explicit finite theorem proves the bound

`|B| ≤ k*q^(k−1) + 2*(|A|/k + (n/q^k + 1))`

for positive `k` and `q>1`. The basis is built by partitioning quotient fibers into bounded-size chunks, then correcting base-q digits so each chunk meets a common universal residue family. The later choice of parameters turns the coarse bound into uniform little-o. All construction and bound lemmas are in the same source; only Mathlib/Lean modules are imported.

The original mathematical result by Noga Alon, Boris Bukh and Benny Sudakov (2009), *Discrete Kakeya-type problems and small bases*, proves the sharper rate `O(sqrt n * log log n/log n)`. The Lean theorem covers the full yes/no little-o question, but that sharper rate is **not claimed**.

The unchanged source retains its mathematical-author header, formal authors Codex and GPT-5.6 Sol, and Apache 2.0 notice. Our contribution is local verification and registration evidence, not new formalization authorship.
