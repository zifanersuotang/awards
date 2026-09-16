# JSP-000460 / Erdős 570

For every cycle length k>=3, there is an edge threshold M(k) such that every finite simple graph H with no isolated vertices and at least M(k) edges satisfies R(C_k,H)<=2|E(H)|+floor((k-1)/2). The threshold is uniform over H for fixed k; the theorem includes triangle, quadrilateral, larger even and larger odd cycles. R is the usual two-colour, ordinary non-induced graph Ramsey number. No bound for every small edge count, optimal explicit threshold, induced-copy variant, or exact Ramsey-number formula is claimed.

Existing formalization by Codex / GPT-5.6 Sol. The 2026 general-cycle theorem is by Stijn Cambie, Andrea Freschi, Patryk Morawski, Kalina Petrova and Alexey Pokrovskiy ([primary paper](https://arxiv.org/abs/2601.10238v1)). The fixed source also retains earlier credits to Paul Erdos, Ralph Faudree, Cecil Rousseau, Richard Schelp, Wayne Goddard, Daniel Kleitman, Alexander Sidorenko and C. J. Jayawardene. Original source bytes and attribution notices are preserved; the two inaccurate given names in its header are clarified below. No new-proof or first-formalization claim.

The 2026 general-cycle result is by Stijn Cambie, Andrea Freschi, Patryk Morawski, Kalina Petrova and Alexey Pokrovskiy ([primary paper](https://arxiv.org/abs/2601.10238v1)). The immutable source header spells two given names as Alberto and Piotr and abbreviates Kalina; these header bytes are preserved for source fidelity, but mathematical attribution here follows the primary paper. Earlier special-case credits and the source's Codex / GPT-5.6 Sol formalization credit are retained.

Main declaration: `Erdos570.erdos_570`. Actual target module: `ErdosProblems.Erdos570`.

All 75 custom sources compiled unchanged; the importing audit and checker exited 0. The checker actually replayed 73 modules.

See [evidence.json](evidence.json) for immutable upstream URLs, every source SHA-256, build order, exact axiom sets, checker selection and links/digests for all logs.

No upstream proof source is copied into this attachment. Reproduction uses [verify.py](../../verify.py) with this evidence.json and a dedicated pinned Mathlib checkout.
