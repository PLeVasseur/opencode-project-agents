# Review: PR6 V2 Plan Artifact Bundle (20260211T163206Z)

**Bundle:** `glossary-pr6-v2-plan-artifact-bundle-20260211T163206Z`
**Review Date:** 2026-02-11
**Prior Bundle:** `20260211T152450Z` (three blocking issues reported)

## Integrity

61 files, all 60 checksum entries verified clean. REVIEWER_INDEX present.

## Status of Prior-Review Issues

All three blocking issues from the `T152450Z` review are addressed, with test evidence for each:

| # | Prior Issue | Fix Applied | Evidence |
|---|------------|-------------|----------|
| 1 | Zero-pass batch clobbers failure JSON and terminates run | Zero-pass now `continue`s loop; failure JSON preserved | `zero-pass-run/`: two consecutive failures, both `batch-NNN-failure.json` intact with detail fields, `orchestrator-summary.json` has `batches_failed=2` |
| 2 | Outer exception handler doesn't restore checklist/ledger | Snapshot restore added; crash-vs-failure file collision handled | `outer-exception-run3/`: checklist and ledger byte-identical to pre-batch snapshot after `--extra-check "false"` trigger |
| 3 | Out-of-scope edit verification dropped | `verify_only_batch_ids_changed()` reintroduced with `excluded_ids` for quarantined terms | `out-of-scope-run/`: WA-002 changes detected and blocked when batch scope was WA-001 only |
| 4* | Reason rubric missing from bundle | `glossary-poor-questionable-reason-rubric.md` now included | File present, 37 lines, content matches orchestrator's default path |

The `fake-opencode.py` test harness is clean — it simulates `no-change`, `pass-first`, and `out-of-scope` modes, correctly modifying only the run-local checklist/ledger files passed via `--file`. The `crash-file-collision-run` evidence confirms the `-failure.json`/`-crash.json` separation works: the pre-seeded failure file is untouched, the new crash gets its own file.

## New Issues

### Issue 1 — Outer Exception Handler Missing `git restore` (Medium)

The zero-pass handler (line 1098) correctly does both:
1. Restore run-local checklist/ledger from snapshot
2. `git restore --staged --worktree .` to roll back spec-file changes in the worktree

The outer exception handler (line 1240) does only step 1. If an exception fires after the OpenCode agent has modified `.rst` spec files but before the commit — for example, if `verify_only_batch_ids_changed` detects out-of-scope edits, or an `--extra-check` fails — the checklist and ledger are restored but the spec-file changes remain in the worktree. The next re-run will see a dirty worktree and fail at the `git_status_porcelain` check unless `--allow-dirty` is passed.

The `rolled_back` field in the failure payload is also slightly misleading — it lists the checklist and ledger paths, implying a complete rollback, but the worktree spec files aren't rolled back.

**Fix — add git restore to the outer handler, between snapshot restore and failure payload assembly:**

```python
except Exception as exc:  # noqa: BLE001
    if checklist_snapshot.exists():
        shutil.copy2(checklist_snapshot, checklist_path)
    if ledger_snapshot.exists():
        shutil.copy2(ledger_snapshot, ledger_path)
    run_command(
        ["git", "restore", "--staged", "--worktree", "."],
        cwd=args.workdir,
        description="rollback worktree changes after batch exception",
        check=False,
    )

    failure_payload = {
        ...
```

And update `rolled_back` to include `"worktree"`:
```python
"rolled_back": [str(checklist_path), str(ledger_path), "worktree (git restore)"],
```

### Issue 2 — Out-of-Scope Check Reports Duplicate Lines (Low)

The test evidence in `out-of-scope-run/batch-001-failure.json` shows:

```
WA-002: checklist row changed outside batch
WA-002: checklist row changed outside batch
WA-002: checklist row changed outside batch
WA-002: checklist row changed outside batch
WA-002: checklist row changed outside batch
WA-002: checklist row changed outside batch
WA-002: checklist row changed outside batch
WA-002: ledger row changed outside batch
```

Seven identical "checklist row changed" messages for WA-002 (1 parent + 6 sub-items). Functionally correct, but noisy. The error is clear enough for debugging, so this doesn't block execution — just a quality-of-life improvement for later.

**Optional fix — include the sub-index in the checklist error message:**

In `verify_only_batch_ids_changed`, change:
```python
errors.append(f"{checklist_id}: checklist row changed outside batch")
```
to:
```python
label = f"{checklist_id}.{sub_index}" if sub_index > 0 else checklist_id
errors.append(f"{label}: checklist row changed outside batch")
```

## Non-Critical Observations

**Plan doesn't reference reason rubric by name.** The plan file has no `grep`-visible reference to `glossary-poor-questionable-reason-rubric.md`. The orchestrator's `build_defaults()` correctly resolves the path, and the file is bootstrapped into the remediation directory as `reason-rubric-v2.md`. This works, but the plan document's G0 checklist could benefit from an explicit line like `- [ ] Reason rubric available at $REMEDIATION_DIR/reason-rubric-v2.md`.

**Validator unchanged.** Byte-identical to the prior bundle. No issues.

**`batch_number` now includes failed batches.** The calculation `len(state["batches"]) + len(state["failed_batches"]) + 1` correctly prevents numbering gaps after zero-pass failures. Good.

**`--retry-quarantine` correctly breaks after zero-pass.** When enabled, a zero-pass batch triggers a `break` instead of `continue`, preventing an infinite loop where the same quarantined terms are re-selected and re-fail. Smart safeguard.

**Outer handler persists failure to state.** The `failed_batches` list in orchestrator state and `batches_failed` count in the summary both capture outer-exception failures. Re-runs will have accurate history.

## Summary

| # | Severity | Issue | Blocks Execution? |
|---|----------|-------|-------------------|
| 1 | Medium | Outer exception handler missing `git restore` — worktree left dirty after non-zero-pass failures | No, but causes friction on re-run (`--allow-dirty` needed) and risks stale spec edits leaking into next batch |
| 2 | Low | Out-of-scope check repeats same checklist_id 7 times | No |

Issue 1 is a one-line addition (the `run_command(["git", "restore", ...])` call). I'd fix it before Wave A. Issue 2 is cosmetic.

With issue 1 fixed, this bundle is ready to execute.
