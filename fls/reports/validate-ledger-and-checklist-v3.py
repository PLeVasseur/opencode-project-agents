#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import re
import subprocess
from pathlib import Path

from definition_alignment_shared import (
    analyze_dt_insert_patch,
    first_compound_split_token,
    is_subject_form_definition,
    jaccard_similarity,
    normalize_text_for_similarity,
)


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

ALLOWED_DEVIATION_STATUSES = {"pending", "approved", "rejected"}
ALLOWED_DEFINITION_OPERATIONS = {"promote", "insert", "adapt"}

DEFINITION_NORMALIZATION_VERSION = "v1"

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

FOUNDATIONAL_REQUIRED_SECTIONS = {
    "value": {"Values"},
    "expression": {"Expressions"},
    "trait": {"Traits", "Trait Types"},
    "item": {"Items"},
    "field": {"Struct Types", "Enum Types"},
    "reference": {"References", "Borrowing"},
    "implementation": {"Implementations", "Inherent Implementations"},
    "method": {"Functions"},
    "crate": {"Crates", "Compilation Roots"},
    "statement": {"Statements"},
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
    "deviation_status",
    "definition_operation",
    "definition_similarity",
    "glossary_definition_sha256",
    "chapter_definition_sha256",
    "definition_normalization_version",
]

FAILED_RECOMMENDATION_LOCK = "FAILED_RECOMMENDATION_LOCK"
FAILED_UUID_GUARDRAIL = "FAILED_UUID_GUARDRAIL"
FAILED_DEVIATION_CONCENTRATION = "FAILED_DEVIATION_CONCENTRATION"
FAILED_RATIONALE_MONOCULTURE = "FAILED_RATIONALE_MONOCULTURE"
FAILED_STRICT_REGRESSION = "FAILED_STRICT_REGRESSION"
FAILED_FOUNDATIONAL_PLACEMENT = "FAILED_FOUNDATIONAL_PLACEMENT"
FAILED_PENDING_DEVIATIONS = "FAILED_PENDING_DEVIATIONS"
FAILED_GLOSSARY_ALIGNMENT = "FAILED_GLOSSARY_ALIGNMENT"
FAILED_INSERT_DIFF_MISMATCH = "FAILED_INSERT_DIFF_MISMATCH"
FAILED_DEFINITION_OPERATION_MISMATCH = "FAILED_DEFINITION_OPERATION_MISMATCH"
FAILED_COMPOUND_DT_SPLIT = "FAILED_COMPOUND_DT_SPLIT"
FAILED_SUBJECT_FORM = "FAILED_SUBJECT_FORM"
FAILED_SIMILARITY_DRIFT = "FAILED_SIMILARITY_DRIFT"

WARN_GLOSSARY_MISMATCH = "WARN_GLOSSARY_MISMATCH"
WARN_DEFINITION_OPERATION_MISMATCH = "WARN_DEFINITION_OPERATION_MISMATCH"


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


def write_markdown(path: Path, summary: dict, warnings: list[str], errors: list[str]) -> None:
    checklist = summary["checklist"]
    pending_deviation_count = summary.get("pending_deviation_count")
    lines = [
        "# Checklist and ledger validation (v3)",
        "",
        f"- Mode: `{summary['mode']}`",
        f"- Parent items: `{checklist['parent_checked']}/{checklist['parent_total']}` checked",
        f"- Sub-items: `{checklist['sub_checked']}/{checklist['sub_total']}` checked",
        f"- Ledger rows: `{summary['ledger_rows']}`",
        f"- Baseline rows: `{summary['baseline_rows']}`",
        f"- Completed ledger rows: `{summary['completed_rows']}`",
        f"- Resolved-high rows: `{summary['resolved_high_rows']}`",
        f"- Warning count: `{len(warnings)}`",
        f"- Error count: `{len(errors)}`",
        "",
    ]
    if pending_deviation_count is not None:
        lines.insert(-2, f"- Pending deviations: `{pending_deviation_count}`")

    if warnings:
        lines.append("## Warnings")
        lines.append("")
        for warning in warnings[:200]:
            lines.append(f"- {warning}")
        if len(warnings) > 200:
            lines.append(f"- ... {len(warnings) - 200} more warnings")
        lines.append("")

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


def append_failure(errors: list[str], code: str, message: str) -> None:
    errors.append(f"{code}: {message}")


def append_warning(warnings: list[str], code: str, message: str) -> None:
    warnings.append(f"{code}: {message}")


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def run_git_show_text(*, workdir: Path, spec: str) -> str:
    result = subprocess.run(
        ["git", "show", spec],
        cwd=str(workdir),
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"git show failed for '{spec}': {result.stderr.strip()}")
    return result.stdout


def similarity_text(value: float) -> str:
    return f"{value:.6f}"


def split_entry_chunks(lines: list[str]) -> list[str]:
    chunks: list[str] = []
    current: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if current:
                chunks.append(" ".join(current))
                current = []
            continue
        if stripped.startswith(".. "):
            continue
        if stripped.startswith(":dp:`"):
            continue
        current.append(stripped)
    if current:
        chunks.append(" ".join(current))
    return chunks


