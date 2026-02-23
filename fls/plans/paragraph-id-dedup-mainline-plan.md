# Plan: Simple Mainline Paragraph-ID Dedup (Separate PR)

## Goal
- [x] Create one focused commit from `origin/main` that removes the two known duplicate `:dp:` IDs.
- [x] Keep that commit ready to cherry-pick onto `system-abi-variadic` for later validation.

## Duplicates to fix
- [x] `fls_t4yeovFm83Wo`
  - [x] Keep `src/types-and-traits.rst` as canonical.
  - [x] Re-ID `src/glossary.rst` occurrence.
- [x] `fls_I9JaKZelMiby`
  - [x] Keep `src/types-and-traits.rst` as canonical.
  - [x] Re-ID `src/glossary.rst` occurrence.

## Quick execution checklist

### 1) Bootstrap
- [x] `printenv OPENCODE_CONFIG_DIR`
- [x] `git fetch origin`
- [x] Work from a clean branch based on `origin/main` (new worktree is fine).

### 2) Report root
- [x] `REPORT_ROOT="$OPENCODE_CONFIG_DIR/reports/paragraph-id-dedup-mainline-<timestamp>"`
- [x] `mkdir -p "$REPORT_ROOT"`
- [x] Initialize `command-exit-codes.tsv`.

### 3) Minimal fix
- [x] Run `./generate-random-ids.py` and pick 2 fresh IDs.
- [x] Replace the 2 duplicate glossary IDs only.
- [x] Save before/after duplicate inventory artifacts.

### 4) Verify
- [x] Verify no duplicate `:dp:` IDs remain in `src/`.
- [x] Run `./make.py` and capture output.
- [x] Run changelog assistant check with base ref from `git merge-base HEAD origin/main`.

### 5) Commit + handoff
- [x] Commit only dedup changes (Conventional Commit).
- [x] Record commit SHA.
- [x] Record cherry-pick command for `/home/pete.levasseur/project/fls-system-abi-variadic-validation` (`system-abi-variadic`).

## Final report (`$REPORT_ROOT/summary.md`)
- [x] Include command exits.
- [x] Include duplicate evidence before/after.
- [x] Include build/check results.
- [x] Include commit SHA and cherry-pick command.

## Acceptance criteria
- [x] Exactly the 2 known duplicate IDs are deduplicated.
- [x] No duplicate `:dp:` IDs remain under `src/`.
- [x] Build/check pass (or failures are unrelated and documented).
- [x] Commit SHA is available for later cherry-pick/testing.
