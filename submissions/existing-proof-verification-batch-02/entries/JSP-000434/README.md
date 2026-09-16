# JSP-000434 / Erdős 543

Let f(N) be the least k such that, for every finite abelian group G of order N, at least half of its k-element subsets A represent every element of G as a sum of a subset of A. There is no real function g with g(N)/log(log N) tending to zero for which f(N) <= log(N)/log(2)+g(N) eventually. For every such g, all sufficiently large primes p give failure of half-completeness in ZMod p at the natural ceiling of that cutoff. The random model is uniform subsets; independent tuples and their collisions are intermediate tools. No exact asymptotic formula for f(N) or failure for every group is asserted.

The unchanged source header credits Q. Tang and ChatGPT for the informal proof, and Codex / GPT-5.6 Sol for the formalization. It separately retains the modified-file Apache 2.0 notice naming Boris Alexeev and ChatGPT. These distinct credit layers are preserved; the present reviewer/uploader claims no original proof or formalization authorship.

Main declaration: `Erdos543.erdos_543`. Actual target module: `ErdosProblems.Erdos543`.

All 26 custom sources compiled unchanged; the importing audit and checker exited 0. The checker actually replayed 26 modules.

See [evidence.json](evidence.json) for immutable upstream URLs, every source SHA-256, build order, exact axiom sets, checker selection and links/digests for all logs.

No upstream proof source is copied into this attachment. Reproduction uses [verify.py](../../verify.py) with this evidence.json and a dedicated pinned Mathlib checkout.

## Mathematical scope and source history

The main declaration is an alias of the negative theorem not_erdos_543: the proposed little-o(log log N) improvement fails. The finite model is uniform k-element subsets, with an explicit collision-controlled transfer from independent tuples.

[Jie Ma and Quanyu Tang's paper](https://arxiv.org/abs/2602.05768v2) also establishes a quantitative prime-order bound with coefficient 1/(2 log 2). This verification packet records the qualitative disproof and the selected prime-cyclic obstruction; it does not assert that the stronger coefficient bound was formalized here.
