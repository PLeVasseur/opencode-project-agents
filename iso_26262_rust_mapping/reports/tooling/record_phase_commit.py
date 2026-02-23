#!/usr/bin/env python3
"""Append/update phased commit entries for durable migration runs.

Usage:
  python3 record_phase_commit.py \
    --run-root <run-root> \
    --stage-checkpoint <M2|M3|...> \
    [--repo-root <repo-root>] \
    [--commit-sha <sha>] \
    [--subject "<subject>"]

Behavior:
  - Reads `state.env` in run root for `COMMIT_LEDGER_FILE` and
    `COMMIT_LEDGER_JSON_FILE`.
  - Resolves commit SHA/subject from git when omitted.
  - Appends one row to markdown ledger and one entry to JSON ledger.
  - Idempotent on `(stage_checkpoint, commit_sha)`.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
import sys
from pathlib import Path


def parse_env(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    if not path.exists():
        return data

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith('"') and value.endswith('"') and len(value) >= 2:
            try:
                value = bytes(value[1:-1], "utf-8").decode("unicode_escape")
            except Exception:
                value = value[1:-1]
        data[key] = value
    return data


def _git_value(repo_root: Path, args: list[str]) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=str(repo_root),
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def _load_json(path: Path) -> dict:
    if not path.exists():
        return {"schema_version": 1, "entries": []}
    with path.open("r", encoding="utf-8") as fh:
        value = json.load(fh)
    if not isinstance(value, dict):
        return {"schema_version": 1, "entries": []}
    value.setdefault("schema_version", 1)
    value.setdefault("entries", [])
    return value


def _write_json(path: Path, value: dict) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def _append_md_row(md_path: Path, stage_checkpoint: str, commit_sha: str, subject: str, timestamp_utc: str) -> None:
    md_path.parent.mkdir(parents=True, exist_ok=True)
    if not md_path.exists():
        md_path.write_text(
            "\n".join(
                [
                    "# Commit Ledger",
                    "",
                    "| stage_checkpoint | commit_sha | subject | timestamp_utc |",
                    "| --- | --- | --- | --- |",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

    row = f"| {stage_checkpoint} | {commit_sha} | {subject.replace('|', '\\|')} | {timestamp_utc} |\n"
    with md_path.open("a", encoding="utf-8") as fh:
        fh.write(row)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Record phased commit checkpoint for durable migration run")
    parser.add_argument("--run-root", required=True)
    parser.add_argument("--stage-checkpoint", required=True)
    parser.add_argument("--repo-root", default="")
    parser.add_argument("--commit-sha", default="")
    parser.add_argument("--subject", default="")
    parser.add_argument("--timestamp-utc", default="")
    args = parser.parse_args(argv)

    run_root = Path(args.run_root).resolve()
    state_path = run_root / "state.env"
    if not state_path.exists():
        print(f"error: missing state file: {state_path}", file=sys.stderr)
        return 2

    state = parse_env(state_path)
    repo_root = Path(args.repo_root or state.get("REPO_ROOT", "")).resolve()
    if not str(repo_root):
        print("error: repo root is not available", file=sys.stderr)
        return 2

    commit_sha = args.commit_sha or _git_value(repo_root, ["rev-parse", "HEAD"])
    subject = args.subject or _git_value(repo_root, ["log", "-1", "--format=%s"])
    timestamp_utc = args.timestamp_utc or dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    md_path = Path(state.get("COMMIT_LEDGER_FILE", run_root / "artifacts" / "commits" / "commit-ledger.md"))
    json_path = Path(state.get("COMMIT_LEDGER_JSON_FILE", run_root / "artifacts" / "commits" / "commit-ledger.json"))

    ledger = _load_json(json_path)
    entries = ledger.setdefault("entries", [])
    existing = any(
        isinstance(item, dict)
        and item.get("stage_checkpoint") == args.stage_checkpoint
        and item.get("commit_sha") == commit_sha
        for item in entries
    )

    if existing:
        print("already-recorded")
        print(f"stage_checkpoint={args.stage_checkpoint}")
        print(f"commit_sha={commit_sha}")
        return 0

    entry = {
        "stage_checkpoint": args.stage_checkpoint,
        "commit_sha": commit_sha,
        "subject": subject,
        "timestamp_utc": timestamp_utc,
    }
    entries.append(entry)
    _write_json(json_path, ledger)
    _append_md_row(md_path, args.stage_checkpoint, commit_sha, subject, timestamp_utc)

    print(f"stage_checkpoint={args.stage_checkpoint}")
    print(f"commit_sha={commit_sha}")
    print(f"subject={subject}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
