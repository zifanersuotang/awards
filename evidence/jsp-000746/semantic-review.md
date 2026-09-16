# JSP-000746 / Erdős 895 replay review

The original question asks whether every triangle-free graph on labels `{1,...,n}` has three independent points `a,b,a+b`, for all sufficiently large `n`. The pinned theorem `Erdos895.erdos_895` establishes exactly this with witness `N = 18`.

## Attribution and immutable inputs

This is a replay and review of existing work, not a new mathematical proof or a new formalization. The complete source header is preserved byte for byte. It attributes the informal argument to **Ben Barber** and formalization to **Codex** and **GPT-5.6 Sol**.

- Original problem: <https://www.erdosproblems.com/895>
- Discussion: <https://www.erdosproblems.com/forum/thread/895>
- Source: <https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos895.lean>
- CNF: <https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos895/Certificate.cnf>
- LRAT: <https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos895/Certificate.lrat>

The three input SHA-256 hashes are pinned in `replay.py` and checked before compilation. `prepare.py` extracts the exact Git blobs, avoiding Windows checkout newline conversion; `source-byte-comparison.json` records the match. The upstream repository's existing license notice is retained as `LICENSE.upstream`, without interpreting that notice as assigning a license to any additional material. Lean is 4.33.0; Mathlib is pinned at `db584cd6d46c92f209a44c0f1c829460d327499d` and read only.

## Statement and proof scope

`Fin n` vertex `i` represents mathematical label `i.val + 1`. Consequently the third vertex has Fin value `a.val + b.val + 1`, exactly mathematical label `(a.val + 1) + (b.val + 1)`. The predicate includes the third vertex's bound and all three absent edges. The order `a.val < b.val` makes the two summands distinct; positivity makes the third label strictly larger than both. Thus it supplies three distinct independent vertices.

`CliqueFree 3` is the standard triangle-free condition for a simple graph. The finite core specializes the certified propositional theorem to all 153 unordered edge variables of 18 vertices. The 816 negative clauses prohibit triangles. The 72 positive clauses require an edge in each distinct-summand triple `a,b,a+b`; together their unsatisfiability gives the finite result. `check_encoding.py` independently enumerates the graph clauses and compares them, in order and without omission, with the input CNF.

`finite_eighteen` converts this propositional contradiction into a graph theorem. `explicit_bound` restricts an arbitrary graph to its first 18 labels using `Fin.castLEEmb`; the map preserves the numerical labels and adjacency. It then transports the three witnesses back. The final theorem quantifies over every `n >= 18` and every triangle-free simple graph on `Fin n`; it is not merely a finite test.

The formal theorem proves **sufficiency** of threshold 18. The source's prose uses the word “sharp”, but this module does not provide a counterexample at 17, and this review makes no sharpness claim. The stronger independent Hindman-set question mentioned on the source page is separate and remains outside this theorem's scope.

## Verification boundaries

`verification.json` is authoritative for command completion and exit codes. `Audit895.lean` prints statement types and the axioms of the certificate, finite core, extension, and final result. No conclusion of successful replay should be inferred from source scanning alone.

The Lean 4.33.0 CLI source `src/lean/LeanChecker.lean` was read before choosing `leanchecker --verbose Erdos895`. It matches target module prefixes and replays the target's declarations into the imported environment. In this isolated directory the prefix matches the single compiled `Erdos895` module. Neither `--fresh`, no-target invocation, nor unrecognized `--help` is used.

This bundled checker uses the same Lean kernel. It checks the emitted declarations against the already imported, pinned Mathlib environment; it is not an independently implemented checker or a fresh replay of all dependencies. Heavy commands are serialized with the shared `run_lean_serial.py` coordinator, wrapping the complete pipeline once.
