# Revised Feedback on PR6 V2 Remediation Plan

## Overall Assessment

The plan is well-structured and execution-ready. The policy framing, gating model, wave structure, and audit controls are solid. The feedback below covers the specific areas where adjustments would strengthen execution.

## What's Good — No Changes Needed

The following aspects of the plan are correct as written:

- **Stage/Wave structure and ordering.** Wave A as 15 foundational terms, small and decisive, is the right call.
- **Conceptual-home-first policy** as the governing principle.
- **Ledger schema with full traceability.** The 16-field schema across identity/before/action/after/status is appropriate for the level of rigor this work requires. Every term needs concrete before/after anchors and substantive rationale — this is specification text, and the audit trail must hold up to scrutiny. The `reason_why >= 80 chars` requirement is right; if a term doesn't warrant 80 characters of rationale, the decision probably wasn't thought through carefully enough.
- **Manual term adjudication for all waves.** This is a specification, not a codebase refactor. Every `:dt:` placement and every definition rewrite changes what the FLS says. Scripted or semi-automated approaches risk introducing subtle semantic errors that are harder to catch in review than to prevent upfront. Manual adjudication for all waves is the correct constraint.
- **Closure thresholds and acceptance criteria.**
- **Rescope checkpoint as mandatory before Waves C/D.**
- **Reporting streamlined to ledger + one summary report.**

## Adjustments Recommended

### 1. Batch Failure Protocol — Allow Partial Completion

The current protocol says: "Rollback run-local checklist/ledger to batch snapshot, discard partial code edits for failed batch." For Waves C/D at 40–50 terms per batch, a single problematic term shouldn't nuke 49 good changes.

**Recommendation:** Allow partial batch completion. When a batch fails validation, quarantine the failing term(s), commit the passing ones, and carry failures forward into the next batch. Persist a `batch-<n>-partial.json` alongside the failure record that documents which terms passed and which were quarantined. This preserves the audit trail while avoiding wasteful rework.

### 2. Per-Wave Pattern Document — Not Just Wave A

The plan should include a short pattern document after *each* wave, not just implicitly after Wave A. After each wave completes, write a half-page document that codifies the decision patterns that emerged during that wave. For example:

- **After Wave A:** "Terms named after their chapter go to the chapter's opening section. Terms named after a specific construct go to that construct's section. Displaced `:dt:` becomes `:t:` with no forward-reference annotation unless the displaced site is more than 2 sections away."
- **After Wave B:** Patterns around high/medium priority terms — which analyzer recommendations were followed, which were overridden and why.
- **After Wave C:** Patterns around definition rewrites — common sentence structures that worked, pitfalls encountered with inline definitions.
- **After Wave D:** Residual placement patterns and forward-reference mitigation approaches.

These documents accumulate into a lightweight decision framework that serves both as execution guidance and as reviewer context. Store them at `$REMEDIATION_DIR/waves/wave-<x>-patterns.md`.

### 3. Separate "Move" and "Rewrite" Actions in the Ledger

The current `decision` field conflates two fundamentally different operations:

- **Moves** (relocating a `:dt:` from one file/section to another without changing the definition text) — these are mechanical and low-risk.
- **Rewrites** (changing the definition text to make it standalone, contextually appropriate, or glossary-aligned) — these change specification semantics and are high-risk.

**Recommendation:** Split the `decision` field into `action_type` (one of: `move`, `rewrite`, `move+rewrite`, `retain`, `retain+rewrite`) and `decision_detail`. This allows a reviewer to quickly batch-approve 30 pure moves and spend review time on the 10 rewrites that actually change specification text.

### 4. Rescope Checkpoint Should Trigger a V3 Analysis

The rescope checkpoint after Waves A/B should not be an eyeball assessment of residual counts. Instead, pause execution after Waves A/B and request a fresh v3 analysis using the same methodology as v2 (placement fitness + definition divergence). This provides:

- Authoritative before/after numbers with no ambiguity.
- Detection of any regressions introduced by the moves.
- Precise scoping data for Waves C/D — specifically, how many of the 160 low-reliability divergence terms cascaded to acceptable without direct intervention.
- A concrete diff against the v2 baseline that demonstrates Wave A/B impact.

**Concretely:** After Waves A and B are committed, stop execution and request the v3 analysis. Do not proceed to Waves C/D until the v3 results are reviewed and Wave C/D scopes are frozen based on actual measured residuals rather than estimates.

Add this to the rescope checkpoint section as a hard gate:

> **Gate B+ (rescope):** V3 analysis requested and received. Wave C/D scopes frozen based on v3 residuals. No Wave C/D execution until rescope gate passes.

### 5. Risk Register Addition — Definition Authoring Quality

The risk register doesn't mention the biggest practical risk of this remediation: **definition rewrite quality**. The hardest part of Wave C isn't moving terms — it's rewriting "Procedural macros shall be defined in a `:dt:`crate` subject to attribute crate_type..." into a standalone definition that matches glossary intent while fitting its new paragraph context. Bad rewrites could introduce semantic inaccuracies into the specification.

**Recommended addition to risk register:**

> - Risk: definition rewrites introduce semantic inaccuracy into specification text.
>   - Mitigation: separate move and rewrite actions in ledger for differentiated review. Flag any rewrite that changes semantic content (not just location) for explicit review attention.

## Summary of Recommended Changes

| # | Area | Change |
|---|------|--------|
| 1 | Batch failure protocol | Allow partial completion; quarantine failing terms instead of full rollback |
| 2 | Pattern documents | Produce per-wave pattern document, not just after Wave A |
| 3 | Ledger `decision` field | Split into `action_type` + `decision_detail` to separate moves from rewrites |
| 4 | Rescope checkpoint | Hard gate: request v3 analysis after A/B, freeze C/D scope from v3 residuals |
| 5 | Risk register | Add definition authoring quality risk with move/rewrite separation as mitigation |
