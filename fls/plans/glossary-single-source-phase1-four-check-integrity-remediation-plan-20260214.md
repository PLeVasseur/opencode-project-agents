# Glossary Single-Source Phase1 Four-Check Integrity Remediation Checklist (Crash-Resumable)

Date: 2026-02-14

## Objective

- [ ] Make all four verifier checks pass (`exit 0` + `result: no differences under configured comparison policy.`):
  - [ ] `diff-upstream-main-vs-commit3.txt`
  - [ ] `diff-commit3-vs-commit4.txt`
  - [ ] `diff-upstream-main-vs-commit4.txt`
  - [ ] `capstone-repro-commit4.txt`
- [ ] Keep strict stack topology: exactly four commits over pinned `UPSTREAM_MAIN_PIN`.
- [ ] Preserve auditability and crash recovery at every stage boundary.

## Mandatory Checkbox Discipline

- [ ] A stage may start only after all parent-stage checkboxes are checked.
- [ ] A stage may be marked complete only when every child checkbox in that stage is checked.
- [ ] `*_DONE=1` may be persisted only after checkbox completion for that stage.
- [ ] If a required checkbox cannot be checked, stop immediately and record a blocker in the run log.

## Hard Constraints

- [ ] Do not rerun unrelated migration waves; scope is integrity remediation for the existing four-commit stack.
- [ ] Do not add a fifth commit.
- [ ] Do not push to upstream.
- [ ] Any history rewrite is restricted to `origin/$REPACK_BRANCH` with explicit `--force-with-lease`.
- [ ] All run artifacts are under `$OPENCODE_CONFIG_DIR/reports/`.

## Script-First Execution Policy

- [ ] Use repository scripts as the execution interface; do not invoke `sphinx-build` or `sphinx-autobuild` directly.
- [ ] Build/rebuild docs through `./make.py`.
- [ ] Run HTML parity/repro checks through `./tools/verify-html-diff.py`.
- [ ] Use `./generate-glossary.py` only for source-level glossary parity diagnostics.

## Canonical Inputs and Paths

- [ ] Canonical relayer state inputs:
  - [ ] `REPO_ROOT_EXPECTED=/home/pete.levasseur/project/fls`
  - [ ] `STATE_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214.state.env`
  - [ ] `REPORT_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214.md`
  - [ ] `REPACK_BRANCH=glossary-single-source-phase1-repack-upstream-main`
  - [ ] `UPSTREAM_MAIN_PIN=fb8a46795eda1f1db5e3232002fd94a270bfbffd`
- [ ] Remediation run coordination files:
  - [ ] `RUN_LOCK_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-four-check-remediation.lock`
  - [ ] `RUN_SUMMARY_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-four-check-remediation-summary.md`

## New-Session Handoff Contract (Mandatory)

- [ ] Validate repository context before any stage transitions:
  - [ ] `test "$(git rev-parse --show-toplevel)" = "$REPO_ROOT_EXPECTED"`
  - [ ] `test -f "$REPO_ROOT_EXPECTED/make.py"`
  - [ ] `test -f "$REPO_ROOT_EXPECTED/tools/verify-html-diff.py"`
- [ ] Validate branch context before mutation:
  - [ ] If local `$REPACK_BRANCH` exists, switch to it.
  - [ ] Else create it tracking `origin/$REPACK_BRANCH`.
  - [ ] Confirm `git rev-parse --abbrev-ref HEAD` equals `$REPACK_BRANCH`.
- [ ] Record handoff snapshot under run artifacts:
  - [ ] Write `handoff-context.txt` containing `HEAD`, `origin/$REPACK_BRANCH`, `UPSTREAM_MAIN_PIN`, and current timestamp.

## Fresh-or-Resume Contract (Mandatory)

- [ ] Run selection behavior:
  - [ ] If `REMEDIATION_RUN_ID` is set and `$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-four-check-remediation-$REMEDIATION_RUN_ID/remediation.state.env` exists, validate it; if invalid/corrupt, stop immediately.
  - [ ] Else scan `$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-four-check-remediation-*/remediation.state.env` and select newest incomplete (`M10_DONE!=1`).
  - [ ] If multiple candidates share identical `mtime`, break ties by lexicographically greatest run path.
  - [ ] During scan-mode, quarantine corrupt state files (`*.corrupt`) and continue scanning older candidates.
  - [ ] Else create new run via Stage M0.
