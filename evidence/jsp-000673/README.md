# JSP-000673 / Erdős 816: existing proof and local verification

Full valid n≥2 range for 2n+1 vertices and n²+n+1 edges. Three-edge path explicitly has four distinct vertices. n=1 is correctly excluded because K3 is a counterexample; stronger ≥ edge bound also proved.

Scope limitation: n=1 is a mathematical counterexample; source theorem correctly uses n>=2

This is checking of an existing public formalization, with no claim of new proof authorship. Mathematical authors credited by the unchanged source: Kaizhe Chen, Jie Ma, Zhen Liu, Qinghou Zeng. Formal authors credited by it: Codex, GPT-5.6 Sol. Original copyright/license notices are retained.

The [original source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos816.lean) is pinned at `8822f7ddef30fadbd92e1c6ab4ed897af356af5e` and included byte-for-byte. inputs.json pins both the proof and audit-harness SHA-256 hashes. Lean is 4.33.0 and Mathlib is `db584cd6d46c92f209a44c0f1c829460d327499d` with matching compiled dependencies.

## Observed verification

Unchanged source compilation, audit compilation and `leanchecker --verbose Erdos816` all exited 0. The exact target `Erdos816.erdos_816` reports only `['Classical.choice', 'Quot.sound', 'propext']`. verified-run/verification.json and the three logs record actual commands, results and hashes. The audit prints the final theorem type for inspection.

The checker uses the same Lean kernel and pinned imported Mathlib environment, replaying only this target module. It is not an independently implemented checker or a fresh replay of all dependency declarations. The run was not network-isolated and does not create an official two-checker record, curator approval or award eligibility.

## Reproduce

Preserve the packet's exact bytes. From this directory, with Python 3, Git and the pinned cached dependencies, run:

```text
python reproduce.py --packet . --lean-bin <Lean-4.33.0-bin> --mathlib <pinned-Mathlib-checkout> --output reproduced-run
```

This executes the same source/audit/checker commands sequentially, with version and hash checks. The output-directory option preserves recorded evidence. The submitted record used the default verified-run directory. Do not run several heavy Lean jobs at once on a shared computer. Obtain the matching Mathlib cache before reproduction.

[Original question](https://www.erdosproblems.com/816) · [Catalog entry](https://github.com/TheJustinSunPrize/awards/blob/main/problems/catalog-0601-0700.md#JSP-000673). The proof is of the explicitly described resolved question; further refinements are not implied by successful compilation.
