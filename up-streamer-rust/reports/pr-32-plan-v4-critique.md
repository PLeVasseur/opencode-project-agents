# PR #32: Plan Critique (v4)

## Summary

The plan is in strong shape. The manifest mutation schedule fixes the workspace member timing. Strategy A is locked in. The worktree-based gates, Phase 4's conditional recheck, the fork-only publish guardrail, and the forward-build fallback escape hatch are all good additions. Phase ordering is correct (validate then publish).

One issue will cause Strategy A to produce a nearly empty commit. One will cause a wrong PR diff. Two are practical.

---

## Issue 1: The `example-streamer-uses/` files are NOT pure log migration

The plan assumes the ~12 `example-streamer-uses/src/bin/*.rs` files are "fully finalizable" in commit 0. I verified every one of them. Only `common/mod.rs` is pure. The other 11 have behavioral changes mixed in:

**Service/subscriber files** (`mqtt_service.rs`, `mqtt_subscriber.rs`, `someip_service.rs`, `someip_subscriber.rs`, `zenoh_service.rs`, `zenoh_subscriber.rs`) each add:
```rust
println!("READY listener_registered");
```
These are readiness markers consumed by the smoke suite's `READY_LISTENER_REGISTERED` constant.

**Client/publisher files** (`mqtt_client.rs`, `someip_client.rs`, `zenoh_client.rs`, `mqtt_publisher.rs`, `someip_publisher.rs`, `zenoh_publisher.rs`) each add ~15 lines: `send_count` and `send_interval_ms` CLI args, bounded loop logic, and interval timing. These are smoke suite infrastructure for deterministic test runs.

These are behavioral changes, not mechanical logging migration. Staging them with `git add` in commit 0 would violate the "no architectural behavior changes" guardrail (line 168).

**The actually pure files across the entire codebase are:**

| File | Changed lines | Nature |
|------|:------------:|--------|
| `example-streamer-uses/src/bin/common/mod.rs` | 2 | `use log::trace` → `use tracing::trace` |
| `utils/integration-test-utils/src/integration_test_listeners.rs` | 2 | `use log::debug` → `use tracing::debug` |
| `utils/integration-test-utils/src/up_client_failing_register.rs` | 2 | `use log::warn` → `use tracing::warn` |
| `up-streamer/src/endpoint.rs` | 12 | Remove `use log::*`, `env_logger::try_init()`, tag constants, debug call |

That's **4 files, ~18 lines**. Plus the workspace `Cargo.toml` addition of `tracing`/`tracing-subscriber` and one or two crate-level `Cargo.toml` dep additions. Commit 0 would be a ~25-line commit touching ~5-7 files.

**This doesn't break anything** — the commit is still valid and compilable — but it fundamentally changes the cost/benefit of having commit 0 as a separate commit. The plan should either:

**(a) Keep commit 0 but accurately scope it** at 4-7 files. Note that the workspace `tracing` dep addition is the most important part, not the `.rs` file migrations. Move `example-streamer-uses/` files to commit 2 (architectural rewire, since the behavioral changes are API/smoke-related) or commit 5 (smoke suite, since the READY markers are smoke infrastructure). Acknowledge in the commit body that commit 0 is small by design — it establishes the tracing dependency for all later commits.

**(b) Eliminate commit 0.** Fold the 4 pure `.rs` file changes into their owning commits (endpoint.rs → commit 2, integration-test-utils files → commit 3). Add the workspace `tracing`/`tracing-subscriber` dep in commit 1 (observability). This gives 5 commits. The log migration story becomes "each commit migrates its own files," which is simple and requires zero overlap exceptions.

Either way, the plan's current assumption that commit 0 contains ~15 fully-finalizable files needs to be corrected. The `example-streamer-uses/` files need an explicit home. Their natural destination is commit 2 (they're example programs being updated alongside the architecture) or commit 5 (the behavioral changes are smoke infrastructure). Given that the smoke suite in commit 5 builds these binaries and relies on the READY markers, commit 5 might be the cleanest fit — but only if the binaries don't need to compile at commit 2 for `cargo check --workspace` to pass.

---

## Issue 2: Fork `main` not verified against `upstream/main` before PR creation

