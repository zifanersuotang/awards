# JSP-000663 / Erdős 806: existing proof and local verification

The unchanged existing proof establishes the uniform little-o assertion: for every ε>0, all sufficiently large n work for every A⊆{1,…,n} with |A|≤√n, admitting a finite B⊆ℤ with A⊆B+B and |B|≤ε√n. The threshold depends on ε, not on A. This covers the resolved yes/no question; the stronger quantitative O(√n log log n / log n) rate is not claimed.

Mathematical authors: Noga Alon, Boris Bukh and Benny Sudakov (2009), *Discrete Kakeya-type problems and small bases*. Formal authors in the retained source: Codex and GPT-5.6 Sol. The original copyright and Apache 2.0 notice are retained. This package contributes local verification only.

The included source is the exact Git blob from [plby/lean-proofs](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos806.lean), SHA-256 `beebec5cbb481dbdeb66adcdc5db9323b080bbe783b01b4b2df13ff9b9743abd`. Lean is 4.33.0 and Mathlib is pinned to `db584cd6d46c92f209a44c0f1c829460d327499d`.

Actual unchanged-source compilation, audit compilation, and `leanchecker --verbose Erdos806` all exited 0 on 2026-09-16. All seven target/helper axiom reports are exactly `[propext, Classical.choice, Quot.sound]`. `verification.json` and the four logs record these observed results. Machine-specific paths alone were removed from the report; source and log bytes were preserved.

The bundled checker replays target-module declarations with the same Lean kernel and pinned imported environment. This is not an independently implemented checker, a fresh replay of all dependencies, or official prize verification. The run was not network-isolated.

With Python 3, Git, the pinned Lean distribution and the pinned Mathlib checkout plus its compiled cache, reproduce with:

```text
python reproduce.py --lean-bin <Lean-4.33.0-bin-directory> --mathlib <pinned-Mathlib-checkout> --stage all
```

The portable wrapper checks versions/source hash and runs the same recorded proof commands sequentially. It was syntax-checked; the recorded local commands themselves ran successfully. It writes fresh `reproduced-*` evidence and does not replace the recorded logs. Obtain the matching Mathlib cache using `lake exe cache get` in the pinned checkout before running.

[Catalog entry](https://github.com/TheJustinSunPrize/awards/blob/main/problems/catalog-0601-0700.md#JSP-000663) · [Original problem](https://www.erdosproblems.com/806). See `statement-review.md` for definitions, quantifiers and scope.
