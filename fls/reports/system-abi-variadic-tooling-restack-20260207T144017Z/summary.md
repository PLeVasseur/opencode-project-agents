# System ABI tooling restack summary

## Report root
- `/home/pete.levasseur/opencode-project-agents/fls/reports/system-abi-variadic-tooling-restack-20260207T144017Z`

## Bootstrap
- `printenv OPENCODE_CONFIG_DIR`: PASS
- `git fetch origin`: PASS
- `uv sync`: PASS
- Bootstrap metadata captured: `bootstrap-metadata.txt`

## Step 1: Capture integration dirty state
- Integration worktree before restack had local edits in:
  - `src/changelog.rst`
  - `tools/changelog_assistant.py`
- Captured artifacts:
  - `integration_tooling_diff_before.stdout.txt`
  - `integration_changelog_diff_before.stdout.txt`
  - `integration-before.changelog_assistant.py`
  - `integration-before.changelog.rst`
  - `tooling.patch`

## Step 2: Create dedicated tooling branch/worktree
- Created branch: `changelog-assistant-paragraph-buckets-inline-tags-on-dedupe-20260207T144017Z`
- Created worktree: `/home/pete.levasseur/project/fls-changelog-assistant-paragraph-buckets-20260207T144017Z`
- Base branch used: `changelog-assistant-upstream-pr-anchor-title-preserve-on-dedupe`

## Step 3: Apply tooling patch in tooling worktree
- Applied `tooling.patch` cleanly.
- Resulting changed file in tooling worktree: `tools/changelog_assistant.py` only.

## Step 4: Tooling validation
- `py_compile`: PASS (`tooling_py_compile.exitcode` = 0)
- `--help`: PASS (`tooling_help.exitcode` = 0)
- verifier compare: PASS (`tooling_verifier_compare.exitcode` = 0)
- verifier extract: PASS (`tooling_verifier_extract.exitcode` = 0)
- canonical default anchor-hit update: PASS (`update_action=replace`, title preserved)
- canonical `--replace-title` update: PASS (`update_action=replace`, title replaced)
- strict missing anchor (`--require-anchor`): PASS (expected non-zero, exit 1)
- default missing anchor append: PASS (`update_action=append`, exit 0)
- section structure assertion: PASS (only paragraph bucket headers; changed items inline-tagged)
- Restored tooling branch changelog baseline after validation to keep tooling commit scoped to tooling file.

## Step 5: Tooling commit
- Commit branch: `changelog-assistant-paragraph-buckets-inline-tags-on-dedupe-20260207T144017Z`
- Commit SHA: `0c590c4f6143b958b73fd793d19855f1e53c1880`
- Commit message: `refactor(changelog-assistant): render paragraph lifecycle buckets`

## Step 6: Clean integration local tooling edits
- Restored `tools/changelog_assistant.py` in integration worktree before cherry-pick.
- Verified tooling file had no local diff after restore.

## Step 7: Cherry-pick tooling commit into integration
- Cherry-picked `0c590c4f6143b958b73fd793d19855f1e53c1880` into integration branch.
- New integration commit SHA: `b4e9f07813f228541e15a59f67b134d2ec9424d1`
- Mapping artifact: `tooling-cherry-pick-mapping.txt`

## Step 8: Regenerate ABI entry from dedupe boundary
- Integration dedupe-boundary base used:
  - `0165ee6ad6e7e6a54705458d491810b0481b7df4`
  - Recorded in `integration-abi-base-ref.txt`
- Regenerated `145954` entry with:
  - `--base 0165ee6ad6e7e6a54705458d491810b0481b7df4`
  - title-preserving default mode
- Result:
  - `update_action=replace`
  - entry line preserved at `src/changelog.rst:29`
  - canonical URL count remains `1`
  - structure assertion PASS (`Added paragraphs` + `Changed paragraphs`, inline changed tags)

## Dedupe spillover exclusion evidence
- Compared prior origin/main-scoped report vs dedupe-boundary report:
  - old base: `f1b193f5197f48686bd56fe881633bb62fad7f27`
  - new base: `0165ee6ad6e7e6a54705458d491810b0481b7df4`
  - old total changes: `41`
  - new total changes: `35`
  - removed records: `6`
  - removed by type: `paragraph_added=2`, `role_change=2`, `term_ref_removed=2`
  - removed paragraph IDs: `fls_H5vkbMFvzrFs`, `fls_I9JaKZelMiby`, `fls_kqdvWGi9cglm`, `fls_t4yeovFm83Wo`
- Artifact: `integration_compare_origin_main_vs_dedupe_base.stdout.txt`

## Final state
- Tooling worktree status: clean (`changelog-assistant-paragraph-buckets-inline-tags-on-dedupe-20260207T144017Z`)
- Integration worktree status: `M src/changelog.rst` only (expected regenerated ABI entry)
- ABI-on-dedupe worktree remains clean and docs-only.
- No push performed.

## Key artifact index
- Command ledger: `command-exit-codes.tsv`
- Tooling commit evidence: `tooling_commit_create.stdout.txt`, `tooling_commit_sha.stdout.txt`
- Cherry-pick evidence: `integration_cherry_pick_tooling_commit.stdout.txt`, `tooling-cherry-pick-mapping.txt`
- ABI regeneration report: `integration-abi-dedupe-base.json`, `integration-abi-dedupe-base.md`
- Final changelog diff: `integration_abi_diff.stdout.txt`
