# ISO 26262 Rust Mapping Critique Remediation Plan (Traceability-Aligned v2)

Date: 2026-02-14
Status: Draft execution plan (rewrite)
Priority: Execute after traceability foundation milestones

## 0) Locked alignment decisions
- [ ] This remediation plan is subordinate to and aligned with `plans/2026-02-14-iso26262-traceability-anchor-plan.md`.
  - [ ] Source-embedded correlation is canonical (no manual tracked mapping file layer).
  - [ ] Any remediation edit that introduces or changes statements must preserve traceability invariants.
  - [ ] Remediation closeout is blocked if traceability gates are not green.
- [ ] Statement-level source anchoring is mandatory.
  - [ ] Every statement in `src/iso26262_rust_mapping.md` has a stable `source_id`.
  - [ ] Every statement in `src/tables/table-*.yaml` has a stable `source_id` (row/cell scope as needed).
  - [ ] Every statement has `trace_status` (`mapped`, `unmapped_with_rationale`, `out_of_scope_with_rationale`) even when not linked to ISO.
  - [ ] For `trace_status=mapped`, at least one valid ISO anchor ID is required.
- [ ] Required final reporting is mandatory under `$OPENCODE_CONFIG_DIR/reports/`.
  - [ ] JSON report: what traced and what did not.
  - [ ] Markdown report: what traced, what did not, and remediation plan.

## 1) Outcomes and success criteria
- [ ] Address critique findings with assessor-ready evidence and reproducible updates.
  - [ ] All accepted critique items map to concrete edits.
  - [ ] All rejected items have explicit rationale and source evidence.
- [ ] Preserve and strengthen ISO/Rust correctness.
  - [ ] ISO claims trace to local licensed PDF anchors.
  - [ ] Rust claims trace to normative Rust documentation anchors.
- [ ] Keep full-document traceability stable during and after remediation.
  - [ ] No statement loses `source_id` due to edits/reorder/reflow.
  - [ ] No duplicate or malformed `source_id` values.
  - [ ] No unknown anchor IDs referenced by source statements.

## 2) Scope
- [ ] In scope.
  - [ ] `src/iso26262_rust_mapping.md` narrative and section structure.
  - [ ] `src/tables/table-01.yaml` ... `src/tables/table-26.yaml`.
  - [ ] New tables added by remediation (if required).
  - [ ] Supporting traceability metadata embedded in markdown and YAML.
  - [ ] Build/verify flow and report outputs needed for acceptance.
- [ ] Out of scope (unless explicitly pulled in by dependency).
  - [ ] Reauthoring ISO hierarchy model itself (handled by traceability plan).
  - [ ] Non-remediation feature work unrelated to critique findings.

## 3) Preconditions (must be met before substantive remediation)
- [ ] Traceability dependency readiness.
  - [ ] Traceability plan has established source-embedded correlation contracts.
  - [ ] Source ID generation/reconciliation tooling is available.
  - [ ] Source/anchor integrity validators are available.
- [ ] Source corpus readiness.
  - [ ] Local PDFs present in `.cache/iso26262/` and checksums captured.
  - [ ] Relevant Rust references identified and linkable.
- [ ] Resumable execution readiness.
  - [ ] Run root and state/checklist files initialized.
  - [ ] Lock discipline and atomic state updates confirmed.

## 4) Branch and commit strategy
- [ ] Branching.
  - [ ] Create and use `docs/iso26262-critique-remediation`.
  - [ ] Keep generated `build/*` artifacts untracked.
- [ ] Commit phasing (Conventional Commits).
  - [ ] `docs(structure): replace internal review notes with normative backbone`
  - [ ] `docs(iso26262): strengthen clause fidelity and decomposition/interference coverage`
  - [ ] `docs(language): correct Rust language classifications and missing constructs`
  - [ ] `docs(library): deepen core/std hazard taxonomy and policy granularity`
  - [ ] `docs(tooling): add TI/TCL framing and supply-chain/tool limits`
  - [ ] `docs(verification): align profile behavior and verification coherence`
  - [ ] `feat(traceability): reconcile statement-level source IDs and trace metadata`
  - [ ] `docs(report): add remediation traceability coverage reports`

