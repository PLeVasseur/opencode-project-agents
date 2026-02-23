# Glossary Single-Source Phase1 Upstream Main Four-Commit Relayer + Generated-Only Capstone Plan

Date: 2026-02-14

## Objective
- [ ] Re-layer `glossary-single-source-phase1` on top of `upstream/main` into four logical commits.
  - [ ] `tooling-core`
  - [ ] `migration`
  - [ ] `ci-verification`
  - [ ] `capstone-generated-only`
- [ ] Remove duplicate glossary source-of-truth in the capstone commit.
  - [ ] Keep generated glossary as the only glossary content source used for HTML.
- [ ] Preserve confidence via explicit integrity chain evidence.
  - [ ] Prove no effective rendered-output differences under documented comparison policy.

## Hard Boundaries
- [ ] First mutating action is syncing `origin/main` from pinned `upstream/main`.
  - [ ] Fast-forward only; never force-push `main`.
- [ ] All rewrite operations use immutable `UPSTREAM_MAIN_PIN`.
  - [ ] Do not use moving refs after pin capture.
- [ ] Stop after pushing repack branch and validating reviewability.
  - [ ] Do not replace `glossary-single-source-phase1` in this run.
- [ ] Store all temporary and report artifacts under `$OPENCODE_CONFIG_DIR/reports/`.
  - [ ] Do not place report artifacts in repo paths.

## Fresh Session Bootstrap (Mandatory)
- [ ] Environment sanity.
  - [ ] `printenv OPENCODE_CONFIG_DIR` is non-empty.
  - [ ] `test -d "$OPENCODE_CONFIG_DIR/plans"`
  - [ ] `test -d "$OPENCODE_CONFIG_DIR/reports" || mkdir -p "$OPENCODE_CONFIG_DIR/reports"`
- [ ] Toolchain availability.
  - [ ] `command -v git`
  - [ ] `command -v uv`
  - [ ] `command -v python3`
  - [ ] `command -v sphinx-build`
  - [ ] `command -v gh`
- [ ] Dependency bootstrap.
  - [ ] `uv sync --frozen`
  - [ ] If it fails, stop and remediate before proceeding.
- [ ] Repository safety checks.
  - [ ] `git status --porcelain=v1` is empty.
  - [ ] No in-progress rebase/cherry-pick/merge.

## Comparison Policy (Bit-for-Bit Where It Makes Sense)
- [ ] Scope of comparison for integrity proofs: rendered output tree (`build/html/**`).
- [ ] Default comparator: strict byte-for-byte file comparison.
- [ ] Exceptions (documented and explicit):
  - [ ] `paragraph-ids.json`: compare normalized logical content (sorted structure), not raw byte order.
  - [ ] `.buildinfo`: require matching `config`; ignore `tags` differences.
- [ ] Link checking is excluded from bit-for-bit proofs.
  - [ ] Network variability is out-of-scope for reproducibility/equivalence checks.
- [ ] Every no-diff claim must explicitly say: "no differences under configured comparison policy."

## Verifier Tooling Contract (To Implement by Capstone)
- [ ] Extend `tools/verify-html-diff.py` with explicit modes.
  - [ ] `--mode export-ref --ref <sha> --output-dir <dir>`
    - [ ] Builds target ref in isolated worktree and exports `build/html/` to `<dir>`.
    - [ ] Writes `<dir>/manifest.sha256` (sorted file checksums).
  - [ ] `--mode compare-dirs --left-dir <dir> --right-dir <dir> --report <path>`
    - [ ] Compares exported HTML directories using the configured policy.
    - [ ] Writes structured report at `<path>`.
  - [ ] `--mode refs --left-ref <sha> --right-ref <sha> --report <path>`
    - [ ] Builds both refs and compares them using the same policy.
  - [ ] `--mode repro --ref <sha> --report <path>`
    - [ ] Builds same ref twice and compares using the same policy.
- [ ] Define exit codes.
  - [ ] `0`: success, no differences under policy.
  - [ ] `1`: differences found.
  - [ ] `2`: operational/tooling failure.
- [ ] Ensure deterministic report locations and filenames.
  - [ ] Default report root under `$OPENCODE_CONFIG_DIR/reports/`.

## Crash-Resilient State Model
- [ ] Human report file.
  - [ ] `REPORT_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214.md`
- [ ] Machine state file.
  - [ ] `STATE_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214.state.env`
