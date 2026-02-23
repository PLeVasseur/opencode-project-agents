# Reviewer index

## Run context

- `orchestrator-summary.json`: final orchestrator run summary (boundaries, commit counts, changed src files).
- `orchestrator-v2-state.json`: per-batch state machine record with commit hashes and batch membership.
- `reports/supersession-note.md`: supersession note for prior invalid/aborted run kept immutable.

## Inputs and policy

- `inputs/`: locked v2 inputs, plan feedback, seed provenance, and `inputs/checksums.sha256`.
- `reports/policy-decisions-v2.md`: frozen conceptual-home-first policy and missing-term closure rules.
- `reason-rubric-v2.md`: rationale quality rubric used during adjudication.

## Checklist and ledger

- `manual-placement-checklist-v2.md`: run-local checklist with WA/WB completion state.
- `manual-placement-ledger-v2.csv`: run-local ledger with action/rationale/after anchors and in-run commit mapping.
- `manual-placement-baseline-reference-v2.csv`: immutable baseline reference used by validator.
- `checklist-progress.md`: latest consolidated validator markdown snapshot.

## Wave scope and outcomes

- `waves/wave-a-terms.json`: frozen Wave A term list.
- `waves/wave-b-terms.json`: deterministic Wave B term derivation from locked v2 placement priorities.
- `waves/wave-a-patterns.md`: Wave A gate outcomes and observed edit patterns.
- `waves/wave-b-patterns.md`: Wave B gate outcomes and observed edit patterns.
- `waves/wave-a-gate-checks.json`: Wave A boundary checks (resolved terms, commit window, changed src files).
- `waves/wave-b-gate-checks.json`: Wave B boundary checks (resolved terms, commit window, changed src files).
- `waves/wave-a-end-head.txt`: WAVE_A_END_HEAD boundary SHA.
- `waves/wave-b-end-head.txt`: END_HEAD (Gate B boundary) SHA.

## Validation and logs

- `validation/tooling-compat/`: Gate T0 compatibility artifacts (validator init, orchestrator dry-run, summary, help captures).
- `baseline/`: Gate G0 baseline captures (git status, START_HEAD, strict check, build/link logs, summary).
- `batch-00*-validate-progress.json` and `batch-00*-validate-post-commit.json`: per-batch validator evidence.
- `batch-00*-opencode.jsonl`: orchestrator OpenCode execution logs per batch.
- `waves/wave-a-phase1-strict.*` and `waves/wave-b-phase1-strict.*`: strict phase checks at Gate A/B.
- `waves/wave-a-make-*.log` and `waves/wave-b-make-*.log`: build and link-check logs at wave gates.

## Commit and integrity evidence

- `batches/commit-manifest.csv`: batch-to-commit manifest for all six in-run commits.
- `reports/execution-integrity.json`: orchestrator-computed integrity contract artifact.
- `reports/execution-integrity.md`: human-readable integrity report companion.
- `reports/execution-integrity-manual-check.json`: explicit hard-fail rule evaluation (`FAILED_INVALID_EXECUTION` guard).
- `reports/execution-integrity-manual-check.md`: markdown companion for manual integrity evaluation.
- `reports/new-commit-hashes.txt`: git log hashes for `START_HEAD..END_HEAD`.
- `reports/changed-src-files.txt`: changed `src/` files for `START_HEAD..END_HEAD`.

## Final reporting

- `reports/phase1-v2-remediation-summary.md`: primary remediation summary (policy, wave outcomes, boundaries, counts, blockers).
- `reports/gate-b-plus-status.json`: Gate B+ blocked status and missing v3 artifact list.
- `reports/rescope-after-wave-b.md`: Gate B+ boundary report and stop rationale.
- `tools/`: immutable copy of v2 validator/orchestrator plus `tools/checksums.sha256`.
