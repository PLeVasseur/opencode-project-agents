# Phase 0 Baseline Report

Date: 2026-02-11
Phase: 0 - Baseline and scoping
Result: PASS

## Evidence

### 1) Baseline branch/status/hash capture

- exact command: `git rev-parse --abbrev-ref HEAD && git status --short --branch && git rev-parse HEAD`
- working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `refactor/up-streamer-domain-architecture`
  - `## refactor/up-streamer-domain-architecture...origin/refactor/up-streamer-domain-architecture`
  - `da0fcb171b0a5127a896cb3351ce220f28209153`
- concise conclusion: Execution started on the pinned branch with a clean working tree.

### 2) Formatting baseline

- exact command: `source build/envsetup.sh highest && cargo fmt -- --check`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Set GENERIC_CPP_STDLIB_PATH=/usr/include/c++/14`
  - `Set ARCH_SPECIFIC_CPP_STDLIB_PATH=/usr/include/x86_64-linux-gnu/c++/14`
- concise conclusion: Formatting check passed with no required edits.

### 3) Clippy baseline (`up-streamer`)

- exact command: `source build/envsetup.sh highest && cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Checking up-streamer v0.1.0 (.../up-streamer)`
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 4.12s`
- concise conclusion: `up-streamer` passes strict clippy for all targets.

### 4) Test baseline (`up-streamer`)

- exact command: `source build/envsetup.sh highest && cargo test -p up-streamer`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `test result: ok. 37 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out`
  - `test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out`
  - `test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out` (integration suites)
  - `Doc-tests up_streamer ... test result: ok. 8 passed; 0 failed`
- concise conclusion: Baseline unit, integration, and doc tests pass for `up-streamer`.

### 5) Benchmark baseline (`streamer_criterion`)

- exact command: `source build/envsetup.sh highest && cargo bench -p up-streamer --bench streamer_criterion -- --noplot`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `routing_lookup/exact_authority time: [62.686 us 62.989 us 63.349 us]`
  - `routing_lookup/wildcard_authority time: [67.414 us 68.905 us 70.535 us]`
  - `publish_resolution/source_filter_derivation time: [85.432 us 86.594 us 87.801 us]`
  - `ingress_registry/register_route time: [1.4819 ms 1.4955 ms 1.5092 ms]`
  - `ingress_registry/unregister_route time: [1.4933 ms 1.5051 ms 1.5181 ms]`
  - `egress_forwarding/single_route_dispatch time: [258.72 ns 263.51 ns 269.04 ns]`
- concise conclusion: Baseline benchmark metrics were captured for all tracked hotspots and will be used for Phase 2 no-regression comparison.

## Phase 0 Exit Criteria Assessment

- Baseline commands, outputs, and benchmark notes recorded: PASS
