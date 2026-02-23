# PR #656 follow-up: phased glossary migration with stacked worktrees (no glossary directives)

## Objective

- [ ] Deliver Tshepang's sequence as a reviewable stack of branches and fork PRs.
- [ ] Reuse PR #656 only as a mechanical donor/reference, not as a landed architecture.
- [ ] Enforce the hard constraint: do not introduce or keep `.. glossary-entry::` / `.. glossary-include::` in this stack.
- [ ] Add Sphinx/lint guardrails at each phase so regressions are blocked immediately.

## Hard constraints

- [ ] Do not land glossary-specific directives (`glossary-entry`, `glossary-include`) in any new branch.
- [ ] Work only against `PLeVasseur/fls` for this stack (no upstream pushes/PRs).
- [ ] Keep branches stacked so each PR diff is phase-local and reviewable.
- [ ] Keep source edits in `src/` + `exts/` + tooling/CI as needed; do not edit `build/`.

## Build command policy

- [ ] Use project entrypoints for local/CI-equivalent checks.
  - [ ] Always use `./make.py` for build and link checks.
  - [ ] Use `./generate-glossary.py` for glossary parity once it exists in the active phase branch (phase 5+ for this stack rooted at `origin/main`).
- [ ] Do not invoke `sphinx-build` or `sphinx-autobuild` directly in manual phase steps.
- [ ] Keep command parity with repo docs and CI:
  - [ ] Build and warnings/check-links via `./make.py`.
  - [ ] Glossary artifact parity via `./generate-glossary.py` and `diff` (as in CI) once generator wiring exists in the phase branch.

## Reporting convention

- [ ] Create and export one timestamped report root once per execution:
  - [ ] `export REPORT_ROOT="$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-$(date -u +%Y%m%dT%H%M%SZ)"`
  - [ ] `mkdir -p "$REPORT_ROOT"`
- [ ] Maintain a reusable per-phase scaffold root:
  - [ ] `export REPORT_SCAFFOLD_ROOT="$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-phase-scaffold"`
  - [ ] Keep scaffold templates versioned in that path (one phase directory per phase).
- [ ] At execution start, copy scaffold templates into the timestamped run root:
  - [ ] `cp -R "$REPORT_SCAFFOLD_ROOT"/. "$REPORT_ROOT"/`
- [ ] Store all logs, machine-readable reports, ancestry checks, and PR metadata under `$REPORT_ROOT/`.
- [ ] Keep all report artifacts under `$OPENCODE_CONFIG_DIR/reports/` (never in-repo).

## Inputs and baseline

- [ ] Treat `rust-lang/fls#656` as source material for mechanical term-placement decisions.
- [ ] Treat Tshepang's 5-step sequence as the canonical phase order:
  - [ ] Ensure main text has all glossary entries.
  - [ ] Ensure duplicate glossary/main definitions match.
  - [ ] Ensure `:dt:` only in main text, none in glossary.
  - [ ] Remove now-redundant glossary "See ..." paragraphs.
  - [ ] Generate glossary from main-text `:dt:` definitions, with parity checks.

## Term-wave grouping (history-derived)

- [ ] Use donor checkpoint history to ensure each phase accounts for all glossary terms.
- [ ] Archive grouping evidence for reproducibility:
  - [ ] `git log --reverse --oneline origin/main..origin/glossary-auto-generation > "$REPORT_ROOT/term-wave-history.log"`
- [ ] Use the following wave map derived from donor commit checkpoints:
  - [ ] Wave `A-H`: `c13b26a`, `aeafe57`, `9a2d8f2`, `6757129`, `cfbedf5`, `6cb641b`, `55fe499`
  - [ ] Wave `I-P`: `5d95464`, `5496961`, `9b60dce`, `0261484`, `2844596`
  - [ ] Wave `Q-T`: `e6873af`, `5afdc13`, `3d83981`, `fac9b30`
  - [ ] Wave `U-W`: `5914509`, `fb7d911`, `cbe68a8`
  - [ ] Wave `X-Z + aliases`: `f119687`, `d95aaa0`, `d77ab3c`
- [ ] If a term is not explicit in checkpoint titles, assign by nearest alphabetical wave and log rationale.

