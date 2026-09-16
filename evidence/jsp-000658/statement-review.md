# JSP-000658 / Erdős 801: statement review

[Original problem](https://www.erdosproblems.com/801).

The original asymptotic statement bounds global independence by sqrt(n) and asks for at most sqrt(n) vertices spanning at least a constant times sqrt(n) log n edges. The source uses Mathlib indepNum, floor square root Nat.sqrt, floor base-two logarithm Nat.log 2, and counts two-element unordered adjacent vertex sets inside S. It supplies positive absolute C and a threshold N, uniformly for every n≥N and every graph. Integer rounding and log-base changes preserve the stated asymptotic order. The terminal inequality sqrt(n)·log₂(n)≤C·edgeCount is a lower bound on edges, not its reverse. No optimal constant or stronger small-n theorem is claimed.

The pinned original source and its full credit/copyright blocks remain byte-for-byte intact. This is a review of an existing public proof, not an assertion of new mathematical or formal proof authorship.

This statement review does not assert compilation success. Only the actual `verified-run/verification.json`, its terminal theorem/axiom output, and command logs establish observed compilation and target-module replay. Imported Mathlib caches are trusted and the checker uses Lean's own kernel, not an independent implementation.
