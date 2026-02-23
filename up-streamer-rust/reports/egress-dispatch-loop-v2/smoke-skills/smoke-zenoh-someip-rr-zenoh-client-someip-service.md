# Smoke Report: smoke-zenoh-someip-rr-zenoh-client-someip-service

- Result: PASS
- Artifacts: `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-someip-rr-zenoh-client-someip-service-artifacts`

## Evidence

### Entry 1
- Exact command:

```bash
set -euo pipefail && source ../build/envsetup.sh highest && export SCENARIO="smoke-zenoh-someip-rr-zenoh-client-someip-service" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && shopt -s nullglob && vsomeip_libs=("$PWD"/../target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib) && test ${#vsomeip_libs[@]} -gt 0 && export LD_LIBRARY_PATH="${vsomeip_libs[0]}:${LD_LIBRARY_PATH:-}" && export RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug" && { cargo run --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" -- --config "DEFAULT_CONFIG.json5" > "$ARTIFACT_DIR/streamer.log" 2>&1 & STREAMER_PID=$!; printf '%s\n' "$STREAMER_PID" > "$ARTIFACT_DIR/streamer.pid"; } && sleep 4
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/example-streamer-implementations`
- Exit status: `0` (pass)
- Key output lines:
  - `Set GENERIC_CPP_STDLIB_PATH=/usr/include/c++/14`
  - `Set ARCH_SPECIFIC_CPP_STDLIB_PATH=/usr/include/x86_64-linux-gnu/c++/14`
- Conclusion: SOME/IP streamer runtime was started correctly.

### Entry 2
- Exact command:

```bash
set -euo pipefail && source build/envsetup.sh highest && export SCENARIO="smoke-zenoh-someip-rr-zenoh-client-someip-service" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && shopt -s nullglob && vsomeip_libs=("$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib) && test ${#vsomeip_libs[@]} -gt 0 && export LD_LIBRARY_PATH="${vsomeip_libs[0]}:${LD_LIBRARY_PATH:-}" && { RUST_LOG=info cargo run -p example-streamer-uses --bin someip_service --features "vsomeip-transport,bundled-vsomeip" > "$ARTIFACT_DIR/service.log" 2>&1 & SERVICE_PID=$!; printf '%s\n' "$SERVICE_PID" > "$ARTIFACT_DIR/service.pid"; } && sleep 4
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `Set GENERIC_CPP_STDLIB_PATH=/usr/include/c++/14`
  - `Set ARCH_SPECIFIC_CPP_STDLIB_PATH=/usr/include/x86_64-linux-gnu/c++/14`
- Conclusion: SOME/IP service launched with bundled runtime libraries.

### Entry 3
- Exact command:

```bash
set -euo pipefail && export SCENARIO="smoke-zenoh-someip-rr-zenoh-client-someip-service" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && rg -n -m 3 "ServiceResponseListener: Received a message|UMESSAGE_TYPE_RESPONSE" "$ARTIFACT_DIR/client.log" && rg -n -m 3 "ServiceResponseListener: Received a message|Sending Response message" "$ARTIFACT_DIR/service.log" && if rg -n "Routing info for remote service could not be found|Static subscription file not found|panicked" "$ARTIFACT_DIR/streamer.log"; then exit 1; fi
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `21: ... zenoh_client::common ... ServiceResponseListener: Received a message ... UMESSAGE_TYPE_RESPONSE ... commstatus: Some(OK) ...`
  - `21: ... someip_service::common ... ServiceResponseListener: Received a message ...`
  - `22: ... someip_service::common ... Sending Response message:`
  - (no matches for critical streamer error signature)
- Conclusion: Zenoh client to SOME/IP service request/response path passed without critical streamer errors.

### Entry 4
- Exact command:

```bash
set -euo pipefail && export SCENARIO="smoke-zenoh-someip-rr-zenoh-client-someip-service" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && if test -f "$ARTIFACT_DIR/service.pid"; then kill -INT "$(< "$ARTIFACT_DIR/service.pid")" || true; fi && if test -f "$ARTIFACT_DIR/streamer.pid"; then kill -INT "$(< "$ARTIFACT_DIR/streamer.pid")" || true; fi && sleep 1 && if test -f "$ARTIFACT_DIR/service.pid"; then kill -TERM "$(< "$ARTIFACT_DIR/service.pid")" || true; fi && if test -f "$ARTIFACT_DIR/streamer.pid"; then kill -TERM "$(< "$ARTIFACT_DIR/streamer.pid")" || true; fi && pgrep -fa "zenoh_someip|zenoh_client|someip_service" || true
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `/bin/bash: line 1: kill: (...) - No such process` (streamer already exited)
  - `1418845 target/debug/someip_service`
- Conclusion: Initial teardown left one lingering `someip_service` process requiring follow-up cleanup.

### Entry 5
- Exact command:

```bash
set -euo pipefail && kill -INT 1418845 || true && sleep 1 && kill -TERM 1418845 || true && pgrep -fa "zenoh_someip|zenoh_client|someip_service" || true
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `/bin/bash: line 1: kill: (1418845) - No such process`
  - (no remaining matching scenario processes)
- Conclusion: Residual service process was fully cleared; scenario cleanup completed.