- [ ] Single-writer lock file.
  - [ ] `STATE_LOCK_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214.state.lock`
  - [ ] If lock exists and PID is alive, stop (concurrent session guard).
  - [ ] If lock exists and PID is stale, record cleanup and recreate lock.
- [ ] Persisted state variables.
  - [ ] `START_BRANCH`
  - [ ] `ORIG_HEAD`
  - [ ] `ORIG_TREE`
  - [ ] `UPSTREAM_MAIN_PIN`
  - [ ] `ORIGIN_MAIN_BEFORE`
  - [ ] `ORIGIN_MAIN_AFTER`
  - [ ] `BACKUP_BRANCH=backup/glossary-single-source-phase1-20260214`
  - [ ] `BACKUP_TAG=backup-glossary-single-source-phase1-20260214`
  - [ ] `REBASED_HEAD`
  - [ ] `REBASED_TREE`
  - [ ] `REPACK_BRANCH=glossary-single-source-phase1-repack-upstream-main`
  - [ ] `COMMIT1_SHA`
  - [ ] `COMMIT2_SHA`
  - [ ] `COMMIT3_SHA`
  - [ ] `COMMIT4_SHA`
  - [ ] `REPACK_REMOTE_SHA`
  - [ ] `ARTIFACT_ROOT`
  - [ ] `INTEGRITY_CHAIN_REPORT`
  - [ ] `PHASE_*` completion flags

