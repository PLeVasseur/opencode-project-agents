# Controller Loop20 Prompt (Post-Remediation + Example Outcome Rewrite)

This prompt pack extends the post-remediation decision/rewrite flow by making outcome-driven Rust examples first-class in rewrite output.

```bash
#!/usr/bin/env bash
set -euo pipefail

mkdir -p .cache/controller

cat > .cache/controller/decision_policy.loop20-post-remediation-examples.yaml <<'YAML'
version: 1
enabled: true
max_selected_candidates: 2
llm:
  enabled: true
  fallback_to_deterministic: true
  command: []
YAML

# Enable rewrite LLM for this run (restored automatically on exit).
REWRITE_POLICY_PATH="config/controller_rewrite_policy.yaml"
REWRITE_POLICY_BACKUP=".cache/controller/controller_rewrite_policy.backup.yaml"
cp "$REWRITE_POLICY_PATH" "$REWRITE_POLICY_BACKUP"
trap 'cp "$REWRITE_POLICY_BACKUP" "$REWRITE_POLICY_PATH"' EXIT

cat > "$REWRITE_POLICY_PATH" <<'YAML'
version: 1
enabled: true
llm:
  enabled: true
  fallback_to_deterministic: true
  command: []
  max_neighbors: 5
constraints:
  min_rule_words: 10
  max_rule_words: 52
  require_normative_modal: true
  require_verification_phrase: true
YAML

DECISION_PROMPT="$(cat <<'PROMPT'
You are selecting candidate ids for an autonomous controller iteration.
Read decision packet JSON at {decision_packet}.

Objective:
Select up to 2 candidate_id values from packet.candidates that maximize net quality improvement while minimizing regression risk.

Priority order:
1) Reduce critical/high deficits first.
2) Improve hard-gate progress and lane health, especially decomposition, quality, known-good alignment, diversity, rust grounding, and example outcome quality.
3) Prefer candidates that reduce example_outcome_gap, example_assertion_gap, example_negative_evidence_gap, and example_diversity_gap.
4) Prefer candidates with positive expected_lane_deltas and lower risk_penalty and mutation_footprint_estimate.
5) Avoid suppressed or repeatedly failing bundle signatures unless they directly target highest-severity deficits.
6) Near-duplicate wording is acceptable only when both are true: distinct obligation_units and clearly different verification constraints.

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
5) Produce stronger executable example evidence with explicit expected outcomes.

Hard constraints for rule text:
- Keep obligation_units and technical scope intact.
- rule_statement must be 10-52 words and include a normative modal (shall/must/avoid/require).
- amplification, exceptions, and rationale must include verification/evidence language (verify/evidence/test/check/review).
- Near-duplicate wording is allowed only when both are true: distinct obligation_units and divergent verification constraints.
- Do not copy neighbor rule text verbatim.

Hard constraints for examples:
- Provide examples.compliant with expected_outcome=assertion_pass unless documented_only is unavoidable.
- Provide examples.non_compliant with expected_outcome in {compile_fail,runtime_panic,lint_trigger} unless documented_only is unavoidable.
- examples.compliant.markdown and examples.non_compliant.markdown must contain at least one fenced Rust code block.
- Compliant markdown should include assertions when expected_outcome=assertion_pass.
- If expected_outcome=documented_only for either side, include verification_notes.

Output:
Return ONLY one JSON object with exactly these keys:
- rule_statement (string)
- amplification (string)
- exceptions (string)
- rationale (string)
- citation_plan (array of strings, prefer :cite:`...` and :std:`...` markers)
- uniqueness_rationale (string)
- confidence (low|medium|high)
- examples (object, optional):
  - compliant (object, optional): explanation, expected_outcome, verification_notes, markdown
  - non_compliant (object, optional): explanation, expected_outcome, verification_notes, markdown

No markdown outside JSON. No extra top-level keys.
PROMPT
)"

export CONTROLLER_DECISION_COMMAND="opencode run --dir {repo_root} --model openai/gpt-5.3-codex \"$DECISION_PROMPT\""
export CONTROLLER_REWRITE_COMMAND="opencode run --dir {repo_root} --model openai/gpt-5.3-codex \"$REWRITE_PROMPT\""

uv run python scripts/controller_supervisor.py \
  --session-id loop20-opencode-live-post-remediation-examples-01 \
  --max-loops 20 \
  --controller-arg=--decision-policy \
  --controller-arg=.cache/controller/decision_policy.loop20-post-remediation-examples.yaml \
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
