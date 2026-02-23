#!/usr/bin/env bash

set -euo pipefail

CONFIG_DIR="${OPENCODE_CONFIG_DIR:-/home/pete.levasseur/opencode-project-agents/fls}"
REPO="/home/pete.levasseur/project/fls"
CHECKLIST="${CONFIG_DIR}/plans/glossary-migration-checklist.md"
VERIFY_HTML="${CONFIG_DIR}/verify-html-diff.py"
STATIC_GLOSSARY="${REPO}/src/glossary.static.rst.inc"
GENERATED_GLOSSARY="${REPO}/build/generated.glossary.rst"
LOG_DIR="${CONFIG_DIR}/reports/opencode-glossary-phase2"
EXTERNAL_ALLOW="${CONFIG_DIR}/**"
PERMISSION_JSON=$(printf '{"external_directory":{"%s":"allow"}}' "$EXTERNAL_ALLOW")

PROMPT=$(cat <<'EOF'
Continue glossary migration Phase 2 in /home/pete.levasseur/project/fls.

Follow /home/pete.levasseur/opencode-project-agents/fls/plans/glossary-migration-phase2.md exactly.
Use the next 20 unchecked terms from /home/pete.levasseur/opencode-project-agents/fls/plans/glossary-migration-checklist.md.
Only migrate terms present in src/glossary.static.rst.inc.
Use generate-glossary-entry.py for directives and /home/pete.levasseur/opencode-project-agents/fls/glossary-term-map.py for term-map updates.
Run ./generate-glossary.py, diff build/generated.glossary.rst against src/glossary.static.rst.inc, and run python3 /home/pete.levasseur/opencode-project-agents/fls/verify-html-diff.py.
Update the checklist and commit only repo files with Conventional Commits.
Never stage or commit anything under $OPENCODE_CONFIG_DIR.
EOF
)

die() {
  echo "error: $*" >&2
  exit 1
}

info() {
  echo "info: $*" >&2
}

unchecked_count() {
  local count
  count=$(grep -c '^- \[ \] ' "$CHECKLIST" || true)
  echo "$count"
}

require_clean_worktree() {
  if [[ -n "$(git -C "$REPO" status --porcelain)" ]]; then
    die "working tree not clean in ${REPO}"
  fi
}

command -v opencode >/dev/null 2>&1 || die "opencode not found in PATH"
[[ -d "$REPO/.git" ]] || die "repo not found at ${REPO}"
[[ -f "$CHECKLIST" ]] || die "checklist not found at ${CHECKLIST}"
[[ -f "$VERIFY_HTML" ]] || die "verify-html-diff.py not found at ${VERIFY_HTML}"

mkdir -p "$LOG_DIR"
cd "$REPO"

while true; do
  prev_unchecked=$(unchecked_count)
  if (( prev_unchecked == 0 )); then
    info "No unchecked terms remaining. Done."
    exit 0
  fi

  expected_delta=20
  if (( prev_unchecked < 20 )); then
    expected_delta=$prev_unchecked
  fi

  require_clean_worktree

  prev_head=$(git -C "$REPO" rev-parse HEAD)
  timestamp=$(date +"%Y%m%d-%H%M%S")
  log_file="${LOG_DIR}/run-${timestamp}.log"

  info "Starting opencode batch (unchecked: ${prev_unchecked}). Log: ${log_file}"
  if ! OPENCODE_CONFIG_DIR="$CONFIG_DIR" OPENCODE_PERMISSION="$PERMISSION_JSON" opencode run "$PROMPT" 2>&1 | tee "$log_file"; then
    die "opencode run failed. See ${log_file}"
  fi

  new_head=$(git -C "$REPO" rev-parse HEAD)
  if [[ "$new_head" == "$prev_head" ]]; then
    die "no new commit detected. See ${log_file}"
  fi

  if [[ -n "$(git -C "$REPO" status --porcelain)" ]]; then
    git -C "$REPO" status -sb >>"$log_file" 2>&1 || true
    die "working tree not clean after run. See ${log_file}"
  fi

  if ! diff -u "$GENERATED_GLOSSARY" "$STATIC_GLOSSARY" >>"$log_file" 2>&1; then
    die "generated glossary diff is non-empty. See ${log_file}"
  fi

  if ! python3 "$VERIFY_HTML" >>"$log_file" 2>&1; then
    die "HTML diff verification failed. See ${log_file}"
  fi

  new_unchecked=$(unchecked_count)
  actual_delta=$(( prev_unchecked - new_unchecked ))
  if (( actual_delta != expected_delta )); then
    die "checklist progress mismatch (expected -${expected_delta}, got -${actual_delta}). See ${log_file}"
  fi

  info "Batch complete (checked ${actual_delta} terms)."
done
