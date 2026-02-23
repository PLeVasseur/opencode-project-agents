Execute the canonical plan at:
`$OPENCODE_CONFIG_DIR/plans/pr656-upstream-refresh-handoff-plan-20260214.md`

Context:
- Repo: `/home/pete.levasseur/project/fls`
- Upstream PR: `https://github.com/rust-lang/fls/pull/656`
- Fork PR/source stack: `https://github.com/PLeVasseur/fls/pull/11`
- Target PR head branch to rewrite: `PLeVasseur:glossary-single-source-phase1`
- Source branch with vetted stack: `glossary-single-source-phase1-repack-upstream-main`
- Required base pin: `fb8a46795eda1f1db5e3232002fd94a270bfbffd`
- Required capstone commit: `8e93f35547fcc123ec47ba723ed13129bc19600f`
- Required 4-commit subjects:
  - `feat(glossary): add single-source glossary tooling core`
  - `docs(glossary): migrate glossary content to single-source entries`
  - `ci(glossary): add transitional html parity verification`
  - `refactor(glossary): switch to generated-only glossary source and reproducibility checks`
- Final four-check evidence root:
  - `$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-final-four-check-20260213T220412Z/`
- Placement analysis source artifacts:
  - `$OPENCODE_CONFIG_DIR/reports/commit4-ci-format-remediation-20260213T205932Z/artifacts/pr-11-review.md`
  - `$OPENCODE_CONFIG_DIR/reports/commit4-ci-format-remediation-20260213T205932Z/artifacts/glossary_placement_scores.jsonl`

Critical rules:
1. Never push directly to `upstream`.
2. Rewrite only fork branch `glossary-single-source-phase1` with `--force-with-lease`.
3. Create and push a backup branch before rewrite.
4. If stop conditions trigger (dirty tree, unexpected remote SHA drift, PR head mismatch), stop and ask user.
5. PR body must reference only GitHub attachment URLs (no local paths).
6. Artifact upload requires GitHub web UI handoff; gather URL mapping from user before final PR body rewrite.

Execution requirements:
1. Run full bootstrap checks from plan and report pass/fail for each item.
2. Validate immutable constants (repo/PR target, SHAs, 4 commit subjects).
3. Record old remote SHA for `origin/glossary-single-source-phase1` and create rollback backup branch.
4. Rewrite PR head branch to `8e93f35547fcc123ec47ba723ed13129bc19600f` with explicit lease on old SHA.
5. Verify PR now has exactly 4 commits over base pin and the subjects match.
6. Stage neutral-named upload artifacts under `$OPENCODE_CONFIG_DIR/prs/` and generate:
   - `pr656-artifact-manifest.md`
   - `pr656-artifacts.sha256`
7. Perform Handoff A:
   - provide upload packet path,
   - provide upload order,
   - provide URL mapping template keys,
   - wait for user to return attachment URLs.
8. After URL mapping is received, update PR title/body (`gh pr edit`) using the plan template.
9. Verify final PR state:
   - head SHA/commit stack,
   - attachment links resolve,
   - body has no local file paths,
   - checks status captured.
10. If anything fails, apply rollback procedure from plan and report outcome.

Finish by returning:
- Phase-by-phase checklist status.
- Old remote SHA, backup branch name/SHA, new remote SHA.
- Commands executed (key ones) and exit outcomes.
- Upload packet path + manifest/checksum paths.
- Attachment URL map used in final PR body.
- Final PR URL, title, and exact verification result (4 commits + links + checks).
