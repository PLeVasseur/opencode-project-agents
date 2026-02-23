## DG-1 decision (pre-runtime)

Date: 2026-02-09
Decision: **Path A**

### Rationale

- Subscription rows are semantically identified by `topic + subscriber`; retaining subscriber-only identity drops valid rows when one subscriber has multiple topic subscriptions.
- Path A is required to satisfy follow-up requirement 4 (same-subscriber/different-topic coexistence and rebuild/removal reflection tests).
- Path A increases overlap exposure, so streamer-side effective publish listener key dedupe is mandatory and will be implemented symmetrically for register/unregister.

### Guardrails

- Right-side wildcard expansion remains limited to subscriber authority `*` only (`//*/...` on the right side).
- Tuple strictness remains unchanged for source matching.
- Add-failure rollback behavior remains transactional for true non-duplicate listener setup failures.

### Notes

- Attempted to load `rust-test-quality-gate` skill before non-trivial test authoring; skill is unavailable in this session tool registry. Test quality constraints from plan are applied explicitly in this execution.
