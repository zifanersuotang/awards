# JSP-000759 / Erdős 915: existing proof and local verification

17 vertices, 41 edges and no 5 internally vertex-disjoint paths between any pair refutes proposed bound.

Scope limitation: Matches JSP internally-disjoint wording. Positive edge-disjoint variant and sharp extremal counts not claimed covered.

This is checking of an existing public formalization, with no claim of new proof authorship. Mathematical authors credited by the unchanged source: Bo Sørensen, Carsten Thomassen. Formal authors credited by it: Codex, GPT-5.6 Sol. Original copyright/license notices are retained.

The [original source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos915.lean) is pinned at `8822f7ddef30fadbd92e1c6ab4ed897af356af5e` and included byte-for-byte. inputs.json pins both the proof and audit-harness SHA-256 hashes. Lean is 4.33.0 and Mathlib is `db584cd6d46c92f209a44c0f1c829460d327499d` with matching compiled dependencies.

## Observed verification

Unchanged source compilation, audit compilation and `leanchecker --verbose Erdos915` all exited 0. The exact target `Erdos915.not_erdos_915` reports only `['Classical.choice', 'Quot.sound', 'propext']`. verified-run/verification.json and the three logs record actual commands, results and hashes. The audit prints the final theorem type for inspection.

The checker uses the same Lean kernel and pinned imported Mathlib environment, replaying only this target module. It is not an independently implemented checker or a fresh replay of all dependency declarations. The run was not network-isolated and does not create an official two-checker record, curator approval or award eligibility.

## Reproduce

Preserve the packet's exact bytes. From this directory, with Python 3, Git and the pinned cached dependencies, run:

```text
python reproduce.py --packet . --lean-bin <Lean-4.33.0-bin> --mathlib <pinned-Mathlib-checkout> --output reproduced-run
```

This executes the same source/audit/checker commands sequentially, with version and hash checks. The output-directory option preserves recorded evidence. The submitted record used the default verified-run directory. Do not run several heavy Lean jobs at once on a shared computer. Obtain the matching Mathlib cache before reproduction.

[Original question](https://www.erdosproblems.com/915) · [Catalog entry](https://github.com/TheJustinSunPrize/awards/blob/main/problems/catalog-0701-0800.md#JSP-000759). The proof is of the explicitly described resolved question; further refinements are not implied by successful compilation.
