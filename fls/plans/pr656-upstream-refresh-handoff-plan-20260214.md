# PR #656 Upstream Refresh Handoff Plan (2026-02-14)

## Objective

- [ ] Replace upstream PR #656 branch history with the vetted 4-commit stack from `glossary-single-source-phase1-repack-upstream-main`.
- [ ] Rewrite PR #656 title/body to match the final generated-only approach and final evidence.
- [ ] Ensure `## Testing` references only GitHub attachment URLs (no local filesystem paths).

## Session Bootstrap (Assistant)

- [ ] Confirm environment and auth before any rewrite.
  - [ ] Run `printenv OPENCODE_CONFIG_DIR` and verify it resolves.
  - [ ] Run `gh auth status` and confirm authenticated access covers `PLeVasseur/fls` and `rust-lang/fls`.
  - [ ] Confirm required tools exist: `git`, `gh`, `python3`.
- [ ] Confirm remotes and resolve fallback naming if needed.
  - [ ] Preferred remotes: `origin=git@github.com:PLeVasseur/fls.git`, `upstream=git@github.com:rust-lang/fls.git`.
  - [ ] If names differ, identify equivalent remotes by URL and record the chosen names in run notes.

## Immutable Constants (Must Match)

- [ ] Repository and PR targets.
  - [ ] Upstream PR: `rust-lang/fls#656`.
  - [ ] PR head branch (fork): `PLeVasseur:glossary-single-source-phase1`.
- [ ] Commit pins.
  - [ ] Base pin: `fb8a46795eda1f1db5e3232002fd94a270bfbffd`.
  - [ ] Commit 1: `06da2fd` - `feat(glossary): add single-source glossary tooling core`.
  - [ ] Commit 2: `85a60b6` - `docs(glossary): migrate glossary content to single-source entries`.
  - [ ] Commit 3: `6716db3` - `ci(glossary): add transitional html parity verification`.
  - [ ] Commit 4: `8e93f35547fcc123ec47ba723ed13129bc19600f` - `refactor(glossary): switch to generated-only glossary source and reproducibility checks`.
- [ ] Current expected old remote tip (revalidate live before push): `00ad8917bb407f976793f6dae384512cb6690549`.

## Stop Conditions (Abort And Ask User)

- [ ] Local worktree is dirty before rewrite (`git status --porcelain` not empty).
- [ ] Remote PR branch tip changed from expected old tip before rewrite.
- [ ] PR #656 head repo/branch no longer points to `PLeVasseur:glossary-single-source-phase1`.
- [ ] Any required artifact file is missing or unreadable.
- [ ] User cannot provide attachment URLs after upload step.

## Phase 1 - Branch Rewrite (Assistant)

- [ ] Preflight validation.
  - [ ] Verify local branch is `glossary-single-source-phase1-repack-upstream-main` at `8e93f35547fcc123ec47ba723ed13129bc19600f`.
  - [ ] Verify old remote tip SHA of `origin/glossary-single-source-phase1` and record it.
- [ ] Create rollback-safe backup references.
  - [ ] Create local backup branch: `backup/pr656-pre-rewrite-<UTCSTAMP>` at old tip.
  - [ ] Push backup branch to fork remote for disaster recovery.
- [ ] Rewrite PR head branch with lease protection.
  - [ ] Run: `git push origin 8e93f35547fcc123ec47ba723ed13129bc19600f:glossary-single-source-phase1 --force-with-lease=glossary-single-source-phase1:<old-sha>`.
  - [ ] Verify PR #656 head SHA is now `8e93f35...`.
  - [ ] Verify commit count over base pin is exactly 4 and subjects match the pinned list.

## Rollback Procedure (If Needed)

- [ ] If rewrite causes an issue, restore previous tip using backup.
  - [ ] Confirm backup branch SHA and name.
  - [ ] Run guarded restore push: `git push origin <backup-sha>:glossary-single-source-phase1 --force-with-lease=glossary-single-source-phase1:<current-remote-sha>`.
  - [ ] Re-verify PR head and notify user immediately.

## Phase 2 - Artifact Staging + Manifest (Assistant)

- [ ] Stage upload artifacts with neutral names in a dedicated staging folder under `$OPENCODE_CONFIG_DIR/prs/`.
  - [ ] Source run dir: `reports/glossary-single-source-phase1-final-four-check-20260213T220412Z/`.
  - [ ] Copy and rename files as:
    - [ ] `integrity-chain.md` -> `pr656-final-integrity-chain.md`
    - [ ] `artifacts/diff-upstream-main-vs-commit3.txt` -> `pr656-diff-upstream-main-vs-commit3.txt`
    - [ ] `artifacts/diff-commit3-vs-commit4.txt` -> `pr656-diff-commit3-vs-commit4.txt`
    - [ ] `artifacts/diff-upstream-main-vs-commit4.txt` -> `pr656-diff-upstream-main-vs-commit4.txt`
    - [ ] `capstone-repro-commit4.txt` -> `pr656-capstone-repro-commit4.txt`
  - [ ] Copy placement artifacts and neutralize names:
    - [ ] `reports/commit4-ci-format-remediation-20260213T205932Z/artifacts/pr-11-review.md` -> `pr656-glossary-placement-analysis.md`
    - [ ] `reports/commit4-ci-format-remediation-20260213T205932Z/artifacts/glossary_placement_scores.jsonl` -> `pr656-glossary-placement-scores.jsonl`
