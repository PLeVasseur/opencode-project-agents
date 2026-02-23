# Checklist and ledger validation (v3)

- Mode: `gate`
- Parent items: `2/2` checked
- Sub-items: `12/12` checked
- Ledger rows: `2`
- Baseline rows: `2`
- Completed ledger rows: `2`
- Resolved-high rows: `2`
- Error count: `19`

## Errors

- WA-001: missing decision_detail (action recorded)
- WA-001: missing reason_code (action recorded)
- WA-001: missing decision_detail (reason quality)
- WA-001: invalid reason_code '' (reason quality)
- WA-001: reason_why shorter than 80 characters (reason quality)
- WA-001: missing decision_detail (completed-row)
- WA-001: invalid reason_code '' (completed-row)
- WA-001: reason_why shorter than 80 characters (completed-row)
- events line 1: missing rationale_uuid
- FAILED_UUID_GUARDRAIL: WA-001: missing rationale_uuid
- FAILED_UUID_GUARDRAIL: WA-001: missing rationale_inserted_at_utc
- FAILED_UUID_GUARDRAIL: WA-001: missing rationale_text_sha256
- FAILED_UUID_GUARDRAIL: WA-001: no rationale events found
- FAILED_UUID_GUARDRAIL: WA-001: no matching rationale event for rationale_uuid=
- FAILED_UUID_GUARDRAIL: WA-002: missing rationale_uuid
- FAILED_UUID_GUARDRAIL: WA-002: missing rationale_inserted_at_utc
- FAILED_UUID_GUARDRAIL: WA-002: missing rationale_text_sha256
- FAILED_UUID_GUARDRAIL: WA-002: latest event uuid mismatch (row=, latest_event=11111111-2222-4333-8444-555555555555)
- FAILED_UUID_GUARDRAIL: WA-002: no matching rationale event for rationale_uuid=