## Artifact and Report Deliverables (Required)
- [ ] Artifact root.
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214-artifacts/`
- [ ] HTML artifacts.
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214-artifacts/html-upstream-main/`
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214-artifacts/html-commit3/`
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214-artifacts/html-commit4/`
- [ ] Manifests.
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214-artifacts/html-upstream-main/manifest.sha256`
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214-artifacts/html-commit3/manifest.sha256`
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214-artifacts/html-commit4/manifest.sha256`
- [ ] Pairwise policy-diff reports.
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214-artifacts/diff-upstream-main-vs-commit3.txt`
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214-artifacts/diff-commit3-vs-commit4.txt`
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214-artifacts/diff-upstream-main-vs-commit4.txt`
- [ ] Integrity summary report.
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214-integrity-chain.md`
  - [ ] Must state all three pairwise diffs show no differences under configured policy.

## Phase 0 - Start/Resume Control
- [ ] Acquire/reacquire lock.
  - [ ] Validate `STATE_LOCK_FILE` ownership semantics (single active writer).
- [ ] Load `STATE_FILE` if present.
  - [ ] Reject malformed values.
  - [ ] If malformed, stop and recover from backup refs.
- [ ] Resume invariants.
  - [ ] If `ORIG_HEAD` exists in state, verify it is reachable.
  - [ ] If `UPSTREAM_MAIN_PIN` exists in state, ensure current `upstream/main` has not changed from pin; if changed, stop and restart from Phase 1 with new run.
  - [ ] If a phase flag is set, verify phase invariants before skipping.
- [ ] Establish deterministic local env for proof phases.
  - [ ] Use `TZ=UTC`.
  - [ ] Use `LANG=C.UTF-8` and `LC_ALL=C.UTF-8`.
  - [ ] Use `PYTHONHASHSEED=0`.
  - [ ] Use `umask 022`.

## Phase 1 - Mandatory First Mutating Step: Sync Fork Main
- [ ] Verify remotes and upstream identity.
  - [ ] `git remote -v`
  - [ ] If missing: `git remote add upstream git@github.com:rust-lang/fls.git`
  - [ ] Confirm upstream URL is exactly `git@github.com:rust-lang/fls.git`.
- [ ] Fetch refs.
  - [ ] `git fetch --prune upstream`
  - [ ] `git fetch --prune origin`
- [ ] Pin base and capture pre-state.
  - [ ] `UPSTREAM_MAIN_PIN=$(git rev-parse upstream/main)`
  - [ ] `ORIGIN_MAIN_BEFORE=$(git rev-parse origin/main)`
- [ ] Enforce fast-forward safety.
  - [ ] `git merge-base --is-ancestor "$ORIGIN_MAIN_BEFORE" "$UPSTREAM_MAIN_PIN"`
  - [ ] On failure, stop (do not force-push `origin/main`).
- [ ] Sync origin main to pinned upstream main.
  - [ ] `git push origin "$UPSTREAM_MAIN_PIN":refs/heads/main`
- [ ] Verify and persist checkpoint.
  - [ ] `git fetch origin main`
  - [ ] `ORIGIN_MAIN_AFTER=$(git rev-parse origin/main)`
  - [ ] Confirm `"$ORIGIN_MAIN_AFTER" == "$UPSTREAM_MAIN_PIN"`.
  - [ ] Persist `PHASE_1_SYNC_DONE=1`.

## Phase 2 - Capture Source Baseline and Create Backups
- [ ] Capture source pointers.
  - [ ] `START_BRANCH=$(git branch --show-current)`
  - [ ] `ORIG_HEAD=$(git rev-parse HEAD)`
  - [ ] `ORIG_TREE=$(git rev-parse HEAD^{tree})`
- [ ] Create or verify backup refs.
  - [ ] Branch `BACKUP_BRANCH` at `ORIG_HEAD`.
  - [ ] Tag `BACKUP_TAG` at `ORIG_HEAD`.
  - [ ] If either exists at different target, stop.
- [ ] Push and verify backup refs on origin.
  - [ ] Push backup branch.
  - [ ] Push backup tag.
  - [ ] Confirm both refs exist remotely.
- [ ] Persist `PHASE_2_BACKUP_DONE=1`.

## Phase 3 - Rebase Existing Work Onto Pinned Upstream
- [ ] Create/reuse disposable integration branch.
  - [ ] `glossary-single-source-phase1-upstream-rebase`
  - [ ] Verify expected ancestry before reuse.
- [ ] Rebase onto `UPSTREAM_MAIN_PIN`.
  - [ ] `git rebase "$UPSTREAM_MAIN_PIN"`
  - [ ] Resolve conflicts with minimal intentional edits only.
- [ ] Post-conflict integrity checks (if applicable).
  - [ ] `git diff --check`
  - [ ] `./make.py`
- [ ] Capture rebased pointers.
  - [ ] `REBASED_HEAD=$(git rev-parse HEAD)`
  - [ ] `REBASED_TREE=$(git rev-parse HEAD^{tree})`
- [ ] Persist `PHASE_3_REBASE_DONE=1`.

## Phase 4 - Flatten Delta on Repack Branch
- [ ] Create/reuse repack branch from `REBASED_HEAD`.
  - [ ] `REPACK_BRANCH=glossary-single-source-phase1-repack-upstream-main`
- [ ] Flatten against pinned base.
  - [ ] `git reset --soft "$UPSTREAM_MAIN_PIN"`
  - [ ] `git restore --staged .`
- [ ] Verify expected unstaged delta exists.
  - [ ] `git status --short`
  - [ ] `git diff --name-only`
- [ ] Persist `PHASE_4_FLATTEN_DONE=1`.

## Phase 5 - Commit 1: `tooling-core`
- [ ] Stage only tooling/core files.
  - [ ] `README.rst`
  - [ ] `exts/ferrocene_spec/README.rst`
  - [ ] `exts/ferrocene_spec/__init__.py`
  - [ ] `exts/ferrocene_spec/glossary.py`
  - [ ] `generate-glossary.py`
  - [ ] `generate-glossary-entry.py`
  - [ ] `make.py`
  - [ ] `src/glossary.prelude.rst.inc`
- [ ] Verify staged set exactly matches checklist.
- [ ] Commit.
  - [ ] Suggested message: `feat(glossary): add single-source glossary tooling core`
- [ ] Trust gate.
  - [ ] `git show --name-only --format=fuller HEAD`
  - [ ] `./make.py`
- [ ] Persist `COMMIT1_SHA` and `PHASE_5_COMMIT1_DONE=1`.

## Phase 6 - Commit 2: `migration`
- [ ] Stage only migration/content files.
  - [ ] `src/glossary.rst`
  - [ ] `src/glossary.rst.inc`
  - [ ] `src/associated-items.rst`
  - [ ] `src/attributes.rst`
  - [ ] `src/concurrency.rst`
  - [ ] `src/entities-and-resolution.rst`
  - [ ] `src/exceptions-and-errors.rst`
  - [ ] `src/expressions.rst`
  - [ ] `src/ffi.rst`
  - [ ] `src/functions.rst`
  - [ ] `src/general.rst`
  - [ ] `src/generics.rst`
  - [ ] `src/implementations.rst`
  - [ ] `src/inline-assembly.rst`
  - [ ] `src/items.rst`
  - [ ] `src/lexical-elements.rst`
  - [ ] `src/macros.rst`
  - [ ] `src/ownership-and-deconstruction.rst`
  - [ ] `src/patterns.rst`
  - [ ] `src/program-structure-and-compilation.rst`
  - [ ] `src/statements.rst`
  - [ ] `src/types-and-traits.rst`
  - [ ] `src/undefined-behavior.rst`
  - [ ] `src/unsafety.rst`
  - [ ] `src/values.rst`
- [ ] Verify staged set exactly matches checklist.
- [ ] Commit.
  - [ ] Suggested message: `docs(glossary): migrate glossary content to single-source entries`
- [ ] Trust gate.
  - [ ] `git show --name-only --format=fuller HEAD`
  - [ ] `./make.py`
- [ ] Persist `COMMIT2_SHA` and `PHASE_6_COMMIT2_DONE=1`.

## Phase 7 - Commit 3: `ci-verification` (Transitional)
- [ ] Stage transitional verification files.
  - [ ] `.github/workflows/ci.yml`
  - [ ] `tools/verify-html-diff.py`
  - [ ] `tools/README.rst`
- [ ] Keep transitional behavior explicit.
  - [ ] Continue static-vs-generated parity while static include still exists.
  - [ ] Ensure report output is deterministic and actionable.
- [ ] Verify staged set exactly matches checklist.
- [ ] Commit.
  - [ ] Suggested message: `ci(glossary): add transitional html parity verification`
- [ ] Trust gate.
  - [ ] `git show --name-only --format=fuller HEAD`
  - [ ] `./tools/verify-html-diff.py`
- [ ] Persist `COMMIT3_SHA` and `PHASE_7_COMMIT3_DONE=1`.

## Phase 8 - Commit 4: `capstone-generated-only`
- [ ] Remove duplicate source of truth.
  - [ ] Delete `src/glossary.rst.inc`.
  - [ ] Update `src/glossary.rst` to include generated glossary only.
  - [ ] Remove tag-based static/generated include switching from glossary page.
- [ ] Make build path generated-only.
  - [ ] Ensure `generate-glossary.py` writes bootstrap prelude before env build unconditionally.
  - [ ] Remove obsolete static-sync and obsolete flags from `make.py`.
  - [ ] Keep generation-before-build behavior in normal and serve paths.
- [ ] Update tooling defaults impacted by static-file removal.
  - [ ] Update `generate-glossary-entry.py` default source behavior and error messages.
- [ ] Implement verifier contract from this plan.
  - [ ] Add `export-ref`, `compare-dirs`, `refs`, and `repro` modes.
  - [ ] Ensure comparison policy exceptions are centralized and documented.
  - [ ] Ensure report defaults write to `$OPENCODE_CONFIG_DIR/reports/`.
- [ ] Update CI for generated-only immediate reflection.
  - [ ] Remove static-file parity step.
  - [ ] Add step: `rm -f build/generated.glossary.rst` before build verification.
  - [ ] Add step: run `./make.py --clear` and assert `build/generated.glossary.rst` exists after build.
  - [ ] Add reproducibility gate via verifier `repro` mode.
- [ ] Update docs to generated-only workflow.
  - [ ] `README.rst`
  - [ ] `tools/README.rst`
  - [ ] `exts/ferrocene_spec/README.rst`
- [ ] Verify staged set exactly matches intended capstone scope.
- [ ] Commit.
  - [ ] Suggested message: `refactor(glossary): switch to generated-only glossary source and reproducibility checks`
- [ ] Trust gate.
  - [ ] `./make.py --clear`
  - [ ] `./tools/verify-html-diff.py --mode repro --ref HEAD --report "$OPENCODE_CONFIG_DIR/reports/capstone-repro-head.txt"`
- [ ] Persist `COMMIT4_SHA` and `PHASE_8_COMMIT4_DONE=1`.

## Phase 9 - Integrity Chain Proof and Deliverable Generation
- [ ] Verify ancestry and commit count.
  - [ ] `git rev-list --count "$UPSTREAM_MAIN_PIN"..HEAD` is `4`.
  - [ ] `git log --oneline --decorate "$UPSTREAM_MAIN_PIN"..HEAD`
- [ ] Configure artifact variables and create root.
  - [ ] `ARTIFACT_ROOT=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214-artifacts`
  - [ ] `mkdir -p "$ARTIFACT_ROOT"`
- [ ] Export three HTML artifact folders.
  - [ ] Export `UPSTREAM_MAIN_PIN` to `html-upstream-main`.
  - [ ] Export `COMMIT3_SHA` to `html-commit3`.
  - [ ] Export `COMMIT4_SHA` to `html-commit4`.
  - [ ] Confirm `index.html` exists in all three outputs.
  - [ ] Confirm `glossary.html` exists in all three outputs.
- [ ] Run pairwise policy-diff comparisons and save reports.
  - [ ] `html-upstream-main` vs `html-commit3` -> `diff-upstream-main-vs-commit3.txt`
  - [ ] `html-commit3` vs `html-commit4` -> `diff-commit3-vs-commit4.txt`
  - [ ] `html-upstream-main` vs `html-commit4` -> `diff-upstream-main-vs-commit4.txt`
  - [ ] All three reports must show no differences under policy.
- [ ] Run reproducibility proof for capstone ref.
  - [ ] `./tools/verify-html-diff.py --mode repro --ref "$COMMIT4_SHA" --report "$OPENCODE_CONFIG_DIR/reports/capstone-repro-commit4.txt"`
  - [ ] Report must show no differences under policy.
- [ ] Write top-level integrity summary report.
  - [ ] Path: `$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214-integrity-chain.md`
  - [ ] Include SHA mapping: `UPSTREAM_MAIN_PIN`, `COMMIT3_SHA`, `COMMIT4_SHA`.
  - [ ] Include artifact directories and manifest paths.
  - [ ] Include all pairwise diff report paths.
  - [ ] Include explicit statement that all pairwise comparisons had no differences under configured policy.
- [ ] Persist `PHASE_9_VERIFY_DONE=1`.

## Phase 10 - Push Repack Branch, Validate Reviewability, Then STOP
- [ ] Push repack branch to fork.
  - [ ] `git push -u origin "$REPACK_BRANCH"`
  - [ ] If rerun and branch exists, use explicit lease protection.
- [ ] Record remote SHA.
  - [ ] `REPACK_REMOTE_SHA=$(git ls-remote --heads origin "$REPACK_BRANCH" | awk '{print $1}')`
- [ ] Validate compare/PR reviewability.
  - [ ] Exactly 4 commits visible.
  - [ ] Scopes map to `tooling-core`, `migration`, `ci-verification`, `capstone-generated-only`.
- [ ] Persist `PHASE_10_STOP_POINT_DONE=1`.
- [ ] STOP for manual review.
  - [ ] Do not replace `glossary-single-source-phase1` in this session.

## Deferred Phase (Only After Manual Approval)
- [ ] Replace original branch with explicit lease.
  - [ ] `OLD_REMOTE_SHA=$(git ls-remote --heads origin glossary-single-source-phase1 | awk '{print $1}')`
  - [ ] `git push --force-with-lease=refs/heads/glossary-single-source-phase1:$OLD_REMOTE_SHA origin "$REPACK_BRANCH":refs/heads/glossary-single-source-phase1`
- [ ] Verify replacement SHA.
  - [ ] `git ls-remote --heads origin glossary-single-source-phase1`

## Crash Recovery Playbook
- [ ] On restart, run bootstrap + Phase 0 first.
  - [ ] Reacquire lock safely.
  - [ ] Load and validate state.
  - [ ] Verify phase invariants before resume.
- [ ] If invariant mismatch is detected.
  - [ ] Stop immediately.
  - [ ] Roll back to backup refs.
  - [ ] Start fresh run with new state/report files.

## Rollback Plan
- [ ] Roll back branch from backup branch ref.
  - [ ] `git push --force-with-lease origin refs/heads/$BACKUP_BRANCH:refs/heads/glossary-single-source-phase1`
- [ ] Or roll back from backup tag ref.
  - [ ] `git push --force-with-lease origin refs/tags/$BACKUP_TAG:refs/heads/glossary-single-source-phase1`
- [ ] Re-run integrity checks after rollback.
  - [ ] Build validation.
  - [ ] Reproducibility validation.
  - [ ] Pairwise artifact policy-diff validation.

## Done Criteria
- [ ] `origin/main` sync from pinned `upstream/main` completed as first mutating action.
- [ ] Four-commit series complete on pinned base.
- [ ] Capstone commit removes duplicate glossary source file and enables generated-only flow.
- [ ] CI/build enforce immediate reflection of glossary directive changes into generated glossary HTML.
- [ ] Three HTML artifact folders and three pairwise diff reports are produced under `$OPENCODE_CONFIG_DIR/reports/`.
- [ ] Integrity summary report states no differences under configured policy.
- [ ] Repack branch pushed and reviewability validated.
- [ ] Execution stops before original branch replacement.
