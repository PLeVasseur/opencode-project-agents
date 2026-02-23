# Glossary poor/questionable manual placement remediation plan

## Objective

- [ ] Remediate placement quality for every term rated `poor` or `questionable` in the feedback snapshot.
- [ ] Complete remediation manually, term-by-term (no scripted adjudication, no scripted bulk edits).
- [ ] Produce auditable before/after/why evidence for Phase 1 and Phase 2.
- [ ] Preserve stacked branch ordering and ancestry (`step1 -> step2 -> step3 -> step4 -> step5`).

## Scope lock (mandatory)

- [ ] Source snapshot: `$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback/fls-pr6-placement-fitness.json`.
- [ ] In-scope rating set: `poor` + `questionable` only.
- [ ] Scope cardinality: exactly `202` terms.
- [ ] Supplementary checklist path (authoritative): `$OPENCODE_CONFIG_DIR/reports/glossary-poor-questionable-202-checklist.md`.
- [ ] Seed ledger template path: `$OPENCODE_CONFIG_DIR/reports/glossary-poor-questionable-202-ledger-seed.csv`.
- [ ] Immutable baseline reference path: `$OPENCODE_CONFIG_DIR/reports/glossary-poor-questionable-202-baseline-reference.csv`.
- [ ] Reason rubric path: `$OPENCODE_CONFIG_DIR/reports/glossary-poor-questionable-reason-rubric.md`.
- [ ] Unified validator path: `$OPENCODE_CONFIG_DIR/reports/validate-ledger-and-checklist.py`.
- [ ] No term may be dropped, merged, or replaced; all 202 checklist IDs must be closed.

## Hard constraints

- [ ] Use absolute paths for all git/worktree/validation commands.
- [ ] Preserve unrelated user edits; do not reset/revert unrelated changes.
- [ ] Use project entrypoints only (`./make.py`, `./generate-glossary.py`, migration checker tool).
- [ ] Keep generated artifacts under `$OPENCODE_CONFIG_DIR/reports/`.
- [ ] Do not use script-based relocation/adjudication of terms; every term decision is manual.

## Canonical paths and branches

- [ ] Worktrees:
  - `/home/pete.levasseur/project/fls-wt/step1`
  - `/home/pete.levasseur/project/fls-wt/step2`
  - `/home/pete.levasseur/project/fls-wt/step3`
  - `/home/pete.levasseur/project/fls-wt/step4`
  - `/home/pete.levasseur/project/fls-wt/step5`
- [ ] Step branches:
  - `glossary-step-1-main-text-coverage`
  - `glossary-step-2-align-duplicate-text`
  - `glossary-step-3-dt-main-only`
  - `glossary-step-4-remove-see-paragraphs`
  - `glossary-step-5-generated-glossary-parity`

## Stage 0: preflight and bootstrap

- [ ] Create `RUN_ID` and `REMEDIATION_DIR="$OPENCODE_CONFIG_DIR/reports/glossary-poor-questionable-manual-remediation-$RUN_ID"`.
- [ ] Capture environment, branch heads, and worktree cleanliness in `commands.log`.
- [ ] Verify PR mapping for the stack (`#6-#10` or discovered equivalents) and store `pr-stack-discovery.json`.
- [ ] Capture baseline reports for step1 and step2 strict checks and build/link status.
- [ ] Record baseline reconciliation against feedback snapshot.
- [ ] Copy seeded ledger into run folder as `${REMEDIATION_DIR}/manual-placement-ledger.csv`.
- [ ] Copy immutable baseline reference into run folder as `${REMEDIATION_DIR}/manual-placement-baseline-reference.csv`.
- [ ] Copy reason rubric into run folder as `${REMEDIATION_DIR}/reason-rubric.md`.
- [ ] Optional automation path: run `$OPENCODE_CONFIG_DIR/reports/glossary-batch-orchestrator.py` to execute 20-ID OpenCode batches with one commit per batch.

```bash
python3 "$OPENCODE_CONFIG_DIR/reports/glossary-batch-orchestrator.py" \
  --workdir "/home/pete.levasseur/project/fls-wt/step1" \
  --expected-branch "glossary-step-1-main-text-coverage" \
  --batch-size 20
```

## Stage 1: checklist integrity gate setup (CG-202)

- [ ] Verify checklist file exists at `$OPENCODE_CONFIG_DIR/reports/glossary-poor-questionable-202-checklist.md`.
- [ ] Verify checklist contains exactly 202 parent task lines (`PQ-001` ... `PQ-202`) and 1010 rubric sub-task lines (`PQ-001.1` ... `PQ-202.5`).
- [ ] Verify checklist IDs align exactly with seeded ledger and baseline reference IDs.
- [ ] Verify all parent and sub-task checklist lines start unchecked (`- [ ]`) before remediation starts.
- [ ] Establish hard gate rule: no Phase 2 edits, no push, and no PR updates until all 202 parent rows and all 1010 rubric sub-rows are `[x]`.

### CG-202 hard gate (must pass)

- [ ] Run the unified validator in `init` mode during bootstrap; write results to `validate-init.json` and `checklist-progress.md`.
- [ ] Run the unified validator in `gate` mode for G1 and G2; write results to `validate-g1.json` / `validate-g2.json` and refresh `checklist-progress.md`.
- [ ] Run the unified validator in `final` mode before closeout; write results to `validate-final.json`.
- [ ] If validator exits non-zero, stop and document blockers before proceeding.

