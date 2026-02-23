---
name: gh-safe-pr-commenting
description: Create and verify GitHub PR bodies/comments safely with gh using shell-safe heredocs and correction patterns.
license: Apache-2.0
compatibility: opencode
metadata:
  project: up-transport-vsomeip-rust
  workflow: github-cli
---

## When to use

Use this skill for `gh pr create` and `gh pr comment` to avoid shell interpolation bugs and malformed comments.

## PR target safety preflight

- Before creating a PR, verify repository and branch context (`git branch --show-current`, `git remote -v`).
- Always create PRs with explicit target/source flags:

```bash
gh pr create --repo <owner>/<repo> --base main --head <fork-owner>:<branch> --title "..." --body "$(cat <<'EOF'
...
EOF
)"
```

- Immediately verify base/head after creation:

```bash
gh pr view <pr-number-or-url> --repo <owner>/<repo> --json url,baseRefName,headRefName
```

## Safe patterns

- Prefer single-quoted heredocs for multiline bodies:

```bash
gh pr comment 42 --body "$(cat <<'EOF'
Independent CI fix PR: https://github.com/org/repo/pull/123

This isolates main-branch failures from feature PR scope.
EOF
)"
```

- Avoid backticks in double-quoted strings; they can trigger command substitution.
- Avoid inline body strings for complex markdown; use heredoc instead.

## Verification

Prefer verifying the specific comment you just posted (not `.[-1]` on busy threads):

```bash
comment_url="$(gh pr comment 42 --repo <owner>/<repo> --body "$(cat <<'EOF'
Independent CI fix PR: https://github.com/org/repo/pull/123

This isolates main-branch failures from feature PR scope.
EOF
)")"
comment_id="${comment_url##*issuecomment-}"
gh api repos/<owner>/<repo>/issues/comments/"$comment_id" --jq '{html_url, body}'
```

Avoid this pattern for high-traffic threads because it can race with other commenters:

```bash
gh api repos/<owner>/<repo>/issues/<number>/comments --jq '.[-1].body'
```

## If a malformed comment is posted

- Do not rewrite history.
- Post a short correction comment immediately with the correct text/link.
- Recommended correction template:

```bash
gh pr comment 42 --repo <owner>/<repo> --body "$(cat <<'EOF'
Correction to my previous comment:

- Correct PR link: https://github.com/<owner>/<repo>/pull/<number>
- Correct intent: <one-line clarification>
EOF
)"
```

- Keep an auditable trail of what was corrected.
