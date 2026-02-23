# PR6 Wave A/B Recovery Plan (Recommendation-Locked, Permit-Gated, UUID-Tracked)

## Mission and scope

- [ ] Recover from the invalid Wave A/B execution with explicit anti-cheating controls.
- [ ] Re-run Wave A and Wave B only after guardrail scripts are updated and smoke-tested.
- [ ] Keep prior run artifacts immutable; use a fresh run directory and supersession note.
- [ ] Defer Wave C/D until Gate B+ passes with external v3 artifacts.

## Root-cause acknowledgment (must remain explicit)

- [ ] First run overused mechanical `:dt:` -> `:t:` conversions and avoided real relocation work.
- [ ] Analyzer recommendations were overridden too often without independent review artifacts.
- [ ] Strict check regression was treated as informational; this is now prohibited.
- [ ] Rationale diversity controls were too weak to detect templated monoculture behavior.

## Policy lock (non-negotiable)

- [ ] Recommendation-first for high/medium placement terms.
  - [ ] Default action must be `move` or `move+rewrite` to `recommended_location`.
  - [ ] Any non-move action requires a deviation permit artifact (see below).
- [ ] Term-source lock for every completed term decision.
  - [ ] Checklist term, ledger term, placement JSON term, and divergence JSON term must match exactly.
  - [ ] Any mismatch hard-fails the term update.
- [ ] Strict baseline lock.
  - [ ] Baseline is pinned to `START_HEAD=19e75856eac5694e5d613c7c59b429848d333992`.
  - [ ] Baseline strict check is pinned to `missing_count=2`.
  - [ ] Every batch/wave/final gate must satisfy `missing_count <= 2` unless explicit waiver artifact is present.
- [ ] Foundational relocation lock.
  - [ ] Ten flagged foundational terms must land in required target files at Gate A.
  - [ ] No deviation permits allowed for these ten terms.

## Locked inputs

- [ ] Wave A/B execution inputs (v2):
  - [ ] `inputs/fls-pr6-placement-fitness-v2.json`
  - [ ] `inputs/fls-pr6-definition-divergence-v2.json`
- [ ] Gate B+/C/D scope inputs (v3):
  - [ ] `inputs/v3/fls-pr6-placement-fitness-v3.json`
  - [ ] `inputs/v3/fls-pr6-definition-divergence-v3.json`
- [ ] Record source checksums in run-local `inputs/checksums.sha256`.

## Script modifications (required before rerun)

### 1) `record-rationale-v3.py` (new, mandatory writer)

- [x] Create `$OPENCODE_CONFIG_DIR/reports/record-rationale-v3.py`.
- [x] Enforce writer-only updates to rationale/decision fields.
  - [x] Completed-term rationale fields may only be set by this script.
  - [x] Direct ledger edits for these fields are invalidated by validator checks.
- [x] Require CLI arguments:
  - [x] `--checklist-id`, `--checklist`, `--ledger`
  - [x] `--placement-json`, `--divergence-json`
  - [x] `--events-jsonl`, `--batch-id`
  - [x] `--implementer-id`
  - [x] `--action-type`, `--decision-detail`, `--reason-code`, `--reason-why`
  - [x] `--semantic-change-flag`, `--review-attention`
  - [x] `--after-file`, `--after-line`, `--after-dp-id`
  - [x] `--phase1-status`, `--final-quality`
  - [x] `--deviation-permit` (required in non-move high/medium cases)
- [x] Enforce term-source lock (fail with no writes):
  - [x] checklist ID exists and resolves to exactly one parent term.
  - [x] ledger row exists for checklist ID.
  - [x] checklist/ledger term equality check passes.
  - [x] exactly one placement JSON entry matches term.
  - [x] exactly one divergence JSON entry matches term.
  - [x] all four term identities match exactly.
- [x] Enforce recommendation lock:
  - [x] read `relocation_priority`, `recommended_location.file`, `recommended_location.section`, `recommended_location.reason`.
  - [x] if priority in `{high, medium}` and action is move-type, require `after_file == recommended_file`.
  - [x] if priority in `{high, medium}` and action is non-move, require valid deviation permit.
- [x] Deviation permit enforcement (new artifact model):
  - [x] permit path format: `deviation-permits/deviation-permit-{checklist_id}.json`.
  - [x] required JSON fields:
    - [x] `checklist_id`, `term`
    - [x] `recommended_file`, `recommended_section`, `recommended_reason`
    - [x] `proposed_action`, `proposed_location`
    - [x] `evidence_against_recommendation` (>= 200 chars)
    - [x] `evidence_for_proposed` (>= 200 chars)
    - [x] `reference_count_argument` (>= 120 chars)
    - [x] `approved_by` (non-empty and must not equal `--implementer-id`)
  - [x] writer validates byte-equality against placement JSON for recommended fields.
  - [x] writer rejects boilerplate evidence patterns.
  - [x] writer records permit path + permit SHA256 in ledger and event.
