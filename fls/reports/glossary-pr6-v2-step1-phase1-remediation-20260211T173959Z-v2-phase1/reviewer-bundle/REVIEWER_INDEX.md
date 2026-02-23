# Reviewer Bundle Index

Run: `20260211T173959Z-v2-phase1`
Worktree: `/home/pete.levasseur/project/fls-wt/step1`
Branch: `glossary-step-1-main-text-coverage`
Execution boundary: Wave A complete, Wave B complete, Gate B+ blocked on missing external v3 artifacts.

## Inputs and policy

- `inputs/`: locked v2 analysis/fitness/divergence inputs and plan-feedback files copied for run immutability.
- `inputs/checksums.sha256`: checksums for copied input files.
- `reports/policy-decisions-v2.md`: frozen conceptual-home-first policy decisions and exception rules.
- `reason-rubric-v2.md`: reason-quality rubric used by ledger decisions.

## Tooling compatibility (Gate T0)

- `validation/tooling-compat/validator-init.json`: validator init-mode machine-readable proof.
- `validation/tooling-compat/validator-init.md`: validator init-mode human-readable proof.
- `validation/tooling-compat/orchestrator-dryrun.json`: orchestrator dry-run and Gate B+ probe evidence.
- `validation/tooling-compat/summary.md`: Gate T0 compatibility summary and evidence index.
- `tools/`: immutable copies of v2 validator/orchestrator scripts used in this run.

## Baseline and environment (Gate G0)

- `baseline/summary.md`: baseline pass/fail and blockers summary.
- `baseline/git-status-start.txt`, `baseline/head-start.txt`: branch/HEAD lock at run start.
- `baseline/phase1-strict.json`, `baseline/phase1-strict.log`: strict phase baseline report.
- `baseline/make-clear.log`, `baseline/make-check-links.log`: baseline build and link-check logs.
- `baseline/uv-version.txt`, `baseline/glossary-migration-check-help.txt`, `baseline/make-help.txt`: toolchain sanity outputs.

## Wave scope and remediation records

- `waves/wave-a-terms.json`: frozen foundational Wave A term set (15 terms).
- `waves/wave-b-terms.json`: frozen Wave B term set (v2 high/medium priorities excluding Wave A).
- `waves/wave-a-patterns.md`, `waves/wave-b-patterns.md`: wave-level decision patterns and counts.
- `manual-placement-checklist-v2.md`: canonical run-local checklist at Wave B boundary.
- `manual-placement-ledger-v2.csv`: canonical run-local ledger at Wave B boundary.
- `manual-placement-baseline-reference-v2.csv`: baseline immutability reference used by validator.
- `manual-placement-checklist-v2.wave-a.md`, `manual-placement-ledger-v2.wave-a.csv`: Wave A checkpoint snapshot.
- `manual-placement-checklist-v2.wave-b.md`, `manual-placement-ledger-v2.wave-b.csv`: Wave B checkpoint snapshot.

## Batch summaries, validation, and commit manifest

- `batches/wave-a-summary.json`, `batches/wave-b-summary.json`: wave completion summaries including commit coverage.
- `batches/commit-manifest.csv`, `batches/commit-manifest.json`: checklist ID to evidence-commit mapping manifest.
- `batches/*-summary.json`: per-commit grouped summaries for reviewer drill-down.
- `validation/wave-a-validate-progress.json`, `validation/wave-a-validate-progress.md`: Wave A validator output.
- `validation/wave-b-validate-progress.json`, `validation/wave-b-validate-progress.md`: Wave B validator progress output.
- `validation/wave-b-validate-gate.json`, `validation/wave-b-validate-gate.md`: Gate B validator output.
- `validation/wave-a-phase1-strict.*`, `validation/wave-b-phase1-strict.*`: strict phase reports/logs for wave boundaries.
- `validation/wave-a-make-*.log`, `validation/wave-b-make-*.log`: build and link-check logs for wave boundaries.

## Gate B+ boundary and final run reporting

- `reports/gate-b-plus-status.json`: Gate B+ machine-readable status and missing artifact list.
- `reports/rescope-after-wave-b.md`: Gate B+ blocked report (external v3 artifacts missing).
- `reports/gate-outcomes.json`: consolidated gate outcomes (T0, G0, A, B, B+).
- `reports/phase1-v2-remediation-summary.md`: single reviewer-facing run summary report.
- `reports/wave-term-mapping.json`: WA/WB term-set construction details and uncovered prior-ledger terms.

## Notes

- No push was performed.
- Gate B+ remained blocked due missing external v3 artifacts; Wave C/D were not executed.