def extract_glossary_definition_from_text(*, glossary_text: str, term: str) -> tuple[str, int]:
    lines = glossary_text.splitlines()
    marker = f":dt:`{term}`"
    matches = [index for index, line in enumerate(lines) if marker in line]
    if len(matches) != 1:
        raise RuntimeError(
            f"glossary definition lookup expected 1 match for term '{term}', got {len(matches)}"
        )

    start = matches[0]
    end = len(lines)
    for index in range(start + 1, len(lines)):
        if lines[index].startswith(".. _fls_"):
            end = index
            break

    chunks = split_entry_chunks(lines[start:end])
    selected: list[str] = []
    for chunk in chunks:
        lowered = chunk.lower().strip()
        if not selected:
            if marker in chunk:
                selected.append(chunk.strip())
            continue
        if lowered.startswith("see "):
            continue
        selected.append(chunk.strip())

    if not selected:
        raise RuntimeError(f"could not extract glossary definition for term '{term}'")

    combined = " ".join(selected)
    sentence_count = len(re.findall(r"[.!?](?:\s|$)", combined))
    sentence_count = max(sentence_count, 1)
    return combined, sentence_count


def extract_chapter_definition_from_text(*, chapter_text: str, after_dp_id: str, term: str) -> str:
    lines = chapter_text.splitlines()
    dp_pattern = re.compile(rf"(^|\s):dp:`{re.escape(after_dp_id)}`(\s|$)")
    dp_index: int | None = None
    for index, line in enumerate(lines):
        if dp_pattern.search(line):
            dp_index = index
            break
    if dp_index is None:
        raise RuntimeError(f"after_dp_id '{after_dp_id}' not found in chapter text")

    paragraph_lines: list[str] = []
    for index in range(dp_index + 1, len(lines)):
        stripped = lines[index].strip()
        if not stripped:
            break
        paragraph_lines.append(stripped)

    if not paragraph_lines:
        raise RuntimeError(f"no paragraph after :dp:`{after_dp_id}` for term '{term}'")

    paragraph = " ".join(paragraph_lines)
    if f":dt:`{term}`" not in paragraph:
        raise RuntimeError(
            f"paragraph after :dp:`{after_dp_id}` does not define '{term}' with :dt:"
        )
    return paragraph


def resolve_repo_path_for_after_file(after_file: str) -> str:
    value = after_file.strip().replace("\\", "/")
    if value.startswith("src/"):
        return value
    return f"src/{value}"


