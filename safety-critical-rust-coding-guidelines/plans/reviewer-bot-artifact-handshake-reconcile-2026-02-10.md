# Reviewer Bot Artifact Handshake Reconcile Plan (2026-02-10)

## Objective

Replace brittle PR discovery in the second-hop reconcile flow with a deterministic artifact handshake from the first-hop `Reviewer Bot` run, then clean up no-longer-needed logic from PR `#399`.

## Why second hop is still required

- Fork `pull_request_review` runs can be read-only and cannot reliably persist reviewer state.
- GitHub documents `workflow_run` as the trusted follow-up pattern and explicitly supports passing data via artifacts from triggering run to triggered run.
- We keep the security model: first hop detects event context, second hop performs write operations.

Reference docs:
- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request_review
- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_run
- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#using-data-from-the-triggering-workflow
- https://docs.github.com/en/rest/actions/artifacts#list-workflow-run-artifacts

## Design summary (artifact handshake)

- First hop writes a tiny JSON payload (`pr_number`, `head_sha`, `event`, `run_id`) to runner temp and uploads it as an artifact bound to that run.
- Second hop (triggered by `workflow_run`) downloads that artifact from `github.event.workflow_run.id`.
- Second hop validates artifact content against `github.event.workflow_run.head_sha` before calling reconciliation.
- If artifact is missing/invalid/mismatched, second hop fails hard (non-zero) rather than green no-op.

## Mandatory execution discipline

- [x] This plan file exists in `$OPENCODE_CONFIG_DIR/plans/`.
- [x] Before branch changes, run `git status --short --branch`; stash if needed.
- [x] Verify `gh auth status` before any remote operations.
- [x] Check off each completed box immediately (no batch check-offs).
- [x] If blocked, append timestamped blocker under "Blockers" and stop.
- [ ] Do not merge to `main` directly; when PR is ready, notify maintainer and wait for merge confirmation.

## Scope

In scope:
- Harden second-hop PR resolution using artifact handshake.
- Remove/replace brittle owner/branch fallback introduced in PR `#399`.
- Add fail-closed behavior for unresolved workflow-run reconcile.
- Update tests and workflow permissions/conditions.

Out of scope:
- Reworking reviewer assignment queue semantics.
- Changing state storage away from issue `#314`.

## Phase 0 - Preflight and branch hygiene

- [x] Source env and confirm config dir:
  - `source /home/pete.levasseur/opencode-project-agents/shell/opencode-env.sh`
  - `printenv OPENCODE_CONFIG_DIR`
- [x] Confirm clean-or-stashed working state:
  - `git status --short --branch`
  - if dirty: `git stash push -u -m "wip before artifact handshake fix"`
  - if stashed: record stash ref from `git stash list --max-count=1`
- [x] Confirm auth: `gh auth status`
- [x] Ensure `upstream` remote exists and points to canonical repo:
  - `git remote get-url upstream || git remote add upstream https://github.com/rustfoundation/safety-critical-rust-coding-guidelines.git`
  - `git remote get-url upstream`
- [x] Sync branch base from `upstream/main` and create/reset fix branch deterministically:
  - `git fetch upstream`
  - `git checkout main`
  - `git reset --hard upstream/main`
  - `if git show-ref --verify --quiet refs/heads/fix/reviewer-bot-artifact-handshake-reconcile; then git switch fix/reviewer-bot-artifact-handshake-reconcile && git reset --hard upstream/main; else git switch -c fix/reviewer-bot-artifact-handshake-reconcile; fi`

## Phase 1 - Reconfirm failure mode and capture baseline evidence

- [x] Select baseline evidence PR:
  - prefer PR `#397`
  - if stale/unavailable, select latest comparable fork PR with an `APPROVED` review
  - example selector: `gh pr list --repo rustfoundation/safety-critical-rust-coding-guidelines --state all --limit 100 --json number,headRepositoryOwner,reviews,url --jq '.[] | select(.headRepositoryOwner.login != "rustfoundation") | select(any(.reviews[]?; .state == "APPROVED")) | "#\(.number) \(.url)"'`