- [ ] New run bootstrap values:
  - [ ] `REMEDIATION_RUN_ID=$(date -u +%Y%m%dT%H%M%SZ)`
  - [ ] `RUN_ROOT=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-four-check-remediation-$REMEDIATION_RUN_ID`
  - [ ] `RUN_STATE_FILE=$RUN_ROOT/remediation.state.env`
  - [ ] `RUN_CHECKLIST_STATE_FILE=$RUN_ROOT/checklist.state.env`
  - [ ] `RUN_LOG=$RUN_ROOT/remediation.log`
  - [ ] `RUN_ARTIFACT_ROOT=$RUN_ROOT/artifacts`
- [ ] Resume semantics:
  - [ ] Load `RUN_STATE_FILE`.
  - [ ] Validate parseability (`bash -n`) before sourcing state.
  - [ ] Validate parseability (`bash -n`) before sourcing checklist state.
  - [ ] Validate immutable keys before any mutation.
  - [ ] Execute Stage M1b reconciliation to select resume stage.
  - [ ] Do not rerun completed stages unless reconciliation requires it.

## Checklist State Enforcement (Mandatory)

- [ ] Child checkboxes must be mirrored in `RUN_CHECKLIST_STATE_FILE` as machine-validated keys.
- [ ] Checkbox key format:
  - [ ] `CB_<STAGE>_<GROUP>_<ITEM>=1` (for example `CB_M7_VERIFY_REF_UPSTREAM_COMMIT3=1`).
  - [ ] Unchecked items are absent or `0`.
- [ ] Stage completion policy:
  - [ ] `M*_DONE=1` is forbidden unless all required `CB_M*_...` keys are `1`.
  - [ ] Persist `M*_CHECKLIST_DONE=1` only after required checkbox keys validate.
  - [ ] At minimum every stage records `CB_M*_STAGE_START=1` and `CB_M*_STAGE_COMPLETE=1`.
- [ ] Resume policy:
  - [ ] If `M*_DONE=1` but `M*_CHECKLIST_DONE!=1`, treat as inconsistent state and reconcile by rerunning that stage.
  - [ ] If checklist state is missing/corrupt, stop and log blocker.
- [ ] Checklist state writes are atomic (`*.tmp` + rename), never in-place edits.
- [ ] Checklist schema synchronization:
  - [ ] Persist `CHECKLIST_SCHEMA_VERSION=2` in `RUN_CHECKLIST_STATE_FILE`.
  - [ ] On resume, backfill any missing required `CB_*` keys to `0` atomically before stage validation.
  - [ ] Log every backfilled key in `RUN_LOG` and persist `CB_SCHEMA_SYNC=1`.
  - [ ] Required keys added by this revision are present:
    - [ ] `CB_M3_M7_BLOCKER_AUTHORITATIVE`
    - [ ] `CB_M3_M7_BLOCKER_SIGNATURE`
    - [ ] `CB_M3_M7_BLOCKER_MACROS_DIFF`
    - [ ] `CB_M3_M7_BLOCKER_ADVISORY`
    - [ ] `CB_M4_MACROS_CONTIGUOUS_LIST`
    - [ ] `CB_M4_MACROS_NO_EXTRA_CONTAINERS`
    - [ ] `CB_M7_TRIAGE_DEBUG_EXPORT`
    - [ ] `CB_M7_TRIAGE_DEBUG_DIFFS`
    - [ ] `CB_M7_TRIAGE_SIGNATURE`
    - [ ] `CB_M7_TRIAGE_FIX_FIRST`
    - [ ] `CB_M7_TRIAGE_RERUN_ALL`

## Crash-Resilient State Model (Mandatory)

- [ ] Immutable keys persisted in `RUN_STATE_FILE`:
  - [ ] `REMEDIATION_RUN_ID`, `RUN_ROOT`, `RUN_STATE_FILE`, `RUN_CHECKLIST_STATE_FILE`, `REPACK_BRANCH`, `UPSTREAM_MAIN_PIN`.
  - [ ] `CANONICAL_COMMIT1_SHA`, `CANONICAL_COMMIT2_SHA`, `CANONICAL_COMMIT3_SHA`, `CANONICAL_COMMIT4_SHA`, `OLD_COMMIT4_SHA`.
  - [ ] `STATE_FILE`, `REPORT_FILE`, `RUN_SUMMARY_FILE`.
- [ ] Active commit pointer keys (mutable across rewrite stages):
  - [ ] `COMMIT1_SHA`, `COMMIT2_SHA`, `COMMIT3_SHA`, `COMMIT4_SHA`.
  - [ ] `COMMIT1_SHA..COMMIT4_SHA` must be atomically promoted to rewritten values before Stage M7 starts.
- [ ] State schema synchronization:
  - [ ] Persist `STATE_SCHEMA_VERSION=2` in `RUN_STATE_FILE`.
  - [ ] On resume from older schema, if `CANONICAL_COMMIT*_SHA` keys are missing, backfill them from canonical `STATE_FILE` during Stage M1.
  - [ ] Log every state-key backfill in `RUN_LOG` and persist `STATE_SCHEMA_SYNC=1`.
