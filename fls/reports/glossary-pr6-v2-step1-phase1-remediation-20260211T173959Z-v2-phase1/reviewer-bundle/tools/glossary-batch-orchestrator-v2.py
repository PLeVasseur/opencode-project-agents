#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PARENT_RE = re.compile(
    r'^- \[(?P<mark>[ xX])\] (?P<id>(?:W[ABCD]|QQ)-\d{3}) (?P<rest>.+)$'
)
TERM_RE = re.compile(r'term="(?P<term>[^"]+)"')
SUB_RE = re.compile(
    r'^  - \[(?P<mark>[ xX])\] (?P<id>(?:W[ABCD]|QQ)-\d{3})\.(?P<idx>[1-6])\b'
)

ALLOWED_REASON_CODES = {
    "relocate-conceptual-owner",
    "relocate-first-use-owner",
    "retain-conceptual-owner",
    "retain-reordered",
    "retain-link-mitigated",
    "no-change-not-mislocated",
    "blocked",
}

ALLOWED_ACTION_TYPES = {
    "move",
    "rewrite",
    "move+rewrite",
    "retain",
    "retain+rewrite",
}


@dataclass
class ChecklistItem:
    checklist_id: str
    term: str
    parent_checked: bool
    sub_checks: dict[int, bool]

    @property
    def wave(self) -> str:
        return self.checklist_id.split("-", 1)[0]


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def normalize_path(path: Path) -> Path:
    return path.expanduser().resolve()


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def run_command(
    args: list[str],
    *,
    cwd: Path,
    env: dict[str, str] | None = None,
    description: str,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        args,
        cwd=str(cwd),
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    if check and result.returncode != 0:
        raise RuntimeError(
            f"{description} failed (exit {result.returncode})\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )
    return result


def run_shell_command(command: str, *, cwd: Path, description: str) -> None:
    result = subprocess.run(
        ["bash", "-lc", command],
        cwd=str(cwd),
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"{description} failed (exit {result.returncode})\n"
            f"command: {command}\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )


def ensure_exists(path: Path, *, kind: str) -> None:
    if kind == "file" and not path.is_file():
        raise RuntimeError(f"Required file not found: {path}")
    if kind == "dir" and not path.is_dir():
        raise RuntimeError(f"Required directory not found: {path}")


def parse_checklist_id(value: str) -> tuple[int, int, str]:
    prefix, number = value.split("-", 1)
    order = {"WA": 1, "WB": 2, "WC": 3, "WD": 4, "QQ": 5}
    return (order.get(prefix, 99), int(number), value)


def parse_checklist(path: Path) -> dict[str, ChecklistItem]:
    items: dict[str, ChecklistItem] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        parent_match = PARENT_RE.match(line)
        if parent_match:
            checklist_id = parent_match.group("id")
            term_match = TERM_RE.search(parent_match.group("rest"))
            term = term_match.group("term") if term_match else ""
            items[checklist_id] = ChecklistItem(
                checklist_id=checklist_id,
                term=term,
                parent_checked=parent_match.group("mark").lower() == "x",
                sub_checks={index: False for index in range(1, 7)},
            )
            continue

        sub_match = SUB_RE.match(line)
        if sub_match:
            checklist_id = sub_match.group("id")
            sub_index = int(sub_match.group("idx"))
            item = items.get(checklist_id)
            if item is None:
                continue
            item.sub_checks[sub_index] = sub_match.group("mark").lower() == "x"

    return items


def checklist_rows_by_key(path: Path) -> dict[tuple[str, int], str]:
    rows: dict[tuple[str, int], str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        parent_match = PARENT_RE.match(line)
        if parent_match:
            rows[(parent_match.group("id"), 0)] = line
            continue
        sub_match = SUB_RE.match(line)
        if sub_match:
            rows[(sub_match.group("id"), int(sub_match.group("idx")))] = line
    return rows


def read_ledger_rows(path: Path) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return {row["checklist_id"]: row for row in reader}


def write_ledger_rows(path: Path, rows_by_id: dict[str, dict[str, str]]) -> None:
    if not rows_by_id:
        raise RuntimeError(f"Ledger is empty: {path}")
    fieldnames = list(next(iter(rows_by_id.values())).keys())
    ordered_ids = sorted(rows_by_id.keys(), key=parse_checklist_id)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for checklist_id in ordered_ids:
            writer.writerow(rows_by_id[checklist_id])


def load_state(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    return load_json(path)


def save_state(path: Path, state: dict[str, Any]) -> None:
    state["updated_at"] = utc_timestamp()
    write_json(path, state)


def git_branch(workdir: Path) -> str:
    result = run_command(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=workdir,
        description="resolve current branch",
    )
    return result.stdout.strip()


def git_status_porcelain(workdir: Path) -> list[str]:
    result = run_command(
        ["git", "status", "--porcelain"],
        cwd=workdir,
        description="collect git status",
    )
    return [line for line in result.stdout.splitlines() if line.strip()]


def latest_session_id(opencode_bin: str, *, workdir: Path, env: dict[str, str]) -> str | None:
    result = run_command(
        [opencode_bin, "session", "list", "--format", "json", "-n", "20"],
        cwd=workdir,
        env=env,
        description="query latest opencode sessions",
        check=False,
    )
    if result.returncode != 0:
        return None
    try:
        sessions = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None
    workdir_resolved = workdir.resolve()
    for session in sessions:
        directory = session.get("directory")
        if directory and Path(directory).resolve() == workdir_resolved:
            return session.get("id")
    if sessions:
        return sessions[0].get("id")
    return None


def remediation_dir_from_args(args: argparse.Namespace) -> tuple[str, Path]:
    if args.remediation_dir is not None:
        remediation_dir = args.remediation_dir
        run_id = remediation_dir.name.rsplit("-", 1)[-1]
        remediation_dir.mkdir(parents=True, exist_ok=True)
        return run_id, remediation_dir
    run_id = args.run_id or utc_timestamp()
    remediation_dir = args.config_dir / "reports" / f"glossary-pr6-v2-step1-phase1-remediation-{run_id}"
    remediation_dir.mkdir(parents=True, exist_ok=True)
    return run_id, remediation_dir


def bootstrap_run_artifacts(
    *,
    remediation_dir: Path,
    checklist_template: Path,
    seed_ledger: Path,
    baseline_reference: Path,
    reason_rubric: Path,
) -> tuple[Path, Path, Path, Path]:
    checklist_path = remediation_dir / "manual-placement-checklist-v2.md"
    ledger_path = remediation_dir / "manual-placement-ledger-v2.csv"
    baseline_path = remediation_dir / "manual-placement-baseline-reference-v2.csv"
    rubric_path = remediation_dir / "reason-rubric-v2.md"

    if not checklist_path.exists():
        shutil.copy2(checklist_template, checklist_path)
    if not ledger_path.exists():
        shutil.copy2(seed_ledger, ledger_path)
    if not baseline_path.exists():
        shutil.copy2(baseline_reference, baseline_path)
    if not rubric_path.exists():
        shutil.copy2(reason_rubric, rubric_path)

    return checklist_path, ledger_path, baseline_path, rubric_path


def update_quarantine_queue(
    queue_path: Path,
    *,
    ids: list[str],
    reason: str,
    batch_number: int,
    wave: str,
) -> None:
    queue: list[dict[str, Any]] = []
    if queue_path.is_file():
        queue = load_json(queue_path).get("items", [])

    existing_ids = {item.get("checklist_id") for item in queue if item.get("status") == "open"}
    for checklist_id in ids:
        if checklist_id in existing_ids:
            continue
        queue.append(
            {
                "checklist_id": checklist_id,
                "wave": wave,
                "status": "open",
                "reason": reason,
                "first_batch": batch_number,
                "updated_at": utc_timestamp(),
            }
        )

    write_json(queue_path, {"items": queue})


def open_quarantine_ids(queue_path: Path) -> set[str]:
    if not queue_path.is_file():
        return set()
    data = load_json(queue_path)
    return {
        item.get("checklist_id")
        for item in data.get("items", [])
        if item.get("status") == "open" and item.get("checklist_id")
    }


def select_active_wave(items: dict[str, ChecklistItem], skip_ids: set[str]) -> str | None:
    for wave in ["WA", "WB", "WC", "WD"]:
        has_unchecked = any(
            item.wave == wave and (not item.parent_checked) and item.checklist_id not in skip_ids
            for item in items.values()
        )
        if has_unchecked:
            return wave
    return None


def choose_batch(
    items: dict[str, ChecklistItem],
    *,
    wave: str,
    batch_size: int,
    skip_ids: set[str],
) -> list[ChecklistItem]:
    candidates = [
        item
        for item in items.values()
        if item.wave == wave and (not item.parent_checked) and item.checklist_id not in skip_ids
    ]
    candidates.sort(key=lambda item: parse_checklist_id(item.checklist_id))
    return candidates[:batch_size]


def run_validator(
    *,
    validator_path: Path,
    mode: str,
    checklist_path: Path,
    ledger_path: Path,
    baseline_path: Path,
    json_out: Path,
    markdown_out: Path,
    expected_parent_count: int | None = None,
) -> None:
    args = [
        "python3",
        str(validator_path),
        "--mode",
        mode,
        "--checklist",
        str(checklist_path),
        "--ledger",
        str(ledger_path),
        "--baseline",
        str(baseline_path),
        "--json-out",
        str(json_out),
        "--markdown-out",
        str(markdown_out),
    ]
    if expected_parent_count is not None:
        args.extend(["--expected-parent-count", str(expected_parent_count)])
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(
            f"validator failed in mode={mode} (exit {result.returncode})\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )


def run_opencode_batch(
    *,
    opencode_bin: str,
    workdir: Path,
    prompt: str,
    log_path: Path,
    session_id: str | None,
    attach_url: str | None,
    model: str | None,
    agent: str | None,
    title: str,
    attached_files: list[Path],
    permission_override: str | None,
    stream_output: bool,
) -> str:
    args = [opencode_bin, "run", "--format", "json", prompt]
    if attach_url:
        args.extend(["--attach", attach_url])
    if session_id:
        args.extend(["--session", session_id])
    else:
        args.extend(["--title", title])
    if model:
        args.extend(["--model", model])
    if agent:
        args.extend(["--agent", agent])
    for path in attached_files:
        args.extend(["--file", str(path)])

    env = os.environ.copy()
    if permission_override:
        env.setdefault("OPENCODE_PERMISSION", permission_override)

    log_path.parent.mkdir(parents=True, exist_ok=True)
    discovered_session = session_id
    error_events: list[str] = []

    with log_path.open("w", encoding="utf-8") as log_handle:
        process = subprocess.Popen(
            args,
            cwd=str(workdir),
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        assert process.stdout is not None
        for line in process.stdout:
            if stream_output:
                sys.stdout.write(line)
            log_handle.write(line)
            try:
                payload = json.loads(line)
            except json.JSONDecodeError:
                continue
            if payload.get("type") == "error":
                error = payload.get("error", {})
                message = (
                    error.get("data", {}).get("message")
                    or error.get("message")
                    or str(error)
                )
                error_events.append(message)
            current_session = payload.get("sessionID")
            if current_session:
                discovered_session = current_session

        return_code = process.wait()

    if return_code != 0:
        raise RuntimeError(f"opencode run failed with exit code {return_code}; see {log_path}")
    if error_events:
        raise RuntimeError(f"opencode emitted error event(s): {error_events[0]}; see {log_path}")
    if discovered_session:
        return discovered_session
    fallback = latest_session_id(opencode_bin, workdir=workdir, env=env)
    if fallback:
        return fallback
    raise RuntimeError("Could not determine OpenCode session ID after batch run")


def build_batch_prompt(
    *,
    batch_items: list[ChecklistItem],
    wave: str,
    plan_path: Path,
    checklist_path: Path,
    ledger_path: Path,
    baseline_path: Path,
    rubric_path: Path,
    validator_path: Path,
    remediation_dir: Path,
    workdir: Path,
    expected_branch: str,
    batch_number: int,
) -> str:
    ids = ", ".join(item.checklist_id for item in batch_items)
    terms = "\n".join(f"- {item.checklist_id}: {item.term}" for item in batch_items)
    return f"""Execute the v2 glossary remediation plan for this wave batch only.

Context:
- Worktree: `{workdir}`
- Expected branch: `{expected_branch}`
- Wave: `{wave}`
- Plan: `{plan_path}`
- Checklist: `{checklist_path}`
- Ledger: `{ledger_path}`
- Baseline reference: `{baseline_path}`
- Reason rubric: `{rubric_path}`
- Validator: `{validator_path}`
- Remediation directory: `{remediation_dir}`
- Batch number: `{batch_number}`

Batch scope (exact IDs only): {ids}

Terms:
{terms}

Required workflow:
1. Process each listed term manually, one by one.
2. Apply step1 spec edits as needed.
3. Update only these term rows in checklist and ledger.
4. For each completed term, ensure checklist sub-items `.1`..`.6` are checked.
5. Ensure ledger fields are complete (`action_type`, `decision_detail`, `reason_*`, `semantic_change_flag`, `review_attention`, after anchors, statuses).
6. Do not commit or push (orchestrator handles commit).
7. Run validator in progress mode before responding:
   `python3 "{validator_path}" --mode progress --checklist "{checklist_path}" --ledger "{ledger_path}" --baseline "{baseline_path}" --json-out "{remediation_dir}/batch-{batch_number:03d}-validate-progress.json" --markdown-out "{remediation_dir}/checklist-progress.md"`

Response format:
- Completed IDs
- Quarantined IDs (if any)
- Files changed
- Any blockers (if none, say "none")
"""


def validate_term_row(item: ChecklistItem, row: dict[str, str]) -> str | None:
    if not item.parent_checked:
        return "parent row is not checked"
    for sub_index in range(1, 7):
        if not item.sub_checks.get(sub_index, False):
            return f"sub-item .{sub_index} is not checked"

    action_type = (row.get("action_type") or "").strip()
    decision_detail = (row.get("decision_detail") or "").strip()
    reason_code = (row.get("reason_code") or "").strip()
    reason_quality = (row.get("reason_quality") or "").strip().lower()
    reason_why = (row.get("reason_why") or "").strip()
    semantic_flag = (row.get("semantic_change_flag") or "").strip()
    review_attention = (row.get("review_attention") or "").strip()
    phase1_status = (row.get("phase1_status") or "").strip().lower()
    final_quality = (row.get("final_quality") or "").strip().lower()

    if action_type not in ALLOWED_ACTION_TYPES:
        return f"invalid action_type '{action_type}'"
    if not decision_detail:
        return "missing decision_detail"
    if reason_code not in ALLOWED_REASON_CODES:
        return f"invalid reason_code '{reason_code}'"
    if reason_quality != "pass":
        return "reason_quality must be pass"
    if len(reason_why) < 80:
        return "reason_why shorter than 80 chars"
    if semantic_flag not in {"none", "clarification-only", "normative-risk"}:
        return f"invalid semantic_change_flag '{semantic_flag}'"
    if "rewrite" in action_type and review_attention != "required":
        return "rewrite action requires review_attention=required"
    if reason_code != "blocked":
        for column in ["after_file", "after_line", "after_dp_id"]:
            if not (row.get(column) or "").strip():
                return f"missing {column}"
    if phase1_status in {"", "pending"}:
        return "phase1_status is pending"
    if final_quality in {"", "pending"}:
        return "final_quality is pending"
    return None


def evaluate_batch_results(
    *,
    batch_items: list[ChecklistItem],
    checklist_path: Path,
    ledger_path: Path,
) -> tuple[list[str], dict[str, str]]:
    checklist = parse_checklist(checklist_path)
    ledger_rows = read_ledger_rows(ledger_path)
    passed: list[str] = []
    quarantined: dict[str, str] = {}
    for batch_item in batch_items:
        item = checklist.get(batch_item.checklist_id)
        row = ledger_rows.get(batch_item.checklist_id)
        if item is None:
            quarantined[batch_item.checklist_id] = "missing checklist parent row"
            continue
        if row is None:
            quarantined[batch_item.checklist_id] = "missing ledger row"
            continue
        reason = validate_term_row(item, row)
        if reason is None:
            passed.append(batch_item.checklist_id)
        else:
            quarantined[batch_item.checklist_id] = reason
    return passed, quarantined


def restore_ledger_rows_from_snapshot(
    *,
    ledger_path: Path,
    snapshot_path: Path,
    checklist_ids: list[str],
) -> None:
    current = read_ledger_rows(ledger_path)
    snapshot = read_ledger_rows(snapshot_path)
    for checklist_id in checklist_ids:
        if checklist_id in snapshot:
            current[checklist_id] = snapshot[checklist_id]
    write_ledger_rows(ledger_path, current)


def restore_checklist_rows_from_snapshot(
    *,
    checklist_path: Path,
    snapshot_path: Path,
    checklist_ids: list[str],
) -> None:
    target_ids = set(checklist_ids)

    def line_key(line: str) -> tuple[str, int] | None:
        parent_match = PARENT_RE.match(line)
        if parent_match:
            return (parent_match.group("id"), 0)
        sub_match = SUB_RE.match(line)
        if sub_match:
            return (sub_match.group("id"), int(sub_match.group("idx")))
        return None

    snapshot_lines = snapshot_path.read_text(encoding="utf-8").splitlines()
    snapshot_lookup: dict[tuple[str, int], str] = {}
    for line in snapshot_lines:
        key = line_key(line)
        if key and key[0] in target_ids:
            snapshot_lookup[key] = line

    current_lines = checklist_path.read_text(encoding="utf-8").splitlines()
    updated: list[str] = []
    for line in current_lines:
        key = line_key(line)
        if key and key[0] in target_ids and key in snapshot_lookup:
            updated.append(snapshot_lookup[key])
        else:
            updated.append(line)

    checklist_path.write_text("\n".join(updated) + "\n", encoding="utf-8")


def verify_only_batch_ids_changed(
    *,
    batch_ids: list[str],
    excluded_ids: set[str],
    checklist_before_path: Path,
    checklist_after_path: Path,
    ledger_before_path: Path,
    ledger_after_path: Path,
) -> None:
    allowed_ids = set(batch_ids) | set(excluded_ids)

    def sort_key(value: str) -> tuple[int, int, str]:
        try:
            return parse_checklist_id(value)
        except Exception:  # noqa: BLE001
            return (99, 0, value)

    errors: list[str] = []

    before_checklist = checklist_rows_by_key(checklist_before_path)
    after_checklist = checklist_rows_by_key(checklist_after_path)
    checklist_keys = set(before_checklist.keys()) | set(after_checklist.keys())
    for checklist_id, sub_index in sorted(
        checklist_keys,
        key=lambda value: (*sort_key(value[0]), value[1]),
    ):
        if checklist_id in allowed_ids:
            continue
        before_line = before_checklist.get((checklist_id, sub_index))
        after_line = after_checklist.get((checklist_id, sub_index))
        if before_line == after_line:
            continue
        label = f"{checklist_id}.{sub_index}" if sub_index > 0 else checklist_id
        if before_line is None:
            errors.append(f"{label}: checklist row added outside batch")
        elif after_line is None:
            errors.append(f"{label}: checklist row removed outside batch")
        else:
            errors.append(f"{label}: checklist row changed outside batch")

    before_ledger = read_ledger_rows(ledger_before_path)
    after_ledger = read_ledger_rows(ledger_after_path)
    ledger_ids = set(before_ledger.keys()) | set(after_ledger.keys())
    for checklist_id in sorted(ledger_ids, key=sort_key):
        if checklist_id in allowed_ids:
            continue
        before_row = before_ledger.get(checklist_id)
        after_row = after_ledger.get(checklist_id)
        if before_row == after_row:
            continue
        if before_row is None:
            errors.append(f"{checklist_id}: ledger row added outside batch")
        elif after_row is None:
            errors.append(f"{checklist_id}: ledger row removed outside batch")
        else:
            errors.append(f"{checklist_id}: ledger row changed outside batch")

    if errors:
        preview = errors[:60]
        raise RuntimeError("Unexpected out-of-scope changes:\n- " + "\n- ".join(preview))


def update_ledger_after_commit(
    *, ledger_path: Path, checklist_ids: list[str], commit_hash: str, batch_id: str
) -> None:
    rows = read_ledger_rows(ledger_path)
    for checklist_id in checklist_ids:
        row = rows.get(checklist_id)
        if row is None:
            continue
        row["after_commit"] = commit_hash
        row["batch_id"] = batch_id
        row["quarantine_status"] = ""
        row["quarantine_reason"] = ""
    write_ledger_rows(ledger_path, rows)


def mark_quarantine_in_ledger(
    *, ledger_path: Path, quarantined: dict[str, str], batch_id: str
) -> None:
    rows = read_ledger_rows(ledger_path)
    for checklist_id, reason in quarantined.items():
        row = rows.get(checklist_id)
        if row is None:
            continue
        row["quarantine_status"] = "open"
        row["quarantine_reason"] = reason
        row["batch_id"] = batch_id
    write_ledger_rows(ledger_path, rows)


def git_commit_batch(
    *,
    workdir: Path,
    batch_items: list[ChecklistItem],
    passed_ids: list[str],
    commit_prefix: str,
    allow_empty_commit: bool,
) -> str:
    status_before = git_status_porcelain(workdir)
    if not status_before and not allow_empty_commit:
        raise RuntimeError("No repository changes to commit for this batch")

    run_command(["git", "add", "-A"], cwd=workdir, description="stage batch changes")

    passed_set = set(passed_ids)
    passed_items = [item for item in batch_items if item.checklist_id in passed_set]
    first_id = passed_items[0].checklist_id
    last_id = passed_items[-1].checklist_id
    subject = f"{commit_prefix} {first_id}-{last_id}"
    lines = [f"Batch IDs: {', '.join(passed_ids)}", "", "Terms:"]
    lines.extend(f"- {item.checklist_id}: {item.term}" for item in passed_items)
    body = "\n".join(lines)

    commit_args = ["git", "commit"]
    if allow_empty_commit:
        commit_args.append("--allow-empty")
    commit_args.extend(["-m", subject, "-m", body])
    run_command(commit_args, cwd=workdir, description="create batch commit")

    return run_command(
        ["git", "rev-parse", "HEAD"],
        cwd=workdir,
        description="resolve batch commit hash",
    ).stdout.strip()


def build_defaults(config_dir: Path) -> dict[str, Path]:
    reports_dir = config_dir / "reports"
    plans_dir = config_dir / "plans"
    v2_root = (
        reports_dir
        / "glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z"
    )
    templates = v2_root / "templates"
    return {
        "checklist": templates / "manual-placement-checklist-v2.template.md",
        "seed_ledger": templates / "manual-placement-ledger-v2.template.csv",
        "baseline_reference": templates / "manual-placement-ledger-v2.template.csv",
        "reason_rubric": reports_dir / "glossary-poor-questionable-reason-rubric.md",
        "validator": reports_dir / "validate-ledger-and-checklist-v2.py",
        "manual_plan": plans_dir / "glossary-pr6-v2-step1-phase1-remediation-plan.md",
    }


def parse_args() -> argparse.Namespace:
    opencode_config_dir = os.environ.get("OPENCODE_CONFIG_DIR")
    if not opencode_config_dir:
        raise RuntimeError("OPENCODE_CONFIG_DIR is not set")
    config_dir = normalize_path(Path(opencode_config_dir))
    defaults = build_defaults(config_dir)

    parser = argparse.ArgumentParser(
        description="Run v2 Step1/Phase1 remediation in wave-aware OpenCode batches"
    )
    parser.add_argument(
        "--workdir",
        type=Path,
        default=Path("/home/pete.levasseur/project/fls-wt/step1"),
        help="Target git worktree directory",
    )
    parser.add_argument(
        "--expected-branch",
        default="glossary-step-1-main-text-coverage",
        help="Expected git branch in target worktree",
    )
    parser.add_argument("--batch-size-wa", type=int, default=20)
    parser.add_argument("--batch-size-wb", type=int, default=20)
    parser.add_argument("--batch-size-wc", type=int, default=40)
    parser.add_argument("--batch-size-wd", type=int, default=40)
    parser.add_argument("--max-batches", type=int, default=0)
    parser.add_argument("--run-id")
    parser.add_argument("--remediation-dir", type=Path)
    parser.add_argument("--session-id")
    parser.add_argument("--attach-url")
    parser.add_argument("--model")
    parser.add_argument("--agent")
    parser.add_argument("--opencode-bin", default="opencode")
    parser.add_argument("--checklist", type=Path, default=defaults["checklist"])
    parser.add_argument("--seed-ledger", type=Path, default=defaults["seed_ledger"])
    parser.add_argument("--baseline-reference", type=Path, default=defaults["baseline_reference"])
    parser.add_argument("--reason-rubric", type=Path, default=defaults["reason_rubric"])
    parser.add_argument("--validator", type=Path, default=defaults["validator"])
    parser.add_argument("--manual-plan", type=Path, default=defaults["manual_plan"])
    parser.add_argument("--state-file", type=Path)
    parser.add_argument("--commit-prefix", default="docs(glossary): remediate placement terms")
    parser.add_argument("--allow-dirty", action="store_true")
    parser.add_argument("--allow-empty-commit", action="store_true")
    parser.add_argument("--pause-seconds", type=float, default=0.0)
    parser.add_argument("--extra-check", action="append", default=[])
    parser.add_argument(
        "--permission-override",
        default='{"*":"allow","external_directory":"allow"}',
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-final-validator", action="store_true")
    parser.add_argument("--stream-opencode-output", action="store_true")
    parser.add_argument(
        "--retry-quarantine",
        action="store_true",
        help="Include open quarantine IDs in batch selection",
    )

    args = parser.parse_args()
    args.config_dir = config_dir

    for attr in [
        "workdir",
        "checklist",
        "seed_ledger",
        "baseline_reference",
        "reason_rubric",
        "validator",
        "manual_plan",
    ]:
        setattr(args, attr, normalize_path(getattr(args, attr)))

    if args.remediation_dir is not None:
        args.remediation_dir = normalize_path(args.remediation_dir)
    if args.state_file is not None:
        args.state_file = normalize_path(args.state_file)

    for field in ["batch_size_wa", "batch_size_wb", "batch_size_wc", "batch_size_wd"]:
        if getattr(args, field) <= 0:
            raise RuntimeError(f"--{field.replace('_', '-')} must be greater than zero")
    if args.max_batches < 0:
        raise RuntimeError("--max-batches must be zero or greater")

    return args


def batch_size_for_wave(args: argparse.Namespace, wave: str) -> int:
    return {
        "WA": args.batch_size_wa,
        "WB": args.batch_size_wb,
        "WC": args.batch_size_wc,
        "WD": args.batch_size_wd,
    }[wave]


def required_v3_paths(remediation_dir: Path) -> dict[str, Path]:
    v3_dir = remediation_dir / "inputs" / "v3"
    return {
        "analysis": v3_dir / "fls-pr6-updated-analysis-v3.md",
        "placement": v3_dir / "fls-pr6-placement-fitness-v3.json",
        "divergence": v3_dir / "fls-pr6-definition-divergence-v3.json",
    }


def v3_available(remediation_dir: Path) -> tuple[bool, list[str]]:
    required = required_v3_paths(remediation_dir)
    missing = [str(path) for path in required.values() if not path.is_file()]
    return (len(missing) == 0, missing)


def main() -> int:
    args = parse_args()

    for path, kind in [
        (args.workdir, "dir"),
        (args.checklist, "file"),
        (args.seed_ledger, "file"),
        (args.baseline_reference, "file"),
        (args.reason_rubric, "file"),
        (args.validator, "file"),
        (args.manual_plan, "file"),
    ]:
        ensure_exists(path, kind=kind)

    run_id, remediation_dir = remediation_dir_from_args(args)
    checklist_path, ledger_path, baseline_path, rubric_path = bootstrap_run_artifacts(
        remediation_dir=remediation_dir,
        checklist_template=args.checklist,
        seed_ledger=args.seed_ledger,
        baseline_reference=args.baseline_reference,
        reason_rubric=args.reason_rubric,
    )

    state_path = args.state_file or (remediation_dir / "orchestrator-v2-state.json")
    state = load_state(state_path)
    if not state:
        state = {
            "run_id": run_id,
            "started_at": utc_timestamp(),
            "workdir": str(args.workdir),
            "expected_branch": args.expected_branch,
            "batch_sizes": {
                "WA": args.batch_size_wa,
                "WB": args.batch_size_wb,
                "WC": args.batch_size_wc,
                "WD": args.batch_size_wd,
            },
            "session_id": args.session_id,
            "last_session_id": args.session_id,
            "batches": [],
            "gate_b_plus_status": "not-evaluated",
        }
        save_state(state_path, state)

    current_branch = git_branch(args.workdir)
    if current_branch != args.expected_branch:
        raise RuntimeError(
            f"Current branch '{current_branch}' does not match expected '{args.expected_branch}'"
        )

    if not args.allow_dirty and git_status_porcelain(args.workdir):
        raise RuntimeError("Worktree is dirty before orchestration start; rerun with --allow-dirty")

    progress_md = remediation_dir / "checklist-progress.md"
    preflight_json = remediation_dir / "validate-progress-preflight.json"
    run_validator(
        validator_path=args.validator,
        mode="progress",
        checklist_path=checklist_path,
        ledger_path=ledger_path,
        baseline_path=baseline_path,
        json_out=preflight_json,
        markdown_out=progress_md,
    )

    quarantine_path = remediation_dir / "batches" / "quarantine-queue.json"
    completed_batches = 0

    while True:
        items = parse_checklist(checklist_path)
        skip_ids = set()
        if not args.retry_quarantine:
            skip_ids = open_quarantine_ids(quarantine_path)

        active_wave = select_active_wave(items, skip_ids)
        if active_wave is None:
            print("No unchecked parent checklist IDs remain (excluding quarantine).")
            break

        if active_wave in {"WC", "WD"}:
            ok, missing = v3_available(remediation_dir)
            if not ok:
                state["gate_b_plus_status"] = "blocked-missing-v3"
                state["gate_b_plus_missing"] = missing
                save_state(state_path, state)
                write_json(
                    remediation_dir / "gate-b-plus-blocked.json",
                    {
                        "status": "blocked",
                        "missing": missing,
                        "timestamp": utc_timestamp(),
                    },
                )
                print("Gate B+ blocked: missing external v3 artifacts.")
                break
            state["gate_b_plus_status"] = "passed"
            save_state(state_path, state)

        batch_size = batch_size_for_wave(args, active_wave)
        batch_items = choose_batch(
            items,
            wave=active_wave,
            batch_size=batch_size,
            skip_ids=skip_ids,
        )
        if not batch_items:
            print(f"No selectable IDs for wave {active_wave}; likely quarantined.")
            break

        if args.max_batches and completed_batches >= args.max_batches:
            print(f"Reached --max-batches limit ({args.max_batches}).")
            break

        batch_number = len(state.get("batches", [])) + len(state.get("failed_batches", [])) + 1
        batch_ids = [item.checklist_id for item in batch_items]
        batch_prefix = f"batch-{batch_number:03d}"

        print(
            f"\n=== {batch_prefix} {active_wave}: {batch_ids[0]} .. {batch_ids[-1]} ({len(batch_ids)} IDs) ==="
        )

        if args.dry_run:
            write_json(
                remediation_dir / f"{batch_prefix}-dryrun.json",
                {
                    "batch_number": batch_number,
                    "wave": active_wave,
                    "ids": batch_ids,
                    "terms": [item.term for item in batch_items],
                    "timestamp": utc_timestamp(),
                },
            )
            for item in batch_items:
                print(f"- {item.checklist_id}: {item.term}")
            break

        checklist_snapshot = remediation_dir / f"{batch_prefix}-checklist-pre.md"
        ledger_snapshot = remediation_dir / f"{batch_prefix}-ledger-pre.csv"
        shutil.copy2(checklist_path, checklist_snapshot)
        shutil.copy2(ledger_path, ledger_snapshot)

        prompt = build_batch_prompt(
            batch_items=batch_items,
            wave=active_wave,
            plan_path=args.manual_plan,
            checklist_path=checklist_path,
            ledger_path=ledger_path,
            baseline_path=baseline_path,
            rubric_path=rubric_path,
            validator_path=args.validator,
            remediation_dir=remediation_dir,
            workdir=args.workdir,
            expected_branch=args.expected_branch,
            batch_number=batch_number,
        )

        opencode_log = remediation_dir / f"{batch_prefix}-opencode.jsonl"

        try:
            session_id = run_opencode_batch(
                opencode_bin=args.opencode_bin,
                workdir=args.workdir,
                prompt=prompt,
                log_path=opencode_log,
                session_id=state.get("session_id"),
                attach_url=args.attach_url,
                model=args.model,
                agent=args.agent,
                title=f"V2 glossary remediation {run_id}",
                attached_files=[
                    args.manual_plan,
                    checklist_path,
                    ledger_path,
                    baseline_path,
                    rubric_path,
                    args.validator,
                ],
                permission_override=(
                    args.permission_override if args.permission_override.strip() else None
                ),
                stream_output=args.stream_opencode_output,
            )
            state["last_session_id"] = session_id
            save_state(state_path, state)

            batch_validate_json = remediation_dir / f"{batch_prefix}-validate-progress.json"
            run_validator(
                validator_path=args.validator,
                mode="progress",
                checklist_path=checklist_path,
                ledger_path=ledger_path,
                baseline_path=baseline_path,
                json_out=batch_validate_json,
                markdown_out=progress_md,
            )

            passed_ids, quarantined = evaluate_batch_results(
                batch_items=batch_items,
                checklist_path=checklist_path,
                ledger_path=ledger_path,
            )

            if not passed_ids:
                shutil.copy2(checklist_snapshot, checklist_path)
                shutil.copy2(ledger_snapshot, ledger_path)
                run_command(
                    ["git", "restore", "--staged", "--worktree", "."],
                    cwd=args.workdir,
                    description="rollback failed batch repo changes",
                    check=False,
                )
                update_quarantine_queue(
                    quarantine_path,
                    ids=batch_ids,
                    reason="all terms failed in batch",
                    batch_number=batch_number,
                    wave=active_wave,
                )
                failure_payload = {
                    "batch_number": batch_number,
                    "wave": active_wave,
                    "ids": batch_ids,
                    "passed": [],
                    "quarantined": batch_ids,
                    "reason": "all terms failed",
                    "rolled_back": [
                        str(checklist_path),
                        str(ledger_path),
                        "worktree (git restore)",
                    ],
                    "timestamp": utc_timestamp(),
                }
                write_json(remediation_dir / f"{batch_prefix}-failure.json", failure_payload)
                state.setdefault("failed_batches", []).append(
                    {
                        "batch_number": batch_number,
                        "wave": active_wave,
                        "ids": batch_ids,
                        "reason": "all terms failed",
                        "timestamp": failure_payload["timestamp"],
                    }
                )
                save_state(state_path, state)
                print(f"{batch_prefix} failed with zero passed terms; all terms quarantined")
                if args.retry_quarantine:
                    print("Stopping after zero-pass batch because --retry-quarantine is enabled.")
                    break
                continue

            if quarantined:
                quarantined_ids = sorted(quarantined.keys(), key=parse_checklist_id)
                restore_checklist_rows_from_snapshot(
                    checklist_path=checklist_path,
                    snapshot_path=checklist_snapshot,
                    checklist_ids=quarantined_ids,
                )
                restore_ledger_rows_from_snapshot(
                    ledger_path=ledger_path,
                    snapshot_path=ledger_snapshot,
                    checklist_ids=quarantined_ids,
                )
                mark_quarantine_in_ledger(
                    ledger_path=ledger_path,
                    quarantined=quarantined,
                    batch_id=batch_prefix,
                )
                update_quarantine_queue(
                    quarantine_path,
                    ids=quarantined_ids,
                    reason="term-level validation failed",
                    batch_number=batch_number,
                    wave=active_wave,
                )
                write_json(
                    remediation_dir / f"{batch_prefix}-partial.json",
                    {
                        "batch_number": batch_number,
                        "wave": active_wave,
                        "passed_ids": passed_ids,
                        "quarantined": quarantined,
                        "timestamp": utc_timestamp(),
                    },
                )

            verify_only_batch_ids_changed(
                batch_ids=batch_ids,
                excluded_ids=set(quarantined.keys()),
                checklist_before_path=checklist_snapshot,
                checklist_after_path=checklist_path,
                ledger_before_path=ledger_snapshot,
                ledger_after_path=ledger_path,
            )

            for index, command in enumerate(args.extra_check, start=1):
                run_shell_command(command, cwd=args.workdir, description=f"extra check {index}")

            passed_items = [item for item in batch_items if item.checklist_id in set(passed_ids)]
            commit_hash = git_commit_batch(
                workdir=args.workdir,
                batch_items=passed_items,
                passed_ids=passed_ids,
                commit_prefix=args.commit_prefix,
                allow_empty_commit=args.allow_empty_commit,
            )

            update_ledger_after_commit(
                ledger_path=ledger_path,
                checklist_ids=passed_ids,
                commit_hash=commit_hash,
                batch_id=batch_prefix,
            )

            post_commit_json = remediation_dir / f"{batch_prefix}-validate-post-commit.json"
            run_validator(
                validator_path=args.validator,
                mode="progress",
                checklist_path=checklist_path,
                ledger_path=ledger_path,
                baseline_path=baseline_path,
                json_out=post_commit_json,
                markdown_out=progress_md,
            )

            batch_summary = {
                "batch_number": batch_number,
                "wave": active_wave,
                "ids": batch_ids,
                "passed_ids": passed_ids,
                "quarantined_ids": sorted(quarantined.keys(), key=parse_checklist_id),
                "terms": [item.term for item in batch_items],
                "commit_hash": commit_hash,
                "session_id": session_id,
                "opencode_log": str(opencode_log),
                "validator_progress": str(batch_validate_json),
                "validator_post_commit": str(post_commit_json),
                "timestamp": utc_timestamp(),
            }
            write_json(remediation_dir / f"{batch_prefix}-summary.json", batch_summary)

            state.setdefault("batches", []).append(batch_summary)
            save_state(state_path, state)

            completed_batches += 1
            print(f"{batch_prefix} committed: {commit_hash}")

            if args.pause_seconds > 0:
                time.sleep(args.pause_seconds)

        except Exception as exc:  # noqa: BLE001
            if checklist_snapshot.exists():
                shutil.copy2(checklist_snapshot, checklist_path)
            if ledger_snapshot.exists():
                shutil.copy2(ledger_snapshot, ledger_path)
            run_command(
                ["git", "restore", "--staged", "--worktree", "."],
                cwd=args.workdir,
                description="rollback worktree changes after batch exception",
                check=False,
            )

            failure_payload = {
                "batch_number": batch_number,
                "wave": active_wave,
                "ids": batch_ids,
                "error": str(exc),
                "rolled_back": [
                    str(checklist_path),
                    str(ledger_path),
                    "worktree (git restore)",
                ],
                "timestamp": utc_timestamp(),
            }
            failure_path = remediation_dir / f"{batch_prefix}-failure.json"
            if failure_path.exists():
                crash_payload = dict(failure_payload)
                crash_payload["failure_record"] = str(failure_path)
                write_json(remediation_dir / f"{batch_prefix}-crash.json", crash_payload)
            else:
                write_json(failure_path, failure_payload)

            state.setdefault("failed_batches", []).append(
                {
                    "batch_number": batch_number,
                    "wave": active_wave,
                    "ids": batch_ids,
                    "reason": "batch exception",
                    "error": str(exc),
                    "timestamp": failure_payload["timestamp"],
                }
            )
            save_state(state_path, state)
            raise RuntimeError(
                f"{exc}; run-local checklist/ledger and git worktree restored to pre-batch state"
            )

    if not args.skip_final_validator:
        remaining = [
            item
            for item in parse_checklist(checklist_path).values()
            if item.wave in {"WA", "WB", "WC", "WD"} and not item.parent_checked
        ]
        if not remaining and not args.dry_run:
            final_json = remediation_dir / "validate-final.json"
            run_validator(
                validator_path=args.validator,
                mode="final",
                checklist_path=checklist_path,
                ledger_path=ledger_path,
                baseline_path=baseline_path,
                json_out=final_json,
                markdown_out=progress_md,
            )
            print(f"Final validator completed: {final_json}")

    final_summary = {
        "run_id": run_id,
        "remediation_dir": str(remediation_dir),
        "workdir": str(args.workdir),
        "expected_branch": args.expected_branch,
        "last_session_id": state.get("last_session_id"),
        "gate_b_plus_status": state.get("gate_b_plus_status"),
        "batches_completed": completed_batches,
        "batches_failed": len(state.get("failed_batches", [])),
        "run_local_checklist": str(checklist_path),
        "canonical_checklist_template": str(args.checklist),
        "remaining_parent_ids": [
            item.checklist_id
            for item in sorted(
                [
                    item
                    for item in parse_checklist(checklist_path).values()
                    if item.wave in {"WA", "WB", "WC", "WD"} and not item.parent_checked
                ],
                key=lambda value: parse_checklist_id(value.checklist_id),
            )
        ],
        "timestamp": utc_timestamp(),
    }
    write_json(remediation_dir / "orchestrator-summary.json", final_summary)

    print("Orchestration complete.")
    print(f"Run directory: {remediation_dir}")
    print(f"Summary: {remediation_dir / 'orchestrator-summary.json'}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
