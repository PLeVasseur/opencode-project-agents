#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import itertools
import json
import os
import re
import shlex
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

RECOVERY_LEDGER_COLUMNS = [
    "rationale_uuid",
    "rationale_inserted_at_utc",
    "rationale_text_sha256",
    "recommendation_priority",
    "recommendation_used",
    "deviation_permit_path",
    "deviation_permit_sha256",
    "deviation_approved_by",
]

UUID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
    re.IGNORECASE,
)

FAILURE_CODE_RE = re.compile(r"FAILED_[A-Z_]+")
CHECKLIST_ID_RE = re.compile(r"\b(?:W[ABCD]|QQ)-\d{3}\b")

QUARANTINABLE_VALIDATOR_CODES = {
    "FAILED_UUID_GUARDRAIL",
    "FAILED_RECOMMENDATION_LOCK",
}

HARD_FAIL_VALIDATOR_CODES = {
    "FAILED_STRICT_REGRESSION",
    "FAILED_DEVIATION_CONCENTRATION",
    "FAILED_RATIONALE_MONOCULTURE",
    "FAILED_FOUNDATIONAL_PLACEMENT",
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


@dataclass
class ValidatorResult:
    returncode: int
    errors: list[str]
    summary: dict[str, Any] | None
    failure_codes: list[str]
    stdout: str
    stderr: str


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


def find_failure_codes(text: str) -> list[str]:
    return sorted(set(FAILURE_CODE_RE.findall(text)))


def jaccard_similarity(a: str, b: str) -> float:
    tokens_a = {token for token in re.split(r"\s+", a.lower().strip()) if token}
    tokens_b = {token for token in re.split(r"\s+", b.lower().strip()) if token}
    if not tokens_a and not tokens_b:
        return 1.0
    if not tokens_a or not tokens_b:
        return 0.0
    return len(tokens_a & tokens_b) / len(tokens_a | tokens_b)


def failure_code_from_error(error: str) -> str | None:
    if not error.startswith("FAILED_"):
        return None
    code, _, _ = error.partition(":")
    code = code.strip()
    return code if code else None


def extract_batch_ids_from_error(error: str, *, batch_ids: set[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for checklist_id in CHECKLIST_ID_RE.findall(error):
        if checklist_id in batch_ids and checklist_id not in seen:
            seen.add(checklist_id)
            ordered.append(checklist_id)
    return ordered


def merge_quarantine_reasons(target: dict[str, str], source: dict[str, str]) -> None:
    for checklist_id, reason in source.items():
        existing = (target.get(checklist_id) or "").strip()
        if not existing:
            target[checklist_id] = reason
            continue
        if reason in existing:
            continue
        target[checklist_id] = f"{existing}; {reason}"


def run_strict_phase_check(
    *,
    strict_command_template: str,
    workdir: Path,
    report_path: Path,
    description: str,
) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    if "{report}" not in strict_command_template:
        raise RuntimeError(
            "strict command template must include '{report}' placeholder"
        )
    command_text = strict_command_template.format(report=str(report_path))
    args = shlex.split(command_text)
    if not args:
        raise RuntimeError("strict command template resolved to empty command")
    run_command(args, cwd=workdir, description=description)
    ensure_exists(report_path, kind="file")


def classify_validator_failures_for_batch(
    *,
    validator_errors: list[str],
    batch_ids: list[str],
) -> tuple[dict[str, str], list[str], list[str]]:
    batch_id_set = set(batch_ids)
    quarantined: dict[str, str] = {}
    hard_codes: set[str] = set()
    unresolved: list[str] = []

    for error in validator_errors:
        code = failure_code_from_error(error)
        ids = extract_batch_ids_from_error(error, batch_ids=batch_id_set)

        if code in HARD_FAIL_VALIDATOR_CODES:
            hard_codes.add(code)
            unresolved.append(error)
            continue

        if code is not None:
            if code in QUARANTINABLE_VALIDATOR_CODES:
                if not ids:
                    unresolved.append(error)
                    continue
                for checklist_id in ids:
                    quarantined[checklist_id] = (
                        f"validator {code.lower()}: {error}"
                    )
                continue

            unresolved.append(error)
            continue

        if ids:
            for checklist_id in ids:
                quarantined[checklist_id] = f"validator error: {error}"
            continue

        unresolved.append(error)

    return quarantined, sorted(hard_codes), unresolved


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


def index_terms_by_name(path: Path) -> dict[str, list[dict[str, Any]]]:
    payload = load_json(path)
    index: dict[str, list[dict[str, Any]]] = {}
    for entry in payload.get("terms", []):
        term = (entry.get("term") or "").strip()
        if not term:
            continue
        index.setdefault(term, []).append(entry)
    return index


def build_term_lock_manifest(
    *,
    batch_items: list[ChecklistItem],
    placement_json: Path,
    divergence_json: Path,
) -> dict[str, Any]:
    placement_index = index_terms_by_name(placement_json)
    divergence_index = index_terms_by_name(divergence_json)

    records = []
    for item in batch_items:
        placement_matches = placement_index.get(item.term, [])
        divergence_matches = divergence_index.get(item.term, [])
        if len(placement_matches) != 1:
            raise RuntimeError(
                f"term lock failed for {item.checklist_id}: placement matches={len(placement_matches)}"
            )
        if len(divergence_matches) != 1:
            raise RuntimeError(
                f"term lock failed for {item.checklist_id}: divergence matches={len(divergence_matches)}"
            )

        placement = placement_matches[0]
        divergence = divergence_matches[0]
        recommended = placement.get("recommended_location") or {}

        records.append(
            {
                "checklist_id": item.checklist_id,
                "term": item.term,
                "relocation_priority": placement.get("relocation_priority"),
                "recommended_file": recommended.get("file"),
                "recommended_section": recommended.get("section"),
                "recommended_reason": recommended.get("reason"),
                "placement_fitness": placement.get("fitness_rating"),
                "divergence_match_category": divergence.get("match_category"),
                "divergence_reliability": divergence.get("reliability"),
            }
        )

    return {
        "placement_json": str(placement_json),
        "divergence_json": str(divergence_json),
        "terms": records,
    }


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


def ensure_ledger_columns(path: Path, required_columns: list[str]) -> None:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)

    missing = [column for column in required_columns if column not in fieldnames]
    if not missing:
        return

    fieldnames.extend(missing)
    for row in rows:
        for column in missing:
            row[column] = ""

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


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


def git_head(workdir: Path) -> str:
    return run_command(
        ["git", "rev-parse", "HEAD"],
        cwd=workdir,
        description="resolve current head",
    ).stdout.strip()


def git_commit_range_count(workdir: Path, start_head: str, end_head: str) -> int:
    result = run_command(
        ["git", "rev-list", "--count", f"{start_head}..{end_head}"],
        cwd=workdir,
        description="count commits in range",
    )
    return int((result.stdout or "0").strip() or "0")


def git_commit_range_hashes(workdir: Path, start_head: str, end_head: str) -> list[str]:
    result = run_command(
        ["git", "log", "--format=%H", f"{start_head}..{end_head}"],
        cwd=workdir,
        description="list commits in range",
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def git_changed_files_in_range(
    workdir: Path,
    start_head: str,
    end_head: str,
    *,
    paths: list[str],
) -> list[str]:
    args = ["git", "diff", "--name-only", f"{start_head}..{end_head}", "--", *paths]
    result = run_command(
        args,
        cwd=workdir,
        description="list changed files in range",
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


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
    remediation_dir = args.config_dir / "reports" / f"glossary-pr6-v3-step1-phase1-remediation-{run_id}"
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
    checklist_path = remediation_dir / "manual-placement-checklist-v3.md"
    ledger_path = remediation_dir / "manual-placement-ledger-v3.csv"
    baseline_path = remediation_dir / "manual-placement-baseline-reference-v3.csv"
    rubric_path = remediation_dir / "reason-rubric-v3.md"

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


def wave_parent_counts(items: dict[str, ChecklistItem], wave: str) -> tuple[int, int]:
    wave_items = [item for item in items.values() if item.wave == wave]
    total = len(wave_items)
    checked = sum(1 for item in wave_items if item.parent_checked)
    return total, checked


def write_execution_integrity_report(
    *,
    remediation_dir: Path,
    start_head: str,
    wave_a_end_head: str | None,
    end_head: str,
    new_commit_count: int,
    new_commit_hashes: list[str],
    changed_src_files: list[str],
    has_wave_ab_scope: bool,
    wave_a_complete: bool,
    wave_b_complete: bool,
    batches_completed_current_run: int,
    batches_completed_total: int,
    dry_run: bool,
) -> tuple[str, Path]:
    reports_dir = remediation_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    failures: list[str] = []
    checks = {
        "has_wave_ab_scope": has_wave_ab_scope,
        "dry_run": dry_run,
        "new_commit_count_gt_zero": new_commit_count > 0,
        "changed_src_files_non_empty": bool(changed_src_files),
        "waves_complete_with_nonzero_batches": (
            not (wave_a_complete or wave_b_complete)
            or batches_completed_total > 0
        ),
    }

    if has_wave_ab_scope and (not dry_run):
        if new_commit_count == 0:
            failures.append("new_commit_count == 0")
        if not changed_src_files:
            failures.append("changed_src_files is empty")
        if (wave_a_complete or wave_b_complete) and batches_completed_total == 0:
            failures.append(
                "wave A/B marked complete while orchestrator recorded zero completed batches"
            )

    verdict = "pass" if not failures else "FAILED_INVALID_EXECUTION"

    payload = {
        "verdict": verdict,
        "start_head": start_head,
        "wave_a_end_head": wave_a_end_head,
        "end_head": end_head,
        "new_commit_count": new_commit_count,
        "new_commit_hashes": new_commit_hashes,
        "changed_src_files": changed_src_files,
        "has_wave_ab_scope": has_wave_ab_scope,
        "wave_a_complete": wave_a_complete,
        "wave_b_complete": wave_b_complete,
        "batches_completed_current_run": batches_completed_current_run,
        "batches_completed_total": batches_completed_total,
        "checks": checks,
        "failures": failures,
        "timestamp": utc_timestamp(),
    }

    json_path = reports_dir / "execution-integrity.json"
    write_json(json_path, payload)

    markdown_lines = [
        "# Execution integrity",
        "",
        f"- Verdict: `{verdict}`",
        f"- Start head: `{start_head}`",
        f"- Wave A end head: `{wave_a_end_head or ''}`",
        f"- End head: `{end_head}`",
        f"- New commit count: `{new_commit_count}`",
        f"- Has Wave A/B scope: `{has_wave_ab_scope}`",
        f"- Wave A complete: `{wave_a_complete}`",
        f"- Wave B complete: `{wave_b_complete}`",
        f"- Batches completed (current run): `{batches_completed_current_run}`",
        f"- Batches completed (total): `{batches_completed_total}`",
        "",
        "## Changed src files",
        "",
    ]
    if changed_src_files:
        markdown_lines.extend(f"- `{path}`" for path in changed_src_files)
    else:
        markdown_lines.append("- none")

    markdown_lines.extend(
        [
            "",
            "## New commits",
            "",
        ]
    )
    if new_commit_hashes:
        markdown_lines.extend(f"- `{commit}`" for commit in new_commit_hashes)
    else:
        markdown_lines.append("- none")

    markdown_lines.extend(
        [
            "",
            "## Integrity checks",
            "",
            f"- `new_commit_count > 0`: `{checks['new_commit_count_gt_zero']}`",
            f"- `changed_src_files` non-empty: `{checks['changed_src_files_non_empty']}`",
            (
                "- wave completion implies nonzero batches: "
                f"`{checks['waves_complete_with_nonzero_batches']}`"
            ),
        ]
    )

    if failures:
        markdown_lines.extend(["", "## Failures", ""])
        markdown_lines.extend(f"- {failure}" for failure in failures)

    markdown_path = reports_dir / "execution-integrity.md"
    markdown_path.write_text("\n".join(markdown_lines) + "\n", encoding="utf-8")

    return verdict, json_path


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
    recovery_guardrails: bool = False,
    events_jsonl: Path | None = None,
    strict_baseline_json: Path | None = None,
    strict_current_json: Path | None = None,
    strict_max_missing: int = 2,
    strict_waiver_file: Path | None = None,
    allow_failure: bool = False,
) -> ValidatorResult:
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
    if recovery_guardrails:
        args.append("--recovery-guardrails")
        args.extend(["--strict-max-missing", str(strict_max_missing)])
        if events_jsonl is not None:
            args.extend(["--events-jsonl", str(events_jsonl)])
        if strict_baseline_json is not None:
            args.extend(["--strict-baseline-json", str(strict_baseline_json)])
        if strict_current_json is not None:
            args.extend(["--strict-current-json", str(strict_current_json)])
        if strict_waiver_file is not None:
            args.extend(["--strict-waiver-file", str(strict_waiver_file)])

    result = subprocess.run(args, capture_output=True, text=True, check=False)

    payload_summary: dict[str, Any] | None = None
    payload_errors: list[str] = []
    if json_out.is_file():
        try:
            payload = load_json(json_out)
            summary = payload.get("summary")
            if isinstance(summary, dict):
                payload_summary = summary
            errors = payload.get("errors")
            if isinstance(errors, list):
                payload_errors = [str(error) for error in errors]
        except Exception:  # noqa: BLE001
            payload_errors = []

    output_text = f"{result.stdout}\n{result.stderr}\n" + "\n".join(payload_errors)
    failure_codes = find_failure_codes(output_text)

    validator_result = ValidatorResult(
        returncode=result.returncode,
        errors=payload_errors,
        summary=payload_summary,
        failure_codes=failure_codes,
        stdout=result.stdout,
        stderr=result.stderr,
    )

    if result.returncode != 0 and not allow_failure:
        prefix = ""
        if failure_codes:
            prefix = f"failure_codes={','.join(failure_codes)}\n"
        raise RuntimeError(
            f"{prefix}validator failed in mode={mode} (exit {result.returncode})\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )

    return validator_result


def run_rationale_analyzer(
    *,
    analyzer_path: Path,
    ledger_path: Path,
    json_out: Path,
    markdown_out: Path,
    workdir: Path,
) -> None:
    run_command(
        [
            "python3",
            str(analyzer_path),
            "--ledger",
            str(ledger_path),
            "--json-out",
            str(json_out),
            "--markdown-out",
            str(markdown_out),
        ],
        cwd=workdir,
        description="run rationale pattern analyzer",
    )


def compute_batch_metrics(
    *,
    passed_items: list[ChecklistItem],
    ledger_rows: dict[str, dict[str, str]],
) -> dict[str, Any]:
    high_medium_total = 0
    recommendation_compliant = 0
    deviation_permit_count = 0
    moved_terms: list[dict[str, str]] = []
    reasons: list[tuple[str, str]] = []

    for item in passed_items:
        row = ledger_rows.get(item.checklist_id, {})
        priority = (row.get("recommendation_priority") or "").strip().lower()
        used = (row.get("recommendation_used") or "").strip().lower()
        action = (row.get("action_type") or "").strip().lower()
        reason_why = (row.get("reason_why") or "").strip()
        reasons.append((item.checklist_id, reason_why))

        if priority in {"high", "medium"}:
            high_medium_total += 1
            if used == "yes":
                recommendation_compliant += 1
            else:
                deviation_permit_count += 1

        if "move" in action:
            moved_terms.append({"checklist_id": item.checklist_id, "term": item.term})

    max_similarity = 0.0
    max_similarity_pair: tuple[str, str] | None = None
    for (id_a, reason_a), (id_b, reason_b) in itertools.combinations(reasons, 2):
        similarity = jaccard_similarity(reason_a, reason_b)
        if similarity > max_similarity:
            max_similarity = similarity
            max_similarity_pair = (id_a, id_b)

    compliance_rate = 1.0
    if high_medium_total > 0:
        compliance_rate = recommendation_compliant / high_medium_total

    return {
        "high_medium_total": high_medium_total,
        "recommendation_compliant_count": recommendation_compliant,
        "recommendation_compliance_rate": compliance_rate,
        "deviation_permit_count": deviation_permit_count,
        "max_rationale_similarity": max_similarity,
        "max_rationale_similarity_pair": max_similarity_pair,
        "moved_term_count": len(moved_terms),
        "moved_terms": moved_terms,
    }


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
    placement_json: Path,
    divergence_json: Path,
    rubric_path: Path,
    rationale_writer: Path,
    rationale_analyzer: Path,
    events_jsonl: Path,
    validator_path: Path,
    term_lock_manifest: Path,
    remediation_dir: Path,
    workdir: Path,
    expected_branch: str,
    batch_number: int,
) -> str:
    ids = ", ".join(item.checklist_id for item in batch_items)
    terms = "\n".join(f"- {item.checklist_id}: {item.term}" for item in batch_items)
    return f"""Execute the v3 glossary remediation plan for this wave batch only.

Context:
- Worktree: `{workdir}`
- Expected branch: `{expected_branch}`
- Wave: `{wave}`
- Plan: `{plan_path}`
- Checklist: `{checklist_path}`
- Ledger: `{ledger_path}`
- Baseline reference: `{baseline_path}`
- Placement JSON: `{placement_json}`
- Divergence JSON: `{divergence_json}`
- Reason rubric: `{rubric_path}`
- Rationale writer: `{rationale_writer}`
- Rationale analyzer: `{rationale_analyzer}`
- Rationale events log: `{events_jsonl}`
- Validator: `{validator_path}`
- Term lock manifest: `{term_lock_manifest}`
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
5. Use rationale writer once per completed term (no direct rationale edits in CSV):
   `python3 "{rationale_writer}" --checklist-id <ID> --checklist "{checklist_path}" --ledger "{ledger_path}" --placement-json "{placement_json}" --divergence-json "{divergence_json}" --events-jsonl "{events_jsonl}" --batch-id "batch-{batch_number:03d}" --implementer-id <implementer> --action-type <action> --decision-detail <detail> --reason-code <code> --reason-why <text> --semantic-change-flag <flag> --review-attention <attention> --after-file <file> --after-line <line> --after-dp-id <dp> --phase1-status completed --final-quality resolved-high [--deviation-permit <path>]`
6. Ensure ledger fields are complete (`action_type`, `decision_detail`, `reason_*`, `semantic_change_flag`, `review_attention`, after anchors, statuses, rationale UUID metadata).
7. Do not commit or push (orchestrator handles commit).
8. Run validator in progress mode before responding:
   `python3 "{validator_path}" --mode progress --checklist "{checklist_path}" --ledger "{ledger_path}" --baseline "{baseline_path}" --recovery-guardrails --events-jsonl "{events_jsonl}" --json-out "{remediation_dir}/batch-{batch_number:03d}-validate-progress.json" --markdown-out "{remediation_dir}/checklist-progress.md"`
9. Run rationale analyzer and keep artifacts current:
   `python3 "{rationale_analyzer}" --ledger "{ledger_path}" --json-out "{remediation_dir}/batch-{batch_number:03d}-rationale-patterns.json" --markdown-out "{remediation_dir}/batch-{batch_number:03d}-rationale-patterns.md"`

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
    rationale_uuid = (row.get("rationale_uuid") or "").strip()
    recommendation_priority = (row.get("recommendation_priority") or "").strip().lower()
    recommendation_used = (row.get("recommendation_used") or "").strip().lower()
    deviation_permit_path = (row.get("deviation_permit_path") or "").strip()
    deviation_permit_sha256 = (row.get("deviation_permit_sha256") or "").strip()
    deviation_approved_by = (row.get("deviation_approved_by") or "").strip()

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

    if "rationale_uuid" in row:
        if not rationale_uuid:
            return "missing rationale_uuid"
        if not UUID_RE.match(rationale_uuid):
            return "invalid rationale_uuid format"

    if recommendation_priority in {"high", "medium"} and recommendation_used != "yes":
        if not deviation_permit_path:
            return "high/medium non-recommended row missing deviation_permit_path"
        if not deviation_permit_sha256:
            return "high/medium non-recommended row missing deviation_permit_sha256"
        if not deviation_approved_by:
            return "high/medium non-recommended row missing deviation_approved_by"

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
        "placement_json": v2_root / "fls-pr6-placement-fitness-v2.json",
        "divergence_json": v2_root / "fls-pr6-definition-divergence-v2.json",
        "reason_rubric": reports_dir / "glossary-poor-questionable-reason-rubric.md",
        "rationale_writer": reports_dir / "record-rationale-v3.py",
        "rationale_analyzer": reports_dir / "analyze-rationale-patterns-v3.py",
        "validator": reports_dir / "validate-ledger-and-checklist-v3.py",
        "manual_plan": plans_dir / "glossary-pr6-wave-ab-recovery-guardrails-v3-plan.md",
    }


def parse_args() -> argparse.Namespace:
    opencode_config_dir = os.environ.get("OPENCODE_CONFIG_DIR")
    if not opencode_config_dir:
        raise RuntimeError("OPENCODE_CONFIG_DIR is not set")
    config_dir = normalize_path(Path(opencode_config_dir))
    defaults = build_defaults(config_dir)

    parser = argparse.ArgumentParser(
        description="Run v3 Step1/Phase1 remediation in wave-aware OpenCode batches"
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
    parser.add_argument("--placement-json", type=Path, default=defaults["placement_json"])
    parser.add_argument("--divergence-json", type=Path, default=defaults["divergence_json"])
    parser.add_argument("--reason-rubric", type=Path, default=defaults["reason_rubric"])
    parser.add_argument("--rationale-writer", type=Path, default=defaults["rationale_writer"])
    parser.add_argument("--rationale-analyzer", type=Path, default=defaults["rationale_analyzer"])
    parser.add_argument("--validator", type=Path, default=defaults["validator"])
    parser.add_argument("--manual-plan", type=Path, default=defaults["manual_plan"])
    parser.add_argument("--events-jsonl", type=Path)
    parser.add_argument("--strict-baseline-json", type=Path)
    parser.add_argument("--strict-current-json", type=Path)
    parser.add_argument(
        "--strict-command-template",
        default='uv run python tools/glossary-migration-check.py --phase 1 --strict --report "{report}"',
        help="Template command for strict phase checks; must include {report}",
    )
    parser.add_argument("--strict-max-missing", type=int, default=2)
    parser.add_argument("--strict-waiver-file", type=Path)
    parser.add_argument("--enforce-recovery-guardrails", action="store_true")
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
        "placement_json",
        "divergence_json",
        "reason_rubric",
        "rationale_writer",
        "rationale_analyzer",
        "validator",
        "manual_plan",
    ]:
        setattr(args, attr, normalize_path(getattr(args, attr)))

    if args.remediation_dir is not None:
        args.remediation_dir = normalize_path(args.remediation_dir)
    if args.state_file is not None:
        args.state_file = normalize_path(args.state_file)
    if args.events_jsonl is not None:
        args.events_jsonl = normalize_path(args.events_jsonl)
    if args.strict_baseline_json is not None:
        args.strict_baseline_json = normalize_path(args.strict_baseline_json)
    if args.strict_current_json is not None:
        args.strict_current_json = normalize_path(args.strict_current_json)
    if args.strict_waiver_file is not None:
        args.strict_waiver_file = normalize_path(args.strict_waiver_file)

    for field in ["batch_size_wa", "batch_size_wb", "batch_size_wc", "batch_size_wd"]:
        if getattr(args, field) <= 0:
            raise RuntimeError(f"--{field.replace('_', '-')} must be greater than zero")
    if args.max_batches < 0:
        raise RuntimeError("--max-batches must be zero or greater")
    if args.strict_max_missing < 0:
        raise RuntimeError("--strict-max-missing must be zero or greater")
    if "{report}" not in args.strict_command_template:
        raise RuntimeError("--strict-command-template must include '{report}' placeholder")

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
        (args.placement_json, "file"),
        (args.divergence_json, "file"),
        (args.reason_rubric, "file"),
        (args.rationale_writer, "file"),
        (args.rationale_analyzer, "file"),
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

    if args.events_jsonl is None:
        args.events_jsonl = remediation_dir / "reports" / "rationale-events.jsonl"
    if args.strict_baseline_json is None:
        args.strict_baseline_json = remediation_dir / "baseline" / "phase1-strict.json"
    if args.enforce_recovery_guardrails and not args.strict_baseline_json.is_file():
        raise RuntimeError(
            "Recovery guardrails require an existing strict baseline JSON. "
            f"Missing: {args.strict_baseline_json}"
        )

    state_path = args.state_file or (remediation_dir / "orchestrator-v3-state.json")
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

    baseline_dir = remediation_dir / "baseline"
    baseline_dir.mkdir(parents=True, exist_ok=True)
    waves_dir = remediation_dir / "waves"
    waves_dir.mkdir(parents=True, exist_ok=True)
    if args.enforce_recovery_guardrails:
        ensure_ledger_columns(ledger_path, RECOVERY_LEDGER_COLUMNS)
        args.events_jsonl.parent.mkdir(parents=True, exist_ok=True)
        args.events_jsonl.touch(exist_ok=True)

    state_changed = False
    if not state.get("start_head"):
        state["start_head"] = git_head(args.workdir)
        state_changed = True
    if state_changed:
        save_state(state_path, state)

    start_head = str(state.get("start_head"))
    (baseline_dir / "start-head.txt").write_text(f"{start_head}\n", encoding="utf-8")

    progress_md = remediation_dir / "checklist-progress.md"
    preflight_json = remediation_dir / "validate-progress-preflight.json"
    preflight_strict_json: Path | None = args.strict_current_json
    if args.enforce_recovery_guardrails and (not args.dry_run):
        preflight_strict_json = remediation_dir / "baseline" / "phase1-strict-preflight.json"
        run_strict_phase_check(
            strict_command_template=args.strict_command_template,
            workdir=args.workdir,
            report_path=preflight_strict_json,
            description="run strict preflight phase check",
        )

    run_validator(
        validator_path=args.validator,
        mode="progress",
        checklist_path=checklist_path,
        ledger_path=ledger_path,
        baseline_path=baseline_path,
        json_out=preflight_json,
        markdown_out=progress_md,
        recovery_guardrails=args.enforce_recovery_guardrails,
        events_jsonl=args.events_jsonl,
        strict_baseline_json=args.strict_baseline_json,
        strict_current_json=preflight_strict_json,
        strict_max_missing=args.strict_max_missing,
        strict_waiver_file=args.strict_waiver_file,
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
        term_lock_manifest_path = remediation_dir / f"{batch_prefix}-term-lock.json"

        term_lock_payload = build_term_lock_manifest(
            batch_items=batch_items,
            placement_json=args.placement_json,
            divergence_json=args.divergence_json,
        )
        term_lock_payload.update(
            {
                "batch_number": batch_number,
                "batch_prefix": batch_prefix,
                "wave": active_wave,
                "timestamp": utc_timestamp(),
            }
        )
        write_json(term_lock_manifest_path, term_lock_payload)

        prompt = build_batch_prompt(
            batch_items=batch_items,
            wave=active_wave,
            plan_path=args.manual_plan,
            checklist_path=checklist_path,
            ledger_path=ledger_path,
            baseline_path=baseline_path,
            placement_json=args.placement_json,
            divergence_json=args.divergence_json,
            rubric_path=rubric_path,
            rationale_writer=args.rationale_writer,
            rationale_analyzer=args.rationale_analyzer,
            events_jsonl=args.events_jsonl,
            validator_path=args.validator,
            term_lock_manifest=term_lock_manifest_path,
            remediation_dir=remediation_dir,
            workdir=args.workdir,
            expected_branch=args.expected_branch,
            batch_number=batch_number,
        )
        prompt_path = remediation_dir / f"{batch_prefix}-prompt.md"
        prompt_path.write_text(prompt, encoding="utf-8")

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
                    "prompt": str(prompt_path),
                    "term_lock_manifest": str(term_lock_manifest_path),
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

        opencode_log = remediation_dir / f"{batch_prefix}-opencode.jsonl"
        batch_strict_pre_json = remediation_dir / f"{batch_prefix}-strict-pre.json"
        batch_strict_post_json = remediation_dir / f"{batch_prefix}-strict-post.json"

        try:
            run_strict_phase_check(
                strict_command_template=args.strict_command_template,
                workdir=args.workdir,
                report_path=batch_strict_pre_json,
                description=f"run strict pre-check for {batch_prefix}",
            )

            session_id = run_opencode_batch(
                opencode_bin=args.opencode_bin,
                workdir=args.workdir,
                prompt=prompt,
                log_path=opencode_log,
                session_id=state.get("session_id"),
                attach_url=args.attach_url,
                model=args.model,
                agent=args.agent,
                title=f"V3 glossary remediation {run_id}",
                attached_files=[
                    args.manual_plan,
                    checklist_path,
                    ledger_path,
                    baseline_path,
                    args.placement_json,
                    args.divergence_json,
                    rubric_path,
                    args.rationale_writer,
                    args.rationale_analyzer,
                    args.validator,
                    term_lock_manifest_path,
                ],
                permission_override=(
                    args.permission_override if args.permission_override.strip() else None
                ),
                stream_output=args.stream_opencode_output,
            )
            state["last_session_id"] = session_id
            save_state(state_path, state)

            run_strict_phase_check(
                strict_command_template=args.strict_command_template,
                workdir=args.workdir,
                report_path=batch_strict_post_json,
                description=f"run strict post-check for {batch_prefix}",
            )

            batch_validate_json = remediation_dir / f"{batch_prefix}-validate-progress.json"
            validator_result = run_validator(
                validator_path=args.validator,
                mode="progress",
                checklist_path=checklist_path,
                ledger_path=ledger_path,
                baseline_path=baseline_path,
                json_out=batch_validate_json,
                markdown_out=progress_md,
                recovery_guardrails=args.enforce_recovery_guardrails,
                events_jsonl=args.events_jsonl,
                strict_baseline_json=args.strict_baseline_json,
                strict_current_json=batch_strict_post_json,
                strict_max_missing=args.strict_max_missing,
                strict_waiver_file=args.strict_waiver_file,
                allow_failure=True,
            )

            passed_ids, quarantined = evaluate_batch_results(
                batch_items=batch_items,
                checklist_path=checklist_path,
                ledger_path=ledger_path,
            )

            if validator_result.returncode != 0:
                validator_quarantined, validator_hard_codes, unresolved_validator_errors = (
                    classify_validator_failures_for_batch(
                        validator_errors=validator_result.errors,
                        batch_ids=batch_ids,
                    )
                )

                if validator_hard_codes:
                    raise RuntimeError(
                        "batch validator hard-fail code(s): "
                        f"{','.join(validator_hard_codes)}"
                    )

                if (not validator_quarantined) and (not validator_result.errors):
                    raise RuntimeError(
                        "batch validator failed without structured error payload"
                    )

                merge_quarantine_reasons(quarantined, validator_quarantined)

                if unresolved_validator_errors:
                    unresolved_preview = " | ".join(unresolved_validator_errors[:4])
                    raise RuntimeError(
                        "batch validator produced unresolved errors after quarantine classification: "
                        f"{unresolved_preview}"
                    )

            passed_ids = [
                checklist_id for checklist_id in passed_ids if checklist_id not in quarantined
            ]

            post_quarantine_validate_json: Path | None = None
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

                post_quarantine_validate_json = (
                    remediation_dir / f"{batch_prefix}-validate-progress-post-quarantine.json"
                )
                run_validator(
                    validator_path=args.validator,
                    mode="progress",
                    checklist_path=checklist_path,
                    ledger_path=ledger_path,
                    baseline_path=baseline_path,
                    json_out=post_quarantine_validate_json,
                    markdown_out=progress_md,
                    recovery_guardrails=args.enforce_recovery_guardrails,
                    events_jsonl=args.events_jsonl,
                    strict_baseline_json=args.strict_baseline_json,
                    strict_current_json=batch_strict_post_json,
                    strict_max_missing=args.strict_max_missing,
                    strict_waiver_file=args.strict_waiver_file,
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
                recovery_guardrails=args.enforce_recovery_guardrails,
                events_jsonl=args.events_jsonl,
                strict_baseline_json=args.strict_baseline_json,
                strict_current_json=batch_strict_post_json,
                strict_max_missing=args.strict_max_missing,
                strict_waiver_file=args.strict_waiver_file,
            )

            batch_patterns_json = remediation_dir / f"{batch_prefix}-rationale-patterns.json"
            batch_patterns_md = remediation_dir / f"{batch_prefix}-rationale-patterns.md"
            run_rationale_analyzer(
                analyzer_path=args.rationale_analyzer,
                ledger_path=ledger_path,
                json_out=batch_patterns_json,
                markdown_out=batch_patterns_md,
                workdir=args.workdir,
            )

            ledger_rows_after_commit = read_ledger_rows(ledger_path)
            batch_metrics = compute_batch_metrics(
                passed_items=passed_items,
                ledger_rows=ledger_rows_after_commit,
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
                "strict_pre": str(batch_strict_pre_json),
                "strict_post": str(batch_strict_post_json),
                "validator_progress": str(batch_validate_json),
                "validator_progress_post_quarantine": (
                    str(post_quarantine_validate_json)
                    if post_quarantine_validate_json is not None
                    else None
                ),
                "validator_failure_codes": validator_result.failure_codes,
                "validator_post_commit": str(post_commit_json),
                "rationale_patterns_json": str(batch_patterns_json),
                "rationale_patterns_md": str(batch_patterns_md),
                "recommendation_compliance_rate": batch_metrics["recommendation_compliance_rate"],
                "recommendation_compliant_count": batch_metrics["recommendation_compliant_count"],
                "high_medium_count": batch_metrics["high_medium_total"],
                "deviation_permit_count": batch_metrics["deviation_permit_count"],
                "max_rationale_similarity": batch_metrics["max_rationale_similarity"],
                "max_rationale_similarity_pair": batch_metrics["max_rationale_similarity_pair"],
                "moved_term_count": batch_metrics["moved_term_count"],
                "moved_terms": batch_metrics["moved_terms"],
                "timestamp": utc_timestamp(),
            }
            write_json(remediation_dir / f"{batch_prefix}-summary.json", batch_summary)

            state.setdefault("batches", []).append(batch_summary)
            post_batch_items = parse_checklist(checklist_path)
            wa_total, wa_checked = wave_parent_counts(post_batch_items, "WA")
            if wa_total > 0 and wa_checked == wa_total and not state.get("wave_a_end_head"):
                state["wave_a_end_head"] = commit_hash
                (waves_dir / "wave-a-end-head.txt").write_text(
                    f"{commit_hash}\n", encoding="utf-8"
                )
            save_state(state_path, state)

            completed_batches += 1
            print(f"{batch_prefix} committed: {commit_hash}")

            if args.pause_seconds > 0:
                time.sleep(args.pause_seconds)

        except Exception as exc:  # noqa: BLE001
            exception_text = str(exc)
            exception_failure_codes = find_failure_codes(exception_text)
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
                "error": exception_text,
                "failure_codes": exception_failure_codes,
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
                    "error": exception_text,
                    "failure_codes": exception_failure_codes,
                    "timestamp": failure_payload["timestamp"],
                }
            )
            save_state(state_path, state)
            raise RuntimeError(
                f"{exc}; run-local checklist/ledger and git worktree restored to pre-batch state"
            )

    final_items = parse_checklist(checklist_path)
    remaining = [
        item
        for item in final_items.values()
        if item.wave in {"WA", "WB", "WC", "WD"} and not item.parent_checked
    ]

    final_strict_json: Path | None = args.strict_current_json
    if args.enforce_recovery_guardrails and (not args.dry_run):
        final_strict_json = remediation_dir / "validate-final-strict-current.json"
        run_strict_phase_check(
            strict_command_template=args.strict_command_template,
            workdir=args.workdir,
            report_path=final_strict_json,
            description="run strict final phase check",
        )

    if not args.skip_final_validator:
        if not remaining and not args.dry_run:
            if state.get("gate_b_plus_status") == "passed":
                final_json = remediation_dir / "validate-final.json"
                run_validator(
                    validator_path=args.validator,
                    mode="final",
                    checklist_path=checklist_path,
                    ledger_path=ledger_path,
                    baseline_path=baseline_path,
                    json_out=final_json,
                    markdown_out=progress_md,
                    recovery_guardrails=args.enforce_recovery_guardrails,
                    events_jsonl=args.events_jsonl,
                    strict_baseline_json=args.strict_baseline_json,
                    strict_current_json=final_strict_json,
                    strict_max_missing=args.strict_max_missing,
                    strict_waiver_file=args.strict_waiver_file,
                )
                print(f"Final validator completed: {final_json}")
            else:
                print(
                    "Skipping final validator because Gate B+ is not passed "
                    "(boundary run or external v3 artifacts missing)."
                )

    wa_total, wa_checked = wave_parent_counts(final_items, "WA")
    wb_total, wb_checked = wave_parent_counts(final_items, "WB")
    wave_a_complete = wa_total > 0 and wa_checked == wa_total
    wave_b_complete = wb_total > 0 and wb_checked == wb_total
    has_wave_ab_scope = (wa_total + wb_total) > 0

    end_head = git_head(args.workdir)
    state["end_head"] = end_head
    if wave_a_complete and not state.get("wave_a_end_head"):
        state["wave_a_end_head"] = end_head
    if state.get("wave_a_end_head"):
        (waves_dir / "wave-a-end-head.txt").write_text(
            f"{state['wave_a_end_head']}\n", encoding="utf-8"
        )
    (waves_dir / "wave-b-end-head.txt").write_text(f"{end_head}\n", encoding="utf-8")
    save_state(state_path, state)

    new_commit_count = git_commit_range_count(args.workdir, start_head, end_head)
    new_commit_hashes = git_commit_range_hashes(args.workdir, start_head, end_head)
    changed_src_files = git_changed_files_in_range(
        args.workdir,
        start_head,
        end_head,
        paths=["src"],
    )

    batches_completed_total = len(state.get("batches", []))
    integrity_verdict, integrity_path = write_execution_integrity_report(
        remediation_dir=remediation_dir,
        start_head=start_head,
        wave_a_end_head=state.get("wave_a_end_head"),
        end_head=end_head,
        new_commit_count=new_commit_count,
        new_commit_hashes=new_commit_hashes,
        changed_src_files=changed_src_files,
        has_wave_ab_scope=has_wave_ab_scope,
        wave_a_complete=wave_a_complete,
        wave_b_complete=wave_b_complete,
        batches_completed_current_run=completed_batches,
        batches_completed_total=batches_completed_total,
        dry_run=args.dry_run,
    )

    overall_patterns_json = remediation_dir / "rationale-patterns.json"
    overall_patterns_md = remediation_dir / "rationale-patterns.md"
    run_rationale_analyzer(
        analyzer_path=args.rationale_analyzer,
        ledger_path=ledger_path,
        json_out=overall_patterns_json,
        markdown_out=overall_patterns_md,
        workdir=args.workdir,
    )

    failed_batches_payload = json.dumps(state.get("failed_batches", []), sort_keys=True)
    hard_fail_codes = find_failure_codes(failed_batches_payload)

    final_summary = {
        "run_id": run_id,
        "remediation_dir": str(remediation_dir),
        "workdir": str(args.workdir),
        "expected_branch": args.expected_branch,
        "last_session_id": state.get("last_session_id"),
        "gate_b_plus_status": state.get("gate_b_plus_status"),
        "batches_completed": completed_batches,
        "batches_completed_total": batches_completed_total,
        "batches_failed": len(state.get("failed_batches", [])),
        "run_local_checklist": str(checklist_path),
        "run_local_ledger": str(ledger_path),
        "events_jsonl": str(args.events_jsonl),
        "strict_command_template": args.strict_command_template,
        "strict_baseline_json": str(args.strict_baseline_json),
        "strict_current_json": str(final_strict_json) if final_strict_json is not None else None,
        "recovery_guardrails": args.enforce_recovery_guardrails,
        "canonical_checklist_template": str(args.checklist),
        "start_head": start_head,
        "wave_a_end_head": state.get("wave_a_end_head"),
        "end_head": end_head,
        "new_commit_count": new_commit_count,
        "new_commit_hashes": new_commit_hashes,
        "changed_src_files": changed_src_files,
        "execution_integrity_verdict": integrity_verdict,
        "execution_integrity_report": str(integrity_path),
        "rationale_patterns_json": str(overall_patterns_json),
        "rationale_patterns_md": str(overall_patterns_md),
        "hard_fail_codes": hard_fail_codes,
        "remaining_parent_ids": [
            item.checklist_id
            for item in sorted(remaining, key=lambda value: parse_checklist_id(value.checklist_id))
        ],
        "timestamp": utc_timestamp(),
    }
    summary_path = remediation_dir / "orchestrator-summary.json"
    write_json(summary_path, final_summary)

    print("Orchestration complete.")
    print(f"Run directory: {remediation_dir}")
    print(f"Summary: {summary_path}")

    if integrity_verdict != "pass":
        print(
            (
                "Execution integrity failed with verdict "
                f"'{integrity_verdict}'. See {integrity_path}"
            ),
            file=sys.stderr,
        )
        return 2

    if hard_fail_codes:
        print(
            (
                "Run ended with hard fail code(s): "
                f"{', '.join(hard_fail_codes)}. See {summary_path}"
            ),
            file=sys.stderr,
        )
        return 2

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
