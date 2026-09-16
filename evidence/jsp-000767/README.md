# JSP-000767 / Erdős 924: attributed existing proof verification

Every k>=2,l>=3 admits finite K_(l+1)-free graph edge Ramsey for K_l in k colors.

Scope boundary: Exact complete-graph instance of Nesetril–Rodl needed by problem; arbitrary target-graph strengthening not required.

The [pinned original source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos924.lean) and its complete local import closure are copied without edits. Main-file mathematical credits: Jaroslav Nešetřil, Vojtěch Rödl. Main-file formal credits: Codex, GPT-5.6 Sol. Imported proof files retain their own credit and license notices. This packet makes no claim of a new mathematical result or new formal proof authorship by the submitting account.





## Observed verification

All 3 local proof modules were compiled in dependency order, followed by the terminal statement/axiom audit and 1 checker invocation(s). Every recorded step exited 0. The exact final theorem `Erdos924.erdos_924` uses only `['Classical.choice', 'Quot.sound', 'propext']`. The actual verbose checker module list equals the whole pinned local source closure; see verified-run/verification.json. Source/log hashes and the individual commands are recorded there and in inputs.json.

The audit also checks every target listed in inputs.json `audit_targets`, including any alternate statement needed for the advertised scope. Their individual axiom sets are recorded in verification.json and contain only the same three allowed standard axioms.

The checker uses Lean 4.33.0's own kernel, with Mathlib pinned at `db584cd6d46c92f209a44c0f1c829460d327499d`. It trusts the imported Mathlib/package caches; it is not an independent implementation or a fresh check of all Mathlib declarations. LEAN_NUM_THREADS=1 was explicit. The run was not network-isolated and does not establish an official two-checker record, prize eligibility, recipient confirmation or curator approval.

## Reproduce

With Python 3, Git and the matching cached Lean/Mathlib environment, run from the packet directory:

```text
python reproduce.py --packet . --lean-bin <Lean-4.33.0-bin> --mathlib <pinned-Mathlib-checkout> --output reproduced-run
```

The coordinator performs stages sequentially. On a shared host, supply `--serial-runner <trusted-run_lean_serial.py>` to acquire and release its mutex separately for every source module/audit/checker stage. Do not also wrap the whole coordinator in that mutex. Recorded successful evidence is preserved. No .olean files are distributed in this source packet; they are produced during reproduction.

[Original question](https://www.erdosproblems.com/924) · [Catalog entry](https://github.com/TheJustinSunPrize/awards/blob/f4e7173d89dfe91022a185427d63452c8ffbf6ae/problems/catalog-0701-0800.md#JSP-000767). statement-review.md records the reviewed definitions, quantifiers and limitations.
