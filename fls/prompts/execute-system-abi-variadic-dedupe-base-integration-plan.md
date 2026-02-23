Execute the plan at:
`$OPENCODE_CONFIG_DIR/plans/system-abi-variadic-dedupe-base-integration-plan.md`

Context:
- Repo: `/home/pete.levasseur/project/fls`
- Dedupe base branch: `dedupe-paragraph-ids-mainline`
- Assistant source branch: `changelog-assistant-upstream-pr-anchor`
- ABI source branch: `system-abi-variadic`
- The derived branches must be based on dedupe (use `*-on-dedupe` branch names from the plan).
- Integration branch must be created on ABI-on-dedupe, then assistant commits are cherry-picked onto it.
- Canonical upstream URL under test:
  - `https://github.com/rust-lang/rust/pull/145954`
- Write all artifacts under `$OPENCODE_CONFIG_DIR/reports/`.
- Do not push unless explicitly requested.

Execution requirements:
1. Run bootstrap checklist first and report pass/fail for each item.
2. Create and print timestamped `REPORT_ROOT`.
3. Create dedupe-based derived branches/worktrees for assistant and ABI (do not rewrite dirty existing worktrees).
4. Rebase both derived branches onto `dedupe-paragraph-ids-mainline` and capture pre/post SHA evidence.
5. Create integration branch from ABI-on-dedupe and cherry-pick selected assistant commits in order (including prerequisite assistant-introduction commit, anchor-fix commit, and assistant CI commit).
6. Run readiness checks for `tools/changelog_assistant.py` (`--require-anchor` + metadata fields + py_compile).
7. Compute `BASE_REF` using `git merge-base HEAD origin/main` and use that exact value for all assistant invocations.
8. Execute full validation flow (`pre-check`, `update`, `update-second`, anchor miss default, anchor miss strict, `post-check`) and capture stdout/stderr + exit codes + report artifacts.
9. Write `$REPORT_ROOT/summary.md` with explicit acceptance criteria pass/fail and remediation for any failures.

Finish by returning:
- Checklist completion status by section.
- Derived branch/worktree summary and SHAs (`ANCHOR_REBASED_BRANCH`, `ABI_REBASED_BRANCH`, `INTEGRATION_BRANCH`).
- Cherry-pick manifest outcome (old SHA -> new SHA).
- Command summary with exit codes.
- Exact artifact paths under `REPORT_ROOT`.
- Exact integration worktree path and active branch.
- Anchor behavior outcomes:
  - canonical URL (`replace` expected),
  - missing URL default (`append` expected),
  - missing URL strict (`non-zero` expected).
- Pre-check vs post-check result and blockers (if any).
