#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import uuid
from datetime import UTC, datetime
from pathlib import Path


PARENT_RE = re.compile(r'^- \[[ xX]\] (?P<id>(?:W[ABCD]|QQ)-\d{3}) term="(?P<term>[^"]+)"$')
UUID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
    re.IGNORECASE,
)

MOVE_ACTIONS = {"move", "move+rewrite"}
HIGH_MEDIUM = {"high", "medium"}
PERMIT_STATUSES = {"pending-review", "approved", "rejected"}

BOILERPLATE_PATTERNS = [
    re.compile(r"Before .+\(.+\) used :dt:`.+`.+After .+uses :t:`", re.IGNORECASE | re.DOTALL),
    re.compile(r"retained .* paragraph .* rewrote term markup", re.IGNORECASE),
]


class GuardrailError(RuntimeError):
    pass


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_checklist_terms(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        match = PARENT_RE.match(line)
        if not match:
            continue
        checklist_id = match.group("id")
        term = match.group("term").strip()
        if checklist_id in result:
            raise GuardrailError(f"duplicate checklist_id in checklist: {checklist_id} (line {line_number})")
        result[checklist_id] = term
    return result


def load_ledger(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    return rows, fieldnames


def write_ledger(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def find_single_term_entry(path: Path, term: str) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    terms = payload.get("terms", [])
    matches = [entry for entry in terms if (entry.get("term") or "").strip() == term]
    if len(matches) != 1:
        raise GuardrailError(
            f"term lookup in {path.name} expected 1 match for '{term}', got {len(matches)}"
        )
    return matches[0]


def reject_boilerplate(label: str, value: str) -> None:
    normalized = value.strip()
    for pattern in BOILERPLATE_PATTERNS:
        if pattern.search(normalized):
            raise GuardrailError(f"{label} matches rejected boilerplate pattern")


def require_length(label: str, value: str, minimum: int) -> None:
    if len(value.strip()) < minimum:
        raise GuardrailError(f"{label} shorter than {minimum} characters")


def validate_uuid(value: str, label: str) -> None:
    if not UUID_RE.match(value):
        raise GuardrailError(f"{label} is not a valid UUID: {value}")


def parse_deviation_permit(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise GuardrailError(f"invalid deviation permit JSON: {path}: {exc}") from exc


def validate_permit_path_layout(permit_path: Path, checklist_id: str) -> None:
    expected_name = f"deviation-permit-{checklist_id}.json"
    if permit_path.name != expected_name:
        raise GuardrailError(
            f"deviation permit filename must be {expected_name}, got {permit_path.name}"
        )
    if permit_path.parent.name != "deviation-permits":
        raise GuardrailError(
            "deviation permit must live under a 'deviation-permits' directory"
        )


def validate_deviation_permit(
    *,
    permit: dict,
    permit_path: Path,
    checklist_id: str,
    term: str,
    placement_entry: dict,
) -> tuple[str, str, str]:
    recommended = placement_entry.get("recommended_location") or {}
    rec_file = (recommended.get("file") or "").strip()
    rec_section = (recommended.get("section") or "").strip()
    rec_reason = (recommended.get("reason") or "").strip()

    for field, expected in [
        ("checklist_id", checklist_id),
        ("term", term),
        ("recommended_file", rec_file),
        ("recommended_section", rec_section),
        ("recommended_reason", rec_reason),
    ]:
        actual = (permit.get(field) or "").strip()
        if actual != expected:
            raise GuardrailError(
                f"deviation permit mismatch for {field}: expected '{expected}', got '{actual}'"
            )

    status = (permit.get("status") or "").strip().lower()
    if not status:
        raise GuardrailError("deviation permit missing status")
    if status not in PERMIT_STATUSES:
        raise GuardrailError(
            "deviation permit status must be one of "
            f"{sorted(PERMIT_STATUSES)}, got '{status}'"
        )

    approved_by = (permit.get("approved_by") or "").strip()
    if status == "pending-review" and approved_by:
        raise GuardrailError("deviation permit pending-review must have empty approved_by")

    proposed_action = (permit.get("proposed_action") or "").strip()
    proposed_location = (permit.get("proposed_location") or "").strip()
    if not proposed_action:
        raise GuardrailError("deviation permit missing proposed_action")
    if not proposed_location:
        raise GuardrailError("deviation permit missing proposed_location")

    against = (permit.get("evidence_against_recommendation") or "").strip()
    proposed = (permit.get("evidence_for_proposed") or "").strip()
    ref_arg = (permit.get("reference_count_argument") or "").strip()

    require_length("evidence_against_recommendation", against, 200)
    require_length("evidence_for_proposed", proposed, 200)
    require_length("reference_count_argument", ref_arg, 120)

    reject_boilerplate("evidence_against_recommendation", against)
    reject_boilerplate("evidence_for_proposed", proposed)
    reject_boilerplate("reference_count_argument", ref_arg)

    permit_sha = sha256_file(permit_path)
    return approved_by, status, permit_sha


def ledger_deviation_status_from_permit(status: str) -> str:
    status = status.strip().lower()
    if status == "pending-review":
        return "pending"
    return status


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Write guarded rationale updates for one v3 checklist term"
    )
    parser.add_argument("--checklist-id", required=True)
    parser.add_argument("--checklist", type=Path, required=True)
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--placement-json", type=Path, required=True)
    parser.add_argument("--divergence-json", type=Path, required=True)
    parser.add_argument("--events-jsonl", type=Path, required=True)
    parser.add_argument("--batch-id", required=True)
    parser.add_argument("--implementer-id", required=True)
    parser.add_argument("--action-type", required=True)
    parser.add_argument("--decision-detail", required=True)
    parser.add_argument("--reason-code", required=True)
    parser.add_argument("--reason-why", required=True)
    parser.add_argument("--reason-quality", default="pass")
    parser.add_argument("--semantic-change-flag", required=True)
    parser.add_argument("--review-attention", required=True)
    parser.add_argument("--after-file", required=True)
    parser.add_argument("--after-line", required=True)
    parser.add_argument("--after-dp-id", required=True)
    parser.add_argument("--after-section", required=True)
    parser.add_argument("--phase1-status", default="completed")
    parser.add_argument("--final-quality", default="resolved-high")
    parser.add_argument("--deviation-permit", type=Path)
    parser.add_argument("--min-reason-length", type=int, default=80)
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    checklist_terms = parse_checklist_terms(args.checklist)
    checklist_term = checklist_terms.get(args.checklist_id)
    if checklist_term is None:
        raise GuardrailError(f"checklist_id not found in checklist: {args.checklist_id}")

    rows, fieldnames = load_ledger(args.ledger)
    id_to_index: dict[str, int] = {}
    for index, row in enumerate(rows):
        row_id = (row.get("checklist_id") or "").strip()
        if row_id:
            if row_id in id_to_index:
                raise GuardrailError(f"duplicate checklist_id in ledger: {row_id}")
            id_to_index[row_id] = index

    if args.checklist_id not in id_to_index:
        raise GuardrailError(f"checklist_id not found in ledger: {args.checklist_id}")

    row = rows[id_to_index[args.checklist_id]]
    ledger_term = (row.get("term") or "").strip()
    if ledger_term != checklist_term:
        raise GuardrailError(
            f"term mismatch for {args.checklist_id}: checklist='{checklist_term}' ledger='{ledger_term}'"
        )

    placement_entry = find_single_term_entry(args.placement_json, checklist_term)
    divergence_entry = find_single_term_entry(args.divergence_json, checklist_term)

    placement_term = (placement_entry.get("term") or "").strip()
    divergence_term = (divergence_entry.get("term") or "").strip()
    if placement_term != divergence_term or placement_term != checklist_term:
        raise GuardrailError(
            f"term-source lock failed for {args.checklist_id}: checklist='{checklist_term}', "
            f"placement='{placement_term}', divergence='{divergence_term}'"
        )

    reason_why = args.reason_why.strip()
    require_length("reason_why", reason_why, args.min_reason_length)
    reject_boilerplate("reason_why", reason_why)

    recommendation_priority = (placement_entry.get("relocation_priority") or "").strip()
    recommended = placement_entry.get("recommended_location") or {}
    recommended_file = (recommended.get("file") or "").strip()
    recommended_section = (recommended.get("section") or "").strip()

    action_type = args.action_type.strip()
    after_file = args.after_file.strip()
    is_high_medium = recommendation_priority in HIGH_MEDIUM
    used_recommendation = False

    deviation_path_text = ""
    deviation_sha = ""
    deviation_approved_by = ""
    deviation_status = ""

    if is_high_medium:
        if action_type in MOVE_ACTIONS:
            if recommended_file and after_file != recommended_file:
                raise GuardrailError(
                    "move action on high/medium term must target recommended file "
                    f"('{recommended_file}'), got '{after_file}'"
                )
            used_recommendation = True
        else:
            if args.deviation_permit is None:
                raise GuardrailError(
                    "high/medium non-move action requires --deviation-permit"
                )
            permit_path = args.deviation_permit
            if not permit_path.is_file():
                raise GuardrailError(f"deviation permit file missing: {permit_path}")
            validate_permit_path_layout(permit_path, args.checklist_id)
            permit = parse_deviation_permit(permit_path)
            deviation_approved_by, permit_status, deviation_sha = validate_deviation_permit(
                permit=permit,
                permit_path=permit_path,
                checklist_id=args.checklist_id,
                term=checklist_term,
                placement_entry=placement_entry,
            )
            if permit_status != "pending-review":
                raise GuardrailError(
                    "high/medium non-move action requires deviation permit status=pending-review"
                )
            if deviation_approved_by:
                raise GuardrailError(
                    "high/medium non-move action requires empty deviation permit approved_by"
                )
            deviation_path_text = str(permit_path)
            deviation_approved_by = ""
            deviation_status = "pending"
            used_recommendation = False
    else:
        if args.deviation_permit is not None:
            permit_path = args.deviation_permit
            if not permit_path.is_file():
                raise GuardrailError(f"deviation permit file missing: {permit_path}")
            validate_permit_path_layout(permit_path, args.checklist_id)
            permit = parse_deviation_permit(permit_path)
            deviation_approved_by, permit_status, permit_sha = validate_deviation_permit(
                permit=permit,
                permit_path=permit_path,
                checklist_id=args.checklist_id,
                term=checklist_term,
                placement_entry=placement_entry,
            )
            deviation_path_text = str(permit_path)
            deviation_sha = permit_sha
            deviation_status = ledger_deviation_status_from_permit(permit_status)

    rationale_uuid = str(uuid.uuid4())
    validate_uuid(rationale_uuid, "generated rationale_uuid")
    inserted_at = utc_now()
    rationale_digest = sha256_text(reason_why)

    updates = {
        "action_type": action_type,
        "decision_detail": args.decision_detail.strip(),
        "reason_code": args.reason_code.strip(),
        "reason_why": reason_why,
        "reason_quality": args.reason_quality.strip(),
        "semantic_change_flag": args.semantic_change_flag.strip(),
        "review_attention": args.review_attention.strip(),
        "after_file": after_file,
        "after_line": args.after_line.strip(),
        "after_dp_id": args.after_dp_id.strip(),
        "after_section": args.after_section.strip(),
        "phase1_status": args.phase1_status.strip(),
        "final_quality": args.final_quality.strip(),
        "batch_id": args.batch_id.strip(),
        "rationale_uuid": rationale_uuid,
        "rationale_inserted_at_utc": inserted_at,
        "rationale_text_sha256": rationale_digest,
        "recommendation_priority": recommendation_priority,
        "recommended_file": recommended_file,
        "recommended_section": recommended_section,
        "recommendation_used": "yes" if used_recommendation else "no",
        "deviation_permit_path": deviation_path_text,
        "deviation_permit_sha256": deviation_sha,
        "deviation_approved_by": deviation_approved_by,
        "deviation_status": deviation_status,
    }

    for key in updates:
        if key not in fieldnames:
            fieldnames.append(key)
    row.update(updates)

    write_ledger(args.ledger, rows, fieldnames)

    placement_sha = sha256_file(args.placement_json)
    divergence_sha = sha256_file(args.divergence_json)
    event = {
        "timestamp": inserted_at,
        "checklist_id": args.checklist_id,
        "term": checklist_term,
        "batch_id": args.batch_id.strip(),
        "rationale_uuid": rationale_uuid,
        "implementer_id": args.implementer_id.strip(),
        "reason_code": args.reason_code.strip(),
        "reason_why_sha256": rationale_digest,
        "action_type": action_type,
        "after_file": after_file,
        "recommendation_priority": recommendation_priority,
        "recommended_file": recommended_file,
        "recommended_section": recommended_section,
        "recommendation_used": "yes" if used_recommendation else "no",
        "placement_json": str(args.placement_json),
        "placement_sha256": placement_sha,
        "divergence_json": str(args.divergence_json),
        "divergence_sha256": divergence_sha,
        "deviation_permit_path": deviation_path_text,
        "deviation_permit_sha256": deviation_sha,
        "deviation_approved_by": deviation_approved_by,
        "deviation_status": deviation_status,
        "event_type": "rationale_recorded",
    }

    args.events_jsonl.parent.mkdir(parents=True, exist_ok=True)
    with args.events_jsonl.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, sort_keys=True) + "\n")

    print(f"ok checklist_id={args.checklist_id} rationale_uuid={rationale_uuid}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except GuardrailError as exc:
        print(f"ERROR: {exc}")
        raise SystemExit(2)
