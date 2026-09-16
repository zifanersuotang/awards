"""Reproduce JSP-000663 / Erdos 806 using explicitly supplied pinned dependencies.

Requires Python 3, Git, Lean 4.33.0 and a built/cached Mathlib checkout at the
recorded revision. This script downloads nothing and does not edit dependencies.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

SOURCE_HASH = 'beebec5cbb481dbdeb66adcdc5db9323b080bbe783b01b4b2df13ff9b9743abd'
MATHLIB_COMMIT = 'db584cd6d46c92f209a44c0f1c829460d327499d'
EXPECTED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
ROOT = Path(__file__).resolve().parent

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--lean-bin', required=True, type=Path)
    parser.add_argument('--mathlib', required=True, type=Path)
    parser.add_argument('--stage', choices=['compile', 'checker', 'all'], default='all')
    args = parser.parse_args()
    binary_dir = args.lean_bin.resolve()
    mathlib = args.mathlib.resolve()
    suffix = '.exe' if os.name == 'nt' else ''
    lean, checker = [binary_dir / (name + suffix) for name in ['lean', 'leanchecker']]
    if sha(ROOT / 'Erdos806.lean') != SOURCE_HASH:
        raise RuntimeError('Original source SHA-256 mismatch')
    commit = subprocess.check_output(['git', '-C', str(mathlib), 'rev-parse', 'HEAD'], text=True).strip()
    if commit != MATHLIB_COMMIT:
        raise RuntimeError('Mathlib revision differs from pinned revision')
    version = subprocess.check_output([str(lean), '--version'], text=True).strip()
    if 'version 4.33.0,' not in version:
        raise RuntimeError('Lean 4.33.0 required')
    paths = [ROOT, mathlib / '.lake/build/lib/lean']
    if not paths[1].is_dir():
        raise RuntimeError('Mathlib compiled module directory missing; obtain its pinned cache first')
    paths += sorted(p for p in (mathlib / '.lake/packages').glob('*/.lake/build/lib/lean') if p.is_dir())
    env = os.environ.copy()
    env['LEAN_PATH'] = os.pathsep.join(map(str, paths))
    commands = []
    if args.stage in ['compile', 'all']:
        commands += [('compile-source', [str(lean), '-j1', '-M4096', '-o', 'Erdos806.olean', 'Erdos806.lean']),
                     ('compile-audit', [str(lean), '-j1', '-M4096', '-o', 'Audit806.olean', 'Audit806.lean'])]
    if args.stage in ['checker', 'all']:
        commands += [('leanchecker', [str(checker), '--verbose', 'Erdos806'])]
    output = ROOT / f'reproduced-{args.stage}.json'
    report = {'source_sha256': SOURCE_HASH, 'mathlib_commit': commit, 'lean_version': version,
              'stage': args.stage, 'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'commands': [], 'success': False,
              'checker_scope': 'Target-module replay using same Lean kernel and pinned imported environment; not a fresh dependency replay or independently implemented checker.'}
    for name, command in commands:
        print(f'Starting {name}', flush=True)
        log = ROOT / f'reproduced-{name}.log'
        start = time.monotonic()
        with log.open('w', encoding='utf-8') as out:
            result = subprocess.run(command, cwd=ROOT, env=env, stdout=out, stderr=subprocess.STDOUT)
        report['commands'].append({'name': name, 'command': [Path(command[0]).name, *command[1:]],
            'exit_code': result.returncode, 'elapsed_seconds': round(time.monotonic()-start, 3),
            'log': log.name, 'log_sha256': sha(log)})
        output.write_text(json.dumps(report, indent=2), encoding='utf-8')
        if result.returncode:
            return result.returncode
        if name == 'compile-audit':
            entries = re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log.read_text(encoding='utf-8'))
            if len(entries) != 7 or any(set(x.strip() for x in ax.split(',')) != EXPECTED_AXIOMS for _, ax in entries):
                raise RuntimeError('Unexpected target axiom report; inspect generated log')
            report['target_axioms'] = {target: [x.strip() for x in ax.split(',')] for target, ax in entries}
    report['success'] = True
    report['finished_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    report['artifacts'] = [{'path': p.name, 'sha256': sha(p)} for p in sorted(ROOT.glob('*.olean'))]
    output.write_text(json.dumps(report, indent=2), encoding='utf-8')
    return 0

if __name__ == '__main__':
    sys.exit(main())
