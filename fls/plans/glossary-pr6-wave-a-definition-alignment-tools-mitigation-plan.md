# PR6 Wave A definition-alignment tooling mitigation plan

## Objective

- [ ] Close the marker-swap loophole so completed terms represent real definition migration, not superficial `:dt:`/`:t:` swaps.
  - [ ] Enforce glossary-definition alignment as the primary quality signal.
  - [ ] Ensure declared operation (`promote|insert|adapt`) matches actual diff reality.
  - [ ] Add validator-side structural checks so writer bypass/manual ledger edits are still blocked.
  - [ ] Preserve implementer/reviewer role separation and existing deviation lifecycle controls.
  - [ ] Block Wave B unless Wave A quality gate evidence is present and passing.

## Scope and non-scope

- [ ] Scope this plan to tooling changes and validation artifacts.
  - [ ] `reports/record-rationale-v3.py`
  - [ ] `reports/validate-ledger-and-checklist-v3.py`
  - [ ] `reports/glossary-batch-orchestrator-v3.py`
  - [ ] `reports/analyze-rationale-patterns-v3.py`
  - [ ] shared definition-alignment helper module (new, under `reports/`) to keep writer/validator logic identical
  - [ ] recovery-guardrail fixtures/smokes under `reports/.../validation/recovery-guardrails-v3/`
- [ ] Keep Wave A prose fixup authoring itself in the execution plan (outside this tooling-only document).
  - [ ] This plan prepares enforcement logic that must pass before rerun acceptance.

## Reviewer feedback incorporation (tracking)

- [ ] Address feedback issue #1: insert-vs-promote diff cross-check.
  - [ ] Add batch/file net-line delta capture and validator enforcement for `insert`.
- [ ] Address feedback issue #2: generalized compound-term split detection.
  - [ ] Add structural check in writer and validator (not hardcoded term list).
- [ ] Address feedback issue #3: deterministic multi-sentence glossary parsing.
  - [ ] Specify canonical sentence extraction rules in code and docs.
- [ ] Address feedback issue #4: permissive `adapt` acceptance.
  - [ ] Keep threshold and add structural subject-form requirement.
- [ ] Address feedback issue #5: unspecified similarity tolerance.
  - [ ] Enforce exact equality between stored and recomputed similarity.
- [ ] Address feedback issue #6: incomplete Wave A dataset.
  - [ ] Revalidate all 15 WA terms through updated writer fields before gate.
- [ ] Address feedback issue #7: ambiguous validator file state.
  - [ ] Pin chapter extraction to committed `HEAD` state.
- [ ] Address feedback issue #8: hash target ambiguity.
  - [ ] Hash normalized text and persist normalization version metadata.
- [ ] Address v2 clarification #1: define "content word" for compound-split checks.
  - [ ] Pin stopword list, role-prefix exemptions, and punctuation handling in writer and validator.
  - [ ] Hardcode the same list in both scripts (no dynamic derivation).
- [ ] Address v2 clarification #2: insert diff cross-check whole-file edge case.
  - [ ] Prefer hunk-scoped insertion checks tied to the `:dt:` location.
  - [ ] Keep whole-file net-positive check as fallback with documented limitation and commit-splitting rule.
- [ ] Address v2 clarification #3: Phase 3 sequencing for known-failing terms.
  - [ ] Split revalidation into 3a (12 promote candidates) and 3b (3 prose-fixup insert candidates).
  - [ ] Require fixup commit before 3b writer runs.
- [ ] Address v3 observation #1: stopword list should cover common function words.
  - [ ] Extend exempt stopword set with `not`, `no`, `but`, `as`, `if`, `so`.
  - [ ] Add fixture coverage for these tokens so they do not trigger compound-split failure.
- [ ] Address v3 observation #2: diff-check mode selection must be explicit.
  - [ ] Define hunk-vs-fallback selection logic in validator section.
  - [ ] Define orchestrator artifact contract required for hunk mode activation.