- [x] Record selected PR number as `BASELINE_PR`.
- [x] Capture primary `Reviewer Bot` run log for `BASELINE_PR` approval event (read-only deferral evidence).
- [x] Capture second-hop `Reviewer Bot Reconcile` run log for same approval showing failure/no-op behavior.
- [x] Capture issue `#314` state entry for `BASELINE_PR` with `review_completed_at: null`.
- [x] Record all run IDs and links used for final report traceability.

Traceability notes:
- `BASELINE_PR=397` (`https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/397`)
- First hop run (pull_request_review submitted): `21842580728` (`https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/actions/runs/21842580728`)
- Second hop run (workflow_run reconcile): `21842595930` (`https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/actions/runs/21842595930`)
- State issue evidence: `https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/314`

## Phase 2 - Define artifact contract and migration cleanup decisions

- [x] Finalize artifact schema (v1), minimum fields:
  - `schema_version` (int)
  - `event_name` (string)
  - `event_action` (string)
  - `pr_number` (int)
  - `head_sha` (string)
  - `source_run_id` (int)
- [x] Finalize artifact name format:
  - `reviewer-bot-reconcile-context-${{ github.run_id }}`
- [x] Lock cleanup strategy for PR `#399` logic:
  - remove owner/branch fallback entirely
  - do not retain fallback behind feature flag
- [x] Lock fail-closed policy:
  - unresolved PR in `workflow_run` path must return non-zero
  - missing/invalid artifact must fail reconcile run

## Phase 3 - First-hop workflow changes (`.github/workflows/reviewer-bot.yml`)

- [x] Add step gated to review submissions only:
  - `if: github.event_name == 'pull_request_review' && github.event.action == 'submitted'`
- [x] Write reconcile context JSON to `${{ runner.temp }}/reviewer-bot/reconcile-context.json` from trusted workflow context fields (not script output).
- [x] Include schema fields exactly:
  - `schema_version`, `event_name`, `event_action`, `pr_number`, `head_sha`, `source_run_id`
- [x] Upload context with `actions/upload-artifact@v4`:
  - `name: reviewer-bot-reconcile-context-${{ github.run_id }}`
  - `path: ${{ runner.temp }}/reviewer-bot/reconcile-context.json`
  - `retention-days: 1`
  - `if-no-files-found: error`
- [x] Ensure upload step executes after bot step when first-hop run is successful, including read-only deferral cases.

## Phase 4 - Second-hop workflow changes (`.github/workflows/reviewer-bot-reconcile.yml`)

- [x] Add guard for both:
  - `github.event.workflow_run.event == 'pull_request_review'`
  - `github.event.workflow_run.conclusion == 'success'`
- [x] Add/confirm permissions include:
  - `issues: write`
  - `pull-requests: write`
  - `contents: read`
  - `actions: read` (artifact download)
- [x] Download artifact from triggering run id using `actions/download-artifact@v5` with explicit inputs:
  - `name: reviewer-bot-reconcile-context-${{ github.event.workflow_run.id }}`
  - `run-id: ${{ github.event.workflow_run.id }}`
  - `repository: ${{ github.repository }}`
  - `github-token: ${{ secrets.GITHUB_TOKEN }}`
  - `path: ${{ runner.temp }}/reviewer-bot`
- [x] Parse artifact JSON and export env vars for script:
  - `WORKFLOW_RUN_RECONCILE_PR_NUMBER`
  - `WORKFLOW_RUN_RECONCILE_HEAD_SHA`
- [x] Pass `WORKFLOW_RUN_HEAD_SHA` from workflow payload for cross-check.
- [x] Fail immediately (non-zero) if artifact missing, JSON parse fails, required fields absent, or SHA mismatch.

## Phase 5 - Script changes (`scripts/reviewer_bot.py`)

- [x] Add strict resolver for workflow-run reconcile:
  - require explicit artifact env (`WORKFLOW_RUN_RECONCILE_PR_NUMBER`, `WORKFLOW_RUN_RECONCILE_HEAD_SHA`)
  - validate artifact SHA equals workflow-run SHA
  - validate PR fetched by number has matching `head.sha`
  - reject zero/negative/non-integer PR numbers
