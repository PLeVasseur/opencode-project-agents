# PR6 V2 Step1/Phase1 Remediation Plan (Conceptual-Home First)

## Mission

- [ ] Remediate Step1/Phase1 glossary placement and definition-quality issues using the v2 feedback bundle.
- [ ] Prioritize conceptual coherence for foundational terms while preserving traceability and reviewability.
- [ ] Produce auditable before/after/why evidence for every touched term.
- [ ] Keep one commit per batch and pass all Phase1 validation gates.

## Scope and decision framing

- [ ] Scope this plan to `glossary-step-1-main-text-coverage` only (Step1/Phase1).
- [ ] Treat this as a targeted remediation cycle against v2 feedback, not a full restack/Phase2 run.
- [ ] Use policy decision: **conceptual-home-first** for foundational terms.
- [ ] Allow controlled forward references when needed to preserve conceptual-home placement quality.
- [ ] Treat analyzer recommendations as diagnostic signals, not authoritative final destinations.

## Inputs (locked)

- [ ] Lock and reference these exact files:
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/fls-pr6-updated-analysis-v2.md`
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/fls-pr6-placement-fitness-v2.json`
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/fls-pr6-definition-divergence-v2.json`
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/plan-feedback/fls-pr6-remediation-plan-feedback.md`
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/plan-feedback/fls-pr6-remediation-plan-revised-feedback.md`
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/plan-feedback/fls-pr6-v2-plan-bundle-feedback.md`
- [ ] Lock branch and worktree:
  - [ ] Worktree: `/home/pete.levasseur/project/fls-wt/step1`
  - [ ] Branch: `glossary-step-1-main-text-coverage`

## Hard constraints

- [ ] Manual term adjudication only (no scripted auto-relocation logic).
- [ ] One canonical `:dt:` definition per concept after each change.
- [ ] Use explicit `:t:` or paragraph forward-reference where canonical `:dt:` is moved away from local usage.
- [ ] Do not revert unrelated user work.
- [ ] Do not push until explicitly requested.

## Gate T0: v2 tooling compatibility (hard blocker before G0)

- [ ] Create and lock v2-specific tooling files (do not modify v1 scripts in place):
  - [ ] `$OPENCODE_CONFIG_DIR/reports/validate-ledger-and-checklist-v2.py`
  - [ ] `$OPENCODE_CONFIG_DIR/reports/glossary-batch-orchestrator-v2.py`
- [ ] Validator v2 compatibility requirements:
  - [ ] Supports checklist parent IDs `WA-###`, `WB-###`, `WC-###`, `WD-###`, `QQ-###`.
  - [ ] Supports 6 sub-items per parent (`.1`..`.6`) with v2 rubric mapping:
    - [ ] `.1` before snapshot locked
    - [ ] `.2` action recorded
    - [ ] `.3` rationale quality pass
    - [ ] `.4` semantic review fields complete
    - [ ] `.5` after snapshot captured
    - [ ] `.6` status finalized
  - [ ] Validates v2 ledger schema (`action_type`, `decision_detail`, `semantic_change_flag`, `review_attention`).
  - [ ] Uses dynamic expected-parent-count (no hardcoded 202 assumption for v2 waves).
- [ ] Orchestrator v2 compatibility requirements:
  - [ ] Parses wave-prefixed checklist IDs and 6-sub-item rows.
  - [ ] Enforces wave boundaries and ordering (A -> B -> Gate B+ -> C -> D).
  - [ ] Enforces Gate B+ hard stop (external v3 artifacts required before C/D).
  - [ ] Supports partial-batch completion with quarantine queue and partial batch records.
  - [ ] Defaults to v2 plan/checklist/ledger template paths.
- [ ] Gate T0 validation proofs (required artifacts):
  - [ ] `$REMEDIATION_DIR/validation/tooling-compat/validator-init.json`
  - [ ] `$REMEDIATION_DIR/validation/tooling-compat/validator-init.md`
  - [ ] `$REMEDIATION_DIR/validation/tooling-compat/orchestrator-dryrun.json`
  - [ ] `$REMEDIATION_DIR/validation/tooling-compat/summary.md`