- [ ] Address script-review critical finding #1: hunk insert check can misclassify marker swaps.
  - [ ] Replace naive `+ line contains :dt:` detection with paired add/remove analysis scoped to target term and destination anchor.
  - [ ] Treat `:t:` -> `:dt:` replacement as swap (not insertion) and fail `FAILED_INSERT_DIFF_MISMATCH`.
  - [ ] In hunk mode, do not downgrade to fallback when anti-swap checks fail; fallback is only for unavailable/incomplete hunk metadata.
  - [ ] Add dedicated swap-as-insert smoke fixture and expected fail artifact.
- [ ] Address script-review medium finding #2: writer/validator Jaccard implementations diverge structurally.
  - [ ] Route both scripts through one shared helper implementation for similarity tokenization and Jaccard math.
  - [ ] Remove redundant validator-only tokenization path (`re.split`, extra lower/strip) on already normalized text.
- [ ] Address script-review medium finding #3: subject-form enforcement is writer-only.
  - [ ] Re-run subject-form checks in validator for `promote` and `insert`.
  - [ ] Re-run subject-form checks in validator for marginal `adapt` cases.
  - [ ] Emit explicit structural-failure code for subject-form violations.
- [ ] Address script-review minor finding #4: shared stopword constant couples unrelated policies.
  - [ ] Separate compound-split stopword policy from similarity normalization policy (even if initial values match).
  - [ ] Version and document both policies independently to avoid accidental drift.

## Data model additions (ledger + events)

- [ ] Add required recovery fields for completed terms.
  - [ ] `definition_operation` (`promote|insert|adapt`)
  - [ ] `definition_similarity` (0.0-1.0 float serialized deterministically)
  - [ ] `glossary_definition_sha256` (hash of normalized glossary text)
  - [ ] `chapter_definition_sha256` (hash of normalized chapter text)
  - [ ] `definition_normalization_version` (e.g. `v1`)
- [ ] Add matching event payload fields to `reports/rationale-events.jsonl`.
  - [ ] Persist all fields listed above.
  - [ ] Persist extraction scope metadata (`definition_sentence_count`, `glossary_entry_anchor`).

## Canonical definition extraction rules (shared)

- [ ] Implement and document deterministic glossary parsing.
  - [ ] Start at glossary entry for target term.
  - [ ] Include sentence containing `:dt:`term`` as canonical sentence 1.
  - [ ] Include following definitional continuation sentence(s) before next glossary heading.
  - [ ] Exclude standalone `See :s:`...`` cross-reference lines.
  - [ ] Exclude non-definitional metadata lines/anchors.
- [ ] Implement and document chapter-side extraction.
  - [ ] Resolve the row target from `after_file` + `after_dp_id`.
  - [ ] Extract the chapter `:dt:` sentence for the target term.
  - [ ] Reject when `:dt:` appears as a substring inside a compound term.

## Compound split token policy (shared)

- [ ] Define `content word` deterministically for token after `:dt:`term``.
  - [ ] Token must be alphabetic to be eligible.
  - [ ] Exempt stopwords: `is`, `are`, `was`, `were`, `a`, `an`, `the`, `of`, `in`, `that`, `which`, `and`, `or`, `for`, `with`, `by`, `to`, `from`, `not`, `no`, `but`, `as`, `if`, `so`.
  - [ ] Exempt RST role-prefix tokens: `:t:`, `:s:`, `:c:`, `:dp:`, `:dc:`, `:ds:`.
  - [ ] Exempt punctuation/whitespace/non-alphabetic tokens.
  - [ ] Treat all other immediate-following tokens as content words and fail with `FAILED_COMPOUND_DT_SPLIT`.
- [ ] Use the same hardcoded policy in writer and validator.
  - [ ] Add unit fixtures that prove both implementations classify tokens identically.

## Subject-form policy (shared)

- [ ] Define subject-form predicate deterministically.
  - [ ] Accept optional bullet/article prefix before `:dt:`term`` with required token boundary after term marker.
  - [ ] Reject cases where `:dt:`term`` is used as part of a larger token/compound phrase.
  - [ ] Keep predicate implementation byte-for-byte identical between writer and validator via shared helper.
- [ ] Define operation enforcement matrix.
  - [ ] `promote`: subject-form required.
  - [ ] `insert`: subject-form required.
  - [ ] `adapt`: subject-form required when similarity is marginal (`< promote threshold`).
  - [ ] Validator must enforce the same matrix to block writer-bypass/manual-ledger paths.