- [ ] Stage progress keys:
  - [ ] `CURRENT_STAGE`
  - [ ] `M0_DONE`, `M1_DONE`, `M1B_DONE`, `M2_DONE`, `M3_DONE`, `M4_DONE`, `M5_DONE`, `M6_DONE`, `M7_DONE`, `M8_DONE`, `M9_DONE`, `M9B_DONE`, `M10_DONE`
  - [ ] `M0_CHECKLIST_DONE`, `M1_CHECKLIST_DONE`, `M1B_CHECKLIST_DONE`, `M2_CHECKLIST_DONE`, `M3_CHECKLIST_DONE`, `M4_CHECKLIST_DONE`, `M5_CHECKLIST_DONE`, `M6_CHECKLIST_DONE`, `M7_CHECKLIST_DONE`, `M8_CHECKLIST_DONE`, `M9_CHECKLIST_DONE`, `M9B_CHECKLIST_DONE`, `M10_CHECKLIST_DONE`
- [ ] Critical value keys:
  - [ ] `OLD_COMMIT4_SHA`, `NEW_COMMIT4_SHA`, `OLD_REMOTE_SHA`, `REPACK_REMOTE_SHA`
  - [ ] `RC_UPSTREAM_VS_COMMIT3`, `RC_COMMIT3_VS_COMMIT4`, `RC_UPSTREAM_VS_COMMIT4`, `RC_REPRO_COMMIT4`
  - [ ] `RESULT_UPSTREAM_VS_COMMIT3`, `RESULT_COMMIT3_VS_COMMIT4`, `RESULT_UPSTREAM_VS_COMMIT4`, `RESULT_REPRO_COMMIT4`
- [ ] Push/finalization keys:
  - [ ] `PUSH_ATTEMPTED`, `PUSH_CONFIRMED`, `PENDING_CANONICAL_UPDATE`, `CANONICAL_STATE_UPDATED`, `REPORT_APPENDED`, `RUN_SUMMARY_UPDATED`
- [ ] Atomic persistence discipline:
  - [ ] Write updates to `RUN_STATE_FILE.tmp`.
  - [ ] Validate temp file parseability before replace.
  - [ ] Replace with atomic rename only after validation.
  - [ ] Never edit `RUN_STATE_FILE` in place.
- [ ] Idempotent finalization discipline:
  - [ ] Include `REMEDIATION_RUN_ID` marker when appending canonical report.
  - [ ] On resume, skip duplicate append when marker already exists.
  - [ ] Include `REMEDIATION_RUN_ID` marker in `RUN_SUMMARY_FILE` and skip duplicate summary append on resume.

## Stage M0 - Bootstrap, Locking, and State Initialization

- [ ] Stage checkpointing:
  - [ ] Persist `CURRENT_STAGE=M0`.
  - [ ] On completion persist `M0_DONE=1`.
- [ ] Environment/tool sanity:
  - [ ] `printenv OPENCODE_CONFIG_DIR` matches expected root.
  - [ ] `test "$(git rev-parse --show-toplevel)" = "$REPO_ROOT_EXPECTED"`.
  - [ ] `command -v git`, `uv`, `python3`.
  - [ ] `test -x ./make.py` and `test -x ./tools/verify-html-diff.py`.
  - [ ] `./make.py --help` and `./tools/verify-html-diff.py --help` complete successfully.
  - [ ] `uv sync --frozen`.
- [ ] Deterministic execution env:
  - [ ] `TZ=UTC`, `LANG=C.UTF-8`, `LC_ALL=C.UTF-8`, `PYTHONHASHSEED=0`, `umask 022`.
- [ ] Single-writer lock handling (`RUN_LOCK_FILE`):
  - [ ] If lock exists, parse `PID/HOST/CREATED_AT`.
  - [ ] Validate active lock (host match, pid alive, owner match, expected command line).
  - [ ] If active lock is valid, stop immediately.
  - [ ] If stale, archive lock content in `RUN_LOG` and replace lock.
  - [ ] Install cleanup path to remove lock on normal/failure exit.
- [ ] Initialize or load `RUN_STATE_FILE`:
  - [ ] New run: initialize `STATE_SCHEMA_VERSION=2`, immutable keys, all stage flags to `0`, push/finalization flags to `0`.
  - [ ] Resume run: validate parseability, keep existing progress flags, and defer immutable key completeness checks until Stage M1 schema synchronization completes.