- [ ] Hard stop rule: **No Wave A execution until Gate T0 is green.**

## Run setup and artifact topology

- [ ] Create a run ID and remediation root:
  - [ ] `RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)-v2-phase1"`
  - [ ] `REMEDIATION_DIR="$OPENCODE_CONFIG_DIR/reports/glossary-pr6-v2-step1-phase1-remediation-$RUN_ID"`
- [ ] Create standard artifact directories:
  - [ ] `$REMEDIATION_DIR/baseline/`
  - [ ] `$REMEDIATION_DIR/inputs/`
  - [ ] `$REMEDIATION_DIR/inputs/v3/`
  - [ ] `$REMEDIATION_DIR/tools/`
  - [ ] `$REMEDIATION_DIR/waves/`
  - [ ] `$REMEDIATION_DIR/batches/`
  - [ ] `$REMEDIATION_DIR/validation/`
  - [ ] `$REMEDIATION_DIR/validation/tooling-compat/`
  - [ ] `$REMEDIATION_DIR/reports/`
  - [ ] `$REMEDIATION_DIR/logs/`
- [ ] Copy locked inputs into `$REMEDIATION_DIR/inputs/` and generate `checksums.sha256`.
- [ ] Copy v2 tooling into `$REMEDIATION_DIR/tools/` for immutable run provenance.

## Gate G0: environment + baseline readiness

- [ ] Precondition: Gate T0 passed.

- [ ] Toolchain sanity:
  - [ ] `uv --version` is available.
  - [ ] `uv run python tools/glossary-migration-check.py --help` works in step1 worktree.
  - [ ] `./make.py --help` works in step1 worktree.
- [ ] Baseline capture:
  - [ ] Capture `git status --short --branch` and `git rev-parse HEAD`.
  - [ ] Capture `uv run python tools/glossary-migration-check.py --phase 1 --strict --report "$REMEDIATION_DIR/baseline/phase1-strict.json"`.
  - [ ] Capture `./make.py --clear` log to `$REMEDIATION_DIR/baseline/make-clear.log`.
  - [ ] Capture `./make.py --check-links` log to `$REMEDIATION_DIR/baseline/make-check-links.log` (if environment supports linkcheck; record explicit exception if not).
- [ ] Baseline summary:
  - [ ] Write `$REMEDIATION_DIR/baseline/summary.md` with pass/fail and blockers.

## Tooling compatibility checklist (G0 prerequisite details)

- [ ] `python3 "$OPENCODE_CONFIG_DIR/reports/validate-ledger-and-checklist-v2.py" --help` works.
- [ ] `python3 "$OPENCODE_CONFIG_DIR/reports/glossary-batch-orchestrator-v2.py" --help` works.
- [ ] Validator init pass against v2 templates succeeds with zero errors.
- [ ] Orchestrator dry-run identifies expected first Wave A IDs.
- [ ] Orchestrator dry-run does not attempt Wave B/C/D before Wave A completion.
- [ ] All tooling compatibility outputs written to `$REMEDIATION_DIR/validation/tooling-compat/`.

## Policy gate (must be explicit before editing)

- [ ] Write and freeze `$REMEDIATION_DIR/reports/policy-decisions-v2.md` with:
  - [ ] Conceptual-home-first rule for foundational terms.
  - [ ] Criteria for choosing canonical home section.
  - [ ] Rule for converting displaced `:dt:` usages to `:t:` or `For :dt:` reference form.
  - [ ] Rule for handling analyzer destination suggestions as non-binding.
  - [ ] Rule for acceptable forward-reference debt when conceptual-home placement is superior.
- [ ] Add explicit decision for missing-term findings:
  - [ ] `crate import` is canonically satisfied by `[crate import]s`.
  - [ ] `declaration` is canonically satisfied by `[declaration]s`.
  - [ ] Record rationale and closure criteria.

## Backlog model (dynamic, reviewer-aligned)

