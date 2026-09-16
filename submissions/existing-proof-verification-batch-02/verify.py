#!/usr/bin/env python3
"""Validate one published evidence record; optionally reproduce it.

Default: local JSON and published-log checks only, with no subprocess or network.
--execute --mathlib CHECKOUT: use a dedicated, already cached Mathlib checkout.
No toolchain installation, cache download or Lake build command is issued.
New sources live in that checkout; compiled outputs and logs go to a new run
directory outside this published attachment. Python 3.10 or later is required.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import uuid

HERE = Path(__file__).resolve().parent
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
NAME = re.compile(r"[A-Za-z_][A-Za-z_0-9]*(?:\.[A-Za-z_][A-Za-z_0-9]*)*")
HASH256 = re.compile(r"[0-9a-f]{64}")
COMMIT = re.compile(r"[0-9a-f]{40}")
LIBRARY_ROOTS = {"Mathlib", "Lean", "Init", "Std", "Lake", "Batteries", "Aesop",
                 "Qq", "Plausible", "ImportGraph", "ProofWidgets", "LeanSearchClient", "Cli"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def named(value, label: str) -> str:
    require(isinstance(value, str) and NAME.fullmatch(value) is not None,
            f"Unsupported or unsafe Lean name in {label}: {value!r}")
    return value


def hashed(value, label: str) -> str:
    require(isinstance(value, str) and HASH256.fullmatch(value) is not None,
            f"Invalid SHA-256 in {label}")
    return value


def relative_path(value, label: str) -> str:
    require(isinstance(value, str) and bool(value), f"Missing {label}")
    path = PurePosixPath(value)
    require(not path.is_absolute() and str(path) == value and
            all(p not in {".", ".."} for p in path.parts) and
            not any(c in value for c in ("\\", ":", "\0")),
            f"Unsafe relative path in {label}: {value!r}")
    return value


def under(root: Path, rel: str) -> Path:
    target = root / relative_path(rel, "file path")
    require(target.resolve().is_relative_to(root.resolve()), f"Path escapes its root: {rel}")
    return target


def unique_list(value, label: str) -> list:
    require(isinstance(value, list) and all(isinstance(x, str) for x in value),
            f"{label} must be a list of strings")
    require(len(value) == len(set(value)), f"Duplicate {label}")
    return value


def pinned_urls(row: dict) -> None:
    raw = urllib.parse.urlsplit(row["raw_url"])
    view = urllib.parse.urlsplit(row["source_url"])
    require(raw.scheme == "https" and raw.netloc == "raw.githubusercontent.com" and
            not raw.query and not raw.fragment, "Raw source URL must be pinned GitHub HTTPS")
    parts = raw.path.lstrip("/").split("/")
    require(len(parts) >= 4 and COMMIT.fullmatch(parts[2]) is not None and
            all(p and p not in {".", ".."} for p in parts), "Raw URL needs a full commit and path")
    require(view.scheme == "https" and view.netloc == "github.com" and not view.query and
            view.path == "/" + "/".join(parts[:2] + ["blob"] + parts[2:]),
            "Source and raw URLs disagree")
    require(raw.path.endswith("/" + row["path"]), "Remote path does not match the recorded module")


def parse_axioms(text: str, names: list[str]) -> tuple[dict, dict]:
    """Normalize universe arguments without splitting commas inside .{u, v}."""
    parsed, raw = {}, {}
    pattern = r"'([^']+)' (?:depends on axioms:\s*\[([^]]*)\]|does not depend on any axioms)"
    for match in re.finditer(pattern, text, re.S):
        name, body = match[1], match[2]
        if name not in names:
            continue
        atoms = []
        for token in re.split(r",\s*(?![^{}]*\})", body or ""):
            if not token.strip():
                continue
            atom = re.fullmatch(
                r"([A-Za-z_][A-Za-z_0-9]*(?:\.[A-Za-z_][A-Za-z_0-9]*)*)(?:\.\{[^{}]+\})?",
                token.strip())
            require(atom is not None, f"Malformed axiom token for {name}: {token!r}")
            atoms.append(atom[1])
        require(len(atoms) == len(set(atoms)), f"Repeated axiom in report for {name}")
        require(set(atoms) <= ALLOWED_AXIOMS, f"Nonstandard axioms for {name}: {atoms}")
        require(name not in parsed or parsed[name] == atoms, f"Conflicting axiom reports for {name}")
        parsed[name], raw[name] = atoms, match[0]
    for name in names:
        require(name in parsed, f"Missing axiom report for {name}")
    return {name: parsed[name] for name in names}, {name: raw[name] for name in names}


def expected_selection(record: dict) -> set[str]:
    target = record["target_module"]
    return {s["module"] for s in record["sources"]
            if s["module"] == target or s["module"].startswith(target + ".")}


def parse_selection(text: str, record: dict) -> list[str]:
    modules = re.findall(r"(?m)^replaying ([A-Za-z_0-9.]+)\s*$", text)
    require(len(modules) == len(set(modules)) and set(modules) == expected_selection(record),
            f"Checker selection differs from the target/descendant closure: {modules}")
    return modules


def validate_record(record: dict, entry_dir: Path) -> dict:
    """Validate schema and published log bytes; never run Lean or access network."""
    require(isinstance(record, dict) and type(record.get("schema_version")) is int and
            record["schema_version"] == 1, "Unsupported schema")
    require(isinstance(record.get("jsp"), str) and re.fullmatch(r"JSP-\d{6}", record["jsp"]), "Invalid JSP ID")
    require(type(record.get("erdos")) is int and record["erdos"] > 0, "Invalid Erdős number")
    for field in ("title", "scope", "attribution"):
        require(isinstance(record.get(field), str) and bool(record[field].strip()), f"Missing {field}")
    target = named(record.get("target_module"), "target_module")
    main = named(record.get("main_theorem"), "main_theorem")
    names = unique_list(record.get("theorems"), "theorems")
    require(names and main in names, "Main theorem must be audited")
    for name in names:
        named(name, "theorems")
    environment = record["environment"]
    require(isinstance(environment, dict), "Missing environment")
    require(re.fullmatch(r"leanprover/lean4:v\d+\.\d+\.\d+", environment["lean_toolchain"]), "Expected a release toolchain")
    require(COMMIT.fullmatch(environment["mathlib_commit"]), "Mathlib must use a full commit")
    require(environment["LEAN_NUM_THREADS"] == "1", "Evidence must record one Lean thread")
    require(environment["compile_flags"] == ["-j1", "-M8192"], "Unsupported compile flags")
    require(isinstance(environment["platform"], str) and environment["platform"], "Missing original platform")
    sources = record["sources"]
    require(isinstance(sources, list) and sources, "No source closure")
    modules = [named(s["module"], "source module") for s in sources]
    require(len(modules) == len(set(modules)) and target in modules, "Duplicate or missing target module")
    known, seen, dependencies = set(modules), set(), {}
    for row in sources:
        module = row["module"]
        require(relative_path(row["path"], "source path") == module.replace(".", "/") + ".lean",
                f"Module/path mismatch: {module}")
        hashed(row["sha256"], "source")
        pinned_urls(row)
        imports = unique_list(row["imports"], "imports")
        dependencies[module] = []
        for imported in imports:
            named(imported, "import")
            if imported in known:
                require(imported in seen, f"Sources are not topologically ordered: {module} -> {imported}")
                dependencies[module].append(imported)
            else:
                require(imported.split(".")[0] in LIBRARY_ROOTS, f"Incomplete custom closure: {imported}")
        seen.add(module)
    reachable, todo = set(), [target]
    while todo:
        module = todo.pop()
        if module not in reachable:
            reachable.add(module)
            todo.extend(dependencies[module])
    require(reachable == known, "Sources include modules outside the target dependency closure")
    verification = record["verification"]
    require(verification["status"] == "verified_unchanged_source" and
            verification["source_bytes_unchanged"] is True, "Entry does not record unchanged-source success")
    require(set(verification["axioms"]) == set(names), "Recorded axiom theorem list differs")
    for name, atoms in verification["axioms"].items():
        require(set(unique_list(atoms, "axioms")) <= ALLOWED_AXIOMS, f"Nonstandard recorded axioms: {name}")
    selected = unique_list(verification["checker_selected_modules"], "checker selection")
    require(set(selected) == expected_selection(record), "Recorded checker scope differs")
    events = verification["events"]
    require(isinstance(events, list) and [e["stage"] for e in events] ==
            ["compile"] * len(sources) + ["audit", "leanchecker"], "Wrong or incomplete verification stages")
    require([e["module"] for e in events[:-2]] == modules and events[-1]["module"] == target,
            "Compile/checker event modules differ from the source closure")
    named(events[-2]["module"], "audit module")
    logs, paths = {}, set()
    for event in events:
        require(type(event["exit_code"]) is int and event["exit_code"] == 0, "A recorded stage failed")
        seconds = event["seconds"]
        require(type(seconds) in (float, int) and math.isfinite(seconds) and seconds >= 0, "Invalid duration")
        path = under(entry_dir, event["log"])
        require(path.is_file(), f"Missing published log: {path}")
        require(path.resolve() not in paths, "A log path is reused for multiple stages")
        paths.add(path.resolve())
        data = path.read_bytes()
        require(sha(data) == hashed(event["log_sha256"], "published log"), f"Published log hash mismatch: {path}")
        original = hashed(event["original_log_sha256"], "original log")
        redactions = event["redactions"]
        require(isinstance(redactions, list), "Redactions must be listed")
        if not redactions:
            require(original == event["log_sha256"], "Unredacted log has differing original/published hashes")
        logs[event["stage"]] = data.decode("utf-8")
    actual_axioms, _ = parse_axioms(logs["audit"], names)
    require(actual_axioms == verification["axioms"], "Published audit differs from the recorded axiom sets")
    require(parse_selection(logs["leanchecker"], record) == selected, "Actual checker log order differs")
    require(isinstance(verification["limits"], list) and verification["limits"], "Verification limits must be recorded")
    return {"status": "metadata_and_published_logs_valid", "jsp": record["jsp"],
            "erdos": record["erdos"], "custom_sources": len(sources), "audited_theorems": len(names),
            "replayed_modules_recorded": len(selected), "lean_invoked": False,
            "limit": "Checks internal evidence consistency; does not itself reproduce the proof or establish mathematical scope."}


def clean_lean(text: str) -> str:
    """Remove nested comments and string contents for import/marker scanning."""
    out, i, depth, quoted = [], 0, 0, False
    while i < len(text):
        if depth:
            if text.startswith("/-", i):
                depth += 1
                out.extend("  ")
                i += 2
            elif text.startswith("-/", i):
                depth -= 1
                out.extend("  ")
                i += 2
            else:
                out.append("\n" if text[i] == "\n" else " ")
                i += 1
        elif quoted:
            if text[i] == "\\":
                out.extend("  ")
                i += 2
            else:
                quoted = text[i] != '"'
                out.append("\n" if text[i] == "\n" else " ")
                i += 1
        elif text.startswith("--", i):
            end = text.find("\n", i)
            end = len(text) if end < 0 else end
            out.extend(" " * (end - i))
            i = end
        elif text.startswith("/-", i):
            depth, i = 1, i + 2
            out.extend("  ")
        elif text[i] == '"':
            quoted, i = True, i + 1
            out.append(" ")
        else:
            out.append(text[i])
            i += 1
    require(not depth and not quoted, "Unterminated Lean comment or string")
    return "".join(out)


def validate_source(data: bytes, row: dict) -> None:
    require(sha(data) == row["sha256"], f"Source hash mismatch: {row['module']}")
    if "bytes" in row:
        require(len(data) == row["bytes"], f"Source length mismatch: {row['module']}")
    clean = clean_lean(data.decode("utf-8-sig"))
    imports = []
    for match in re.finditer(r"(?m)^\s*(?:(?:public|private)\s+)?import\s+(?:all\s+)?([^\n]+)", clean):
        imports.extend(re.findall(NAME.pattern, match[1]))
    require(imports == row["imports"], f"Actual imports differ from manifest: {row['module']}")
    require(not re.search(r"\b(?:sorry|admit|axiom|native_decide|unsafe|implemented_by)\b", clean),
            f"Unapproved proof marker in source: {row['module']}")


def write_exact(path: Path, data: bytes) -> None:
    if path.exists():
        require(path.is_file() and path.read_bytes() == data, f"Existing file differs: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(data)


def write_json(path: Path, data: dict) -> None:
    path.write_bytes((json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))


def release_matches(text: str, toolchain: str) -> bool:
    release = toolchain.rsplit(":v", 1)[1]
    return re.search(r"\bversion\s+" + re.escape(release) + r"(?:[,\s])", text) is not None


def execute(record: dict, entry_file: Path, work: Path, requested_output: Path | None) -> Path:
    work = work.resolve()
    require(work.is_dir() and not work.is_relative_to(HERE), "Use a dedicated checkout outside the published attachment")
    env = os.environ.copy()
    env["LEAN_NUM_THREADS"] = "1"  # Set before every possible Lean/Lake child.
    pinned = record["environment"]
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=work, env=env, text=True).strip()
    require(head == pinned["mathlib_commit"], "Mathlib HEAD is not the pinned commit")
    require((work / "lean-toolchain").read_text(encoding="utf-8").strip() == pinned["lean_toolchain"],
            "Mathlib toolchain differs from the record")
    require((work / ".lake/build/lib/lean/Mathlib.olean").is_file(), "Install the pinned Mathlib cache first")
    # Ask Lake for its local environment once. All proof stages use direct tools
    # with our isolated build directory first in LEAN_PATH; no `lake build` runs.
    probe = "import json,os; print(json.dumps({k:os.environ.get(k,'') for k in ['PATH','LEAN_PATH','LEAN_SYSROOT']}))"
    output = subprocess.check_output(["lake", "env", sys.executable, "-c", probe], cwd=work, env=env, text=True)
    lake_env = json.loads(output)
    env.update({k: v for k, v in lake_env.items() if v})
    env["LEAN_NUM_THREADS"] = "1"
    lean = shutil.which("lean", path=env["PATH"])
    checker = shutil.which("leanchecker", path=env["PATH"])
    require(lean is not None and checker is not None, "Pinned Lean/checker executables are unavailable")
    require(Path(lean).resolve().parent == Path(checker).resolve().parent,
            "Lean and leanchecker must come from the same toolchain directory")
    version = subprocess.check_output([lean, "--version"], cwd=work, env=env, text=True).strip()
    require(release_matches(version, pinned["lean_toolchain"]), f"Actual Lean version mismatch: {version}")
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
    run_dir = (requested_output or work / ".existing-proof-verification" / (record["jsp"] + "-" + run_id)).resolve()
    require(not run_dir.is_relative_to(HERE) and not run_dir.is_relative_to(entry_file.parent.resolve()),
            "New results must be outside the published attachment")
    run_dir.mkdir(parents=True, exist_ok=False)
    build = run_dir / "build"
    build.mkdir()
    env["LEAN_PATH"] = str(build) + os.pathsep + env.get("LEAN_PATH", "")
    result = {"status": "running", "jsp": record["jsp"], "erdos": record["erdos"],
              "evidence_sha256": sha(entry_file.read_bytes()), "main_theorem": record["main_theorem"],
              "lean_version": version, "mathlib_commit": head, "LEAN_NUM_THREADS": "1",
              "events": [], "sources": [], "limits": record["verification"]["limits"]}
    result_file = run_dir / "result.json"
    write_json(result_file, result)
    try:
        # Check every pre-existing file before any download or proof compilation.
        for row in record["sources"]:
            path = under(work, row["path"])
            if path.exists():
                require(path.is_file(), f"Source path is not a file: {path}")
                validate_source(path.read_bytes(), row)
        for row in record["sources"]:
            path = under(work, row["path"])
            if path.exists():
                data = path.read_bytes()
            else:
                request = urllib.request.Request(row["raw_url"], headers={"User-Agent": "Lean-evidence-verifier/1"})
                with urllib.request.urlopen(request, timeout=60) as response:
                    data = response.read()
                validate_source(data, row)
                write_exact(path, data)
            validate_source(data, row)
            result["sources"].append({"module": row["module"], "sha256": sha(data)})
        audit_module = "ExistingProofAudit" + record["jsp"].replace("-", "") + uuid.uuid4().hex
        audit_rel = audit_module + ".lean"
        audit = "import " + record["target_module"] + "\n\nset_option pp.universes true\n\n"
        audit += "\n\n".join("#check @" + t + "\n#print axioms " + t for t in record["theorems"]) + "\n"
        write_exact(under(work, audit_rel), audit.encode("utf-8"))
        (run_dir / "audit.lean").write_bytes(audit.encode("utf-8"))
        commands = []
        for row in record["sources"]:
            olean = under(build, row["path"].removesuffix(".lean") + ".olean")
            olean.parent.mkdir(parents=True, exist_ok=True)
            commands.append(("compile", row["module"], [lean, *pinned["compile_flags"], "-o", str(olean), row["path"]]))
        commands.append(("audit", audit_module, [lean, *pinned["compile_flags"], "-o", str(build / (audit_module + ".olean")), audit_rel]))
        commands.append(("leanchecker", record["target_module"], [checker, "--verbose", record["target_module"]]))
        for index, (stage, module, command) in enumerate(commands):
            log = run_dir / f"{index:02d}-{stage}.log"
            start, clock = datetime.now(timezone.utc).isoformat(), time.monotonic()
            print(f"{stage} {module}", flush=True)
            with log.open("wb") as stream:
                process = subprocess.run(command, cwd=work, env=env, stdout=stream, stderr=subprocess.STDOUT)
            event = {"stage": stage, "module": module, "command": command, "exit_code": process.returncode,
                     "seconds": round(time.monotonic() - clock, 3), "started": start,
                     "finished": datetime.now(timezone.utc).isoformat(), "log": log.name,
                     "log_sha256": sha(log.read_bytes()), "LEAN_NUM_THREADS": "1"}
            result["events"].append(event)
            write_json(result_file, result)
            require(process.returncode == 0, f"{stage} failed; see {log}")
            if stage == "audit":
                result["axioms"], result["axioms_raw_printed"] = parse_axioms(log.read_text(encoding="utf-8"), record["theorems"])
            elif stage == "leanchecker":
                result["checker_selected_modules"] = parse_selection(log.read_text(encoding="utf-8"), record)
            write_json(result_file, result)
        for row in record["sources"]:
            validate_source(under(work, row["path"]).read_bytes(), row)
        result["status"] = "verified_unchanged_source"
        result["source_bytes_unchanged"] = True
        result["final_source_hashes_match"] = True
        write_json(result_file, result)
    except Exception as error:
        result["status"], result["error"] = "failed", str(error)
        write_json(result_file, result)
        raise
    return result_file


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entry", type=Path, required=True, help="One entries/JSP-NNNNNN/evidence.json")
    parser.add_argument("--execute", action="store_true", help="Actually download pinned sources and run Lean/checker")
    parser.add_argument("--mathlib", type=Path, help="Dedicated pinned Mathlib checkout with cache already installed")
    parser.add_argument("--output", type=Path, help="New run directory outside this attachment; must not exist")
    args = parser.parse_args()
    if args.execute and args.mathlib is None:
        parser.error("--execute requires --mathlib")
    if not args.execute and (args.mathlib is not None or args.output is not None):
        parser.error("--mathlib and --output apply only with --execute")
    entry = args.entry.resolve()
    record = json.loads(entry.read_text(encoding="utf-8-sig"))
    report = validate_record(record, entry.parent)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if args.execute:
        result = execute(record, entry, args.mathlib, args.output)
        print("Reproduction passed. New evidence: " + str(result))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, TypeError, OSError, subprocess.SubprocessError) as error:
        print("Verification failed: " + str(error), file=sys.stderr)
        raise SystemExit(1)
