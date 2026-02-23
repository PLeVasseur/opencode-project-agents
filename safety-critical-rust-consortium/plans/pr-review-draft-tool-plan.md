# Plan: Two-Step PR Review Workflow (Generate + Draft)

## Objective
Create a reusable workflow in `$OPENCODE_CONFIG_DIR` that supports two explicit steps:

1. Generate structured review feedback files for a PR.
2. Convert those files into a pending GitHub review with inline comments on the correct lines.

The workflow intentionally keeps final submission manual so the reviewer can inspect and edit in the browser before clicking `Request changes`.

## Decisions already locked

- [x] Use a two-step process, not one-shot auto-submit.
- [x] Keep generated feedback as a folder of markdown files (`00`, `01+`, etc).
- [x] Use Python for core posting logic.
- [x] Use a thin JS wrapper only because OpenCode custom tools must be JS/TS.
- [x] Post only inline issue files (`01+`) when drafting comments.
- [x] Keep `00-summary.md` and any `comment_type: general` files for manual final summary.
- [x] Create draft reviews in `PENDING` state only (private to reviewer until submission).

## Scope

### In scope
- [x] Add a "generate" mode that creates split review files in `pr-reviews/<name>/`.
- [x] Add a "draft" mode that posts `01+` files as pending inline review comments.
- [x] Validate frontmatter, file mappings, and line anchors before posting.
- [x] Support dry-run previews before any API write.
- [x] Keep command UX simple and repeatable.

### Out of scope (v1)
- [ ] Auto-submitting review events (`REQUEST_CHANGES`, `COMMENT`, `APPROVE`).
- [ ] Auto-posting general comments from `00`/`20`/`21` files.
- [ ] Full bidirectional sync between local files and existing draft comments.
- [ ] Cross-platform path translation beyond normal POSIX paths.

## Architecture

### Components
- [x] `commands/pr-review-generate.md` (LLM-driven generation command).
- [x] `skills/pr-review-split-format/SKILL.md` (format and quality rules for generation).
- [x] `tools/pr_review_draft.py` (Python posting engine).
- [x] `tools/pr-review-draft.js` (OpenCode tool wrapper around Python).
- [x] `commands/pr-review-draft.md` (command to invoke draft tool).

### Why this split
- [x] Generation is best handled by the model with explicit formatting rules.
- [x] Draft posting is deterministic and should be handled by a strict script.

## Step 1: Generate mode design

### Inputs
- [ ] PR number (required).
- [ ] Optional review slug/name (if omitted, derive from PR title).

### Output folder contract
- [ ] Create: `pr-reviews/<pr-number>-<slug>/`.
- [ ] Include:
  - [ ] `00-summary.md`
  - [ ] `01-<issue>.md`
  - [ ] `02-<issue>.md`
  - [ ] ...
- [ ] One issue per file for `01+` files.
- [ ] Keep numbering stable and gapless.

### Generation behavior
- [ ] Inspect PR diff and changed files with `gh pr view --json files,headRefOid,baseRefName,headRefName,url`.
- [ ] Produce comments that are actionable and line-specific where possible.
- [ ] Include line number and context in frontmatter for inline comments.
- [ ] Mark non-inline feedback as `comment_type: general`.
- [ ] Prioritize blockers first (build failures, correctness, safety-critical misstatements).

### Generation quality rules (in skill)
- [ ] Avoid duplicate issues across files.
- [ ] Keep each body copy-paste ready for GitHub review comments.
- [ ] Keep tone direct and reviewer-friendly.
- [ ] Prefer factual claims tied to file context.
- [ ] Avoid invented line numbers; use actual diff anchors.

## Step 2: Draft mode design

### Inputs
- [ ] PR number (required).
- [ ] Feedback folder path (required).
- [ ] `--dry-run` (default true).
- [ ] `--apply` to post.
- [ ] `--replace-pending` (default true).

### Parsing and filtering
- [ ] Read all `*.md` in feedback folder.
- [ ] Sort by numeric prefix.
- [ ] Skip `00-summary.md`.
- [ ] Skip files with `comment_type: general`.
- [ ] Keep only inline records with required metadata.

### Required frontmatter for inline files
- [ ] `comment_type: inline`
- [ ] `target_file`
- [ ] `line_start`
- [ ] `line_end`
- [ ] `context`

### File mapping rules
- [ ] Exact path match first.
- [ ] Unique suffix match second (example: `intro.md` maps to changed full path).
- [ ] Fail if ambiguous and print candidates.
- [ ] Fail if no mapping exists in current PR diff.

### Comment payload rules
- [ ] Use `path` (resolved changed file path).
- [ ] Use `line` from `line_start`.
- [ ] Use `side: RIGHT`.
- [ ] Use markdown body exactly from file content.
- [ ] v1 assumes single-line inline comments.

### Review lifecycle rules
- [ ] If `--replace-pending` is enabled, delete current reviewer's existing pending reviews first.
- [ ] Create one pending review with all inline comments (`POST /pulls/{pr}/reviews`, no `event`).
- [ ] Return `review_id`, posted count, and PR URL.
- [ ] Never submit review event from the script.

## File format contract

### Example inline issue file (`01+`)

