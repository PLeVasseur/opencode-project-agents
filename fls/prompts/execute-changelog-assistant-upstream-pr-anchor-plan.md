Execute the plan at:
`$OPENCODE_CONFIG_DIR/plans/changelog-assistant-upstream-pr-anchor-plan.md`

Context:
- Repo: `/home/pete.levasseur/project/fls`
- Focus file: `tools/changelog_assistant.py`
- The anchor key must be the upstream Rust PR URL (for example `https://github.com/rust-lang/rust/pull/145954`), not an FLS PR URL.
- Write run artifacts under `$OPENCODE_CONFIG_DIR/reports/`.
- Do not push unless explicitly requested.

Execution requirements:
1. Run the Session bootstrap checklist first and report pass/fail for each item.
2. Set and print `REPORT_ROOT` using a timestamped directory under `$OPENCODE_CONFIG_DIR/reports/`.
3. Determine `BASE_REF` explicitly via `git merge-base HEAD origin/main` and use that exact value for all assistant invocations.
4. Implement the plan completely (design, CLI behavior, update logic, reporting, and validation checks).
5. Validate both anchor-hit and anchor-miss scenarios, including strict failure behavior when anchor is required.
6. Capture command outputs and diffs listed in the plan, with exit codes.
7. Write a final report at `$REPORT_ROOT/summary.md` with explicit acceptance-criteria pass/fail.

Finish by returning:
- Checklist completion status by section.
- Summary of implementation changes (file paths + behavior changes).
- Command summary with exit codes.
- Exact report artifact paths under `$REPORT_ROOT`.
- Exact worktree path and active branch.
- Anchor behavior outcome for:
  - canonical upstream PR URL (`replace` expected),
  - missing URL default mode (`append` expected),
  - missing URL strict mode (`non-zero` expected).
- Any remediation suggestions if acceptance criteria are not fully met.
