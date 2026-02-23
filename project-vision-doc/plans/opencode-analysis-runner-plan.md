# Plan: Provider-Agnostic Analysis Runners (Q + OpenCode)

## Goal
Make the analysis scripts runnable via OpenCode while preserving the existing `q` CLI behavior. Remove tool-call dependencies so outputs are written by the scripts, not the model.

## Assumptions
- Default runner remains `q` for backward compatibility.
- OpenCode integration uses `opencode run` (non-interactive) with optional `--attach` to a running server.
- Prompts will request plain markdown output; scripts write files directly.
- Q runtime validation will be done by a team member (not executed by me).

## Checklist Plan

### 1) Inventory + design adjustments
- [ ] Identify all `q` usage in scripts and docs (`scripts/question_asker.py`, `scripts/question_analyzer.py`, `README.md`).
- [ ] Define a small runner interface (`run(prompt, files?, model?, agent?, attach?) -> text`).
- [ ] Decide where to store the runner module (recommended: `scripts/llm_runner.py`).

### 2) Prompt and output flow changes
- [ ] Update prompts in both scripts to request markdown-only output (no tool calls).
- [ ] Remove `fs_write` instructions from `question_asker` prompts.
- [ ] Ensure the scripts save outputs to files after receiving the model response.

### 3) Add OpenCode runner
- [ ] Implement `opencode run` execution with optional `--model`, `--agent`, `--attach`.
- [ ] Support large prompts by writing a temp prompt file and passing `--file`.
- [ ] Parse `--format json` output to extract the final assistant response text.

### 4) Wire runner into scripts
- [ ] Add `--runner q|opencode` (default `q`) and optional `--model`, `--agent`, `--attach` flags.
- [ ] Route both scripts through the runner module.
- [ ] Preserve existing behavior and output paths.

### 5) Documentation updates
- [ ] Update `README.md` requirements to mention OpenCode as optional.
- [ ] Add usage examples for OpenCode (with `--attach` optional).

### 6) Validate locally (manual checks)
- [ ] Run a small sample with `--runner opencode` and verify output file matches expected format.
- [ ] Hand off to team member to validate `--runner q` output file creation.

## Commit Checkpoints
1) **Commit A**: Prompt/output refactor and runner interface added (no OpenCode yet).
   - Touches: `scripts/question_asker.py`, `scripts/question_analyzer.py`, `scripts/llm_runner.py`.
2) **Commit B**: OpenCode runner implementation and CLI flags wired.
   - Touches: `scripts/llm_runner.py`, `scripts/question_asker.py`, `scripts/question_analyzer.py`.
3) **Commit C**: Documentation updates.
   - Touches: `README.md`.

## Rollout Notes
- Keep `q` as default to avoid breaking existing workflows.
- OpenCode usage should be opt-in via `--runner opencode`.
- Avoid modifying existing output data; only alter scripts and docs.

## Open Questions (if any)
- None. Proceed with defaults above unless you want OpenCode to be default.
