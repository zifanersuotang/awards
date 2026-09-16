# Existing-proof verification evidence — batch 2 continuation

This attachment supports bounded follow-up registrations to
[Issue 16](https://github.com/TheJustinSunPrize/awards/issues/16), whose original
eighteen-entry evidence packet remains intact. Each entry here must have
successful source compilation, a named-theorem axiom audit and an actual
target/descendant-module checker run before it is exported.

The proofs are pre-existing public work. Every entry preserves its exact
mathematical scope and source attribution. This attachment contains source
URLs and hashes, recorded results and logs; it does not vendor upstream proofs.
It is reproducibility evidence submitted for review, not an official signed
verification, author/recipient confirmation or award decision.

The original runs used Lean 4.33.0 on Windows with Mathlib commit
`db584cd6d46c92f209a44c0f1c829460d327499d`. All custom source files were built
from unchanged bytes in their dependency order with `-j1`; child environments
set `LEAN_NUM_THREADS=1`. The checker uses a structured Lean Name prefix,
so each entry records the modules it actually replayed. Imported Mathlib
libraries were reused from the pinned cache. This is not a fresh replay of
all Mathlib or an independently implemented kernel check.

Each `entries/JSP-NNNNNN/evidence.json` links the immutable upstream source
commit, source SHA-256 values, actual axiom sets, build order and all stage
logs. Each published log has its own byte hash. Any local-path redaction is
explicitly listed, with the original byte hash retained for provenance.

Run `python verify.py --entry entries/JSP-NNNNNN/evidence.json` to validate
the published metadata and logs without invoking Lean. To reproduce a proof,
prepare a fresh dedicated Mathlib checkout and cache, then pass `--execute`
and its absolute path via `--mathlib`:

```sh
git clone https://github.com/leanprover-community/mathlib4.git mathlib4-dedicated
git -C mathlib4-dedicated checkout --detach db584cd6d46c92f209a44c0f1c829460d327499d
cd mathlib4-dedicated
lake exe cache get
cd ..
python /path/to/attachment/verify.py --entry /path/to/attachment/entries/JSP-NNNNNN/evidence.json --execute --mathlib /absolute/path/to/mathlib4-dedicated
```

The verifier checks the actual Lean version, toolchain, Mathlib commit and
downloaded source bytes before compilation. Existing conflicting source files
are rejected. Results from a new reproduction are separate from this retained
evidence. The helper’s metadata/log validation has been checked locally; the
public recipe is a portable equivalent, not a claimed fresh Linux rerun.
