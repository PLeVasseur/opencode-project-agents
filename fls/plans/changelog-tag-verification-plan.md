# Plan: Changelog Tag Verification (Extractor + Comparator + E2E)

## Goal
- [ ] Verify that changelog tag detection is correct across the full pipeline:
  - [ ] extraction (`.rst` -> `paragraph-ids-rich.json`),
  - [ ] classification (`base/head rich JSON` -> tags),
  - [ ] end-to-end CLI behavior (`tools/changelog_assistant.py`).

## Explicit reporting exception for this workflow
- [ ] Use `build/` for all verification reports and logs for local/CI traceability.
- [ ] Default report directory: `build/changelog-tag-verification`.
- [ ] Verifier must accept `--report-dir <path>` to override output location.
- [ ] Do not add env-var fallback for report path selection.

## Session bootstrap checklist
- [ ] `printenv OPENCODE_CONFIG_DIR` resolves successfully.
- [ ] `git fetch origin`.
- [ ] `git switch changelog-automation-mainline`.
- [ ] `git pull --ff-only origin changelog-automation-mainline`.
- [ ] `git status --short` is clean before implementation starts.
- [ ] `uv sync` (or equivalent dependency refresh) has run.

## Repository assets to create
- [ ] `tools/changelog_tag_verifier.py` (single entry point).
- [ ] `tools/changelog_tag_cases.json` (manifest of all cases).
- [ ] `tools/changelog_tag_cases.schema.json` (manifest schema).
- [ ] `tools/changelog_tag_fixtures/comparator/<case-id>/base.json`.
- [ ] `tools/changelog_tag_fixtures/comparator/<case-id>/head.json`.
- [ ] `tools/changelog_tag_fixtures/extraction/<case-id>/src/*.rst`.
- [ ] `tools/changelog_tag_fixtures/extraction/<case-id>/expected.json`.

## Harness behavior contract

### CLI and modes
- [ ] Support `--mode compare|extract|e2e|all`.
- [ ] Support `--cases all|<csv case ids>`.
- [ ] Support `--report-dir <path>` with default `build/changelog-tag-verification`.

### Compare mode
- [ ] Load base/head fixture pairs and execute `compare_payloads`.
- [ ] Assert all required tags are present.
- [ ] Assert all forbidden tags are absent.
- [ ] Record observed tags and detailed mismatch diagnostics.

### Extract mode (targeted assertions only)
- [ ] Build extraction mini-doc fixtures with Sphinx dummy builder.
- [ ] Read generated `paragraph-ids-rich.json`.
- [ ] Assert targeted fields only; do not use full JSON snapshot equality.
- [ ] Target fields include:
  - [ ] `role_inventory` counts (`dt`, `t`, `ds`, `s`, `std`),
  - [ ] `literal_inventory` counts/hashes,
  - [ ] `list_structure` (`depth`, `item_count`, `ordered`),
  - [ ] definition/ref mapping and paragraph association,
  - [ ] expected presence/change of `markup_checksum`.

### E2E mode
- [ ] Run `tools/changelog_assistant.py` against controlled smoke edits.
- [ ] Validate emitted tags from report JSON even if changelog coverage check returns non-zero.
- [ ] Capture command output and parsed findings under `--report-dir`.

### Outputs
- [ ] Write `results.json` (machine-readable).
- [ ] Write `summary.md` (human-readable pass/fail matrix).
- [ ] Write `logs/` with command transcripts and stderr/stdout captures.
- [ ] Exit non-zero if any selected case fails.

## Case manifest contract (`tools/changelog_tag_cases.json`)
- [ ] Each case defines: `id`, `category`, `mode`, `require_tags`, `forbid_tags`, fixture paths.
- [ ] Include provenance metadata for non-synthetic cases: `base_ref`, `head_ref`, optional `upstream_pr`.
- [ ] Add optional `notes` field for reviewer context.

## Best-practice case checklist (required + forbidden tags)

### `fls_3qj3jvmtxvx6` safe `#[target_feature]` calls
- [ ] Comparator fixture pair created.
- [ ] Require `paragraph-changed`.
- [ ] Forbid `paragraph-added`, `paragraph-removed`.

### `fls_SYnFJBhi0IWj` trait object upcasting rule
- [ ] Comparator fixture pair created.
- [ ] Require `paragraph-changed`.
- [ ] Forbid `paragraph-added`, `paragraph-removed`.

### `fls_8i4jzksxlrw0` raw pointer deref exception
- [ ] Comparator fixture pair created.
- [ ] Require `paragraph-changed`, `normative-shift`.
- [ ] Forbid `paragraph-added`, `paragraph-removed`.

