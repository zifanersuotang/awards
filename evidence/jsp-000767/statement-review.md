# JSP-000767 / Erdős 924: statement review

[Original problem](https://www.erdosproblems.com/924).

For every k>=2 and l>=3 the terminal theorem constructs a finite simple graph with no (l+1)-clique, and every edge labeling by Fin k has a monochromatic l-clique. The source's IsEdgeRamseyForClique quantifies over edge labelings, then chooses a color and a finite vertex set which is an l-clique in that color's label graph. It concerns edge colors, not vertex colors. CliqueFree(l+1) is a property of the host graph, not just of a selected color. The finite type witness and clique-freeness are actual conclusions of the final theorem, rather than an uninstantiated ExtensionRule hypothesis. This is the complete-graph instance needed for the problem; the packet does not claim the full arbitrary-target-graph strengthening of the Nesetril-Rodl theorem.

The root review inspected the pinned original definitions and terminal declarations. Original mathematical/formal credits and all copyright/license notices remain byte-for-byte intact in every proof file. This documents existing public work and makes no claim of new proof authorship, recipient identity, or worldwide priority by the submitting account.

This statement review is not a claim of compilation success. Actual success, if present, is recorded only in verified-run/verification.json with the audited target names, individual axiom sets, and successful command logs. The checker must replay exactly the compiled local proof closure. It uses Lean's own kernel and trusts imported pinned Mathlib/package caches; it is not an independently implemented checker or a fresh whole-Mathlib replay.
