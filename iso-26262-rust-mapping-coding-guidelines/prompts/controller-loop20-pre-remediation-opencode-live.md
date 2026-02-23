# Controller Loop20 Prompt (Pre-Remediation)

This is the exact LLM-in-the-loop kickoff command used for the prior `loop20-opencode-live-01` run before the remediation changes.

```bash
CONTROLLER_DECISION_COMMAND='opencode run --dir {repo_root} --model openai/gpt-5.3-codex "You are selecting candidate ids for an autonomous controller iteration. Read decision packet JSON at {decision_packet}. Select up to 2 candidate_id values from packet.candidates that best reduce high-severity deficits, improve hard-gate progress, and minimize regression risk. Prefer explicit gains in decomposition, quality, and known-good alignment lanes. Return ONLY one JSON object with keys selected_candidate_ids (array), rejected_candidate_ids (array), rationale (string), risk_notes (array of strings), confidence (low|medium|high or 0-1), fallback_recommended (boolean). Do not output markdown or commentary."' uv run python scripts/controller_supervisor.py --session-id loop20-opencode-live-01 --max-loops 20 --controller-arg=--decision-policy --controller-arg=.cache/controller/decision_policy.loop20-opencode-live.yaml --controller-arg=--max-iterations --controller-arg=20 --controller-arg=--stall-window --controller-arg=5 --controller-arg=--beam-width --controller-arg=6 --controller-arg=--max-actions-per-bundle --controller-arg=3 --controller-arg=--full-eval-top-k --controller-arg=2
```
