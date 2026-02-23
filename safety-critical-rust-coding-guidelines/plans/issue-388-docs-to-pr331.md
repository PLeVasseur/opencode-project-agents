# Plan: Apply issue-388 doc clarifications to PR 331

## Goal
Integrate the issue-388 documentation clarifications into PR 331's `CONTRIBUTING.md` without mixing them into the reviewer-bot code PR.

## Scope
- Add issue completion text for `sign-off: create pr` label.
- Add PR completion text for assigned reviewer approval and timer reset behavior.

## Deliverables
- Doc-only patch file stored at `~/opencode-project-agents/safety-critical-rust-coding-guidelines/patches/issue-388-docs-to-pr331.patch`.
- Targeted update applied to PR 331 (either a commit on its branch or suggestion comments).

## Steps
1) Verify PR 331 is still open and `maintainerCanModify` is true.
2) Apply the patch to the PR 331 branch (preferred) or post the patch as inline suggestion comments.
3) Confirm placement:
   - Issue sign-off completion sentence is near the “Within 14 days…” issue review guidance.
   - PR approval completion sentence is near the “Review Deadlines” section.
4) Re-check for conflicts with existing reviewer-bot text and adjust wording if needed.
5) Request review or mark the PR as updated once changes are applied.

## Notes
- Do not touch upstream issue #314 or any upstream state issues.
- Keep these doc changes separate from the feature branch code changes.
