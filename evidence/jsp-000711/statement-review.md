# JSP-000711 / Erdős 858: statement review

[Original problem](https://www.erdosproblems.com/858).

Admissibility excludes a proper multiplicative pair b=a*t with t>1 and every prime divisor of t greater than a. The strict t>1 condition avoids accidentally treating a point paired with itself as forbidden. All sets lie in the positive interval [1,N]. `extremalMass` is the actual maximum of the finite nonempty family of reciprocal sums, and the source proves an extremizer exists. The audited conclusion is extremalMass(N)/log(N) -> constant. The constant is explicitly defined using the profile log((1-u)/u) plus its two-prime integral, the threshold alphaTwo given by the profile condition on [1/4,1/3], and the integral of 1-profile from alphaTwo to 1/2 added to 1/2. No decimal value, exact finite-N maximizing family, or sharper error term is inferred from this limit. The imported UnitFractions modules are included in the local closure and are not hidden proof assumptions.

The root review inspected the pinned original definitions and terminal declarations. Original mathematical/formal credits and all copyright/license notices remain byte-for-byte intact in every proof file. This documents existing public work and makes no claim of new proof authorship, recipient identity, or worldwide priority by the submitting account.

This statement review is not a claim of compilation success. Actual success, if present, is recorded only in verified-run/verification.json with the audited target names, individual axiom sets, and successful command logs. The checker must replay exactly the compiled local proof closure. It uses Lean's own kernel and trusts imported pinned Mathlib/package caches; it is not an independently implemented checker or a fresh whole-Mathlib replay.
