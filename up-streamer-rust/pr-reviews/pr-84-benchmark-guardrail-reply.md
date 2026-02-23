Thanks for calling this out. You are right that the intent was not clear enough.

I updated the PR summary to make the purpose explicit, including `Why`, `What This Adds`, `What This Does Not Do`, and `CI Mode (Advisory)` with the rationale for advisory mode and the promotion criteria.

I also expanded the repo docs in `up-streamer/README.md` under `Benchmark Guardrails` to explain what the guardrail checks, how pass/fail is computed from Criterion `raw.csv`, what `allocation_proxy` means here, and how local hard-fail differs from CI advisory behavior.

If anything is still unclear, I can tighten the wording further.
