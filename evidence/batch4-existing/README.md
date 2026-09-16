# Existing Lean proof verification evidence: batch 4

This directory contains actual local verification metadata and logs for 24 existing public formalizations. The official registration is [Issue 24](https://github.com/TheJustinSunPrize/awards/issues/24); a successful local result does not establish official acceptance.

[Read the exact mathematical scope and caveats for every entry](SCOPES.md).

The original proof sources and their attributions remain at the immutable plby commit referenced in verification.json. No third-party proof source is distributed here. Every listed local proof module was compiled and explicitly replayed with Lean 4.33.0 and the pinned Mathlib environment. Each exported target has a separately compiled axiom report. The metadata records exact source hashes, successful process exits, durations and checksummed public logs.

Newer process records also preserve their actually recorded output artifacts, replay inputs and direct-project dependency identities. Older absent fields are not backfilled. Artifact paths use the proof-project root; compile-record references use the local verification-project root and identify original local metadata, which is not necessarily part of this public archive. These fields do not establish an automatic cross-project cache contract.

From the pinned upstream src/latest project with its dependencies installed, reproduce a target with lake build ErdosProblems.ErdosN and lake env leanchecker --verbose ErdosProblems.ErdosN. Replay the local modules listed in compile_order as well. For an axiom report, create an importing Lean file containing one #print axioms command per listed target and run lake env lean on it.

Lean elaboration and leanchecker use the same kernel. Imported Mathlib cache declarations were not all freshly replayed. These are AI-assisted source-scope reviews and local checks, with organizer verification, recipient confirmation and any award decision pending.
