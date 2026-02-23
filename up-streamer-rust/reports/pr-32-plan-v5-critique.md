# PR #32: Plan Critique (v5)

## Summary

This plan is nearly execution-ready. Every issue from the last four rounds has been resolved — Strategy A is correctly scoped to 4 files, `example-streamer-uses/` behavioral changes are deferred to commit 5, the manifest mutation schedule is explicit with per-commit negative guardrails, the fork sync check is in Phase 6, and the workspace `log`/`env_logger`/`async-std` removal is properly sequenced across commits 3 and 5.

One compile blocker remains. One gap in the manifest schedule.

---

## Issue 1: Commit 2 deletes `subscription-cache` but commit 3 removes the dangling path dep (compile failure)

The manifest schedule (line 157-158) says:

> `utils/usubscription-static-file/Cargo.toml` mutation timing: **Commit 3**: remove `async-std`, remove `subscription-cache` dependency, and migrate logging dependencies.

But commit 2 deletes the `subscription-cache/` directory and removes `subscription-cache` from the workspace member list. After commit 2, `utils/usubscription-static-file/Cargo.toml` still contains:

```toml
subscription-cache = {path="../../subscription-cache"}
```

This path now points to a nonexistent directory. `cargo check --workspace` will fail at commit 2's gate.

This is the same class of issue that originally motivated collapsing commits 2-4: deleting `subscription-cache` has ripple effects on every crate that depends on it. The `up-streamer/Cargo.toml` dep was handled (it's in commit 2's scope), but the `usubscription-static-file/Cargo.toml` dep was assigned to commit 3 and slipped through.

**Fix:** Split `usubscription-static-file/Cargo.toml` across two commits in the manifest schedule:

```
- Commit 2: remove `subscription-cache` path dependency only.
- Commit 3: remove `async-std`, migrate `log` → `tracing`, add `[dev-dependencies]` tokio.
```

This is already allowed by the existing exception list (all `Cargo.toml` files are multi-touch wiring exceptions). The manifest schedule at line 157-158 just needs the split made explicit.

---

## Issue 2: Manifest schedule doesn't cover 3 crate `Cargo.toml` files

The schedule (lines 135-159) explicitly covers: root `Cargo.toml`, `up-streamer/Cargo.toml`, `example-streamer-uses/Cargo.toml`, `utils/integration-test-utils/Cargo.toml`, and `utils/usubscription-static-file/Cargo.toml`.

Three crate `Cargo.toml` files that also change are not listed:

| Crate `Cargo.toml` | Changes needed | Implicit commit |
|---------------------|---------------|-----------------|
| `configurable-streamer/Cargo.toml` | Remove `log`/`env_logger`, add `tracing`/`tracing-subscriber`, add tokio `signal` feature | Commit 2 |
| `example-streamer-implementations/Cargo.toml` | Remove `log`/`env_logger`, add `tracing`/`tracing-subscriber`, add tokio `signal` feature | Commit 2 |
| `up-linux-streamer-plugin/Cargo.toml` | Remove `env_logger`, add `tracing-subscriber` (already has `tracing`) | Commit 2 |

These are implicitly part of commit 2's scope ("entrypoint/plugin wiring files impacted by module/API rewire") and will work correctly. But the schedule's otherwise exhaustive per-crate style creates an expectation that all crate manifests are covered. An executor following the manifest schedule as a checklist would have no entry for these three files.

**Fix:** Add entries for these three under the manifest schedule, all assigned to Commit 2.

---

## Everything else checks out

I verified the following against the actual codebase:

**Commit 0 compiles.** After staging the 4 `.rs` files + 3 manifest changes, the committed tree has: `endpoint.rs` with log removed (no tracing needed — it just stops logging), `common/mod.rs` using `tracing::trace` (crate `Cargo.toml` has tracing), two `integration-test-utils` files using `tracing::debug`/`tracing::warn` (crate `Cargo.toml` has tracing). Old `ustreamer.rs` and other files remain at main state using `log`, which is still in their respective `Cargo.toml`s. Compiles.

**Commit 1 compiles.** Observability module has zero tracing macro calls — it only defines constants and helper functions using `up_rust` types. Adding `pub mod observability;` to `lib.rs` introduces no new dependency requirements. Compiles.

**`async-std` removal timing (commit 3) is correct.** Only `subscription-cache` (deleted in commit 2) and `usubscription-static-file` (updated in commit 3) use it. After commit 3 updates `usubscription-static-file/Cargo.toml`, no workspace member references `async-std`. Safe to remove from workspace.

**`log`/`env_logger` removal timing (commit 5) is correct.** After commits 0-3, the only remaining user of workspace `log` is `example-streamer-uses` (`log = { workspace = true }`). Other `env_logger` users (`example-streamer-uses`, `up-linux-streamer-plugin`) use non-workspace direct version deps, which don't need the workspace definition. Technically workspace `env_logger` could be removed as early as commit 3 (no remaining workspace-ref users), but keeping it until commit 5 is conservative and harmless. The plan is correct.

**PR C (commits 0-3 + 5, without commit 4) compiles.** Commit 4's additions (`criterion-guardrail`, `benchmark_support.rs`, bench wiring) are absent from PR C's branch, which is correct — commit 5 doesn't depend on any commit 4 artifacts. Workspace `Cargo.toml` on PR C's branch doesn't list `criterion-guardrail` as a member. `up-streamer/Cargo.toml` doesn't have bench wiring. `lib.rs` doesn't declare `pub mod benchmark_support;`. Clean.

**Fork sync check (Phase 6 lines 428-432) is correct.** Verifies `origin/$FORK_BASE_BRANCH` matches `BASE_SHA` before creating PRs. Catches drift.

**Shared `CARGO_TARGET_DIR` (line 168-170) is correct.** Sequential worktree gates share a build cache, avoiding 6 cold compiles.

---

## Verdict

| Issue | Severity | Fix |
|-------|----------|-----|
| `usubscription-static-file/Cargo.toml` subscription-cache dep must be removed in commit 2, not commit 3 | **Compile failure** | Split the manifest schedule entry: commit 2 removes subscription-cache dep, commit 3 does the rest |
| 3 crate `Cargo.toml` files missing from manifest schedule | **Completeness gap** | Add entries for configurable-streamer, example-streamer-implementations, up-linux-streamer-plugin under commit 2 |

Both are small edits to the manifest schedule section. After those, the plan is ready to execute.
