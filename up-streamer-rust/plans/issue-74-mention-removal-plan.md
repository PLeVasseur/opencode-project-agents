# Issue-74 Mention Removal Plan

## Goal

- [x] Remove issue-specific wording (`Issue #74`, `issue-74`, `issue_74`, `issue74`) from repo docs and code/tests where it is not needed for long-term maintenance.
- [x] Preserve behavior; this is a naming/docs cleanup only.

## Scope Confirmed So Far

- [x] `configurable-streamer/README.md`
  - [x] Remove the full section `## Issue #74 runbook (left-side/topic authority enforcement)`.
  - [x] Remove all runbook-local references like `issue-74`, `ISSUE74_DIR`, and `subscription_data.issue74.json`.
- [x] `up-streamer/src/ustreamer.rs`
  - [x] Rename test functions to issue-agnostic names.
  - [x] Replace test-only forwarding ID string literal `"issue-74"` with a neutral value.

## Execution Steps

- [x] Step 1: Reconfirm current matches before editing.
  - [x] Run: `rg -n --hidden --glob '!.git/*' -e 'Issue #74|issue #74|issue-74|issue_74|issue74|ISSUE74'`
  - [x] Save the baseline list in working notes (for review traceability).

- [x] Step 2: Remove issue-specific runbook from `configurable-streamer/README.md`.
  - [x] Delete from the `## Issue #74 runbook...` header through the line before `### Client-Service Setups`.
  - [x] Ensure README flow still reads cleanly from setup intro into client/service and pub/sub sections.

- [x] Step 3: Make test naming neutral in `up-streamer/src/ustreamer.rs`.
  - [x] Rename:
    - [x] `issue_74_publish_filter_respects_topic_authority` -> `publish_filter_respects_topic_authority`
    - [x] `issue_74_publish_filter_allows_left_wildcard` -> `publish_filter_allows_left_wildcard`
    - [x] `issue_74_publish_filter_blocks_unmapped_authority` -> `publish_filter_blocks_unmapped_authority`
    - [x] `issue_74_unregistration_removes_publish_filters` -> `unregistration_removes_publish_filters`
  - [x] Replace all test-only `"issue-74"` forwarding IDs with a neutral string (example: `"test-forwarding"`).

- [x] Step 4: Validate cleanup and behavior.
  - [x] Run mention scan again:
    - [x] `rg -n --hidden --glob '!.git/*' -e 'Issue #74|issue #74|issue-74|issue_74|issue74|ISSUE74'`
  - [x] Run focused tests:
    - [x] `cargo test -p up-streamer publish_filter -- --nocapture`
    - [x] `cargo test -p up-streamer unregistration_removes_publish_filters -- --nocapture`
  - [x] Optional style check for touched file:
    - [x] `cargo fmt -- --check`

## Non-Goals

- [x] Do not change forwarding semantics, transport behavior, or subscription matching logic.
- [x] Do not alter branch names, git metadata, or external issue/PR history text.

## Handoff

- [x] Provide a short diff summary listing exactly what mentions were removed and where.
- [ ] If requested, prepare a small follow-up commit and update PR `#77` with this docs/test naming cleanup.
