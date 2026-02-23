# Glossary single-source phase1 commit4 CI format remediation plan (2026-02-14)

Date: 2026-02-14

## Objective

- [ ] Fix the CI failure on `glossary-single-source-phase1-repack-upstream-main` caused by Python formatting/lint in commit4.
  - [ ] `uvx black . --check --diff --color` passes.
  - [ ] `uvx flake8 . --exclude .venv` passes.
  - [ ] `./tools/verify-html-diff.py --mode repro --ref HEAD` still passes.
- [ ] Keep strict topology: exactly 4 commits over `UPSTREAM_MAIN_PIN`.
- [ ] Rewrite commit4 only; keep commit1-3 SHAs unchanged.

## Hard constraints

- [ ] Do not push to `upstream`.
- [ ] Push only to `origin/glossary-single-source-phase1-repack-upstream-main`.
- [ ] Use explicit lease on force push.
- [ ] Keep all artifacts under `$OPENCODE_CONFIG_DIR/reports/`.

## Canonical inputs (must match before editing)

- [ ] `REPO_ROOT=/home/pete.levasseur/project/fls`
- [ ] `REPACK_BRANCH=glossary-single-source-phase1-repack-upstream-main`
- [ ] `UPSTREAM_MAIN_PIN=fb8a46795eda1f1db5e3232002fd94a270bfbffd`
- [ ] `COMMIT1_SHA=06da2fde57a1b195325e91fa322614ce1bbe2d04`
- [ ] `COMMIT2_SHA=85a60b64f816b284a3191dfc730b9e5d8ac49030`
- [ ] `COMMIT3_SHA=6716db3a49cfbffa30ccac3a51cf76ebd9ab60a7`
- [ ] `OLD_COMMIT4_SHA=1132eb4c632c0d1b65bc7000d9bced2fca3842bd`
- [ ] If any value differs, stop and update this plan first.

## New-session bootstrap contract

- [ ] Validate environment and repo context:
  - [ ] `test -n "$OPENCODE_CONFIG_DIR"`
  - [ ] `test "$(git rev-parse --show-toplevel)" = "$REPO_ROOT"`
  - [ ] `test -f "$REPO_ROOT/make.py"`
  - [ ] `test -f "$REPO_ROOT/tools/verify-html-diff.py"`
- [ ] Validate branch context:
  - [ ] `git fetch origin --prune`
  - [ ] Switch to `$REPACK_BRANCH` (create local tracking branch if missing).
  - [ ] `test "$(git rev-parse --abbrev-ref HEAD)" = "$REPACK_BRANCH"`
  - [ ] `test -z "$(git status --porcelain)"`
- [ ] Validate topology baseline:
  - [ ] `test "$(git rev-list --count $UPSTREAM_MAIN_PIN..HEAD)" = "4"`
  - [ ] `git rev-list --reverse --format=%H $UPSTREAM_MAIN_PIN..HEAD` resolves exactly to `COMMIT1_SHA`, `COMMIT2_SHA`, `COMMIT3_SHA`, `OLD_COMMIT4_SHA`.

## Run-state contract (fresh or resume)

- [ ] New run or resume selection:
  - [ ] `RUN_ID=${REMEDIATION_RUN_ID:-$(date -u +%Y%m%dT%H%M%SZ)}`
  - [ ] `RUN_ROOT=$OPENCODE_CONFIG_DIR/reports/commit4-ci-format-remediation-$RUN_ID`
  - [ ] `RUN_STATE_FILE=$RUN_ROOT/remediation.state.env`
  - [ ] `RUN_LOG=$RUN_ROOT/remediation.log`
  - [ ] `RUN_ARTIFACT_ROOT=$RUN_ROOT/artifacts`
- [ ] If `RUN_STATE_FILE` exists, resume from `CURRENT_STAGE`.
- [ ] If `RUN_STATE_FILE` does not exist, initialize stage flags to `0` and `CURRENT_STAGE=C0`.
- [ ] State updates must be atomic (`*.tmp` + rename).

## Stage C0 - capture failing signal

- [ ] Record CI failure context:
  - [ ] Capture latest failing run URL for `$REPACK_BRANCH`.
  - [ ] Capture failed job/step name and failed command.
  - [ ] Save failed-step log excerpt to `$RUN_ARTIFACT_ROOT/ci-failure.log`.
- [ ] Persist state:
  - [ ] `C0_DONE=1`