## 5) Durable execution contract (crash-safe)
- [ ] Use resumable skill discipline for the remediation run.
  - [ ] Run root: `$OPENCODE_CONFIG_DIR/reports/critique-remediation-<run-id>/`.
  - [ ] Files: `state.env`, `checklist.state.env`, `run.log`, `artifacts/`.
  - [ ] Lock file required for single-writer execution.
  - [ ] Use `reports/tooling/state_tool.py` for all state/checklist updates.
- [ ] Immutable run contract.
  - [ ] Persist `RUN_ID`, `TASK_NAME`, `RUN_ROOT`, `REPO_ROOT`, `PLAN_PATH`.
  - [ ] Persist `TARGET_BRANCH`, `BASE_PIN_SHA`, `EXPECTED_OLD_REMOTE_SHA`.
  - [ ] Persist traceability dependency pointer and expected readiness gate.
- [ ] Resume rules.
  - [ ] Resume from earliest incomplete stage.
  - [ ] If stage done but checklist incomplete, resume same stage.
  - [ ] If push state unknown, reconcile remote SHA first.
  - [ ] If finalization partially complete, resume closeout only.

## 6) Stage map (critique remediation)
- [ ] `CR0` Bootstrap and contracts.
  - [ ] Initialize run files and lock.
  - [ ] Record immutable contract and dependency pointers.
- [ ] `CR1` Critique claim normalization.
  - [ ] Convert critique into claim-by-claim ledger with dispositions.
  - [ ] Link each claim to target file/section/table locations.
- [ ] `CR2` Structural backbone rewrite.
  - [ ] Restructure section flow and governance to match assessor expectations.
- [ ] `CR3` ISO fidelity corrections.
  - [ ] Apply ISO-content corrections and strengthen normative framing.
- [ ] `CR4` Rust language corrections.
  - [ ] Correct language-level classification and construct coverage.
- [ ] `CR5` Library inventory and hazard taxonomy corrections.
  - [ ] Refine `core`/`alloc`/`std` mappings and policy granularity.
- [ ] `CR6` Tooling and qualification corrections.
  - [ ] Expand TI/TCL, tool limits, and supply-chain controls.
- [ ] `CR7` Verification/profile coherence.
  - [ ] Align debug/release, coverage, and profile summaries.
- [ ] `CR8` Modified-file traceability reconciliation.
  - [ ] Reconcile all touched statements to stable source IDs and trace statuses.
  - [ ] Ensure no edited statement lacks required trace metadata.
- [ ] `CR9` Full-document statement instrumentation freeze.
  - [ ] Verify each and every statement in markdown and YAML is instrumented.
  - [ ] Run duplication/malformed/missing checks.
  - [ ] Reconcile movement/reflow without changing existing IDs.
- [ ] `CR10` Integrated validation gate.
  - [ ] Run traceability validators and build validators.
  - [ ] Run document validate/build/verify.
- [ ] `CR11` Reporting and remediation backlog.
  - [ ] Emit JSON+Markdown traceability remediation reports under `$OPENCODE_CONFIG_DIR/reports/`.
  - [ ] Record unresolved items with explicit remediation plans.
- [ ] `CR12` Closeout and handoff.
  - [ ] Write final disposition ledger and run summary.
  - [ ] Mark finalization flags and release lock.

## 7) Work packages by stage
- [ ] `CR1` Critique claim normalization.
  - [ ] Parse `feedback/iso26262_rust_mapping_critique.md` into atomic claims.
  - [ ] Assign claim IDs and disposition categories.
  - [ ] Record evidence requirements per claim.
  - [ ] Record target files and expected edits.
- [ ] `CR2` Structural backbone rewrite.
  - [ ] Update section structure in `src/iso26262_rust_mapping.md`.
  - [ ] Ensure governance/revision handling is explicit.
  - [ ] Ensure backbone methodology reflects language + library audit framing.
- [ ] `CR3` ISO fidelity corrections.
  - [ ] Add/strengthen Clause 6 coverage and language suitability framing.
  - [ ] Reconcile decomposition/interference/dependent-failure references.
  - [ ] Reconcile ISO table symbol interpretation language.
  - [ ] Update impacted tables with ISO-consistent logic.