## Worktree and branch topology

- [ ] Create one read-only donor worktree from PR #656 branch:
  - [ ] `../fls-wt/ref-pr656` -> `origin/glossary-single-source-phase1`
- [ ] Create five execution worktrees/branches, stacked sequentially:
  - [ ] `../fls-wt/step1` -> `glossary-step-1-main-text-coverage` (base: `origin/main`)
  - [ ] `../fls-wt/step2` -> `glossary-step-2-align-duplicate-text` (base: step 1)
  - [ ] `../fls-wt/step3` -> `glossary-step-3-dt-main-only` (base: step 2)
  - [ ] `../fls-wt/step4` -> `glossary-step-4-remove-see-paragraphs` (base: step 3)
  - [ ] `../fls-wt/step5` -> `glossary-step-5-generated-glossary-parity` (base: step 4)

## Setup commands (one-time)

- [ ] Preflight checks (must pass before creating worktrees):
  - [ ] Confirm `OPENCODE_CONFIG_DIR` is set and writable (`test -n "$OPENCODE_CONFIG_DIR" && test -w "$OPENCODE_CONFIG_DIR"`).
  - [ ] Confirm `origin` points to `PLeVasseur/fls` (`git remote -v`).
  - [ ] Confirm authentication is ready; fail fast if not authenticated (`gh auth status >/dev/null 2>&1 || { echo "error: gh is not authenticated; run gh auth login"; exit 1; }`).
  - [ ] Confirm baseline toolchain is present (`uv --version`, `./make.py --help`).
  - [ ] Handle generator availability according to branch baseline:
    - [ ] If `./generate-glossary.py` exists in the current branch, run `./generate-glossary.py --help`.
    - [ ] If it does not exist (expected for `origin/main`-based worktrees in this plan), record a deferred check and require it before phase 5 strict/parity commands.
  - [ ] Confirm `origin/main` and `origin/glossary-single-source-phase1` exist after `git fetch origin --prune`.
  - [ ] Confirm `../fls-wt/` paths are either absent or intentionally reusable.
  - [ ] Confirm target branch names are either absent or intentionally reusable.
- [ ] Fetch and prepare working area.
- [ ] If rerunning setup, use an idempotent path:
  - [ ] Remove stale worktrees that are no longer needed (for example `git worktree remove "../fls-wt/step5"`).
  - [ ] If a branch already exists and should be reused, attach it with `git worktree add "../fls-wt/step3" glossary-step-3-dt-main-only` (without `-b`).

```bash
git fetch origin --prune
mkdir -p ../fls-wt
git worktree add "../fls-wt/ref-pr656" origin/glossary-single-source-phase1
git worktree add -b glossary-step-1-main-text-coverage "../fls-wt/step1" origin/main
git worktree add -b glossary-step-2-align-duplicate-text "../fls-wt/step2" glossary-step-1-main-text-coverage
git worktree add -b glossary-step-3-dt-main-only "../fls-wt/step3" glossary-step-2-align-duplicate-text
git worktree add -b glossary-step-4-remove-see-paragraphs "../fls-wt/step4" glossary-step-3-dt-main-only
git worktree add -b glossary-step-5-generated-glossary-parity "../fls-wt/step5" glossary-step-4-remove-see-paragraphs
```

- [ ] Post-creation verification:
  - [ ] `git -C "../fls-wt/step1" status --short --branch` reports `glossary-step-1-main-text-coverage`.
  - [ ] `git -C "../fls-wt/step2" status --short --branch` reports `glossary-step-2-align-duplicate-text`.
  - [ ] `git -C "../fls-wt/step3" status --short --branch` reports `glossary-step-3-dt-main-only`.
  - [ ] `git -C "../fls-wt/step4" status --short --branch` reports `glossary-step-4-remove-see-paragraphs`.
  - [ ] `git -C "../fls-wt/step5" status --short --branch` reports `glossary-step-5-generated-glossary-parity`.

## Guardrail strategy (progressive hardening)

