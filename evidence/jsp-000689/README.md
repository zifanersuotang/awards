# JSP-000689 / Erdős 833: existing proof and local verification

This package records a successful local replay of an existing public Lean proof. It does not claim a new mathematical result, a new formalization, or ownership of the original authors' work.

The theorem gives one absolute constant `c=1/9` such that every finite `r`-uniform hypergraph of chromatic number three, `r≥2`, contains a vertex of degree at least `(1+c)^r`. The established degree bound `2^(r−1)/(4r)` is also proved. The exact extremal function `f(r)` is not claimed.

Mathematical authors: Paul Erdős and László Lovász. Formal authors credited by the source: Codex and GPT-5.6 Sol. The original Formal Conjectures copyright and Apache 2.0 notice are retained.

## Pinned source and dependencies

* Source: [plby/lean-proofs](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos833.lean), commit `8822f7ddef30fadbd92e1c6ab4ed897af356af5e`. Included `Erdos833.lean` is byte-for-byte the original LF git blob, SHA-256 `5cad260bdd589d4be977765c3934f8389395c6e6b480efee4dd8e325a7bf7cdb`.
* Lean `4.33.0`; Mathlib commit `db584cd6d46c92f209a44c0f1c829460d327499d`, with its pinned dependency manifest and compiled cache. Obtain the cache from that Mathlib checkout using `lake exe cache get` with the matching Lean toolchain.
* `Audit833.lean` prints the exact target types and seven target/helper axiom reports.

## Actual verification

On 2026-09-16, unchanged source compilation, audit compilation and bundled `leanchecker --verbose Erdos833` all exited 0. All seven reported axiom sets are exactly `[propext, Classical.choice, Quot.sound]`. The saved `verification.json` and four logs contain the observed evidence; machine-specific path fields have been removed from the JSON. Source and log bytes are preserved.

`leanchecker` replays target-module declarations using the same Lean kernel against the pinned imported environment. It is not an independently implemented checker and this run did not replay all dependency declarations into an empty environment. No official verifier or prize determination is claimed.

## Portable reproduction

With Python 3, Git, the matching Lean distribution and the pinned cached Mathlib checkout, run from this directory:

```text
python reproduce.py --lean-bin <Lean-4.33.0-bin-directory> --mathlib <pinned-Mathlib-checkout> --stage all
```

The Python script verifies the source hash, Lean version and Mathlib commit, then compiles each file with `-j1 -M4096` and runs the target checker sequentially. It downloads nothing and does not change shared dependency files. It omits absent optional package build directories. The recorded replay used equivalent commands through a local concurrency mutex; the portable wrapper was syntax-checked, but has not itself been run end-to-end again. Its fresh output uses `reproduced-*` filenames and does not overwrite the recorded evidence.

[Catalog question](https://github.com/TheJustinSunPrize/awards/blob/main/problems/catalog-0601-0700.md#JSP-000689) · [Original problem and bibliography](https://www.erdosproblems.com/833)
