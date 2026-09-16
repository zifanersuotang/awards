# JSP-000673 / Erdős 816: statement review

[Original problem](https://www.erdosproblems.com/816).

The original page asks for equal-degree vertices joined by a three-edge path in a graph on 2n+1 vertices with n²+n+1 edges. The selected source proves the assertion for every n ≥ 2 (and an internal stronger at-least edge bound). JoinedByPathThree explicitly demands four distinct vertices and three successive edges, so it means a simple path, not a walk. The n ≥ 2 guard is essential: for n=1 the triangle has the specified size but lacks four distinct vertices. The webpage wording omits this small-case guard. The packet must display this caveat and does not claim an affirmative theorem for n=1. It also does not claim the later n≥600 classification at n²+n edges.

The pinned original source and its full credit/copyright blocks remain byte-for-byte intact. This is a review of an existing public proof, not an assertion of new mathematical or formal proof authorship.

This statement review does not assert compilation success. Only the actual `verified-run/verification.json`, its terminal theorem/axiom output, and command logs establish observed compilation and target-module replay. Imported Mathlib caches are trusted and the checker uses Lean's own kernel, not an independent implementation.