- [ ] Add a dedicated migration lint module (for example `exts/ferrocene_spec_lints/glossary_migration.py`) and register it in `exts/ferrocene_spec_lints/__init__.py`.
- [ ] Start with warning-compatible checks while content is in motion, then flip each check to hard error at the end of its phase.
- [ ] Keep guardrails source-based/AST-based; avoid fragile regex-only checks except for hard ban of disallowed directives.
- [ ] Add explicit migration config values in `src/conf.py` (phase gates + report output location).
  - [ ] Keep report artifacts under `$OPENCODE_CONFIG_DIR/reports/`.
  - [ ] Ensure local and CI execution use the same defaults.
- [ ] Add one canonical migration check entrypoint (single command) for all phases.
  - [ ] Implement `tools/glossary-migration-check.py` with `--phase`, `--strict`, and `--report` options.
  - [ ] Standard strict commands for this plan:
    - [ ] `uv run ./tools/glossary-migration-check.py --phase 1 --strict --report "$REPORT_ROOT/glossary-phase1-check.json"`
    - [ ] `uv run ./tools/glossary-migration-check.py --phase 2 --strict --report "$REPORT_ROOT/glossary-phase2-check.json"`
    - [ ] `uv run ./tools/glossary-migration-check.py --phase 3 --strict --report "$REPORT_ROOT/glossary-phase3-check.json"`
    - [ ] `uv run ./tools/glossary-migration-check.py --phase 4 --strict --report "$REPORT_ROOT/glossary-phase4-check.json"`
    - [ ] `uv run ./tools/glossary-migration-check.py --phase 5 --strict --report "$REPORT_ROOT/glossary-phase5-check.json"`
  - [ ] Ensure command exits non-zero when `--strict` phase checks fail.
- [ ] Document severity transitions per phase.
  - [ ] During active edits: warning mode allowed for in-progress checks.
  - [ ] Before opening each phase PR: target phase checks must run in error mode.

Planned guardrails by phase:

- [ ] Phase 1: all glossary terms must have a chapter definition (non-glossary doc).
- [ ] Phase 1: hard ban on disallowed directives (`glossary-entry`/`glossary-include`).
- [ ] Phase 2: glossary definition text and chapter definition text for same term must normalize to the same content.
- [ ] Phase 3: no `:dt:` in `glossary` document.
- [ ] Phase 3: canonical term target must resolve to chapter definitions.
- [ ] Phase 4: reject glossary paragraphs that are purely redundant "See ..." navigation.
- [ ] Phase 5: generated glossary must match committed glossary artifact (deterministic order/anchors).

## Stacked branch synchronization

- [ ] Before starting each phase, ensure the phase branch contains the latest tip of its immediate predecessor.
- [ ] Fast-forward-only sync path (when the target phase branch has no unique commits yet):
  - [ ] Before phase 2: `git -C "../fls-wt/step2" merge --ff-only glossary-step-1-main-text-coverage`
  - [ ] Before phase 3: `git -C "../fls-wt/step3" merge --ff-only glossary-step-2-align-duplicate-text`
  - [ ] Before phase 4: `git -C "../fls-wt/step4" merge --ff-only glossary-step-3-dt-main-only`
  - [ ] Before phase 5: `git -C "../fls-wt/step5" merge --ff-only glossary-step-4-remove-see-paragraphs`
- [ ] If the target phase branch already has unique commits, follow restack policy:
  - [ ] Prefer merge-forward updates in the target branch (for example `git -C "../fls-wt/step3" merge glossary-step-2-align-duplicate-text`).
  - [ ] Use rebase only when it materially improves review clarity and document it in the PR thread.
- [ ] Verify ancestry after each sync:
  - [ ] `git merge-base --is-ancestor glossary-step-1-main-text-coverage glossary-step-2-align-duplicate-text`
  - [ ] `git merge-base --is-ancestor glossary-step-2-align-duplicate-text glossary-step-3-dt-main-only`
  - [ ] `git merge-base --is-ancestor glossary-step-3-dt-main-only glossary-step-4-remove-see-paragraphs`
  - [ ] `git merge-base --is-ancestor glossary-step-4-remove-see-paragraphs glossary-step-5-generated-glossary-parity`

## Phase-by-phase execution

### Term-wave execution matrix (all phases)

