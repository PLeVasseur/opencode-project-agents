`$OPENCODE_CONFIG_DIR/plans/transport-smoke-suite-file-based-scenario-claims-plan.md`

Mission:

Resume and complete the remaining work for file-based scenario claims in `transport-smoke-suite` while preserving all locked deterministic behavior and claim semantics.

Current implementation state (already done in working tree):

1. File-backed claim schema/loader/path resolution exists in `utils/transport-smoke-suite/src/claims.rs`.
2. Scenario runtime is refactored to load claims during preflight and evaluate loaded claims in validation.
3. All 8 scenario binaries no longer use inline `const CLAIMS`; they call `run_scenario(SCENARIO_ID, cli.common)`.
4. Matrix runner has `--claims-path`, forwards it to child scenarios, and blocks file override for multi-scenario runs.

Known immediate gap to fix first:

- `cargo check -p transport-smoke-suite` currently fails with:
  - `E0560: struct ScenarioReport has no field named claims_source_path`
  - `utils/transport-smoke-suite/src/scenario.rs` sets `claims_source_path` but `utils/transport-smoke-suite/src/report.rs` does not define it yet.

Execution constraints:

1. Continue from earliest unchecked item in the plan; keep checkboxes accurate.
2. Do not revert unrelated local changes.
3. Keep strict file-only claim sourcing:
   - missing/malformed/mismatched claims file = hard failure
   - no fallback to inline claim constants.
4. Preserve existing deterministic orchestration and claim semantics:
   - non-overlapping regex count behavior
   - independent claim evaluation
   - threshold defaults and CLI overrides remain authoritative.
5. Keep matrix behavior unchanged (sequential, continue-on-failure, non-zero if any fail).

Remaining required work:

1. Finish Phase B unresolved item:
   - Include resolved claims source path in diagnostics/repro/report metadata with deliberate report schema handling.
2. Phase E:
   - Add `utils/transport-smoke-suite/claims/<scenario-id>.json` for all 8 scenarios.
   - Mirror existing claim IDs/categories/patterns exactly, including SOME/IP-only forbidden routing claim.
3. Phase F:
   - Update `utils/transport-smoke-suite/tests/scenario_contracts.rs` to validate claims files + category coverage.
   - Update `utils/transport-smoke-suite/tests/fixture_audit.rs` to load file-based claims (no ad hoc templates).
   - Add remaining loader unit tests: missing file, malformed JSON, invalid threshold descriptor, and success paths (default/dir/file override).
4. Phase G:
   - Update `README.md` deterministic smoke section with:
     - default claims directory
     - `--claims-path` behavior for scenario + matrix
     - matrix file override restriction
     - one single-scenario custom claims file example
     - one matrix custom claims directory example.

Validation gates (must run and report):

1. `cargo fmt -- --check`
2. `cargo clippy -p transport-smoke-suite --all-targets -- -W warnings -D warnings`
3. `cargo test -p transport-smoke-suite`
4. Runtime checks:
   - one scenario default claims path
   - one scenario explicit claims file override
   - matrix default claims path
   - matrix explicit claims directory override
   - matrix fast-fail on multi-scenario with file override.

Commit strategy:

1. Commit 1: finalize runtime/report integration + remaining loader/test plumbing.
2. Commit 2: add 8 claims JSON files + test updates + README updates.

Completion output:

Provide a concise closeout with:
- final checkbox status by phase
- key file changes
- validation command results
- any remaining follow-ups (if any).
