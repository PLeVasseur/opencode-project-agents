#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import json
import re
import itertools
from pathlib import Path


PARENT_RE = re.compile(
    r"^- \[(?P<mark>[ xX])\] (?P<id>(?:W[ABCD]|QQ)-\d{3}) term="
)
SUB_RE = re.compile(
    r"^  - \[(?P<mark>[ xX])\] (?P<id>(?:W[ABCD]|QQ)-\d{3})\.(?P<idx>\d+)\b"
)

BASELINE_COLUMNS = [
    "term",
    "wave",
    "source_set",
    "baseline_file",
    "baseline_line",
    "baseline_dp_id",
    "baseline_section",
    "baseline_commit",
    "first_use_file",
    "first_use_line",
    "recommended_file",
    "recommended_section",
    "placement_priority",
    "placement_fitness_rating",
    "divergence_match_category",
    "divergence_reliability",
    "divergence_similarity",
    "before_evidence_ref",
]

AFTER_COLUMNS = ["after_file", "after_line", "after_dp_id", "after_commit"]

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

ALLOWED_SEMANTIC_FLAGS = {
    "none",
    "clarification-only",
    "normative-risk",
}

ALLOWED_REVIEW_ATTENTION = {
    "",
    "none",
    "required",
    "recommended",
}

UUID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
    re.IGNORECASE,
)

BOILERPLATE_REASONS = [
    re.compile(r"Before .+\(.+\) used :dt:`.+`.+After .+uses :t:`", re.IGNORECASE | re.DOTALL),
]

FOUNDATIONAL_REQUIRED_FILES = {
    "value": "values.rst",
    "expression": "expressions.rst",
    "trait": "types-and-traits.rst",
    "item": "items.rst",
    "field": "types-and-traits.rst",
    "reference": "ownership-and-deconstruction.rst",
    "implementation": "implementations.rst",
    "method": "functions.rst",
    "crate": "program-structure-and-compilation.rst",
    "statement": "statements.rst",
}

RECOVERY_EXTRA_COLUMNS = [
    "rationale_uuid",
    "rationale_inserted_at_utc",
    "rationale_text_sha256",
    "recommendation_priority",
    "recommendation_used",
    "deviation_permit_path",
    "deviation_permit_sha256",
    "deviation_approved_by",
]


def parse_checklist_id(value: str) -> tuple[int, int, str]:
    prefix, number_text = value.split("-", 1)
    prefix_order = {"WA": 1, "WB": 2, "WC": 3, "WD": 4, "QQ": 5}
    return (prefix_order.get(prefix, 99), int(number_text), value)


