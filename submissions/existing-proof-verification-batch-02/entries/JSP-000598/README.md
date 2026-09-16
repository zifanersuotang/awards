# JSP-000598 / Erdős 730

Infinitely many natural indices n have exactly the same set of prime divisors in choose(2*n,n) and choose(2*(n+1),n+1), hence infinitely many strictly ordered distinct pairs do. The explicit quadratic family has parameter lower density greater than 107/2500. This is not positive natural density of the output indices and no standalone square-root counting bound for all cutoffs is claimed by the replay entry.

Main source header: informal authors Liam Price, Tomodovodoo, Will Blair, GPT Pro; formal authors Will Blair, Codex, Claude Code. Header cites williamjblair/lean-proofs versions 03729c9cbb0b602f5a828bb850c85e84c5a6d460 and 5d10b4d91f257cfbe8c563cf927f543a868845e0 and a proof claim. The selected execution bytes are the plby pinned port. All source bytes and notices remain unchanged; dependency files without author notices do not establish ownership. Do not label this reviewer/uploader an original formalizer.

Main declaration: `Erdos730.erdos_730`. Actual target module: `ErdosProblems.Erdos730`.

All 47 custom sources compiled unchanged; the importing audit and checker exited 0. The checker actually replayed 38 modules.

See [evidence.json](evidence.json) for immutable upstream URLs, every source SHA-256, build order, exact axiom sets, checker selection and links/digests for all logs.

No upstream proof source is copied into this attachment. Reproduction uses [verify.py](../../verify.py) with this evidence.json and a dedicated pinned Mathlib checkout.

## Source history and prior records

The execution uses unchanged plby/lean-proofs sources at 8822f7ddef30fadbd92e1c6ab4ed897af356af5e. Earlier williamjblair source versions and the proof claim are credited in the retained source headers; equivalence to every earlier version is not asserted.

The original problem asks for infinitely many distinct pairs. Both that statement and the stronger consecutive-index infinitude theorem were checked in the completed axiom audit.

The explicit density bound is a lower density of the family parameter x, with n(x)=84591927504*x^2+7076682*x+142. It is not a positive natural density claim for output indices.

[PR #40](https://github.com/TheJustinSunPrize/awards/pull/40) already identifies this pinned source and reports source-only review. [Issue #20](https://github.com/TheJustinSunPrize/awards/issues/20) records the omitted infinitude quantifier. [Issue #69](https://github.com/TheJustinSunPrize/awards/issues/69) explicitly concerns only the historical finite witness (87, 88), excludes infinitude and reports kernel verification pending; this packet does not adjudicate that separate recipient request.

Issue #69 is an open formal recipient request, not a completed kernel-verification record. This packet supplies new execution evidence for an already identified source; it is not a recipient application by this reviewer or uploader.
