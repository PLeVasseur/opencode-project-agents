# Plan: Open 3 Upstream PRs to `main` with Upstream-Numbered Summaries

Date: 2026-02-14
Repo: `eclipse-uprotocol/up-streamer-rust`
Head owner: `PLeVasseur`

## Objective

- [x] Create three upstream PRs from fork branches, all targeting `main`.
  - [x] Upstream PR for `cleanup/refactor-upstream-main-prA-architecture` created.
  - [x] Upstream PR for `cleanup/refactor-upstream-main-prB-benchmark` created.
  - [x] Upstream PR for `cleanup/refactor-upstream-main-prC-smoke` created.
- [x] Keep the same summary/body style while replacing stack terms with upstream PR numbers.
  - [x] Remove A/B/C terminology in upstream PR text.
  - [x] Replace fork numbering references (`#33/#34/#35`) with upstream numbers (`#83/#84/#85`).
  - [x] Use explicit dependency text because all upstream PRs target `main`.

## Non-Negotiables

- [x] All three upstream PRs target `main`.
  - [x] PR `#83` base is `main`.
  - [x] PR `#84` base is `main`.
  - [x] PR `#85` base is `main`.
- [x] Do not push stack branches to `upstream`.
  - [x] Use `--head PLeVasseur:<branch>` for each `gh pr create`.
  - [x] If push is required, push only to `origin`.
- [x] Preserve existing PR body style sections.
  - [x] Keep `Summary` section structure.
  - [x] Keep `Stack Context` section structure.
  - [x] Keep `Validation` section structure.

## Constants (copy/paste once)

- [x] Export execution variables.
  - [x] Run:

```bash
UPSTREAM_REPO="eclipse-uprotocol/up-streamer-rust"
HEAD_OWNER="PLeVasseur"
BRANCH_U1="cleanup/refactor-upstream-main-prA-architecture"
BRANCH_U2="cleanup/refactor-upstream-main-prB-benchmark"
BRANCH_U3="cleanup/refactor-upstream-main-prC-smoke"
FORK_PR_U1="33"
FORK_PR_U2="34"
FORK_PR_U3="35"
```

## Phase 0: Preflight

- [x] Confirm CLI auth and upstream visibility.
  - [x] `gh auth status`
  - [x] `gh repo view "$UPSTREAM_REPO" --json nameWithOwner,defaultBranchRef`
- [x] Confirm no existing upstream PRs already use these heads.
  - [x] `gh pr list --repo "$UPSTREAM_REPO" --head "$HEAD_OWNER:$BRANCH_U1" --state all`
  - [x] `gh pr list --repo "$UPSTREAM_REPO" --head "$HEAD_OWNER:$BRANCH_U2" --state all`
  - [x] `gh pr list --repo "$UPSTREAM_REPO" --head "$HEAD_OWNER:$BRANCH_U3" --state all`
- [x] Confirm branch heads exist on fork (`origin`).
  - [x] `git fetch origin --prune`
  - [x] `git rev-parse "origin/$BRANCH_U1" "origin/$BRANCH_U2" "origin/$BRANCH_U3"`

## Phase 1: Prepare Body Templates

- [x] Pull current fork PR titles/bodies as baseline text.
  - [x] `gh pr view "$FORK_PR_U1" --repo "PLeVasseur/up-streamer-rust" --json title,body`
  - [x] `gh pr view "$FORK_PR_U2" --repo "PLeVasseur/up-streamer-rust" --json title,body`
  - [x] `gh pr view "$FORK_PR_U3" --repo "PLeVasseur/up-streamer-rust" --json title,body`
- [x] Draft upstream body templates with placeholders in `$OPENCODE_CONFIG_DIR/prompts/`.
  - [x] `upstream-u1-body.md` uses placeholders `#U1/#U2/#U3`.
  - [x] `upstream-u2-body.md` uses placeholders `#U1/#U2/#U3` and dependency text.
  - [x] `upstream-u3-body.md` uses placeholders `#U1/#U2/#U3` and dependency text.
- [x] Normalize terminology in templates before creation.
  - [x] Replace A/B/C words with explicit `PR #...` wording.
  - [x] Replace fork PR-number mentions with placeholders pending real upstream numbers.

## Phase 2: Create Upstream PR `#U1` (Architecture)

- [x] Create upstream PR from fork head to upstream `main`.
  - [x] Run:

```bash
gh pr create \
  --repo "$UPSTREAM_REPO" \
  --base main \
  --head "$HEAD_OWNER:$BRANCH_U1" \
  --title "$(gh pr view "$FORK_PR_U1" --repo PLeVasseur/up-streamer-rust --json title -q .title)" \
  --body-file "$OPENCODE_CONFIG_DIR/prompts/upstream-u1-body.md"
```

