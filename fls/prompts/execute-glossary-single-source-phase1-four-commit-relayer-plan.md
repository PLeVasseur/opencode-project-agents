Execute the canonical plan at:
`$OPENCODE_CONFIG_DIR/plans/glossary-single-source-phase1-upstream-main-four-commit-relayer-plan-20260214.md`

Context:
- Repo: `/home/pete.levasseur/project/fls`
- Canonical base: `upstream/main` (pin to immutable SHA before rewrite)
- First mutating step: sync `origin/main` from pinned `upstream/main` (fast-forward only)
- Required commit stack: `tooling-core`, `migration`, `ci-verification`, `capstone-generated-only`
- Final deliverables must be written under `$OPENCODE_CONFIG_DIR/reports/`
- Stop point is mandatory: push repack branch + validate compare view, then stop for manual review
- Do not replace `glossary-single-source-phase1` unless explicitly requested afterward

Kickoff/Resume contract (must work for fresh or crashed session):
1. Use these fixed run files:
   - `STATE_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214.state.env`
   - `STATE_LOCK_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214.state.lock`
   - `REPORT_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214.md`
2. If `STATE_FILE` is absent, initialize a new run from Phase 1 of the canonical plan.
3. If `STATE_FILE` exists, resume from the first incomplete phase:
   - Validate state invariants before skipping completed phases.
   - Handle stale lock safely (single-writer guarantee).
   - If git operation is interrupted (rebase/cherry-pick/merge), stabilize repo before continuing.
4. Persist state after each successful phase (`PHASE_*` flags + SHAs + artifact paths).
5. If any invariant fails, stop and recover via the backup refs defined in the plan.

Execution requirements:
1. Run fresh-session bootstrap checks exactly as defined in the plan.
2. Implement verifier-mode/tooling updates required by the capstone commit.
3. Implement generated-only glossary flow in capstone (remove duplicate source-of-truth file).
4. Enforce CI/build immediate-reflection guarantees for glossary directive changes.
5. Generate all integrity-chain deliverables:
   - HTML artifacts from `UPSTREAM_MAIN_PIN`, `COMMIT3_SHA`, `COMMIT4_SHA`
   - Manifests for each artifact folder
   - Three pairwise policy-diff reports
   - Top-level integrity summary report with explicit no-difference statement under configured policy
6. Push repack branch and validate reviewability (exactly 4 commits, expected scopes).
7. Stop immediately at the manual-review checkpoint.

Finish by returning:
- Phase-by-phase checklist status (including resume decisions).
- Commit/branch SHA map (`UPSTREAM_MAIN_PIN`, `ORIG_HEAD`, `REBASED_HEAD`, `COMMIT1..4`, `REPACK_REMOTE_SHA`).
- Command summary with exit codes.
- Exact artifact/report paths under `$OPENCODE_CONFIG_DIR/reports/`.
- Integrity verdict for each pairwise comparison and reproducibility run.
- Confirmation that execution stopped before original branch replacement.
