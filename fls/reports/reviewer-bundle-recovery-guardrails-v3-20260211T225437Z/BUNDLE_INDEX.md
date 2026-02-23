# PR6 Wave A/B Recovery Guardrails v3 Reviewer Bundle

## Included scope

- `plan/glossary-pr6-wave-ab-recovery-guardrails-v3-plan.md`
- `scripts/record-rationale-v3.py`
- `scripts/validate-ledger-and-checklist-v3.py`
- `scripts/glossary-batch-orchestrator-v3.py`
- `scripts/analyze-rationale-patterns-v3.py`
- `feedback/fls-pr6-recovery-v3-feedback.md`
- `validation/recovery-guardrails-v3/` (smoke tests, dry-run artifacts, summaries, fixtures, review index)

## Reviewer starting points

- `validation/recovery-guardrails-v3/REVIEW_INDEX.md`
- `validation/recovery-guardrails-v3/smoke-test-summary.md`
- `validation/recovery-guardrails-v3/integration-summary.md`
- `validation/recovery-guardrails-v3/orchestrator-dryrun-v3/orchestrator-summary.json`
- `feedback/fls-pr6-recovery-v3-feedback.md`

## Notes

- Orchestrator strict command template default is:
  `uv run python tools/glossary-migration-check.py --phase 1 --strict --report "{report}"`
- Bundle generated on `2026-02-11T22:54:37Z`.