def parse_checklist(
    path: Path,
    *,
    subitems_per_parent: int,
    expected_ids: set[str] | None,
) -> tuple[dict, list[str]]:
    errors: list[str] = []
    parent_marks: dict[str, bool] = {}
    sub_marks: dict[str, dict[int, bool]] = {}

    lines = path.read_text(encoding="utf-8").splitlines()
    for line_number, line in enumerate(lines, start=1):
        parent_match = PARENT_RE.match(line)
        if parent_match:
            checklist_id = parent_match.group("id")
            is_checked = parent_match.group("mark").lower() == "x"
            if checklist_id in parent_marks:
                errors.append(f"checklist line {line_number}: duplicate parent item {checklist_id}")
            parent_marks[checklist_id] = is_checked
            continue

        sub_match = SUB_RE.match(line)
        if sub_match:
            checklist_id = sub_match.group("id")
            sub_index = int(sub_match.group("idx"))
            is_checked = sub_match.group("mark").lower() == "x"
            item_marks = sub_marks.setdefault(checklist_id, {})
            if sub_index in item_marks:
                errors.append(
                    f"checklist line {line_number}: duplicate sub-item {checklist_id}.{sub_index}"
                )
            item_marks[sub_index] = is_checked

    parent_ids = set(parent_marks)
    if expected_ids is not None:
        missing = sorted(expected_ids - parent_ids, key=parse_checklist_id)
        extra = sorted(parent_ids - expected_ids, key=parse_checklist_id)
        if missing:
            errors.append(f"missing parent checklist IDs: {', '.join(missing[:20])}")
        if extra:
            errors.append(f"unexpected parent checklist IDs: {', '.join(extra[:20])}")

    expected_sub_index = set(range(1, subitems_per_parent + 1))
    for checklist_id in sorted(parent_ids, key=parse_checklist_id):
        seen = set(sub_marks.get(checklist_id, {}).keys())
        missing = sorted(expected_sub_index - seen)
        extra = sorted(seen - expected_sub_index)
        if missing:
            errors.append(
                f"{checklist_id}: missing sub-items {', '.join(str(index) for index in missing)}"
            )
        if extra:
            errors.append(
                f"{checklist_id}: unexpected sub-items {', '.join(str(index) for index in extra)}"
            )

    for checklist_id in sorted(set(sub_marks) - parent_ids, key=parse_checklist_id):
        errors.append(f"{checklist_id}: has sub-items but no parent row")

    parent_checked = sum(1 for mark in parent_marks.values() if mark)
    parent_unchecked = sum(1 for mark in parent_marks.values() if not mark)
    sub_total = 0
    sub_checked = 0
    sub_unchecked = 0
    for item_marks in sub_marks.values():
        sub_total += len(item_marks)
        sub_checked += sum(1 for mark in item_marks.values() if mark)
        sub_unchecked += sum(1 for mark in item_marks.values() if not mark)

    summary = {
        "parent_total": len(parent_marks),
        "parent_checked": parent_checked,
        "parent_unchecked": parent_unchecked,
        "sub_total": sub_total,
        "sub_checked": sub_checked,
        "sub_unchecked": sub_unchecked,
        "parent_marks": parent_marks,
        "sub_marks": sub_marks,
    }
    return summary, errors


def load_csv_by_id(path: Path, label: str) -> tuple[dict[str, dict[str, str]], list[str], list[str]]:
    errors: list[str] = []
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)

    if "checklist_id" not in fieldnames:
        errors.append(f"{label}: missing required column checklist_id")

    rows_by_id: dict[str, dict[str, str]] = {}
    for index, row in enumerate(rows, start=2):
        checklist_id = (row.get("checklist_id") or "").strip()
        if not checklist_id:
            errors.append(f"{label}: row {index} missing checklist_id")
            continue
        if checklist_id in rows_by_id:
            errors.append(f"{label}: duplicate checklist_id {checklist_id}")
            continue
        rows_by_id[checklist_id] = row

    return rows_by_id, fieldnames, errors


def require_columns(fieldnames: list[str], required: list[str], label: str, errors: list[str]) -> None:
    missing = [column for column in required if column not in fieldnames]
    if missing:
        errors.append(f"{label}: missing required columns: {', '.join(missing)}")


def validate_alignment(
    expected: set[str],
    checklist_ids: set[str],
    ledger_ids: set[str],
    baseline_ids: set[str],
    errors: list[str],
) -> None:
    for label, ids in [
        ("checklist", checklist_ids),
        ("ledger", ledger_ids),
        ("baseline", baseline_ids),
    ]:
        missing = sorted(expected - ids, key=parse_checklist_id)
        extra = sorted(ids - expected, key=parse_checklist_id)
        if missing:
            errors.append(f"{label}: missing expected IDs: {', '.join(missing[:20])}")
        if extra:
            errors.append(f"{label}: unexpected IDs: {', '.join(extra[:20])}")

    if checklist_ids != ledger_ids:
        errors.append("checklist and ledger ID sets differ")
    if checklist_ids != baseline_ids:
        errors.append("checklist and baseline ID sets differ")


