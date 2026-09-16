# JSP-000633 / Erdős 772: existing proof and local verification

The unchanged attributed proof answers the growth questions for Sidon subsets under bounded two-term representation counts. Its direct finite-set theorem says: if every ordered sum representation count of A is at most k, some Sidon subset S⊆A satisfies |A|²≤4096(k+1)³|S|³. This gives an explicit n^(2/3) lower bound, so the guaranteed subset size divided by √n tends to infinity and admits a positive exponent improvement for each fixed admissible representation bound.

Mathematical authors: Noga Alon and Paul Erdős (1985). Formal authors in the retained source header: Codex and GPT-5.6 Sol. Original copyright and Apache 2.0 notice remain. The submitter contributes verification evidence only.

## Definitions and edge cases

The modern source page uses ordered convolution counts. The source's H(k,n) caps candidate guarantee sizes at n; when k=1 and n≥2 the admissible class is empty, giving H=n by that explicit convention. The direct finite-set theorem avoids relying on an empty-class maximum. For the nonvacuous range k≥2 it gives the original asymptotic conclusions. The source does not assert an unrestricted maximum of a vacuous predicate.

The 1985 primary paper uses unordered representations with distinct summands. An upper bound k in that convention implies ordered counts including a possible diagonal are at most 2k+1, so the stated finite-set theorem applies with that substitution. The formal Sidon predicate also excludes nontrivial diagonal collisions. This package does not claim to formalize all other results in the original paper.

## Pinned source and observed result

[Exact upstream source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos772.lean), saved as Erdos772Existing.lean, SHA-256 `c11e5d58be0b3e8a690fa5f790d59ff2a7eb6e4df63390f4aa68c04784a626de`. Lean 4.33.0; Mathlib `db584cd6d46c92f209a44c0f1c829460d327499d`.

Unchanged source compilation, the axiom/statement audit and target `leanchecker Erdos772Existing` all exited 0. The main theorem, direct finite-set cubic bound and real-power lower bound all report exactly `[propext, Classical.choice, Quot.sound]`. Recorded commands/results are in replay-result.json; the three logs and manifest contain actual evidence and hashes.

The bundled checker uses the same Lean kernel with the pinned imported Mathlib environment; it does not independently reimplement the kernel or replay all dependencies. The run was not network-isolated and is not an official two-checker prize verification record.

## Reproduce

In a fresh copy of this packet, supply a Lean 4.33.0 distribution root and the pinned Mathlib checkout with its matching compiled cache:

```text
python replay.py --toolchain <Lean-4.33.0-root> --mathlib <pinned-Mathlib-checkout>
```

This is the actual portable script used for the recorded successful run. It writes its own output and logs in that copy, and does not change Mathlib. It accepts explicit paths or REPLAY_LEAN_TOOLCHAIN / REPLAY_MATHLIB environment variables. No private local-config.json is included. Obtain the pinned Mathlib cache before replay, for example with `lake exe cache get` in the matching checkout.

[Original question](https://www.erdosproblems.com/772) · [Catalog](https://github.com/TheJustinSunPrize/awards/blob/main/problems/catalog-0601-0700.md#JSP-000633). Further source and boundary-case details are in statement-review.md.
