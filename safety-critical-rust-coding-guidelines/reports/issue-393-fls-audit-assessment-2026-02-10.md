# Issue #393 FLS Audit Assessment (2026-02-10)

## Scope

- Issue: https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/393
- Goal: determine whether guideline content changes are required, or whether only `src/spec.lock` needs updating.

## Commands Run

- `uv run python scripts/fls_audit.py`
- `uv run python scripts/fls_audit.py --print-diffs`
- `gh issue view 393 --repo rustfoundation/safety-critical-rust-coding-guidelines --json ...`

## Evidence

### Local audit report (current run)

- Report: `build/fls_audit/report.md`
- JSON: `build/fls_audit/report.json`
- Baseline commit: `eaafc97e1db8f4a3d153db1abe96ececacf1be2c`
- Current commit: `e66c7ade08cc89a6e76a59517e51c3798200e56f`

Summary counts:

- Added IDs: 2
- Removed IDs: 0
- Content changed: 3
- Renumbered only: 8
- Header changes: 0
- Section reorders: 0
- Guidelines affected: 0

Changed content observed:

- `fls_8m7pc3riokst`: ABI text for `extern "system"` expanded with platform-specific details.
- `fls_I9JaKZelMiby`: glossary sentence moved out of `Types and Traits` location.
- `fls_t4yeovFm83Wo`: glossary sentence moved out of `Types and Traits` location.

Added IDs observed:

- `fls_H5vkbMFvzrFs` (`local trait`) in glossary.
- `fls_kqdvWGi9cglm` (`discriminant type`) in glossary.

### Cross-check against issue #393

Issue #393 was generated from an earlier FLS current commit:

- Issue #393 current commit: `f1b193f5197f48686bd56fe881633bb62fad7f27`
- Local rerun current commit: `e66c7ade08cc89a6e76a59517e51c3798200e56f`

Even with newer upstream FLS content in the local rerun:

- `Guidelines affected` remains `0`.
- No guideline IDs are listed as affected.
- Heuristic section contains no matched guideline IDs (`matches: []`).

### CI corroboration

Latest PR build failures also indicate spec lock drift, not guideline test regressions:

- Run: https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/actions/runs/21835747027
- Key error: `ERROR: The FLS specification has changed since the lock file was created`
- Recommended command in log: `./make.py --update-spec-lock-file`

## Assessment

Based on the local audit evidence and issue #393 context:

- There is clear FLS/spec-lock drift.
- There is no evidence that existing coding guidelines require textual updates.
- The additional deltas in the newer FLS commit are glossary relocations/additions and one ABI explanatory expansion; none map to affected guideline entries.

## Recommendation

- Proceed with a spec-lock-only update PR (`src/spec.lock`) from a fresh branch off `upstream/main`.
- Include `Closes #393` in the PR body so the issue auto-closes upon merge.
