---
description: Create pending inline PR review from split feedback files
agent: build
---

Use the `pr-review-draft` tool exactly once with these arguments:

- `pr`: parse `$1` as an integer pull request number.
- `feedback_dir`: use `$2` exactly as provided (supports paths under `$OPENCODE_CONFIG_DIR`).
- `apply`: `true` only if `$3` is `--apply`; otherwise `false`.
- `replace_pending`: `false` if either `$3` or `$4` is `--no-replace-pending`; otherwise `true`.

Behavior requirements:

- If required arguments are missing, explain correct usage and stop.
- Do not call `gh api` directly unless the tool fails before execution.
- After tool output, return a concise status and remind the user to run `gh pr view $1 --web` when `apply=true`.

Examples:

- `/pr-review-draft 562 $OPENCODE_CONFIG_DIR/pr-reviews/562-safety-assessor-green-yellow-red --dry-run`
- `/pr-review-draft 562 $OPENCODE_CONFIG_DIR/pr-reviews/562-safety-assessor-green-yellow-red --apply`
