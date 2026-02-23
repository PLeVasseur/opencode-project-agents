# PR 84 Benchmark Guardrail Clarity Follow-up Plan

Date: 2026-02-19
Status: ready-for-execution
Target PR: #84 (`bench: criterion harness and guardrail crate (c4)`)
Target branch: `cleanup/refactor-upstream-main-prB-benchmark`

## Objective

Address review feedback that the Criterion guardrail purpose is unclear by improving in-repo documentation first, then updating the PR description, then responding in-thread with a concise and objective rationale.

## Why this plan exists

- [ ] Ensure we respond constructively and non-defensively.
- [ ] Make rationale obvious without forcing reviewers to reverse-engineer code.
- [ ] Keep changes scoped to clarity/communication unless a real logic issue is discovered.

## Scope

### In scope

- [ ] Clarify guardrail intent, behavior, and non-goals in repository docs.
- [ ] Tighten terminology (especially `alloc_proxy`) and explain threshold mapping.
- [ ] Improve PR #84 summary/body so reviewers can understand "why" quickly.
- [ ] Post a clear review response acknowledging feedback and linking to the clarifications.

### Out of scope

- [ ] No benchmark algorithm redesign.
- [ ] No threshold value changes (3/5/5) unless a correctness bug is found.
- [ ] No CI mode promotion from advisory to required in this pass.
- [ ] No unrelated refactors or feature changes.

## Execution order (locked)

- [x] 1) Docs in repo
- [x] 2) PR summary/body update
- [x] 2.5) User checkpoint: review docs + PR summary updates
- [ ] 3) Reviewer response

## Phase 0 - Preflight and guardrails

- [x] Confirm we are on the PR B branch before editing:
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] If needed: `git checkout cleanup/refactor-upstream-main-prB-benchmark`
- [x] Capture working tree state:
  - [x] `git status --short --branch`
- [x] Re-open current PR feedback context:
  - [x] `gh pr view 84 --comments`
- [x] Keep scope narrow to files directly supporting clarity updates.

## Phase 1 - Repository documentation improvements (first)

### 1.1 Clarify purpose and positioning

- [x] Update `up-streamer/README.md` benchmark guardrail section to explicitly state:
  - [x] What the guardrail is for (machine-checkable regression gate for canonical hotspots).
  - [x] Why it exists (safe ergonomics/perf refactors with objective non-regression checks).
  - [x] What it is not (not a full macrobenchmark suite, not transport E2E performance proof).

### 1.2 Clarify metric semantics

- [x] Document benchmark ID groups and threshold semantics in plain language:
  - [x] Throughput-sensitive IDs/groups and 3% threshold.
  - [x] Latency-sensitive IDs/groups and 5% threshold.
  - [x] Allocation-proxy IDs and what "allocation proxy" means in this context.
- [x] Add concise explanation for how pass/fail is computed from baseline vs candidate.

### 1.3 Clarify local vs CI behavior

- [x] Explicitly document operating modes:
  - [x] Local: hard-fail on threshold breach.
  - [x] CI workflow: advisory mode with artifact upload.
- [x] Add pointer to advisory workflow file for discoverability.

### 1.4 CLI wording improvements (if needed)

- [x] Update `utils/criterion-guardrail/src/main.rs` `about` text to better describe intent.
- [x] Ensure help text remains concise but explicit about threshold evaluation role.

### 1.5 Script UX notes (if needed)

- [x] Review `scripts/bench_streamer_criterion.sh` usage text for clarity.
- [x] Add/adjust one-line usage wording only if it materially improves readability.

### 1.6 Validation for Phase 1 changes

- [x] `cargo fmt --all`
- [x] `cargo check -p criterion-guardrail --all-targets`
- [x] `cargo check -p up-streamer --benches`
- [x] Confirm no behavioral diffs beyond docs/help text.

### 1.7 Phase 1 acceptance criteria

- [x] A reviewer can answer in under 1 minute:
  - [x] What guardrail does.
  - [x] Why we need it in this PR.
  - [x] How local and CI behavior differ.

## Phase 2 - PR summary/body update (second)

### 2.1 Rewrite structure for fast review

- [x] Update PR #84 body with explicit sections:
  - [x] `Why`
  - [x] `What this adds`
  - [x] `What this does not do`
  - [x] `How to run locally`
  - [x] `CI mode (advisory)`

### 2.2 Keep claims aligned with code/docs

- [x] Ensure PR text references actual files and behavior only.
- [x] Avoid speculative or defensive language.
- [x] Keep wording objective and reviewer-oriented.

### 2.3 PR body acceptance criteria

- [x] Guardrail rationale is understandable without opening source files.
- [x] Non-goals are explicit to reduce scope confusion.
- [x] Validation commands remain accurate and reproducible.

### 2.4 Mandatory user review checkpoint (before any reviewer reply)

- [x] Prepare a concise delta summary for user review including:
  - [x] Repo documentation files changed.
  - [x] Exact PR #84 body sections added/updated.
  - [x] Any wording decisions that could be interpreted differently.
- [x] Pause execution before drafting/posting reviewer response.
- [x] Request user approval on docs + PR body updates.
- [x] Proceed to Phase 3 only after explicit user go-ahead.

## Phase 3 - Review-thread response (third)

### 3.1 Response content

- [ ] Reply directly to the feedback comment and acknowledge the confusion plainly.
- [ ] Provide a short rationale in plain language (what/why).
- [ ] Point to specific updated docs/PR sections.
- [ ] Invite follow-up questions on remaining unclear points.

### 3.2 Tone and communication guardrails

- [ ] No defensiveness.
- [ ] No over-justification.
- [ ] No blame-shifting to reviewer context.
- [ ] Focus on improved clarity and reviewer ergonomics.

### 3.3 Response acceptance criteria

- [ ] Reviewer can see both acknowledgement and concrete corrective action.
- [ ] Response is concise and technical, not argumentative.

## Phase 4 - Final hygiene and handoff

- [ ] Verify change scope:
  - [ ] `git diff --name-only`
  - [ ] Confirm only intended docs/help text/PR metadata changed.
- [ ] Summarize results for handoff:
  - [ ] What was clarified in repo docs.
  - [ ] What was clarified in PR body.
  - [ ] Exact reviewer reply posted.

## Risks and mitigations

- [ ] Risk: wording remains too abstract.
  - [ ] Mitigation: include one concrete baseline/candidate example flow.
- [ ] Risk: terminology mismatch between README and CLI.
  - [ ] Mitigation: verify shared terms before posting response.
- [ ] Risk: accidental scope creep into benchmark behavior.
  - [ ] Mitigation: block any non-clarity edits unless a correctness bug is found and documented.

## Done definition

- [ ] Repo docs clearly explain guardrail purpose, behavior, thresholds, and mode.
- [ ] PR #84 summary/body reflects that rationale and non-goals.
- [ ] Reviewer feedback thread has an objective, appreciative response with references.
- [ ] Validation commands for touched Rust/docs surfaces pass.
