# Glossary PR6 feedback remediation execution plan

## Objective

- [ ] Resolve and disposition all issues raised in the PR6 feedback bundle, with explicit evidence and reviewer-ready artifacts.
- [ ] Keep remediation aligned to the staged migration strategy (phase 1 correctness first, then phase 2 harmonization), while preserving stacked branch integrity.
- [ ] Make execution reproducible for a fresh session (deterministic preflight, run-scoped report paths, explicit stop conditions).

## Feedback inputs (must be referenced throughout)

- [ ] `"$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback/fls-pr6-review-report.md"`
- [ ] `"$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback/term_reliability.json"`
- [ ] `"$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback/fls-pr6-placement-fitness.json"`
- [ ] `"$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback/fls-pr6-placement-fitness-examples.md"`

## Scope and sequencing

- [ ] **Phase 1 (PR6) blocker fixes**
  - [ ] Fix coverage-accounting blind spots in migration tooling.
  - [ ] Add chapter definitions for terms reported missing (`casting`, `namespace qualifier`, `shadowed`) or document final disposition if a term is intentionally alias-only.
- [ ] **Phase 2 (PR7) harmonization fixes**
  - [ ] Resolve low-confidence semantic divergence terms from `term_reliability.json`.
  - [ ] Reassess moderate divergences and chapter-only terms; capture explicit keep/move/add rationale.
- [ ] **Cross-cutting**
  - [ ] Produce remediation reports under a dedicated report folder.
  - [ ] Restack and revalidate downstream branches after step1/step2 updates.

## Guardrails

- [ ] Do not introduce `.. glossary-entry::` or `.. glossary-include::`.
- [ ] Use project entrypoints (`./make.py`, `./generate-glossary.py`) for build/parity commands.
- [ ] Do not run `sphinx-build` or `sphinx-autobuild` directly.
- [ ] Preserve unrelated user changes in all worktrees.
- [ ] Keep all generated remediation artifacts under `$OPENCODE_CONFIG_DIR/reports/`.

## Fresh-session preflight (required)

- [ ] Export canonical absolute paths and branch names used by this plan:

```bash
export REPO_ROOT="/home/pete.levasseur/project/fls"
export STEP1_WT="/home/pete.levasseur/project/fls-wt/step1"
export STEP2_WT="/home/pete.levasseur/project/fls-wt/step2"
export STEP3_WT="/home/pete.levasseur/project/fls-wt/step3"
export STEP4_WT="/home/pete.levasseur/project/fls-wt/step4"
export STEP5_WT="/home/pete.levasseur/project/fls-wt/step5"
export STEP1_BRANCH="glossary-step-1-main-text-coverage"
export STEP2_BRANCH="glossary-step-2-align-duplicate-text"
export STEP3_BRANCH="glossary-step-3-dt-main-only"
export STEP4_BRANCH="glossary-step-4-remove-see-paragraphs"
export STEP5_BRANCH="glossary-step-5-generated-glossary-parity"
```

- [ ] Verify environment and auth:

```bash
printenv OPENCODE_CONFIG_DIR
gh auth status
```

- [ ] Verify remotes and fetch latest branch state:

```bash
git -C "$REPO_ROOT" remote -v
git -C "$REPO_ROOT" fetch --all --prune
```

- [ ] Verify worktree/branch mapping and cleanliness before edits:

```bash
git -C "$REPO_ROOT" worktree list
for wt in "$STEP1_WT" "$STEP2_WT" "$STEP3_WT" "$STEP4_WT" "$STEP5_WT"; do
  echo "=== $wt ==="
  git -C "$wt" status --short --branch
done
```

- [ ] Verify local/remote sync for step branches and record in report:

```bash
for b in "$STEP1_BRANCH" "$STEP2_BRANCH" "$STEP3_BRANCH" "$STEP4_BRANCH" "$STEP5_BRANCH"; do
  local_sha=$(git -C "$REPO_ROOT" rev-parse "$b")
  remote_sha=$(git -C "$REPO_ROOT" ls-remote --heads origin "$b" | cut -f1)
  printf '%s local=%s remote=%s\n' "$b" "$local_sha" "$remote_sha"
done
```

