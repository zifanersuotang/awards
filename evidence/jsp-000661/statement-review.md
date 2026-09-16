# JSP-000661 / Erdős 804: statement review

[Original problem](https://www.erdosproblems.com/804).

The original asks for the best global independence guaranteed by local independent sets of size at least log n on windows of size (log n)² or (log n)³. HasLocalIndependence uses exact-size windows; the extremal guarantee is defined as an attained finite maximum. The source explicitly rounds windows downward and thresholds upward. Its terminal theorem gives log²n/loglog n lower and log²n upper bounds for the square window, and matching constant-factor log²n/loglog n bounds for the cubic window, as in Alon–Sudakov. These bounds refute the two proposed stronger growth rates. It does not identify the exact square-window order inside the remaining loglog gap.

The pinned original source and its full credit/copyright blocks remain byte-for-byte intact. This is a review of an existing public proof, not an assertion of new mathematical or formal proof authorship.

This statement review does not assert compilation success. Only the actual `verified-run/verification.json`, its terminal theorem/axiom output, and command logs establish observed compilation and target-module replay. Imported Mathlib caches are trusted and the checker uses Lean's own kernel, not an independent implementation.
