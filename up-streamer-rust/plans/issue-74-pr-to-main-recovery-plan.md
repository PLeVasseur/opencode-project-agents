# Issue #74 PR-to-main Recovery Plan

## Goal

- [x] Open a PR from `PLeVasseur:bugfix/issue-74-left-topic-authority` to `eclipse-uprotocol/up-streamer-rust:main` without rebasing/cherry-picking.

## Steps

- [x] Abort the accidental in-progress cherry-pick on `bugfix/issue-74-left-topic-authority-main`:
  - [x] `git cherry-pick --abort`
- [x] Switch back to the original branch that contains the intended stacked work:
  - [x] `git switch bugfix/issue-74-left-topic-authority`
- [x] Verify branch/worktree state before PR creation:
  - [x] `git status -sb`
  - [x] `git branch --show-current`
  - [x] confirm `HEAD` is `a553a37` (or the expected latest commit on this branch)
- [x] Confirm remote context:
  - [x] `origin` points to `PLeVasseur/up-streamer-rust`
  - [x] `upstream` points to `eclipse-uprotocol/up-streamer-rust`
- [x] Create PR targeting upstream `main` (not the unavailable stacked base):
  - [x] head: `PLeVasseur:bugfix/issue-74-left-topic-authority`
  - [x] base: `main`
  - [x] use `gh pr create --repo eclipse-uprotocol/up-streamer-rust --base main --head PLeVasseur:bugfix/issue-74-left-topic-authority`
- [x] Use issue-74 plan-aligned PR title and summary:
  - [x] title: `fix(issue-74): enforce left-side publish authority mapping and add reproducible CLI validation`
  - [x] summary includes: left-side authority enforcement, register/unregister symmetry, regression tests, full example-binary CLI parameterization, docs/runbook updates, integration harness alignment
- [x] Include explicit stacked-branch context in PR body:
  - [x] note that this branch was developed on top of `perf/ci-pr-latency-reduction`
  - [x] note that base is `main` because the stacked base branch is not present upstream
  - [x] clearly separate issue-74 commits from inherited parent commits in the write-up
- [x] Capture and share final PR URL.

- [x] Final PR URL: `https://github.com/eclipse-uprotocol/up-streamer-rust/pull/77`