- [ ] Phase 1 wave tracker: `$REPORT_ROOT/phase1-main-text-coverage/term-wave-checklist.md`
  - [ ] Wave `A-H`
  - [ ] Wave `I-P`
  - [ ] Wave `Q-T`
  - [ ] Wave `U-W`
  - [ ] Wave `X-Z + aliases`
- [ ] Phase 2 wave tracker: `$REPORT_ROOT/phase2-align-duplicate-text/term-wave-checklist.md`
  - [ ] Wave `A-H`
  - [ ] Wave `I-P`
  - [ ] Wave `Q-T`
  - [ ] Wave `U-W`
  - [ ] Wave `X-Z + aliases`
- [ ] Phase 3 wave tracker: `$REPORT_ROOT/phase3-dt-main-only/term-wave-checklist.md`
  - [ ] Wave `A-H`
  - [ ] Wave `I-P`
  - [ ] Wave `Q-T`
  - [ ] Wave `U-W`
  - [ ] Wave `X-Z + aliases`
- [ ] Phase 4 wave tracker: `$REPORT_ROOT/phase4-remove-see-paragraphs/term-wave-checklist.md`
  - [ ] Wave `A-H`
  - [ ] Wave `I-P`
  - [ ] Wave `Q-T`
  - [ ] Wave `U-W`
  - [ ] Wave `X-Z + aliases`
- [ ] Phase 5 wave tracker: `$REPORT_ROOT/phase5-generated-glossary-parity/term-wave-checklist.md`
  - [ ] Wave `A-H`
  - [ ] Wave `I-P`
  - [ ] Wave `Q-T`
  - [ ] Wave `U-W`
  - [ ] Wave `X-Z + aliases`

### Phase 1 (branch: `glossary-step-1-main-text-coverage`)

Goal: ensure every glossary term exists as chapter-side definition.

- [ ] Build a term inventory from current glossary and chapter docs.
  - [ ] Extract glossary term definitions from `src/glossary.rst`.
  - [ ] Extract chapter term definitions from `src/*.rst` except `glossary.rst`, `index.rst`, and `changelog.rst`.
  - [ ] Normalize term identity with the same term-ID logic used by the extension (`definitions.id_from_text("term", text)`).
- [ ] Write inventory and missing-term reports to `$REPORT_ROOT/`.
  - [ ] Include term, chosen chapter, and source paragraph IDs used for placement.
- [ ] For each glossary term missing in chapters, add chapter `:dt:` text near first relevant semantic location.
- [ ] Use PR #656 donor worktree to accelerate placement and wording seeds; port only plain RST content (no glossary directives).
- [ ] Preserve glossary semantics in this phase; avoid structural glossary simplification here.
- [ ] Define tie-break policy for ambiguous placement.
  - [ ] Prefer chapter with the first normative use of the term.
  - [ ] If still ambiguous, select the chapter with the most direct subject ownership and log rationale in report.
- [ ] Add guardrail: fail when a glossary term has no non-glossary definition.
- [ ] Add guardrail: fail if disallowed glossary directives appear.

Definition of done:

- [ ] Phase 1 term-wave checklist marks all wave buckets complete with evidence links.
- [ ] Coverage check reports 0 glossary-only terms.
- [ ] Phase 1 strict command exits 0 (coverage + disallowed directive checks): `uv run ./tools/glossary-migration-check.py --phase 1 --strict --report "$REPORT_ROOT/glossary-phase1-check.json"`.
- [ ] `./make.py --clear` succeeds.
- [ ] `./make.py --check-links` succeeds.

### Phase 2 (branch: `glossary-step-2-align-duplicate-text`)

Goal: unify duplicate glossary/chapter definition text.

- [ ] Compare glossary definition paragraphs against chapter definition paragraphs term-by-term.
- [ ] Define and implement comparison normalization rules.
  - [ ] Ignore whitespace and line-wrap differences.
  - [ ] Preserve role kinds and explicit link targets (no role-kind downgrades hidden by normalization).
  - [ ] Treat wording/punctuation changes as real differences unless explicitly waived.
