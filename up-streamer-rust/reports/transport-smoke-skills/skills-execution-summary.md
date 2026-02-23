# Transport Smoke Skill Execution Summary

## Scope

Executed 8 smoke skills (request/response in both directions, pub/sub in both directions) across:

- Zenoh <=> SOME/IP via `up-linux-streamer` bin `zenoh_someip`
- Zenoh <=> MQTT via `configurable-streamer`

## Overall result

- Passed skills: 8/8
- Failed skills after fixes: 0/8

## Skill outcomes

1. `smoke-zenoh-someip-rr-someip-client-zenoh-service` -> PASS
2. `smoke-zenoh-someip-rr-zenoh-client-someip-service` -> PASS
3. `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber` -> PASS
4. `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber` -> PASS (after fix)
5. `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service` -> PASS
6. `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service` -> PASS
7. `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber` -> PASS
8. `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber` -> PASS

## Fixes made while exercising skills

### Fix 1: Explicit runtime logging for validation markers

- Problem: Some binaries did not emit deterministic info-level markers without explicit `RUST_LOG`.
- Change: Added explicit `RUST_LOG` exports in client/publisher commands across skills that validate log markers.
- Effect: Validation regex checks are now stable and reproducible.

### Fix 2: SOME/IP subscriber local URI resource constraint

- Problem: `someip_subscriber` failed with `ValidationError("Resource ID must be 0x0")` when run with `--resource 0x1234`.
- Change: Updated skill `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber` to use `--resource 0x0` for local SOME/IP subscriber identity while keeping publish source filter overrides.
- Effect: Subscriber starts correctly and receives bridged publish traffic.

## Notes

- Client/publisher loops use `timeout 45s`; exit code `124` is expected and accepted when pass markers are present in logs.
- Non-interactive teardown occasionally required SIGTERM fallback after SIGINT for parked background processes.

## Recovered evidence verification (post-crash resume)

Artifacts were recovered from existing per-skill directories and re-validated without re-running full smoke triads.

### 1) smoke-zenoh-someip-rr-someip-client-zenoh-service

- Command: `REPORT="$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service"; rg -n -m 2 "UMESSAGE_TYPE_RESPONSE|commstatus: Some\\(OK\\)" "$REPORT/client.validation" && rg -n -m 2 "ServiceResponseListener: Received a message|Sending Response message" "$REPORT/service.validation" && if rg -n "Routing info for remote service could not be found|Static subscription file not found|panicked" "$REPORT/streamer.log"; then exit 1; else printf '%s\\n' "streamer guard: no forbidden patterns"; fi`
- Working directory: repo root
- Exit status: `0` (pass)
- Key output lines: `UMESSAGE_TYPE_RESPONSE ... commstatus: Some(OK)`; `ServiceResponseListener: Received a message`; `Sending Response message`
- Conclusion: PASS

### 2) smoke-zenoh-someip-rr-zenoh-client-someip-service

- Command: `REPORT="$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-someip-rr-zenoh-client-someip-service"; rg -n -m 2 "UMESSAGE_TYPE_RESPONSE|commstatus: Some\\(OK\\)" "$REPORT/client.validation" && rg -n -m 2 "ServiceResponseListener: Received a message|Sending Response message" "$REPORT/service.validation" && if rg -n "Routing info for remote service could not be found|Static subscription file not found|panicked" "$REPORT/streamer.log"; then exit 1; else printf '%s\\n' "streamer guard: no forbidden patterns"; fi`
- Working directory: repo root
- Exit status: `0` (pass)
- Key output lines: `ServiceResponseListener: Received a message`; `Sending Response message`; `streamer guard: no forbidden patterns`
- Conclusion: PASS

### 3) smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber

- Command: `REPORT="$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber"; rg -n -m 2 "Publishing message|Published message|Sending" "$REPORT/publisher.validation" && rg -n -m 2 "PublishReceiver: Received a message|Received a message" "$REPORT/subscriber.validation" && rg -n -m 2 "forward|publish|listener|route" "$REPORT/streamer.validation"`
- Working directory: repo root
- Exit status: `0` (pass)
- Key output lines: `Sending Publish message`; `PublishReceiver: Received a message`
- Conclusion: PASS

### 4) smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber

- Command: `REPORT="$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber"; rg -n -m 2 "Publishing message|Published message|Sending" "$REPORT/publisher.validation" && rg -n -m 2 "PublishReceiver: Received a message|Received a message" "$REPORT/subscriber.validation" && rg -n -m 2 "forward|publish|listener|route" "$REPORT/streamer.validation"`
- Working directory: repo root
- Exit status: `0` (pass)
- Key output lines: `Sending Publish message`; `PublishReceiver: Received a message`
- Conclusion: PASS

### 5) smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service

- Command: `REPORT="$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service"; rg -n -m 2 "UMESSAGE_TYPE_RESPONSE|ServiceResponseListener: Received a message" "$REPORT/client.validation" && rg -n -m 2 "ServiceResponseListener: Received a message|Sending Response message" "$REPORT/service.validation" && rg -n -m 2 "request|response|dispatch|forward" "$REPORT/streamer.validation" && if rg -n "." "$REPORT/failure-signatures"; then exit 1; else printf '%s\\n' "failure-signatures guard: no forbidden patterns"; fi`
- Working directory: repo root
- Exit status: `0` (pass)
- Key output lines: `ServiceResponseListener: Received a message`; `Sending Response message`; `failure-signatures guard: no forbidden patterns`
- Conclusion: PASS

### 6) smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service

- Command: `REPORT="$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service"; rg -n -m 2 "UMESSAGE_TYPE_RESPONSE|ServiceResponseListener: Received a message" "$REPORT/client.validation" && rg -n -m 2 "ServiceResponseListener: Received a message|Sending Response message" "$REPORT/service.validation" && rg -n -m 2 "request|response|dispatch|forward" "$REPORT/streamer.validation" && if rg -n "." "$REPORT/failure-signatures"; then exit 1; else printf '%s\\n' "failure-signatures guard: no forbidden patterns"; fi`
- Working directory: repo root
- Exit status: `0` (pass)
- Key output lines: `ServiceResponseListener: Received a message`; `Sending Response message`; `failure-signatures guard: no forbidden patterns`
- Conclusion: PASS

### 7) smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber

- Command: `REPORT="$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber"; rg -n -m 2 "Publishing message|Published message|Sending" "$REPORT/publisher.validation" && rg -n -m 2 "PublishReceiver: Received a message|Received a message" "$REPORT/subscriber.validation" && rg -n -m 2 "publish|listener|route|forward" "$REPORT/streamer.validation"`
- Working directory: repo root
- Exit status: `0` (pass)
- Key output lines: `Sending Publish message`; `PublishReceiver: Received a message`
- Conclusion: PASS

### 8) smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber

- Command: `REPORT="$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber"; rg -n -m 2 "Publishing message|Published message|Sending" "$REPORT/publisher.validation" && rg -n -m 2 "PublishReceiver: Received a message|Received a message" "$REPORT/subscriber.validation" && rg -n -m 2 "publish|listener|route|forward" "$REPORT/streamer.validation"`
- Working directory: repo root
- Exit status: `0` (pass)
- Key output lines: `Sending Publish message`; `PublishReceiver: Received a message`
- Conclusion: PASS