```md
---
pr: 562
comment_type: inline
target_file: iso26262.md
line_start: 29
line_end: 29
context: "possible e.g. Option'<T'>, Result<T, E>"
---

The apostrophes in `Option'<T'>` break MDX parsing.
Suggested fix: use backticks around generic types.
```

### Example summary/general file

```md
---
pr: 562
comment_type: general
target_file: null
line_start: null
line_end: null
context: "Overall review summary"
---

High-level assessment for manual final review body.
```

## Command UX

### Generate step
- [ ] `/pr-review-generate 562`
- [ ] `/pr-review-generate 562 safety-assessor-green-yellow-red`

### Draft step
- [ ] `/pr-review-draft 562 $OPENCODE_CONFIG_DIR/pr-reviews/562-safety-assessor-green-yellow-red --dry-run`
- [ ] `/pr-review-draft 562 $OPENCODE_CONFIG_DIR/pr-reviews/562-safety-assessor-green-yellow-red --apply`

## Operator runbook (OpenCode)

Use this exact sequence after implementation is complete.

- [ ] If slash commands are not discovered, restart OpenCode once.
- [ ] Run generation:
  - [ ] `/pr-review-generate 562 safety-assessor-green-yellow-red`
- [ ] Run draft preview (no API write):
  - [ ] `/pr-review-draft 562 $OPENCODE_CONFIG_DIR/pr-reviews/562-safety-assessor-green-yellow-red --dry-run`
- [ ] Run draft apply (create pending review comments):
  - [ ] `/pr-review-draft 562 $OPENCODE_CONFIG_DIR/pr-reviews/562-safety-assessor-green-yellow-red --apply`
- [ ] Open PR in browser and verify pending comments:
  - [ ] `gh pr view 562 --web`
- [ ] Manually add final summary from `00-summary.md` and submit `Request changes` when ready.

### Runbook expectations
- [ ] `--dry-run` must show exactly which `01+` files will be posted.
- [ ] `00-summary.md` and `comment_type: general` files must not be auto-posted.
- [ ] Apply step must create a `PENDING` review only (no auto-submit event).

## Python CLI contract

- [x] `python3 tools/pr_review_draft.py --pr <number> --feedback-dir <path> [--dry-run|--apply] [--replace-pending|--no-replace-pending] [--repo owner/name]`
- [ ] Exit codes:
  - [x] `0` success
  - [x] `2` input/frontmatter validation failure
  - [x] `3` GitHub API/auth failure
  - [x] `4` path or anchor resolution failure

## Validation checklist

### Local checks
- [x] Verify `python3`, `gh`, and `PyYAML` availability.
- [x] Run draft step in dry-run mode and inspect payload preview.
- [x] Confirm only `01+` inline files are queued for posting.

### Integration checks
- [ ] Run draft step with `--apply` on a test PR.
- [ ] Open PR in browser and confirm all comments are in pending review state.
- [ ] Confirm comments are visible only to reviewer before submission.
- [ ] Confirm summary/general files were not auto-posted.

### Negative-path checks
- [ ] Missing frontmatter key produces clear file-specific error.
- [ ] Ambiguous `target_file` produces candidate list.
- [ ] Invalid line anchor surfaces actionable API error.
- [ ] Empty inline comment body is rejected.

## Safety and reliability requirements

- [ ] Do not expose credentials or tokens in output.
- [ ] Do not submit or finalize reviews automatically.
- [ ] Keep apply behavior idempotent with `--replace-pending` default.
- [ ] Preserve source markdown bodies as posted text.
- [ ] Log source filename for each comment in dry-run and apply outputs.

## Risks and mitigations

- [ ] Risk: line anchors drift after new commits.
  - [ ] Mitigation: validate against current PR head and fail with clear remediation.
- [ ] Risk: ambiguous filename suffixes.
  - [ ] Mitigation: fail-fast and require explicit `target_file` path.
- [ ] Risk: duplicate pending drafts from reruns.
  - [ ] Mitigation: remove current reviewer's pending drafts by default.
- [ ] Risk: over-generation (too many weak comments).
  - [ ] Mitigation: enforce quality rules in generation skill and keep one issue per file.

## Acceptance criteria

- [ ] Reviewer can run generate step and get a structured folder (`00`, `01+`) with valid frontmatter.
- [ ] Reviewer can run draft step to create one pending review from `01+` inline files only.
- [ ] Posted comments appear on correct files/lines in GitHub pending review UI.
- [ ] `00-summary.md` and general comments remain manual.
- [ ] No automatic review submission occurs.
- [ ] Re-running draft with defaults replaces existing pending draft cleanly.

## Rollout checklist

- [x] Implement generation command and format skill.
- [x] Implement Python drafting script.
- [x] Implement JS wrapper tool.
- [x] Implement drafting command.
- [x] Dry-run on PR 562 feedback folder.
- [ ] Apply on PR 562 and verify pending comments.
- [x] Document normal reviewer workflow in a short usage note.

## Handoff notes

- [ ] Always run generate first, then review/edit local files if needed.
- [ ] Always run draft with `--dry-run` before `--apply`.
- [ ] Do final summary and `Request changes` manually in GitHub UI.
