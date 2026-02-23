# PR6 Recovery v3 Feedback Remediation Plan

## Scope

- [x] Capture remediation work for reviewer feedback in a separate executable plan.
- [x] Apply script and plan updates for deviation permit lifecycle redesign.
- [x] Apply script and plan updates for foundational section-level enforcement.
- [x] Exercise updated flows with smoke tests and artifact refresh.
- [x] Do not start Wave A execution.

## Inputs

- [x] Reviewer feedback source: `/Users/pete.levasseur/Downloads/fls-pr6-recovery-v3-feedback.md`.
- [x] Current scripts:
  - [x] `$OPENCODE_CONFIG_DIR/reports/record-rationale-v3.py`
  - [x] `$OPENCODE_CONFIG_DIR/reports/validate-ledger-and-checklist-v3.py`
  - [x] `$OPENCODE_CONFIG_DIR/reports/glossary-batch-orchestrator-v3.py`
  - [x] `$OPENCODE_CONFIG_DIR/reports/analyze-rationale-patterns-v3.py`
- [x] Current plan: `$OPENCODE_CONFIG_DIR/plans/glossary-pr6-wave-ab-recovery-guardrails-v3-plan.md`.

## Workstream A: Deviation Permit Lifecycle Redesign

### A1) Writer (`record-rationale-v3.py`)

- [x] Remove write-time `approved_by` non-empty requirement and self-approval check.
- [x] Require permit `status=pending-review` for high/medium non-move term completion.
- [x] Continue enforcing evidence quality and anti-boilerplate permit fields.
- [x] Write ledger `deviation_status=pending` for high/medium non-move decisions.
- [x] Emit event fields needed for later approval/rejection audit.

### A2) Approval script (`approve-deviation.py`)

- [x] Add `$OPENCODE_CONFIG_DIR/reports/approve-deviation.py`.
- [x] Support CLI: `--permit`, `--approved-by`, `--decision`, `--ledger`, `--events-jsonl`.
- [x] On approve: set permit status/approver and ledger deviation approval metadata.
- [x] On reject: set permit status rejected and ledger quarantine marker for re-execution.
- [x] Append immutable approval/rejection event with checklist ID, rationale UUID, and permit SHA.
- [x] Emit/update `deviation-review-summary.json` with filed/approved/rejected/pending totals.

### A3) Validator (`validate-ledger-and-checklist-v3.py`)

- [x] Add `deviation_status` ledger column requirement under recovery guardrails.
- [x] Add failure code `FAILED_PENDING_DEVIATIONS`.
- [x] In `progress` mode, allow pending deviations for completed rows.
- [x] In `gate`/`final` mode, fail pending deviations with `FAILED_PENDING_DEVIATIONS`.
- [x] Keep deviation concentration gate independent of approval status.
- [x] Ensure rejected deviations cannot pass gate/final as completed accepted rows.

### A4) Orchestrator (`glossary-batch-orchestrator-v3.py`)

- [x] Accept pending deviations in batch-level row checks.
- [x] Stop requiring `deviation_approved_by` during execution-time validation.
- [x] Include `deviation_status` in recovery ledger required columns.
- [x] Add `pending_deviation_count` to batch summary.

## Workstream B: Foundational Placement Section Enforcement

- [x] Add foundational allowed-section map in validator.
- [x] Enforce `after_section` for foundational term placements.
- [x] Keep file-level foundational enforcement and return `FAILED_FOUNDATIONAL_PLACEMENT` on mismatch.

## Workstream C: Plan and Matrix Corrections

- [x] Update foundational matrix entry for `method` to allowed section `Functions` only.
- [x] Update v3 recovery plan text/checklists for pending-review deviation lifecycle.
- [x] Add reviewer handoff artifact requirement for `deviation-review-summary.json`.

## Workstream D: Exercising and Artifacts

- [x] Update v3 fixtures for new permit/ledger fields and states.
- [x] Run script `--help` smoke checks for all affected scripts including `approve-deviation.py`.
- [x] Run writer smoke checks for pending deviation permit acceptance.
- [x] Run validator smoke checks for progress acceptance and gate/final pending-deviation failure.
- [x] Run foundational section mismatch smoke check.
- [x] Run approval flow smoke checks for approve and reject decisions.
- [x] Run orchestrator dry-run (no Wave A execution) to ensure prompt and summary compatibility.
- [x] Refresh `validation/recovery-guardrails-v3/` summaries and review index.

## Exit Criteria

- [x] All required script changes implemented and syntax-checked.
- [x] Smoke tests and flow exercises pass with stored artifacts.
- [x] Pending-deviation behavior is mode-correct (`progress` vs `gate/final`).
- [x] Foundational placements are enforced by file and section.
- [x] No Wave A run has been started.
