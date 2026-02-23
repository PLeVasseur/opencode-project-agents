# PR-32 Remediation Concerns (Pre-Execution)

Date: 2026-02-14
Context: concerns identified while reviewing `plans/pr-32-multi-pr-feedback-remediation-plan.md`

## 1) Constraint conflict: single-touch files vs per-commit compilability

### Concern

The remediation targets two strong constraints at once:

1. Each file should reach final state in exactly one commit (except explicit exceptions like `Cargo.lock`).
2. Every commit should compile (`cargo check --workspace --all-targets`).

For this refactor shape, those constraints can conflict in early extraction commits. In practice, module extraction can require temporary top-level wiring updates to compile, but those updates often touch files that are supposed to be finalized later.

### Risk if not handled explicitly

- Accidental re-touching of previously finalized files to fix compile failures.
- Reintroduction of reviewer pain (diff-of-diffs across the same files).
- Last-minute commit surgery that undermines confidence and traceability.

### Recommended policy (lock before execution)

- Keep both constraints as hard goals.
- If a compile fix would require re-touching files already finalized in earlier commits, prefer **collapsing adjacent commit boundaries** rather than re-touching files.
- Preserve isolation for naturally independent scopes (`observability/`, tests-only, benchmark harness, smoke suite).
- Record any collapse decision in the report with:
  - reason for conflict,
  - files that would otherwise be re-touched,
  - resulting revised commit boundary.

## 2) Overlap proof is currently end-loaded

### Concern

The plan currently proves "no file overlap across commits" at the end of the stack rebuild. That catches violations too late.

### Risk if checked only at phase end

- A single accidental overlap (for example, a tiny whitespace follow-up in a file from an earlier commit) can force broad rework.
- Debug/rewrite time is spent after all commits are already built.

### Recommended guardrail (fail fast)

After each reconstructed commit:

1. Capture current commit file list.
2. Compare with cumulative prior-commit file set.
3. Fail immediately on overlap not in allowlist.
4. Fix boundary at once before creating the next commit.

Keep the final end-of-phase overlap report as confirmation, not first detection.

## 3) Stacked PR operational risk (manageable)

### Concern

PR B and PR C are intentionally based on PR A. If PR A changes during review, B/C may need refresh/rebase/cherry-pick updates.

### Mitigation

- Treat PR A as the stabilization anchor.
- Avoid force-updating PR B/C until PR A review stabilizes.
- If PR A changes, regenerate B/C from the updated anchor with explicit report notes.

## 4) Commit-body quality is now a gating quality signal

### Concern

The feedback explicitly calls out missing commit bodies. Weak or mechanical bodies would leave the core reviewer concern unresolved.

### Mitigation

Require each commit body to include:

- what changed,
- why this boundary exists,
- key review files,
- whether changes are behavioral or mechanical.

## Recommended defaults to proceed

- Adopt boundary-collapse policy when single-touch vs compile constraints conflict.
- Add per-commit fail-fast overlap gate (not just final overlap audit).
- Keep stacked PR topology (A architecture, B benchmark, C smoke), with A as anchor.
