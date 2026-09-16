"""Portable exact-input replay. Run through the shared compiler coordinator.

Each proof directory contains an identical copy of this script and inputs.json.
The report uses portable path labels; process arguments use the supplied paths.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
PACKAGES = ['aesop', 'batteries', 'Cli', 'importGraph', 'LeanSearchClient', 'plausible', 'proofwidgets', 'Qq']

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lean-bin', required=True, type=Path)
    parser.add_argument('--mathlib', required=True, type=Path)
    parser.add_argument('--stage', choices=['all', 'compile', 'checker'], default='all')
    args = parser.parse_args()
    lean_bin = args.lean_bin.resolve()
    mathlib = args.mathlib.resolve()
    manifest = json.loads((ROOT / 'inputs.json').read_text(encoding='utf-8'))
    for relative, expected in manifest['input_sha256'].items():
        if sha(ROOT / relative) != expected:
            raise RuntimeError(f'Pinned input mismatch: {relative}')
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=mathlib, text=True).strip()
    if commit != manifest['mathlib_commit']:
        raise RuntimeError(f'Mathlib commit mismatch: {commit}')
    paths = [ROOT, mathlib / '.lake/build/lib/lean']
    for path in paths:
        if not path.is_dir():
            raise RuntimeError('Missing main build directory')
    package_paths = {package: mathlib / '.lake/packages' / package / '.lake/build/lib/lean' for package in PACKAGES}
    present_packages = [package for package, path in package_paths.items() if path.is_dir()]
    paths.extend(package_paths[package] for package in present_packages)
    env = os.environ.copy()
    env['LEAN_PATH'] = os.pathsep.join(map(str, paths))
    executable_suffix = '.exe' if os.name == 'nt' else ''
    lean = lean_bin / ('lean' + executable_suffix)
    checker = lean_bin / ('leanchecker' + executable_suffix)
    module = manifest['module']
    harness = manifest['harness_module']
    commands = [('version', [str(lean), '--version'])]
    if args.stage in ('all', 'compile'):
        commands.extend([
            ('compile-source', [str(lean), '-j1', '-M6144', '-o', module + '.olean', './' + module + '.lean']),
            ('compile-audit', [str(lean), '-j1', '-M6144', '-o', harness + '.olean', harness + '.lean']),
        ])
    if args.stage in ('all', 'checker'):
        commands.append(('leanchecker', [str(checker), '--verbose', module]))
    report = {
        'jsp': manifest['jsp'], 'erdos': manifest['erdos'],
        'source_repo': manifest['source_repo'], 'source_commit': manifest['source_commit'],
        'source_unchanged': True, 'source_sha256': manifest['input_sha256'],
        'mathlib_commit': commit, 'stage': args.stage, 'started_utc': now(),
        'available_package_builds': present_packages,
        'omitted_nonexistent_optional_package_builds': [p for p in PACKAGES if p not in present_packages],
        'runtime_sha256': {'lean': sha(lean), 'leanchecker': sha(checker)},
        'lean_path': ['<proof-directory>', '<mathlib>/.lake/build/lib/lean'] +
            [f'<mathlib>/.lake/packages/{p}/.lake/build/lib/lean' for p in present_packages],
        'commands': [], 'success': False,
        'checker_scope': 'Bundled leanchecker replays only the target module declarations with the same Lean kernel into its pinned imported Mathlib environment. This is not an independently implemented checker or a fresh replay of all dependencies.',
    }
    report_path = ROOT / ('portable-verification.json' if manifest['erdos'] == 895 else 'verification.json')
    for name, command in commands:
        print(f'Starting {name}', flush=True)
        started = time.monotonic()
        log = ROOT / (name + '.log')
        with log.open('w', encoding='utf-8') as output:
            result = subprocess.run(command, cwd=ROOT, env=env, stdout=output, stderr=subprocess.STDOUT)
        portable_command = ['<lean-bin>/' + Path(command[0]).name, *command[1:]]
        report['commands'].append({
            'name': name, 'command': portable_command, 'exit_code': result.returncode,
            'elapsed_seconds': round(time.monotonic() - started, 3),
            'log': log.name, 'log_sha256': sha(log),
        })
        if name == 'version' and result.returncode == 0:
            version = log.read_text(encoding='utf-8').strip()
            report['lean_version'] = version
            if 'version 4.33.0' not in version:
                raise RuntimeError(f'Lean version mismatch: {version}')
        report_path.write_text(json.dumps(report, indent=2), encoding='utf-8')
        print(f'{name}: exit {result.returncode}', flush=True)
        if result.returncode:
            return result.returncode
    report['success'] = True
    report['finished_utc'] = now()
    report['artifacts'] = [{'path': path.name, 'sha256': sha(path)} for path in sorted(ROOT.glob('*.olean'))]
    report_path.write_text(json.dumps(report, indent=2), encoding='utf-8')
    return 0

if __name__ == '__main__':
    sys.exit(main())