- [ ] Build a run-local master ledger/checklist pair (new files, do not reuse old run files):
  - [ ] `$REMEDIATION_DIR/manual-placement-checklist-v2.md`
  - [ ] `$REMEDIATION_DIR/manual-placement-ledger-v2.csv`
- [ ] Ledger required columns:
  - [ ] identity: `checklist_id`, `term`
  - [ ] before: `baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_section`, `baseline_commit`
  - [ ] action: `action_type`, `decision_detail`, `reason_code`, `reason_why`, `reason_quality`, `semantic_change_flag`
  - [ ] after: `after_file`, `after_line`, `after_dp_id`, `after_section`, `after_commit`
  - [ ] status: `wave`, `phase1_status`, `final_quality`, `review_attention`, `notes`
- [ ] Start with staged backlog strategy:
  - [ ] Stage A/B scope first (foundational + high/medium placement priorities).
  - [ ] Recompute residual scope before locking C/D.
  - [ ] Avoid hard-coding 233 as mandatory execution scope before A/B effects are measured.

## Definition action taxonomy (required)

- [ ] Allowed `action_type` values:
  - [ ] `move`
  - [ ] `rewrite`
  - [ ] `move+rewrite`
  - [ ] `retain`
  - [ ] `retain+rewrite`
- [ ] `decision_detail` must explain specific disposition at chapter/section level.
- [ ] `semantic_change_flag` values:
  - [ ] `none`
  - [ ] `clarification-only`
  - [ ] `normative-risk`
- [ ] Any `action_type` containing `rewrite` requires explicit reviewer attention (`review_attention=required`).

## Wave A (foundational terms) - small and decisive

- [ ] Wave A must be completed first as a dedicated tranche.
- [ ] Foundational term set (15):
  - [ ] `value`
  - [ ] `expression`
  - [ ] `type`
  - [ ] `trait`
  - [ ] `construct`
  - [ ] `entity`
  - [ ] `name`
  - [ ] `item`
  - [ ] `field`
  - [ ] `reference`
  - [ ] `implementation`
  - [ ] `method`
  - [ ] `crate`
  - [ ] `module`
  - [ ] `statement`
- [ ] For each Wave A term, complete all subchecks:
  - [ ] capture before paragraph and anchor (file/line/dp)
  - [ ] select conceptual-home section with explicit reason
  - [ ] move or rewrite canonical `:dt:` accordingly
  - [ ] convert old definitional site to `:t:` or explicit forward-reference
  - [ ] ensure exactly one canonical `:dt:` remains
  - [ ] capture after paragraph and anchor (file/line/dp)
  - [ ] write term-specific `reason_why` (>= 80 chars, not template prose)
  - [ ] mark checklist sub-items and ledger status complete
- [ ] Batch size for Wave A: `<=20`.
- [ ] Gate A:
  - [ ] validator pass for checklist/ledger
  - [ ] strict phase check pass
  - [ ] build pass
  - [ ] link-check pass or documented environment exception
  - [ ] no unresolved foundational term
  - [ ] write `$REMEDIATION_DIR/waves/wave-a-patterns.md`

## Wave B (remaining high/medium placement priorities)

- [ ] Build Wave B set from v2 placement priorities:
  - [ ] include all terms with `relocation_priority in {high, medium}`
  - [ ] exclude terms already finished in Wave A
  - [ ] write frozen list to `$REMEDIATION_DIR/waves/wave-b-terms.json`
- [ ] Execute Wave B term-by-term manual remediation.
- [ ] Batch size for Wave B: `20` terms per batch.
- [ ] Per-batch controls:
  - [ ] batch prompt lists exact IDs only
  - [ ] no out-of-scope checklist/ledger edits
  - [ ] one commit per successful batch
  - [ ] store per-batch summary and validator outputs
- [ ] Gate B:
  - [ ] all Wave B terms resolved or explicitly justified exceptions
  - [ ] strict phase check pass
  - [ ] build pass
  - [ ] link-check pass or exception documented
  - [ ] write `$REMEDIATION_DIR/waves/wave-b-patterns.md`