- [ ] `CR4` Rust language corrections.
  - [ ] Correct keyword/macro/attribute classifications.
  - [ ] Add missing constructs (`closures`, `Drop` family, repr splits, etc.).
  - [ ] Reconcile build profile policy and language edge cases.
- [ ] `CR5` Library inventory and hazard taxonomy.
  - [ ] Refine collections and synchronization granularity.
  - [ ] Add missing APIs and hazardous escape-hatch handling.
  - [ ] Tighten method-level hazard procedure language.
- [ ] `CR6` Tooling and qualification.
  - [ ] Expand Section 12 TI/TCL framing and method expectations.
  - [ ] Add Miri limitations, crate governance, and LTO implications.
- [ ] `CR7` Verification/profile coherence.
  - [ ] Align guidance across Sections 6/7/8/10/11/13.
  - [ ] Ensure summary matrices reflect all introduced constructs and constraints.

## 8) Statement-level traceability instrumentation policy (strict)
- [ ] Markdown requirements (`src/iso26262_rust_mapping.md`).
  - [ ] Every heading statement has `source_id` and `trace_status`.
  - [ ] Every paragraph sentence has `source_id` and `trace_status`.
  - [ ] Every list/bullet statement has `source_id` and `trace_status`.
  - [ ] Every mapped statement includes valid ISO anchor IDs.
- [ ] YAML requirements (`src/tables/table-*.yaml`).
  - [ ] Every row statement has `source_id` and `trace_status`.
  - [ ] Every normative cell statement has `source_id` and `trace_status`.
  - [ ] Cell-level anchor refs are required when row-level refs are insufficient.
- [ ] Instrumentation stability requirements.
  - [ ] Preserve existing IDs during reorder/move.
  - [ ] Mint IDs only for new statements.
  - [ ] Detect and resolve duplicate IDs.
  - [ ] Prevent missing IDs from entering final state.
- [ ] Unmapped statement policy.
  - [ ] Allowed only with explicit rationale, owner, and remediation target stage.
  - [ ] Required unresolved count must be zero at final gate.

## 9) Validation and acceptance gates
- [ ] Content correctness gate.
  - [ ] Each accepted critique claim implemented or justified.
  - [ ] Each rejected claim includes clear rationale.
- [ ] Traceability integrity gate.
  - [ ] Every statement has `source_id` and `trace_status`.
  - [ ] Every mapped statement resolves to valid ISO anchor IDs.
  - [ ] No unknown anchors, no duplicate IDs, no malformed IDs.
- [ ] Build/doc gate.
  - [ ] `uv run python make.py validate` passes.
  - [ ] `uv run python make.py build` passes.
  - [ ] `uv run python make.py verify` passes.
  - [ ] `build/docx/iso26262_rust_mapping_generated.docx` exists.
- [ ] Reporting gate.
  - [ ] JSON traceability remediation report generated.
  - [ ] Markdown traceability remediation report generated.
  - [ ] Both reports include what traced, what did not, and remediation plan.

## 10) Required reports (under `$OPENCODE_CONFIG_DIR/reports/`)
- [ ] Run-scoped reports.
  - [ ] `$OPENCODE_CONFIG_DIR/reports/critique-remediation-<run-id>/critique-traceability-remediation-report.json`.
  - [ ] `$OPENCODE_CONFIG_DIR/reports/critique-remediation-<run-id>/critique-traceability-remediation-report.md`.
- [ ] Latest pointers.
  - [ ] `$OPENCODE_CONFIG_DIR/reports/critique-traceability-remediation-report-latest.json`.
  - [ ] `$OPENCODE_CONFIG_DIR/reports/critique-traceability-remediation-report-latest.md`.
- [ ] Report JSON minimum content.
  - [ ] `run_id`, `plan_path`, `generated_at_utc`.
  - [ ] `statement_counts` (`total`, `mapped`, `unmapped_with_rationale`, `out_of_scope_with_rationale`).
  - [ ] `by_file` and `by_section_or_table` breakdown.
  - [ ] `untraced_items[]` with reason and owner.
  - [ ] `remediation_actions[]` with priority and target stage.
