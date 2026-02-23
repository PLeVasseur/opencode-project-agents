# Recovery Guardrails Review Bundle

- Purpose: provide a fair-review package for the revised PR6 Wave A/B recovery plan, guardrail scripts, and smoke-test evidence before re-executing Wave A/B.
- Source run: `glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1`.

## Contents

- `plan/`: recovery plan and baseline execution plan used for comparison.
- `scripts/`: updated/new guardrail scripts under review.
- `feedback/`: reviewer feedback and v3 critique context that drove changes.
- `smoke-tests/recovery-guardrails/`: full smoke-test artifacts including fixtures, outputs, dry-run prompt, and term-lock manifest.
- `context/`: prior execution integrity and supersession context for fair assessment.
- `checksums.sha256`: SHA256 for every file in this bundle.

## Key Review Targets

- `plan/glossary-pr6-wave-ab-recovery-guardrails-plan.md`
- `scripts/record-rationale-v2.py`
- `scripts/validate-ledger-and-checklist-v2.py`
- `scripts/glossary-batch-orchestrator-v2.py`
- `scripts/analyze-rationale-patterns-v2.py`
- `smoke-tests/recovery-guardrails/smoke-test-summary.md`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun/batch-001-prompt.md`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun/batch-001-term-lock.json`

## Smoke Test Summary

- Expected summary: `16/16` checks passed (see smoke-test summary file).

## Inventory (relative paths)

- `context/execution-integrity-manual-check.json`
- `context/execution-integrity-manual-check.md`
- `context/gate-b-plus-status.json`
- `context/phase1-v2-remediation-summary.md`
- `context/rescope-after-wave-b.md`
- `context/supersession-note.md`
- `feedback/fls-pr6-recovery-plan-feedback.md`
- `feedback/fls-pr6-updated-analysis-v3.md`
- `feedback/fls-pr6-v3-wave-ab-concerns.md`
- `feedback/fls-pr6-v3-wave-ab-review.md`
- `plan/glossary-pr6-v2-step1-phase1-remediation-plan.md`
- `plan/glossary-pr6-wave-ab-recovery-guardrails-plan.md`
- `scripts/analyze-rationale-patterns-v2.py`
- `scripts/glossary-batch-orchestrator-v2.py`
- `scripts/record-rationale-v2.py`
- `scripts/validate-ledger-and-checklist-v2.py`
- `smoke-tests/recovery-guardrails/fixtures/baseline-two.csv`
- `smoke-tests/recovery-guardrails/fixtures/baseline.csv`
- `smoke-tests/recovery-guardrails/fixtures/checklist-two.md`
- `smoke-tests/recovery-guardrails/fixtures/checklist-unchecked.md`
- `smoke-tests/recovery-guardrails/fixtures/checklist.md`
- `smoke-tests/recovery-guardrails/fixtures/deviation-permit-WA-001-bad-approved.json`
- `smoke-tests/recovery-guardrails/fixtures/deviation-permit-WA-001.json`
- `smoke-tests/recovery-guardrails/fixtures/divergence-mismatch.json`
- `smoke-tests/recovery-guardrails/fixtures/divergence.json`
- `smoke-tests/recovery-guardrails/fixtures/events-two.jsonl`
- `smoke-tests/recovery-guardrails/fixtures/events.jsonl`
- `smoke-tests/recovery-guardrails/fixtures/ledger-concentration.csv`
- `smoke-tests/recovery-guardrails/fixtures/ledger-dup-uuid.csv`
- `smoke-tests/recovery-guardrails/fixtures/ledger.csv`
- `smoke-tests/recovery-guardrails/fixtures/placement.json`
- `smoke-tests/recovery-guardrails/fixtures/strict-baseline.json`
- `smoke-tests/recovery-guardrails/fixtures/strict-current-bad.json`
- `smoke-tests/recovery-guardrails/fixtures/strict-current-ok.json`
- `smoke-tests/recovery-guardrails/integration-summary.md`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun/baseline/start-head.txt`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun/batch-001-dryrun.json`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun/batch-001-prompt.md`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun/batch-001-term-lock.json`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun/checklist-progress.md`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun/manual-placement-baseline-reference-v2.csv`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun/manual-placement-checklist-v2.md`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun/manual-placement-ledger-v2.csv`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun/orchestrator-summary.json`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun/orchestrator-v2-state.json`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun/reason-rubric-v2.md`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun/reports/execution-integrity.json`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun/reports/execution-integrity.md`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun/validate-progress-preflight.json`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun/waves/wave-b-end-head.txt`
- `smoke-tests/recovery-guardrails/orchestrator-dryrun-output.txt`
- `smoke-tests/recovery-guardrails/orchestrator-help.txt`
- `smoke-tests/recovery-guardrails/rationale-analyzer-help.txt`
- `smoke-tests/recovery-guardrails/rationale-patterns-fixture.json`
- `smoke-tests/recovery-guardrails/rationale-patterns-fixture.md`
- `smoke-tests/recovery-guardrails/rationale-patterns-fixture.txt`
- `smoke-tests/recovery-guardrails/record-rationale-bad-approved-by.txt`
- `smoke-tests/recovery-guardrails/record-rationale-help.txt`
- `smoke-tests/recovery-guardrails/record-rationale-mismatch.txt`
- `smoke-tests/recovery-guardrails/record-rationale-nonmove-no-permit.txt`
- `smoke-tests/recovery-guardrails/record-rationale-success.txt`
- `smoke-tests/recovery-guardrails/smoke-test-summary.md`
- `smoke-tests/recovery-guardrails/validator-concentration.json`
- `smoke-tests/recovery-guardrails/validator-concentration.md`
- `smoke-tests/recovery-guardrails/validator-concentration.txt`
- `smoke-tests/recovery-guardrails/validator-dup-uuid.json`
- `smoke-tests/recovery-guardrails/validator-dup-uuid.md`
- `smoke-tests/recovery-guardrails/validator-dup-uuid.txt`
- `smoke-tests/recovery-guardrails/validator-help.txt`
- `smoke-tests/recovery-guardrails/validator-strict-regression.json`
- `smoke-tests/recovery-guardrails/validator-strict-regression.md`
- `smoke-tests/recovery-guardrails/validator-strict-regression.txt`
- `smoke-tests/recovery-guardrails/validator-success.json`
- `smoke-tests/recovery-guardrails/validator-success.md`
- `smoke-tests/recovery-guardrails/validator-success.txt`