def load_acknowledged_ids(path: Path | None) -> set[str]:
    if path is None:
        return set()
    if not path.is_file():
        raise RuntimeError(f"glossary acknowledgment file not found: {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return {str(item).strip() for item in payload if str(item).strip()}
    if isinstance(payload, dict):
        for key in ["acknowledged_ids", "ids", "allowed_ids"]:
            value = payload.get(key)
            if isinstance(value, list):
                return {str(item).strip() for item in value if str(item).strip()}
    raise RuntimeError("glossary acknowledgment file must be a list or object with acknowledged_ids")


def load_diff_audit_index(path: Path | None) -> dict[str, dict]:
    if path is None or not path.is_file():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    terms = payload.get("terms")
    if isinstance(terms, dict):
        return {str(key): value for key, value in terms.items() if isinstance(value, dict)}
    return {}


def git_numstat_for_file(*, workdir: Path, commit_hash: str, repo_path: str) -> tuple[int, int, int]:
    result = subprocess.run(
        ["git", "show", "--numstat", "--format=", commit_hash, "--", repo_path],
        cwd=str(workdir),
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"git show --numstat failed for commit={commit_hash} path={repo_path}: {result.stderr.strip()}"
        )
    added = 0
    deleted = 0
    for line in result.stdout.splitlines():
        parts = line.strip().split("\t")
        if len(parts) < 3:
            continue
        try:
            add_value = int(parts[0])
        except ValueError:
            add_value = 0
        try:
            del_value = int(parts[1])
        except ValueError:
            del_value = 0
        added += add_value
        deleted += del_value
    return added, deleted, added - deleted


def git_hunk_insert_analysis(
    *, workdir: Path, commit_hash: str, repo_path: str, term: str
) -> tuple[bool, dict[str, int | bool]]:
    result = subprocess.run(
        ["git", "show", "--format=", "--unified=0", commit_hash, "--", repo_path],
        cwd=str(workdir),
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return False, {
            "dt_added": 0,
            "dt_removed": 0,
            "t_removed": 0,
            "marker_removed": 0,
            "insert_net": 0,
            "has_dt_addition": False,
            "swap_detected": False,
            "insert_pass": False,
        }
    return True, analyze_dt_insert_patch(result.stdout, term)


def parse_int_or_none(value: object) -> int | None:
    try:
        return int(str(value))
    except Exception:  # noqa: BLE001
        return None


def parse_bool_or_none(value: object) -> bool | None:
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return bool(value)
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"true", "1", "yes"}:
            return True
        if lowered in {"false", "0", "no"}:
            return False
    return None


def evaluate_operation_insert_evidence(
    *,
    checklist_id: str,
    definition_operation: str,
    term: str,
    after_file: str,
    after_commit: str,
    repo_after_path: str,
    workdir: Path,
    diff_audit_index: dict[str, dict],
) -> tuple[str, bool, bool, int | None, str]:
    mode_used = "fallback"
    insert_pass: bool | None = None
    evidence_source = ""
    swap_detected = False
    insert_net: int | None = None

    def _audit_file_matches(audit_file: str) -> bool:
        value = audit_file.strip().replace("\\", "/")
        if not value:
            return False
        if value == after_file:
            return True
        return value == repo_after_path

    diff_entry = diff_audit_index.get(checklist_id)
    if isinstance(diff_entry, dict):
        audit_mode = str(diff_entry.get("mode") or "").strip().lower()
        audit_path = str(diff_entry.get("evidence_source") or "").strip()
        audit_file = str(diff_entry.get("after_file") or "").strip()
        if audit_mode == "hunk" and _audit_file_matches(audit_file):
            dt_added = parse_int_or_none(diff_entry.get("hunk_dt_added"))
            marker_removed = parse_int_or_none(diff_entry.get("hunk_marker_removed"))
            if dt_added is not None and marker_removed is not None:
                insert_net = dt_added - marker_removed
                parsed_insert_pass = parse_bool_or_none(diff_entry.get("hunk_insert_pass"))
                if parsed_insert_pass is None:
                    parsed_insert_pass = dt_added > 0 and insert_net > 0
                parsed_swap_detected = parse_bool_or_none(diff_entry.get("swap_detected"))
                if parsed_swap_detected is None:
                    parsed_swap_detected = dt_added > 0 and marker_removed > 0 and insert_net <= 0
                insert_pass = parsed_insert_pass
                swap_detected = parsed_swap_detected
                mode_used = "hunk"
                evidence_source = audit_path or "diff-audit-index"
        elif (
            definition_operation == "insert"
            and audit_mode == "fallback"
            and _audit_file_matches(audit_file)
        ):
            file_net_delta = parse_int_or_none(diff_entry.get("file_net_delta"))
            if file_net_delta is None:
                file_net_delta = 0
            insert_pass = file_net_delta > 0
            insert_net = file_net_delta
            mode_used = "fallback"
            evidence_source = audit_path or "diff-audit-index"

    if insert_pass is None:
        hunk_available, hunk_analysis = git_hunk_insert_analysis(
            workdir=workdir,
            commit_hash=after_commit,
            repo_path=repo_after_path,
            term=term,
        )
        if hunk_available:
            insert_pass = bool(hunk_analysis.get("insert_pass", False))
            swap_detected = bool(hunk_analysis.get("swap_detected", False))
            insert_net = int(hunk_analysis.get("insert_net", 0))
            mode_used = "hunk"
            evidence_source = f"git show --unified=0 {after_commit} -- {repo_after_path}"
        else:
            _, _, file_net_delta = git_numstat_for_file(
                workdir=workdir,
                commit_hash=after_commit,
                repo_path=repo_after_path,
            )
            insert_pass = file_net_delta > 0
            insert_net = file_net_delta
            mode_used = "fallback"
            evidence_source = f"git show --numstat {after_commit} -- {repo_after_path}"

    return mode_used, bool(insert_pass), swap_detected, insert_net, evidence_source


def jaccard_similarity_reason(a: str, b: str) -> float:
    tokens_a = {token for token in re.split(r"\s+", a.lower().strip()) if token}
    tokens_b = {token for token in re.split(r"\s+", b.lower().strip()) if token}
    if not tokens_a and not tokens_b:
        return 1.0
    if not tokens_a or not tokens_b:
        return 0.0
    return len(tokens_a & tokens_b) / len(tokens_a | tokens_b)


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
    warnings: list[str],
    errors: list[str],
) -> tuple[int, dict[str, str], dict[str, str]]:
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
    ledger_path = Path(getattr(args, "ledger"))
    pending_deviation_count = 0
    insert_diff_modes: dict[str, str] = {}
    definition_operation_diff_modes: dict[str, str] = {}
    if args.events_jsonl is None:
        append_failure(
            errors,
            FAILED_UUID_GUARDRAIL,
            "recovery guardrails require --events-jsonl",
        )
    else:
        events_required = True
        events_by_id, event_errors = load_events(args.events_jsonl)
        errors.extend(event_errors)

    workdir: Path | None = None
    glossary_repo_path = ""
    glossary_head_text = ""
    acknowledged_ids: set[str] = set()
    diff_audit_index: dict[str, dict] = {}

    if args.workdir is None:
        append_failure(
            errors,
            FAILED_GLOSSARY_ALIGNMENT,
            "recovery guardrails require --workdir for glossary alignment checks",
        )
    else:
        resolved_workdir = args.workdir.expanduser().resolve()
        workdir = resolved_workdir
        if not resolved_workdir.is_dir():
            append_failure(
                errors,
                FAILED_GLOSSARY_ALIGNMENT,
                f"--workdir is not a directory: {resolved_workdir}",
            )
        else:
            raw_glossary = args.glossary_file
            if raw_glossary.is_absolute():
                glossary_path = raw_glossary
                glossary_repo_path = raw_glossary.as_posix()
            else:
                glossary_path = (resolved_workdir / raw_glossary).resolve()
                glossary_repo_path = raw_glossary.as_posix()
            if glossary_repo_path.startswith("./"):
                glossary_repo_path = glossary_repo_path[2:]
            try:
                glossary_head_text = run_git_show_text(
                    workdir=resolved_workdir,
                    spec=f"HEAD:{glossary_repo_path}",
                )
            except Exception as exc:  # noqa: BLE001
                append_failure(
                    errors,
                    FAILED_GLOSSARY_ALIGNMENT,
                    f"could not load glossary text from committed HEAD ({glossary_path}): {exc}",
                )

            try:
                acknowledged_ids = load_acknowledged_ids(args.glossary_ack_json)
            except Exception as exc:  # noqa: BLE001
                append_failure(
                    errors,
                    FAILED_GLOSSARY_ALIGNMENT,
                    f"could not parse --glossary-ack-json: {exc}",
                )

            try:
                diff_audit_index = load_diff_audit_index(args.diff_audit_json)
            except Exception as exc:  # noqa: BLE001
                append_failure(
                    errors,
                    FAILED_INSERT_DIFF_MISMATCH,
                    f"could not parse --diff-audit-json: {exc}",
                )

    for checklist_id, row in completed_rows:
        rationale_uuid = (row.get("rationale_uuid") or "").strip()
        inserted_at = (row.get("rationale_inserted_at_utc") or "").strip()
        rationale_sha = (row.get("rationale_text_sha256") or "").strip()
        reason_why = (row.get("reason_why") or "").strip()

        if not rationale_uuid:
            append_failure(
                errors,
                FAILED_UUID_GUARDRAIL,
                f"{checklist_id}: missing rationale_uuid",
            )
        elif not UUID_RE.match(rationale_uuid):
            append_failure(
                errors,
                FAILED_UUID_GUARDRAIL,
                f"{checklist_id}: invalid rationale_uuid format",
            )
        elif rationale_uuid in seen_uuid:
            append_failure(
                errors,
                FAILED_UUID_GUARDRAIL,
                f"{checklist_id}: duplicate rationale_uuid {rationale_uuid}",
            )
        else:
            seen_uuid.add(rationale_uuid)

        if not inserted_at:
            append_failure(
                errors,
                FAILED_UUID_GUARDRAIL,
                f"{checklist_id}: missing rationale_inserted_at_utc",
            )
        if not rationale_sha:
            append_failure(
                errors,
                FAILED_UUID_GUARDRAIL,
                f"{checklist_id}: missing rationale_text_sha256",
            )
        elif not re.fullmatch(r"[0-9a-f]{64}", rationale_sha):
            append_failure(
                errors,
                FAILED_UUID_GUARDRAIL,
                f"{checklist_id}: rationale_text_sha256 is not hex sha256",
            )
        else:
            expected_sha = sha256_text(reason_why)
            if rationale_sha != expected_sha:
                append_failure(
                    errors,
                    FAILED_UUID_GUARDRAIL,
                    (
                        f"{checklist_id}: rationale_text_sha256 does not match reason_why "
                        f"(expected {expected_sha}, got {rationale_sha})"
                    ),
                )

        for pattern in BOILERPLATE_REASONS:
            if pattern.search(reason_why):
                append_failure(
                    errors,
                    FAILED_RATIONALE_MONOCULTURE,
                    f"{checklist_id}: reason_why matches rejected boilerplate",
                )
                break

        priority = (row.get("recommendation_priority") or "").strip().lower()
        used = (row.get("recommendation_used") or "").strip().lower()
        if priority in {"high", "medium"} and used != "yes":
            permit_path = (row.get("deviation_permit_path") or "").strip()
            permit_sha = (row.get("deviation_permit_sha256") or "").strip()
            approved_by = (row.get("deviation_approved_by") or "").strip()
            deviation_status = (row.get("deviation_status") or "").strip().lower()

            if not permit_path:
                append_failure(
                    errors,
                    FAILED_RECOMMENDATION_LOCK,
                    f"{checklist_id}: high/medium non-recommended decision missing deviation_permit_path",
                )
            if not permit_sha:
                append_failure(
                    errors,
                    FAILED_RECOMMENDATION_LOCK,
                    f"{checklist_id}: high/medium non-recommended decision missing deviation_permit_sha256",
                )
            elif not re.fullmatch(r"[0-9a-f]{64}", permit_sha):
                append_failure(
                    errors,
                    FAILED_RECOMMENDATION_LOCK,
                    f"{checklist_id}: deviation_permit_sha256 is not hex sha256",
                )

            if not deviation_status:
                append_failure(
                    errors,
                    FAILED_RECOMMENDATION_LOCK,
                    f"{checklist_id}: high/medium non-recommended decision missing deviation_status",
                )
            elif deviation_status not in ALLOWED_DEVIATION_STATUSES:
                append_failure(
                    errors,
                    FAILED_RECOMMENDATION_LOCK,
                    (
                        f"{checklist_id}: high/medium non-recommended decision has invalid "
                        f"deviation_status '{deviation_status}'"
                    ),
                )
            else:
                if deviation_status == "pending":
                    pending_deviation_count += 1
                    if approved_by:
                        append_failure(
                            errors,
                            FAILED_RECOMMENDATION_LOCK,
                            (
                                f"{checklist_id}: deviation_status=pending requires empty "
                                "deviation_approved_by"
                            ),
                        )
                    if args.mode in {"gate", "final"}:
                        append_failure(
                            errors,
                            FAILED_PENDING_DEVIATIONS,
                            (
                                f"{checklist_id}: pending deviation is not allowed in mode={args.mode}; "
                                "approval/rejection required before wave gate"
                            ),
                        )
                if deviation_status in {"approved", "rejected"} and not approved_by:
                    append_failure(
                        errors,
                        FAILED_RECOMMENDATION_LOCK,
                        (
                            f"{checklist_id}: deviation_status={deviation_status} requires "
                            "deviation_approved_by"
                        ),
                    )
                if deviation_status == "rejected":
                    append_failure(
                        errors,
                        FAILED_RECOMMENDATION_LOCK,
                        (
                            f"{checklist_id}: deviation_status=rejected requires re-execution; "
                            "completed row cannot pass"
                        ),
                    )

            if permit_path and permit_sha:
                permit_file = Path(permit_path)
                if not permit_file.is_absolute():
                    permit_file = ledger_path.parent / permit_file
                if not permit_file.is_file():
                    append_failure(
                        errors,
                        FAILED_RECOMMENDATION_LOCK,
                        f"{checklist_id}: deviation permit file missing: {permit_file}",
                    )
                else:
                    actual_sha = hashlib.sha256(permit_file.read_bytes()).hexdigest()
                    if actual_sha != permit_sha:
                        append_failure(
                            errors,
                            FAILED_RECOMMENDATION_LOCK,
                            (
                                f"{checklist_id}: deviation permit sha mismatch "
                                f"(expected {permit_sha}, got {actual_sha})"
                            ),
                        )
                    try:
                        permit_payload = json.loads(permit_file.read_text(encoding="utf-8"))
                    except Exception as exc:  # noqa: BLE001
                        append_failure(
                            errors,
                            FAILED_RECOMMENDATION_LOCK,
                            f"{checklist_id}: could not parse deviation permit JSON: {exc}",
                        )
                    else:
                        permit_status = (permit_payload.get("status") or "").strip().lower()
                        permit_approved_by = (permit_payload.get("approved_by") or "").strip()
                        normalized_permit_status = (
                            "pending" if permit_status == "pending-review" else permit_status
                        )
                        if normalized_permit_status == "pending" and permit_approved_by:
                            append_failure(
                                errors,
                                FAILED_RECOMMENDATION_LOCK,
                                (
                                    f"{checklist_id}: deviation permit with status pending-review "
                                    "must keep approved_by empty"
                                ),
                            )
                        if deviation_status and normalized_permit_status and (
                            normalized_permit_status != deviation_status
                        ):
                            append_failure(
                                errors,
                                FAILED_RECOMMENDATION_LOCK,
                                (
                                    f"{checklist_id}: deviation_status mismatch between ledger "
                                    f"('{deviation_status}') and permit ('{normalized_permit_status}')"
                                ),
                            )
                        if (
                            deviation_status in {"approved", "rejected"}
                            and approved_by
                            and permit_approved_by
                            and permit_approved_by != approved_by
                        ):
                            append_failure(
                                errors,
                                FAILED_RECOMMENDATION_LOCK,
                                (
                                    f"{checklist_id}: deviation_approved_by mismatch between ledger "
                                    f"('{approved_by}') and permit ('{permit_approved_by}')"
                                ),
                            )

        if events_required:
            events_for_id = events_by_id.get(checklist_id, [])
            latest_event = events_for_id[-1] if events_for_id else None
            if latest_event is None:
                append_failure(
                    errors,
                    FAILED_UUID_GUARDRAIL,
                    f"{checklist_id}: no rationale events found",
                )
            else:
                latest_uuid = (latest_event.get("rationale_uuid") or "").strip()
                if latest_uuid != rationale_uuid:
                    append_failure(
                        errors,
                        FAILED_UUID_GUARDRAIL,
                        (
                            f"{checklist_id}: latest event uuid mismatch "
                            f"(row={rationale_uuid}, latest_event={latest_uuid})"
                        ),
                    )
                latest_reason_sha = (latest_event.get("reason_why_sha256") or "").strip()
                if latest_reason_sha and rationale_sha and latest_reason_sha != rationale_sha:
                    append_failure(
                        errors,
                        FAILED_UUID_GUARDRAIL,
                        (
                            f"{checklist_id}: latest event digest mismatch "
                            f"(row={rationale_sha}, latest_event={latest_reason_sha})"
                        ),
                    )

            matches = [
                event
                for event in events_for_id
                if (event.get("rationale_uuid") or "").strip() == rationale_uuid
            ]
            if not matches:
                append_failure(
                    errors,
                    FAILED_UUID_GUARDRAIL,
                    f"{checklist_id}: no matching rationale event for rationale_uuid={rationale_uuid}",
                )

        definition_operation = (row.get("definition_operation") or "").strip().lower()
        definition_similarity_text = (row.get("definition_similarity") or "").strip()
        glossary_sha = (row.get("glossary_definition_sha256") or "").strip().lower()
        chapter_sha = (row.get("chapter_definition_sha256") or "").strip().lower()
        normalization_version = (row.get("definition_normalization_version") or "").strip()
        after_file = (row.get("after_file") or "").strip()
        after_dp_id = (row.get("after_dp_id") or "").strip()
        after_commit = (row.get("after_commit") or "").strip()
        review_attention = (row.get("review_attention") or "").strip().lower()
        term = (row.get("term") or "").strip()

        if not definition_operation:
            append_failure(
                errors,
                FAILED_GLOSSARY_ALIGNMENT,
                f"{checklist_id}: missing definition_operation",
            )
            continue
        if definition_operation not in ALLOWED_DEFINITION_OPERATIONS:
            append_failure(
                errors,
                FAILED_GLOSSARY_ALIGNMENT,
                f"{checklist_id}: invalid definition_operation '{definition_operation}'",
            )
            continue

        if not definition_similarity_text:
            append_failure(
                errors,
                FAILED_GLOSSARY_ALIGNMENT,
                f"{checklist_id}: missing definition_similarity",
            )
            continue
        try:
            stored_similarity = float(definition_similarity_text)
        except ValueError:
            append_failure(
                errors,
                FAILED_GLOSSARY_ALIGNMENT,
                f"{checklist_id}: invalid definition_similarity '{definition_similarity_text}'",
            )
            continue

        if not glossary_sha or not re.fullmatch(r"[0-9a-f]{64}", glossary_sha):
            append_failure(
                errors,
                FAILED_GLOSSARY_ALIGNMENT,
                f"{checklist_id}: invalid glossary_definition_sha256",
            )
            continue
        if not chapter_sha or not re.fullmatch(r"[0-9a-f]{64}", chapter_sha):
            append_failure(
                errors,
                FAILED_GLOSSARY_ALIGNMENT,
                f"{checklist_id}: invalid chapter_definition_sha256",
            )
            continue

        if normalization_version != DEFINITION_NORMALIZATION_VERSION:
            append_failure(
                errors,
                FAILED_GLOSSARY_ALIGNMENT,
                (
                    f"{checklist_id}: definition_normalization_version must be "
                    f"{DEFINITION_NORMALIZATION_VERSION}, got '{normalization_version}'"
                ),
            )
            continue

        if not after_commit:
            if args.mode in {"gate", "final"}:
                append_failure(
                    errors,
                    FAILED_GLOSSARY_ALIGNMENT,
                    f"{checklist_id}: missing after_commit for mode={args.mode}",
                )
            else:
                append_warning(
                    warnings,
                    WARN_GLOSSARY_MISMATCH,
                    f"{checklist_id}: alignment deferred until committed after_commit is available",
                )
            continue

        if workdir is None or not glossary_head_text:
            append_failure(
                errors,
                FAILED_GLOSSARY_ALIGNMENT,
                f"{checklist_id}: glossary alignment context unavailable",
            )
            continue

        repo_after_path = resolve_repo_path_for_after_file(after_file)
        try:
            chapter_head_text = run_git_show_text(workdir=workdir, spec=f"HEAD:{repo_after_path}")
        except Exception as exc:  # noqa: BLE001
            append_failure(
                errors,
                FAILED_GLOSSARY_ALIGNMENT,
                f"{checklist_id}: could not read committed chapter file HEAD:{repo_after_path}: {exc}",
            )
            continue

        try:
            glossary_definition, _ = extract_glossary_definition_from_text(
                glossary_text=glossary_head_text,
                term=term,
            )
            chapter_definition = extract_chapter_definition_from_text(
                chapter_text=chapter_head_text,
                after_dp_id=after_dp_id,
                term=term,
            )
        except Exception as exc:  # noqa: BLE001
            append_failure(
                errors,
                FAILED_GLOSSARY_ALIGNMENT,
                f"{checklist_id}: could not extract definitions: {exc}",
            )
            continue

        split_token = first_compound_split_token(chapter_definition, term)
        if split_token is not None:
            append_failure(
                errors,
                FAILED_COMPOUND_DT_SPLIT,
                (
                    f"{checklist_id}: token '{split_token}' immediately after :dt:`{term}` "
                    "indicates compound split"
                ),
            )

        subject_form = is_subject_form_definition(chapter_definition, term)
        if definition_operation in {"promote", "insert"} and not subject_form:
            append_failure(
                errors,
                FAILED_SUBJECT_FORM,
                f"{checklist_id}: definition_operation={definition_operation} requires subject-form chapter definition",
            )

        normalized_glossary = normalize_text_for_similarity(glossary_definition)
        normalized_chapter = normalize_text_for_similarity(chapter_definition)
        recomputed_similarity = jaccard_similarity(normalized_glossary, normalized_chapter)
        recomputed_similarity_text = similarity_text(recomputed_similarity)
        recomputed_glossary_sha = sha256_text(normalized_glossary)
        recomputed_chapter_sha = sha256_text(normalized_chapter)

        if glossary_sha != recomputed_glossary_sha:
            append_failure(
                errors,
                FAILED_SIMILARITY_DRIFT,
                (
                    f"{checklist_id}: glossary_definition_sha256 mismatch "
                    f"(stored={glossary_sha}, recomputed={recomputed_glossary_sha})"
                ),
            )
        if chapter_sha != recomputed_chapter_sha:
            append_failure(
                errors,
                FAILED_SIMILARITY_DRIFT,
                (
                    f"{checklist_id}: chapter_definition_sha256 mismatch "
                    f"(stored={chapter_sha}, recomputed={recomputed_chapter_sha})"
                ),
            )

        stored_similarity_text = similarity_text(stored_similarity)
        if stored_similarity_text != recomputed_similarity_text:
            append_failure(
                errors,
                FAILED_SIMILARITY_DRIFT,
                (
                    f"{checklist_id}: definition_similarity drift "
                    f"(stored={stored_similarity_text}, recomputed={recomputed_similarity_text})"
                ),
            )

        if definition_operation == "promote" and recomputed_similarity < args.min_promote_similarity:
            append_failure(
                errors,
                FAILED_GLOSSARY_ALIGNMENT,
                (
                    f"{checklist_id}: promote similarity {recomputed_similarity_text} below "
                    f"{args.min_promote_similarity:.2f}"
                ),
            )

        if definition_operation == "adapt" and review_attention != "required":
            append_failure(
                errors,
                FAILED_GLOSSARY_ALIGNMENT,
                f"{checklist_id}: definition_operation=adapt requires review_attention=required",
            )
        if (
            definition_operation == "adapt"
            and recomputed_similarity < args.min_promote_similarity
            and not subject_form
        ):
            append_failure(
                errors,
                FAILED_SUBJECT_FORM,
                f"{checklist_id}: marginal adapt definition requires subject-form chapter definition",
            )

        if recomputed_similarity < args.min_glossary_similarity:
            message = (
                f"{checklist_id}: glossary/chapter similarity {recomputed_similarity_text} below "
                f"{args.min_glossary_similarity:.2f}"
            )
            if args.mode == "progress":
                append_warning(warnings, WARN_GLOSSARY_MISMATCH, message)
            elif checklist_id not in acknowledged_ids:
                append_failure(
                    errors,
                    FAILED_GLOSSARY_ALIGNMENT,
                    f"{message}; reviewer acknowledgment required",
                )

        if definition_operation in {"insert", "promote"}:
            try:
                mode_used, insert_pass, swap_detected, insert_net, evidence_source = (
                    evaluate_operation_insert_evidence(
                        checklist_id=checklist_id,
                        definition_operation=definition_operation,
                        term=term,
                        after_file=after_file,
                        after_commit=after_commit,
                        repo_after_path=repo_after_path,
                        workdir=workdir,
                        diff_audit_index=diff_audit_index,
                    )
                )
            except Exception as exc:  # noqa: BLE001
                failure_code = (
                    FAILED_INSERT_DIFF_MISMATCH
                    if definition_operation == "insert"
                    else FAILED_DEFINITION_OPERATION_MISMATCH
                )
                append_failure(
                    errors,
                    failure_code,
                    f"{checklist_id}: could not evaluate {definition_operation} diff check: {exc}",
                )
            else:
                definition_operation_diff_modes[checklist_id] = mode_used
                if definition_operation == "insert":
                    insert_diff_modes[checklist_id] = mode_used
                    if not insert_pass:
                        detail = (
                            f"{checklist_id}: definition_operation=insert did not show qualifying insertion "
                            f"(mode={mode_used}, evidence={evidence_source}"
                        )
                        if insert_net is not None:
                            detail += f", insert_net={insert_net}"
                        if mode_used == "hunk":
                            detail += f", swap_detected={'true' if swap_detected else 'false'}"
                        detail += ")"
                        append_failure(
                            errors,
                            FAILED_INSERT_DIFF_MISMATCH,
                            detail,
                        )
                elif insert_pass:
                    detail = (
                        f"{checklist_id}: definition_operation=promote showed insertion-like diff "
                        f"(mode={mode_used}, evidence={evidence_source}"
                    )
                    if insert_net is not None:
                        detail += f", insert_net={insert_net}"
                    if mode_used == "hunk":
                        detail += f", swap_detected={'true' if swap_detected else 'false'}"
                    detail += "); expected definition_operation=insert"
                    if args.fail_on_definition_operation_mismatch:
                        append_failure(
                            errors,
                            FAILED_DEFINITION_OPERATION_MISMATCH,
                            detail,
                        )
                    else:
                        append_warning(
                            warnings,
                            WARN_DEFINITION_OPERATION_MISMATCH,
                            detail,
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

        if len(wave_rows) > 1:
            max_pair_fraction = max(pair_counts.values()) / len(wave_rows)
            if max_pair_fraction > args.max_action_reason_fraction:
                append_failure(
                    errors,
                    FAILED_RATIONALE_MONOCULTURE,
                    (
                        f"{wave}: action+reason concentration {max_pair_fraction:.3f} exceeds "
                        f"{args.max_action_reason_fraction:.3f}"
                    ),
                )

        if len(wave_rows) > args.min_wave_size_for_multi_action and len(action_types) < args.min_unique_actions:
            append_failure(
                errors,
                FAILED_RATIONALE_MONOCULTURE,
                (
                    f"{wave}: requires >= {args.min_unique_actions} unique action_type values when "
                    f"row count > {args.min_wave_size_for_multi_action}"
                ),
            )

        if high_medium_total > 0:
            deviation_fraction = deviation_count / high_medium_total
            if deviation_fraction > args.max_deviation_fraction:
                append_failure(
                    errors,
                    FAILED_DEVIATION_CONCENTRATION,
                    (
                        f"{wave}: deviation concentration {deviation_fraction:.3f} exceeds "
                        f"{args.max_deviation_fraction:.3f}"
                    ),
                )

        for (id_a, reason_a), (id_b, reason_b) in itertools.combinations(reasons, 2):
            similarity = jaccard_similarity_reason(reason_a, reason_b)
            if similarity > args.max_reason_jaccard:
                append_failure(
                    errors,
                    FAILED_RATIONALE_MONOCULTURE,
                    (
                        f"{wave}: reason_why similarity {similarity:.3f} exceeds "
                        f"{args.max_reason_jaccard:.3f} for {id_a} vs {id_b}"
                    ),
                )
                break

    for checklist_id, row in completed_rows:
        term = (row.get("term") or "").strip()
        required_file = FOUNDATIONAL_REQUIRED_FILES.get(term)
        if required_file is None:
            continue

        permit_path = (row.get("deviation_permit_path") or "").strip()
        permit_sha = (row.get("deviation_permit_sha256") or "").strip()
        approved_by = (row.get("deviation_approved_by") or "").strip()
        deviation_status = (row.get("deviation_status") or "").strip()
        recommendation_used = (row.get("recommendation_used") or "").strip().lower()

        if permit_path or permit_sha or approved_by or deviation_status:
            append_failure(
                errors,
                FAILED_FOUNDATIONAL_PLACEMENT,
                (
                    f"{checklist_id}: foundational term does not allow deviation permit fields; "
                    "clear deviation_permit_path/deviation_permit_sha256/"
                    "deviation_approved_by/deviation_status"
                ),
            )

        if recommendation_used != "yes":
            append_failure(
                errors,
                FAILED_FOUNDATIONAL_PLACEMENT,
                f"{checklist_id}: foundational term requires recommendation_used=yes",
            )

        after_file = (row.get("after_file") or "").strip()
        if after_file != required_file:
            append_failure(
                errors,
                FAILED_FOUNDATIONAL_PLACEMENT,
                (
                    f"{checklist_id}: foundational placement requires after_file={required_file}, "
                    f"got {after_file}"
                ),
            )
        required_sections = FOUNDATIONAL_REQUIRED_SECTIONS.get(term, set())
        after_section = (row.get("after_section") or "").strip()
        if required_sections and after_section not in required_sections:
            append_failure(
                errors,
                FAILED_FOUNDATIONAL_PLACEMENT,
                (
                    f"{checklist_id}: foundational placement requires after_section in "
                    f"{sorted(required_sections)}, got '{after_section}'"
                ),
            )

    if args.strict_baseline_json is not None and args.strict_current_json is not None:
        baseline_missing, baseline_error = extract_missing_count(args.strict_baseline_json)
        current_missing, current_error = extract_missing_count(args.strict_current_json)
        if baseline_error:
            append_failure(errors, FAILED_STRICT_REGRESSION, baseline_error)
        if current_error:
            append_failure(errors, FAILED_STRICT_REGRESSION, current_error)
        if baseline_missing is not None and current_missing is not None:
            if current_missing > args.strict_max_missing:
                waiver_ok = args.strict_waiver_file is not None and args.strict_waiver_file.is_file()
                if not waiver_ok:
                    append_failure(
                        errors,
                        FAILED_STRICT_REGRESSION,
                        (
                            "strict missing_count regression without waiver: "
                            f"baseline={baseline_missing}, current={current_missing}, "
                            f"max={args.strict_max_missing}"
                        ),
                    )

    return pending_deviation_count, insert_diff_modes, definition_operation_diff_modes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate v3 checklist + ledger remediation gates")
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
        "--workdir",
        type=Path,
        help="Worktree root used for committed HEAD extraction checks",
    )
    parser.add_argument(
        "--glossary-file",
        type=Path,
        default=Path("src/glossary.rst"),
        help="Glossary file path (absolute or relative to --workdir)",
    )
    parser.add_argument(
        "--min-glossary-similarity",
        type=float,
        default=0.50,
        help="Minimum glossary/chapter similarity before mismatch warning/failure",
    )
    parser.add_argument(
        "--min-promote-similarity",
        type=float,
        default=0.72,
        help="Minimum similarity required for definition_operation=promote",
    )
    parser.add_argument(
        "--glossary-ack-json",
        type=Path,
        help="Reviewer acknowledgment JSON for known glossary mismatches in gate/final",
    )
    parser.add_argument(
        "--diff-mode",
        choices=["head"],
        default="head",
        help="Diff validation mode (head uses committed git state)",
    )
    parser.add_argument(
        "--diff-audit-json",
        type=Path,
        help="Optional per-run diff audit index JSON produced by orchestrator",
    )
    parser.add_argument(
        "--fail-on-definition-operation-mismatch",
        action="store_true",
        help=(
            "Promote rows that look insertion-like fail validation; "
            "default behavior emits WARN_DEFINITION_OPERATION_MISMATCH"
        ),
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
    if not (0.0 <= args.min_glossary_similarity <= 1.0):
        raise RuntimeError("--min-glossary-similarity must be between 0.0 and 1.0")
    if not (0.0 <= args.min_promote_similarity <= 1.0):
        raise RuntimeError("--min-promote-similarity must be between 0.0 and 1.0")
    warnings: list[str] = []
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

    pending_deviation_count = 0
    insert_diff_modes: dict[str, str] = {}
    definition_operation_diff_modes: dict[str, str] = {}
    if args.recovery_guardrails:
        (
            pending_deviation_count,
            insert_diff_modes,
            definition_operation_diff_modes,
        ) = enforce_recovery_guardrails(
            ordered_ids=ordered_ids,
            ledger_rows=ledger_rows,
            args=args,
            warnings=warnings,
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
        "pending_deviation_count": pending_deviation_count,
        "insert_diff_modes": insert_diff_modes,
        "definition_operation_diff_modes": definition_operation_diff_modes,
        "warning_count": len(warnings),
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
                f"pending_deviation_count={pending_deviation_count}",
                f"errors={len(errors)}",
            ]
        )
    )

    if args.json_out is not None:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(
            json.dumps({"summary": summary, "warnings": warnings, "errors": errors}, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    if args.markdown_out is not None:
        args.markdown_out.parent.mkdir(parents=True, exist_ok=True)
        write_markdown(args.markdown_out, summary, warnings, errors)

    for warning in warnings[:100]:
        print(f"WARN: {warning}")
    if len(warnings) > 100:
        print(f"WARN: ... {len(warnings) - 100} more")

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