- [x] Make unresolved/invalid workflow-run reconcile return failure (non-zero), not success/no-op.
- [x] Keep idempotency: already-completed review remains no-op success.
- [x] Keep `/rectify` behavior unchanged.

### Cleanup from earlier PR `#399`

- [x] Remove now-unneeded env wiring from reconcile workflow:
  - `WORKFLOW_RUN_PULL_REQUESTS`
  - `WORKFLOW_RUN_HEAD_BRANCH`
  - `WORKFLOW_RUN_HEAD_REPO_OWNER`
- [x] Remove brittle fallback helpers:
  - `find_open_pr_by_head`
  - owner/branch fallback path inside `resolve_workflow_run_pr_number`
- [x] Remove tests that enforce owner/branch fallback behavior.
- [x] Update log text to reflect artifact-based resolution path.

## Phase 6 - Tests and quality gates

- [x] Add/adjust tests in `.github/reviewer-bot-tests/test_reviewer_bot.py` for:
  - artifact-based PR resolution success
  - missing artifact env -> hard failure
  - SHA mismatch -> hard failure
  - PR head SHA mismatch -> hard failure
  - idempotent no-op when review already complete
- [x] Run lint autofix: `uv run ruff check --fix`
- [x] Run tests: `uv run pytest .github/reviewer-bot-tests`
- [x] Verify tests demonstrate fail-closed behavior (invalid context yields failure, not no-op success).
- [x] Verify no unexpected diffs remain.

## Phase 7 - Ship and validate live behavior

- [x] Commit with Conventional Commit message.
- [x] Push branch and open upstream PR:
  - `--repo rustfoundation/safety-critical-rust-coding-guidelines`
  - `--head PLeVasseur:<branch>`
- [x] In PR body, explicitly call out cleanup of PR `#399` fallback logic.
- [x] Notify maintainer PR is ready to merge and stop; do not merge it yourself.
- [ ] Wait for maintainer confirmation that fix PR is merged to `upstream/main`.
- [ ] After maintainer merge confirmation, ask maintainer to have a collaborator submit an approval on target fork PR (prefer `BASELINE_PR` if still open).
- [ ] Validate post-merge behavior on that approval event:
  - verify first-hop run uploads `reviewer-bot-reconcile-context-<run_id>` artifact
  - verify second-hop run downloads artifact from triggering run id
  - verify second-hop run reconciles and persists state
  - verify issue `#314` entry has non-null `review_completed_at`
  - verify `review_completion_source: workflow_run:pull_request_review`
  - verify no manual `/rectify` required
- [ ] If no suitable open fork PR exists, create a disposable fork smoke PR, run same checks, then close it without merge.

## Phase 8 - Rollback and contingency

- [ ] If artifact handshake fails in production smoke, rollback plan:
  - disable reconcile workflow in follow-up hotfix PR, or
  - temporarily restore manual `/rectify`-only operation while retaining diagnostics.
- [ ] Keep failure logs and run IDs in incident notes for root-cause follow-up.
- [ ] If a preflight stash was created, restore it at the end:
  - inspect `git stash list`
  - `git stash pop` only for the stash created in this plan session

## Acceptance criteria

- [x] Second-hop reconcile resolves PR deterministically via artifact contract.
- [x] No silent green no-op when PR cannot be resolved.
- [ ] Fork PR approval auto-persists without manual `/rectify`.
- [x] Lint and reviewer-bot tests pass.
- [x] Cleanup of obsolete PR `#399` fallback paths is complete (or explicitly justified if retained).
- [ ] PR was handed off to maintainer for merge (no self-merge), then post-merge validation completed.

## Blockers

- [ ] No blockers logged yet.
- [x] 2026-02-09T23:16:53Z - Blocked pending maintainer merge confirmation for PR `#400`; post-merge collaborator approval event is required to complete live validation steps.
