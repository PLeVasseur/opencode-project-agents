# Plan: Sync CONTRIBUTING.md branch updates into upstream PR branch

## Goal

Move any commit(s) that exist only on the fork PR branch onto the branch backing the upstream PR so the upstream PR includes the progressive disclosure changes.

## Current State (confirmed)

- Upstream PR: `rustfoundation/safety-critical-rust-coding-guidelines#331`
  - Head branch: `docs/update-contributing-md-with-bot-details`
- Fork PR: `PLeVasseur/safety-critical-rust-coding-guidelines#8`
  - Head branch: `docs/contributing-progressive-disclosure`
- Extra commits on fork branch:
  - `252fdba` - docs: streamline contributing and add reviewing guide
  - `1dd1461` - docs: switch reviewer note to tip
- Relationship check: `docs/update-contributing-md-with-bot-details` is an ancestor of `docs/contributing-progressive-disclosure`.

## Checklist

- [x] Ensure clean local context for branch operations (`git status`).
- [x] Fetch latest refs from `origin` and `upstream`.
- [x] Check out `docs/update-contributing-md-with-bot-details`.
- [x] Fast-forward upstream-PR branch from progressive-disclosure branch:
  - [x] `git merge --ff-only docs/contributing-progressive-disclosure`
- [x] If fast-forward fails, cherry-pick only missing commits in order (not needed; ff-only succeeded):
  - [x] `git cherry-pick 252fdba` (skipped)
  - [x] `git cherry-pick 1dd1461` (skipped)
- [x] Verify local history contains prior upstream commits plus progressive-disclosure commits.
- [x] Push updated branch to `origin/docs/update-contributing-md-with-bot-details`.
- [x] Confirm upstream PR #331 now shows intended changes (including progressive disclosure updates).
- [x] Decide disposition of fork PR #8 (recommend close as superseded by upstream PR #331).

## Validation Commands

```bash
git log --oneline --decorate --graph -n 12
gh pr view 331 --repo rustfoundation/safety-critical-rust-coding-guidelines --json commits,files,url
```

## Success Criteria

- Upstream PR #331 contains the progressive disclosure commit(s).
- No unintended commits are added.
- Branch history remains linear (fast-forward preferred).
