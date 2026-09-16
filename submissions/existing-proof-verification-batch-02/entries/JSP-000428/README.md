# JSP-000428 / Erdős 534

For every N>=2, some nonempty initial segment q1<...<qj of the distinct prime divisors of N gives a maximum-cardinality subset of [1,N] containing N with gcd(a,b)>1 for distinct members: take all integers divisible by one of 2q1,...,2qj or by q1*...*qj. The theorem proves both candidate admissibility and domination of every admissible family, establishing the refined Ahlswede-Khachatrian result; it does not assert the earlier two-case formula or uniqueness of all maximizers.

Existing plby/lean-proofs source. The original header credits Rudolf Ahlswede and Levon H. Khachatrian mathematically, and Codex / GPT-5.6 Sol for formalization; all source bytes and notices are preserved with no uploader-as-original-author, priority, recipient or new-proof claim.

Main declaration: `Erdos534.erdos_534`. Actual target module: `ErdosProblems.Erdos534`.

All 7 custom sources compiled unchanged; the importing audit and checker exited 0. The checker actually replayed 7 modules.

See [evidence.json](evidence.json) for immutable upstream URLs, every source SHA-256, build order, exact axiom sets, checker selection and links/digests for all logs.

No upstream proof source is copied into this attachment. Reproduction uses [verify.py](../../verify.py) with this evidence.json and a dedicated pinned Mathlib checkout.