- [ ] Resolve mismatches to most accurate wording, preserving technical intent and references.
- [ ] Classify mismatches in reports (`wording`, `scope`, `role-only`, `structural`) under `$REPORT_ROOT/`.
- [ ] For semantic changes, capture rationale in a phase report entry.
- [ ] Keep edits narrowly scoped to definition harmonization (not role migration yet).
- [ ] Add guardrail: mismatch detector between glossary and chapter definitions (normalized whitespace/line-wrap insensitive).

Definition of done:

- [ ] Phase 2 term-wave checklist marks all wave buckets complete with evidence links.
- [ ] Mismatch report is empty.
- [ ] Phase 2 strict command exits 0 (mismatch detector in error mode): `uv run ./tools/glossary-migration-check.py --phase 2 --strict --report "$REPORT_ROOT/glossary-phase2-check.json"`.
- [ ] Build + links pass.

### Phase 3 (branch: `glossary-step-3-dt-main-only`)

Goal: move canonical term definitions out of glossary.

- [ ] Replace glossary-side `:dt:` usage with referential roles (`:t:`) where appropriate.
- [ ] Keep chapter-side `:dt:` as canonical definitions.
- [ ] Verify glossary term links resolve into main text definitions.
- [ ] Define and enforce zero-definition-in-glossary checks.
  - [ ] AST check: no term `DefIdNode` definitions in `glossary` doctree.
  - [ ] Source check: no `:dt:` term definitions in glossary source.
- [ ] Add guardrail: `glossary` document contains zero `:dt:` roles.
- [ ] Add guardrail: term canonical object origin is non-glossary document.

- [ ] Add explicit term-target validation report.
  - [ ] For each glossary term, record canonical target document and anchor.
  - [ ] Fail if canonical target document is `glossary`.

Definition of done:

- [ ] Phase 3 term-wave checklist marks all wave buckets complete with evidence links.
- [ ] Lint confirms no glossary `:dt:`.
- [ ] Canonical-target report confirms 0 glossary-owned term targets.
- [ ] Sample and automated link checks confirm term jumps land in chapters.
- [ ] Phase 3 strict command exits 0: `uv run ./tools/glossary-migration-check.py --phase 3 --strict --report "$REPORT_ROOT/glossary-phase3-check.json"`.

### Phase 4 (branch: `glossary-step-4-remove-see-paragraphs`)

Goal: remove redundant glossary-only navigational paragraphs.

- [ ] Identify "See ..." paragraphs now rendered redundant by phase 3 behavior.
- [ ] Define redundant "See ..." pattern precisely.
  - [ ] Paragraph text starts with `See` or `For ... see ...`.
  - [ ] Paragraph carries only navigational references and no unique semantic constraints.
  - [ ] Paragraphs with unique semantic content are not dropped; content is migrated to chapter definitions first.
- [ ] Remove redundant entries while preserving non-redundant semantic content.
- [ ] If a removed line had unique semantics, move that content to chapter definition text.
- [ ] Add guardrail: reject pure redundant "See ..." patterns in glossary.
- [ ] Write removed/retained ledger report under `$REPORT_ROOT/`.

Definition of done:

- [ ] Phase 4 term-wave checklist marks all wave buckets complete with evidence links.
- [ ] No redundant "See ..." entries remain.
- [ ] Phase 4 strict command exits 0 (redundant-see detector in error mode): `uv run ./tools/glossary-migration-check.py --phase 4 --strict --report "$REPORT_ROOT/glossary-phase4-check.json"`.
- [ ] Build + links pass.

### Phase 5 (branch: `glossary-step-5-generated-glossary-parity`)

Goal: generate glossary from chapter definitions and enforce parity.

- [ ] Freeze committed artifact strategy before coding.
  - [ ] Decide and document which in-repo file is the canonical committed glossary artifact.
  - [ ] Document how contributors regenerate/update that artifact.
- [ ] Freeze parity policy before coding.
  - [ ] Prefer byte-for-byte parity.
  - [ ] If normalized parity is required, document exact normalization and why byte parity is insufficient.
- [ ] Implement generation path from chapter `:dt:` definitions to `build/generated.glossary.rst`.
- [ ] Keep committed glossary artifact (stable in-repo record) and compare generated vs committed in CI.
- [ ] Ensure deterministic output ordering and stable anchors/paragraph IDs.
- [ ] Add CI step and local command wiring (`make.py` and/or dedicated tooling).
- [ ] Confirm generator entrypoint availability in phase branch before running strict/parity checks (`./generate-glossary.py --help`).

