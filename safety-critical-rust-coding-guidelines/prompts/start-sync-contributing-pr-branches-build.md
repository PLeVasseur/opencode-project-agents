Execute this plan end-to-end:
`$OPENCODE_CONFIG_DIR/plans/sync-contributing-pr-branches-2026-02-11.md`

Execution requirements:
- Treat the plan as the source of truth.
- Read the full plan before running commands.
- Check off each checkbox immediately when completed (do not batch updates).
- Confirm both PRs and both branch heads still match the plan before applying changes.
- Preferred path: fast-forward `docs/update-contributing-md-with-bot-details` from `docs/contributing-progressive-disclosure` using `git merge --ff-only`.
- Fallback path only if needed: cherry-pick `252fdba` then `1dd1461` onto `docs/update-contributing-md-with-bot-details`.
- Push only `docs/update-contributing-md-with-bot-details` to `origin` so upstream PR `#331` updates.
- Verify upstream PR `#331` includes the progressive disclosure commits and intended file deltas.
- Do not merge to `main`.
- If blocked, stop and report the blocker with exact command output and recommended resolution.

Final report must include:
- checklist status
- commit graph outcome
- exact commit SHAs now on `docs/update-contributing-md-with-bot-details`
- PR `#331` verification evidence
- disposition recommendation for fork PR `#8`
