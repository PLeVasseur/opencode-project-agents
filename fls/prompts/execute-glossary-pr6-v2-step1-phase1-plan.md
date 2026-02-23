Execute this plan in execute mode (not plan mode):
`$OPENCODE_CONFIG_DIR/plans/glossary-pr6-v2-step1-phase1-remediation-plan.md`

Requirements:
- Work in `/home/pete.levasseur/project/fls-wt/step1` on branch `glossary-step-1-main-text-coverage`.
- Do not push.
- Use v2-only tooling paths:
  - Validator: `$OPENCODE_CONFIG_DIR/reports/validate-ledger-and-checklist-v2.py`
  - Orchestrator: `$OPENCODE_CONFIG_DIR/reports/glossary-batch-orchestrator-v2.py`
- Execute actual Wave A/B remediation through the orchestrator in non-dry mode (`--dry-run` is only for Gate T0 tooling checks).
- Do not synthesize completion artifacts from prior runs (no backfilling checklist/ledger completion or `after_commit` hashes from old commits).
- Use a fresh `RUN_ID` / `REMEDIATION_DIR`; do not reuse prior remediation directories.
- If a prior invalid/aborted run exists, keep it immutable and include a supersession note in the new summary and reviewer index.
- Capture and report run boundary SHAs:
  - `START_HEAD` before wave execution
  - `WAVE_A_END_HEAD` at Gate A
  - `END_HEAD` at Gate B boundary
- Compute and report execution integrity:
  - `NEW_COMMIT_COUNT = git rev-list --count START_HEAD..END_HEAD`
  - `NEW_COMMIT_HASHES = git log --format=%H START_HEAD..END_HEAD`
  - `CHANGED_SRC_FILES = git diff --name-only START_HEAD..END_HEAD -- src`
- Hard-fail the run as `FAILED_INVALID_EXECUTION` (and stop) if any condition is true:
  - `NEW_COMMIT_COUNT == 0`
  - `CHANGED_SRC_FILES` is empty
  - Wave A/B is reported complete while orchestrator summary reports `batches_completed == 0`
- Execute through Wave A, Wave B, and Gate B+ boundary.
- If Wave B scope cannot be derived deterministically from locked v2 documents, stop before Wave B and report `BLOCKED_WAVE_B_UNCLEAR`.
- If Gate B+ is blocked on external v3 artifacts, stop cleanly and report blocked.

Reviewer handoff package:
- Build `$REMEDIATION_DIR/reviewer-bundle/`.
- Include all required artifacts (inputs, policy, wave term lists, checklist/ledger, batch summaries, validation outputs, logs, commit manifest, summary report).
- Include execution-integrity artifacts (`$REMEDIATION_DIR/reports/execution-integrity.json` and companion markdown if produced).
- Add reviewer index file listing each artifact and purpose.
- Create a zip archive: `$REMEDIATION_DIR/reviewer-bundle.zip`.
- Return exact paths and sha256 for the zip.

Return:
- Run directory and gate outcomes.
- Wave A/B completion status and commit ranges.
- Execution integrity verdict and metrics (`START_HEAD`, `WAVE_A_END_HEAD`, `END_HEAD`, `NEW_COMMIT_COUNT`).
- New commit hashes created in this run and changed `src/` files.
- Gate B+ status and any blockers.
- Reviewer bundle path and `sha256`.