## `record-rationale-v3.py` changes

- [ ] Extend CLI contract.
  - [ ] Add `--definition-operation` with choices `promote`, `insert`, `adapt`.
  - [ ] Add `--workdir` (required absolute path to step1 worktree).
  - [ ] Add `--glossary-file` (default `src/glossary.rst` resolved under `--workdir`).
- [ ] Add normalization + similarity pipeline.
  - [ ] Strip roles/markup to normalized text.
  - [ ] Normalize case and punctuation consistently.
  - [ ] Compute deterministic Jaccard on normalized token sets through shared helper used by validator.
  - [ ] Keep similarity stopword list independent from compound-split stopword list.
- [ ] Add structural definition checks (writer-time hard fail).
  - [ ] Reject if token immediately after `:dt:`term`` is a content word (per shared token policy).
  - [ ] Require subject-form definition structure for `promote` and `insert`.
  - [ ] Require subject-form definition structure for `adapt` when similarity is marginal.
- [ ] Enforce operation-specific thresholds.
  - [ ] `promote`: `definition_similarity >= 0.72`.
  - [ ] `insert`: `definition_similarity >= 0.85`.
  - [ ] `adapt`: `definition_similarity >= 0.55` and `review_attention=required`.
- [ ] Persist new fields to ledger and event stream.
  - [ ] Write hashes over normalized text (not raw RST).
  - [ ] Write exact serialized similarity and normalization version.

## `validate-ledger-and-checklist-v3.py` changes

- [ ] Require new columns under recovery guardrails.
  - [ ] Fail if any definition-alignment column is missing.
- [ ] Add failure/warning families.
  - [ ] `FAILED_GLOSSARY_ALIGNMENT`
  - [ ] `FAILED_INSERT_DIFF_MISMATCH`
  - [ ] `FAILED_COMPOUND_DT_SPLIT`
  - [ ] `FAILED_SUBJECT_FORM`
  - [ ] `FAILED_SIMILARITY_DRIFT`
  - [ ] `WARN_GLOSSARY_MISMATCH`
- [ ] Add glossary-alignment CLI options.
  - [ ] `--workdir`
  - [ ] `--glossary-file`
  - [ ] `--min-glossary-similarity` (default `0.50`)
  - [ ] `--min-promote-similarity` (default `0.72`)
  - [ ] `--glossary-ack-json` (reviewer acknowledgment list for gate/final)
  - [ ] `--diff-mode` (default `head`, committed state only)
- [ ] Recompute and verify (do not trust stored values).
  - [ ] Re-extract glossary canonical text and chapter definition text.
  - [ ] Recompute normalized similarity using the same shared Jaccard/tokenization helper as writer.
  - [ ] Require exact equality with stored `definition_similarity`.
  - [ ] Require exact hash match with stored normalized hashes.
- [ ] Enforce insert-vs-promote diff truth.
  - [ ] Mode selection rule: use hunk mode when `batch-XXX-diff-audit.json` exists and includes hunk metadata for target `after_file` + destination anchor.
  - [ ] Mode selection fallback: use whole-file mode only when required hunk metadata is unavailable/incomplete (not when hunk evidence is contradictory).
  - [ ] Primary hunk check: for `insert`, parse paired added/removed lines at destination and require term-scoped net insertion.
  - [ ] Anti-swap rule: treat `:t:` -> `:dt:` replacement (or `:dt:` replacement with no net sentence addition) as non-insert and fail.
  - [ ] No silent downgrade rule: if hunk mode is active and anti-swap/net-insert checks fail, emit `FAILED_INSERT_DIFF_MISMATCH` directly.
  - [ ] Fallback check: if hunk mapping is unavailable, require positive whole-file net line delta in `after_file`.
  - [ ] Document fallback limitation: same-file deletions can mask valid inserts when using whole-file net delta.
  - [ ] Enforce fallback hygiene rule: when fallback mode is active, `insert` terms must avoid unrelated same-file deletions or be split into separate commits.
  - [ ] For `promote`, allow marker-only edits and no required net line increase.
  - [ ] Fail contradictory declarations (`insert` with zero/negative net lines).
