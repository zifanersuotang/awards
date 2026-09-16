# Statement review — JSP-000689 / Erdős 833

The original asks whether an absolute real constant `c > 0` works for every `r ≥ 2` and every `r`-uniform hypergraph with chromatic number 3, forcing a vertex of degree at least `(1+c)^r`. It also asks more generally for the exact largest guaranteed integer `f(r)`. The catalog's resolved yes/no statement is the first question. This formalization answers that first question and the established `2^(r−1)/(4r)` bound. It does not claim exact `f(r)`.

`Hypergraph V` is a finite set of finite vertex sets; repeated edges are absent. `IsUniform H r` means every edge has cardinality `r`. `Monochromatic c e` compares the colors of all pairs in the edge. `IsProper` forbids monochromatic edges. `Colorable H k` is existence of a coloring into `Fin k`, and `HasChromaticNumber H k` asserts such a coloring exists and no coloring with fewer colors exists. `degree H v` counts exactly the edges containing `v`.

The terminal statement quantifies the constant before every finite vertex type, uniformity parameter and hypergraph. Thus the constant is genuinely absolute, not chosen separately for a hypergraph:

```lean
theorem erdos_833 :
  ∃ c : ℝ, 0 < c ∧
    ∀ (W : Type u) [Fintype W] [DecidableEq W]
      (r : ℕ), 2 ≤ r → ∀ H : Hypergraph W,
        IsUniform H r → HasChromaticNumber H 3 →
          ∃ v : W, (1 + c) ^ r ≤ degree H v
```

The proof chooses `c = 1/9`. For `2 ≤ r ≤ 6`, non-two-colorability forces a vertex of degree at least two. For `r ≥ 7`, it uses the established Erdős–Lovász degree bound and an elementary exponential comparison.

The symmetric local lemma is proved in this file rather than assumed. Its conditional non-neighbor cardinality hypothesis `hfar` is discharged explicitly in the hypergraph application by `monoEvent_inter_avoid_card_bound`, via recoloring outside disjoint edges. The final theorem contains no probabilistic independence hypothesis or unproved analytic assumption. The only imported module is Mathlib.

The original mathematical result is attributed to Erdős and Lovász, *Problems and results on 3-chromatic hypergraphs and some related questions* (1975), pp. 609–627. The pinned source retains its original formal-author header and Apache 2.0 copyright notice. Our contribution is local verification only.
