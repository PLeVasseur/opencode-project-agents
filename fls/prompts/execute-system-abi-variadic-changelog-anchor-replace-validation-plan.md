Execute the plan at:
`$OPENCODE_CONFIG_DIR/plans/system-abi-variadic-changelog-anchor-replace-validation-plan.md`

Context:
- Repo: `/home/pete.levasseur/project/fls`
- Branch: `system-abi-variadic`
- This run validates anchor-hit replacement behavior for canonical upstream PR URL:
  - `https://github.com/rust-lang/rust/pull/145954`
- Artifacts must be written under `$OPENCODE_CONFIG_DIR/reports/`.
- Do **not** enable `--require-tags`.
- Do not push unless explicitly requested.

Execution requirements:
1. Run the Session bootstrap checklist first and report pass/fail for each item.
2. Set and print `REPORT_ROOT` as a timestamped directory under `$OPENCODE_CONFIG_DIR/reports/`.
3. Determine `BASE_REF` explicitly via `git merge-base HEAD origin/main` and use that exact value for all assistant invocations.
4. Validate branch readiness before behavior tests:
   - verify `tools/changelog_assistant.py` exists,
   - verify `--require-anchor` appears in help,
   - verify update report metadata supports `update_action` and anchor fields.
   - If missing and needed, rebase `system-abi-variadic` onto `origin/main` (allowed), then re-run readiness checks.
5. Execute pre-check, update, idempotence second update, and post-check exactly as defined in the plan, capturing stdout/stderr and exit codes.
6. Capture `git diff -- src/changelog.rst` artifacts and verify:
   - entry is updated under the correct release section,
   - `Change tags:` line is present,
   - paragraph/section references use `:p:` / `:ref:` consistently with detected changes.
7. Provide explicit anchor evidence:
   - canonical URL top-level entry count and line location before update,
   - canonical URL count/line after first update,
   - canonical URL count/line after second update,
   - expected count remains `1` throughout (replacement, not duplication).
8. Produce tags-to-generated-content mapping evidence and include it in the report.
9. Write final report to `$REPORT_ROOT/summary.md` with acceptance-criteria pass/fail.

Finish by returning:
- Checklist completion status by section.
- Command summary with exit codes.
- Exact artifact paths under `$REPORT_ROOT`.
- Exact worktree path and active branch.
- Readiness-check outcome (and whether rebase was performed).
- Pre-check vs post-check results.
- Anchor behavior verdict for canonical upstream URL (`replace` expected).
- Generated entry quality assessment and remediation suggestions for any failure.
