#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


PARENT_RE = re.compile(r"^- \[(?P<mark>[ xX])\] (?P<id>PQ-\d{3}) term=")
SUB_RE = re.compile(r"^  - \[(?P<mark>[ xX])\] (?P<id>PQ-\d{3})\.(?P<idx>\d+)\b")

BASELINE_COLUMNS = [
    "term",
    "baseline_rating",
    "baseline_file",
    "baseline_line",
    "baseline_dp_id",
    "baseline_section",
    "baseline_commit",
    "first_use_file",
    "first_use_line",
    "recommended_file",
    "recommended_section",
    "relocation_priority",
    "conceptual_home",
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


def expected_ids(count: int) -> list[str]:
    return [f"PQ-{index:03d}" for index in range(1, count + 1)]


def parse_checklist(path: Path, expected_parent_count: int, subitems_per_parent: int) -> tuple[dict, list[str]]:
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
            index = int(sub_match.group("idx"))
            is_checked = sub_match.group("mark").lower() == "x"
            item_marks = sub_marks.setdefault(checklist_id, {})
            if index in item_marks:
                errors.append(
                    f"checklist line {line_number}: duplicate sub-item {checklist_id}.{index}"
                )
            item_marks[index] = is_checked

    expected = set(expected_ids(expected_parent_count))
    parent_ids = set(parent_marks)
    missing_parent = sorted(expected - parent_ids)
    extra_parent = sorted(parent_ids - expected)
    if missing_parent:
        errors.append(f"missing parent checklist IDs: {', '.join(missing_parent[:20])}")
    if extra_parent:
        errors.append(f"unexpected parent checklist IDs: {', '.join(extra_parent[:20])}")

    expected_sub_index = set(range(1, subitems_per_parent + 1))
    for checklist_id in sorted(expected):
        seen_indexes = set(sub_marks.get(checklist_id, {}).keys())
        missing = sorted(expected_sub_index - seen_indexes)
        extra = sorted(seen_indexes - expected_sub_index)
        if missing:
            errors.append(
                f"{checklist_id}: missing sub-items {', '.join(str(index) for index in missing)}"
            )
        if extra:
            errors.append(
                f"{checklist_id}: unexpected sub-items {', '.join(str(index) for index in extra)}"
            )

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
        missing = sorted(expected - ids)
        extra = sorted(ids - expected)
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
    phase2 = (row.get("phase2_status") or "").strip().lower()
    final_quality = (row.get("final_quality") or "").strip().lower()
    return phase1 == "completed" or phase2 == "completed" or final_quality in {
        "resolved-high",
        "blocked",
    }


def require_non_empty(
    row: dict[str, str], checklist_id: str, columns: list[str], errors: list[str], label: str
) -> None:
    for column in columns:
        if not (row.get(column) or "").strip():
            errors.append(f"{checklist_id}: missing {column} ({label})")


def check_reason_quality(
    checklist_id: str,
    row: dict[str, str],
    min_reason_length: int,
    errors: list[str],
    *,
    label: str,
) -> None:
    decision = (row.get("decision") or "").strip()
    reason_code = (row.get("reason_code") or "").strip()
    reason_quality = (row.get("reason_quality") or "").strip().lower()
    reason_why = (row.get("reason_why") or "").strip()

    if not decision:
        errors.append(f"{checklist_id}: missing decision ({label})")

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


def check_rubric_subitems(
    checklist_id: str,
    sub_marks: dict[int, bool],
    row: dict[str, str],
    min_reason_length: int,
    errors: list[str],
) -> None:
    for sub_index, sub_label in [
        (1, "before snapshot"),
        (2, "decision/reason"),
        (3, "reason quality"),
        (4, "after snapshot"),
        (5, "statuses/final quality"),
    ]:
        is_checked = sub_marks.get(sub_index, False)
        if not is_checked:
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
                ["decision", "reason_code"],
                errors,
                sub_label,
            )

        if sub_index == 3:
            check_reason_quality(
                checklist_id,
                row,
                min_reason_length,
                errors,
                label=sub_label,
            )

        if sub_index == 4:
            require_non_empty(row, checklist_id, AFTER_COLUMNS, errors, sub_label)

        if sub_index == 5:
            require_non_empty(
                row,
                checklist_id,
                ["phase1_status", "phase2_status", "final_quality"],
                errors,
                sub_label,
            )
            if (row.get("final_quality") or "").strip().lower() == "pending":
                errors.append(f"{checklist_id}: final_quality is pending ({sub_label})")


