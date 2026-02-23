Execute the plan at:

`plans/issue-74-followup-validation-matrix-plan.md`

Execution requirements:

1. Follow phases and gates in strict order; do not skip gate criteria.
2. Update the plan file continuously as work progresses.
3. Change each checkbox from `[ ]` to `[x]` immediately after completion.
4. Stay on branch `bugfix/issue-74-left-topic-authority`; do not create a new branch.
5. Use upstream PR `https://github.com/eclipse-uprotocol/up-streamer-rust/pull/77` as canonical.
6. Before runtime changes, record DG-1 decision in report artifacts. Default is Path A unless explicitly overridden by user.
7. Keep all report artifacts under `$OPENCODE_CONFIG_DIR/reports/issue-74-followups/` and do not commit those artifacts.

Test implementation requirements:

1. Load `rust-test-quality-gate` before non-trivial test authoring/refactors.
2. Reuse and extend existing `RecordingTransport` in `up-streamer/src/ustreamer.rs` for D/E assertions:
   - per-key register/unregister counters keyed by `(source_filter, sink_filter)`
   - forced register-fail injection by key + `UStatus` (including `ALREADY_EXISTS`)
3. Keep tests reviewer-friendly:
   - one primary behavior per test
   - behavior-first names with no issue IDs
   - compact bodies (roughly 15-35 lines before helper extraction)
   - explicit assertions with concrete expected values/call counts
4. Under Path A, update `subscription-cache` identity semantics and add tests for:
   - same-subscriber/different-topic rows coexisting
   - reconstruction/update semantics via rebuilt cache payloads (including row removal reflection)

Runtime safety requirements:

1. Implement right-side wildcard subscriber-authority expansion only (`//*/...` on right side).
2. Implement dedupe of effective publish listener keys in both insert/remove paths.
3. Implement add-failure rollback consistency in `add_forwarding_rule`:
   - remove just-added forwarding rule bookkeeping on insert failure
   - rollback transport forwarder refcount/acquisition on insert failure
4. Preserve transactional rollback behavior for true non-duplicate failures.

Validation requirements:

1. Add fail-before/pass-after deterministic tests for A/B/C/D/E assertions in plan.
2. Run targeted tests first, then broader crate/workspace checks per plan.
3. Run CI parity matrix. Load `ci-parity-preflight` before matrix execution if needed.
4. If unbundled prerequisites are unavailable (for example no usable `VSOMEIP_INSTALL_PATH`), mark unbundled matrix as skipped with explicit reason in `ci-parity-results.md` and continue bundled/base/workspace matrices.

Commit and scope control:

1. Follow commit slicing defined in the plan.
2. Before each commit, run:
   - `git diff --name-only --cached`
   - `git diff --stat --cached`
3. Keep changes scoped to the plan; avoid unrelated refactors.

Final deliverables:

1. Final commit list (hash + subject + scope).
2. Updated PR URL and concise PR notes reflecting A/B/C/D/E outcomes.
3. DG-1 decision and rationale.
4. Test evidence and CI/parity outcomes.
5. Explicit list of any skipped/deferred items with rationale.
