Execute this implementation plan end-to-end:
`$OPENCODE_CONFIG_DIR/plans/reviewer-bot-reconcile-comment-followup-2026-02-10.md`

Execution rules:
- Treat the plan as the source of truth.
- Check off each checkbox immediately when completed (do not batch updates).
- If blocked, stop and log the blocker in the plan's "Blockers" section with timestamp.
- Run preflight exactly as specified, including branching from `upstream/main` (not stale local `main`).
- Implement only the scoped follow-up fix:
  - second-hop reconcile must post PR comment when `state_changed == true`
  - idempotent no-op reconcile must not post comment
  - fail-closed artifact/context validation behavior must remain intact
- Run quality gates with:
  - `uv run ruff check --fix`
  - `uv run pytest .github/reviewer-bot-tests`
- Use Conventional Commit message style and open the PR against upstream using:
  - `--repo rustfoundation/safety-critical-rust-coding-guidelines`
  - `--head PLeVasseur:<branch>`
- After pushing the fix PR, stop and send a clear heads-up that the PR is ready for maintainer merge.
- Do not merge to `main` yourself; wait for maintainer merge confirmation.
- After merge confirmation, create a fresh smoke PR from `upstream/main` with a trivial change and request collaborator approval for live validation.
- Smoke validation preconditions (must be explicitly checked):
  - smoke PR has a review-tracked label (`coding guideline` or `fls-audit`)
  - `active_reviews[PR]` exists with a `current_reviewer`
  - approval is submitted by that `current_reviewer` (or assign/claim first)
- Validate post-merge behavior on the approval event:
  - first hop defers + uploads reconcile artifact
  - second hop downloads/validates artifact from triggering run
  - second hop posts reconcile PR comment when state changes
  - issue `#314` persists `review_completed_at`
- Reactions note: missing `eyes`/`+1` is not a failure for this plan; those reactions are currently tied to `issue_comment` command handling unless explicitly implemented as a separate feature.

Final report must include:
- root cause
- code changes
- validation evidence (run IDs, URLs, and key log lines)
- whether reconcile PR comment was posted on smoke PR
- reaction behavior explanation (`issue_comment` path vs review/reconcile path)
- remaining risks
- exact plan checkbox status
