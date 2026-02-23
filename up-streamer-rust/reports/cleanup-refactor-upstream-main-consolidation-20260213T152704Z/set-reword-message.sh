#!/usr/bin/env bash
set -euo pipefail

msg_file="$1"
current_subject=""
if IFS= read -r current_subject < "$msg_file"; then
  :
fi

case "$current_subject" in
  "chore: checkpoint domain modernization baseline")
    next_subject="refactor: modernize up-streamer domain architecture boundaries"
    ;;
  "chore: checkpoint usubscription decoupling prep state")
    next_subject="refactor: complete USubscription and route identity contract migration"
    ;;
  "refactor: add borrowed route APIs for ergonomic call sites")
    next_subject="perf+obs: optimize worker/runtime paths and structured tracing coverage"
    ;;
  "feat: add Criterion harness and guardrail CLI foundation")
    next_subject="feat(ci): add benchmark guardrail harness and advisory workflow"
    ;;
  "Add transport-smoke-suite orchestration foundation")
    next_subject="feat(smoke): add deterministic cross-transport smoke suite, claims, and matrix workflow"
    ;;
  "chore: align new-file copyright headers to 2026")
    next_subject="chore: align new-file copyright headers to 2026"
    ;;
  *)
    exit 0
    ;;
esac

printf '%s\n\n' "$next_subject" > "$msg_file"
