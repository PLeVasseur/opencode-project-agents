# Plan: Stack Dedup + Anchor Logic and Revalidate on `system-abi-variadic`

## Goal
- [ ] Build a clean stacked branch that contains:
  - [ ] the paragraph-ID dedup commit (`0165ee6ad6e7e6a54705458d491810b0481b7df4`), and
  - [ ] the changelog anchor replacement logic commit for `tools/changelog_assistant.py`.
- [ ] Re-run anchor replacement validation and confirm canonical upstream URL behavior is stable (`replace`, not duplicate).
- [ ] Produce a complete artifact set under `$OPENCODE_CONFIG_DIR/reports/` for review.

## Canonical URL under test
- [ ] `CANONICAL_UPSTREAM_PR="https://github.com/rust-lang/rust/pull/145954"`

## Constraints
- [ ] Do not push unless explicitly requested.
- [ ] Do not force-reset or discard unrelated user changes.
- [ ] Keep this as a stacked-commit workflow (dedup base + anchor logic on top).

## Required outputs
- [ ] Timestamped `REPORT_ROOT` under `$OPENCODE_CONFIG_DIR/reports/`.
- [ ] Command + exit-code table (`command-exit-codes.tsv`).
- [ ] Stacked commit manifest (base SHA, anchor SHA, final HEAD).
- [ ] Full validation artifacts (pre-check/update/update-second/post-check, diffs, anchor evidence).
- [ ] Final summary (`$REPORT_ROOT/summary.md`) with pass/fail acceptance criteria.

## Session bootstrap checklist
- [ ] `printenv OPENCODE_CONFIG_DIR`
- [ ] `git fetch origin` in `/home/pete.levasseur/project/fls`
- [ ] Record UTC timestamp and create `REPORT_ROOT`
- [ ] Initialize `$REPORT_ROOT/command-exit-codes.tsv`

## 1) Create clean stacked validation worktree
- [ ] Verify `/home/pete.levasseur/project` exists.
- [ ] Create fresh worktree from `origin/system-abi-variadic`:
- [ ] `git worktree add -b system-abi-variadic-anchor-stack /home/pete.levasseur/project/fls-system-abi-variadic-anchor-stack origin/system-abi-variadic`
- [ ] `uv sync` inside new worktree.
- [ ] Record path/branch/HEAD metadata.

## 2) Resolve anchor logic commit SHA
- [ ] In source repo `/home/pete.levasseur/project/fls`, identify a commit containing anchor features in `tools/changelog_assistant.py`:
- [ ] must include `--require-anchor`
- [ ] must include report metadata fields (`update_action`, `anchored_pr_url`, `anchored_entry_line`, `anchored_entry_index`)
- [ ] If no committed SHA exists, create one (stage/commit only `tools/changelog_assistant.py`) and record SHA.
- [ ] Save chosen SHA to `$REPORT_ROOT/anchor-commit.txt`.

## 3) Build stacked branch state
- [ ] In stacked worktree, cherry-pick dedup base commit:
- [ ] `git cherry-pick 0165ee6ad6e7e6a54705458d491810b0481b7df4`
- [ ] Cherry-pick resolved anchor logic commit:
- [ ] `git cherry-pick <ANCHOR_COMMIT_SHA>`
- [ ] Record `git log --oneline -n 5` to `$REPORT_ROOT/stack-log.txt`.
- [ ] Record final stack manifest (`base`, `anchor`, `head`) to `$REPORT_ROOT/stack-manifest.txt`.

## 4) Pre-validation readiness checks
- [ ] Verify duplicate-ID fix is present:
- [ ] `src/glossary.rst` no longer contains `fls_t4yeovFm83Wo` / `fls_I9JaKZelMiby`
- [ ] `src/types-and-traits.rst` still contains canonical IDs
- [ ] Run duplicate-ID scan across `src/*.rst` and confirm zero duplicates.
- [ ] Verify changelog assistant readiness on stacked branch:
- [ ] `tools/changelog_assistant.py` exists
- [ ] `--require-anchor` appears in `--help`
- [ ] anchor metadata fields appear in report schema/code
- [ ] Compute explicit `BASE_REF="$(git merge-base HEAD origin/main)"` and use it for all assistant invocations.

## 5) Execute anchor replacement validation run (stacked branch)

### 5a) Baseline anchor evidence
- [ ] Record canonical URL count + line(s) before update in `$REPORT_ROOT/anchor-before.txt` (target count: `1`).

### 5b) Pre-check
- [ ] Run:

```bash
uv run python tools/changelog_assistant.py \
  --check \
  --base "$BASE_REF" \
  --emit-report "$REPORT_ROOT/pre-check"
```

- [ ] Capture exit code and artifact existence (`pre-check.json`, `pre-check.md`).

### 5c) First anchored update
- [ ] Run:

```bash
uv run python tools/changelog_assistant.py \
  --update \
  --base "$BASE_REF" \
  --title "Anchor replace validation (system-abi-variadic)" \
  --upstream-pr "$CANONICAL_UPSTREAM_PR" \
  --emit-report "$REPORT_ROOT/update"
```

- [ ] Capture exit code.
- [ ] Verify in `update.json`:
- [ ] `update_action == "replace"`
- [ ] `anchored_pr_url == "$CANONICAL_UPSTREAM_PR"`
- [ ] `anchored_entry_line` + `anchored_entry_index` present

### 5d) Diff and quality checks
- [ ] Save first diff to `$REPORT_ROOT/changelog.diff`.
- [ ] Verify updated entry is in correct release section.
- [ ] Verify `Change tags:` line is present.
- [ ] Verify paragraph and section refs use `:p:` and `:ref:` consistently.

### 5e) Idempotence (second update)
- [ ] Re-run the exact same update command with same title and URL.
- [ ] Save second diff to `$REPORT_ROOT/changelog-second.diff`.
- [ ] Record anchor count + line(s) after first and second updates.
- [ ] Verify canonical URL top-level count remains `1` throughout.

### 5f) Post-check
- [ ] Run:

```bash
uv run python tools/changelog_assistant.py \
  --check \
  --base "$BASE_REF" \
  --emit-report "$REPORT_ROOT/post-check"
```

- [ ] Capture exit code and artifact existence (`post-check.json`, `post-check.md`).

## 6) Reporting checklist
- [ ] Build tags-to-generated-content mapping (`$REPORT_ROOT/tag-mapping.md`).
- [ ] Write final report (`$REPORT_ROOT/summary.md`) including:
- [ ] bootstrap + readiness pass/fail
- [ ] stack commit SHAs and order
- [ ] duplicate-ID before/after status
- [ ] pre-check vs post-check outcomes
- [ ] anchor verdict (`replace` expected)
- [ ] remediation actions if any failures remain

## Operator handoff checklist
- [ ] Return checklist completion status by section.
- [ ] Return command summary with exit codes.
- [ ] Return exact artifact paths under `$REPORT_ROOT`.
- [ ] Return exact worktree path, branch, and head SHA.
- [ ] Return stack manifest (dedup SHA + anchor SHA + head SHA).
- [ ] Return pre-check vs post-check comparison and anchor verdict.

## Acceptance criteria
- [ ] Stacked branch includes dedup commit and anchor commit in correct order.
- [ ] Duplicate `:dp:` IDs are zero in stacked branch.
- [ ] Anchor update behavior is `replace` (not append), with canonical count staying `1` across both updates.
- [ ] Post-check exits `0`.
- [ ] Report artifacts are sufficient for standalone review.