- [ ] Determinism contract checks:
  - [ ] Stable sort key rules are explicit and tested.
  - [ ] Paragraph/section IDs are stable across repeated runs.
  - [ ] Generator output is free of timestamps or machine-specific data.

Definition of done:

- [ ] Phase 5 term-wave checklist marks all wave buckets complete with evidence links.
- [ ] Generator output is deterministic and reproducible.
- [ ] CI parity check is green.
- [ ] Phase 5 strict command exits 0 (generator parity in error mode): `uv run ./tools/glossary-migration-check.py --phase 5 --strict --report "$REPORT_ROOT/glossary-phase5-check.json"`.
- [ ] CI-equivalent glossary parity command exits 0: `./generate-glossary.py && diff -u build/generated.glossary.rst src/glossary.rst.inc`.
- [ ] Build + links pass.

## PR stack and review flow (fork only)

- [ ] Push each branch to `origin` (fork) with `-u` tracking.
- [ ] Use explicit push commands:

```bash
git -C "../fls-wt/step1" push -u origin glossary-step-1-main-text-coverage
git -C "../fls-wt/step2" push -u origin glossary-step-2-align-duplicate-text
git -C "../fls-wt/step3" push -u origin glossary-step-3-dt-main-only
git -C "../fls-wt/step4" push -u origin glossary-step-4-remove-see-paragraphs
git -C "../fls-wt/step5" push -u origin glossary-step-5-generated-glossary-parity
```

- [ ] Create stacked PRs on `PLeVasseur/fls`:
  - [ ] PR1: `glossary-step-1-main-text-coverage` -> `main`
  - [ ] PR2: `glossary-step-2-align-duplicate-text` -> `glossary-step-1-main-text-coverage`
  - [ ] PR3: `glossary-step-3-dt-main-only` -> `glossary-step-2-align-duplicate-text`
  - [ ] PR4: `glossary-step-4-remove-see-paragraphs` -> `glossary-step-3-dt-main-only`
  - [ ] PR5: `glossary-step-5-generated-glossary-parity` -> `glossary-step-4-remove-see-paragraphs`
- [ ] Use explicit PR creation commands (base/head fully specified to fork branches):