## Stage C1 - implement commit4-only fix

- [ ] Limit source edits to `tools/verify-html-diff.py`.
- [ ] Apply formatting-first remediation:
  - [ ] Run `uvx black tools/verify-html-diff.py`.
  - [ ] If needed, manually wrap any remaining `E501` lines without changing behavior.
- [ ] Save source diff artifact:
  - [ ] `git diff -- tools/verify-html-diff.py > $RUN_ARTIFACT_ROOT/commit4-format-fix.patch`
- [ ] Persist state:
  - [ ] `C1_DONE=1`

## Stage C2 - local verification gates

- [ ] `uvx black . --check --diff --color`
- [ ] `uvx flake8 . --exclude .venv`
- [ ] `./tools/verify-html-diff.py --mode repro --ref HEAD --report "$RUN_ARTIFACT_ROOT/local-repro-head.txt"`
- [ ] Validate all three commands exit `0`.
- [ ] Persist state:
  - [ ] `C2_DONE=1`

## Stage C3 - rewrite capstone only

- [ ] Rebuild commit4 from commit3 baseline:
  - [ ] Create temporary branch at `COMMIT3_SHA`.
  - [ ] Cherry-pick old commit4 with `--no-commit`.
  - [ ] Keep only intended commit4 path set; include fixed `tools/verify-html-diff.py`.
  - [ ] Commit with same subject: `refactor(glossary): switch to generated-only glossary source and reproducibility checks`.
  - [ ] Capture `NEW_COMMIT4_SHA`.
- [ ] Move `$REPACK_BRANCH` to rebuilt 4-commit tip.
- [ ] Validate topology:
  - [ ] `git rev-list --count $UPSTREAM_MAIN_PIN..HEAD` is `4`.
  - [ ] First three SHAs are unchanged (`COMMIT1_SHA`, `COMMIT2_SHA`, `COMMIT3_SHA`).
- [ ] Persist state:
  - [ ] `NEW_COMMIT4_SHA` recorded.
  - [ ] `C3_DONE=1`

## Stage C4 - pre-push verification on new capstone

- [ ] Re-run:
  - [ ] `uvx black . --check --diff --color`
  - [ ] `uvx flake8 . --exclude .venv`
  - [ ] `./tools/verify-html-diff.py --mode repro --ref $NEW_COMMIT4_SHA --report "$RUN_ARTIFACT_ROOT/repro-new-commit4.txt"`
- [ ] All return code `0`.
- [ ] Persist state:
  - [ ] `C4_DONE=1`

## Stage C5 - safe push and CI confirmation

- [ ] Determine expected remote SHA before push:
  - [ ] `OLD_REMOTE_SHA=$(git rev-parse origin/$REPACK_BRANCH)`
- [ ] Push with explicit lease:
  - [ ] `git push --force-with-lease=refs/heads/$REPACK_BRANCH:$OLD_REMOTE_SHA origin HEAD:refs/heads/$REPACK_BRANCH`
- [ ] Confirm remote tip equals `NEW_COMMIT4_SHA`.
- [ ] Confirm CI run on `NEW_COMMIT4_SHA` completes successfully:
  - [ ] `Build the documentation` success.
  - [ ] `Verify Python code formatting` success.
  - [ ] `Lint Python code with flake8` success.
- [ ] Save CI run metadata to `$RUN_ARTIFACT_ROOT/ci-success.json`.
- [ ] Persist state:
  - [ ] `C5_DONE=1`

## Stage C6 - closeout

- [ ] Append final summary to `$RUN_LOG`:
  - [ ] old/new commit4 SHA pair.
  - [ ] CI run URL and conclusion.
  - [ ] confirmation that commit1-3 were unchanged.
- [ ] Write summary report:
  - [ ] `$RUN_ROOT/summary.md`
- [ ] Persist completion:
  - [ ] `C6_DONE=1`
  - [ ] `CURRENT_STAGE=COMPLETE`

## Mandatory stop conditions

- [ ] Stop if working tree is dirty before Stage C1.
- [ ] Stop if any stage command returns non-zero unless explicitly handled by the stage.
- [ ] Stop if commit count over `UPSTREAM_MAIN_PIN` is not exactly `4`.
- [ ] Stop if commit1-3 SHAs change at any point.
- [ ] Stop if push lease cannot be proven against `OLD_REMOTE_SHA`.
- [ ] Stop if CI formatting or flake8 checks fail after push.