- [x] UUID/event behavior:
  - [x] generate fresh `rationale_uuid` (`uuid4`) on every accepted write.
  - [x] write `rationale_inserted_at_utc`, `rationale_text_sha256`.
  - [x] append immutable JSON event to `rationale-events.jsonl`.
  - [x] include source JSON checksums and permit checksum in event.

### 2) `validate-ledger-and-checklist-v3.py` (upgrade)

- [x] Add required ledger columns:
  - [x] `rationale_uuid`, `rationale_inserted_at_utc`, `rationale_text_sha256`
  - [x] `recommendation_priority`, `recommended_file`, `recommended_section`, `recommendation_used`
  - [x] `deviation_permit_path`, `deviation_permit_sha256`, `deviation_approved_by`
- [x] Add CLI arguments:
  - [x] `--events-jsonl`
  - [x] `--strict-baseline-json`
  - [x] `--strict-current-json`
  - [x] `--strict-max-missing` (default `2`)
- [x] UUID/event integrity checks:
  - [x] every completed row must have valid UUID.
  - [x] UUID must be unique across completed rows.
  - [x] matching event record must exist for each completed row.
  - [x] latest event digest must match current row digest.
- [x] Recommendation/deviation checks:
  - [x] high/medium non-move rows require permit path, SHA256, and non-empty `deviation_approved_by`.
  - [x] missing/invalid permit metadata hard-fails.
- [x] Deviation concentration gate:
  - [x] if deviation permits >30% of high/medium terms in a wave, fail with `FAILED_DEVIATION_CONCENTRATION`.
- [x] Foundational placement gate (hardcoded targets):
  - [x] validate `after_file` for required terms at Gate A.
  - [x] fail with `FAILED_FOUNDATIONAL_PLACEMENT` on mismatch.
- [x] Anti-monoculture thresholds (pinned values):
  - [x] max 60% for any `action_type + reason_code` pair per wave.
  - [x] max Jaccard similarity 0.80 for any `reason_why` pair in same wave.
  - [x] reject known boilerplate regex from first invalid run.
  - [x] waves with >20 terms must use at least 2 distinct `action_type` values.
- [x] Strict non-regression gate:
  - [x] read baseline/current strict reports.
  - [x] fail if `current_missing > strict_max_missing` and no approved waiver artifact.

### 3) `glossary-batch-orchestrator-v3.py` (upgrade)

- [x] Add script wiring arguments:
  - [x] `--rationale-writer`
  - [x] `--placement-json`
  - [x] `--divergence-json`
  - [x] `--events-jsonl`
  - [x] `--strict-baseline-json`
- [x] Prompt hardening:
  - [x] require `record-rationale-v3.py` invocation per completed term.
  - [x] prohibit direct rationale/decision edits in ledger.
  - [x] include batch term-lock manifest in prompt context.
- [x] Batch gates:
  - [x] pre/post strict check run for each batch.
  - [x] validator run must include events-jsonl and strict-baseline checks.
  - [x] quarantine any term lacking UUID event/permit compliance.
  - [x] block commit on strict regression or concentration failures.
- [x] Batch summary additions:
  - [x] recommendation compliance rate
  - [x] deviation permit count
  - [x] maximum rationale similarity
  - [x] moved-term count and moved-term list
- [x] Run-end hard fails:
  - [x] `FAILED_RECOMMENDATION_LOCK`
  - [x] `FAILED_UUID_GUARDRAIL`
  - [x] `FAILED_DEVIATION_CONCENTRATION`
  - [x] `FAILED_RATIONALE_MONOCULTURE`
  - [x] `FAILED_STRICT_REGRESSION`
  - [x] `FAILED_FOUNDATIONAL_PLACEMENT`

### 4) `analyze-rationale-patterns-v3.py` (new, now required)

- [x] Build helper script that computes:
  - [x] action/reason concentration by wave
  - [x] pairwise rationale similarity summary
  - [x] boilerplate hit counts
  - [x] deviation permit concentration by wave
- [x] Emit JSON + Markdown artifacts consumed by validator/orchestrator gate logic.

## Foundational relocation matrix (hardcoded)

