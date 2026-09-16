# JSP-000751 / Erdős 903: statement review

[Original problem](https://www.erdosproblems.com/903).

The original statement has n=p²+p+1 with p a prime power and asks that a pairwise-balanced block design with more than n blocks has at least n+p blocks. The terminal theorem has precisely these quantifiers. PairwiseBalanced requires each pair of distinct points to occur in exactly one block and every block to have size at least two. The latter is the standard nondegenerate linear-space convention: if singleton or empty blocks could be arbitrarily appended, the displayed question would be false. This convention must remain visible. The source proves an internal result for integer p as well; the audited target retains the original prime-power hypothesis. It does not prove the later stronger gap for designs not obtained by breaking up a projective-plane line.

The pinned original source and its full credit/copyright blocks remain byte-for-byte intact. This is a review of an existing public proof, not an assertion of new mathematical or formal proof authorship.

This statement review does not assert compilation success. Only the actual `verified-run/verification.json`, its terminal theorem/axiom output, and command logs establish observed compilation and target-module replay. Imported Mathlib caches are trusted and the checker uses Lean's own kernel, not an independent implementation.
