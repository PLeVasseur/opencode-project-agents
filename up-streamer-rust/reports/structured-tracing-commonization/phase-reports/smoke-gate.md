# Smoke Gate - Mandatory 8-scenario validation

## Phase pre-check

- Command: `git rev-parse --abbrev-ref HEAD && git status --short --branch`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output:
  - `refactor/up-streamer-domain-architecture`
  - `## refactor/up-streamer-domain-architecture...origin/refactor/up-streamer-domain-architecture [ahead 6]`
- Conclusion: smoke gate started on required execution branch with clean worktree.

## Scenario coverage

- Command: `rg -n "^- Status: PASS$" "$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills"/smoke-*.md; count=$(rg -n "^- Status: PASS$" "$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills"/smoke-*.md | wc -l); printf 'pass_count=%s\n' "$count"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output:
  - `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber.md:5:- Status: PASS`
  - `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber.md:5:- Status: PASS`
  - `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service.md:5:- Status: PASS`
  - `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service.md:5:- Status: PASS`
  - `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber.md:5:- Status: PASS`
  - `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber.md:5:- Status: PASS`
  - `smoke-zenoh-someip-rr-zenoh-client-someip-service.md:5:- Status: PASS`
  - `smoke-zenoh-someip-rr-someip-client-zenoh-service.md:5:- Status: PASS`
  - `pass_count=8`
- Conclusion: all 8 mandatory scenario reports are present and marked PASS.

## Structured logging assertion coverage

- Command: `rg -n "egress_send_attempt.*worker_id|worker_id.*egress_send_attempt" "$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills"/smoke-*.md | wc -l`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output:
  - `16`
- Conclusion: each scenario report contains both the attempt assertion command and matching proof line.

- Command: `rg -n "egress_send_ok.*worker_id|worker_id.*egress_send_ok" "$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills"/smoke-*.md | wc -l`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output:
  - `16`
- Conclusion: each scenario report contains both the success assertion command and matching proof line.

- Command: `rg -n "egress_worker_create.*route_label|egress_worker_reuse.*route_label" "$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills"/smoke-*.md | wc -l`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output:
  - `16`
- Conclusion: each scenario report contains both the route-label assertion command and matching proof line.

- Command: `rg -n "not observed in bounded" "$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills"/smoke-*.md | wc -l`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output:
  - `8`
- Conclusion: each scenario report explicitly records that lag/closed events were not naturally observed in bounded healthy runs.

- Command: `rg -n "constrained-skip|Status: SKIP|Status: CONSTRAINED-SKIP" "$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills"/smoke-*.md`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 1 (pass for negative check)
- Key output:
  - none
- Conclusion: no scenario required constrained-skip handling.

## Gate conclusion

- Status: PASS
- Conclusion: smoke-8 gate is satisfied with all scenarios PASS and mandatory structured logging assertions recorded.
