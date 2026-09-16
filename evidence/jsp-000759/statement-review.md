# JSP-000759 / Erdős 915: exact interpretation and disproof scope

The [catalog entry](https://github.com/TheJustinSunPrize/awards/blob/f4e7173d89dfe91022a185427d63452c8ffbf6ae/problems/catalog-0701-0800.md#JSP-000759)
explicitly asks about **internally disjoint** paths. The [original problem
page](https://www.erdosproblems.com/915) explains the historical ambiguity
between internal-vertex and edge disjointness, and identifies its main
conjecture using the vertex-disjoint threshold k_m. Thus this package's
negative interpretation matches the catalog wording; it is not a negative
claim about the different, positive edge-disjoint theorem.

The unchanged source defines the internal vertices of a simple graph path
by removing its two endpoints from its support. Its path-family condition
requires distinct endpoints, an injective family of paths, and pairwise
disjoint internal-vertex sets. The usual direct edge is handled as a path
with empty internal set; injectivity prevents counting the same path many
times. This is the requested internally vertex-disjoint interpretation.

`Erdos915.not_erdos_915` refutes the universal claim with m≥2,n≥1. It uses
an explicit simple graph on Fin 17 with 41 unordered edges and proves that
no pair admits five internally vertex-disjoint paths. Substituting m=5,n=4
gives exactly 17=1+4(5−1) vertices and 41=1+4*choose(5,2) edges, contradicting
the proposed assertion. The source proves the edge count and excludes all
endpoint pairs, using explicit small separators for the high-degree
vertices and the degree bound for the remaining vertices.

One counterexample completely refutes that universally quantified
conjecture. The theorem does not give every extremal threshold k_m(n),
derive the sharp k_5(n) formula, or formalize the positive edge-disjoint
variant. Those are separate statements, not consequences of this replay.

The preserved source header credits the mathematical work to Bo Sørensen
and Carsten Thomassen, and the formalization to Codex and GPT-5.6 Sol.
This packet adds source review and observed local verification only.

The current page, its LaTeX and the full discussion were captured on
2026-09-16 in the assignment's source audit. This interpretation relies
on their explicit definitions and the catalog's wording, rather than
inferring completeness from a Solved flag or a theorem name.
