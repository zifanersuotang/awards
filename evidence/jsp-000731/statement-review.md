# JSP-000731 / Erdős 880: statement review

The [original question](https://www.erdosproblems.com/880) asks whether sums of at most k distinct elements of an additive basis of order k have bounded consecutive gaps, with the bound allowed to depend on the basis and k. The recorded resolution is positive at order two and negative at every order at least three.

The unchanged source represents unrestricted sums by lists of length at most k and restricted sums by finite sets of cardinality at most k. Its additive-basis predicate is asymptotic, infinite and of exact least order k. Its gap predicate uses the increasing `Nat.nth` enumeration; the proof establishes the required infinitude before applying enumeration facts.

`Erdos880.not_erdos_880` proves both clauses: every basis of exact order two has bounded restricted-sum gaps, while every h ≥ 3 admits an explicit exact-order-h basis whose restricted sums have unbounded gaps. The order-two argument includes the eventual bound two internally. The negative clause verifies the constructed basis has the stated least order, not merely an upper bound on its order. Zero and the empty sum are permitted by the finite-set convention, affecting only the initial terms rather than boundedness of gaps.

The source credits Norbert Hegyvári, François Hennecart and Alain Plagne for the mathematics, and Codex/GPT-5.6 Sol for formalization. This packet claims only verification of that existing proof, not a new mathematical result.

Source compilation, terminal statement/axiom audit and target-module replay all exited 0. The exact terminal axiom set is propext, Classical.choice, Quot.sound. Logs and hashes are in `verified-run/verification.json`. The checker shares Lean's kernel and trusts the pinned imported Mathlib environment; it is not an independent checker implementation or a fresh replay of all dependencies.
