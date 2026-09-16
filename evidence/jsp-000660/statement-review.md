# JSP-000660 / Erdős 803: statement review

The [original question](https://www.erdosproblems.com/803) asks for absolute positive lower-density and balance constants, then for every target size m a sufficiently large host size n, such that every n-vertex graph with at least n log n edges contains an m-vertex balanced subgraph with at least a constant times m log m edges.

`Erdos803.not_erdos_803` negates this exact order of quantifiers. Both ε and D precede m, the eventual threshold in n may depend on m, and the host graph is universally quantified after that threshold. The selected source imports `ErdosProblems.Erdos1077` for the shared balanced-graph setup; its local proof closure therefore consists of both 803 and 1077, not only the terminal file.

For every proposed ε>0 it chooses m with ε log m>6 and constructs arbitrarily large host graphs with at least n log n edges for which every m-vertex subgraph has fewer than 6m edges. This stronger obstruction makes the D-balanced condition irrelevant to the contradiction; it is not achieved by weakening the requested subgraph to an induced graph or by allowing constants to depend on m. Edge counts are the actual unordered edges of Mathlib simple graphs.

The packet covers the negative answer to the stated universal assertion. It does not claim Alon's full uniform balanced-subgraph upper estimate or the later Janzer–Sudakov positive theorem. The unchanged main-file header credits Noga Alon mathematically and Codex/GPT-5.6 Sol formally. The imported file retains its own author/copyright notices. The submitting account claims no original authorship.

This review alone is not a successful run. `verified-run/verification.json` must establish compilation of both local modules, the terminal target/axiom audit, and actual checker replay of both modules with the verbose names compared against the source manifest. Imported pinned Mathlib caches remain trusted and the checker uses the same Lean kernel; no independent checker implementation is asserted.