- [ ] Initialize or load `RUN_CHECKLIST_STATE_FILE`:
  - [ ] New run: create checklist state with `CHECKLIST_SCHEMA_VERSION=2` and all required `CB_*` keys initialized to `0`.
  - [ ] Resume run: validate presence/parseability, backfill missing required `CB_*` keys to `0`, and keep existing `CB_*` progress.
  - [ ] Persist `CB_M0_STAGE_START=1` and `CB_M0_STAGE_COMPLETE=1` before `M0_DONE=1`.

## Stage M1 - Canonical State Load and Invariant Validation

- [ ] Stage checkpointing:
  - [ ] Persist `CURRENT_STAGE=M1`.
  - [ ] On completion persist `M1_DONE=1`.
- [ ] Canonical state load:
  - [ ] `test -f "$STATE_FILE"` and source it.
  - [ ] Require non-empty `UPSTREAM_MAIN_PIN`, `COMMIT1_SHA..COMMIT4_SHA`, `REPACK_BRANCH`.
  - [ ] Run state schema synchronization for canonical baseline keys:
    - [ ] If missing, backfill `CANONICAL_COMMIT1_SHA..CANONICAL_COMMIT4_SHA` from canonical `COMMIT1_SHA..COMMIT4_SHA`.
    - [ ] Persist `STATE_SCHEMA_SYNC=1` after atomic write and log migrated keys.
  - [ ] Persist canonical immutable identity baseline from canonical state: `CANONICAL_COMMIT1_SHA`, `CANONICAL_COMMIT2_SHA`, `CANONICAL_COMMIT3_SHA`, `CANONICAL_COMMIT4_SHA`, and `OLD_COMMIT4_SHA=$CANONICAL_COMMIT4_SHA`.
  - [ ] Persist active commit pointers for execution:
    - [ ] New run: initialize `COMMIT1_SHA=$CANONICAL_COMMIT1_SHA`, `COMMIT2_SHA=$CANONICAL_COMMIT2_SHA`, `COMMIT3_SHA=$CANONICAL_COMMIT3_SHA`, `COMMIT4_SHA=$CANONICAL_COMMIT4_SHA`.
    - [ ] Resume run: preserve existing `COMMIT1_SHA..COMMIT4_SHA`; only backfill missing keys from canonical baseline.
- [ ] Topology and ancestry checks:
  - [ ] Verify commit objects exist.
  - [ ] Verify exactly 4 commits over `UPSTREAM_MAIN_PIN` on current branch tip.
  - [ ] Verify parent chain preserves commit1->commit2->commit3->commit4 order.
- [ ] Branch/remote checks:
  - [ ] `git fetch --prune origin`.
  - [ ] Confirm `origin/$REPACK_BRANCH` exists.
  - [ ] Ensure local branch is `$REPACK_BRANCH` (switch existing branch or create tracking branch).
  - [ ] Confirm local branch upstream is `origin/$REPACK_BRANCH`.
  - [ ] Capture `OLD_REMOTE_SHA` and ensure expected starting point is known.
  - [ ] If `M6_DONE=0`, require `HEAD == COMMIT4_SHA` and `origin/$REPACK_BRANCH == COMMIT4_SHA` before rewrite.
- [ ] Safety checks:
  - [ ] No in-progress rebase/merge/cherry-pick operations.

## Stage M1b - Crash Resume Reconciliation

- [ ] Stage checkpointing:
  - [ ] Persist `CURRENT_STAGE=M1b`.
  - [ ] On completion persist `M1B_DONE=1`.
- [ ] Resume decision logic:
  - [ ] If any completed stage has `M*_CHECKLIST_DONE!=1`, resume from that stage (not the next stage).
  - [ ] If `PUSH_ATTEMPTED=1` and `PUSH_CONFIRMED=0`, fetch remote and resolve push outcome.
  - [ ] If `M9_DONE=1` and (`CANONICAL_STATE_UPDATED=0` or `REPORT_APPENDED=0`), resume at `M9b` only.
  - [ ] If `M7_DONE=1` and `M8_DONE=0`, resume at `M8`.
  - [ ] If `M6_DONE=1` and `M7_DONE=0`, resume at `M7`.
  - [ ] Else resume at earliest incomplete stage.
- [ ] Record reconciliation:
  - [ ] Append decision and evidence to `RUN_LOG`.
  - [ ] Persist chosen `CURRENT_STAGE`.

## Stage M2 - Forensic Snapshot and Safety Refs

- [ ] Stage checkpointing:
  - [ ] Persist `CURRENT_STAGE=M2`.
  - [ ] On completion persist `M2_DONE=1`.
- [ ] Capture baseline forensic artifacts:
  - [ ] `status-before.txt`
  - [ ] `worktree-before.patch`
  - [ ] Existing report copies (if present) for four-check comparison history
  - [ ] `old-capstone.txt` (old commit4 metadata)
