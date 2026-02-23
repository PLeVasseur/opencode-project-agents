# Diffset HTML Review Feedback Loop Plan

This plan adds a first-class diffset review flow so a reviewer can inspect changes quickly, leave structured feedback, and iterate until sign-off.

## Execution status (2026-02-18)

- [x] Implemented diffset schemas, builder, HTML review UI, review server, and browser auto-open command.
- [x] Implemented tracked feedback persistence plus report/reconcile/review-gate commands.
- [x] Integrated review gate into docs and CI, and added unit/smoke tests.

## 0) Goals and guardrails

- [ ] Add a single command that builds a diffset and opens a review page in the browser automatically.
- [ ] Keep review artifacts deterministic and reproducible from `before_run` + `after_run`.
- [ ] Make reviewer feedback structured, machine-readable, and easy to carry into the next run.
- [ ] Keep the first version local-first (no external service required).
- [ ] Keep volatile review bundles in `.cache/`; keep durable review decisions in tracked `feedback/` files.

## 1) Diffset contract and schemas

- [ ] Add `schemas/diffset_manifest.schema.json`.
- [ ] Add `schemas/diffset_item.schema.json` (for JSONL row shape).
- [ ] Add `schemas/diffset_review.schema.json`.
- [ ] Extend `scripts/validate_schemas.py` to validate tracked review files in `feedback/diffset_reviews/`.

### Required diffset bundle layout

- [ ] Write bundle to `.cache/reviews/diffsets/<diffset_id>/`.
- [ ] Include:
  - [ ] `manifest.json`
  - [ ] `items.jsonl`
  - [ ] `summary.md`
  - [ ] `review.html`
  - [ ] `review_state.json` (latest saved review state for local session continuity)

### Diffset item fields (minimum)

- [ ] `item_id` (stable across reruns when the underlying change is the same).
- [ ] `entity_type` (`guideline|category|coverage|scope|gate`).
- [ ] `change_type` (`added|removed|modified|unchanged-context`).
- [ ] `path_hint` (where this change belongs, such as `data/todo_guidelines.yaml`).
- [ ] `before_value` and `after_value` (small payload slices; avoid large text dumps).
- [ ] `severity_hint` (`info|warn|high`).
- [ ] `context` (seed IDs, guideline ID, category, evidence path, etc.).

## 2) Diffset builder implementation

- [ ] Add `scripts/build_diffset.py`.
- [ ] Inputs:
  - [ ] `--after-run <run_id>` (required)
  - [ ] `--before-run <run_id>` (optional; default to accepted baseline from `data/run_registry.yaml`)
  - [ ] `--output-root .cache/reviews/diffsets`
- [ ] Build diffs for:
  - [ ] `data/guideline_categories.yaml`
  - [ ] `data/todo_guidelines.yaml`
  - [ ] `data/coverage_matrix.csv`
  - [ ] `data/target_scope.yaml`
  - [ ] gate outcomes from run manifests/reports
- [ ] Emit deterministic ordering and stable `item_id` generation.
- [ ] Generate reviewer summary (`summary.md`) with counts by entity and severity.

## 3) HTML review UI (MVP)

- [ ] Generate a self-contained `review.html` in each diffset bundle.
- [ ] Include filter controls for:
  - [ ] `entity_type`
  - [ ] `change_type`
  - [ ] `severity_hint`
  - [ ] free-text search (ID/text/context)
- [ ] Show list + details pane:
  - [ ] compact rows for scan speed
  - [ ] expanded before/after details
  - [ ] links to relevant file paths and IDs
- [ ] Include per-item review actions:
  - [ ] `accept`
  - [ ] `needs_change`
  - [ ] `block`
  - [ ] reviewer comment field
- [ ] Include top-level counters for accepted/pending/blocking items.

## 4) Review command and automatic browser launch

- [ ] Add `scripts/review_diffset.py` as the primary command.
- [ ] Command behavior:
  - [ ] build (or load) diffset
  - [ ] start lightweight localhost server for the active diffset
  - [ ] open browser automatically unless `--no-open`
  - [ ] print the URL always for manual fallback
- [ ] Browser launch behavior:
  - [ ] default: Python `webbrowser.open(url)`
  - [ ] fallback: platform launcher (`xdg-open`/`open`/`start`) when needed
  - [ ] fail-soft: if launch fails, keep server running and print instructions
- [ ] Useful flags:
  - [ ] `--port <n>`
  - [ ] `--host 127.0.0.1`
  - [ ] `--no-open` (CI/headless)
  - [ ] `--once` (build + print URL + exit, no long-running server)

### Example operator command

- [ ] `uv run python scripts/review_diffset.py --after-run <run_id>`
- [ ] Expected UX: command prints and opens `http://127.0.0.1:<port>/` directly in browser.

## 5) Feedback persistence and iteration loop

- [ ] Save tracked review decisions to `feedback/diffset_reviews/<diffset_id>.yaml`.
- [ ] Review entry fields (minimum):
  - [ ] `diffset_id`
  - [ ] `reviewer`
  - [ ] `reviewed_at`
  - [ ] `items[]` with `item_id`, `verdict`, `comment`, `status`
- [ ] Add `scripts/review_feedback_report.py` to summarize open blockers/needs-change items.
- [ ] Add optional `scripts/reconcile_diffset_feedback.py` to map prior feedback onto a new diffset and mark resolved items.

## 6) Promotion gate integration

- [ ] Update docs to require no unresolved `block` feedback before promotion.
- [ ] Add a policy check command:
  - [ ] `uv run python scripts/check_diffset_review_gate.py --diffset-id <id>`
- [ ] Integrate review gate into promotion workflow docs and CI (when diffset exists).

## 7) Tests and quality checks

- [ ] Add unit tests for stable `item_id` generation.
- [ ] Add tests for diff classification (`added/removed/modified`).
- [ ] Add test for feedback serialization/deserialization schema compliance.
- [ ] Add smoke test for `review_diffset.py --no-open --once` command path.

## 8) Phased commit strategy (Conventional Commits)

- [ ] Phase A: schemas and data contracts.
  - [ ] Suggested commit: `feat(diffset): add schemas for manifest items and reviews`.
- [ ] Phase B: diffset builder and summary generation.
  - [ ] Suggested commit: `feat(diffset): build deterministic review bundles from run pairs`.
- [ ] Phase C: HTML review page rendering and filtering.
  - [ ] Suggested commit: `feat(review-ui): add local html diffset reviewer`.
- [ ] Phase D: review server and browser auto-open command.
  - [ ] Suggested commit: `feat(review-cli): serve diffset and open browser automatically`.
- [ ] Phase E: feedback persistence and review gate check.
  - [ ] Suggested commit: `feat(review-gates): persist feedback and enforce blocker policy`.
- [ ] Phase F: docs and operator workflow updates.
  - [ ] Suggested commit: `docs(review): document diffset review and sign-off flow`.

## 9) Definition of done

- [ ] Running one command builds a diffset and opens the review page in the browser.
- [ ] Reviewer can filter, inspect diffs, and record per-item verdicts/comments.
- [ ] Feedback is saved in a tracked file under `feedback/diffset_reviews/` and schema-valid.
- [ ] A follow-up command can report unresolved blocking feedback.
- [ ] Promotion workflow references the diffset review gate.
- [ ] Local quality checks and CI pass with the new diffset/review workflow.