- [ ] Enforce mode-specific outcomes.
  - [ ] `progress`: emit `WARN_GLOSSARY_MISMATCH` with ID list.
  - [ ] `gate`/`final`: fail unacknowledged mismatches.
  - [ ] Always hard-fail low-similarity `promote`, `insert` diff mismatch, compound split, and subject-form violations.
- [ ] Pin validator extraction state.
  - [ ] Read chapter files from committed `HEAD` only.
  - [ ] Reject/abort if called while required commit context is unavailable.
  - [ ] Apply shared compound token policy in validator extraction path before similarity evaluation.
  - [ ] Apply shared subject-form policy in validator extraction path before final operation acceptance.

## `glossary-batch-orchestrator-v3.py` changes

- [ ] Strengthen prompt instructions to prohibit shortcut behavior.
  - [ ] State glossary definition text is canonical.
  - [ ] Require true `promote` only when equivalent sentence already exists.
  - [ ] Require `insert` when equivalent sentence does not exist.
  - [ ] Forbid marker swap on non-definitional sentences.
- [ ] Update prompt command templates.
  - [ ] Include new writer args (`--definition-operation`, `--workdir`, `--glossary-file`).
  - [ ] Include validator args (`--workdir`, `--glossary-file`, thresholds, ack file).
- [ ] Add batch diff telemetry for operation cross-check.
  - [ ] Capture `git diff --numstat` for commit and store per-file net lines in `batch-XXX-summary.json`.
  - [ ] Capture hunk-level patch metadata needed to map insert checks to destination `:dt:` locations.
  - [ ] Persist per-term hunk add/remove marker counts for `:dt:` and `:t:` term lines.
  - [ ] Persist explicit `swap_detected` signal when marker replacement occurs without net sentence insertion.
  - [ ] Emit artifact (e.g. `batch-XXX-diff-audit.json`) with per-term check mode (`hunk` vs `fallback`) and pass/fail evidence.
  - [ ] Persist per-term evidence source (`hunk` metadata path or summary fallback field) for reviewer traceability.
- [ ] Expand local term-row validation.
  - [ ] Require `definition_operation` and parseable `definition_similarity`.
  - [ ] Require `definition_normalization_version` and both definition hashes.
- [ ] Add Wave A quality gate before WB selection.
  - [ ] Require `wa-quality-gate.json` with reviewer pass metadata.
  - [ ] Require no unresolved high-severity glossary-alignment failures.
  - [ ] Hard stop with explicit message if gate preconditions are not satisfied.
- [ ] Ensure alignment validator executes post-commit for authoritative checks.
  - [ ] Keep pre-commit validation limited to progress sanity.
  - [ ] Gate/final alignment enforcement runs against committed artifacts.

## `analyze-rationale-patterns-v3.py` changes

- [ ] Extend analysis outputs for definition-alignment observability.
  - [ ] Count operations by wave (`promote|insert|adapt`).
  - [ ] Report similarity distribution (`min`, `p50`, `p95`, `max`).
  - [ ] Report IDs below `min-glossary-similarity`.
  - [ ] Report contradictory operation signals (e.g. insert with non-positive line deltas).
  - [ ] Report swap-detected insert contradictions from diff-audit artifacts.
  - [ ] Report subject-form validation failure counts by operation.
- [ ] Surface metrics in both JSON and Markdown.

## Fixture and smoke-test updates

- [ ] Add canonical extraction fixtures.
  - [ ] Multi-sentence glossary entry with continuation sentence.
  - [ ] Glossary entry with standalone `See :s:`...`` line excluded.
- [ ] Add structural trap fixtures.
  - [ ] Compound split after `:dt:`term`` fails (`FAILED_COMPOUND_DT_SPLIT`).
  - [ ] Stopword-following token after `:dt:`term`` does not fail compound-split check.
  - [ ] Function-word-following token (`not`, `no`, `but`, `as`, `if`, `so`) after `:dt:`term`` does not fail compound-split check.
  - [ ] RST-role-following token after `:dt:`term`` does not fail compound-split check.
  - [ ] Non-definitional sentence with promoted marker fails.