- [x] Capture number/URL for `#U1`.
  - [x] `gh pr list --repo "$UPSTREAM_REPO" --head "$HEAD_OWNER:$BRANCH_U1" --state open --json number,url`

## Phase 3: Create Upstream PR `#U2` (Benchmark)

- [x] Substitute known `#U1` into PR2 body template.
  - [x] Ensure dependency line reads: `Depends on #U1`.
  - [x] Keep base target text as `main`.
- [x] Create upstream PR from fork head to upstream `main`.
  - [x] Run:

```bash
gh pr create \
  --repo "$UPSTREAM_REPO" \
  --base main \
  --head "$HEAD_OWNER:$BRANCH_U2" \
  --title "$(gh pr view "$FORK_PR_U2" --repo PLeVasseur/up-streamer-rust --json title -q .title)" \
  --body-file "$OPENCODE_CONFIG_DIR/prompts/upstream-u2-body.md"
```

- [x] Capture number/URL for `#U2`.
  - [x] `gh pr list --repo "$UPSTREAM_REPO" --head "$HEAD_OWNER:$BRANCH_U2" --state open --json number,url`

## Phase 4: Create Upstream PR `#U3` (Smoke)

- [x] Substitute known `#U1` and `#U2` into PR3 body template.
  - [x] Ensure dependency line reads: `Depends on #U2` (transitively `#U1`).
  - [x] Keep base target text as `main`.
- [x] Create upstream PR from fork head to upstream `main`.
  - [x] Run:

```bash
gh pr create \
  --repo "$UPSTREAM_REPO" \
  --base main \
  --head "$HEAD_OWNER:$BRANCH_U3" \
  --title "$(gh pr view "$FORK_PR_U3" --repo PLeVasseur/up-streamer-rust --json title -q .title)" \
  --body-file "$OPENCODE_CONFIG_DIR/prompts/upstream-u3-body.md"
```

- [x] Capture number/URL for `#U3`.
  - [x] `gh pr list --repo "$UPSTREAM_REPO" --head "$HEAD_OWNER:$BRANCH_U3" --state open --json number,url`

## Phase 5: Renumbering and Dependency Consistency Pass

- [x] Update all three upstream PR bodies to use only upstream numbering.
  - [x] PR `#83` mentions downstream as `#84` and `#85`.
  - [x] PR `#84` references `#83` as dependency and review order `#83 -> #84 -> #85`.
  - [x] PR `#85` references `#84` dependency and transitive `#83`.
- [x] Ensure no A/B/C stack tokens remain in upstream PR bodies.
  - [x] Verify PR `#83` body has no `PR A/PR B/PR C` language.
  - [x] Verify PR `#84` body has no `PR A/PR B/PR C` language.
  - [x] Verify PR `#85` body has no `PR A/PR B/PR C` language.
- [x] Ensure each body states target branch as `main`.
  - [x] PR `#83` text and metadata agree on `main`.
  - [x] PR `#84` text and metadata agree on `main`.
  - [x] PR `#85` text and metadata agree on `main`.

## Phase 6: Verification and Handoff

- [x] Verify base/head metadata for all three upstream PRs.
  - [x] `gh pr view "#83" --repo "$UPSTREAM_REPO" --json number,url,baseRefName,headRefName`
  - [x] `gh pr view "#84" --repo "$UPSTREAM_REPO" --json number,url,baseRefName,headRefName`
  - [x] `gh pr view "#85" --repo "$UPSTREAM_REPO" --json number,url,baseRefName,headRefName`
- [x] Record final mapping and URLs.
  - [x] `#U1 = #83` URL: `https://github.com/eclipse-uprotocol/up-streamer-rust/pull/83`
  - [x] `#U2 = #84` URL: `https://github.com/eclipse-uprotocol/up-streamer-rust/pull/84`
  - [x] `#U3 = #85` URL: `https://github.com/eclipse-uprotocol/up-streamer-rust/pull/85`
- [x] Record dependency chain exactly as text to share back.
  - [x] `#84` depends on `#83`.
  - [x] `#85` depends on `#84` (transitively `#83`).

## Failure Handling (only if needed)

- [x] If `gh pr create` reports branch is missing remotely: (N/A; not needed)
  - [x] Push missing branch to `origin` only: `git push origin <branch>`. (N/A)
  - [x] Retry `gh pr create` with same `--head "$HEAD_OWNER:<branch>"`. (N/A)
- [x] If upstream PR already exists for a head branch: (N/A; not needed)
  - [x] Reuse existing upstream PR number as `#U1/#U2/#U3` mapping. (N/A)
  - [x] Skip creation and continue with renumbering consistency pass. (N/A)