- [ ] Create run-scoped rollback refs:
  - [ ] `backup/glossary-single-source-phase1-four-check-pre-remediation-$REMEDIATION_RUN_ID`
  - [ ] `backup-glossary-single-source-phase1-four-check-pre-remediation-$REMEDIATION_RUN_ID`
  - [ ] Push both refs to origin and verify they resolve to `OLD_COMMIT4_SHA`.

## Stage M3 - Parity Diagnostics (Blocking)

- [ ] Stage checkpointing:
  - [ ] Persist `CURRENT_STAGE=M3`.
  - [ ] On completion persist `M3_DONE=1`.
- [ ] Produce deterministic diagnostics under `RUN_ARTIFACT_ROOT`:
  - [ ] `chapter-macros-materialized-upstream.txt`
  - [ ] `chapter-macros-materialized-current.txt`
  - [ ] `chapter-macros-materialized.diff`
  - [ ] `glossary-term-anchor-map-upstream.tsv`
  - [ ] `glossary-term-anchor-map-current.tsv`
  - [ ] `glossary-term-anchor-map.diff`
  - [ ] `glossary-term-dp-map-upstream.tsv`
  - [ ] `glossary-term-dp-map-current.tsv`
  - [ ] `glossary-term-dp-map.diff`
- [ ] Validate known drift signatures are captured before editing:
  - [ ] Macros hygiene list-depth drift confirmed.
  - [ ] `C signed int type` anchor drift confirmed.
  - [ ] `discriminant type` and `local trait` glossary `:dp:` drifts confirmed.
- [ ] Capture known M7 blocker signature for targeted triage:
  - [ ] Treat `diff-upstream-main-vs-commit3.txt` and `diff-upstream-main-vs-commit4.txt` as authoritative pass/fail artifacts.
  - [ ] If both upstream comparisons change only `macros.html` and `searchindex.js`, record this as the current blocker signature.
  - [ ] Confirm `m7-up-vs-c3-macros.diff` shows Hygiene list-container boundary drift (`</ul><ul>`).
  - [ ] Treat `m7-*-types.diff` and `m7-*-glossary.diff` as advisory unless corroborated by required M7 reports.

## Stage M4 - Source and Tooling Remediation

- [ ] Stage checkpointing:
  - [ ] Persist `CURRENT_STAGE=M4`.
  - [ ] On completion persist `M4_DONE=1`.
- [ ] Fix chapter structure parity:
  - [ ] Adjust `src/macros.rst` hygiene section so chapter-emitted list depth matches upstream.
  - [ ] Keep Hygiene chapter bullets as one contiguous list (upstream-equivalent list container structure).
  - [ ] Preserve glossary export semantics for hygiene terms without introducing extra chapter list containers.
- [ ] Fix glossary anchor and definition-ID parity:
  - [ ] Restore `C signed int type` glossary anchor parity to upstream value.
  - [ ] Restore `discriminant type` glossary `:dp:` to `fls_kqdvWGi9cglm`.
  - [ ] Restore `local trait` glossary `:dp:` to `fls_H5vkbMFvzrFs`.
- [ ] If required, align generator/extension behavior:
  - [ ] Preserve historical upstream-stable anchor text where required.
  - [ ] Keep duplicate detection strict.

## Stage M5 - Pre-Restack Parity Gates

- [ ] Stage checkpointing:
  - [ ] Persist `CURRENT_STAGE=M5`.
  - [ ] On completion persist `M5_DONE=1`.
- [ ] Regenerate and validate source parity before restack:
  - [ ] Run `./make.py --clear` once after remediation edits to validate wrapper-driven build path.
  - [ ] Run `./generate-glossary.py` when refreshing glossary source artifacts for parity diagnostics.
  - [ ] Recompute Stage M3 diagnostics.
  - [ ] `chapter-macros-materialized.diff` is empty (exact-text parity required).
  - [ ] `glossary-term-anchor-map.diff` is empty.
  - [ ] `glossary-term-dp-map.diff` is empty for migrated terms.
- [ ] Working tree discipline:
  - [ ] No unexpected files modified.
  - [ ] No unstaged drift before restack operations.

## Stage M6 - Rebuild Strict Four-Commit Stack

- [ ] Stage checkpointing:
  - [ ] Persist `CURRENT_STAGE=M6`.
  - [ ] On completion persist `M6_DONE=1`.
- [ ] Rebuild stack without adding commit count:
  - [ ] Rewrite from earliest affected boundary while preserving four logical commits.
  - [ ] Preserve intended commit subjects/scopes.
  - [ ] Capture rewritten stack SHAs in order and persist active commit pointers:
    - [ ] `COMMIT1_SHA`, `COMMIT2_SHA`, `COMMIT3_SHA`, `COMMIT4_SHA`.
    - [ ] `NEW_COMMIT4_SHA=$COMMIT4_SHA` for downstream reporting compatibility.
