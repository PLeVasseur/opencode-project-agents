# Bug #1 Validation Report: vSomeIP streamer use-case detection (PR #42)

## Scope

Validated the `up-transport-vsomeip-rust` streamer-listener classification bug and confirmed behavior:

1. **Baseline** (pre-fix commit in downstream lockfile)
2. **With PR #42 commit** (`3e277e835916b9428d8492ea1ae1383c5131bca6`)

Downstream scenario used: `zenoh_someip` + `someip_client` <-> `zenoh_service` (issue `up-streamer-rust#69` flow).

---

## Environment + setup

- Repo under test: `up-streamer-rust`
- SOME/IP runtime setup:
  - `source build/envsetup.sh highest`
  - `LD_LIBRARY_PATH` includes bundled `vsomeip` libs built under `target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib`
- Scenario started from `example-streamer-implementations` directory with `DEFAULT_CONFIG.json5`

---

## Dependency revisions tested

### Baseline (pre-fix)

- `up-transport-vsomeip` resolved to:
  - `cb0151394966a4ed5047b246da62c4a9352a90a4`
  - Evidence: prior `Cargo.lock` resolution captured during baseline run logs

### Fixed (PR #42 commit)

- `Cargo.toml` pin in downstream workspace:
  - `up-transport-vsomeip = { git = "https://github.com/eclipse-uprotocol/up-transport-vsomeip-rust", rev = "3e277e835916b9428d8492ea1ae1383c5131bca6", default-features = false }`
  - File: `Cargo.toml:57`
- `Cargo.lock` resolved source:
  - `git+https://github.com/eclipse-uprotocol/up-transport-vsomeip-rust?rev=3e277e835916b9428d8492ea1ae1383c5131bca6#3e277e835916b9428d8492ea1ae1383c5131bca6`
  - File: `Cargo.lock:4871`

---

## Commands used

Build:

```bash
source build/envsetup.sh highest
cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport vsomeip-transport bundled-vsomeip"
cargo build -p example-streamer-uses --bin someip_client --features "vsomeip-transport bundled-vsomeip"
cargo build -p example-streamer-uses --bin zenoh_service --features "zenoh-transport"
```

Run scenario (baseline/fixed, same shape):

```bash
source ../build/envsetup.sh highest
export LD_LIBRARY_PATH="<bundled-vsomeip-lib-dirs>:${LD_LIBRARY_PATH:-}"
export RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug"

timeout 90s ../target/debug/zenoh_someip --config="DEFAULT_CONFIG.json5" > /tmp/<streamer_log> 2>&1 &
timeout 45s ../target/debug/someip_client > /tmp/<client_log> 2>&1 &
timeout 45s ../target/debug/zenoh_service > /tmp/<service_log> 2>&1 &
```

Captured logs:

- Baseline:
  - `/tmp/bug1_baseline_streamer_trace.log`
  - `/tmp/bug1_baseline_client_trace.log`
  - `/tmp/bug1_baseline_service_trace.log`
- Fixed:
  - `/tmp/bug1_fixed_streamer_trace.log`
  - `/tmp/bug1_fixed_client_trace.log`
  - `/tmp/bug1_fixed_service_trace.log`

---

## Baseline results (pre-fix)

### Expected failing behavior reproduced

- Streamer listener registration classified as **Request** instead of streamer/use-case `AllPointToPoint`:
  - `registration_type: Request`
  - Evidence: `/tmp/bug1_baseline_streamer_trace.log:52`
- SOME/IP routing failure repeatedly observed:
  - `Routing info for remote service could not be found!`
  - First occurrence: `/tmp/bug1_baseline_streamer_trace.log:93`
  - Repeats continuously after that in same log
- End-to-end forwarding did **not** complete.

---

## Fixed results (PR #42 commit)

### Streamer use-case now detected correctly

- `streamer_use_case final result: true`
  - Evidence: `/tmp/bug1_fixed_streamer_trace.log:62`
- `registration_type: AllPointToPoint`
  - Evidence: `/tmp/bug1_fixed_streamer_trace.log:64`

### End-to-end forwarding now works

- Requests from SOME/IP side are received/forwarded by streamer:
  - Evidence: `/tmp/bug1_fixed_streamer_trace.log:121`
- Responses are forwarded back and sent over SOME/IP:
  - Evidence: `/tmp/bug1_fixed_streamer_trace.log:177`
- Client receives correlated responses with successful commstatus:
  - `MT_RESPONSE type`, `request_id` correlation, `commstatus: Some(OK)`
  - Evidence: `/tmp/bug1_fixed_client_trace.log:169`, `/tmp/bug1_fixed_client_trace.log:170`, `/tmp/bug1_fixed_client_trace.log:177`

No `Routing info for remote service could not be found` errors were observed in fixed streamer logs.

---

## Regression sanity checks from logs

- Publish registration path still present:
  - `registration_type: Publish`
  - Evidence: `/tmp/bug1_fixed_streamer_trace.log:86`
- Request/response classification still behaves as expected for normal traffic:
  - Request path evidence: `/tmp/bug1_fixed_client_trace.log:80`
  - Response path evidence: `/tmp/bug1_fixed_client_trace.log:169`

---

## Conclusion

PR #42 commit `3e277e835916b9428d8492ea1ae1383c5131bca6` resolves the streamer use-case misclassification that caused the downstream forwarding failure in the issue #69 scenario.

- **Baseline:** reproduced failure (misclassification + routing failure)
- **With PR commit:** streamer detection corrected + end-to-end request/response flow succeeds

This provides high confidence that merging PR #42 fixes the reported bug, with downstream depending on consuming the merged commit (via release or temporary pin).