- [ ] Report Markdown minimum content.
  - [ ] Executive summary.
  - [ ] What traced successfully.
  - [ ] What did not trace successfully.
  - [ ] Remediation thoughts and action plan.

## 11) Stage artifact checklist
- [ ] `CR0` artifacts.
  - [ ] `artifacts/bootstrap/contract.json`.
  - [ ] `artifacts/bootstrap/lock-state.log`.
- [ ] `CR1` artifacts.
  - [ ] `artifacts/claims/critique-claim-matrix.csv`.
  - [ ] `artifacts/claims/critique-disposition-draft.md`.
- [ ] `CR2`..`CR7` artifacts.
  - [ ] `artifacts/diffs/commit-<n>-working-diff.patch` for each commit stage.
  - [ ] `artifacts/evidence/<stage>-evidence.md` for rationale and references.
- [ ] `CR8` artifacts.
  - [ ] `artifacts/source/modified-files-trace-reconciliation.md`.
  - [ ] `artifacts/source/modified-files-missing-source-id.json`.
- [ ] `CR9` artifacts.
  - [ ] `artifacts/source/full-document-source-id-audit.json`.
  - [ ] `artifacts/source/full-document-trace-status-audit.json`.
  - [ ] `artifacts/source/source-id-reconciliation-log.md`.
- [ ] `CR10` artifacts.
  - [ ] `artifacts/verify/validate.log`.
  - [ ] `artifacts/verify/build.log`.
  - [ ] `artifacts/verify/verify.log`.
  - [ ] `artifacts/verify/traceability-validator-summary.json`.
- [ ] `CR11` artifacts.
  - [ ] Run-scoped JSON and Markdown remediation traceability reports.
  - [ ] `artifacts/disposition/unresolved-remediation-items.md`.
- [ ] `CR12` artifacts.
  - [ ] `artifacts/disposition/critique-disposition-ledger.md`.
  - [ ] `artifacts/summary.md` (resume and handoff details).

## 12) Risk register and mitigations
- [ ] Risk: edits introduce uninstrumented statements.
  - [ ] Mitigation: mandatory `CR8` and `CR9` stages with hard gates.
- [ ] Risk: statement reflow causes ID churn.
  - [ ] Mitigation: reconciliation tool preserving existing IDs and diff checks.
- [ ] Risk: anchor references drift during rapid edits.
  - [ ] Mitigation: source-anchor integrity validator at `CR10`.
- [ ] Risk: reports under-document unresolved traceability.
  - [ ] Mitigation: required report schema fields + markdown remediation section.
- [ ] Risk: long run interrupted.
  - [ ] Mitigation: durable state/checklist gating and lock discipline.

## 13) Prompt and new-session operations
- [ ] Use resumable execution prompt for this plan.
  - [ ] `prompts/execute-critique-remediation-resumable.md`.
  - [ ] Inputs: optional `RUN_ID`, optional `MAX_STAGES`.
  - [ ] Outputs: stage before/after, artifacts, blockers, exact resume instruction.
- [ ] New session startup checklist.
  - [ ] Verify `OPENCODE_CONFIG_DIR` and repository path.
  - [ ] Load specified run or newest incomplete run.
  - [ ] Validate immutable contract and lock status.
  - [ ] Resume at earliest incomplete safe stage.

## 14) Definition of done
- [ ] Critique remediation complete and evidence-backed.
  - [ ] Accepted claims implemented.
  - [ ] Rejected claims justified.
- [ ] Full statement-level source anchoring preserved.
  - [ ] Every statement has `source_id`.
  - [ ] Every statement has `trace_status`.
  - [ ] Every mapped statement has valid anchor refs.
- [ ] Build outputs and checks are green.
  - [ ] Validate/build/verify pass.
  - [ ] Generated DOCX exists.
- [ ] Reporting complete.
  - [ ] JSON report produced under `$OPENCODE_CONFIG_DIR/reports/`.
  - [ ] Markdown report produced under `$OPENCODE_CONFIG_DIR/reports/`.
  - [ ] Reports explicitly include what traced, what did not, and remediation plan.
- [ ] Durable closeout complete.
  - [ ] Finalization flags set in run state.
  - [ ] Summary/handoff includes exact next-session resume behavior.