def check_baseline_immutability(
    checklist_ids: list[str],
    ledger_rows: dict[str, dict[str, str]],
    baseline_rows: dict[str, dict[str, str]],
    errors: list[str],
) -> None:
    for checklist_id in checklist_ids:
        ledger_row = ledger_rows.get(checklist_id)
        baseline_row = baseline_rows.get(checklist_id)
        if ledger_row is None or baseline_row is None:
            continue
        for column in BASELINE_COLUMNS:
            if (ledger_row.get(column) or "") != (baseline_row.get(column) or ""):
                errors.append(f"{checklist_id}: baseline column changed ({column})")


def is_row_completed(row: dict[str, str]) -> bool:
    phase1 = (row.get("phase1_status") or "").strip().lower()
    final_quality = (row.get("final_quality") or "").strip().lower()
    return phase1 == "completed" or final_quality in {
        "resolved-high",
        "blocked",
        "resolved-exception",
    }


def require_non_empty(
    row: dict[str, str], checklist_id: str, columns: list[str], errors: list[str], label: str
) -> None:
    for column in columns:
        if not (row.get(column) or "").strip():
            errors.append(f"{checklist_id}: missing {column} ({label})")


def check_semantic_fields(
    checklist_id: str,
    row: dict[str, str],
    errors: list[str],
    *,
    label: str,
) -> None:
    action_type = (row.get("action_type") or "").strip()
    semantic_flag = (row.get("semantic_change_flag") or "").strip()
    review_attention = (row.get("review_attention") or "").strip()

    if action_type not in ALLOWED_ACTION_TYPES:
        errors.append(f"{checklist_id}: invalid action_type '{action_type}' ({label})")

    if semantic_flag not in ALLOWED_SEMANTIC_FLAGS:
        errors.append(f"{checklist_id}: invalid semantic_change_flag '{semantic_flag}' ({label})")

    if review_attention not in ALLOWED_REVIEW_ATTENTION:
        errors.append(f"{checklist_id}: invalid review_attention '{review_attention}' ({label})")

    if "rewrite" in action_type and review_attention != "required":
        errors.append(f"{checklist_id}: rewrite action requires review_attention=required ({label})")


def check_action_and_reason(
    checklist_id: str,
    row: dict[str, str],
    min_reason_length: int,
    errors: list[str],
    *,
    label: str,
) -> None:
    action_type = (row.get("action_type") or "").strip()
    decision_detail = (row.get("decision_detail") or "").strip()
    reason_code = (row.get("reason_code") or "").strip()
    reason_quality = (row.get("reason_quality") or "").strip().lower()
    reason_why = (row.get("reason_why") or "").strip()

    if action_type not in ALLOWED_ACTION_TYPES:
        errors.append(f"{checklist_id}: invalid action_type '{action_type}' ({label})")

    if not decision_detail:
        errors.append(f"{checklist_id}: missing decision_detail ({label})")

    if reason_code not in ALLOWED_REASON_CODES:
        errors.append(f"{checklist_id}: invalid reason_code '{reason_code}' ({label})")

    if reason_quality != "pass":
        errors.append(f"{checklist_id}: reason_quality must be pass ({label})")

    if len(reason_why) < min_reason_length:
        errors.append(
            f"{checklist_id}: reason_why shorter than {min_reason_length} characters ({label})"
        )

    if reason_code != "blocked":
        require_non_empty(row, checklist_id, AFTER_COLUMNS, errors, label)

    check_semantic_fields(checklist_id, row, errors, label=label)


