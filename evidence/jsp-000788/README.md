# JSP-000788 / Erdős 948: existing proof and local verification

For every rate f and finite nonempty palette, a coloring forces all colors among finite sums of every qualifying strictly increasing sequence.

Scope limitation: Integer and natural variants retain the infinite-often growth condition. The nonempty finite-sum helper also covers that convention. The Lisa/Liam name discrepancy is disclosed, not silently repaired; no recipient identity is asserted.

This is checking of an existing public formalization, with no claim of new proof authorship. Mathematical authors credited by the unchanged source: Lisa Price, GPT-5.5 Pro. Formal authors credited by it: Codex, GPT-5.6 Sol. Original copyright/license notices are retained.

**Attribution discrepancy requiring curatorial review:** the unchanged source header says Lisa Price/GPT-5.5 Pro; the [primary proof-announcement thread](https://www.erdosproblems.com/forum/thread/948) is signed Liam Price (21 June 2026, 20:38), and the catalog names Liam Price. We preserve both records, do not infer they are the same person, and do not nominate a recipient. The forum reports an Aristotle formalization, while this selected source credits Codex/GPT-5.6 Sol; these are separate attribution records. This submission concerns the checked proof artifact and does not certify disputed identity or discovery credit.

The [original source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos948.lean) is pinned at `8822f7ddef30fadbd92e1c6ab4ed897af356af5e` and included byte-for-byte. inputs.json pins both the proof and audit-harness SHA-256 hashes. Lean is 4.33.0 and Mathlib is `db584cd6d46c92f209a44c0f1c829460d327499d` with matching compiled dependencies.

## Observed verification

Unchanged source compilation, audit compilation and `leanchecker --verbose Erdos948` all exited 0. The exact target `Erdos948.not_erdos_948` reports only `['Classical.choice', 'Quot.sound', 'propext']`. verified-run/verification.json and the three logs record actual commands, results and hashes. The audit prints the final theorem type for inspection.

The checker uses the same Lean kernel and pinned imported Mathlib environment, replaying only this target module. It is not an independently implemented checker or a fresh replay of all dependency declarations. The run was not network-isolated and does not create an official two-checker record, curator approval or award eligibility.

## Reproduce

Preserve the packet's exact bytes. From this directory, with Python 3, Git and the pinned cached dependencies, run:

```text
python reproduce.py --packet . --lean-bin <Lean-4.33.0-bin> --mathlib <pinned-Mathlib-checkout> --output reproduced-run
```

This executes the same source/audit/checker commands sequentially, with version and hash checks. The output-directory option preserves recorded evidence. The submitted record used the default verified-run directory. Do not run several heavy Lean jobs at once on a shared computer. Obtain the matching Mathlib cache before reproduction.

[Original question](https://www.erdosproblems.com/948) · [Catalog entry](https://github.com/TheJustinSunPrize/awards/blob/main/problems/catalog-0701-0800.md#JSP-000788). The proof is of the explicitly described resolved question; further refinements are not implied by successful compilation.
