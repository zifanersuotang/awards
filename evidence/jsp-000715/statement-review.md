# JSP-000715 / Erdős 863: statement review

[Original problem](https://www.erdosproblems.com/863).

The original question explicitly assumes existence of the two square-root asymptotic constants and asks whether the positive-difference constant is strictly smaller than the unordered-sum constant for r≥2. The source counts sum representations with a≤b, positive differences n≥1, and attained maxima over subsets of [1,N]. HasSqrtAsymptotic retains the original conditional limit assumptions. The proof obtains the bounds cDiff≤sqrt(r)<(r+floor(r/2))/sqrt(r+2floor(r/2))≤cSum, and the audited terminal concludes cDiff<cSum. It does not prove existence of either asymptotic constant or assert a result at r=1.

The pinned original source and its full credit/copyright blocks remain byte-for-byte intact. This is a review of an existing public proof, not an assertion of new mathematical or formal proof authorship.

This statement review does not assert compilation success. Only the actual `verified-run/verification.json`, its terminal theorem/axiom output, and command logs establish observed compilation and target-module replay. Imported Mathlib caches are trusted and the checker uses Lean's own kernel, not an independent implementation.
