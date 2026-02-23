# Glossary poor/questionable orchestrator implementation plan

## Objective

- [x] Build a Python orchestrator that repeatedly calls `opencode run` to remediate terms in batches of `20`.
- [x] Enforce one commit per completed batch in the target worktree branch.
- [x] Reuse the existing checklist, ledger, baseline-reference, and validator artifacts under `$OPENCODE_CONFIG_DIR/reports/`.

## Hard requirements

- [x] Batch size is configurable but defaults to `20`.
- [x] Each batch is selected from the next unchecked parent IDs (`PQ-###`) in checklist order.
- [x] Each batch triggers one git commit on success (or fails loudly if commit cannot be made).
- [x] Script does not perform bulk scripted term adjudication; OpenCode performs manual term-by-term remediation via prompt instructions.

## Implementation stages

### Stage A: bootstrap and safety

- [x] Resolve `OPENCODE_CONFIG_DIR` and default artifact paths.
- [x] Create a timestamped remediation directory when one is not provided.
- [x] Seed run-local ledger/baseline files from canonical seed artifacts when missing.
- [x] Verify required files exist (plan, checklist, seed ledger, baseline reference, validator).
- [x] Verify target worktree/branch and clean git status by default before automation starts.

### Stage B: orchestration engine

- [x] Parse checklist parent/sub-item state and select the next unchecked 20 IDs.
- [x] Build a strict batch prompt referencing plan/checklist/ledger/rubric/validator paths.
- [x] Execute `opencode run --format json` per batch and capture JSONL logs.
- [x] Persist/resume OpenCode `session_id` across batches using a run-local state file.

### Stage C: gates and verification

- [x] Run unified validator in `progress` mode before and after each batch.
- [x] Enforce per-batch completion checks for selected IDs (parent + all sub-items + ledger quality fields).
- [x] Stop execution on first failure with explicit error output.

### Stage D: batch commit workflow

- [x] Stage all repo changes in target worktree after successful validation.
- [x] Create one conventional commit per batch (`docs(glossary): remediate placement terms PQ-xxx-PQ-yyy`).
- [x] Optionally allow empty commits (flag-controlled); default behavior fails if there are no changes.
- [x] Write commit hash back into ledger `after_commit` for batch IDs.

### Stage E: completion and reporting

- [x] Emit per-batch artifacts (`opencode.jsonl`, validator JSON, batch summary JSON).
- [x] Emit run-level state file and machine-readable summary at end of execution.
- [x] Run unified validator in `final` mode when checklist completion is reached.

## Verification tasks

- [x] `python3 -m py_compile` passes for the orchestrator script.
- [x] Script `--help` renders expected arguments.
- [x] Dry/smoke invocation validates control flow without launching full remediation.

## Deliverables

- [x] Orchestrator script under `$OPENCODE_CONFIG_DIR/reports/`.
- [x] Updated operational usage notes in this plan and execution summary.
