# PR #32: Restructured Plan Critique (v3)

## Summary

Every blocker from the last round has been addressed: validation now precedes publishing (Phase 6 before Phase 7), commit 0 explicitly doesn't remove `log`/`env_logger`/`async-std` from the workspace, the overlap check is an appendix invoked from Phase 3, the exception list covers all `Cargo.toml` files, and the overlap is pre-sized at ~16 files. The `subscription-cache` exclusion from commit 0 is explicit. The completion criteria now include the workspace dep constraint. Good work.

Two issues remain. One will cause a compile failure. The other is a gap in execution strategy that, depending on the executor, could cause a lot of wasted time.

---

## Issue 1: Workspace member additions will break `cargo check` (compile failure)

The workspace `Cargo.toml` adds two new members in the final state:

```toml
members = [
    ...
    "utils/criterion-guardrail",    # new
    "utils/transport-smoke-suite",  # new
    ...
]
```

But these directories don't exist until commit 4 and commit 5 respectively. If commit 2's "manifest/workspace changes for module and crate ownership" (line 189) stages the final workspace `Cargo.toml` — which includes these member entries — then `cargo check --workspace` will fail because Cargo can't find the crate directories.

The plan only mentions the workspace `Cargo.toml` in the context of removing `subscription-cache` and obsolete deps (line 189). It never says "do NOT add `criterion-guardrail` or `transport-smoke-suite` to workspace members yet." Since `Cargo.toml` is in the multi-touch exception list, touching it in multiple commits is allowed, but the plan needs to be explicit about *what* changes land *when*:

| Commit | Workspace `Cargo.toml` changes |
|--------|-------------------------------|
| 0 | Add `tracing`, `tracing-subscriber` to `[workspace.dependencies]` |
| 2 | Remove `subscription-cache` from members. Remove `log`, `env_logger`, `async-std` from `[workspace.dependencies]` |
| 4 | Add `utils/criterion-guardrail` to members |
| 5 | Add `utils/transport-smoke-suite` to members |

Similarly, `up-streamer/Cargo.toml` adds `criterion` and `[[bench]]` in the final state — those must land in commit 4, not commit 2.

**Fix:** Add explicit workspace manifest scoping to commits 2, 4, and 5. Either add a guardrail ("do NOT add workspace members for crates not yet created") or enumerate the exact workspace `Cargo.toml` changes per commit.

---

## Issue 2: The staging strategy doesn't support intermediate file states

Phase 2 materializes all changes as unstaged (`git reset --soft $BASE_SHA` then `git reset HEAD .`). Phase 3 then stages subsets for each commit. This works for single-touch files — stage the final on-disk state, done — but **breaks for commit 0's overlapping files**.

After Phase 2, every file is in its **final** state on disk. For commit 0, you need files in an **intermediate** state (only the `log → tracing` swap, not the architectural changes). You can't `git add ustreamer.rs` because that would stage all 2,288 changed lines, not just the 4 log-related lines.

The natural thought is `git add -p` (interactive patch mode). I checked the actual diffs. The log→tracing changes are **in the same hunk** as architectural changes for most of the overlapping files:

| File | Log lines | Total changed | Hunk separable? |
|------|-----------|---------------|----|
| `up-streamer/src/ustreamer.rs` | 4 | 2,288 | **No** — entire import section is one rewrite hunk |
| `configurable-streamer/src/main.rs` | 4 | 232 | **No** — `use log::info` → `use tracing::info` is in same hunk as other import additions |
| `example-streamer-implementations/.../zenoh_someip.rs` | 4 | 131 | **No** — same pattern |
| `up-streamer/src/endpoint.rs` | 7 | 12 | Edge case — nearly all changes are log-related |
| `up-streamer/tests/single_local_single_remote.rs` | 2 | 45 | **No** — log swap entangled with `mod support;` and import changes |
| `up-streamer/tests/..._add_remove_rules.rs` | 2 | 122 | **No** — same pattern |
| `up-streamer/tests/..._different_remote_transport.rs` | 2 | 47 | Maybe — smaller diff, might split |
| `up-streamer/tests/..._same_remote_transport.rs` | 2 | 43 | Maybe |
| `utils/.../integration_test_utils.rs` | 2 | 185 | **Yes** — log swap in import region, new functions are separate hunks |
| `utils/.../up_client_foo.rs` | 2 | 14 | Maybe |
| `utils/usubscription-static-file/src/lib.rs` | 2 | 525 | **No** — import changes are entangled |

