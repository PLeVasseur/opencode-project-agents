Execute this implementation plan end-to-end:
`$OPENCODE_CONFIG_DIR/plans/reviewer-bot-burst-pr-assignment-remediation-2026-02-11.md`

Execution rules:
- Treat the plan as source of truth and keep it updated in real time.
- Check off each checkbox immediately when completed (do not batch updates).
- If blocked, stop and log the blocker in the plan with a timestamp and exact failing command.
- Run fresh-session bootstrap exactly as written, including branching from `upstream/main`.
- Keep this as one comprehensive implementation PR.

Implementation requirements (must preserve intent):
- Implement durable in-repo lease locking with optimistic concurrency (`ETag` + `If-Match`).
- Guarantee event durability: process every event or fail loudly with diagnostics.
- Enforce lock boundary: acquire before first mutating state read, release after final `save_state()` attempt.
- Preserve queue policy: read-level members remain assignable as designated reviewers.
- Do not claim GitHub reviewer request success when reviewer request API returns `422`.

Critical contract (do not violate):
- `save_state()` must no longer blind-rewrite issue body.
- Preserve lock metadata and YAML state blocks via explicit parse/render markers.
- All state issue writes must use conditional patching to avoid stale clobber.
- Add tests proving lock metadata cannot be lost or corrupted across saves.

Mandatory approval behavior to implement:
- Create/use label `triage approver required` (idempotent create-if-missing).
- If a read-level designated reviewer approves, mark review complete immediately.
- Post one escalation comment per PR, pinging:
  - `@PLeVasseur @felix91gr @rcseacord @plaindocs @AlexCeleste @sei-dsvoboda`
- First triage+ `APPROVED` satisfies mandatory approval and clears escalation label/state.

Quality gates:
- `uv run ruff check --fix`
- `uv run pytest .github/reviewer-bot-tests`

Shipping rules:
- Use Conventional Commit message style.
- Open PR against upstream with:
  - `--repo rustfoundation/safety-critical-rust-coding-guidelines`
  - `--head PLeVasseur:<branch>`
- Do not merge to `main` yourself; hand off to maintainer.

Final report must include:
- root cause recap
- lock contract and preserve/update strategy
- mandatory triage approval workflow changes
- validation evidence (tests + live verification commands)
- exact plan checkbox status