- [ ] Commit-scope allowlist gates (exact changed-path sets):
  - [ ] Generate actual changed-path manifests for `COMMIT1_SHA`, `COMMIT2_SHA`, `COMMIT3_SHA`, `NEW_COMMIT4_SHA` into `RUN_ARTIFACT_ROOT/m6-commit*-files.actual.txt`.
  - [ ] Validate commit1 changed-path set equals exactly:
    - [ ] `README.rst`
    - [ ] `exts/ferrocene_spec/README.rst`
    - [ ] `exts/ferrocene_spec/__init__.py`
    - [ ] `exts/ferrocene_spec/glossary.py`
    - [ ] `generate-glossary-entry.py`
    - [ ] `generate-glossary.py`
    - [ ] `make.py`
    - [ ] `src/glossary.prelude.rst.inc`
  - [ ] Validate commit2 changed-path set equals exactly:
    - [ ] `src/associated-items.rst`
    - [ ] `src/attributes.rst`
    - [ ] `src/concurrency.rst`
    - [ ] `src/entities-and-resolution.rst`
    - [ ] `src/exceptions-and-errors.rst`
    - [ ] `src/expressions.rst`
    - [ ] `src/ffi.rst`
    - [ ] `src/functions.rst`
    - [ ] `src/general.rst`
    - [ ] `src/generics.rst`
    - [ ] `src/glossary.rst`
    - [ ] `src/glossary.rst.inc`
    - [ ] `src/implementations.rst`
    - [ ] `src/inline-assembly.rst`
    - [ ] `src/items.rst`
    - [ ] `src/lexical-elements.rst`
    - [ ] `src/macros.rst`
    - [ ] `src/ownership-and-deconstruction.rst`
    - [ ] `src/patterns.rst`
    - [ ] `src/program-structure-and-compilation.rst`
    - [ ] `src/statements.rst`
    - [ ] `src/types-and-traits.rst`
    - [ ] `src/undefined-behavior.rst`
    - [ ] `src/unsafety.rst`
    - [ ] `src/values.rst`
  - [ ] Validate commit3 changed-path set equals exactly:
    - [ ] `.github/workflows/ci.yml`
    - [ ] `tools/README.rst`
    - [ ] `tools/verify-html-diff.py`
  - [ ] Validate commit4 changed-path set equals exactly:
    - [ ] `.github/workflows/ci.yml`
    - [ ] `README.rst`
    - [ ] `exts/ferrocene_spec/README.rst`
    - [ ] `generate-glossary-entry.py`
    - [ ] `generate-glossary.py`
    - [ ] `make.py`
    - [ ] `src/glossary.rst`
    - [ ] `src/glossary.rst.inc`
    - [ ] `tools/README.rst`
    - [ ] `tools/verify-html-diff.py`
  - [ ] Persist expected manifests under `RUN_ARTIFACT_ROOT/m6-commit*-files.expected.txt` and require diff vs actual to be empty.
- [ ] Topology hard gates:
  - [ ] Exactly four commits over `UPSTREAM_MAIN_PIN`.
  - [ ] Commit order remains tooling -> migration -> ci-verification -> capstone.
  - [ ] Clean index/worktree before verification stage.

## Stage M7 - Four-Check Verification Matrix (All Blocking)

- [ ] Stage checkpointing:
  - [ ] Persist `CURRENT_STAGE=M7`.
  - [ ] On completion persist `M7_DONE=1`.
- [ ] Run all four checks with run-scoped report paths:
  - [ ] `./tools/verify-html-diff.py --mode refs --left-ref $UPSTREAM_MAIN_PIN --right-ref $COMMIT3_SHA --report $RUN_ARTIFACT_ROOT/diff-upstream-main-vs-commit3.txt`
  - [ ] `./tools/verify-html-diff.py --mode refs --left-ref $COMMIT3_SHA --right-ref $NEW_COMMIT4_SHA --report $RUN_ARTIFACT_ROOT/diff-commit3-vs-commit4.txt`
  - [ ] `./tools/verify-html-diff.py --mode refs --left-ref $UPSTREAM_MAIN_PIN --right-ref $NEW_COMMIT4_SHA --report $RUN_ARTIFACT_ROOT/diff-upstream-main-vs-commit4.txt`
  - [ ] `./tools/verify-html-diff.py --mode repro --ref $NEW_COMMIT4_SHA --report $RUN_ROOT/capstone-repro-commit4.txt`
