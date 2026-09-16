# JSP-000415 / Erdős 518

For every natural n and every red-blue edge-coloring of the complete graph on n vertices, all vertices are covered by at most floor(sqrt(n)) simple paths, all in one common color. Paths are nonempty, have no repeated vertices and have adjacent consecutive vertices; singleton paths are allowed. Different covering paths may overlap. The empty graph case is included. No disjoint-cover, exactly-sqrt(n), multi-color or sharpness-witness claim is made.

Existing plby/lean-proofs source. The unchanged entry header credits Alexey Pokrovskiy, Leo Versteegen and Ella Williams for mathematics and Codex / GPT-5.6 Sol for formalization. Supporting NoConfiguration documentation identifies the Chen--Chen argument; all original headers and notices are preserved. The all-n theorem is distinguished from the earlier sufficiently-large-n result in the primary-source history below. No uploader-as-original-author, new-proof, priority or recipient claim.

Main declaration: `Erdos518.erdos_518`. Actual target module: `ErdosProblems.Erdos518`.

All 36 custom sources compiled unchanged; the importing audit and checker exited 0. The checker actually replayed 36 modules.

See [evidence.json](evidence.json) for immutable upstream URLs, every source SHA-256, build order, exact axiom sets, checker selection and links/digests for all logs.

No upstream proof source is copied into this attachment. Reproduction uses [verify.py](../../verify.py) with this evidence.json and a dedicated pinned Mathlib checkout.

## Source history

The earlier [Pokrovskiy--Versteegen--Williams paper, v2](https://arxiv.org/abs/2409.03623v2) states the result for all sufficiently large n. [Hangdi Chen and Yaojun Chen, v1](https://arxiv.org/html/2607.21915v1) give the all-positive-n result in Theorem 1.5, explicitly allowing overlapping and singleton paths. The pinned Lean source uses an all-n minimal-counterexample argument and names Chen--Chen in its NoConfiguration documentation. This attribution distinction supplements, without rewriting, the existing source header; the uploader claims neither result as new.
