# JSP-000746 / Erdős 895: existing proof and local verification

The unchanged public proof establishes that every triangle-free graph on labels {1,…,n}, for all n≥18, has three distinct independent vertices a,b,a+b. The theorem proves sufficiency of 18; it does not prove a counterexample at 17 or the stronger Hindman-set question. The original source's prose uses “sharp”; this verification makes no sharpness claim.

Mathematical author: Ben Barber. Formal authors named by the source: Codex and GPT-5.6 Sol. The original author header is preserved. The submitter contributes reproducible checking and statement review only, with no new-formalization claim. The upstream license notice is retained as LICENSE.upstream.

The source and CNF/LRAT certificates are exact Git blobs from plby/lean-proofs commit `8822f7ddef30fadbd92e1c6ab4ed897af356af5e`; all three SHA-256 hashes are pinned in inputs.json and the recorded verification report. Lean is 4.33.0 and Mathlib is `db584cd6d46c92f209a44c0f1c829460d327499d`.

The finite graph encoding has 153 edge variables, 816 clauses excluding triangles, and 72 clauses requiring an edge in every distinct-summand Schur triple. check_encoding.py independently enumerates and compares these clauses exactly. Lean reconstructs a proof from the LRAT certificate; no external SAT solver is trusted or required during replay. The source extends the 18-vertex result to every larger n by a label-preserving graph restriction.

## Actual verification

On 2026-09-16, source compilation, audit compilation and `leanchecker --verbose Erdos895` all exited 0. The certificate theorem, finite contradiction, 18-vertex theorem, extension and terminal theorem all report exactly `[propext, Classical.choice, Quot.sound]`. Commands, timings and log hashes are recorded in verification.json; input and log bytes are preserved in this packet.

Two earlier invocations failed before a successful result: a bare input filename lacked a parent directory for the certificate paths, and a later run hit the 4096 MiB kernel cap. The successful invocation uses `./Erdos895.lean` and `-M6144`, with the original source and certificates unchanged. The failed runs are not counted as successful checks.

The bundled checker replays only this target module with the same Lean kernel and pinned imported Mathlib environment. This is neither an independently implemented checker nor a fresh replay of all dependencies. The run was not network-isolated and does not create an official prize verification record.

## Reproduce

Use a fresh copy of this packet, preserving exact LF bytes. Supply a matching Lean 4.33.0 bin directory and the pinned cached Mathlib checkout:

```text
python reproduce.py --lean-bin <Lean-4.33.0-bin> --mathlib <pinned-Mathlib-checkout>
```

The portable wrapper checks the input hashes and versions, then executes the successful source/audit/checker commands sequentially. It was syntax-checked; the recorded equivalent local commands actually ran. It writes portable-verification.json and new logs in the fresh copy. Obtain the matching Mathlib compiled cache before replay. For shared machines, serialize the entire command; no simultaneous heavy Lean jobs are needed.

[Original problem](https://www.erdosproblems.com/895) · [Pinned source](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos895.lean) · [Catalog](https://github.com/TheJustinSunPrize/awards/blob/main/problems/catalog-0701-0800.md#JSP-000746). See semantic-review.md for the exact coordinate and boundary checks.
