#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path


REQUIRED_PERMIT_KEYS = {
    "checklist_id",
    "term",
    "recommended_file",
    "recommended_section",
    "recommended_reason",
    "proposed_action",
    "proposed_location",
    "evidence_against_recommendation",
    "evidence_for_proposed",
    "reference_count_argument",
}


class DeviationApprovalError(RuntimeError):
    pass


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_ledger(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader), list(reader.fieldnames or [])


def write_ledger(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def parse_permit(path: Path) -> dict:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise DeviationApprovalError(f"invalid permit JSON: {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise DeviationApprovalError(f"permit payload must be an object: {path}")
    missing = sorted(key for key in REQUIRED_PERMIT_KEYS if not str(payload.get(key, "")).strip())
    if missing:
        raise DeviationApprovalError(f"permit missing required keys: {', '.join(missing)}")
    return payload


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Approve or reject filed deviation permits")
    parser.add_argument("--permit", type=Path, required=True)
    parser.add_argument("--approved-by", required=True)
    parser.add_argument("--decision", choices=["approve", "reject"], required=True)
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--events-jsonl", type=Path, required=True)
    parser.add_argument("--summary-json", type=Path)
    return parser.parse_args()


def summarize_deviations(rows: list[dict[str, str]]) -> dict:
    details = []
    filed = 0
    approved = 0
    rejected = 0
    pending = 0

    for row in rows:
        permit_path = (row.get("deviation_permit_path") or "").strip()
        if not permit_path:
            continue
        filed += 1
        status = (row.get("deviation_status") or "").strip().lower()
        if status == "approved":
            approved += 1
        elif status == "rejected":
            rejected += 1
        elif status == "pending":
            pending += 1

        details.append(
            {
                "checklist_id": (row.get("checklist_id") or "").strip(),
                "term": (row.get("term") or "").strip(),
                "status": status,
                "approved_by": (row.get("deviation_approved_by") or "").strip(),
                "permit_path": permit_path,
            }
        )

    return {
        "generated_at": utc_now(),
        "total_filed": filed,
        "total_approved": approved,
        "total_rejected": rejected,
        "total_pending": pending,
        "permits": sorted(details, key=lambda value: value.get("checklist_id") or ""),
    }


def main() -> int:
    args = parse_args()
    permit_path = args.permit.expanduser().resolve()
    ledger_path = args.ledger.expanduser().resolve()
    events_jsonl = args.events_jsonl.expanduser().resolve()

    if not permit_path.is_file():
        raise DeviationApprovalError(f"permit not found: {permit_path}")
    if not ledger_path.is_file():
        raise DeviationApprovalError(f"ledger not found: {ledger_path}")

    permit = parse_permit(permit_path)
    checklist_id = str(permit.get("checklist_id") or "").strip()
    permit_term = str(permit.get("term") or "").strip()
    current_status = str(permit.get("status") or "").strip().lower()
    if current_status and current_status not in {"pending-review", "approved", "rejected"}:
        raise DeviationApprovalError(
            "permit status must be pending-review, approved, or rejected"
        )

    approved_by = args.approved_by.strip()
    if not approved_by:
        raise DeviationApprovalError("--approved-by must be non-empty")

    target_status = "approved" if args.decision == "approve" else "rejected"
    permit["status"] = target_status
    permit["approved_by"] = approved_by
    permit_path.write_text(json.dumps(permit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    permit_sha = sha256_file(permit_path)

    rows, fieldnames = load_ledger(ledger_path)
    for column in [
        "deviation_permit_path",
        "deviation_permit_sha256",
        "deviation_approved_by",
        "deviation_status",
        "quarantine_status",
        "quarantine_reason",
    ]:
        if column not in fieldnames:
            fieldnames.append(column)

    row = None
    for candidate in rows:
        if (candidate.get("checklist_id") or "").strip() == checklist_id:
            row = candidate
            break
    if row is None:
        raise DeviationApprovalError(f"checklist_id not found in ledger: {checklist_id}")

    ledger_term = (row.get("term") or "").strip()
    if ledger_term != permit_term:
        raise DeviationApprovalError(
            f"permit term mismatch with ledger row: permit='{permit_term}' ledger='{ledger_term}'"
        )

    rationale_uuid = (row.get("rationale_uuid") or "").strip()
    if not rationale_uuid:
        raise DeviationApprovalError(f"ledger row missing rationale_uuid: {checklist_id}")

    row["deviation_permit_path"] = (row.get("deviation_permit_path") or "").strip() or str(permit_path)
    row["deviation_permit_sha256"] = permit_sha
    row["deviation_approved_by"] = approved_by
    row["deviation_status"] = target_status
    if target_status == "rejected":
        row["quarantine_status"] = "quarantined-deviation-rejected"
        row["quarantine_reason"] = f"deviation permit rejected by {approved_by}"
    elif (row.get("quarantine_status") or "").strip() == "quarantined-deviation-rejected":
        row["quarantine_status"] = ""
        row["quarantine_reason"] = ""

    write_ledger(ledger_path, rows, fieldnames)

    events_jsonl.parent.mkdir(parents=True, exist_ok=True)
    event = {
        "timestamp": utc_now(),
        "event_type": "deviation_reviewed",
        "decision": args.decision,
        "checklist_id": checklist_id,
        "term": permit_term,
        "rationale_uuid": rationale_uuid,
        "approved_by": approved_by,
        "deviation_status": target_status,
        "deviation_permit_path": str(permit_path),
        "deviation_permit_sha256": permit_sha,
    }
    with events_jsonl.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, sort_keys=True) + "\n")

    summary_path = args.summary_json
    if summary_path is None:
        summary_path = events_jsonl.parent / "deviation-review-summary.json"
    summary_path = summary_path.expanduser().resolve()
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary = summarize_deviations(rows)
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(
        "ok "
        f"checklist_id={checklist_id} "
        f"decision={args.decision} "
        f"status={target_status} "
        f"summary={summary_path}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except DeviationApprovalError as exc:
        print(f"ERROR: {exc}")
        raise SystemExit(2)
