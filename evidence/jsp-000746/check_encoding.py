"""Independently compare the certificate's CNF to the stated graph problem.

This is a transparent structural check, not an LRAT proof verifier.
Lean's compiled proof term and target-module kernel replay verify unsatisfiability.
"""
import hashlib
import itertools
import json
from pathlib import Path

root = Path(__file__).resolve().parent
source = root / 'Erdos895/Certificate.cnf'
lines = source.read_text(encoding='utf-8').splitlines()
assert lines[0].split() == ['p', 'cnf', '153', '888']
clauses = []
for line in lines[1:]:
    if not line.strip() or line.startswith('c'):
        continue
    literals = list(map(int, line.split()))
    assert literals[-1] == 0
    assert all(1 <= abs(lit) <= 153 for lit in literals[:-1])
    clauses.append(tuple(literals[:-1]))
edges = list(itertools.combinations(range(1, 19), 2))
edge_id = {edge: i + 1 for i, edge in enumerate(edges)}
triangle_clauses = [
    (-edge_id[a, b], -edge_id[a, c], -edge_id[b, c])
    for a, b, c in itertools.combinations(range(1, 19), 3)
]
schur_triples = [(a, b, a + b) for a in range(1, 19) for b in range(a + 1, 19) if a + b <= 18]
schur_clauses = [(edge_id[a, b], edge_id[a, c], edge_id[b, c]) for a, b, c in schur_triples]
expected = triangle_clauses + schur_clauses
assert len(set(clauses)) == len(clauses) == 888
assert clauses == expected
report = {
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'encoding': 'Mathematical labels 1..18; edge variables are lexicographically ordered unordered pairs.',
    'edge_variables': len(edges),
    'triangle_clauses': len(triangle_clauses),
    'distinct_summand_schur_clauses': len(schur_clauses),
    'ordered_exact_match': True,
    'scope': 'Structural correspondence only. LRAT proof validity is checked by Lean compilation/kernel replay.',
}
(root / 'encoding-verification.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps(report, indent=2))
