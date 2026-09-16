# JSP-000437 / Erdős 546

For every finite simple graph G with no isolated vertices and m edges, the ordinary diagonal two-color graph Ramsey number is at most 2^(C*sqrt(m)) for one universal positive real C; the proof supplies C=65536. The discrete bound is 2^(32768*(floor(sqrt(m))+1)). Containment is ordinary and injective, not induced. The zero-edge case is included, and no claim is made for three or more colors or an optimal constant.

Existing plby/lean-proofs source. Primary headers credit Benny Sudakov for the mathematical result and Codex / GPT-5.6 Sol, also described as OpenAI Codex, for formalization. All 16 source headers and notices remain unchanged. No uploader-as-original-author, new-proof, priority or recipient claim.

Main declaration: `Erdos546.erdos_546`. Actual target module: `ErdosProblems.Erdos546`.

All 16 custom sources compiled unchanged; the importing audit and checker exited 0. The checker actually replayed 15 modules.

See [evidence.json](evidence.json) for immutable upstream URLs, every source SHA-256, build order, exact axiom sets, checker selection and links/digests for all logs.

No upstream proof source is copied into this attachment. Reproduction uses [verify.py](../../verify.py) with this evidence.json and a dedicated pinned Mathlib checkout.