### `fls_imr2jx6cbuzq` inferred array size constants
- [ ] Comparator fixture pair created.
- [ ] Require `paragraph-changed`.
- [ ] Forbid `paragraph-added`, `paragraph-removed`.

### `fls_hbn1l42xmr3h` variadic ABI expansion
- [ ] Comparator fixture pair created.
- [ ] Require `paragraph-changed`, `list-structure-change`, `paragraph-added`.
- [ ] Forbid `paragraph-removed`.

### `fls_IKSPR7ZQMErU` duplicate word removal
- [ ] Comparator fixture pair created.
- [ ] Require `paragraph-changed`.
- [ ] Forbid `paragraph-added`, `paragraph-removed`, `normative-shift`.

### `fls_icdzs1mjh0n4` wording tightened to "shall"
- [ ] Comparator fixture pair created.
- [ ] Require `paragraph-changed`, `normative-shift`.
- [ ] Forbid `paragraph-added`, `paragraph-removed`.

### `fls_VhzGfnWg7YrG` missing case added
- [ ] Comparator fixture pair created.
- [ ] Require `paragraph-changed`.
- [ ] Forbid `paragraph-removed`.

### `fls_zyuxqty09SDO` wording refinement
- [ ] Comparator fixture pair created.
- [ ] Require `paragraph-changed`.
- [ ] Forbid `paragraph-added`, `paragraph-removed`, `normative-shift`.

### `fls_8m7pc3riokst` unused term removed
- [ ] Comparator fixture pair created.
- [ ] Require `paragraph-changed`, `role-change`, `term-def-removed`.
- [ ] Forbid `paragraph-added`, `paragraph-removed`.

## Supplemental synthetic coverage checklist
- [ ] `section-added` case.
- [ ] `section-removed` case.
- [ ] `definition-relocated` case.
- [ ] `term-ref-added` case.
- [ ] `term-ref-removed` case.
- [ ] `syntax-ref-added` case.
- [ ] `syntax-ref-removed` case.
- [ ] `syntax-def-added` case.
- [ ] `syntax-def-removed` case.
- [ ] `literal-change` case.
- [ ] No-change control case with expected empty tag list.

## Extraction-specific case checklist
- [ ] Add at least one extraction fixture that exercises role inventory deltas.
- [ ] Add at least one extraction fixture that exercises list structure detection.
- [ ] Add at least one extraction fixture that exercises literal inventory changes.
- [ ] Add at least one extraction fixture that exercises definition/ref paragraph mapping.

## CI integration checklist

### Pull request (gating)
- [ ] Add a CI step/job that runs comparator + extraction verification.
- [ ] Command includes deterministic report path under build:
  - [ ] `uv run python tools/changelog_tag_verifier.py --mode compare --report-dir build/changelog-tag-verification/pr`.
  - [ ] `uv run python tools/changelog_tag_verifier.py --mode extract --report-dir build/changelog-tag-verification/pr`.
- [ ] Upload `build/changelog-tag-verification/pr` as artifact on CI runs.

### Nightly / manual dispatch (non-gating)
- [ ] Add scheduled nightly workflow (`on.schedule`) and `workflow_dispatch`.
- [ ] Run E2E smoke only:
  - [ ] `uv run python tools/changelog_tag_verifier.py --mode e2e --report-dir build/changelog-tag-verification/nightly`.
- [ ] Mark this workflow non-gating for PR merges.
- [ ] Upload `build/changelog-tag-verification/nightly` as artifact.

## Recommended commit checkpoints (encouraged)
- [ ] Commit 1: verifier scaffold + manifest + schema.
- [ ] Commit 2: comparator fixtures + best-practice/synthetic case definitions.
- [ ] Commit 3: extraction fixtures + targeted assertion engine.
- [ ] Commit 4: CI integration (PR gating + nightly smoke) + docs/help updates.

## New-session execution runbook
- [ ] `uv run python tools/changelog_tag_verifier.py --mode compare --report-dir build/changelog-tag-verification/local`.
- [ ] `uv run python tools/changelog_tag_verifier.py --mode extract --report-dir build/changelog-tag-verification/local`.
- [ ] `uv run python tools/changelog_tag_verifier.py --mode e2e --report-dir build/changelog-tag-verification/local`.
- [ ] `uv run python tools/changelog_tag_verifier.py --mode all --report-dir build/changelog-tag-verification/local`.

## Final acceptance criteria
- [ ] Every best-practice case passes required/forbidden checks.
- [ ] Every supplemental synthetic case passes.
- [ ] No-change control case reports no tags.
- [ ] PR-gating CI checks pass on branch.
- [ ] Nightly/manual e2e workflow runs and publishes artifacts.
- [ ] `build/changelog-tag-verification/summary.md` and `build/changelog-tag-verification/results.json` are produced for local runs.
