# JSP-000745 / Erdős 894

This packet replays an existing formalization, without claiming new proof authorship. The original source header is preserved byte for byte from plby commit `8822f7ddef30fadbd92e1c6ab4ed897af356af5e`. It credits the informal argument to **Yuval Peres and Wilhelm Schlag** and the formalization to **Codex and GPT-5.6 Sol**.

- Problem: <https://www.erdosproblems.com/894>
- Existing source: <https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos894.lean>
- Discussion: <https://www.erdosproblems.com/forum/thread/894>

## Main statement and coverage

`Erdos894.IsLacunary n` requires a positive sequence `n : ℕ → ℕ` and a real `ε > 0` with `(1 + ε) * n k ≤ n (k + 1)` for every index. These conditions entail the increasing lacunary sequence in the original question. Indexing from zero instead of one does not change the range of the sequence.

`Erdos894.erdos_894` proves `HasAvoidingColoring n` for every such sequence. The conclusion is a natural number `C` and a total coloring `ℕ → Fin C` such that any `a - b` in the sequence's range forces distinct colors. Natural-number subtraction truncates at zero, but no sequence member is zero, so the condition can hold only with `b < a`. It therefore expresses exactly the requested positive differences. The domain includes zero, which is at least as strong as coloring only positive natural numbers.

The proof constructs separated rotations for sequences growing by a factor of at least four using nested intervals, divides a general lacunary sequence into finitely many such subsequences, and takes a finite product of quarter-circle colorings. Its final theorem has no unproved separation hypothesis: that intermediate hypothesis is discharged inside the file from lacunarity.

This covers the original existence of a finite coloring. It does not assert the best quantitative estimate `O(ε⁻¹ log(1/ε))` discussed as a refinement on the source page.

## Replay scope

`inputs.json` pins exact Git-blob SHA-256 hashes, source commit, mathematical/formal authors, and Lean/Mathlib versions. `Audit894.lean` exposes the main theorem's type and axiom dependencies. `verified-run/verification.json`, when produced, records actual command completion and exit codes; this review by itself is not a claim of successful compilation.

The target command `leanchecker --verbose Erdos894` replays this module's declarations into the pinned imported environment using the same Lean kernel. It does not independently implement the kernel or replay all Mathlib dependencies. The shared compiler coordinator must serialize heavy processes.
