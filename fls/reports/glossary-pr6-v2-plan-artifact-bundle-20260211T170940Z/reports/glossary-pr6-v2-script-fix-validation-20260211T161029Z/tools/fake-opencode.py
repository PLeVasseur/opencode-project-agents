#!/usr/bin/env python3

from __future__ import annotations

import csv
import json
import os
import re
import sys
from pathlib import Path


PARENT_RE = re.compile(r'^- \[[ xX]\] (?P<id>(?:W[ABCD]|QQ)-\d{3})\b')
SUB_RE = re.compile(r'^  - \[[ xX]\] (?P<id>(?:W[ABCD]|QQ)-\d{3})\.(?P<idx>[1-6])\b')


def parse_attached_files(args: list[str]) -> list[Path]:
    paths: list[Path] = []
    index = 0
    while index < len(args):
        if args[index] == "--file" and index + 1 < len(args):
            paths.append(Path(args[index + 1]))
            index += 2
            continue
        index += 1
    return paths


def find_path(paths: list[Path], filename: str) -> Path:
    for path in paths:
        if path.name == filename:
            return path
    raise RuntimeError(f"Attached file not found: {filename}")


def mark_checklist_ids(path: Path, ids: set[str]) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    updated: list[str] = []
    for line in lines:
        parent_match = PARENT_RE.match(line)
        if parent_match and parent_match.group("id") in ids:
            line = re.sub(r"^- \[[ xX]\]", "- [x]", line, count=1)
        sub_match = SUB_RE.match(line)
        if sub_match and sub_match.group("id") in ids:
            line = re.sub(r"^  - \[[ xX]\]", "  - [x]", line, count=1)
        updated.append(line)
    path.write_text("\n".join(updated) + "\n", encoding="utf-8")


def update_ledger_ids(path: Path, ids: set[str]) -> None:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)

    for row in rows:
        checklist_id = (row.get("checklist_id") or "").strip()
        if checklist_id not in ids:
            continue
        row["action_type"] = "move"
        row["decision_detail"] = "Moved to conceptual owner location for fixture validation."
        row["reason_code"] = "relocate-conceptual-owner"
        row["reason_why"] = (
            f"{checklist_id} fixture rationale: ownership and discoverability improve at the target "
            "location while keeping Rust 2021 semantics unchanged and traceable."
        )
        row["reason_quality"] = "pass"
        row["semantic_change_flag"] = "none"
        row["review_attention"] = "none"
        row["after_file"] = "src/glossary.rst"
        row["after_line"] = "10"
        row["after_dp_id"] = f"dp-after-{checklist_id.lower()}"
        row["after_section"] = "Fixture Section"
        row["after_commit"] = "fixture-precommit"
        row["phase1_status"] = "completed"
        row["final_quality"] = "resolved-high"

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def emit_session() -> None:
    print(json.dumps({"type": "done", "sessionID": "fake-session"}))


def handle_run(args: list[str]) -> int:
    mode = os.environ.get("FAKE_OPENCODE_MODE", "no-change")
    attached = parse_attached_files(args)
    checklist_path = find_path(attached, "manual-placement-checklist-v2.md")
    ledger_path = find_path(attached, "manual-placement-ledger-v2.csv")

    if mode == "no-change":
        emit_session()
        return 0

    if mode == "pass-first":
        target_ids = {"WA-001"}
        mark_checklist_ids(checklist_path, target_ids)
        update_ledger_ids(ledger_path, target_ids)
        emit_session()
        return 0

    if mode == "out-of-scope":
        target_ids = {"WA-001", "WA-002"}
        mark_checklist_ids(checklist_path, target_ids)
        update_ledger_ids(ledger_path, target_ids)
        emit_session()
        return 0

    raise RuntimeError(f"Unsupported FAKE_OPENCODE_MODE: {mode}")


def handle_session_list() -> int:
    print("[]")
    return 0


def main() -> int:
    args = sys.argv[1:]
    if not args:
        raise RuntimeError("No command provided")
    if args[0] == "run":
        return handle_run(args[1:])
    if args[0] == "session" and len(args) > 1 and args[1] == "list":
        return handle_session_list()
    raise RuntimeError(f"Unsupported fake opencode command: {' '.join(args)}")


if __name__ == "__main__":
    raise SystemExit(main())
