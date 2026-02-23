Run the glossary placement orchestrator in execute mode.

Context:
- Repo root: `/home/pete.levasseur/project/fls`
- Target worktree: `/home/pete.levasseur/project/fls-wt/step1`
- Expected branch: `glossary-step-1-main-text-coverage`
- Batch orchestrator: `$OPENCODE_CONFIG_DIR/reports/glossary-batch-orchestrator.py`
- Manual remediation plan: `$OPENCODE_CONFIG_DIR/plans/glossary-poor-questionable-manual-remediation-plan.md`
- Checklist: `$OPENCODE_CONFIG_DIR/reports/glossary-poor-questionable-202-checklist.md`
- Validator: `$OPENCODE_CONFIG_DIR/reports/validate-ledger-and-checklist.py`

Hard requirements:
1. Use batch size `20`.
2. Enforce exactly one commit per completed batch.
3. Stop immediately on any failure (validator, orchestrator, or commit failure).
4. Do not push to remote.
5. Preserve unrelated user edits; do not reset/revert unrelated changes.

Execution flow:
1. Preflight:
   - verify `OPENCODE_CONFIG_DIR` is set,
   - verify script/plan/checklist/validator files exist,
   - verify target worktree is on `glossary-step-1-main-text-coverage`.
2. Create one run ID and one remediation directory:
   - `RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)-orchestrator"`
   - `REMEDIATION_DIR="$OPENCODE_CONFIG_DIR/reports/glossary-poor-questionable-manual-remediation-$RUN_ID"`
3. Pilot batch (exactly one batch):
   - run the orchestrator with `--batch-size 20 --max-batches 1 --remediation-dir "$REMEDIATION_DIR"`.
4. If pilot succeeds, continue full execution from the same remediation directory:
   - rerun orchestrator with `--batch-size 20 --remediation-dir "$REMEDIATION_DIR"` (no `--max-batches`).
5. After completion, run final validator in `final` mode if not already done by orchestrator.

Commands:

```bash
RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)-orchestrator"
REMEDIATION_DIR="$OPENCODE_CONFIG_DIR/reports/glossary-poor-questionable-manual-remediation-$RUN_ID"

python3 "$OPENCODE_CONFIG_DIR/reports/glossary-batch-orchestrator.py" \
  --workdir "/home/pete.levasseur/project/fls-wt/step1" \
  --expected-branch "glossary-step-1-main-text-coverage" \
  --batch-size 20 \
  --max-batches 1 \
  --remediation-dir "$REMEDIATION_DIR"

python3 "$OPENCODE_CONFIG_DIR/reports/glossary-batch-orchestrator.py" \
  --workdir "/home/pete.levasseur/project/fls-wt/step1" \
  --expected-branch "glossary-step-1-main-text-coverage" \
  --batch-size 20 \
  --remediation-dir "$REMEDIATION_DIR"
```

Finish by returning:
- Pilot batch result (IDs, commit hash, validator status).
- Full run result (number of batches, remaining IDs, final validator status).
- Exact `REMEDIATION_DIR` path.
- Per-batch commit list (batch number -> commit hash -> ID range).
- Any blockers/deviations and proposed next actions.
