# JSP-000465 / Erdős 575

There exists a nonempty finite family F of connected bipartite finite graphs, each containing a cycle, and c>0 such that ex(n,G)>=c*n^(4/3) eventually for every G in F, while ex(n,F)=O(n^(4/3-1/48)); no member G has ex(n,G)=O(ex(n,F)). This gives a negative answer to JSP-000465 / Erdos 575, whose hypothesis asks only that F contain a bipartite member. The subgraphs are ordinary copies, not induced copies. The lower-bound threshold may depend on G as printed; finiteness permits a common threshold. No new or first formalization is claimed.

Existing Apache-2.0 plby/lean-proofs port. The headers credit Astra (an internal OpenAI model) for the informal proof and Astra / OpenAI team for formalization, and explicitly say the source was modified and ported from Lean/Mathlib 4.32.0 to 4.33.0. All selected plby source bytes and notices are preserved; this work only supplies verification evidence.

Main declaration: `Erdos180.compactnessCounterexample_bigO`. Actual target module: `ErdosProblems.Erdos180`.

All 8 custom sources compiled unchanged; the importing audit and checker exited 0. The checker actually replayed 8 modules.

See [evidence.json](evidence.json) for immutable upstream URLs, every source SHA-256, build order, exact axiom sets, checker selection and links/digests for all logs.

No upstream proof source is copied into this attachment. Reproduction uses [verify.py](../../verify.py) with this evidence.json and a dedicated pinned Mathlib checkout.
