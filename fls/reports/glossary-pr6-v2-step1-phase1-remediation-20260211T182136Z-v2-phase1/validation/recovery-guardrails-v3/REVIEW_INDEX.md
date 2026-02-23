# Recovery Guardrails v3 Validation Index

- Scope: v2 -> v3 guardrail migration validation artifacts for rationale writer, validator, orchestrator, and rationale analyzer.

## Key files

- `smoke-test-summary.md`
- `integration-summary.md`
- `record-rationale-help.txt`
- `record-rationale-help-v4.txt`
- `validator-help.txt`
- `validator-help-v4.txt`
- `orchestrator-help.txt`
- `orchestrator-help-v4.txt`
- `rationale-analyzer-help.txt`
- `rationale-analyzer-help-v4.txt`
- `approve-deviation-help.txt`
- `record-rationale-success-v3.txt`
- `record-rationale-mismatch-v3.txt`
- `record-rationale-nonmove-no-permit-v3.txt`
- `record-rationale-bad-approved-by-v3.txt`
- `record-rationale-bad-permit-path-v3.txt`
- `record-rationale-pending-permit-success-v3.txt`
- `record-rationale-definition-success-v4.txt`
- `record-rationale-definition-compound-fail-v4.txt`
- `record-rationale-definition-stopword-not-success-v4.txt`
- `record-rationale-definition-stopword-no-success-v4.txt`
- `record-rationale-definition-stopword-but-success-v4.txt`
- `record-rationale-definition-stopword-as-success-v4.txt`
- `record-rationale-definition-stopword-if-success-v4.txt`
- `record-rationale-definition-stopword-so-success-v4.txt`
- `record-rationale-definition-success-v5.txt`
- `validator-success-v3.json`
- `validator-pending-progress-v3.json`
- `validator-pending-gate-fail-v3.json`
- `validator-approved-gate-v3.json`
- `validator-rejected-gate-fail-v3.json`
- `validator-foundational-section-fail-v3.json`
- `validator-dup-uuid-v3.json`
- `validator-strict-regression-v3.json`
- `validator-concentration-v3.json`
- `validator-definition-progress-warn-v4.json`
- `validator-definition-gate-missing-commit-fail-v4.json`
- `validator-definition-similarity-drift-fail-v4.json`
- `validator-definition-insert-diff-mismatch-fail-v4.json`
- `validator-definition-progress-pass-v5.json`
- `validator-definition-insert-swap-diff-audit-fail-v5.json`
- `validator-definition-insert-swap-live-fail-v5.json`
- `validator-definition-promote-subject-fail-v5.json`
- `validator-definition-insert-subject-fail-v5.json`
- `validator-definition-adapt-subject-fail-v5.json`
- `validator-definition-insert-swap-diff-audit-v5.json`
- `rationale-patterns-fixture-v3.json`
- `rationale-patterns-definition-v4.json`
- `orchestrator-dryrun-output-v3.txt`
- `orchestrator-dryrun-v3/batch-001-prompt.md`
- `orchestrator-dryrun-v3/batch-001-term-lock.json`
- `orchestrator-validator-classification-smoke-v3.json`
- `orchestrator-validator-hard-fail-smoke-v3.json`
- `approve-deviation-approve-v3.txt`
- `approve-deviation-reject-v3.txt`
- `deviation-review-summary-approve-v3.json`
- `deviation-review-summary-reject-v3.json`

## Notes

- This directory is specific to v3 tooling validation and does not supersede external analysis/review bundles provided by other contributors.
- v5 artifacts capture post-review hardening for swap-as-insert rejection and validator-side subject-form enforcement.