## Gate B+ (rescope, hard lock)

- [ ] Stop after Waves A/B commits are complete.
- [ ] Require externally provided v3 artifacts (no internal regeneration path):
  - [ ] `$REMEDIATION_DIR/inputs/v3/fls-pr6-updated-analysis-v3.md`
  - [ ] `$REMEDIATION_DIR/inputs/v3/fls-pr6-placement-fitness-v3.json`
  - [ ] `$REMEDIATION_DIR/inputs/v3/fls-pr6-definition-divergence-v3.json`
- [ ] Verify presence and checksums of all 3 v3 artifacts.
- [ ] Produce `$REMEDIATION_DIR/reports/rescope-after-wave-b.md`:
  - [ ] v2 vs v3 count deltas by category
  - [ ] terms auto-resolved by Waves A/B
  - [ ] measured residual universe for C and D
  - [ ] explicit frozen scope rationale for C and D
- [ ] Freeze scopes using measured v3 residuals:
  - [ ] write `$REMEDIATION_DIR/waves/wave-c-terms.json`
  - [ ] write `$REMEDIATION_DIR/waves/wave-d-terms.json`
- [ ] Hard gate rule: **No Wave C/D execution until Gate B+ passes**.

## Wave C (residual low-reliability divergence)

- [ ] Precondition: Gate B+ passed and Wave C scope frozen from v3 residuals.
- [ ] Scope Wave C to residual divergence `reliability=low` terms not already resolved.
- [ ] Focus fixes on definition quality:
  - [ ] rewrite incidental inline `:dt:` into standalone definitional language where needed
  - [ ] preserve semantics and avoid contextual overfitting
  - [ ] keep glossary compatibility intent explicit
- [ ] Batch size for Wave C: `40-50` terms per batch.
- [ ] Wave C gate:
  - [ ] validator pass
  - [ ] strict phase check pass
  - [ ] no unresolved low-reliability term without justification
  - [ ] write `$REMEDIATION_DIR/waves/wave-c-patterns.md`

## Wave D (residual placement poor/questionable)

- [ ] Precondition: Gate B+ passed and Wave D scope frozen from v3 residuals.
- [ ] Scope Wave D to residual placement poor/questionable terms after A/B/C.
- [ ] Resolve via one of:
  - [ ] relocate to conceptual home
  - [ ] retain location with explicit conceptual-home justification
  - [ ] retain with forward-reference mitigation and explicit rationale
- [ ] Batch size for Wave D: `40-50` terms per batch.
- [ ] Wave D gate:
  - [ ] validator pass
  - [ ] strict phase check pass
  - [ ] all residual placement items closed or explicitly excepted
  - [ ] write `$REMEDIATION_DIR/waves/wave-d-patterns.md`

## Batch protocol (all waves)

- [ ] Before each batch:
  - [ ] snapshot run-local checklist/ledger
  - [ ] record current branch SHA and clean/dirty status
- [ ] During batch:
  - [ ] process only listed term IDs
  - [ ] enforce manual decision per term
  - [ ] keep evidence paths updated in ledger
- [ ] After batch:
  - [ ] run validator `progress`
  - [ ] run strict check if wave policy requires per-batch strict
  - [ ] commit once (`docs(glossary): remediate placement terms <range>`)
  - [ ] update ledger `after_commit` for batch IDs
- [ ] On failure:
  - [ ] classify term outcomes into `passed` and `quarantined` sets
  - [ ] if at least one term passed:
    - [ ] preserve passing term edits
    - [ ] commit passing term subset once
    - [ ] rollback only quarantined term checklist/ledger rows to pre-batch snapshot values
    - [ ] persist `batch-<n>-partial.json` with passed/quarantined IDs and reasons
    - [ ] persist `batch-<n>-quarantine.json` with quarantined IDs and retry metadata
  - [ ] if zero terms passed:
    - [ ] rollback run-local checklist/ledger to batch snapshot
    - [ ] discard partial code edits for full batch
  - [ ] update `$REMEDIATION_DIR/batches/quarantine-queue.json` with quarantined IDs for retry in next batch
  - [ ] persist `batch-<n>-failure.json` with error and attempted IDs

