"""Replay exact existing source; run this whole pipeline through the shared serial queue."""
import hashlib
import json
import argparse
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--toolchain', help='Root of Lean 4.33.0 installation')
parser.add_argument('--mathlib', help='Root of pinned Mathlib source and compiled cache')
args = parser.parse_args()
local_file = HERE / 'local-config.json'
local = json.loads(local_file.read_text(encoding='utf-8')) if local_file.exists() else {}
toolchain = args.toolchain or os.environ.get('REPLAY_LEAN_TOOLCHAIN') or local.get('toolchain')
mathlib = args.mathlib or os.environ.get('REPLAY_MATHLIB') or local.get('mathlib')
if not toolchain or not mathlib:
    parser.error('--toolchain and --mathlib are required (or corresponding REPLAY_* environment variables)')
TOOLCHAIN = Path(toolchain)
MATHLIB = Path(mathlib)
EXE = '.exe' if os.name == 'nt' else ''
PACKAGES = ['aesop', 'batteries', 'Cli', 'importGraph', 'LeanSearchClient', 'plausible', 'proofwidgets', 'Qq']
expected = 'c11e5d58be0b3e8a690fa5f790d59ff2a7eb6e4df63390f4aa68c04784a626de'
actual = hashlib.sha256((HERE / 'Erdos772Existing.lean').read_bytes()).hexdigest()
assert actual == expected, 'Exact-source hash changed'
env = os.environ.copy()
paths = [HERE, MATHLIB / '.lake/build/lib/lean'] + [MATHLIB / '.lake/packages' / p / '.lake/build/lib/lean' for p in PACKAGES]
env['LEAN_PATH'] = os.pathsep.join(map(str, paths))
env['PATH'] = str(TOOLCHAIN / 'bin') + os.pathsep + env['PATH']
mathlib_commit = subprocess.check_output(['git', '-C', str(MATHLIB), 'rev-parse', 'HEAD'], text=True).strip()
assert mathlib_commit == 'db584cd6d46c92f209a44c0f1c829460d327499d', 'Mathlib commit mismatch'
lean_version = subprocess.check_output([str(TOOLCHAIN / f'bin/lean{EXE}'), '--version'], text=True).strip()
assert 'version 4.33.0' in lean_version, 'Lean version mismatch'
steps = [
    ('compile', [str(TOOLCHAIN / f'bin/lean{EXE}'), '-j1', '-o', 'Erdos772Existing.olean', 'Erdos772Existing.lean']),
    ('axioms', [str(TOOLCHAIN / f'bin/lean{EXE}'), '-j1', 'Audit772.lean']),
    ('leanchecker', [str(TOOLCHAIN / f'bin/leanchecker{EXE}'), 'Erdos772Existing'])
]
report = {'source_sha256': actual, 'source_commit': '8822f7ddef30fadbd92e1c6ab4ed897af356af5e',
          'mathlib_commit': mathlib_commit, 'toolchain': lean_version,
          'source_export': 'Exact git show blob, LF; no mathematical or attribution changes',
          'steps': [], 'success': False}
for name, args in steps:
    start = time.time()
    print(f'START {name}', flush=True)
    with (HERE / f'{name}.log').open('wb') as log:
        result = subprocess.run(args, cwd=HERE, env=env, stdout=log, stderr=subprocess.STDOUT)
    record = {'name': name, 'args': [Path(args[0]).name, *args[1:]], 'exit_code': result.returncode, 'elapsed_seconds': round(time.time()-start, 3), 'log': f'{name}.log'}
    report['steps'].append(record)
    (HERE / 'replay-result.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(record), flush=True)
    if result.returncode:
        sys.exit(result.returncode)
report['success'] = True
(HERE / 'replay-result.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
