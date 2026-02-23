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

### 1) `record-rationale-v2.py` (new, mandatory writer)

- [x] Create `$OPENCODE_CONFIG_DIR/reports/record-rationale-v2.py`.
- [ ] Enforce writer-only updates to rationale/decision fields.
  - [x] Completed-term rationale fields may only be set by this script.
  - [ ] Direct ledger edits for these fields are invalidated by validator checks.
- [ ] Require CLI arguments:
  - [ ] `--checklist-id`, `--checklist`, `--ledger`
  - [ ] `--placement-json`, `--divergence-json`
  - [ ] `--events-jsonl`, `--batch-id`
  - [ ] `--implementer-id`
  - [ ] `--action-type`, `--decision-detail`, `--reason-code`, `--reason-why`
  - [ ] `--semantic-change-flag`, `--review-attention`
  - [ ] `--after-file`, `--after-line`, `--after-dp-id`
  - [ ] `--phase1-status`, `--final-quality`
  - [ ] `--deviation-permit` (required in non-move high/medium cases)
- [x] Enforce term-source lock (fail with no writes):
  - [ ] checklist ID exists and resolves to exactly one parent term.
  - [ ] ledger row exists for checklist ID.
  - [ ] checklist/ledger term equality check passes.
  - [ ] exactly one placement JSON entry matches term.
  - [ ] exactly one divergence JSON entry matches term.
  - [ ] all four term identities match exactly.
- [x] Enforce recommendation lock:
  - [ ] read `relocation_priority`, `recommended_location.file`, `recommended_location.section`, `recommended_location.reason`.
  - [ ] if priority in `{high, medium}` and action is move-type, require `after_file == recommended_file`.
  - [ ] if priority in `{high, medium}` and action is non-move, require valid deviation permit.
- [x] Deviation permit enforcement (new artifact model):
  - [ ] permit path format: `deviation-permits/deviation-permit-{checklist_id}.json`.
  - [ ] required JSON fields:
    - [ ] `checklist_id`, `term`
    - [ ] `recommended_file`, `recommended_section`, `recommended_reason`
    - [ ] `proposed_action`, `proposed_location`
    - [ ] `evidence_against_recommendation` (>= 200 chars)
    - [ ] `evidence_for_proposed` (>= 200 chars)
    - [ ] `reference_count_argument` (>= 120 chars)
    - [x] `approved_by` (non-empty and must not equal `--implementer-id`)
  - [ ] writer validates byte-equality against placement JSON for recommended fields.
  - [ ] writer rejects boilerplate evidence patterns.
  - [ ] writer records permit path + permit SHA256 in ledger and event.
- [x] UUID/event behavior:
  - [ ] generate fresh `rationale_uuid` (`uuid4`) on every accepted write.
  - [ ] write `rationale_inserted_at_utc`, `rationale_text_sha256`.
  - [ ] append immutable JSON event to `rationale-events.jsonl`.
  - [ ] include source JSON checksums and permit checksum in event.

### 2) `validate-ledger-and-checklist-v2.py` (upgrade)

- [x] Add required ledger columns:
  - [ ] `rationale_uuid`, `rationale_inserted_at_utc`, `rationale_text_sha256`
  - [ ] `recommendation_priority`, `recommended_file`, `recommended_section`, `recommendation_used`
  - [ ] `deviation_permit_path`, `deviation_permit_sha256`, `deviation_approved_by`
- [x] Add CLI arguments:
  - [ ] `--events-jsonl`
  - [ ] `--strict-baseline-json`
  - [ ] `--strict-current-json`
  - [ ] `--strict-max-missing` (default `2`)
- [x] UUID/event integrity checks:
  - [ ] every completed row must have valid UUID.
  - [ ] UUID must be unique across completed rows.
  - [ ] matching event record must exist for each completed row.
  - [ ] latest event digest must match current row digest.
