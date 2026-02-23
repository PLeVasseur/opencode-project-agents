# Paragraph-ID Dedup Mainline Run Summary

## Run metadata
- Worktree: `/home/pete.levasseur/project/fls-paragraph-id-dedup-mainline`
- Branch: `dedupe-paragraph-ids-mainline`
- HEAD: `0165ee6ad6e7e6a54705458d491810b0481b7df4`
- REPORT_ROOT: `/home/pete.levasseur/opencode-project-agents/fls/reports/paragraph-id-dedup-mainline-2026-02-07T014419Z`

## What changed
- Updated `src/glossary.rst` only:
  - `fls_t4yeovFm83Wo` -> `fls_kqdvWGi9cglm`
  - `fls_I9JaKZelMiby` -> `fls_H5vkbMFvzrFs`
- Kept canonical IDs unchanged in `src/types-and-traits.rst`.

## Duplicate evidence
- Before: `duplicate-ids-before.md` reports 2 duplicates (`fls_t4yeovFm83Wo`, `fls_I9JaKZelMiby`).
- After: `duplicate-ids-after.md` reports 0 duplicates.

## Validation results
- Build: `./make.py` exit `0` (`make.stdout.txt`).
- Changelog assistant check command was executed with explicit base ref (`f1b193f5197f48686bd56fe881633bb62fad7f27`) but exited `2` because `tools/changelog_assistant.py` is not present on this mainline branch (`changelog-check.stdout.txt`, `changelog-assistant-file-check.stdout.txt`).

## Commit and handoff
- Commit: `0165ee6ad6e7e6a54705458d491810b0481b7df4`
- Message: `fix(paragraph-ids): deduplicate reused glossary IDs`
- Cherry-pick onto system-abi worktree:
  - In `/home/pete.levasseur/project/fls-system-abi-variadic-validation` on `system-abi-variadic`:
  - `git cherry-pick 0165ee6ad6e7e6a54705458d491810b0481b7df4`

## Acceptance criteria
- PASS: Exactly the 2 known duplicate IDs were deduplicated.
- PASS: No duplicate `:dp:` IDs remain under `src/`.
- PASS: Build succeeded.
- PASS (documented exception): Changelog check could not run on this branch because the script is absent.
- PASS: Commit SHA is available for later cherry-pick/testing.