Phase 1 sets `BASE_SHA = git rev-parse upstream/main` and builds the entire commit stack against that base. Phase 6 creates PR A against `$FORK_BASE_BRANCH` which is `"main"` on the fork (`origin/main`).

If the fork's `main` has drifted from `upstream/main` (common — forks don't auto-sync), the PR diff shown on GitHub will include commits that aren't part of this work. Worse, if the fork's `main` is *ahead* of `upstream/main`, the PR might show fewer changes than intended.

**Fix:** Add a sync check to Phase 6 before creating PRs:

```bash
# Verify fork main matches the base we built against
git fetch origin main
test "$(git rev-parse origin/main)" = "$BASE_SHA" \
  || { echo "Fork main differs from upstream/main. Sync fork first."; exit 1; }
```

Or, if the fork's `main` is reliably behind, force-update it:

```bash
git push origin "$BASE_SHA":refs/heads/main
```

---

## Issue 3: Worktree gates will be slow (practical)

The worktree approach (lines 147-151) is correct — it isolates `cargo check` from the dirty working tree. But each `git worktree add --detach` creates a fresh checkout with no `target/` directory. Every `cargo check --workspace --all-targets` will compile the full dependency tree from scratch.

For a project with `up-rust`, `protobuf`, `tokio`, `zenoh`, MQTT, and optional VSOMEIP C++ bindings, a cold `cargo check` is likely 2-5 minutes. Six commits × 2-5 minutes = 12-30 minutes just for Phase 3 gates, doing work that's mostly redundant (the dependency tree is identical across commits; only the crate code changes).

**Mitigation options (pick one):**
- **Share `target/` via `CARGO_TARGET_DIR`.** Set `CARGO_TARGET_DIR=/tmp/pr32-shared-target` before running gates. All worktrees share the build cache. Incremental compilation kicks in for inter-commit changes. Risk: concurrent worktrees could conflict if somehow run in parallel (they won't be here, so it's safe).
- **Accept the cost.** 12-30 minutes is a one-time tax. If correctness matters more than speed, just note the expected duration so the executor doesn't think it's stuck.
- **Skip worktrees for commits 4 and 5.** These commits add self-contained crates (`criterion-guardrail`, `transport-smoke-suite`) that can be validated with targeted `cargo check -p` / `cargo test -p` commands in the main worktree without interference from unstaged files (the unstaged files are in different crates). Only commits 0-3 need worktree isolation because they modify `up-streamer` crate files that also have unstaged changes in the working tree.

---

## Issue 4: Phase 5 still has redundant `cargo check`

Line 349: `cargo check --workspace --all-targets` appears alongside `cargo build` (line 346). `cargo build` is a strict superset — it does everything `cargo check` does plus codegen. Running both wastes a full compilation cycle. Drop line 349.

---

## Everything else looks good

The manifest mutation schedule (lines 126-138) is exactly what was needed — explicit per-commit scoping of workspace `Cargo.toml` and `up-streamer/Cargo.toml` changes, with negative guardrails ("do NOT add X in this commit"). This directly prevents the compile failure I flagged last round.

Strategy A with whole-file-only staging (line 171) is clean and the forward-build fallback (line 122) is a reasonable escape hatch. The per-invocation overlap checklist in Appendix A (lines 302-308) fixes the checkbox ambiguity. The fork-only publish guardrail (lines 385-391) prevents accidental upstream pushes. Phase 4's conditional recheck (lines 329-330) avoids redundant recompilation when Phase 3 logs are intact.

---

## Verdict

| Issue | Severity | Fix effort |
|-------|----------|-----------|
| `example-streamer-uses` files aren't pure — commit 0 scope is ~4 files, not ~15 | **Medium** — plan is built on a wrong assumption about commit 0's size | Update scope lists + decide where example-streamer-uses lands |
| Fork/upstream sync not verified | **Low-Medium** — will cause wrong PR diff if fork has drifted | 3-line check in Phase 6 |
| Worktree compilation speed | **Low** — correctness isn't affected, just wall time | Optional `CARGO_TARGET_DIR` hint |
| Redundant `cargo check` in Phase 5 | **Trivial** | Delete one line |

The plan is ready to execute after updating commit 0's scope to reflect the actual 4-file reality and adding the fork sync check. Everything else is solid.
