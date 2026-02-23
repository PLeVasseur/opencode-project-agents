Execute the plan at:
`$OPENCODE_CONFIG_DIR/plans/dedupe-maintenance-corrections-pr5-execution-plan.md`

Context:
- Repo: `/home/pete.levasseur/project/fls`
- Existing PR under update: `https://github.com/PLeVasseur/fls/pull/5`
- PR head branch: `dedupe-paragraph-ids-mainline`
- PR base branch: `main`
- Preferred worktree: `/home/pete.levasseur/project/fls-paragraph-id-dedup-mainline`
- Add this exact standalone section before `Language changes in Rust 1.93.0`:

```rst
FLS maintenance corrections
---------------------------

- Deduplicate historically reused paragraph IDs in the glossary (ID-integrity fix).

  - Corrected glossary `discriminant type` paragraph ID:
    - old reused ID: ``fls_t4yeovFm83Wo``
    - new unique ID: ``fls_kqdvWGi9cglm``
  - Corrected glossary `local trait` paragraph ID:
    - old reused ID: ``fls_I9JaKZelMiby``
    - new unique ID: ``fls_H5vkbMFvzrFs``
  - This is a historical FLS maintenance correction (no Rust language semantics change).
```

- Write all artifacts under `$OPENCODE_CONFIG_DIR/reports/`.
- This execution SHOULD update the existing PR #5 branch and PR body (push is expected for that).

Execution requirements:
1. Run bootstrap checklist and create timestamped `REPORT_ROOT`.
2. Attach to the existing PR head branch (`dedupe-paragraph-ids-mainline`) in the dedupe worktree; verify clean/dirty status and preserve unrelated edits.
3. Capture pre-change evidence (`git status`, `git diff`, relevant changelog excerpt).
4. Insert the maintenance section exactly once, in the required location.
5. Run `./make.py` and capture stdout/stderr + exit code.
6. Stage only intended files (expected: `src/changelog.rst`), commit with:
   - `docs(changelog): add maintenance note for deduplicated glossary IDs`
   - capture commit SHA.
7. Push `dedupe-paragraph-ids-mainline` to update PR #5.
8. Update PR #5 body to include maintenance rationale. Use this structure:

```md
## Summary
- Deduplicate two reused `:dp:` IDs inherited from mainline by updating glossary entries only.
- Add a standalone `FLS maintenance corrections` changelog section documenting the old->new ID mapping.
- Keep canonical IDs in `src/types-and-traits.rst` unchanged and re-ID the duplicate glossary entries.
- Reduce duplicate paragraph IDs across `src/` from 2 to 0.

## Reference alignment
- No Rust language-rule semantic changes.
- This is historical FLS maintenance (paragraph-ID integrity correction), so it is documented outside the Rust 1.93 language-change item.

## Testing
- `./make.py`
- Duplicate `:dp:` inventory before/after (before: 2 duplicates, after: 0 duplicates)
```

9. Verify final PR metadata with:
   - `gh pr view 5 --json title,headRefName,baseRefName,body,url`
10. Write `$REPORT_ROOT/summary.md` with explicit pass/fail by section and remediation notes for any failures.

Finish by returning:
- Checklist completion status by section.
- Branch/worktree used and final `git status`.
- Commit SHA and push outcome.
- PR #5 URL + head/base confirmation + summary of body updates.
- Command summary with exit codes.
- Exact artifact paths under `REPORT_ROOT`.
