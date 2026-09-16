# JSP-000605 / Erdős 737: statement review

[Original problem](https://www.erdosproblems.com/737).

The source defines uncountable chromaticity as the absence of a coloring by natural numbers (Erdos594.IsUncountablyChromatic). The global terminal theorem `erdos_737` additionally asks for a coloring by the first uncountable ordinal, thus describing exact aleph-one chromatic number. Its separately audited helper `Erdos737.eventually_cycles_through_fixed_edge` assumes only the absence of a countable coloring. This helper supplies the full advertised scope: one fixed adjacent pair, one threshold N, and, for every n >= N, a simple cycle of length exactly n containing that same edge. The quantifier order does not allow the edge to vary with n. The audit includes both declarations; the main declaration is global, not Erdos737.erdos_737. The packet includes the original Erdos594 dependency rather than assuming this helper as an axiom.

The root review inspected the pinned original definitions and terminal declarations. Original mathematical/formal credits and all copyright/license notices remain byte-for-byte intact in every proof file. This documents existing public work and makes no claim of new proof authorship, recipient identity, or worldwide priority by the submitting account.

This statement review is not a claim of compilation success. Actual success, if present, is recorded only in verified-run/verification.json with the audited target names, individual axiom sets, and successful command logs. The checker must replay exactly the compiled local proof closure. It uses Lean's own kernel and trusts imported pinned Mathlib/package caches; it is not an independently implemented checker or a fresh whole-Mathlib replay.
