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


PARENT_RE = re.compile(r'^- \[(?P<mark>[ xX])\] (?P<id>PQ-\d{3}) (?P<rest>.+)$')
TERM_RE = re.compile(r'term="(?P<term>[^"]+)"')
SUB_RE = re.compile(r'^  - \[(?P<mark>[ xX])\] (?P<id>PQ-\d{3})\.(?P<idx>[1-5])\b')

ALLOWED_REASON_CODES = {
    "relocate-conceptual-owner",
    "relocate-first-use-owner",
    "retain-conceptual-owner",
    "retain-reordered",
    "retain-link-mitigated",
    "no-change-not-mislocated",
    "blocked",
}


@dataclass
class ChecklistItem:
    checklist_id: str
    term: str
    parent_checked: bool
    sub_checks: dict[int, bool]


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def normalize_path(path: Path) -> Path:
    return path.expanduser().resolve()


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


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


def checklist_index(checklist_id: str) -> int:
    return int(checklist_id.split("-")[1])


def parse_checklist(path: Path) -> dict[str, ChecklistItem]:
    items: dict[str, ChecklistItem] = {}

    for line in path.read_text(encoding="utf-8").splitlines():
        parent_match = PARENT_RE.match(line)
        if parent_match:
            checklist_id = parent_match.group("id")
            term_match = TERM_RE.search(parent_match.group("rest"))
            term = term_match.group("term") if term_match else ""
            item = ChecklistItem(
                checklist_id=checklist_id,
                term=term,
                parent_checked=parent_match.group("mark").lower() == "x",
                sub_checks={index: False for index in range(1, 6)},
            )
            items[checklist_id] = item
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


def read_ledger_rows(path: Path) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = {row["checklist_id"]: row for row in reader}
    return rows


def write_ledger_rows(path: Path, rows_by_id: dict[str, dict[str, str]]) -> None:
    if not rows_by_id:
        raise RuntimeError(f"Ledger is empty: {path}")

    first_row = next(iter(rows_by_id.values()))
    fieldnames = list(first_row.keys())
    ordered_ids = sorted(rows_by_id.keys(), key=checklist_index)

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for checklist_id in ordered_ids:
            writer.writerow(rows_by_id[checklist_id])


def choose_batch(items: dict[str, ChecklistItem], batch_size: int) -> list[ChecklistItem]:
    unchecked = [item for item in items.values() if not item.parent_checked]
    unchecked.sort(key=lambda item: checklist_index(item.checklist_id))
    return unchecked[:batch_size]


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
    lines = [line for line in result.stdout.splitlines() if line.strip()]
    return lines


def latest_session_id(
    opencode_bin: str,
    *,
    workdir: Path,
    env: dict[str, str],
) -> str | None:
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


