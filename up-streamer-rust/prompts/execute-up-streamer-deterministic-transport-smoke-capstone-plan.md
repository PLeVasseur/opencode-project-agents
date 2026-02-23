Execute the plan at:

`$OPENCODE_CONFIG_DIR/plans/up-streamer-deterministic-transport-smoke-capstone-plan.md`

Fresh-session execution requirements:

1. Manual execution only. Do not use autopilot orchestration.
2. First action must be to read and honor the plan section:
   - `## Fresh Session Kickoff (Locked Contract)`
   - Treat every `[x]` item there as non-negotiable unless explicitly overridden by the user.
3. Keep execution branch runtime-selected:
   - Do not hardcode branch names.
   - Only enforce branch matching if `--expected-branch` or `SMOKE_EXPECTED_BRANCH` is provided.
4. Execute the plan in strict section order and do not skip gates:
   - architecture and crate setup -> deterministic controls -> claims/orchestration -> scenario binaries -> matrix runner -> tests/docs/workflow -> validation matrix.
5. Continuously update the plan in place; flip each completed checkbox from `[ ]` to `[x]` immediately.

Implementation lock points (must remain intact):

1. Deterministic run contract
   - Active senders use bounded runs (`send-count`/`send-interval-ms`) and complete all configured sends before final claim evaluation.
   - No early-pass termination in v1.

2. Readiness contract
   - Canonical readiness markers are raw stdout lines emitted with `println!`:
     - `READY streamer_initialized`
     - `READY listener_registered`
   - Marker parsing must not depend on tracing subscriber formatting or `RUST_LOG` filters.

3. Claims contract
   - Keep locked thresholds and semantics from the plan.
   - Use narrow forbidden signatures; avoid broad generic patterns.
   - Keep scenario-specific claims explicit and auditable.

4. Matrix contract
   - Run scenarios sequentially, continue after failures, emit full summary, return non-zero if any scenario fails.

5. Profile and CI contract
   - SOME/IP v1 remains bundled-only.
   - Workflow mode remains `workflow_dispatch` + nightly only.
   - Nightly schedule remains `03:00 UTC` (`0 3 * * *`).
   - MQTT and SOME/IP run in separate jobs; artifact upload uses `if: always()`.

Hygiene and commit discipline:

1. Before each phase and before each commit, run and record:
   - `git rev-parse --abbrev-ref HEAD`
   - `git status --short --branch`
2. Before each commit, also run and record:
   - `git diff --name-only --cached`
   - `git diff --stat --cached`
3. Keep commit sequence aligned to plan section `## 16) Commit Plan (Scoped Chunks)`.
4. Never stage repo-local operational artifacts by mistake (`plans/`, `prompts/`, `reports/` in repo root).

Artifacts and reporting:

1. Runtime smoke artifacts default under `target/transport-smoke/...` with optional `--artifacts-root` override.
2. If execution notes/reports are needed, write them under:
   - `$OPENCODE_CONFIG_DIR/reports/transport-smoke-capstone/`
3. Scenario/matrix JSON outputs must follow the locked schema in plan section `11.1`.

Validation and blocking policy:

1. Treat plan section `## 15) Validation Matrix` as mandatory completion gate.
2. If any gate fails, stop progression, capture exact command/output, and record blocker details.
3. Ask one targeted question only when blocked by missing external prerequisite or ambiguity that materially changes behavior.

Completion deliverable in the fresh session:

- concise execution summary by plan section
- changed files by commit chunk (A-E)
- validation matrix results
- scenario and matrix outcome summary
- any accepted deviations and rationale
