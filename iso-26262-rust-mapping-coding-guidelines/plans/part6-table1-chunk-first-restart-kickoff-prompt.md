# Part 6 Table 1 Retrieval Restart Kickoff Prompt (Rip-and-Replace)

Use this prompt to start a fresh implementation session for the restart.

```text
You are continuing the Part 6 Table 1 retrieval restart (rip-and-replace).

Working repo:
- /home/pete.levasseur/personal/iso-26262-rust-mapping-coding-guidelines

First, read these files in order:
1) $OPENCODE_CONFIG_DIR/feedback/rust-reference/retrieval-restart-plan-feedback.md
2) $OPENCODE_CONFIG_DIR/plans/part6-table1-chunk-first-session-bootstrap-capsule.md
3) $OPENCODE_CONFIG_DIR/plans/part6-table1-chunk-first-retrieval-restart-plan.md
4) $OPENCODE_CONFIG_DIR/plans/part6-table1-retrieval-restart-implementation-runbook.md

Then do the following in order:
1) Summarize current restart state, constraints, and blockers in <= 8 bullets.
2) Validate runbook prerequisites under "Required Interfaces Before Running Cycles".
3) If any prerequisite is missing, implement it first with tests and report what changed.
4) Continue implementation from the earliest unchecked step in the restart plan.
5) Run only the commands needed for the current step from the implementation runbook.
6) Keep the active DB at .cache/sqlite_kb/current/rust_reference.sqlite, and save cycle artifacts under .cache/sqlite_kb/reports/rust_reference/restart_phase0/<RUN_ID>/...
   - If the canonical DB is stale (`user_version < 6` or no `chunks` table), rebuild it before materialization/eval/review.
7) Update:
   - $OPENCODE_CONFIG_DIR/plans/part6-table1-chunk-first-retrieval-restart-plan.md (checkboxes)
   - $OPENCODE_CONFIG_DIR/plans/part6-table1-chunk-first-session-bootstrap-capsule.md (new paths/facts)
8) When a step is complete, create a commit before moving to the next step:
   - use Conventional Commits,
   - include step number in subject,
   - include commands/artifacts/blockers in commit body.

Guardrails:
- Keep deterministic source pinning exactly as defined.
- Do not point active `--db-path` to restart artifact directories.
- Do not run legacy control artifact freeze/copy/compare.
- Do not introduce statement_id compatibility mapping.
- Do not change thresholds/policies unless explicitly requested.
- Commit after each completed step; do not batch multiple steps into one commit.
- Do not push unless explicitly requested.

At the end, return:
- concise status by restart step (done/pending/blocker),
- exact artifact paths generated,
- the next 3 highest-priority actions.
```
