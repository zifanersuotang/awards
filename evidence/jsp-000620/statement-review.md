# JSP-000620 / Erdős 754: statement review

[Original problem](https://www.erdosproblems.com/754).

The ambient `E4` is real four-dimensional Euclidean space. A configuration is a Finset, hence has distinct points. `IsFavorite` explicitly requires x != y; each point x has its own strictly positive distance c(x). `Attainable n k` asks that every point have at least k other points at that point's chosen distance, and f(n) is the supremum of attainable k, with f(0)=0. The source proves this set nonempty and bounded before applying the supremum, so the conclusion does not exploit a default supremum of an invalid family. The audited theorem proves an absolute-constant upper bound f(n) <= n/2+C and its proof chooses C=202. No sharp constant, exact extremal configuration, or other-dimensional extension is claimed. Erdos755 is retained in the local proof closure.

The root review inspected the pinned original definitions and terminal declarations. Original mathematical/formal credits and all copyright/license notices remain byte-for-byte intact in every proof file. This documents existing public work and makes no claim of new proof authorship, recipient identity, or worldwide priority by the submitting account.

This statement review is not a claim of compilation success. Actual success, if present, is recorded only in verified-run/verification.json with the audited target names, individual axiom sets, and successful command logs. The checker must replay exactly the compiled local proof closure. It uses Lean's own kernel and trusts imported pinned Mathlib/package caches; it is not an independently implemented checker or a fresh whole-Mathlib replay.