## Validation matrix

- [ ] Ledger/checklist validator (run-local files):
  - [ ] use `validate-ledger-and-checklist-v2.py`
  - [ ] `progress` mode after each batch
  - [ ] `gate` mode at wave boundaries
  - [ ] `final` mode at closeout
- [ ] Phase checks:
  - [ ] `uv run python tools/glossary-migration-check.py --phase 1 --strict --report ...`
- [ ] Build checks:
  - [ ] `./make.py --clear`
  - [ ] `./make.py --check-links` (or documented environment exception)

## Reporting (streamlined)

- [ ] Primary source-of-truth artifact:
  - [ ] `$REMEDIATION_DIR/manual-placement-ledger-v2.csv`
- [ ] Single summary report:
  - [ ] `$REMEDIATION_DIR/reports/phase1-v2-remediation-summary.md`
  - [ ] must include:
    - [ ] policy decisions and exceptions
    - [ ] wave-by-wave outcomes
    - [ ] before/after counts (placement + divergence)
    - [ ] unresolved terms (target: none or explicitly justified)
    - [ ] commit manifest by batch
    - [ ] Gate B+ decision and v2-v3 delta summary
    - [ ] rewrite review summary (counts by `action_type` and `semantic_change_flag`)
- [ ] Supporting logs:
  - [ ] per-batch validator JSON
  - [ ] per-batch summary JSON
  - [ ] per-batch partial/quarantine JSON where applicable
  - [ ] per-wave pattern documents (`wave-a-patterns.md` ... `wave-d-patterns.md`)
  - [ ] tooling compatibility report (`$REMEDIATION_DIR/validation/tooling-compat/summary.md`)
  - [ ] strict/build/link logs

## Acceptance criteria (review pass targets)

- [ ] Foundational Wave A terms are placed in conceptual homes with clear rationale.
- [ ] High-priority placement terms reduced to zero unresolved (or explicit, reviewer-ready exceptions).
- [ ] Medium-priority placement terms reduced to zero unresolved (or explicit exceptions).
- [ ] Low-reliability divergence substantially reduced after A/B/C with explicit residual rationale.
- [ ] Missing-term pluralization decision documented and accepted (`crate import`, `declaration`).
- [ ] Gate B+ passed with externally provided v3 artifacts and frozen C/D scopes.
- [ ] Gate T0 passed and tooling compatibility report archived.
- [ ] Final validator: `parent_checked == total`, `sub_checked == total`, `resolved_high` for all scoped terms.
- [ ] All terms with `action_type` containing `rewrite` reviewed with explicit attention.
- [ ] Strict phase check passes at closeout.
- [ ] Build passes at closeout.

## Risk register and mitigations

- [ ] Risk: analyzer recommendations push terms into narrow contexts.
  - [ ] Mitigation: policy gate enforces conceptual-home-first.
- [ ] Risk: divergence backlog overestimation causes unnecessary churn.
  - [ ] Mitigation: rescope checkpoint after A/B before locking C/D.
- [ ] Risk: batch overhead slows completion.
  - [ ] Mitigation: 20-term batches for high-risk waves, 40-50 for mechanical waves.
- [ ] Risk: environment instability for link checks.
  - [ ] Mitigation: explicit G0 verification and documented exception policy.
- [ ] Risk: definition rewrites introduce semantic inaccuracy into specification text.
  - [ ] Mitigation: separate move vs rewrite in ledger, set `review_attention=required` for rewrites, and flag `semantic_change_flag` for explicit review scrutiny.

## Final closeout checklist

- [ ] All scoped terms have before/after/why and commit traceability.
- [ ] All wave gates marked pass with evidence paths.
- [ ] Final summary report completed and reviewer-ready.
- [ ] Step1 branch status captured (`git status --short --branch`, `git log --oneline`).
- [ ] Push decision deferred until explicit user instruction.