For the "No" files, creating the intermediate state requires line-by-line hunk editing (`git add -p` with the `e` option) or a different workflow. This is extremely error-prone and the plan provides no guidance on it.

**Three strategies (pick one):**

**Strategy A (recommended): Narrow commit 0 to only fully-finalizable files.** Don't include ANY overlapping `.rs` files in commit 0. Only include the ~12 `example-streamer-uses/` files where 100% of the diff is `log → tracing`, plus the 2-3 `integration-test-utils` files with cleanly separable hunks, plus `endpoint.rs` (which is essentially all log removal). Cargo.toml dep additions land as wiring-exception touches. The log migration in `ustreamer.rs`, `main.rs`, `zenoh_someip.rs`, and most test files just becomes part of their respective later commits (2 or 3). The overlap exception drops from ~16 files to essentially zero for `.rs` files. Execution becomes trivial: `git add` each file, no patch surgery.

The tradeoff: some files' log migration happens alongside their architectural changes. But a reviewer seeing `use tracing::debug` instead of `use log::debug` in the same commit that rewrites 2,000 lines of `ustreamer.rs` won't even notice — it's 4 lines out of 2,288. The migration-as-separate-commit is only valuable when the reviewer *can actually see it*, which means it only helps for files where the migration IS the whole change.

**Strategy B: Stash + clean-checkout for commit 0.** After Phase 2 unstages everything, stash all changes. On the clean tree (matching BASE_SHA), do a mechanical `sed` find-and-replace for `log → tracing` across all files, edit Cargo.tomls, stage, commit. Then `git stash pop` and resolve conflicts. This cleanly produces intermediate states without hunk surgery but adds a conflict-resolution step that requires judgment.

**Strategy C: Build forward instead of subtracting from final.** Don't use the "unstage everything" approach at all. Instead, start from BASE_SHA and apply changes incrementally: cherry-pick or manually construct each commit's content by referring to the final state as a reference. More manual work, but total control over intermediate states.

---

## Smaller observations

**Phase numbering gap.** The sequence goes 1, 2, 3, (Appendix A), 5, 6, 7, (Appendix B), 8. Phase 4 was moved to Appendix A but downstream phases weren't renumbered. Cosmetic, but an agent tracking phase numbers might stumble on the gap.

**Phase 5 is partially redundant with Phase 3.** Phase 3 gates each commit with `cargo check --workspace --all-targets`. Phase 5 re-runs the same check at each commit SHA in detached HEAD mode. The only scenario where Phase 5 catches something Phase 3 missed is if Phase 3's gate was skipped or repo state changed between phases. That's 6 full compile cycles for defensive redundancy. Consider making Phase 5's per-commit recheck optional and mandatory only for the final-tree identity check.

**Phase 6 runs both `cargo build` and `cargo check --workspace --all-targets`.** `cargo build` is a strict superset of `cargo check` — it does everything check does plus codegen. Running both is redundant. Drop `cargo check` from Phase 6.

**`endpoint.rs` may not need to be in the overlap list.** I examined the full diff: every changed line in `endpoint.rs` is removing log-related code (`use log::*`, `env_logger::try_init()`, `ENDPOINT_TAG` constants, `debug!()` call). If commit 0 handles all of this, `endpoint.rs` is fully finalized in commit 0 and shouldn't appear in the C0→C2 overlap list at line 56. Unless there are non-log changes I didn't find, it should be in the "fully finalizable" column, not the overlap column.

**Appendix A's checkboxes don't reflect repeated invocation.** The per-commit overlap flow (line 272) says "Run this flow immediately after each commit (c0..c5)" but uses `- [ ]` checkboxes that are binary. An agent would mark them done after the first run. Consider adding "(repeat for each commit)" or removing checkboxes from the per-invocation steps.

---

## Verdict

| Aspect | Status |
|--------|--------|
| 6-commit structure | Correct |
| Commit 0 workspace dep handling | Fixed from last round |
| Phase ordering (validate before publish) | Fixed from last round |
| Overlap exception list and sizing | Fixed from last round |
| Appendix A (overlap subroutine, not sequential phase) | Fixed from last round |
| **Workspace member timing for commits 4/5** | **Compile failure — needs explicit scoping** |
| **Staging strategy for commit 0 overlapping files** | **Unaddressed — recommend narrowing commit 0 scope** |
| Phase numbering gap | Cosmetic |
| Redundant Phase 5 / Phase 6 checks | Minor efficiency |

Fix the workspace member timing (a 5-line addition to the plan) and decide on a staging strategy for commit 0 (I recommend Strategy A — narrowing scope to fully-finalizable files only), and this plan is ready to execute.