- [x] Recommendation/deviation checks:
  - [ ] high/medium non-move rows require permit path, SHA256, and non-empty `deviation_approved_by`.
  - [ ] missing/invalid permit metadata hard-fails.
- [x] Deviation concentration gate:
  - [ ] if deviation permits >30% of high/medium terms in a wave, fail with `FAILED_DEVIATION_CONCENTRATION`.
- [x] Foundational placement gate (hardcoded targets):
  - [ ] validate `after_file` for required terms at Gate A.
  - [ ] fail with `FAILED_FOUNDATIONAL_PLACEMENT` on mismatch.
- [x] Anti-monoculture thresholds (pinned values):
  - [ ] max 60% for any `action_type + reason_code` pair per wave.
  - [ ] max Jaccard similarity 0.80 for any `reason_why` pair in same wave.
  - [ ] reject known boilerplate regex from first invalid run.
  - [ ] waves with >20 terms must use at least 2 distinct `action_type` values.
- [x] Strict non-regression gate:
  - [ ] read baseline/current strict reports.
  - [ ] fail if `current_missing > strict_max_missing` and no approved waiver artifact.

### 3) `glossary-batch-orchestrator-v2.py` (upgrade)

- [x] Add script wiring arguments:
  - [ ] `--rationale-writer`
  - [ ] `--placement-json`
  - [ ] `--divergence-json`
  - [ ] `--events-jsonl`
  - [ ] `--strict-baseline-json`
- [x] Prompt hardening:
  - [ ] require `record-rationale-v2.py` invocation per completed term.
  - [ ] prohibit direct rationale/decision edits in ledger.
  - [ ] include batch term-lock manifest in prompt context.
- [ ] Batch gates:
  - [ ] pre/post strict check run for each batch.
  - [ ] validator run must include events-jsonl and strict-baseline checks.
  - [ ] quarantine any term lacking UUID event/permit compliance.
  - [ ] block commit on strict regression or concentration failures.
- [ ] Batch summary additions:
  - [ ] recommendation compliance rate
  - [ ] deviation permit count
  - [ ] maximum rationale similarity
  - [ ] moved-term count and moved-term list
- [ ] Run-end hard fails:
  - [ ] `FAILED_RECOMMENDATION_LOCK`
  - [ ] `FAILED_UUID_GUARDRAIL`
  - [ ] `FAILED_DEVIATION_CONCENTRATION`
  - [ ] `FAILED_RATIONALE_MONOCULTURE`
  - [ ] `FAILED_STRICT_REGRESSION`
  - [ ] `FAILED_FOUNDATIONAL_PLACEMENT`

### 4) `analyze-rationale-patterns-v2.py` (new, now required)

- [x] Build helper script that computes:
  - [ ] action/reason concentration by wave
  - [ ] pairwise rationale similarity summary
  - [ ] boilerplate hit counts
  - [ ] deviation permit concentration by wave
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

- [x] `record-rationale-v2.py` smoke tests:
  - [x] `--help` works.
  - [x] success case writes UUID and event for a synthetic fixture row.
  - [x] mismatch case hard-fails on term-source lock.
  - [x] non-move high-priority case hard-fails without deviation permit.
  - [x] deviation permit with `approved_by == implementer_id` hard-fails.
- [x] `validate-ledger-and-checklist-v2.py` smoke tests:
  - [x] `--help` works.
  - [x] validates fixture with events and permit metadata.
  - [x] fails on duplicate UUID.
  - [x] fails on concentration threshold breach.
  - [x] fails on strict regression breach.
- [x] `glossary-batch-orchestrator-v2.py` smoke tests:
  - [x] `--help` works.
  - [x] dry-run includes writer/lock requirements in batch prompt.
  - [x] dry-run emits term-lock manifest artifact.

## Pre-Wave entry criteria (all required)

- [ ] All script modifications implemented.
- [ ] All script smoke tests pass with stored outputs.
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