def check_rubric_subitems(
    checklist_id: str,
    sub_marks: dict[int, bool],
    row: dict[str, str],
    min_reason_length: int,
    errors: list[str],
) -> None:
    for sub_index, sub_label in [
        (1, "before snapshot"),
        (2, "action recorded"),
        (3, "reason quality"),
        (4, "semantic review"),
        (5, "after snapshot"),
        (6, "status finalized"),
    ]:
        if not sub_marks.get(sub_index, False):
            continue

        if sub_index == 1:
            require_non_empty(
                row,
                checklist_id,
                [
                    "baseline_file",
                    "baseline_line",
                    "baseline_dp_id",
                    "baseline_commit",
                ],
                errors,
                sub_label,
            )

        if sub_index == 2:
            require_non_empty(
                row,
                checklist_id,
                ["action_type", "decision_detail", "reason_code"],
                errors,
                sub_label,
            )

        if sub_index == 3:
            check_action_and_reason(
                checklist_id,
                row,
                min_reason_length,
                errors,
                label=sub_label,
            )

        if sub_index == 4:
            require_non_empty(
                row,
                checklist_id,
                ["semantic_change_flag", "review_attention"],
                errors,
                sub_label,
            )
            check_semantic_fields(checklist_id, row, errors, label=sub_label)

        if sub_index == 5:
            require_non_empty(row, checklist_id, AFTER_COLUMNS, errors, sub_label)

        if sub_index == 6:
            require_non_empty(
                row,
                checklist_id,
                ["phase1_status", "final_quality"],
                errors,
                sub_label,
            )
            if (row.get("final_quality") or "").strip().lower() == "pending":
                errors.append(f"{checklist_id}: final_quality is pending ({sub_label})")


def write_markdown(path: Path, summary: dict, errors: list[str]) -> None:
    checklist = summary["checklist"]
    lines = [
        "# Checklist and ledger validation (v2)",
        "",
        f"- Mode: `{summary['mode']}`",
        f"- Parent items: `{checklist['parent_checked']}/{checklist['parent_total']}` checked",
        f"- Sub-items: `{checklist['sub_checked']}/{checklist['sub_total']}` checked",
        f"- Ledger rows: `{summary['ledger_rows']}`",
        f"- Baseline rows: `{summary['baseline_rows']}`",
        f"- Completed ledger rows: `{summary['completed_rows']}`",
        f"- Resolved-high rows: `{summary['resolved_high_rows']}`",
        f"- Error count: `{len(errors)}`",
        "",
    ]

    if errors:
        lines.append("## Errors")
        lines.append("")
        for error in errors[:200]:
            lines.append(f"- {error}")
        if len(errors) > 200:
            lines.append(f"- ... {len(errors) - 200} more errors")
    else:
        lines.append("All checks passed.")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_expected_ids(path: Path) -> set[str]:
    ids: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        value = line.strip()
        if not value or value.startswith("#"):
            continue
        ids.add(value)
    return ids


def load_events(path: Path) -> tuple[dict[str, list[dict]], list[str]]:
    errors: list[str] = []
    events: dict[str, list[dict]] = {}
    if not path.is_file():
        return events, [f"events file does not exist: {path}"]

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        text = line.strip()
        if not text:
            continue
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            errors.append(f"events line {line_number}: invalid JSON")
            continue

        checklist_id = (payload.get("checklist_id") or "").strip()
        rationale_uuid = (payload.get("rationale_uuid") or "").strip()
        if not checklist_id:
            errors.append(f"events line {line_number}: missing checklist_id")
            continue
        if not rationale_uuid:
            errors.append(f"events line {line_number}: missing rationale_uuid")
            continue
        events.setdefault(checklist_id, []).append(payload)

    return events, errors


def jaccard_similarity(a: str, b: str) -> float:
    tokens_a = {token for token in re.split(r"\s+", a.lower().strip()) if token}
    tokens_b = {token for token in re.split(r"\s+", b.lower().strip()) if token}
    if not tokens_a and not tokens_b:
        return 1.0
    if not tokens_a or not tokens_b:
        return 0.0
    return len(tokens_a & tokens_b) / len(tokens_a | tokens_b)


def extract_missing_count(path: Path) -> tuple[int | None, str | None]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return None, f"could not parse strict report {path}: {exc}"

    checks = payload.get("checks", [])
    for check in checks:
        details = check.get("details") or {}
        value = details.get("missing_count")
        if isinstance(value, int):
            return value, None
    return None, f"strict report missing details.missing_count: {path}"


