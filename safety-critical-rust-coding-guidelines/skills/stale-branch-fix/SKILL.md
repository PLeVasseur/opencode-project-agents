---
name: stale-branch-fix
description: Rebase stale PR branches and restore green CI for this repo.
compatibility: opencode
---

# Stale Branch Fix

## Purpose

Rebase a stale PR branch onto main, repair CI failures, and push fixes back to the PR branch.

## Inputs

- Required:
  ```
  PR_URLS:
  - https://github.com/ORG/REPO/pull/123
  - https://github.com/ORG/REPO/pull/456
  ```
- Optional: `REBASE_BASE: <ref>` (default: rustfoundation/safety-critical-rust-coding-guidelines main)

## Steps

1. For each PR URL, collect metadata and failing checks.
   - `gh pr view` for head repo/ref, base, files, and status checks.
   - `gh pr checks` to identify failed jobs.
   - If needed, `gh run view <id> --log-failed` to capture the root error.
2. Create or update a plan file at `$OPENCODE_CONFIG_DIR/plans/stale-branch-fix-YYYYMMDD.md` with each PR, failures, and intended fixes.
3. Checkout the PR branch locally.
   - Fetch the head branch from an existing remote that matches the head repo owner.
   - Create a local branch that tracks `REMOTE/BRANCH`.
4. Rebase on the latest main (do not merge).
   - Fetch main from the base repo URL without adding a remote:
     - `git fetch https://github.com/rustfoundation/safety-critical-rust-coding-guidelines.git main`
   - `git rebase FETCH_HEAD`
   - Resolve conflicts and continue the rebase.
5. Diagnose and fix failures based on the failing checks.
   - Rust example failures:
     - `uv run python scripts/extract_rust_examples.py --test --src-dir src/coding-guidelines --prelude src/examples_prelude.rs --json build/examples/guideline-results.json --fail-on-error --verbose`
   - Build failures:
     - `uv run python make.py`
   - Python changes:
     - `uv run ruff check --fix`
6. Apply common fixes (see below) so examples compile as standalone crates and match expected behavior.
7. Commit fixes using Conventional Commits.
8. Push updates to the PR head remote and branch.
   - Rebases require `git push --force-with-lease`.
9. Re-check CI status and summarize results.
10. Update this skill with any new failure patterns and fixes discovered.

## Common fixes

- Missing `fn main()` in example snippets: wrap with `fn main() { ... }` or use `:no_run:` with a complete crate.
- Top-level `let`: move into `fn main()` or a test function.
- Inner attributes in the wrong scope: convert to outer attributes or move to the crate/module header.
- Unresolved imports in examples: define minimal mock modules/types inline.
- Unsafe examples: add `:miri:` (`expect_ub` or `skip`) with a short rationale.
- Use `:compile_fail:`, `:should_panic:`, or `:no_run:` to match expected behavior.
- `:compile_fail:` is incompatible with `:miri:`. If an example must fail under Rust 2024 rules, add `:edition: 2024` and remove `unsafe` keywords so Miri is not required.
- Bibliography/citation IDs must match the current guideline ID. Update `:cite:` and `:bibentry:` prefixes (and bibliography `:id:`) to the guideline’s ID when copied.
- Unsupported directives like `.. enforcement::` or `.. related_guidelines::` should be converted to plain text sections.
- `.rst.inc` guideline files are not allowed; convert them to `.rst` and ensure the chapter index uses the `.. toctree::` + `:glob:` pattern.
- Replace all `.. code-block:: rust` with `.. rust-example::` blocks; ensure each example compiles (add `fn main()` or hidden `# fn main() {}` as needed).
- Keep existing generator-format IDs. Only replace IDs that are duplicated, non-template (e.g., `WholeWordsLikeThis`), or look like manual incrementation of a trailing number.
- IDs must follow the template generator format (prefix + 12 chars) when replacements are needed.
- Do not chase unused-citation warnings unless `bibliography_check_unused` is explicitly enabled (default is False in `src/conf.py`).
- If you are confident about a `:release:` value, verify it against the releases.rs website and cite the exact release.
- Avoid function item casts to integers in examples (new warnings); prefer comparing raw pointers (`as *const ()`) to keep examples warning-free.

## Notes

- Do not update `src/spec.lock` unless the user explicitly requests it.
- Netlify failures are often downstream of build or rust-example failures. Focus on the root error first.

## Output

- Per-PR summary of failures found, fixes applied, and files changed.
- Tests or checks run.
- Commit SHAs and push status.
- Updated skill notes for new patterns.