- [ ] Deterministic blocker-evidence capture (required when targeted triage triggers):
  - [ ] Export comparison directories with repository script interface:
    - [ ] `./tools/verify-html-diff.py --mode export-ref --ref $UPSTREAM_MAIN_PIN --output-dir $RUN_ARTIFACT_ROOT/m7-debug-upstream`
    - [ ] `./tools/verify-html-diff.py --mode export-ref --ref $COMMIT3_SHA --output-dir $RUN_ARTIFACT_ROOT/m7-debug-commit3`
  - [ ] Produce deterministic diff artifacts:
    - [ ] `$RUN_ARTIFACT_ROOT/m7-up-vs-c3-macros.diff`
    - [ ] `$RUN_ARTIFACT_ROOT/m7-up-vs-c3-searchindex.diff`
  - [ ] Write `$RUN_ARTIFACT_ROOT/m7-up-vs-c3-provenance.txt` with refs and source file paths used for the two diffs.
- [ ] Targeted triage before wider rewrites:
  - [ ] If upstream comparisons fail with only `macros.html` and `searchindex.js`, resolve Hygiene list structural parity first.
  - [ ] Rerun all four M7 checks after the targeted fix before expanding remediation scope.
- [ ] Persist and validate all results:
  - [ ] Store RCs and result lines in state/log.
  - [ ] All four RCs are `0`.
  - [ ] All four result lines are exactly `result: no differences under configured comparison policy.`
  - [ ] Any non-zero RC or mismatched result line is a mandatory stop.

## Stage M8 - Pre-Push Finalization Prep (State Only)

- [ ] Stage checkpointing:
  - [ ] Persist `CURRENT_STAGE=M8`.
  - [ ] On completion persist `M8_DONE=1`.
- [ ] Generate integrity-chain report:
  - [ ] Write `$RUN_ROOT/integrity-chain.md`.
  - [ ] Include old/new capstone SHAs, all four commands, RCs, and result lines.
  - [ ] Include parity-diagnostics references proving source/anchor/ID parity.
- [ ] Persist provisional markers only:
  - [ ] `PENDING_CANONICAL_UPDATE=1`.
  - [ ] `PROPOSED_COMMIT4_SHA=$NEW_COMMIT4_SHA`.
  - [ ] Do not update canonical state/report before push confirmation.

## Stage M9 - Push Corrected Branch Safely

- [ ] Stage checkpointing:
  - [ ] Persist `CURRENT_STAGE=M9`.
  - [ ] On completion persist `M9_DONE=1`.
- [ ] Push discipline:
  - [ ] Persist `PUSH_ATTEMPTED=1`, `PUSH_CONFIRMED=0` before push.
  - [ ] Push using explicit lease:
    - [ ] `git push --force-with-lease=refs/heads/$REPACK_BRANCH:$OLD_REMOTE_SHA origin HEAD:refs/heads/$REPACK_BRANCH`
  - [ ] Never retry with plain `--force`.
- [ ] Verify push result:
  - [ ] Fetch remote branch.
  - [ ] `REPACK_REMOTE_SHA == NEW_COMMIT4_SHA`.
  - [ ] Persist `PUSH_CONFIRMED=1` and `REPACK_REMOTE_SHA`.

## Stage M9b - Canonical State/Report Finalization (Post-Push)

- [ ] Stage checkpointing:
  - [ ] Persist `CURRENT_STAGE=M9b`.
  - [ ] On completion persist `M9B_DONE=1`.
- [ ] Enforce preconditions:
  - [ ] `PUSH_CONFIRMED=1`.
  - [ ] `REPACK_REMOTE_SHA == NEW_COMMIT4_SHA`.
  - [ ] `PENDING_CANONICAL_UPDATE=1`.
  - [ ] All four check reports are pass (`exit 0`, exact no-differences result line).
- [ ] Update canonical `STATE_FILE` atomically:
  - [ ] `COMMIT4_SHA=$NEW_COMMIT4_SHA`
  - [ ] `PHASE_8_COMMIT4_DONE=1`
  - [ ] `PHASE_9_VERIFY_DONE=1`
  - [ ] `REPACK_REMOTE_SHA=$NEW_COMMIT4_SHA`
  - [ ] `ARTIFACT_ROOT=$RUN_ARTIFACT_ROOT`
  - [ ] `INTEGRITY_CHAIN_REPORT=$RUN_ROOT/integrity-chain.md`
  - [ ] `PHASE_10_STOP_POINT_DONE=1`
- [ ] Append canonical report idempotently:
  - [ ] Include root-cause and remediation narrative.
  - [ ] Include `REMEDIATION_RUN_ID` marker.
  - [ ] Skip duplicate append if marker already exists.
