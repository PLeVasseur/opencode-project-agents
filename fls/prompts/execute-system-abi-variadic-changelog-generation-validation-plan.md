Execute the plan at:
`$OPENCODE_CONFIG_DIR/plans/system-abi-variadic-changelog-generation-validation-plan.md`

Context:
- Repo: `/home/pete.levasseur/project/fls`
- Branch: `system-abi-variadic`
- This plan writes validation artifacts under `$OPENCODE_CONFIG_DIR/reports/`.
- Do **not** enable `--require-tags` for this validation run.
- Do not push unless requested.

Requirements:
1. Run the Session bootstrap checklist first and report pass/fail per item.
2. Set and print `REPORT_ROOT` with a timestamped path under `$OPENCODE_CONFIG_DIR/reports/`.
3. Determine `BASE_REF` explicitly via merge-base with `origin/main` and use it for all assistant commands.
4. Execute the pre-check, update, and post-check commands exactly as the plan specifies, recording exit codes.
5. Capture `git diff -- src/changelog.rst` into report artifacts and verify:
   - generated entry is under the correct release section,
   - `Change tags:` line is present,
   - paragraph/section references align with detected changes.
6. Produce tags-to-generated-content mapping evidence and include it in the report.
7. Write a final summary report to `$REPORT_ROOT/summary.md`.

Finish by returning:
- Checklist completion status by section.
- Summary of commands executed with exit codes.
- Exact artifact paths written under `$REPORT_ROOT`.
- Exact worktree path used for execution, plus active branch name.
- Pre-check vs post-check results.
- Generated entry quality assessment and any remediation suggestions if validation fails.
