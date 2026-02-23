# Checklist Plan: Worktree Setup, Main Update, and Perf Rebase Push

## Goal

Rebase `perf/ci-pr-latency-reduction` onto the latest `main` from remote, using a dedicated worktree at `~/eclipse/uprotocol/up-streamer-rust-ci-perf/`, then push the rebased branch.

## Checklist Discipline (Mandatory)

- [x] Read this checklist end-to-end before starting execution.
- [x] Check each box immediately after the associated task is completed.
- [x] Keep only one checklist item actively in progress at a time.
- [x] If a command fails, stop, note the failure, and resolve before continuing.

## Phase 0 - Preflight

- [x] Verify remote state for `main` and `perf/ci-pr-latency-reduction`.
  - Suggested commands:
    - `git ls-remote origin refs/heads/main refs/heads/perf/ci-pr-latency-reduction`
    - `git ls-remote upstream refs/heads/main`
- [x] Verify worktree target path does not already exist.
  - Suggested command:
    - `ls -la ~/eclipse/uprotocol/up-streamer-rust-ci-perf`
- [x] Confirm local baseline commit used as rebase split point is present.
  - Expected split point: `37a1bb81e512b73f6ff3c7d6a685c8ef809a4fd8`
  - Suggested command:
    - `git show --no-patch --oneline 37a1bb81e512b73f6ff3c7d6a685c8ef809a4fd8`

## Phase 1 - Create Worktree and Update Main

- [x] Create the new worktree on `main`.
  - Command:
    - `git worktree add ~/eclipse/uprotocol/up-streamer-rust-ci-perf main`
- [x] In the new worktree, fast-forward `main` from `origin`.
  - Command:
    - `git pull --ff-only origin main`
- [x] Verify `main` now matches `origin/main` in the worktree.
  - Suggested commands:
    - `git rev-parse HEAD`
    - `git rev-parse origin/main`

## Phase 2 - Rebase Perf Branch onto Updated Main

- [x] Switch to `perf/ci-pr-latency-reduction` in the new worktree.
  - Command:
    - `git switch perf/ci-pr-latency-reduction`
- [x] Rebase only perf-specific commits onto updated `main`.
  - Command:
    - `git rebase --onto main 37a1bb81e512b73f6ff3c7d6a685c8ef809a4fd8`
- [x] If conflicts occur, resolve and continue to completion.
  - Suggested loop:
    - `git status`
    - resolve files
    - `git add <resolved-files>`
    - `git rebase --continue`
- [x] Confirm rebase result is correct.
  - Suggested commands:
    - `git merge-base --is-ancestor main HEAD`
    - `git log --oneline --decorate --max-count=25`

## Phase 3 - Push and Verify Remote

- [x] Push the rebased branch to `origin` with lease protection.
  - Command:
    - `git push --force-with-lease origin perf/ci-pr-latency-reduction`
- [x] Verify remote tip matches local `HEAD`.
  - Suggested commands:
    - `git rev-parse HEAD`
    - `git ls-remote origin refs/heads/perf/ci-pr-latency-reduction`
- [x] Confirm working tree is clean after push.
  - Command:
    - `git status --short --branch`

## Success Criteria

- [x] Worktree exists at `~/eclipse/uprotocol/up-streamer-rust-ci-perf/`.
- [x] `main` in that worktree is fast-forwarded to remote `main`.
- [x] `perf/ci-pr-latency-reduction` is rebased onto updated `main`.
- [x] Rebased branch is pushed to `origin` via `--force-with-lease`.
- [x] Remote branch tip equals local branch tip after push.
