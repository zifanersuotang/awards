# JSP-000657 / Erdős 800: statement review

[Original problem](https://www.erdosproblems.com/800).

The original question requires an absolute linear diagonal Ramsey bound for graphs with no adjacent pair of vertices both of degree at least three. NoAdjacentHighDegree has precisely that restriction. RamseyFor H N asserts a non-induced copy of H in an arbitrary graph on Fin N or its complement, encoding the two colors of a complete graph. The explicit theorem supplies N=12n for every n (including the empty case); the audited terminal erdos_800_linear packages the absolute constant existentially. No degree bound on individual nonadjacent high-degree vertices, optimal constant, or induced Ramsey variant is asserted.

The pinned original source and its full credit/copyright blocks remain byte-for-byte intact. This is a review of an existing public proof, not an assertion of new mathematical or formal proof authorship.

This statement review does not assert compilation success. Only the actual `verified-run/verification.json`, its terminal theorem/axiom output, and command logs establish observed compilation and target-module replay. Imported Mathlib caches are trusted and the checker uses Lean's own kernel, not an independent implementation.
