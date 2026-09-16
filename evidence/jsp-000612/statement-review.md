# Erdős 744: selected statement review

[Original question](https://www.erdosproblems.com/744).

For k-critical graphs on exactly n vertices, f(k,n) is the minimum number of actual edges whose deletion makes the graph bipartite. Criticality quantifies over all proper subgraphs, so both vertex and edge deletions are included. The source proves, for every k≥4 and all sufficiently large n, f(k,n)=choose(k−1,2), constructing critical graphs throughout that range so that a natural infimum over an empty class cannot drive the answer. The audited target is the eventual formulation, not a claim about every small n.

The root review checks these definitions and terminal quantifiers against the prior source audit and pinned proof. All original proof bytes, author headers and license notices are preserved. This is existing-proof verification, not a claim of a new mathematical result or new proof authorship.

Successful compilation and target-module replay must be established by the actual `verified-run/verification.json` and logs; this preparatory review alone is not a kernel check. The checker uses the same Lean kernel and trusts pinned imported Mathlib caches.