- [ ] Update `RUN_SUMMARY_FILE` idempotently:
  - [ ] Append one run block keyed by `REMEDIATION_RUN_ID` containing branch, old/new commit4, all four RC/result lines, and artifact paths.
  - [ ] Skip duplicate summary append if `REMEDIATION_RUN_ID` marker already exists.
- [ ] Persist finalization markers:
  - [ ] `CANONICAL_STATE_UPDATED=1`
  - [ ] `REPORT_APPENDED=1`
  - [ ] `RUN_SUMMARY_UPDATED=1`

## Stage M10 - Exit, Cleanliness, and Manual Review Stop

- [ ] Stage checkpointing:
  - [ ] Persist `CURRENT_STAGE=M10`.
  - [ ] On completion persist `M10_DONE=1`.
- [ ] Final checks:
  - [ ] `git status --short` is clean.
  - [ ] Run lock is removed on exit.
  - [ ] Run backup refs exist locally and on origin.
  - [ ] `RUN_SUMMARY_FILE` contains exactly one block for current `REMEDIATION_RUN_ID`.
- [ ] Rollback readiness in run log:
  - [ ] Hard rollback SHA documented.
  - [ ] Safety rollback refs documented.
- [ ] Stop at manual-review checkpoint after M10 (do not improvise further branch replacement).

## Crash Window Reconciliation Rules

- [ ] Window A: crash after `M6_DONE=1` and before `M7_DONE=1`.
  - [ ] Verify `HEAD == NEW_COMMIT4_SHA`.
  - [ ] Resume at `M7`.
- [ ] Window B: crash after `M7_DONE=1` and before `PUSH_ATTEMPTED=1`.
  - [ ] Verify all four reports exist and all pass.
  - [ ] Resume at `M8` then `M9`.
- [ ] Window C: crash after `PUSH_ATTEMPTED=1` with unknown push outcome.
  - [ ] Fetch `origin/$REPACK_BRANCH` and compare to `NEW_COMMIT4_SHA`.
  - [ ] If equal, set `PUSH_CONFIRMED=1` and resume at `M9b`.
  - [ ] If not equal, keep `PUSH_CONFIRMED=0` and resume at `M9`.
- [ ] Window D: crash after push success but before canonical finalization.
  - [ ] Resume at `M9b` only.
- [ ] Window E: crash after canonical state update but before report append (or inverse).
  - [ ] Reconcile idempotently using `CANONICAL_STATE_UPDATED`, `REPORT_APPENDED`, and `RUN_SUMMARY_UPDATED`.
  - [ ] Complete only missing finalization step, then continue to `M10`.

## Mandatory Stop Conditions

- [ ] Stop immediately if any stage has unchecked required child checkboxes.
- [ ] Stop immediately if `RUN_STATE_FILE` or `RUN_CHECKLIST_STATE_FILE` is missing or unparsable.
- [ ] Stop immediately if required immutable keys are still missing after state/checklist schema synchronization.
- [ ] Stop immediately if any `M*_DONE=1` without matching `M*_CHECKLIST_DONE=1`.
- [ ] Stop immediately if `M6_DONE=1` and `COMMIT3_SHA`/`NEW_COMMIT4_SHA` are missing or do not resolve to commit objects.
- [ ] Stop immediately if topology is not exactly four commits over `UPSTREAM_MAIN_PIN`.
- [ ] Stop immediately if any commit-scope allowlist manifest differs from expected paths.
- [ ] Stop immediately if parity diagnostics still show source/anchor/ID drift after Stage M4/M5.
- [ ] Stop immediately if any of the four verification checks exits non-zero or has a non-pass result line.
- [ ] Stop immediately if targeted triage is triggered and required M7 deterministic debug artifacts are missing.
- [ ] Stop immediately if explicit `--force-with-lease` cannot prove expected remote SHA.
- [ ] Stop immediately if canonical `STATE_FILE` is modified before push confirmation.
- [ ] Stop immediately if any stage bypasses repo scripts by directly invoking `sphinx-build`/`sphinx-autobuild`.
- [ ] Stop immediately if `RUN_SUMMARY_UPDATED!=1` after Stage `M9b`.

## Exit Criteria

- [ ] All four reports are pass (`exit 0`, exact no-differences result lines).
- [ ] Source/chapter structure parity, glossary anchor parity, and glossary definition-ID parity are proven by saved diagnostics.
- [ ] Branch remains exactly four commits over pinned base.
- [ ] Canonical state/report are updated atomically and idempotently.
- [ ] `RUN_SUMMARY_FILE` is updated idempotently with current `REMEDIATION_RUN_ID` and full verification evidence.
- [ ] Execution stops at manual-review checkpoint with rollback refs preserved.