```bash
gh pr create --repo PLeVasseur/fls --base main --head PLeVasseur:glossary-step-1-main-text-coverage --title "docs(glossary): phase 1 main text coverage" --body "$(cat <<'EOF'
## Summary
- Ensure all glossary terms are defined in main text.
- Add phase-1 guardrails for missing chapter definitions and banned glossary directives.

## Reference alignment
- Follow-up to rust-lang/fls#656 and Tshepang phased strategy (step 1/5).
- No glossary-entry/glossary-include directives are introduced.

## Testing
- ./make.py --clear
- ./make.py --check-links
- uv run ./tools/glossary-migration-check.py --phase 1 --strict --report "$REPORT_ROOT/glossary-phase1-check.json"
EOF
)"

gh pr create --repo PLeVasseur/fls --base glossary-step-1-main-text-coverage --head PLeVasseur:glossary-step-2-align-duplicate-text --title "docs(glossary): phase 2 align duplicate text" --body "$(cat <<'EOF'
## Summary
- Align glossary and chapter duplicate definitions to identical text.
- Add phase-2 mismatch guardrails.

## Reference alignment
- Follow-up to rust-lang/fls#656 and Tshepang phased strategy (step 2/5).
- No glossary-entry/glossary-include directives are introduced.

## Testing
- ./make.py --clear
- ./make.py --check-links
- uv run ./tools/glossary-migration-check.py --phase 2 --strict --report "$REPORT_ROOT/glossary-phase2-check.json"
EOF
)"

gh pr create --repo PLeVasseur/fls --base glossary-step-2-align-duplicate-text --head PLeVasseur:glossary-step-3-dt-main-only --title "docs(glossary): phase 3 keep dt in main text only" --body "$(cat <<'EOF'
## Summary
- Remove glossary-side term definitions and keep canonical :dt: definitions in chapters.
- Add phase-3 guardrails for canonical target ownership.

## Reference alignment
- Follow-up to rust-lang/fls#656 and Tshepang phased strategy (step 3/5).
- No glossary-entry/glossary-include directives are introduced.

## Testing
- ./make.py --clear
- ./make.py --check-links
- uv run ./tools/glossary-migration-check.py --phase 3 --strict --report "$REPORT_ROOT/glossary-phase3-check.json"
EOF
)"

gh pr create --repo PLeVasseur/fls --base glossary-step-3-dt-main-only --head PLeVasseur:glossary-step-4-remove-see-paragraphs --title "docs(glossary): phase 4 remove redundant see paragraphs" --body "$(cat <<'EOF'
## Summary
- Remove redundant glossary navigation-only "See ..." paragraphs.
- Preserve and relocate any remaining semantic content into chapters.

## Reference alignment
- Follow-up to rust-lang/fls#656 and Tshepang phased strategy (step 4/5).
- No glossary-entry/glossary-include directives are introduced.

## Testing
- ./make.py --clear
- ./make.py --check-links
- uv run ./tools/glossary-migration-check.py --phase 4 --strict --report "$REPORT_ROOT/glossary-phase4-check.json"
EOF
)"

gh pr create --repo PLeVasseur/fls --base glossary-step-4-remove-see-paragraphs --head PLeVasseur:glossary-step-5-generated-glossary-parity --title "docs(glossary): phase 5 generated glossary parity" --body "$(cat <<'EOF'
## Summary
- Generate glossary content from chapter definitions and enforce parity checks.
- Add deterministic generation and CI-equivalent parity guardrails.

## Reference alignment
- Follow-up to rust-lang/fls#656 and Tshepang phased strategy (step 5/5).
- No glossary-entry/glossary-include directives are introduced.

## Testing
- ./make.py --clear
- ./make.py --check-links
- uv run ./tools/glossary-migration-check.py --phase 5 --strict --report "$REPORT_ROOT/glossary-phase5-check.json"
- ./generate-glossary.py && diff -u build/generated.glossary.rst src/glossary.rst.inc
EOF
)"
```
- [ ] Use PR body sections on each PR:
  - [ ] `## Summary`
  - [ ] `## Reference alignment`
  - [ ] `## Testing`
- [ ] Restack policy when lower PRs change:
  - [ ] Prefer forward-only updates first (for example `git -C "../fls-wt/step3" merge glossary-step-2-align-duplicate-text`).
  - [ ] If rebase is required for clarity, limit history rewrite to fork feature branches only and document it in PR comments.
  - [ ] Never push directly to upstream and never force-push `main`.

## Per-phase test checklist

- [ ] `./make.py --clear`
- [ ] `./make.py --check-links`
- [ ] Phase-specific migration lints/check scripts
  - [ ] Run strict mode for the target phase before opening/updating that phase PR.
  - [ ] Archive machine-readable reports to `$REPORT_ROOT/`.
- [ ] Update phase scaffold files for the active phase under `$REPORT_ROOT/phaseN-*/`.
  - [ ] Mark all term waves completed in `term-wave-checklist.md`.
  - [ ] Record command logs and exit codes in `artifacts-checklist.md`.
- [ ] (Phase 5+) generator entrypoint readiness check: `./generate-glossary.py --help`
- [ ] (Phase 5+) generator parity check (generated == committed glossary): `./generate-glossary.py && diff -u build/generated.glossary.rst src/glossary.rst.inc`

## Risks and mitigations

- [ ] Risk: large content churn obscures correctness.
  - [ ] Mitigation: keep changes phase-local and stacked; avoid mixed-purpose commits.
- [ ] Risk: accidental reintroduction of banned directives.
  - [ ] Mitigation: explicit lint failure on directive tokens.
- [ ] Risk: non-deterministic generation/paragraph ID drift.
  - [ ] Mitigation: deterministic sort keys + stable ID policy + CI parity gate.

## Exit criteria for this plan

- [ ] All five stacked fork PRs exist.
- [ ] Each PR demonstrates its phase guardrail enforcement.
- [ ] Final phase proves generated glossary parity without glossary directives.
- [ ] All five phase term-wave checklists are complete (25/25 wave boxes checked).
