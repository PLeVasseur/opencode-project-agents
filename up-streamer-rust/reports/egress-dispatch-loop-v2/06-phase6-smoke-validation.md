# Phase 6 Report - Mandatory Smoke Validation (8 Scenarios)

- Phase: 6 - Mandatory Smoke Validation
- Gate: 6
- Result: PASS (all 8 scenarios)

## Evidence

### Entry 1
- Exact command:

```bash
set -euo pipefail && git rev-parse --abbrev-ref HEAD && git status --short --branch
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `refactor/up-streamer-domain-architecture`
  - `## refactor/up-streamer-domain-architecture...origin/refactor/up-streamer-domain-architecture [ahead 1]`
- Conclusion: Required pre-phase branch/status recording executed before smoke phase.

### Entry 2
- Exact command:

```bash
set -euo pipefail && source build/envsetup.sh highest && docker compose -f utils/mosquitto/docker-compose.yaml up -d
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `Set GENERIC_CPP_STDLIB_PATH=/usr/include/c++/14`
  - `Set ARCH_SPECIFIC_CPP_STDLIB_PATH=/usr/include/x86_64-linux-gnu/c++/14`
  - `Container mosquitto-mosquitto-1  Started`
- Conclusion: Base Phase 6 prerequisites (env setup + broker startup) were met.

### Entry 3
- Exact command:

```bash
set -euo pipefail && source build/envsetup.sh highest && cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" && cargo build -p example-streamer-uses --bin someip_client --features "vsomeip-transport,bundled-vsomeip"
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `Compiling up-linux-streamer v0.1.0`
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s)`
- Conclusion: SOME/IP binaries and runtime prerequisites were available for all SOME/IP smoke scenarios.

### Entry 4
- Exact command:

```bash
set -euo pipefail && docker compose -f utils/mosquitto/docker-compose.yaml down && pgrep -fa "configurable-streamer|zenoh_someip|mqtt_(publisher|subscriber|client|service)|someip_(publisher|subscriber|client|service)|zenoh_(publisher|subscriber|client|service)" || true
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `Container mosquitto-mosquitto-1  Removed`
  - `Network mosquitto_default  Removed`
- Conclusion: Post-validation cleanup completed with no lingering transport smoke processes.

## Scenario Outcomes

- `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber`: PASS (`$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber.md`)
- `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber`: PASS (`$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber.md`)
- `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service`: PASS (`$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service.md`)
- `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service`: PASS (`$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service.md`)
- `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber`: PASS (`$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber.md`)
- `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber`: PASS (`$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber.md`)
- `smoke-zenoh-someip-rr-zenoh-client-someip-service`: PASS (`$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-someip-rr-zenoh-client-someip-service.md`)
- `smoke-zenoh-someip-rr-someip-client-zenoh-service`: PASS (`$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service.md`)

## Conclusion

- All mandated smoke scenarios executed and satisfied their scenario-level validation criteria.
- No constrained skips were needed.