def build_batch_prompt(
    *,
    batch_items: list[ChecklistItem],
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
    terms = "\n".join(
        f"- {item.checklist_id}: {item.term}" for item in batch_items
    )

    return f"""Execute the glossary placement remediation plan manually for this batch only.

Context:
- Worktree: `{workdir}`
- Expected branch: `{expected_branch}`
- Plan: `{plan_path}`
- Checklist: `{checklist_path}`
- Ledger: `{ledger_path}`
- Baseline reference: `{baseline_path}`
- Reason rubric: `{rubric_path}`
- Validator: `{validator_path}`
- Remediation directory: `{remediation_dir}`
- Batch number: `{batch_number}`

Batch scope (exact IDs, do not touch IDs outside this list): {ids}

Terms in this batch:
{terms}

Required workflow:
1. Process each term one-by-one manually.
2. Apply spec/tooling edits in this step1 worktree as needed for the batch IDs.
3. For this batch, do not mark any checklist parent ID complete unless the worktree has real repository edits related to that ID.
4. Update this run-local checklist parent + sub-items `.1`..`.5` for each completed ID.
4. Update the matching ledger row fields for each completed ID.
5. Keep `reason_code` within allowed rubric values and set `reason_quality=pass` only when justified.
6. Do not run any git commit or push command (commit is handled by the orchestrator).
7. Before finishing, run:
   `python3 "{validator_path}" --mode progress --checklist "{checklist_path}" --ledger "{ledger_path}" --baseline "{baseline_path}" --json-out "{remediation_dir}/batch-{batch_number:03d}-validate-progress.json" --markdown-out "{remediation_dir}/checklist-progress.md"`
8. If validator reports errors, fix them in this batch before finishing.

Response format:
- Completed IDs
- Files changed
- Any blockers (if none, say "none")
"""


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
        raise RuntimeError(
            f"opencode emitted error event(s): {error_events[0]}; see {log_path}"
        )

    if discovered_session:
        return discovered_session

    fallback = latest_session_id(opencode_bin, workdir=workdir, env=env)
    if fallback:
        return fallback
    raise RuntimeError("Could not determine OpenCode session ID after batch run")


def run_validator(
    *,
    validator_path: Path,
    mode: str,
    checklist_path: Path,
    ledger_path: Path,
    baseline_path: Path,
    json_out: Path,
    markdown_out: Path,
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
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(
            f"validator failed in mode={mode} (exit {result.returncode})\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )


def verify_batch_completion(
    *,
    batch_ids: list[str],
    checklist_path: Path,
    ledger_path: Path,
) -> None:
    checklist = parse_checklist(checklist_path)
    ledger_rows = read_ledger_rows(ledger_path)
    errors: list[str] = []

    for checklist_id in batch_ids:
        item = checklist.get(checklist_id)
        if item is None:
            errors.append(f"{checklist_id}: missing checklist parent row")
            continue
        if not item.parent_checked:
            errors.append(f"{checklist_id}: parent row is not checked")
        for sub_index in range(1, 6):
            if not item.sub_checks.get(sub_index, False):
                errors.append(f"{checklist_id}: sub-item .{sub_index} is not checked")

        row = ledger_rows.get(checklist_id)
        if row is None:
            errors.append(f"{checklist_id}: missing ledger row")
            continue

        if not (row.get("decision") or "").strip():
            errors.append(f"{checklist_id}: missing decision")

        reason_code = (row.get("reason_code") or "").strip()
        if reason_code not in ALLOWED_REASON_CODES:
            errors.append(f"{checklist_id}: invalid reason_code '{reason_code}'")

        reason_quality = (row.get("reason_quality") or "").strip().lower()
        if reason_quality != "pass":
            errors.append(f"{checklist_id}: reason_quality must be pass")

        reason_why = (row.get("reason_why") or "").strip()
        if len(reason_why) < 80:
            errors.append(f"{checklist_id}: reason_why shorter than 80 chars")

        if reason_code != "blocked":
            for column in ["after_file", "after_line", "after_dp_id"]:
                if not (row.get(column) or "").strip():
                    errors.append(f"{checklist_id}: missing {column}")

        phase1_status = (row.get("phase1_status") or "").strip().lower()
        final_quality = (row.get("final_quality") or "").strip().lower()
        if phase1_status in {"", "pending"}:
            errors.append(f"{checklist_id}: phase1_status is pending")
        if final_quality in {"", "pending"}:
            errors.append(f"{checklist_id}: final_quality is pending")

    if errors:
        raise RuntimeError("Batch verification failed:\n- " + "\n- ".join(errors))


def verify_only_batch_ids_changed(
    *,
    batch_ids: list[str],
    checklist_before_path: Path,
    checklist_after_path: Path,
    ledger_before_path: Path,
    ledger_after_path: Path,
) -> None:
    batch_set = set(batch_ids)
    before_checklist = parse_checklist(checklist_before_path)
    after_checklist = parse_checklist(checklist_after_path)
    before_ledger = read_ledger_rows(ledger_before_path)
    after_ledger = read_ledger_rows(ledger_after_path)

    errors: list[str] = []

    for checklist_id, before_item in before_checklist.items():
        if checklist_id in batch_set:
            continue
        after_item = after_checklist.get(checklist_id)
        if after_item is None:
            errors.append(f"{checklist_id}: missing in post-batch checklist")
            continue
        if before_item.parent_checked != after_item.parent_checked:
            errors.append(f"{checklist_id}: parent checkbox changed outside batch")
        for sub_index in range(1, 6):
            if before_item.sub_checks.get(sub_index) != after_item.sub_checks.get(sub_index):
                errors.append(
                    f"{checklist_id}: sub-item .{sub_index} changed outside batch"
                )

    for checklist_id, before_row in before_ledger.items():
        if checklist_id in batch_set:
            continue
        after_row = after_ledger.get(checklist_id)
        if after_row is None:
            errors.append(f"{checklist_id}: missing in post-batch ledger")
            continue
        if before_row != after_row:
            errors.append(f"{checklist_id}: ledger row changed outside batch")

    if errors:
        preview = errors[:60]
        raise RuntimeError("Unexpected out-of-scope changes:\n- " + "\n- ".join(preview))


def update_ledger_after_commit(
    *, ledger_path: Path, batch_ids: list[str], commit_hash: str
) -> None:
    rows = read_ledger_rows(ledger_path)
    for checklist_id in batch_ids:
        row = rows.get(checklist_id)
        if row is None:
            continue
        row["after_commit"] = commit_hash
    write_ledger_rows(ledger_path, rows)


def git_commit_batch(
    *,
    workdir: Path,
    batch_items: list[ChecklistItem],
    commit_prefix: str,
    allow_empty_commit: bool,
) -> str:
    status_before = git_status_porcelain(workdir)
    if not status_before and not allow_empty_commit:
        raise RuntimeError("No repository changes to commit for this batch")

    run_command(["git", "add", "-A"], cwd=workdir, description="stage batch changes")

    first_id = batch_items[0].checklist_id
    last_id = batch_items[-1].checklist_id
    subject = f"{commit_prefix} {first_id}-{last_id}"
    lines = [
        f"Batch IDs: {', '.join(item.checklist_id for item in batch_items)}",
        "",
        "Terms:",
    ]
    lines.extend(f"- {item.checklist_id}: {item.term}" for item in batch_items)
    body = "\n".join(lines)

    commit_args = ["git", "commit"]
    if allow_empty_commit:
        commit_args.append("--allow-empty")
    commit_args.extend(["-m", subject, "-m", body])
    run_command(commit_args, cwd=workdir, description="create batch commit")

    commit_hash = run_command(
        ["git", "rev-parse", "HEAD"],
        cwd=workdir,
        description="resolve batch commit hash",
    ).stdout.strip()
    return commit_hash


def build_defaults(config_dir: Path) -> dict[str, Path]:
    reports_dir = config_dir / "reports"
    plans_dir = config_dir / "plans"
    return {
        "checklist": reports_dir / "glossary-poor-questionable-202-checklist.md",
        "seed_ledger": reports_dir / "glossary-poor-questionable-202-ledger-seed.csv",
        "baseline_reference": reports_dir
        / "glossary-poor-questionable-202-baseline-reference.csv",
        "reason_rubric": reports_dir / "glossary-poor-questionable-reason-rubric.md",
        "validator": reports_dir / "validate-ledger-and-checklist.py",
        "manual_plan": plans_dir / "glossary-poor-questionable-manual-remediation-plan.md",
    }


def parse_args() -> argparse.Namespace:
    opencode_config_dir = os.environ.get("OPENCODE_CONFIG_DIR")
    if not opencode_config_dir:
        raise RuntimeError("OPENCODE_CONFIG_DIR is not set")
    config_dir = normalize_path(Path(opencode_config_dir))
    defaults = build_defaults(config_dir)

    parser = argparse.ArgumentParser(
        description="Run glossary poor/questionable remediation in 20-item OpenCode batches"
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
    parser.add_argument(
        "--batch-size",
        type=int,
        default=20,
        help="Number of checklist parent IDs per batch",
    )
    parser.add_argument(
        "--max-batches",
        type=int,
        default=0,
        help="Maximum batches this invocation (0 means until checklist completion)",
    )
    parser.add_argument(
        "--remediation-dir",
        type=Path,
        help="Run directory for logs/artifacts (defaults to timestamped directory)",
    )
    parser.add_argument("--run-id", help="Optional custom run ID")
    parser.add_argument("--session-id", help="Continue a specific OpenCode session")
    parser.add_argument(
        "--reuse-session",
        action="store_true",
        help="Reuse OpenCode session across batches (default is fresh session per batch)",
    )
    parser.add_argument("--attach-url", help="Attach to running OpenCode server URL")
    parser.add_argument("--model", help="Model in provider/model format")
    parser.add_argument("--agent", help="OpenCode agent name")
    parser.add_argument("--opencode-bin", default="opencode", help="OpenCode CLI binary")
    parser.add_argument("--checklist", type=Path, default=defaults["checklist"])
    parser.add_argument("--seed-ledger", type=Path, default=defaults["seed_ledger"])
    parser.add_argument(
        "--baseline-reference", type=Path, default=defaults["baseline_reference"]
    )
    parser.add_argument("--reason-rubric", type=Path, default=defaults["reason_rubric"])
    parser.add_argument("--validator", type=Path, default=defaults["validator"])
    parser.add_argument("--manual-plan", type=Path, default=defaults["manual_plan"])
    parser.add_argument(
        "--state-file",
        type=Path,
        help="Override run state file path (defaults to remediation-dir/orchestrator-state.json)",
    )
    parser.add_argument(
        "--commit-prefix",
        default="docs(glossary): remediate placement terms",
        help="Commit message prefix",
    )
    parser.add_argument(
        "--allow-dirty",
        action="store_true",
        help="Allow starting with a dirty worktree",
    )
    parser.add_argument(
        "--allow-empty-commit",
        action="store_true",
        help="Allow empty git commit when batch has no repository changes",
    )
    parser.add_argument(
        "--pause-seconds",
        type=float,
        default=0.0,
        help="Pause duration between successful batches",
    )
    parser.add_argument(
        "--extra-check",
        action="append",
        default=[],
        help="Additional shell command to run in workdir after each batch",
    )
    parser.add_argument(
        "--permission-override",
        default='{"*":"allow","external_directory":"allow"}',
        help="Value for OPENCODE_PERMISSION for opencode subprocess (empty string disables override)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print next batch and exit without calling OpenCode or committing",
    )
    parser.add_argument(
        "--skip-final-validator",
        action="store_true",
        help="Do not run validator in final mode when checklist reaches completion",
    )
    parser.add_argument(
        "--stream-opencode-output",
        action="store_true",
        help="Stream raw opencode JSON events to stdout while running batches",
    )

    args = parser.parse_args()

    args.workdir = normalize_path(args.workdir)
    args.checklist = normalize_path(args.checklist)
    args.seed_ledger = normalize_path(args.seed_ledger)
    args.baseline_reference = normalize_path(args.baseline_reference)
    args.reason_rubric = normalize_path(args.reason_rubric)
    args.validator = normalize_path(args.validator)
    args.manual_plan = normalize_path(args.manual_plan)
    args.config_dir = config_dir

    if args.remediation_dir is not None:
        args.remediation_dir = normalize_path(args.remediation_dir)

    if args.state_file is not None:
        args.state_file = normalize_path(args.state_file)

    if args.batch_size <= 0:
        raise RuntimeError("--batch-size must be greater than zero")
    if args.max_batches < 0:
        raise RuntimeError("--max-batches must be zero or greater")

    if args.session_id and not args.reuse_session:
        args.reuse_session = True

    return args


def load_state(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    return load_json(path)


def save_state(path: Path, state: dict[str, Any]) -> None:
    state["updated_at"] = utc_timestamp()
    write_json(path, state)


def remediation_dir_from_args(args: argparse.Namespace) -> tuple[str, Path]:
    if args.remediation_dir is not None:
        remediation_dir = args.remediation_dir
        run_id = remediation_dir.name.rsplit("-", 1)[-1]
        remediation_dir.mkdir(parents=True, exist_ok=True)
        return run_id, remediation_dir

    run_id = args.run_id or utc_timestamp()
    remediation_dir = args.config_dir / "reports" / (
        f"glossary-poor-questionable-manual-remediation-{run_id}"
    )
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
    checklist_path = remediation_dir / "manual-placement-checklist.md"
    ledger_path = remediation_dir / "manual-placement-ledger.csv"
    baseline_path = remediation_dir / "manual-placement-baseline-reference.csv"
    rubric_path = remediation_dir / "reason-rubric.md"

    if not checklist_path.exists():
        shutil.copy2(checklist_template, checklist_path)
    if not ledger_path.exists():
        shutil.copy2(seed_ledger, ledger_path)
    if not baseline_path.exists():
        shutil.copy2(baseline_reference, baseline_path)
    if not rubric_path.exists():
        shutil.copy2(reason_rubric, rubric_path)

    return checklist_path, ledger_path, baseline_path, rubric_path


def main() -> int:
    args = parse_args()

    ensure_exists(args.workdir, kind="dir")
    ensure_exists(args.checklist, kind="file")
    ensure_exists(args.seed_ledger, kind="file")
    ensure_exists(args.baseline_reference, kind="file")
    ensure_exists(args.reason_rubric, kind="file")
    ensure_exists(args.validator, kind="file")
    ensure_exists(args.manual_plan, kind="file")

    run_id, remediation_dir = remediation_dir_from_args(args)
    checklist_path, ledger_path, baseline_path, rubric_path = bootstrap_run_artifacts(
        remediation_dir=remediation_dir,
        checklist_template=args.checklist,
        seed_ledger=args.seed_ledger,
        baseline_reference=args.baseline_reference,
        reason_rubric=args.reason_rubric,
    )

    state_path = args.state_file or (remediation_dir / "orchestrator-state.json")
    state = load_state(state_path)
    if not state:
        state = {
            "run_id": run_id,
            "started_at": utc_timestamp(),
            "workdir": str(args.workdir),
            "expected_branch": args.expected_branch,
            "batch_size": args.batch_size,
            "reuse_session": args.reuse_session,
            "session_id": args.session_id,
            "last_session_id": args.session_id,
            "batches": [],
        }
        save_state(state_path, state)

    if args.session_id:
        state["session_id"] = args.session_id

    current_branch = git_branch(args.workdir)
    if current_branch != args.expected_branch:
        raise RuntimeError(
            f"Current branch '{current_branch}' does not match expected '{args.expected_branch}'"
        )

    if not args.allow_dirty:
        status = git_status_porcelain(args.workdir)
        if status:
            raise RuntimeError(
                "Worktree is dirty before orchestration start; rerun with --allow-dirty if intentional"
            )

    progress_md = remediation_dir / "checklist-progress.md"
    preflight_progress_json = remediation_dir / "validate-progress-preflight.json"
    run_validator(
        validator_path=args.validator,
        mode="progress",
        checklist_path=checklist_path,
        ledger_path=ledger_path,
        baseline_path=baseline_path,
        json_out=preflight_progress_json,
        markdown_out=progress_md,
    )

    completed_batches = 0
    while True:
        checklist = parse_checklist(checklist_path)
        batch_items = choose_batch(checklist, args.batch_size)
        if not batch_items:
            print("No unchecked parent checklist IDs remain.")
            break

        if args.max_batches and completed_batches >= args.max_batches:
            print(f"Reached --max-batches limit ({args.max_batches}).")
            break

        batch_number = len(state.get("batches", [])) + 1
        batch_ids = [item.checklist_id for item in batch_items]
        print(
            f"\n=== Batch {batch_number:03d}: {batch_ids[0]} .. {batch_ids[-1]} ({len(batch_ids)} IDs) ==="
        )

        if args.dry_run:
            print("Dry run mode: selected IDs")
            for item in batch_items:
                print(f"- {item.checklist_id}: {item.term}")
            break

        prompt = build_batch_prompt(
            batch_items=batch_items,
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

        batch_prefix = f"batch-{batch_number:03d}"
        opencode_log = remediation_dir / f"{batch_prefix}-opencode.jsonl"
        checklist_snapshot = remediation_dir / f"{batch_prefix}-checklist-pre.md"
        ledger_snapshot = remediation_dir / f"{batch_prefix}-ledger-pre.csv"
        shutil.copy2(checklist_path, checklist_snapshot)
        shutil.copy2(ledger_path, ledger_snapshot)

        try:
            session_for_call = state.get("session_id") if args.reuse_session else None
            session_id = run_opencode_batch(
                opencode_bin=args.opencode_bin,
                workdir=args.workdir,
                prompt=prompt,
                log_path=opencode_log,
                session_id=session_for_call,
                attach_url=args.attach_url,
                model=args.model,
                agent=args.agent,
                title=f"Glossary placement remediation {run_id}",
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
            if args.reuse_session:
                state["session_id"] = session_id
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

            verify_batch_completion(
                batch_ids=batch_ids,
                checklist_path=checklist_path,
                ledger_path=ledger_path,
            )

            verify_only_batch_ids_changed(
                batch_ids=batch_ids,
                checklist_before_path=checklist_snapshot,
                checklist_after_path=checklist_path,
                ledger_before_path=ledger_snapshot,
                ledger_after_path=ledger_path,
            )

            if not git_status_porcelain(args.workdir):
                raise RuntimeError(
                    "Batch produced no changes in step1 worktree"
                )

            for index, command in enumerate(args.extra_check, start=1):
                run_shell_command(
                    command,
                    cwd=args.workdir,
                    description=f"extra check {index}",
                )
        except Exception as exc:  # noqa: BLE001
            shutil.copy2(checklist_snapshot, checklist_path)
            shutil.copy2(ledger_snapshot, ledger_path)
            write_json(
                remediation_dir / f"{batch_prefix}-failure.json",
                {
                    "batch_number": batch_number,
                    "ids": batch_ids,
                    "error": str(exc),
                    "rolled_back": [str(checklist_path), str(ledger_path)],
                    "timestamp": utc_timestamp(),
                },
            )
            raise RuntimeError(
                f"{exc}; run-local checklist/ledger restored to pre-batch state"
            )

        commit_hash = git_commit_batch(
            workdir=args.workdir,
            batch_items=batch_items,
            commit_prefix=args.commit_prefix,
            allow_empty_commit=args.allow_empty_commit,
        )

        update_ledger_after_commit(
            ledger_path=ledger_path,
            batch_ids=batch_ids,
            commit_hash=commit_hash,
        )

        post_commit_validate_json = remediation_dir / f"{batch_prefix}-validate-post-commit.json"
        run_validator(
            validator_path=args.validator,
            mode="progress",
            checklist_path=checklist_path,
            ledger_path=ledger_path,
            baseline_path=baseline_path,
            json_out=post_commit_validate_json,
            markdown_out=progress_md,
        )

        batch_summary = {
            "batch_number": batch_number,
            "ids": batch_ids,
            "terms": [item.term for item in batch_items],
            "commit_hash": commit_hash,
            "session_id": session_id,
            "opencode_log": str(opencode_log),
            "validator_progress": str(batch_validate_json),
            "validator_post_commit": str(post_commit_validate_json),
            "timestamp": utc_timestamp(),
        }
        write_json(remediation_dir / f"{batch_prefix}-summary.json", batch_summary)

        state.setdefault("batches", []).append(batch_summary)
        save_state(state_path, state)

        completed_batches += 1
        print(f"Batch {batch_number:03d} committed: {commit_hash}")

        if args.pause_seconds > 0:
            time.sleep(args.pause_seconds)

    if not args.skip_final_validator:
        remaining = choose_batch(parse_checklist(checklist_path), args.batch_size)
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
        "session_id": state.get("session_id"),
        "batches_completed": completed_batches,
        "run_local_checklist": str(checklist_path),
        "canonical_checklist": str(args.checklist),
        "remaining_parent_ids": [
            item.checklist_id
            for item in choose_batch(parse_checklist(checklist_path), 10_000)
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