- [ ] Add operation truth fixtures.
  - [ ] `promote` good case (high similarity, no inserted prose needed).
  - [ ] `insert` good case (high similarity + positive hunk insertion at destination).
  - [ ] `insert` bad case (high similarity but zero net lines).
  - [ ] `insert` bad case (marker swap `:t:` -> `:dt:` with no net prose insertion) fails in hunk mode.
  - [ ] `insert` edge case: valid insertion + unrelated same-file deletion (fails in fallback mode, passes in hunk mode).
  - [ ] `adapt` case (passes threshold + review attention required).
- [ ] Add validator parity fixtures.
  - [ ] Subject-form invalid `promote` row fails validator even if writer is bypassed.
  - [ ] Subject-form invalid `insert` row fails validator even if writer is bypassed.
  - [ ] Subject-form invalid marginal `adapt` row fails validator.
  - [ ] Writer/validator similarity recompute parity holds for normalized edge cases.
- [ ] Add policy-separation regression fixtures.
  - [ ] Updating compound-split stopword list does not silently change similarity math.
  - [ ] Updating similarity-stopword list does not silently change compound-split classification.
- [ ] Add Wave A-specific regression fixtures.
  - [ ] `method` compound split failure.
  - [ ] `item` macro-expansion non-definition failure.
  - [ ] `field` enum-narrowing non-definition failure.
- [ ] Refresh smoke summaries/review index.
  - [ ] Include all new warning/failure codes.
  - [ ] Include command examples with all new CLI args.

## Execution order (tooling)

- [ ] Phase 1: implement script changes.
  - [ ] Update writer.
  - [ ] Update validator.
  - [ ] Update orchestrator.
  - [ ] Update analyzer.
- [ ] Phase 2: validate tooling behavior.
  - [ ] `python3 -m py_compile` for modified scripts.
  - [ ] Run fixture-backed smokes for new codes and operation checks.
  - [ ] Run dedicated swap-as-insert exploit smoke and confirm `FAILED_INSERT_DIFF_MISMATCH`.
  - [ ] Run validator writer-bypass subject-form smokes and confirm `FAILED_SUBJECT_FORM`.
  - [ ] Store artifacts under recovery-guardrails validation directory.
- [ ] Phase 3a: apply updated tooling to 12 Wave A terms already expected to align via `promote`.
  - [ ] Re-run rationale recording for 12 non-fixup IDs using `--definition-operation promote`.
  - [ ] Ensure 12 rows carry hashes/similarity/operation fields and pass alignment checks.
- [ ] Phase 3b: process 3 Wave A fixup terms requiring prose insertion (`method`, `item`, `field`).
  - [ ] Author and commit prose fixups first.
  - [ ] Re-run rationale recording for the 3 fixup IDs using `--definition-operation insert`.
  - [ ] Ensure all 15 rows now carry hashes/similarity/operation fields.
  - [ ] Produce WA alignment report artifact for reviewer gate.
- [ ] Phase 4: readiness gate.
  - [ ] Confirm Wave B is blocked without `wa-quality-gate.json` pass artifact.
  - [ ] Confirm gate/final fail unresolved high-severity alignment issues.

## Acceptance criteria

- [ ] Tools block shortcut behavior that previously passed Wave A.
  - [ ] Compound split markers are rejected.
  - [ ] Non-definitional promoted sentences are rejected.
  - [ ] Marker-swap-as-insert exploit is rejected in hunk mode.
- [ ] Operation declarations are provably consistent with git diff reality.
  - [ ] `insert` requires term-scoped net insertion (not just marker replacement).
  - [ ] Validator output records which diff-check mode (`hunk` or `fallback`) was used per `insert` term.
- [ ] Alignment math and hashes are deterministic and reproducible.
  - [ ] Stored/recomputed similarity equality is exact.
  - [ ] Writer and validator use one shared similarity implementation path.
  - [ ] Hashes represent normalized text with explicit version metadata.
- [ ] Structural checks are enforced in both writer and validator.
  - [ ] Validator catches subject-form failures even when ledger rows are edited manually.
- [ ] All 15 WA terms are represented in the new alignment data model.
- [ ] Progress mode emits mismatch warnings; gate/final mode blocks unresolved mismatches.
- [ ] Wave B remains blocked until explicit Wave A quality gate pass artifact exists.