- [ ] Generate checksum manifest for upload integrity.
  - [ ] Create `pr656-artifacts.sha256` over all staged files.
  - [ ] Create `pr656-artifact-manifest.md` listing: filename, source path, sha256.

## Handoff A (Assistant -> User)

- [ ] Assistant provides upload packet.
  - [ ] Exact staging directory path.
  - [ ] Upload order recommendation (integrity chain, diff reports, repro report, placement analysis, scores).
  - [ ] Copy/paste template for URL return mapping:
    - [ ] `INTEGRITY_CHAIN_URL=<url>`
    - [ ] `DIFF_UPSTREAM_VS_C3_URL=<url>`
    - [ ] `DIFF_C3_VS_C4_URL=<url>`
    - [ ] `DIFF_UPSTREAM_VS_C4_URL=<url>`
    - [ ] `REPRO_C4_URL=<url>`
    - [ ] `PLACEMENT_ANALYSIS_URL=<url>`
    - [ ] `PLACEMENT_SCORES_URL=<url>`
- [ ] User uploads artifacts in PR #656 via GitHub web UI and returns URL mapping.
  - [ ] Note: `gh` CLI does not provide direct PR attachment upload in this flow; web UI upload is required.

## Phase 3 - PR Title + Body Rewrite With Attachment URLs (Assistant)

- [ ] Update title.
  - [ ] `gh pr edit 656 --repo rust-lang/fls --title "glossary: generated-only glossary source with reproducibility checks"`.
- [ ] Build final body from a template file and apply with `--body-file`.
  - [ ] Keep sections: `## Summary`, `## Reference alignment`, `## Testing`.
  - [ ] Remove outdated statement about committing generated `glossary.rst`/`glossary.rst.inc` as source-of-truth.
  - [ ] Use only attachment URLs provided in Handoff A.
  - [ ] Include placement analysis links and mention score distribution highlights.

### PR Body Template (Fill URL Placeholders Before Edit)

```md
## Summary
- Rebase and restack the glossary single-source migration onto pinned upstream `main` (`fb8a46795eda1f1db5e3232002fd94a270bfbffd`) as 4 logical commits.
- Remove committed autogenerated glossary source (`src/glossary.rst.inc`) to avoid dual source-of-truth, while preserving generated-output reproducibility.
- Keep glossary generation and HTML parity verification in CI, and preserve output parity under configured comparison policy.

Closes rust-lang/fls#655

## Reference alignment
- No Rust Reference semantic changes; this PR is glossary architecture/tooling/verification work.
- Rust 2021 scope remains unchanged.

## Testing
- Final-stack four-check chain on capstone `8e93f35547fcc123ec47ba723ed13129bc19600f`:
  - Integrity chain: <INTEGRITY_CHAIN_URL>
  - `main` vs commit3: <DIFF_UPSTREAM_VS_C3_URL>
  - commit3 vs commit4: <DIFF_C3_VS_C4_URL>
  - `main` vs commit4: <DIFF_UPSTREAM_VS_C4_URL>
  - commit4 reproducibility: <REPRO_C4_URL>
- Automated placement analysis:
  - Review report: <PLACEMENT_ANALYSIS_URL>
  - Per-entry scores JSONL: <PLACEMENT_SCORES_URL>
```

## Phase 4 - Post-Update Verification (Assistant)

- [ ] Verify branch + commit stack.
  - [ ] PR head SHA is `8e93f35...`.
  - [ ] Exactly 4 commits on PR branch over base pin.
  - [ ] Commit subjects match immutable constants.
- [ ] Verify body/link quality.
  - [ ] No local paths (no `/home/`, no `file://`).
  - [ ] All attachment URLs resolve.
  - [ ] `## Testing` includes parity chain + placement analysis links.
- [ ] Verify checks.
  - [ ] Required CI checks are passing or clearly reported as pending/failing.

## Handoff B (Assistant -> User)

- [ ] Assistant returns:
  - [ ] PR URL.
  - [ ] Final title used.
  - [ ] Commit stack verification result.
  - [ ] Attachment URL map used in body.
  - [ ] Any remaining manual follow-up (if any).
- [ ] User performs final sign-off in GitHub UI.
  - [ ] Confirm attachment links open correctly.
  - [ ] Confirm reviewer-facing narrative is accurate and complete.

## Completion Criteria

- [ ] PR #656 head branch rewritten to the 4-commit stack with lease safety and backup created.
- [ ] Rollback path documented and tested-at-command-level (ready if needed).
- [ ] PR title/body accurately reflect final architecture and verification.
- [ ] PR body contains only attachment URLs for artifacts (no local file references).
- [ ] Final four-check reports and placement analysis are accessible from PR #656.