```bash
python3 "$OPENCODE_CONFIG_DIR/reports/validate-ledger-and-checklist.py" \
  --mode init \
  --checklist "$OPENCODE_CONFIG_DIR/reports/glossary-poor-questionable-202-checklist.md" \
  --ledger "$REMEDIATION_DIR/manual-placement-ledger.csv" \
  --baseline "$REMEDIATION_DIR/manual-placement-baseline-reference.csv" \
  --json-out "$REMEDIATION_DIR/validate-init.json" \
  --markdown-out "$REMEDIATION_DIR/checklist-progress.md"
```

```bash
python3 "$OPENCODE_CONFIG_DIR/reports/validate-ledger-and-checklist.py" \
  --mode gate \
  --checklist "$OPENCODE_CONFIG_DIR/reports/glossary-poor-questionable-202-checklist.md" \
  --ledger "$REMEDIATION_DIR/manual-placement-ledger.csv" \
  --baseline "$REMEDIATION_DIR/manual-placement-baseline-reference.csv" \
  --json-out "$REMEDIATION_DIR/validate-g1.json" \
  --markdown-out "$REMEDIATION_DIR/checklist-progress.md"
```

- For G2, rerun the same command with `--json-out "$REMEDIATION_DIR/validate-g2.json"`.

```bash
python3 "$OPENCODE_CONFIG_DIR/reports/validate-ledger-and-checklist.py" \
  --mode final \
  --checklist "$OPENCODE_CONFIG_DIR/reports/glossary-poor-questionable-202-checklist.md" \
  --ledger "$REMEDIATION_DIR/manual-placement-ledger.csv" \
  --baseline "$REMEDIATION_DIR/manual-placement-baseline-reference.csv" \
  --json-out "$REMEDIATION_DIR/validate-final.json" \
  --markdown-out "$REMEDIATION_DIR/checklist-progress.md"
```

## Stage 2: manual Phase 1 remediation (step1)

- [ ] Process all 202 checklist entries one-by-one in step1.
- [ ] For each term, manually inspect:
  - baseline definition location,
  - first meaningful use location,
  - conceptual ownership section,
  - chapter order/discoverability impact.
- [ ] Apply one manual disposition per term:
  - relocate definition,
  - retain but reorder within owning chapter,
  - retain with explicit discoverability mitigation at first use.
- [ ] Keep one canonical term definition location (no accidental duplicates).
- [ ] After each term is completed, mark its checklist row `[x]`.
- [ ] Record per-term audit row in `manual-placement-ledger.csv` with before/after/why + commit evidence.
- [ ] Run periodic strict/build/link checkpoints and log all exit codes.

## Stage 3: Gate G1 (strict)

- [ ] Unified validator `gate` mode passed (`validate-g1.json` shows zero errors).
- [ ] `manual-placement-ledger.csv` has 202 resolved rows and no unresolved entries.
- [ ] Step1 strict check passes.
- [ ] Step1 `./make.py --clear` passes.
- [ ] Step1 `./make.py --check-links` passes.
- [ ] If any G1 check fails, stop before any step2 edits and write blocker/remediation notes.

## Stage 4: manual Phase 2 harmonization (step2)

- [ ] Sync step2 from updated step1 (FF-first; document fallback if FF fails).
- [ ] Reconcile wording/definition alignment impacts introduced by Phase 1 moves.
- [ ] Continue manual, term-by-term updates only for impacted terms.
- [ ] Update `manual-placement-ledger.csv` with Phase 2 evidence where applicable.
- [ ] Run Phase 2 strict checks and capture artifacts.
- [ ] Run step2 `./make.py --clear` and `./make.py --check-links`.

## Stage 5: Gate G2 (strict)

- [ ] Unified validator `gate` mode re-run and passed (`validate-g2.json` shows zero errors).
- [ ] Phase 2 strict check passes.
- [ ] Phase 2 build and link checks pass.
- [ ] No unresolved poor/questionable terms remain in ledger summary.
- [ ] If any G2 check fails, stop before push/restack and document blocker/remediation.

## Stage 6: reports (before => after => why)

- [ ] Write `phase1-before-after-why.md` with explicit before location, after location, and rationale per term.
- [ ] Write `phase2-before-after-why.md` with harmonization deltas and rationale.
- [ ] Write `placement-resolution-summary.md` with counts by action and unresolved count.
- [ ] Write `checklist-progress.md` with final CG-202 counts and pass evidence.
- [ ] Ensure all reports reference checklist IDs (`PQ-001`..`PQ-202`) for traceability.

## Stage 7: restack and downstream verification

- [ ] Restack `step3 -> step4 -> step5` using FF-only first.
- [ ] If FF fails on any edge, apply explicit merge fallback and document conflict decisions.
- [ ] Re-run required strict/build/link checks on affected downstream branches.
- [ ] Verify ancestry chain pass (`step1->step2->step3->step4->step5`).

## Stage 8: push and PR updates

- [ ] Push updated step branches to fork (no force push).
- [ ] Update PR6 body with Phase 1 before/after/why and checklist evidence.
- [ ] Update PR7 body with Phase 2 before/after/why and checklist evidence.
- [ ] Post restack notes to PR8-PR10 (or discovered equivalents).
- [ ] Capture base/head confirmation for all updated PRs.

## Exit criteria (all mandatory)

- [ ] All 202 parent checklist items are `[x]`.
- [ ] All 1010 rubric sub-checklist items are `[x]`.
- [ ] All 202 terms show `resolved-high` in `manual-placement-ledger.csv`.
- [ ] All 202 terms have `reason_quality=pass` and complete before/after anchors.
- [ ] Unified validator `final` mode passed (`validate-final.json` shows zero errors).
- [ ] Phase 1 and Phase 2 strict/build/link gates are green.
- [ ] Restack and ancestry verification are green for step2-step5.
- [ ] PR updates completed with artifact references.
- [ ] Final report includes blockers/deviations (if any) and next actions.
