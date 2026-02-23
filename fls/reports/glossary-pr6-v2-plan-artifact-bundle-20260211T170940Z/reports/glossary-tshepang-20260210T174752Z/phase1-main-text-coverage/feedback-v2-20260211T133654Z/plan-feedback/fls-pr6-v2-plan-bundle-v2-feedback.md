# Review: PR6 V2 Plan Artifact Bundle (20260211T152450Z)

**Bundle:** `glossary-pr6-v2-plan-artifact-bundle-20260211T152450Z`
**Review Date:** 2026-02-11

## Integrity

All 24 files present. `checksums.sha256` verified clean on every file. The REVIEWER_INDEX now uses a Purpose column with hashes delegated to the checksums file — this is fine and arguably cleaner than inline hashes.

## Overall Assessment

This bundle is a substantial improvement over the v1 bundle. Every issue identified in the prior review has been addressed:

- Validator and orchestrator are rewritten for v2 (wave-prefixed IDs, 6 sub-items, v2 column names)
- Tooling compatibility was smoke-tested and evidence is included (Gate T0)
- Plan now has Gate T0 as a hard blocker before G0
- Checklist and ledger templates reference v2-only tooling paths
- A README tooling contract document prevents accidental v1 usage
- Orchestrator has wave awareness, per-wave batch sizes, Gate B+ enforcement, partial-batch quarantine
- `phase2_status` correctly removed from validator (not relevant to this Phase 1 scope)
- Default paths updated to v2 artifact locations
- Execution prompt explicitly specifies v2 tooling paths

The consistency across all artifacts — plan, templates, validator, orchestrator, and execution prompt — is tight. There are two bugs and one enforcement gap worth fixing before execution.

## Bug: Double-Write on Zero-Passed Batch Failure

In `glossary-batch-orchestrator-v2.py`, when zero terms pass in a batch, two things happen:

1. **Lines 1024–1054** (inner handler): Rolls back checklist/ledger/worktree, quarantines all IDs, writes `batch-NNN-failure.json` with detailed fields (`passed: []`, `quarantined: [...]`, `reason`), then raises `RuntimeError`.

2. **Lines 1146–1157** (outer `except Exception`): Catches the RuntimeError, overwrites `batch-NNN-failure.json` with a minimal record (`error: str(exc)`, no pass/quarantine detail), then re-raises.

The second write clobbers the first. The detailed failure record (with the quarantined ID list and reason) is lost, replaced by a generic error string.

**Fix:** Either (a) skip the failure JSON write in the outer handler if the file already exists, (b) use a different filename for the outer handler (e.g., `batch-NNN-crash.json`), or (c) don't re-raise from the inner zero-passed path — instead `continue` the loop (since quarantine already happened and the state is clean).

Option (c) is probably cleanest: after quarantining all terms and writing the failure record, the orchestrator should continue to the next batch rather than crashing. The current behavior terminates the entire orchestration run on the first fully-failed batch, which may not be the intent.

## Bug: Outer Exception Handler Doesn't Roll Back

Related to the above: the outer `except Exception` handler (line 1146) writes a failure JSON and re-raises, but it does **not** restore the checklist/ledger from the pre-batch snapshot. If an exception occurs *after* `evaluate_batch_results` but *before* `git_commit_batch` (for example, during an `extra_check` command), the checklist and ledger will have been modified by the OpenCode agent but no commit will exist, leaving them in an inconsistent state.

The v1 orchestrator's outer handler did restore from snapshot. The v2 outer handler should do the same.

**Fix:** Add snapshot restoration to the outer handler:

```python
except Exception as exc:
    shutil.copy2(checklist_snapshot, checklist_path)
    shutil.copy2(ledger_snapshot, ledger_path)
    write_json(...)
    raise
```

## Enforcement Gap: Out-of-Scope Edit Verification Dropped

The plan requires "no out-of-scope checklist/ledger edits" (lines 203, 267) as a per-batch control. The v1 orchestrator enforced this with `verify_only_batch_ids_changed()`, which compared pre- and post-batch snapshots and flagged any modifications to rows outside the batch scope.

The v2 orchestrator removed this function entirely. With partial-batch handling, the quarantined rows do get modified (restored to snapshot + quarantine status marked), so a naive diff would false-positive on quarantined IDs. But there's still a real risk: the OpenCode agent could accidentally modify checklist/ledger rows for terms in other waves or other batches, and nothing would catch it.

**Fix:** Reintroduce `verify_only_batch_ids_changed()` with an exclusion set for quarantined IDs. Compare the pre-batch snapshot against the post-batch state for all IDs *not* in the current batch, and flag any unexpected changes. Run this check before committing.

## Non-Critical Observations

### Baseline Reference = Seed Ledger (Acceptable)

The orchestrator's `build_defaults()` sets both `seed_ledger` and `baseline_reference` to the same file (`manual-placement-ledger-v2.template.csv`). This is correct for initial bootstrap — the baseline *is* the seed before any edits. The `bootstrap_run_artifacts()` function copies them to separate files in the remediation directory and only copies if the target doesn't already exist, so the baseline stays immutable across re-runs.

### Template Has 6 Extra Columns Beyond Validator Requirements

The ledger template has 38 columns; the validator requires 32. The 6 extras (`after_evidence_ref`, `after_section`, `batch_id`, `notes`, `quarantine_reason`, `quarantine_status`) are operational fields used by the orchestrator for quarantine tracking and traceability but aren't quality-gate validated. This is the right design — the validator checks quality, the orchestrator manages operations.

### Reason Rubric Still References v1 Path

The orchestrator's default for `reason_rubric` points to `glossary-poor-questionable-reason-rubric.md` (v1 naming). This file isn't in the bundle. If this file doesn't exist at runtime, the orchestrator will fail at `ensure_exists()`. Either include it in the bundle, create a v2 version, or make the rubric path optional.

### Gate B+ Correctly Blocks WC/WD

The `select_active_wave()` → `v3_available()` check correctly gates WC and WD behind the presence of v3 artifacts. The dry-run evidence confirms WA-001 is selected first, and the Gate B+ blocked evidence confirms the hard stop fires when v3 files are absent. The `gate_b_plus_status` is persisted in orchestrator state, so re-runs after providing v3 artifacts will pass through.

### Tooling Compat Evidence Is Convincing

The validator init-mode test shows 1 parent with 6 sub-items, 0 checked, 0 errors — correct for a fresh template. The orchestrator dry-run correctly selects WA-001. The Gate B+ blocked test correctly identifies the three missing v3 files. These tests validate the core v2 behaviors.

## Summary

| # | Severity | Issue | Fix |
|---|----------|-------|-----|
| 1 | Bug | Zero-passed batch writes failure JSON twice; second write clobbers first | Skip outer write if file exists, or continue loop instead of raising |
| 2 | Bug | Outer exception handler doesn't restore checklist/ledger from snapshot | Add snapshot restoration to outer handler |
| 3 | Gap | Out-of-scope edit verification dropped from v2 orchestrator | Reintroduce with quarantine-aware exclusion set |
| 4 | Minor | Reason rubric default path references v1 file not in bundle | Include, rename, or make optional |

Fix items 1–3 and this bundle is ready to execute.