def enforce_recovery_guardrails(
    *,
    ordered_ids: list[str],
    ledger_rows: dict[str, dict[str, str]],
    args: argparse.Namespace,
    errors: list[str],
) -> None:
    completed_rows: list[tuple[str, dict[str, str]]] = []
    for checklist_id in ordered_ids:
        row = ledger_rows.get(checklist_id)
        if row is None:
            continue
        if is_row_completed(row):
            completed_rows.append((checklist_id, row))

    seen_uuid: set[str] = set()
    events_by_id: dict[str, list[dict]] = {}
    events_required = False
    if args.events_jsonl is None:
        errors.append("recovery guardrails require --events-jsonl")
    else:
        events_required = True
        events_by_id, event_errors = load_events(args.events_jsonl)
        errors.extend(event_errors)

    for checklist_id, row in completed_rows:
        rationale_uuid = (row.get("rationale_uuid") or "").strip()
        inserted_at = (row.get("rationale_inserted_at_utc") or "").strip()
        rationale_sha = (row.get("rationale_text_sha256") or "").strip()
        reason_why = (row.get("reason_why") or "").strip()

        if not rationale_uuid:
            errors.append(f"{checklist_id}: missing rationale_uuid (recovery)")
        elif not UUID_RE.match(rationale_uuid):
            errors.append(f"{checklist_id}: invalid rationale_uuid format (recovery)")
        elif rationale_uuid in seen_uuid:
            errors.append(f"{checklist_id}: duplicate rationale_uuid {rationale_uuid} (recovery)")
        else:
            seen_uuid.add(rationale_uuid)

        if not inserted_at:
            errors.append(f"{checklist_id}: missing rationale_inserted_at_utc (recovery)")
        if not rationale_sha:
            errors.append(f"{checklist_id}: missing rationale_text_sha256 (recovery)")
        elif not re.fullmatch(r"[0-9a-f]{64}", rationale_sha):
            errors.append(f"{checklist_id}: rationale_text_sha256 is not hex sha256 (recovery)")

        for pattern in BOILERPLATE_REASONS:
            if pattern.search(reason_why):
                errors.append(f"{checklist_id}: reason_why matches rejected boilerplate (recovery)")
                break

        priority = (row.get("recommendation_priority") or "").strip().lower()
        used = (row.get("recommendation_used") or "").strip().lower()
        if priority in {"high", "medium"} and used != "yes":
            permit_path = (row.get("deviation_permit_path") or "").strip()
            permit_sha = (row.get("deviation_permit_sha256") or "").strip()
            approved_by = (row.get("deviation_approved_by") or "").strip()
            if not permit_path:
                errors.append(f"{checklist_id}: high/medium non-recommended decision missing deviation_permit_path")
            if not permit_sha:
                errors.append(f"{checklist_id}: high/medium non-recommended decision missing deviation_permit_sha256")
            if not approved_by:
                errors.append(f"{checklist_id}: high/medium non-recommended decision missing deviation_approved_by")

        if events_required:
            matches = [
                event
                for event in events_by_id.get(checklist_id, [])
                if (event.get("rationale_uuid") or "").strip() == rationale_uuid
            ]
            if not matches:
                errors.append(
                    f"{checklist_id}: no matching rationale event for rationale_uuid={rationale_uuid}"
                )

    waves: dict[str, list[tuple[str, dict[str, str]]]] = {}
    for checklist_id, row in completed_rows:
        wave = (row.get("wave") or "").strip().upper()
        waves.setdefault(wave, []).append((checklist_id, row))

    for wave, wave_rows in waves.items():
        if not wave_rows:
            continue

        pair_counts: dict[tuple[str, str], int] = {}
        action_types: set[str] = set()
        high_medium_total = 0
        deviation_count = 0

        reasons = []
        for checklist_id, row in wave_rows:
            action = (row.get("action_type") or "").strip()
            reason_code = (row.get("reason_code") or "").strip()
            pair = (action, reason_code)
            pair_counts[pair] = pair_counts.get(pair, 0) + 1
            if action:
                action_types.add(action)

            reasons.append((checklist_id, (row.get("reason_why") or "").strip()))

            priority = (row.get("recommendation_priority") or "").strip().lower()
            used = (row.get("recommendation_used") or "").strip().lower()
            if priority in {"high", "medium"}:
                high_medium_total += 1
                if used != "yes":
                    deviation_count += 1

        max_pair_fraction = max(pair_counts.values()) / len(wave_rows)
        if max_pair_fraction > args.max_action_reason_fraction:
            errors.append(
                f"{wave}: action+reason concentration {max_pair_fraction:.3f} exceeds "
                f"{args.max_action_reason_fraction:.3f}"
            )

        if len(wave_rows) > args.min_wave_size_for_multi_action and len(action_types) < args.min_unique_actions:
            errors.append(
                f"{wave}: requires >= {args.min_unique_actions} unique action_type values when "
                f"row count > {args.min_wave_size_for_multi_action}"
            )

        if high_medium_total > 0:
            deviation_fraction = deviation_count / high_medium_total
            if deviation_fraction > args.max_deviation_fraction:
                errors.append(
                    f"{wave}: deviation concentration {deviation_fraction:.3f} exceeds "
                    f"{args.max_deviation_fraction:.3f}"
                )

        for (id_a, reason_a), (id_b, reason_b) in itertools.combinations(reasons, 2):
            similarity = jaccard_similarity(reason_a, reason_b)
            if similarity > args.max_reason_jaccard:
                errors.append(
                    f"{wave}: reason_why similarity {similarity:.3f} exceeds "
                    f"{args.max_reason_jaccard:.3f} for {id_a} vs {id_b}"
                )
                break

    for checklist_id, row in completed_rows:
        term = (row.get("term") or "").strip()
        required_file = FOUNDATIONAL_REQUIRED_FILES.get(term)
        if required_file is None:
            continue
        after_file = (row.get("after_file") or "").strip()
        if after_file != required_file:
            errors.append(
                f"{checklist_id}: foundational placement requires after_file={required_file}, got {after_file}"
            )

    if args.strict_baseline_json is not None and args.strict_current_json is not None:
        baseline_missing, baseline_error = extract_missing_count(args.strict_baseline_json)
        current_missing, current_error = extract_missing_count(args.strict_current_json)
        if baseline_error:
            errors.append(baseline_error)
        if current_error:
            errors.append(current_error)
        if baseline_missing is not None and current_missing is not None:
            if current_missing > args.strict_max_missing:
                waiver_ok = args.strict_waiver_file is not None and args.strict_waiver_file.is_file()
                if not waiver_ok:
                    errors.append(
                        "strict missing_count regression without waiver: "
                        f"baseline={baseline_missing}, current={current_missing}, "
                        f"max={args.strict_max_missing}"
                    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate v2 checklist + ledger remediation gates")
    parser.add_argument("--checklist", type=Path, required=True)
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument(
        "--mode",
        choices=["progress", "init", "gate", "final"],
        default="progress",
        help="init=all unchecked, gate=all checked, final=all checked + allowed final qualities",
    )
    parser.add_argument(
        "--expected-parent-count",
        type=int,
        default=None,
        help="Optional expected parent count; if omitted checklist count is used",
    )
    parser.add_argument(
        "--expected-id-list",
        type=Path,
        help="Optional file listing expected checklist IDs (one per line)",
    )
    parser.add_argument("--subitems-per-parent", type=int, default=6)
    parser.add_argument("--min-reason-length", type=int, default=80)
    parser.add_argument(
        "--final-allowed-quality",
        action="append",
        default=["resolved-high"],
        help="Allowed final_quality value(s) in final mode (repeatable)",
    )
    parser.add_argument(
        "--recovery-guardrails",
        action="store_true",
        help="Enable recommendation/UUID/deviation/strict guardrails",
    )
    parser.add_argument(
        "--events-jsonl",
        type=Path,
        help="Rationale events jsonl for recovery guardrail checks",
    )
    parser.add_argument(
        "--strict-baseline-json",
        type=Path,
        help="Strict check JSON baseline report",
    )
    parser.add_argument(
        "--strict-current-json",
        type=Path,
        help="Strict check JSON current report",
    )
    parser.add_argument(
        "--strict-max-missing",
        type=int,
        default=2,
        help="Max allowed strict missing_count when recovery guardrails are enabled",
    )
    parser.add_argument(
        "--strict-waiver-file",
        type=Path,
        help="Optional waiver file path to allow strict missing regression",
    )
    parser.add_argument(
        "--max-action-reason-fraction",
        type=float,
        default=0.60,
        help="Maximum allowed concentration for one action_type+reason_code pair",
    )
    parser.add_argument(
        "--max-reason-jaccard",
        type=float,
        default=0.80,
        help="Maximum allowed Jaccard similarity between two reason_why entries",
    )
    parser.add_argument(
        "--max-deviation-fraction",
        type=float,
        default=0.30,
        help="Maximum allowed deviation permit fraction among high/medium terms",
    )
    parser.add_argument(
        "--min-wave-size-for-multi-action",
        type=int,
        default=20,
        help="Require multiple action types when wave has more than this many completed rows",
    )
    parser.add_argument(
        "--min-unique-actions",
        type=int,
        default=2,
        help="Minimum unique action_type values when multi-action gate applies",
    )
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--markdown-out", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors: list[str] = []

    explicit_expected_ids: set[str] | None = None
    if args.expected_id_list is not None:
        explicit_expected_ids = parse_expected_ids(args.expected_id_list)

    checklist_summary, checklist_errors = parse_checklist(
        args.checklist,
        subitems_per_parent=args.subitems_per_parent,
        expected_ids=explicit_expected_ids,
    )
    errors.extend(checklist_errors)

    ledger_rows, ledger_fields, ledger_errors = load_csv_by_id(args.ledger, "ledger")
    baseline_rows, baseline_fields, baseline_errors = load_csv_by_id(args.baseline, "baseline")
    errors.extend(ledger_errors)
    errors.extend(baseline_errors)

    require_columns(ledger_fields, ["checklist_id"], "ledger", errors)
    require_columns(baseline_fields, ["checklist_id", *BASELINE_COLUMNS], "baseline", errors)
    require_columns(
        ledger_fields,
        [
            "checklist_id",
            *BASELINE_COLUMNS,
            "action_type",
            "decision_detail",
            "reason_code",
            "reason_why",
            "reason_quality",
            "semantic_change_flag",
            "review_attention",
            *AFTER_COLUMNS,
            "phase1_status",
            "final_quality",
        ],
        "ledger",
        errors,
    )

    if args.recovery_guardrails:
        require_columns(ledger_fields, RECOVERY_EXTRA_COLUMNS, "ledger", errors)

    checklist_ids = set(checklist_summary["parent_marks"].keys())
    if args.expected_parent_count is not None and checklist_summary["parent_total"] != args.expected_parent_count:
        errors.append(
            f"parent_total expected {args.expected_parent_count}, got {checklist_summary['parent_total']}"
        )

    expected_ids = explicit_expected_ids if explicit_expected_ids is not None else checklist_ids
    validate_alignment(
        expected_ids,
        checklist_ids,
        set(ledger_rows.keys()),
        set(baseline_rows.keys()),
        errors,
    )

    ordered_ids = sorted(expected_ids, key=parse_checklist_id)
    check_baseline_immutability(ordered_ids, ledger_rows, baseline_rows, errors)

    parent_total = checklist_summary["parent_total"]
    parent_checked = checklist_summary["parent_checked"]
    parent_unchecked = checklist_summary["parent_unchecked"]
    sub_total = checklist_summary["sub_total"]
    sub_checked = checklist_summary["sub_checked"]
    sub_unchecked = checklist_summary["sub_unchecked"]

    expected_sub_total = parent_total * args.subitems_per_parent
    if sub_total != expected_sub_total:
        errors.append(f"sub_total expected {expected_sub_total}, got {sub_total}")

    if args.mode == "init":
        if parent_checked != 0 or parent_unchecked != parent_total:
            errors.append("init mode requires all parent items unchecked")
        if sub_checked != 0 or sub_unchecked != expected_sub_total:
            errors.append("init mode requires all sub-items unchecked")

    if args.mode in {"gate", "final"}:
        if parent_checked != parent_total or parent_unchecked != 0:
            errors.append("gate/final mode requires all parent items checked")
        if sub_checked != expected_sub_total or sub_unchecked != 0:
            errors.append("gate/final mode requires all sub-items checked")

    completed_rows = 0
    resolved_high_rows = 0
    for checklist_id in ordered_ids:
        row = ledger_rows.get(checklist_id)
        if row is None:
            continue
        sub_marks = checklist_summary["sub_marks"].get(checklist_id, {})
        parent_mark = checklist_summary["parent_marks"].get(checklist_id, False)

        if parent_mark:
            expected_sub = set(range(1, args.subitems_per_parent + 1))
            checked_sub = {index for index, mark in sub_marks.items() if mark}
            if checked_sub != expected_sub:
                errors.append(
                    f"{checklist_id}: parent checked but not all rubric sub-items are checked"
                )

        check_rubric_subitems(checklist_id, sub_marks, row, args.min_reason_length, errors)

        if is_row_completed(row):
            completed_rows += 1
            check_action_and_reason(
                checklist_id,
                row,
                args.min_reason_length,
                errors,
                label="completed-row",
            )

        if (row.get("final_quality") or "").strip().lower() == "resolved-high":
            resolved_high_rows += 1

    allowed_final_quality = {value.strip().lower() for value in args.final_allowed_quality}
    if args.mode == "final":
        for checklist_id in ordered_ids:
            row = ledger_rows.get(checklist_id)
            if row is None:
                continue
            final_quality = (row.get("final_quality") or "").strip().lower()
            if final_quality not in allowed_final_quality:
                errors.append(
                    f"{checklist_id}: final mode requires final_quality in {sorted(allowed_final_quality)}"
                )

    if args.recovery_guardrails:
        enforce_recovery_guardrails(
            ordered_ids=ordered_ids,
            ledger_rows=ledger_rows,
            args=args,
            errors=errors,
        )

    summary = {
        "mode": args.mode,
        "recovery_guardrails": args.recovery_guardrails,
        "expected_parent_count": args.expected_parent_count,
        "expected_ids_provided": args.expected_id_list is not None,
        "expected_sub_count": expected_sub_total,
        "checklist": {
            "parent_total": parent_total,
            "parent_checked": parent_checked,
            "parent_unchecked": parent_unchecked,
            "sub_total": sub_total,
            "sub_checked": sub_checked,
            "sub_unchecked": sub_unchecked,
        },
        "ledger_rows": len(ledger_rows),
        "baseline_rows": len(baseline_rows),
        "completed_rows": completed_rows,
        "resolved_high_rows": resolved_high_rows,
        "error_count": len(errors),
    }

    print(f"mode={summary['mode']}")
    print(
        " ".join(
            [
                f"parent_total={parent_total}",
                f"parent_checked={parent_checked}",
                f"parent_unchecked={parent_unchecked}",
                f"sub_total={sub_total}",
                f"sub_checked={sub_checked}",
                f"sub_unchecked={sub_unchecked}",
            ]
        )
    )
    print(
        " ".join(
            [
                f"ledger_rows={summary['ledger_rows']}",
                f"baseline_rows={summary['baseline_rows']}",
                f"completed_rows={completed_rows}",
                f"resolved_high_rows={resolved_high_rows}",
                f"errors={len(errors)}",
            ]
        )
    )

    if args.json_out is not None:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(
            json.dumps({"summary": summary, "errors": errors}, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    if args.markdown_out is not None:
        args.markdown_out.parent.mkdir(parents=True, exist_ok=True)
        write_markdown(args.markdown_out, summary, errors)

    if errors:
        for error in errors[:100]:
            print(f"ERROR: {error}")
        if len(errors) > 100:
            print(f"ERROR: ... {len(errors) - 100} more")
        return 1

    print("validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
