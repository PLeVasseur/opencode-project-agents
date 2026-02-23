# Controller Loop20 Prompt (Post-Remediation, Decision + Rewrite LLM)

This bundle defines both inner prompts and a 20-iteration controller launch command.

Important precondition for rewrite LLM:
- `config/controller_rewrite_policy.yaml` must have `enabled: true` and `llm.enabled: true`.

```bash
#!/usr/bin/env bash
set -euo pipefail

cat > .cache/controller/decision_policy.loop20-post-remediation.yaml <<'YAML'
version: 1
enabled: true
max_selected_candidates: 2
llm:
  enabled: true
  fallback_to_deterministic: true
  command: []
YAML

DECISION_PROMPT="$(cat <<'PROMPT'
You are selecting candidate ids for an autonomous controller iteration.
Read decision packet JSON at {decision_packet}.

Objective:
Select up to 2 candidate_id values from packet.candidates that maximize net quality improvement while minimizing regression risk.

Priority order:
1) Reduce critical/high deficits first.
2) Improve hard-gate progress and lane health, especially decomposition, quality, known-good alignment, diversity, and rust grounding.
3) Prefer candidates with positive expected_lane_deltas and lower risk_penalty and mutation_footprint_estimate.
4) Avoid suppressed or repeatedly failing bundle signatures unless they directly target highest-severity deficits.
5) Near-duplicate wording is acceptable only when both are true: distinct obligation_units and clearly different verification constraints.

Use packet fields directly:
- deficits_summary
- observation_summary
- candidates[].expected_lane_deltas
- candidates[].risk_penalty
- candidates[].mutation_footprint_estimate
- candidates[].bundle_signature
- suppressed_signatures
- historical_signatures

Set fallback_recommended=true only when no candidate set has credible net-positive impact with acceptable regression risk.

Return ONLY one JSON object with keys:
- selected_candidate_ids (array)
- rejected_candidate_ids (array)
- rationale (string)
- risk_notes (array of strings)
- confidence (low|medium|high)
- fallback_recommended (boolean)

Do not output markdown or commentary.
PROMPT
)"

REWRITE_PROMPT="$(cat <<'PROMPT'
You are rewriting one guideline used by an autonomous controller.
Read rewrite packet JSON at {rewrite_packet}. Use only packet context.

Primary goals:
1) Preserve the same safety intent and obligation scope.
2) Increase specificity, enforceability, and verification clarity.
3) Increase lexical/structural diversity vs nearest_neighbors.
4) Improve Rust grounding quality using concrete citation markers.

Hard constraints:
- Keep obligation_units and technical scope intact.
- rule_statement must be 10-52 words and include a normative modal (shall/must/avoid/require).
- amplification, exceptions, and rationale must include verification/evidence language (verify/evidence/test/check/review).
- Near-duplicate wording is allowed only when both are true: distinct obligation_units and divergent verification constraints.
- Do not copy neighbor rule text verbatim.

Output:
Return ONLY one JSON object with exactly these keys:
- rule_statement (string)
- amplification (string)
- exceptions (string)
- rationale (string)
- citation_plan (array of strings, prefer :cite:`...` and :std:`...` markers)
- uniqueness_rationale (string)
- confidence (low|medium|high)

No markdown. No extra keys.
PROMPT
)"

export CONTROLLER_DECISION_COMMAND="opencode run --dir {repo_root} --model openai/gpt-5.3-codex \"$DECISION_PROMPT\""
export CONTROLLER_REWRITE_COMMAND="opencode run --dir {repo_root} --model openai/gpt-5.3-codex \"$REWRITE_PROMPT\""

uv run python scripts/controller_supervisor.py \
  --session-id loop20-opencode-live-post-remediation-01 \
  --max-loops 20 \
  --controller-arg=--decision-policy \
  --controller-arg=.cache/controller/decision_policy.loop20-post-remediation.yaml \
  --controller-arg=--max-iterations \
  --controller-arg=20 \
  --controller-arg=--stall-window \
  --controller-arg=5 \
  --controller-arg=--beam-width \
  --controller-arg=6 \
  --controller-arg=--max-actions-per-bundle \
  --controller-arg=3 \
  --controller-arg=--full-eval-top-k \
  --controller-arg=2
```