- [ ] Enforce this exact target table at Gate A:
  - [ ] `value` -> `values.rst` (allowed sections: Values)
  - [ ] `expression` -> `expressions.rst` (allowed sections: Expressions)
  - [ ] `trait` -> `types-and-traits.rst` (allowed sections: Traits, Trait Types)
  - [ ] `item` -> `items.rst` (allowed sections: Items)
  - [ ] `field` -> `types-and-traits.rst` (allowed sections: Struct Types, Enum Types)
  - [ ] `reference` -> `ownership-and-deconstruction.rst` (allowed sections: References, Borrowing)
  - [ ] `implementation` -> `implementations.rst` (allowed sections: Implementations, Inherent Implementations)
  - [ ] `method` -> `functions.rst` (allowed sections: Functions, Associated Functions)
  - [ ] `crate` -> `program-structure-and-compilation.rst` (allowed sections: Crates, Compilation Roots)
  - [ ] `statement` -> `statements.rst` (allowed sections: Statements)

## Revert and reset strategy (explicit)

- [ ] Restore `src/` to `START_HEAD` in one forward commit:
  - [ ] `git checkout 19e75856eac5694e5d613c7c59b429848d333992 -- src/`
  - [ ] `git commit -m "docs(glossary): revert Wave A/B for recovery rerun"`
- [ ] Do not rewrite history; do not force-push.
- [ ] Keep prior invalid run immutable and mark supersession in new run artifacts.

## Post-revert baseline verification (required before Wave A)

- [ ] Re-run strict check and verify `missing_count == 2`.
- [ ] Re-run placement analysis and verify aggregate parity with locked v2 baseline counts.
- [ ] Store both reports as new Gate G0 baseline artifacts.
- [ ] Stop with `FAILED_POST_REVERT_BASELINE_MISMATCH` on any mismatch.

## Human quality spot-check protocol

- [ ] Wave A human gate (required before Wave B):
  - [ ] reviewer spot-checks at least 5 of the 10 relocated foundational terms.
  - [ ] verify prose quality at destination and source back-reference quality.
  - [ ] verify semantic fidelity vs glossary definition.
  - [ ] Wave B blocked until this gate is explicitly marked pass.
- [ ] Wave B sampling gate:
  - [ ] reviewer spot-checks at least 5 terms per WB batch.
  - [ ] prioritize highest divergence-risk terms in each batch.

## Script smoke tests (must pass before Wave A/B rerun)

- [x] `record-rationale-v3.py` smoke tests:
  - [x] `--help` works.
  - [x] success case writes UUID and event for a synthetic fixture row.
  - [x] mismatch case hard-fails on term-source lock.
  - [x] non-move high-priority case hard-fails without deviation permit.
  - [x] deviation permit with `approved_by == implementer_id` hard-fails.
- [x] `validate-ledger-and-checklist-v3.py` smoke tests:
  - [x] `--help` works.
  - [x] validates fixture with events and permit metadata.
  - [x] fails on duplicate UUID.
  - [x] fails on concentration threshold breach.
  - [x] fails on strict regression breach.
- [x] `glossary-batch-orchestrator-v3.py` smoke tests:
  - [x] `--help` works.
  - [x] dry-run includes writer/lock requirements in batch prompt.
  - [x] dry-run emits term-lock manifest artifact.

## Pre-Wave entry criteria (all required)

- [x] All script modifications implemented.
- [x] All script smoke tests pass with stored outputs.
- [ ] Revert/reset complete and baseline parity verified.
- [ ] Fresh run ID/remediation directory created.
- [ ] Reviewer-approved policy lock acknowledged (`approved_by` permit rule included).

## Reviewer handoff artifacts (expanded)

- [ ] `deviation-permits/` directory with one file per approved exception.
- [ ] `reports/rationale-events.jsonl` + checksum.
- [ ] recommendation compliance report by batch and wave.
- [ ] rationale pattern report (JSON + Markdown).
- [ ] foundational relocation compliance table.
- [ ] strict regression ledger (`baseline_missing`, `current_missing`, `delta`, waiver state).

## Acceptance criteria

- [ ] Every completed term has unique UUID + matching event.
- [ ] High/medium terms are recommendation-compliant or have reviewer-approved deviation permit artifacts.
- [ ] Deviation concentration stays <=30% per wave.
- [ ] Foundational target files are satisfied for all 10 required terms.
- [ ] Strict check remains at `missing_count <= 2` unless explicit waiver artifact exists.
- [ ] Anti-monoculture thresholds remain within pinned limits.
- [ ] Execution integrity checks and wave boundary SHA checks pass.
