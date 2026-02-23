# Phase 5 Lint Policy Handoff

## Result

- Gate 5 status: PASS
- No production `#[allow(clippy::mutable_key_type)]` remains in touched runtime paths.
- No raw `UUri` map/set keying remains in touched runtime paths.

## Command Evidence

1. Command: `git rev-parse --abbrev-ref HEAD`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `refactor/up-streamer-domain-architecture`
   - Conclusion: Correct branch before Phase 5.

2. Command: `git status --short --branch`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `## refactor/up-streamer-domain-architecture`
     - modified files include only planned migration surfaces.
   - Conclusion: Baseline captured before lint-policy verification.

3. Command: `rg -n "allow\(clippy::mutable_key_type\)" up-streamer/src utils/usubscription-static-file/src || true`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `(no matches)`
   - Conclusion: No `mutable_key_type` allowances remain in production source trees checked by this phase.

4. Command: `rg -n "HashMap<\s*UUri|HashSet<\s*UUri" up-streamer/src/routing up-streamer/src/data_plane/ingress_registry.rs utils/usubscription-static-file/src/lib.rs || true`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `(no matches)`
   - Conclusion: No raw `UUri` map/set keying remains in touched runtime code.

5. Command: `rg -n "allow\(clippy::mutable_key_type\)" up-streamer utils || true`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `utils/integration-test-utils/src/integration_test_utils.rs:67:    #[allow(clippy::mutable_key_type)]`
   - Conclusion: One remaining allowance exists in test-support utility only.

## Remaining Allowance Rationale

- `utils/integration-test-utils/src/integration_test_utils.rs:67`
  - Scope: test-support helper only (not runtime/production path).
  - Rationale: helper groups recorded messages by source `UUri` for order assertions across integration scenarios; changing this helper is outside this migration scope and does not affect runtime map/set key semantics in shipped code.

## Phase Conclusion

Production lint policy objective is achieved for touched runtime paths; remaining allowance is test-only and explicitly justified.
