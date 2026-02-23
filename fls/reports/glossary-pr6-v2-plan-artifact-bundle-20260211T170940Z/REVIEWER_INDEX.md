# Reviewer Artifact Bundle (v2 refresh)

- Bundle: `glossary-pr6-v2-plan-artifact-bundle-20260211T170940Z`
- Created (UTC): `20260211T170940Z`
- Integrity manifest: `checksums.sha256`

## Included artifacts

| Relative path | Purpose |
|---|---|
| `planss/glossary-pr6-v2-step1-phase1-remediation-plan.md` | Primary v2 Step1/Phase1 execution plan, including explicit run-local reason rubric path. |
| `prompts/execute-glossary-pr6-v2-step1-phase1-plan.md` | Updated execution prompt with explicit v2 tooling paths. |
| `reports/validate-ledger-and-checklist-v2.py` | v2 validator for wave-prefixed IDs and 6-sub-item rubric checks. |
| `reports/glossary-batch-orchestrator-v2.py` | v2 orchestrator with rollback hardening, out-of-scope checks, and v3 follow-up fixes. |
| `reports/glossary-poor-questionable-reason-rubric.md` | Reason-quality rubric used by orchestrator defaults and run bootstrap. |
| `reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/fls-pr6-updated-analysis-v2.md` | Source analysis input for v2 remediation. |
| `reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/fls-pr6-placement-fitness-v2.json` | Placement fitness source input for v2 remediation. |
| `reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/fls-pr6-definition-divergence-v2.json` | Definition-divergence source input for v2 remediation. |
| `reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/checksums.sha256` | Original checksums delivered with v2 input bundle. |
| `reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/step1-phase1-v2-remediation-plan-proposal.md` | v2 plan proposal reference artifact. |
| `reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/plan-feedback/fls-pr6-remediation-plan-feedback.md` | Reviewer feedback on initial remediation plan. |
| `reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/plan-feedback/fls-pr6-remediation-plan-revised-feedback.md` | Reviewer feedback on revised remediation plan. |
| `reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/plan-feedback/fls-pr6-v2-plan-bundle-feedback.md` | Reviewer feedback identifying v1/v2 tooling mismatch. |
| `reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/plan-feedback/fls-pr6-v2-plan-bundle-v2-feedback.md` | Reviewer feedback identifying remaining v2 script issues. |
| `reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/plan-feedback/fls-pr6-v2-plan-bundle-v3-feedback.md` | Latest reviewer feedback confirming prior fixes and requesting final rollback polish. |
| `reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/templates/manual-placement-checklist-v2.template.md` | v2 checklist template with explicit v2 tool references. |
| `reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/templates/manual-placement-ledger-v2.template.csv` | v2 ledger template (schema baseline for validator/orchestrator). |
| `reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/templates/README-v2-tooling-contract.md` | Template/tooling compatibility contract for v2 execution. |
| `reports/glossary-pr6-v2-tooling-compat-20260211T151833Z/validation/tooling-compat/validator-init.json` | Validator v2 init-mode smoke evidence (machine-readable). |
| `reports/glossary-pr6-v2-tooling-compat-20260211T151833Z/validation/tooling-compat/validator-init.md` | Validator v2 init-mode smoke evidence (human-readable). |
| `reports/glossary-pr6-v2-tooling-compat-20260211T151833Z/validation/tooling-compat/validator-progress.json` | Validator v2 progress-mode smoke evidence. |
| `reports/glossary-pr6-v2-tooling-compat-20260211T151833Z/validation/tooling-compat/validator-progress.md` | Validator v2 progress-mode smoke evidence (markdown). |
| `reports/glossary-pr6-v2-tooling-compat-20260211T151833Z/validation/tooling-compat/orchestrator-dryrun.json` | Orchestrator dry-run evidence (wave-prefixed batch selection). |
| `reports/glossary-pr6-v2-tooling-compat-20260211T151833Z/validation/tooling-compat/orchestrator-gate-bplus-blocked.json` | Gate B+ hard-stop evidence when v3 artifacts are absent. |
| `reports/glossary-pr6-v2-tooling-compat-20260211T151833Z/validation/tooling-compat/summary.md` | Consolidated Gate T0 tooling-compatibility summary. |
| `reports/glossary-pr6-v2-script-fix-validation-20260211T161029Z/summary.md` | Consolidated validation for script fixes, including v3 follow-up scenarios. |
| `reports/glossary-pr6-v2-script-fix-validation-20260211T161029Z/fixtures/checklist-wa-two-items.template.md` | Two-item checklist fixture for script-fix scenarios. |
| `reports/glossary-pr6-v2-script-fix-validation-20260211T161029Z/fixtures/ledger-wa-two-items.template.csv` | Two-item ledger fixture for script-fix scenarios. |
| `reports/glossary-pr6-v2-script-fix-validation-20260211T161029Z/fixtures/baseline-wa-two-items.template.csv` | Baseline fixture paired with script-fix ledger scenarios. |
| `reports/glossary-pr6-v2-script-fix-validation-20260211T161029Z/tools/fake-opencode.py` | Deterministic harness used to trigger orchestrator failure modes. |
| `reports/glossary-pr6-v2-script-fix-validation-20260211T161029Z/results/zero-pass-run/batch-001-failure.json` | Zero-pass detailed failure record (batch 001). |
| `reports/glossary-pr6-v2-script-fix-validation-20260211T161029Z/results/zero-pass-run/batch-002-failure.json` | Zero-pass detailed failure record (batch 002). |
| `reports/glossary-pr6-v2-script-fix-validation-20260211T161029Z/results/zero-pass-run/orchestrator-summary.json` | Confirms run continuity and failed-batch accounting. |
| `reports/glossary-pr6-v2-script-fix-validation-20260211T161029Z/results/outer-exception-run3/batch-001-failure.json` | Outer exception rollback evidence from previous round. |
| `reports/glossary-pr6-v2-script-fix-validation-20260211T161029Z/results/out-of-scope-run/batch-001-failure.json` | Out-of-scope modification detection evidence from previous round. |
| `reports/glossary-pr6-v2-script-fix-validation-20260211T161029Z/results/crash-file-collision-run/batch-001-failure.json` | Preexisting failure record retained (no clobber). |
| `reports/glossary-pr6-v2-script-fix-validation-20260211T161029Z/results/crash-file-collision-run/batch-001-crash.json` | Crash-side record emitted when failure file already exists. |
| `reports/glossary-pr6-v2-script-fix-validation-20260211T161029Z/results/outer-exception-run4/batch-001-failure.json` | v3 follow-up evidence: outer exception now rolls back checklist/ledger and worktree. |
| `reports/glossary-pr6-v2-script-fix-validation-20260211T161029Z/results/out-of-scope-run2/batch-001-failure.json` | v3 follow-up evidence: out-of-scope rows include sub-item labels (`WA-002.1`..`.6`). |

All SHA256 values for included artifacts are recorded in `checksums.sha256`.
