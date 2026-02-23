# Execute PR-78 Copyright Header Remediation Plan

You are executing a focused, non-functional remediation pass.

## Plan to Execute

- Read and execute: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/plans/pr-78-copyright-header-remediation-plan.md`
- Keep all checkboxes in that plan accurate as you progress.

## Objective

Add missing copyright headers and correct non-2026 year values for files introduced in this branch scope, while preserving behavior and keeping fixture/data artifacts unchanged.

## Branch/Scope

- Working branch: `cleanup/refactor-upstream-main`
- Scope range: `bugfix/issue-74-left-topic-authority..cleanup/refactor-upstream-main`
- In-scope files for header work:
  - newly added `.rs`, `.toml`, `.sh` in the above range
  - `up-streamer/tests/api_contract_forwarding_rules.rs` year correction (`2024` -> `2026`)
- Out-of-scope: fixture/data files (`.log`, `.csv`, `.json`) including:
  - `utils/transport-smoke-suite/tests/fixtures/**/*.log`
  - `utils/criterion-guardrail/tests/fixtures/**/*.csv`
  - `utils/transport-smoke-suite/claims/*.json`

## Hard Requirements

1. Use `2026` in all new/updated headers in this remediation.
2. Match existing repository header styles by file type:
   - Rust block header style (as in `up-streamer/src/lib.rs`)
   - TOML `#` header style
   - Shell `#` style after shebang
3. Preserve shebang on line 1 for shell scripts.
4. Do not introduce functional changes.
5. Keep edits header-only.

## Execution Steps

1. Run session bootstrap checks exactly as documented in the plan.
2. Generate authoritative in-scope target list from git range and reconcile with plan inventory before editing.
3. Capture baseline audit outputs (missing headers + non-2026 years + wrong-year seed check).
4. Apply headers and year correction to all in-scope targets.
5. Re-run verification commands from the plan until all checks pass.
6. Update plan checkboxes to completed for all executed items.
7. Stage only header/year edits.
8. Commit with:
   - `chore: align new-file copyright headers to 2026`
9. Push branch.
10. Add a PR comment on `https://github.com/eclipse-uprotocol/up-streamer-rust/pull/78` summarizing:
    - number of files updated
    - confirmation that changes are header-only
    - verification command outcomes

## Verification Commands (must pass/return clean)

- `git diff --name-only --diff-filter=A bugfix/issue-74-left-topic-authority..cleanup/refactor-upstream-main | rg '\\.(rs|toml|sh)$' | xargs -r rg -L "Copyright"`
- `git diff --name-only --diff-filter=A bugfix/issue-74-left-topic-authority..cleanup/refactor-upstream-main | rg '\\.(rs|toml|sh)$' | xargs -r rg -n "Copyright \\(c\\) (2024|2025|2027|2028|2029)"`
- `rg -n "Copyright \\(c\\) 2026" up-streamer/tests/api_contract_forwarding_rules.rs`
- `git diff --stat`
- `git diff` (spot-check header-only scope)

## Final Output Requirements

Provide a concise closeout that includes:

- executed plan status (all checkboxes complete or explicit blockers)
- files changed (count + key paths)
- commit hash
- PR comment link or confirmation message ID
- verification command results
- explicit confirmation: no behavior changes, header-only remediation
