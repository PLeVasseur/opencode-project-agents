# Phase 6 - Validation and regression protection

## Phase pre-check

1) Command: `git rev-parse --abbrev-ref HEAD`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `refactor/up-streamer-domain-architecture`
- Conclusion: phase started on required branch.

2) Command: `git status --short --branch`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `## refactor/up-streamer-domain-architecture`
  - `M up-streamer/src/ustreamer.rs`
  - `M configurable-streamer/src/main.rs`
  - `M up-linux-streamer-plugin/src/lib.rs`
- Conclusion: in-progress scope captured before full validation.

## 6.1 Required checks

3) Command: `cargo fmt -- --check`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `1` (fail)
- Key output:
  - `Diff in .../up-streamer/src/control_plane/route_lifecycle.rs`
  - `Diff in .../utils/usubscription-static-file/src/lib.rs`
- Conclusion: formatting gate initially failed.

4) Command: `cargo fmt`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - (no stdout/stderr)
- Conclusion: formatting remediation applied.

5) Command: `cargo fmt -- --check`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - (no stdout/stderr)
- Conclusion: formatting gate passed after remediation.

6) Command: `cargo clippy --all-targets -- -W warnings -D warnings`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `101` (fail)
- Key output:
  - `error: mutable key type`
  - `... because it contains UUri ... SpecialFields ... CachedSize ... AtomicUsize`
  - `error: could not compile up-streamer (lib) due to previous errors`
- Conclusion: direct `UUri` key migration triggered clippy `mutable_key_type` blocker.

7) Remediation applied:
- Added scoped `#[allow(clippy::mutable_key_type)]` only at affected route/subscription map scopes (no crate-wide allow).
- Re-ran formatting to keep tree rustfmt-clean.

8) Command: `cargo clippy --all-targets -- -W warnings -D warnings`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `Checking up-streamer v0.1.0 ...`
  - `Checking configurable-streamer v0.1.0 ...`
  - `Finished 'dev' profile ...`
- Conclusion: strict clippy gate passed with scoped lint exceptions.

9) Command: `cargo check --workspace --all-targets`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `Checking up-streamer v0.1.0 ...`
  - `Checking up-linux-streamer-plugin v0.1.0 ...`
  - `Finished 'dev' profile ...`
- Conclusion: full workspace target graph compiles.

10) Command: `cargo test --workspace`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `test result: ok. 20 passed; 0 failed` (`up_streamer` unit tests)
  - `test add_delete_route_contract_duplicate_and_missing_rules ... ok`
  - `test tests::fetch_subscribers_dedupes_duplicate_subscribers_after_topic_normalization ... ok`
  - `Doc-tests up_streamer ... 8 passed`
- Conclusion: workspace test and doctest suites are green.

## 6.2 Transport-facing build confidence

11) Command: `cargo build -p configurable-streamer`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `Compiling configurable-streamer v0.1.0 ...`
  - `Finished 'dev' profile ...`
- Conclusion: configurable-streamer builds successfully.

12) Command: `cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip"`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `Compiling up-linux-streamer v0.1.0 ...`
  - `Finished 'dev' profile ...`
- Conclusion: bundled Zenoh/SOMEIP streamer target builds successfully.

## 6.3 CI parity matrix

13) Command: `source build/envsetup.sh highest`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `Set GENERIC_CPP_STDLIB_PATH=/usr/include/c++/14`
  - `Set ARCH_SPECIFIC_CPP_STDLIB_PATH=/usr/include/x86_64-linux-gnu/c++/14`
- Conclusion: base environment bootstrap succeeded.

14) Command: `cargo build`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `Compiling up-linux-streamer-plugin ...`
  - `Compiling configurable-streamer ...`
  - `Finished 'dev' profile ...`
- Conclusion: CI base build command passes.

15) Command: `cargo clippy --all-targets -- -W warnings -D warnings`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `Checking configurable-streamer v0.1.0 ...`
  - `Checking up-streamer v0.1.0 ...`
  - `Finished 'dev' profile ...`
- Conclusion: CI base clippy command passes.

16) Command: `cargo fmt -- --check`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - (no stdout/stderr)
- Conclusion: CI base format check passes.

17) Command: `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `Compiling up-linux-streamer v0.1.0 ...`
  - `Compiling up-linux-streamer-plugin v0.1.0 ...`
  - `Finished 'dev' profile ...`
- Conclusion: bundled transport feature matrix build passes.

18) Command: `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `Checking example-streamer-uses v0.1.0 ...`
  - `Checking up-linux-streamer-plugin v0.1.0 ...`
  - `Finished 'dev' profile ...`
- Conclusion: bundled transport feature matrix clippy passes.

19) Command: `if [ -n "$VSOMEIP_INSTALL_PATH" ]; then printf "%s\n" "$VSOMEIP_INSTALL_PATH"; else printf "VSOMEIP_INSTALL_PATH is not set\n"; fi`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: `0` (pass)
- Key output:
  - `VSOMEIP_INSTALL_PATH is not set`
- Conclusion: unbundled matrix prerequisite is unavailable in this environment.

20) Unbundled matrix status:
- Commands skipped due missing prerequisite:
  - `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
  - `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- Remediation path:
  - Export `VSOMEIP_INSTALL_PATH` to a valid vsomeip install tree.
  - Re-run the two unbundled commands above from repo root.

## 6.4 Optional smoke escalation trigger

- Trigger decision: **not triggered**.
- Rationale: route resolution behavior was preserved (identity key representation changed, behavior covered by targeted and workspace tests, no material routing-policy change).

## Gate 6 decision

- Result: **PASS with constrained unbundled skip**
- Rationale: all required and bundled CI-parity commands are green; unbundled matrix is blocked only by unavailable `VSOMEIP_INSTALL_PATH`, documented with concrete remediation.
