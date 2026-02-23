Execute the plan at:
`$OPENCODE_CONFIG_DIR/plans/system-abi-variadic-anchor-title-preserve-and-integration-plan.md`

Context:
- Repo: `/home/pete.levasseur/project/fls`
- Dedupe base branch: `dedupe-paragraph-ids-mainline`
- Assistant source branch: `changelog-assistant-upstream-pr-anchor`
- ABI source branch: `system-abi-variadic`
- Canonical upstream URL under test:
  - `https://github.com/rust-lang/rust/pull/145954`
- Missing upstream URL under test:
  - `https://github.com/rust-lang/rust/pull/999999`
- Preserve-title behavior under test:
  - Default anchor-hit update preserves existing title.
  - `--replace-title` anchor-hit update replaces title.
- Baseline expected canonical title:
  - `Stabilize declaration of C-style variadic functions for the system ABI`
- Override probe title:
  - `Anchor replace validation title override probe`
- Write all artifacts under `$OPENCODE_CONFIG_DIR/reports/`.
- Do not push unless explicitly requested.

Execution requirements:
1. Run bootstrap checklist first and report pass/fail for each item.
2. Create and print timestamped `REPORT_ROOT`.
3. Implement assistant-side behavior change in `tools/changelog_assistant.py`:
   - add `--replace-title`,
   - preserve anchored title by default,
   - keep append behavior unchanged,
   - keep `--require-anchor` behavior unchanged.
4. Run assistant readiness checks and validation (`--help`, `py_compile`, compare/extract verifier runs).
5. Commit assistant changes with a Conventional Commit message and capture commit SHA.
6. Create dedupe-based derived branches/worktrees for assistant and ABI (do not rewrite dirty existing worktrees).
7. Rebase both derived branches onto `dedupe-paragraph-ids-mainline` and capture pre/post SHA evidence.
8. Create integration branch from ABI-on-dedupe and cherry-pick selected assistant commits in order, including:
   - assistant introduction commit,
   - anchor-fix commit,
   - assistant CI commit,
   - new preserve-title commit,
   - any prerequisites (document rationale).
9. Run readiness checks in integration worktree (`--require-anchor`, `--replace-title`, metadata fields, `py_compile`).
10. Compute `BASE_REF` using `git merge-base HEAD origin/main` and use that exact value for all assistant invocations.
11. Execute full validation flow and capture stdout/stderr + exit codes + artifacts:
   - pre-check,
   - canonical update without `--replace-title` using alternate title (must preserve existing title),
   - canonical update with `--replace-title` using alternate title (must replace title),
   - idempotence rerun for `--replace-title`,
   - strict missing-anchor check first (must be non-zero),
   - default missing-anchor check second (must append, exit 0),
   - post-check.
12. Write `$REPORT_ROOT/summary.md` with explicit acceptance criteria pass/fail and remediation for any failures.

Finish by returning:
- Checklist completion status by section.
- Derived branch/worktree summary and SHAs (`ANCHOR_REBASED_BRANCH`, `ABI_REBASED_BRANCH`, `INTEGRATION_BRANCH`).
- Cherry-pick manifest outcome (old SHA -> new SHA).
- Command summary with exit codes.
- Exact artifact paths under `REPORT_ROOT`.
- Exact integration worktree path and active branch.
- Title behavior outcomes:
  - anchor-hit default preserves title,
  - anchor-hit + `--replace-title` replaces title.
- Anchor behavior outcomes:
  - canonical URL (`replace` expected),
  - missing URL default (`append` expected),
  - missing URL strict (`non-zero` expected).
- Pre-check vs post-check result and blockers (if any).
