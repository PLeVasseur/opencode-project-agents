# PR review workflow usage

## Two-step process

1. Generate split feedback files.
2. Draft pending inline review comments from those files.

If newly added slash commands are not visible, restart OpenCode once.

## Commands

Generate files:

```text
/pr-review-generate 562 safety-assessor-green-yellow-red
```

Preview draft payload (no writes):

```text
/pr-review-draft 562 $OPENCODE_CONFIG_DIR/pr-reviews/562-safety-assessor-green-yellow-red --dry-run
```

Create pending inline review comments:

```text
/pr-review-draft 562 $OPENCODE_CONFIG_DIR/pr-reviews/562-safety-assessor-green-yellow-red --apply
```

Open the PR in browser:

```text
gh pr view 562 --web
```

## Notes

- `00-summary.md` and any `comment_type: general` files are not auto-posted.
- Only inline `01+` files are posted by draft mode.
- Draft mode creates a pending review and does not submit it.
- You manually add final summary and submit `Request changes` in GitHub UI.
