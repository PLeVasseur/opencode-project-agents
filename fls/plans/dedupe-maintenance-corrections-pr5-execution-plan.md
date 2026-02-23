# Plan: Add maintenance-corrections changelog note on existing PR #5

## Objective
- [ ] Add a standalone `FLS maintenance corrections` section to `src/changelog.rst`.
- [ ] Land it on the **existing PR branch** (`dedupe-paragraph-ids-mainline`), not a new branch.
- [ ] Update PR #5 summary to explain why this is historical FLS maintenance, not a Rust 1.93 language-change item.

## Fixed context for new session
- [ ] Repo: `/home/pete.levasseur/project/fls`
- [ ] Existing PR: `https://github.com/PLeVasseur/fls/pull/5`
- [ ] PR head branch: `dedupe-paragraph-ids-mainline`
- [ ] PR base branch: `main`
- [ ] Preferred worktree for this branch: `/home/pete.levasseur/project/fls-paragraph-id-dedup-mainline`

## Scope
- [ ] Edit: `src/changelog.rst` only.
- [ ] PR metadata update: PR #5 body text.
- [ ] Validation: `./make.py` (+ optional duplicate-ID sanity check).

## Non-goals
- [ ] No tooling refactors.
- [ ] No ABI-entry restructuring.
- [ ] No new branch and no new PR.

## Content to insert (exact)
- [ ] Add this section **after** the full `Language changes in Rust 1.93.0` section (that is, between `Language changes in Rust 1.93.0` and `Language changes in Rust 1.92.0`):

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

## Execution checklist

### 1) Bootstrap and report root
- [ ] `printenv OPENCODE_CONFIG_DIR`
- [ ] `git fetch origin`
- [ ] `uv sync`
- [ ] Create report root under `$OPENCODE_CONFIG_DIR/reports/`, e.g.:
  - [ ] `$OPENCODE_CONFIG_DIR/reports/dedupe-maintenance-corrections-pr5-<timestamp>/`
- [ ] Start command ledger with stdout/stderr/exit codes.

### 2) Attach to existing PR branch
- [ ] Open worktree `/home/pete.levasseur/project/fls-paragraph-id-dedup-mainline`.
- [ ] Verify branch is `dedupe-paragraph-ids-mainline`.
- [ ] Capture `git status --short --branch`.
- [ ] If dirty with unrelated edits, preserve them and only stage intended file(s).

### 3) Apply changelog edit
- [ ] Insert maintenance section exactly once, immediately after the Rust 1.93.0 section (before the Rust 1.92.0 heading).
- [ ] Keep release sections intact.
- [ ] Preserve RST formatting/spaces/blank lines.

### 4) Validate
- [ ] Run `./make.py`.
- [ ] Record warnings/errors in report artifacts.
- [ ] Read back edited region to confirm text and placement.
- [ ] Optional sanity check (if available): verify duplicate paragraph-ID count remains 0.

### 5) Commit on same branch
- [ ] Stage `src/changelog.rst` only (unless another file is intentionally required).
- [ ] Commit with conventional message:
  - [ ] `docs(changelog): add maintenance note for deduplicated glossary IDs`
- [ ] Capture new commit SHA.

### 6) Push and update existing PR #5
- [ ] Push `dedupe-paragraph-ids-mainline`.
- [ ] Update PR #5 body to include maintenance rationale.

Use this PR body structure:

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

### 7) Final verification
- [ ] Confirm PR #5 now contains the new commit and updated body.
- [ ] Capture `gh pr view 5 --json title,headRefName,baseRefName,body,url` to report.
- [ ] Confirm no additional branches/PRs were created.

## Acceptance criteria
- [ ] Maintenance section exists in `src/changelog.rst` after the 1.93 release section and before the 1.92 release section.
- [ ] Change is on branch `dedupe-paragraph-ids-mainline` and attached to PR #5.
- [ ] PR body clearly explains historical-maintenance nature of the change.
- [ ] Build succeeds or warnings are documented with rationale.
- [ ] Report artifacts are complete for fresh-session replay.