def write_markdown(path: Path, summary: dict, errors: list[str]) -> None:
    checklist = summary["checklist"]
    lines = [
        "# Checklist and ledger validation",
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate checklist + ledger remediation gates")
    parser.add_argument("--checklist", type=Path, required=True)
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument(
        "--mode",
        choices=["progress", "init", "gate", "final"],
        default="progress",
        help="init=all unchecked, gate=all checked, final=all checked + resolved-high",
    )
    parser.add_argument("--expected-parent-count", type=int, default=202)
    parser.add_argument("--subitems-per-parent", type=int, default=5)
    parser.add_argument("--min-reason-length", type=int, default=80)
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--markdown-out", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors: list[str] = []

    checklist_summary, checklist_errors = parse_checklist(
        args.checklist, args.expected_parent_count, args.subitems_per_parent
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
            "decision",
            "reason_code",
            "reason_why",
            "reason_quality",
            *AFTER_COLUMNS,
            "phase1_status",
            "phase2_status",
            "final_quality",
        ],
        "ledger",
        errors,
    )

    expected = set(expected_ids(args.expected_parent_count))
    checklist_ids = set(checklist_summary["parent_marks"].keys())
    ledger_ids = set(ledger_rows.keys())
    baseline_ids = set(baseline_rows.keys())
    validate_alignment(expected, checklist_ids, ledger_ids, baseline_ids, errors)

    ordered_ids = expected_ids(args.expected_parent_count)
    check_baseline_immutability(ordered_ids, ledger_rows, baseline_rows, errors)

    parent_total = checklist_summary["parent_total"]
    parent_checked = checklist_summary["parent_checked"]
    parent_unchecked = checklist_summary["parent_unchecked"]
    sub_total = checklist_summary["sub_total"]
    sub_checked = checklist_summary["sub_checked"]
    sub_unchecked = checklist_summary["sub_unchecked"]

    expected_parent_total = args.expected_parent_count
    expected_sub_total = args.expected_parent_count * args.subitems_per_parent

    if parent_total != expected_parent_total:
        errors.append(f"parent_total expected {expected_parent_total}, got {parent_total}")
    if sub_total != expected_sub_total:
        errors.append(f"sub_total expected {expected_sub_total}, got {sub_total}")

    if args.mode == "init":
        if parent_checked != 0 or parent_unchecked != expected_parent_total:
            errors.append("init mode requires all parent items unchecked")
        if sub_checked != 0 or sub_unchecked != expected_sub_total:
            errors.append("init mode requires all sub-items unchecked")

    if args.mode in {"gate", "final"}:
        if parent_checked != expected_parent_total or parent_unchecked != 0:
            errors.append("gate/final mode requires all parent items checked")
        if sub_checked != expected_sub_total or sub_unchecked != 0:
            errors.append("gate/final mode requires all sub-items checked")

    completed_rows = 0
    resolved_high_rows = 0
    for checklist_id in ordered_ids:
        row = ledger_rows.get(checklist_id)
        sub_marks = checklist_summary["sub_marks"].get(checklist_id, {})
        parent_mark = checklist_summary["parent_marks"].get(checklist_id, False)
        if row is None:
            continue

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
            check_reason_quality(
                checklist_id,
                row,
                args.min_reason_length,
                errors,
                label="completed-row",
            )

        if (row.get("final_quality") or "").strip().lower() == "resolved-high":
            resolved_high_rows += 1

    if args.mode == "final":
        for checklist_id in ordered_ids:
            row = ledger_rows.get(checklist_id)
            if row is None:
                continue
            if (row.get("final_quality") or "").strip().lower() != "resolved-high":
                errors.append(f"{checklist_id}: final mode requires final_quality=resolved-high")

    summary = {
        "mode": args.mode,
        "expected_parent_count": args.expected_parent_count,
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
