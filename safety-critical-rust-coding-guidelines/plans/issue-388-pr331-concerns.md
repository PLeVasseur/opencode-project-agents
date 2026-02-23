# Plan: Address PR 331 concerns and add missing completion notes

## Goal
Respond to Felix's PR 331 review concerns with one commit per concern, and add the missing completion-signal notes from issue 388 in a separate commit. Then reply with “Addressed in: <SHA>” on each concern.

## Prereqs
- Work on PR 331 branch `docs/update-contributing-md-with-bot-details`.
- Keep changes doc-only and scoped to `CONTRIBUTING.md`.
- Confirm PR 331 is open and `maintainerCanModify` is true.

## Steps
1) Sync local branch
   - `gh pr checkout 331`
   - `git fetch --all`
   - `git pull --ff-only`

2) Commit 1: clarify round-robin and no-reviewer behavior
   - Add a short explanation of round-robin: queue order + `current_index` cursor; assignments advance the cursor and do not reorder the queue.
   - Note that `/pass` repositions the reviewer to be next up for future assignments.
   - Document that when no reviewer is available (queue empty or all candidates skipped), the bot posts “No reviewers available... /sync-members” and leaves the issue/PR unassigned.
   - Commit message: `docs: clarify round-robin and empty queue behavior`

3) Commit 2: apply wording suggestion
   - Change to: “The queue’s state is stored in Issue #314.”
   - Commit message: `docs: fix queue state wording`

4) Commit 3: add missing completion signals (issue 388 docs)
   - Apply patch: `~/opencode-project-agents/safety-critical-rust-coding-guidelines/patches/issue-388-docs-to-pr331.patch`.
   - Adds issue sign-off completion sentence near the “Within 14 days...” paragraph.
   - Adds PR approval completion sentence in “Review Deadlines.”
   - Ensure wording is scoped correctly: `sign-off: create pr` applies to issues, and PR completion applies only to approvals by the assigned reviewer.
   - Commit message: `docs: add review completion signals`

5) Reply to review comments
   - Post “Addressed in: <SHA>” for Felix’s round-robin comment (Commit 1).
   - Post “Addressed in: <SHA>” for the queue-state wording suggestion (Commit 2).
   - Reply mechanism (use commit SHAs for each):
     - `gh api -X POST repos/rustfoundation/safety-critical-rust-coding-guidelines/pulls/comments/2666489944/replies -f body="Addressed in: <SHA>"`
     - `gh api -X POST repos/rustfoundation/safety-critical-rust-coding-guidelines/pulls/comments/2666492134/replies -f body="Addressed in: <SHA>"`
   - Post replies after pushing commits so SHAs resolve publicly.

6) Push and confirm
   - Push the three commits to the PR 331 head branch.
   - Confirm PR 331 shows the updates and no merge conflicts.

7) Doc checks after edits
   - Confirm round-robin text matches actual behavior (queue + current_index cursor, and `/pass` repositioning).
   - Confirm “No reviewers available” text matches the bot’s comment and triggers only when queue is empty or all candidates are skipped.
   - Confirm completion-signal sentences read cleanly in the “Review Deadlines” section.
   - Confirm text does not imply reviewers are removed from the queue while assigned.
   - Check for redundancy with the “Acceptable Responses” list and trim if needed.

## Draft text (for round-robin + empty queue)
Round-robin here means the bot maintains a queue of Producers and a `current_index` cursor. Each assignment takes the next eligible reviewer in queue order and advances the cursor; the queue order does not change, except when `/pass` repositions the reviewer to be next up for future assignments. If no eligible reviewer is available (queue empty or all candidates skipped), the bot leaves the issue or PR unassigned and posts: “No reviewers available in the queue. Please use `@guidelines-bot /sync-members` to update the queue.”

## Notes
- Do not touch upstream state issue #314.
- Keep these doc changes separate from reviewer-bot code PR 391.