- [ ] Confirm stacked PR mapping is still the expected chain (#6-#10 for step1-step5):

```bash
for n in 6 7 8 9 10; do
  gh pr view "$n" --repo PLeVasseur/fls --json number,baseRefName,headRefName,url
done
```

- [ ] If any expected PR is missing/closed/repointed, proceed with discovered stack IDs from bootstrap PR-discovery artifact.

## Bootstrap

- [ ] Set execution variables:

```bash
export FEEDBACK_ROOT="$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage"
export FEEDBACK_DIR="$FEEDBACK_ROOT/feedback"
export RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)"
export REMEDIATION_DIR="$OPENCODE_CONFIG_DIR/reports/glossary-pr6-feedback-remediation-$RUN_ID"
mkdir -p "$REMEDIATION_DIR"
```

- [ ] Confirm `"$REMEDIATION_DIR"` starts empty before writing artifacts.

- [ ] Discover active stack PR IDs by step-branch head and persist mapping:

```bash
gh pr list --repo PLeVasseur/fls --state open --limit 200 --json number,baseRefName,headRefName,url \
  | jq '[.[] | select(.headRefName==env.STEP1_BRANCH or .headRefName==env.STEP2_BRANCH or .headRefName==env.STEP3_BRANCH or .headRefName==env.STEP4_BRANCH or .headRefName==env.STEP5_BRANCH)]' \
  > "$REMEDIATION_DIR/pr-stack-discovery.json"

export PR_STEP1="$(jq -r '.[] | select(.headRefName==env.STEP1_BRANCH) | .number' "$REMEDIATION_DIR/pr-stack-discovery.json")"
export PR_STEP2="$(jq -r '.[] | select(.headRefName==env.STEP2_BRANCH) | .number' "$REMEDIATION_DIR/pr-stack-discovery.json")"
export PR_STEP3="$(jq -r '.[] | select(.headRefName==env.STEP3_BRANCH) | .number' "$REMEDIATION_DIR/pr-stack-discovery.json")"
export PR_STEP4="$(jq -r '.[] | select(.headRefName==env.STEP4_BRANCH) | .number' "$REMEDIATION_DIR/pr-stack-discovery.json")"
export PR_STEP5="$(jq -r '.[] | select(.headRefName==env.STEP5_BRANCH) | .number' "$REMEDIATION_DIR/pr-stack-discovery.json")"
```

- [ ] Validate `PR_STEP1..PR_STEP5` are all non-empty before any PR updates/comments.
- [ ] Record whether discovered IDs match expected `6..10`; if they differ, use discovered IDs everywhere in this run and note the divergence in `"$REMEDIATION_DIR/feedback-baseline-reconciliation.md"`.

- [ ] Save a feedback manifest (input provenance + checksums):

```bash
sha256sum \
  "$FEEDBACK_DIR/term_reliability.json" \
  "$FEEDBACK_DIR/fls-pr6-review-report.md" \
  "$FEEDBACK_DIR/fls-pr6-placement-fitness.json" \
  "$FEEDBACK_DIR/fls-pr6-placement-fitness-examples.md" \
  > "$REMEDIATION_DIR/feedback-inputs.sha256"
```

- [ ] Capture baseline checker output before changes:

```bash
uv run ./tools/glossary-migration-check.py --phase 1 --strict --report "$REMEDIATION_DIR/baseline-phase1-check.json"
uv run ./tools/glossary-migration-check.py --phase 2 --strict --report "$REMEDIATION_DIR/baseline-phase2-check.json"
```

## Baseline reconciliation (feedback snapshot vs current branch)

- [ ] Record feedback snapshot metadata and current branch heads:

```bash
jq '.metadata' "$FEEDBACK_DIR/term_reliability.json" > "$REMEDIATION_DIR/feedback-metadata.json"
for b in "$STEP1_BRANCH" "$STEP2_BRANCH"; do
  printf '%s %s\n' "$b" "$(git -C "$REPO_ROOT" rev-parse "$b")"
done > "$REMEDIATION_DIR/current-step-heads.txt"
```

- [ ] Compare feedback analyzed commit to current step1 head and record staleness (`same` / `different`) in `"$REMEDIATION_DIR/feedback-baseline-reconciliation.md"`.
- [ ] Recompute current coverage/alignment metrics from strict checker outputs and compare against feedback counts (`missing`, `low`, `moderate`, `chapter_only`) with explicit notes on any mismatch drivers.
- [ ] Treat feedback files as advisory when snapshot commit differs, but keep all dispositions traceable to both the feedback and current branch outputs.

## Workstream A - Fix phase 1 coverage accounting blind spots (PR6)

### A0) Policy decision gate: disallowed directive check

- [ ] Confirm directive policy for this remediation run:
  - [ ] Remove disallowed-directive enforcement from migration tooling and extension (requested direction), or
  - [ ] Keep enforcement and document reason.
- [ ] If removed, update plan/test expectations so phase strict reports do not require `no-disallowed-directives` entries.
- [ ] Record final decision in `"$REMEDIATION_DIR/policy-decisions.md"`.

### A1) Tooling correction (`tools/glossary-migration-check.py`)

- [ ] Update glossary term collection logic to account for multi-term glossary definitions inside one heading/paragraph.
- [ ] Ensure all glossary-defined aliases are represented in term inventory (not only first `:dt:` in section).
- [ ] Verify `term_id` derivation remains aligned with extension rules (`id_from_text("term", target)`).
- [ ] Preserve deterministic inventory ordering.

### A2) Regression checks for known blind-spot examples

- [ ] Add executable checks (script output assertions and/or tests) proving coverage includes:
  - [ ] `cast` and `casting`
  - [ ] `path` and `namespace qualifier`
  - [ ] `shadowing` and `shadowed`
- [ ] Save evidence to `"$REMEDIATION_DIR/coverage-accounting-regression.md"`.

### A3) Re-run phase 1 strict check and inventory after tooling fix

- [ ] Regenerate reports:

```bash
uv run ./tools/glossary-migration-check.py --phase 1 --strict --report "$REMEDIATION_DIR/post-tooling-phase1-check.json"
```

- [ ] Record deltas vs baseline in `"$REMEDIATION_DIR/phase1-check-delta.md"`.

## Workstream B - Close missing chapter definitions (PR6)

### B1) Missing terms from feedback

- [ ] Address all terms flagged as `missing_from_chapter` in `term_reliability.json`:
  - [ ] `casting`
  - [ ] `namespace qualifier`
  - [ ] `shadowed`

### B2) Placement and wording policy for these terms

- [ ] Place each term near first normative use.
- [ ] If alias-style, define using concise redirect wording that preserves canonical target.
- [ ] Ensure paragraph IDs and roles conform to FLS lint expectations.

### B3) Validation for missing-term closure

- [ ] Verify these terms appear in chapter definitions via checker inventory/report.
- [ ] Produce `"$REMEDIATION_DIR/missing-term-resolution.md"` with:
  - [ ] term
  - [ ] chapter file and line
  - [ ] chosen wording
  - [ ] rationale

## Phase gates and hard stops

- [ ] **Gate G1 (must pass before Workstream C / PR7 edits):**
  - [ ] `post-tooling-phase1-check.json` is green.
  - [ ] Missing-term closure is complete (`casting`, `namespace qualifier`, `shadowed` resolved or explicitly dispositioned).
  - [ ] `./make.py --clear` and `./make.py --check-links` pass on step1 branch.
- [ ] If Gate G1 fails, do not start phase2 harmonization; fix and rerun or stop and record blocker in `"$REMEDIATION_DIR/blockers.md"`.

- [ ] **Gate G2 (must pass before push/restack):**
  - [ ] Phase1 final strict/build/link checks pass.
  - [ ] Phase2 final strict/build/link checks pass.
  - [ ] Divergence adjudication and placement disposition artifacts are complete.
- [ ] If Gate G2 fails, do not push; fix and rerun or stop and document blocker/remediation.

## Workstream C - Resolve semantic divergence backlog (PR7 / Phase 2)

### C1) Build adjudication ledger from `term_reliability.json`

- [ ] Create `"$REMEDIATION_DIR/divergence-adjudication.csv"` with columns:
  - [ ] `term`
  - [ ] `chapter_file`
  - [ ] `similarity`
  - [ ] `category` (`significant_reword` / `moderate_divergence` / `extended` / redirect)
  - [ ] `decision` (`chapter_wins` / `glossary_wins` / `merge-both` / `tooling-artifact`)
  - [ ] `action`
  - [ ] `rationale`
  - [ ] `status`

### C2) Prioritize low-confidence terms first

- [ ] Triage all `reliability=low` entries (68 in feedback file).
- [ ] Start with terms under similarity `< 0.45` and terms called out as concept drift risks in feedback:
  - [ ] `call conformance`
  - [ ] `concrete type`
  - [ ] `ffi`
  - [ ] `borrowed`
  - [ ] `construct`
  - [ ] `char`
  - [ ] `primitive representation`

### C3) Handle extraction/normalization artifacts explicitly

- [ ] Validate whether list-item formatting causes false divergence signals (`call site hygiene` case).
- [ ] If tooling artifact, record as `tooling-artifact` in ledger and adjust checker normalization as needed.

### C4) Execute harmonization edits on phase 2 branch

- [ ] Apply wording alignment decisions to chapter and/or glossary content (as scoped for phase 2).
- [ ] Keep changes narrowly targeted to definition harmonization.
- [ ] Re-run strict phase 2 checker and confirm mismatch report is empty.

## Workstream D - Placement fitness disposition (reviewer confidence)

### D1) Triage placement recommendations with conceptual-home filter

- [ ] Use `fls-pr6-placement-fitness.json` high/medium candidates.
- [ ] For each candidate, classify as:
  - [ ] `relocate-now`
  - [ ] `keep-conceptual-home`
  - [ ] `forward-reference-only` (keep location, improve local discoverability)
- [ ] Apply explicit acceptance criteria:
  - [ ] `relocate-now` only when all are true:
    - [ ] `conceptual_home.is_conceptual_home != true`
    - [ ] relocation priority is `high` or `medium`
    - [ ] recommendation has clear owning section fit (not only first-use frequency)
  - [ ] `keep-conceptual-home` when any are true:
    - [ ] `conceptual_home.is_conceptual_home == true`
    - [ ] term is foundational taxonomy likely to be broadly forward-referenced (`value`, `construct`, etc.)
  - [ ] `forward-reference-only` when conceptual home is correct but definition occurs after first important use.
- [ ] Do not relocate terms solely based on reference count concentration if it would break chapter ownership semantics.

### D2) Required disposition report

- [ ] Produce `"$REMEDIATION_DIR/placement-disposition.md"` including:
  - [ ] high-priority candidates from fitness report
  - [ ] decision and rationale per term
  - [ ] mapping to follow-up phase/PR

### D3) Forward-reference mitigations

- [ ] For kept-at-home terms with early use, add precise cross-links/nearby references where beneficial.
- [ ] Capture all such mitigations in `placement-disposition.md`.

## Validation matrix (must pass before pushing)

### PR6 / phase 1 branch

- [ ] `uv run ./tools/glossary-migration-check.py --phase 1 --strict --report "$REMEDIATION_DIR/final-phase1-check.json"`
- [ ] `./make.py --clear`
- [ ] `./make.py --check-links`
- [ ] Confirm missing-term set is empty in final phase1 report.

### PR7 / phase 2 branch

- [ ] `uv run ./tools/glossary-migration-check.py --phase 2 --strict --report "$REMEDIATION_DIR/final-phase2-check.json"`
- [ ] `./make.py --clear`
- [ ] `./make.py --check-links`
- [ ] Confirm mismatch report empty for phase2 strict run.

### Stack integrity after updates

- [ ] Fast-forward restack downstream branches:
  - [ ] `git -C "$STEP2_WT" merge --ff-only "$STEP1_BRANCH"`
  - [ ] `git -C "$STEP3_WT" merge --ff-only "$STEP2_BRANCH"`
  - [ ] `git -C "$STEP4_WT" merge --ff-only "$STEP3_BRANCH"`
  - [ ] `git -C "$STEP5_WT" merge --ff-only "$STEP4_BRANCH"`
- [ ] If any FF-only merge fails, follow this fallback policy:
  - [ ] Fetch and inspect divergence first:

```bash
git -C "$REPO_ROOT" fetch --all --prune
for pair in \
  "$STEP2_WT:$STEP1_BRANCH" \
  "$STEP3_WT:$STEP2_BRANCH" \
  "$STEP4_WT:$STEP3_BRANCH" \
  "$STEP5_WT:$STEP4_BRANCH"; do
  wt="${pair%%:*}"
  base="${pair##*:}"
  echo "=== divergence $wt vs $base ==="
  git -C "$wt" log --oneline --left-right --cherry-pick --boundary "$base...HEAD"
done
```

  - [ ] For published branches (PR already open), prefer merge-based restack (no force-push history rewrite).
  - [ ] Use rebase only if branch has not been pushed yet; otherwise document why rebase is avoided.
  - [ ] Re-run strict/build/link checks on that branch immediately after non-FF synchronization.
  - [ ] Record sync decision and commands in `"$REMEDIATION_DIR/stack-sync-decisions.md"`.
- [ ] Verify ancestry chain with concrete checks:

```bash
git -C "$REPO_ROOT" merge-base --is-ancestor "$STEP1_BRANCH" "$STEP2_BRANCH"
git -C "$REPO_ROOT" merge-base --is-ancestor "$STEP2_BRANCH" "$STEP3_BRANCH"
git -C "$REPO_ROOT" merge-base --is-ancestor "$STEP3_BRANCH" "$STEP4_BRANCH"
git -C "$REPO_ROOT" merge-base --is-ancestor "$STEP4_BRANCH" "$STEP5_BRANCH"
```

## Reporting deliverables (required)

- [ ] `"$REMEDIATION_DIR/feedback-inputs.sha256"`
- [ ] `"$REMEDIATION_DIR/pr-stack-discovery.json"`
- [ ] `"$REMEDIATION_DIR/feedback-metadata.json"`
- [ ] `"$REMEDIATION_DIR/current-step-heads.txt"`
- [ ] `"$REMEDIATION_DIR/feedback-baseline-reconciliation.md"`
- [ ] `"$REMEDIATION_DIR/baseline-phase1-check.json"`
- [ ] `"$REMEDIATION_DIR/baseline-phase2-check.json"`
- [ ] `"$REMEDIATION_DIR/post-tooling-phase1-check.json"`
- [ ] `"$REMEDIATION_DIR/phase1-check-delta.md"`
- [ ] `"$REMEDIATION_DIR/policy-decisions.md"`
- [ ] `"$REMEDIATION_DIR/coverage-accounting-regression.md"`
- [ ] `"$REMEDIATION_DIR/missing-term-resolution.md"`
- [ ] `"$REMEDIATION_DIR/divergence-adjudication.csv"`
- [ ] `"$REMEDIATION_DIR/placement-disposition.md"`
- [ ] `"$REMEDIATION_DIR/stack-sync-decisions.md"`
- [ ] `"$REMEDIATION_DIR/final-phase1-check.json"`
- [ ] `"$REMEDIATION_DIR/final-phase2-check.json"`
- [ ] `"$REMEDIATION_DIR/blockers.md"` (if any gate fails)
- [ ] `"$REMEDIATION_DIR/pr6-body.md"`
- [ ] `"$REMEDIATION_DIR/pr7-body.md"`
- [ ] `"$REMEDIATION_DIR/pr8-restack-note.md"`
- [ ] `"$REMEDIATION_DIR/pr9-restack-note.md"`
- [ ] `"$REMEDIATION_DIR/pr10-restack-note.md"`
- [ ] `"$REMEDIATION_DIR/commands.log"` (append-only, timestamped)
- [ ] `"$REMEDIATION_DIR/exit-codes.md"`

## Commit and PR update checklist

- [ ] Commit tooling + phase1 missing-term fixes on `glossary-step-1-main-text-coverage` with Conventional Commit messages.
- [ ] Commit phase2 harmonization fixes on `glossary-step-2-align-duplicate-text`.
- [ ] Push updated branches and verify checks for PR6/PR7.
- [ ] Update PR descriptions with:
  - [ ] what issue from feedback was fixed
  - [ ] where evidence artifact lives
  - [ ] what remains deferred and why
- [ ] Use explicit PR update commands with body files captured in remediation artifacts:

```bash
gh pr edit "$PR_STEP1" --repo PLeVasseur/fls --title "docs(glossary): phase 1 main text coverage" --body-file "$REMEDIATION_DIR/pr6-body.md"
gh pr edit "$PR_STEP2" --repo PLeVasseur/fls --title "docs(glossary): phase 2 align duplicate text" --body-file "$REMEDIATION_DIR/pr7-body.md"
```

- [ ] Post stack status comments after restack so reviewers know inheritance changed:

```bash
gh pr comment "$PR_STEP3" --repo PLeVasseur/fls --body-file "$REMEDIATION_DIR/pr8-restack-note.md"
gh pr comment "$PR_STEP4" --repo PLeVasseur/fls --body-file "$REMEDIATION_DIR/pr9-restack-note.md"
gh pr comment "$PR_STEP5" --repo PLeVasseur/fls --body-file "$REMEDIATION_DIR/pr10-restack-note.md"
```

## Exit criteria

- [ ] No glossary terms are silently dropped by coverage accounting.
- [ ] `casting`, `namespace qualifier`, and `shadowed` are resolved and evidenced.
- [ ] Low-confidence divergence terms are fully dispositioned with explicit decisions.
- [ ] Placement-fitness recommendations are fully dispositioned (move/keep/forward-ref rationale).
- [ ] Phase 1 and phase 2 strict checks pass with artifacts attached.
- [ ] Stacked branch ancestry and CI are green after restack.
