#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  glossary-parallel.sh --next <LETTERS...> [--attach <url>] [--discover] [--no-attach] [--finalize] [--root <dir>] [--repo <dir>] [--heartbeat <seconds>] [--dry-run]

Examples:
  glossary-parallel.sh --next N O P Q --attach http://localhost:4096 --finalize
  glossary-parallel.sh --next NOPQ --finalize

Flags:
  --next <LETTERS...>   Letters to process (space separated, or grouped, e.g. NOPQ)
  --attach <url>        Attach to a running opencode server (shared backend)
  --discover            Probe local servers if attach URL is unreachable
  --no-attach           Disable default shared backend and run separate backends
  --finalize            Run consolidation prompt after all letters succeed
  --root <dir>          Base directory for worktrees (default: parent of repo root)
  --repo <dir>          Repo root (default: git rev-parse --show-toplevel)
  --heartbeat <seconds> Heartbeat interval (default: 30)
  --dry-run             Print planned actions without executing
  --help                Show this help text
EOF
}

die() {
  printf 'error: %s\n' "$*" >&2
  exit 1
}

info() {
  printf '%s\n' "$*" >&2
}

is_letter() {
  [[ "$1" =~ ^[A-Z]$ ]]
}

build_auth_args() {
  auth_args=()
  if [[ -n "${OPENCODE_SERVER_PASSWORD:-}" ]]; then
    local user="${OPENCODE_SERVER_USERNAME:-opencode}"
    auth_args=(-u "${user}:${OPENCODE_SERVER_PASSWORD}")
  fi
}

server_health_ok() {
  local url="$1"
  command -v curl >/dev/null 2>&1 || return 1
  curl -fsS "${auth_args[@]}" "$url/global/health" >/dev/null 2>&1
}

server_project_matches() {
  local url="$1"
  command -v python3 >/dev/null 2>&1 || return 2
  command -v curl >/dev/null 2>&1 || return 2
  local json
  json="$(curl -fsS "${auth_args[@]}" "$url/project/current" 2>/dev/null || true)"
  [[ -n "$json" ]] || return 2
  python3 - "$json" "$repo_root" "$repo_root_real" <<'PY'
import json
import sys

raw = sys.argv[1]
repo_root = sys.argv[2]
repo_root_real = sys.argv[3]
targets = {repo_root, repo_root_real}

try:
    data = json.loads(raw)
except Exception:
    sys.exit(2)

def matches(value):
    if isinstance(value, dict):
        return any(matches(v) for v in value.values())
    if isinstance(value, list):
        return any(matches(v) for v in value)
    if isinstance(value, str):
        return value in targets
    return False

if matches(data):
    sys.exit(0)
sys.exit(1)
PY
}

discover_note=""
discover_server() {
  discover_note=""
  build_auth_args
  local found_any=0
  local port
  for port in $(seq 4096 4110); do
    local url="http://localhost:$port"
    if server_health_ok "$url"; then
      found_any=1
      if server_project_matches "$url"; then
        printf '%s\n' "$url"
        return 0
      fi
    fi
  done
  if [[ "$found_any" -eq 1 ]]; then
    discover_note="found servers but none matched repo"
  else
    discover_note="no servers detected"
  fi
  return 1
}

resolve_attach_url() {
  [[ -n "$attach_url" ]] || return 0
  if ! command -v curl >/dev/null 2>&1; then
    info "curl not found; skipping attach verification"
    return 0
  fi

  build_auth_args

  if ! server_health_ok "$attach_url"; then
    if [[ "$discover" -eq 1 ]]; then
      if discovered_url="$(discover_server)"; then
        attach_url="$discovered_url"
        attach_source="discovered"
        return 0
      else
        if [[ -n "$discover_note" ]]; then
          info "discover: $discover_note"
        fi
      fi
    fi

    if [[ "$attach_source" == "explicit" ]]; then
      die "attach url unreachable; use --discover or --no-attach"
    fi
    info "attach url unreachable; falling back to --no-attach"
    attach_url=""
    attach_source="none"
    return 0
  fi

  server_project_matches "$attach_url"
  local match_status=$?
  if [[ "$match_status" -eq 0 ]]; then
    return 0
  fi

  if [[ "$discover" -eq 1 ]]; then
    if discovered_url="$(discover_server)"; then
      attach_url="$discovered_url"
      attach_source="discovered"
      return 0
    else
      if [[ -n "$discover_note" ]]; then
        info "discover: $discover_note"
      fi
    fi
  fi

  if [[ "$attach_source" == "explicit" ]]; then
    if [[ "$match_status" -eq 1 ]]; then
      info "warning: attach url project does not match repo; proceeding anyway"
    else
      info "warning: could not verify attach server repo; proceeding anyway"
    fi
    return 0
  fi

  if [[ "$match_status" -eq 1 ]]; then
    info "attach url project does not match repo; falling back to --no-attach"
  else
    info "could not verify attach server repo; falling back to --no-attach"
  fi
  attach_url=""
  attach_source="none"
}

create_session() {
  local title="$1"
  command -v curl >/dev/null 2>&1 || return 1
  command -v python3 >/dev/null 2>&1 || return 1

  build_auth_args
  local payload
  payload="{\"title\":\"$title\"}"
  local json
  json="$(curl -fsS "${auth_args[@]}" -H "content-type: application/json" -d "$payload" "$attach_url/session" 2>/dev/null || true)"
  [[ -n "$json" ]] || return 1

  python3 - "$json" <<'PY'
import json
import sys

raw = sys.argv[1]
try:
    data = json.loads(raw)
except Exception:
    sys.exit(1)

for key in ("id", "sessionID", "sessionId"):
    if key in data and isinstance(data[key], str):
        print(data[key])
        sys.exit(0)

sys.exit(1)
PY
}

letters=()
attach_url=""
attach_source="none"
discover=0
no_attach=0
root_dir=""
repo_dir=""
dry_run=0
finalize=0
heartbeat_interval=30
auth_args=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --next)
      shift
      if [[ $# -eq 0 || "${1:-}" == --* ]]; then
        die "--next requires at least one letter"
      fi
      while [[ $# -gt 0 && "${1:-}" != --* ]]; do
        arg="${1//,/}"
        arg="${arg^^}"
        shift
        if [[ -z "$arg" ]]; then
          continue
        fi
        for ((i=0; i<${#arg}; i++)); do
          ch="${arg:i:1}"
          if [[ "$ch" =~ [A-Z] ]]; then
            letters+=("$ch")
          else
            die "invalid letter: $ch"
          fi
        done
      done
      ;;
    --attach)
      [[ $# -ge 2 ]] || die "--attach requires a url"
      attach_url="$2"
      attach_source="explicit"
      shift 2
      ;;
    --discover)
      discover=1
      shift
      ;;
    --no-attach)
      no_attach=1
      shift
      ;;
    --root)
      [[ $# -ge 2 ]] || die "--root requires a directory"
      root_dir="$2"
      shift 2
      ;;
    --repo)
      [[ $# -ge 2 ]] || die "--repo requires a directory"
      repo_dir="$2"
      shift 2
      ;;
    --heartbeat)
      [[ $# -ge 2 ]] || die "--heartbeat requires a number"
      heartbeat_interval="$2"
      shift 2
      ;;
    --dry-run)
      dry_run=1
      shift
      ;;
    --finalize)
      finalize=1
      shift
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      die "unknown flag: $1"
      ;;
  esac
done

[[ ${#letters[@]} -gt 0 ]] || die "no letters provided; use --next"

BASE_CONFIG_DIR="${OPENCODE_CONFIG_DIR:-}"
[[ -n "$BASE_CONFIG_DIR" ]] || die "OPENCODE_CONFIG_DIR is not set"
[[ -d "$BASE_CONFIG_DIR" ]] || die "OPENCODE_CONFIG_DIR does not exist: $BASE_CONFIG_DIR"

config_parent="$(dirname "$BASE_CONFIG_DIR")"

if [[ -n "$repo_dir" ]]; then
  repo_root="$repo_dir"
else
  repo_root="$(git -C "${PWD}" rev-parse --show-toplevel 2>/dev/null)" || die "not in a git repo; use --repo"
fi
repo_root_real="$repo_root"
if command -v realpath >/dev/null 2>&1; then
  repo_root_real="$(realpath "$repo_root")"
fi
permission_json="{\"external_directory\":{\"$config_parent/**\":\"allow\",\"$repo_root/**\":\"allow\",\"$repo_root_real/**\":\"allow\"}}"

if [[ -n "$root_dir" ]]; then
  worktree_base="$root_dir"
else
  worktree_base="$(dirname "$repo_root")"
fi

[[ -d "$worktree_base" ]] || die "worktree base does not exist: $worktree_base"

declare -A seen
deduped=()
for letter in "${letters[@]}"; do
  if ! is_letter "$letter"; then
    die "invalid letter: $letter"
  fi
  if [[ -n "${seen[$letter]+x}" ]]; then
    info "skipping duplicate letter: $letter"
    continue
  fi
  seen[$letter]=1
  deduped+=("$letter")
done
letters=("${deduped[@]}")

letters_joined=""
for letter in "${letters[@]}"; do
  letters_joined+="$letter"
done

if [[ ! "$heartbeat_interval" =~ ^[0-9]+$ ]]; then
  die "--heartbeat must be an integer"
fi

RUN_ID="$(date -u +%Y%m%d-%H%M%SZ)"

if [[ -n "$attach_url" && "$no_attach" -eq 1 ]]; then
  die "--attach and --no-attach cannot be used together"
fi

if [[ "$no_attach" -eq 1 ]]; then
  attach_url=""
  attach_source="disabled"
fi

if [[ -z "$attach_url" && "$no_attach" -eq 0 ]]; then
  if [[ -n "${OPENCODE_ATTACH_URL:-}" ]]; then
    attach_url="$OPENCODE_ATTACH_URL"
    attach_source="env"
  else
    attach_url="http://localhost:4096"
    attach_source="default"
  fi
fi

if [[ "$dry_run" -eq 1 ]]; then
  info "dry run: no changes will be made"
fi

if [[ "$dry_run" -eq 1 ]]; then
  for letter in "${letters[@]}"; do
    worktree_dir="$worktree_base/fls-glossary-$letter"
    info "would create/use worktree: $worktree_dir (branch glossary-$letter)"
    info "would run opencode for letter $letter in $worktree_dir"
  done
  if [[ "$finalize" -eq 1 ]]; then
    info "would run finalize in $repo_root"
  fi
  exit 0
fi

if [[ -n "$attach_url" ]]; then
  resolve_attach_url
fi

if [[ -n "$attach_url" ]]; then
  info "using --attach $attach_url ($attach_source)"
else
  info "using --no-attach; each opencode run will start its own backend"
fi

[[ -f "$BASE_CONFIG_DIR/plans/glossary-migration.md" ]] || die "missing plan: $BASE_CONFIG_DIR/plans/glossary-migration.md"
[[ -d "$BASE_CONFIG_DIR/reports/glossary-auto-generation" ]] || die "missing reports dir: $BASE_CONFIG_DIR/reports/glossary-auto-generation"

declare -A pids
declare -A log_files
declare -A exit_codes
declare -A session_ids

seed_letter_config() {
  local letter="$1"
  local letter_dir="$2"

  mkdir -p "$letter_dir/plans" "$letter_dir/reports" "$letter_dir/logs"
  if [[ ! -f "$letter_dir/plans/glossary-migration.md" ]]; then
    cp -a "$BASE_CONFIG_DIR/plans/glossary-migration.md" "$letter_dir/plans/"
  fi
  if [[ ! -d "$letter_dir/reports/glossary-auto-generation" ]]; then
    cp -a "$BASE_CONFIG_DIR/reports/glossary-auto-generation" "$letter_dir/reports/"
  fi
  if [[ -f "$BASE_CONFIG_DIR/reports/glossary-coverage-compare.md" && ! -f "$letter_dir/reports/glossary-coverage-compare.md" ]]; then
    cp -a "$BASE_CONFIG_DIR/reports/glossary-coverage-compare.md" "$letter_dir/reports/"
  fi
}

ensure_worktree() {
  local letter="$1"
  local worktree_dir="$2"
  local branch="glossary-$letter"

  if [[ -e "$worktree_dir" && ! -e "$worktree_dir/.git" ]]; then
    die "worktree path exists but is not a worktree: $worktree_dir"
  fi

  if [[ -e "$worktree_dir/.git" ]]; then
    return 0
  fi

  if git -C "$repo_root" show-ref --verify --quiet "refs/heads/$branch"; then
    git -C "$repo_root" worktree add "$worktree_dir" "$branch"
  else
    git -C "$repo_root" worktree add "$worktree_dir" -b "$branch"
  fi
}

build_letter_prompt() {
  local letter="$1"
  local letter_dir="$2"
  local repo_path="$3"

  cat <<EOF
Continue the FLS glossary migration.

Repo: $repo_path
OPENCODE_CONFIG_DIR: $letter_dir

Start by opening:
- $letter_dir/plans/glossary-migration.md
- $letter_dir/reports/glossary-auto-generation/migration-checklist.md
- $letter_dir/reports/glossary-auto-generation/$letter.md

Follow the plan exactly:
- Migrate terms into chapters (upgrade/add :dt: definitions)
- Update glossary-only-placement.md and the per-letter audit file
- Update migration-checklist.md
- Run ./make.py --check-generated-glossary
- Update glossary-coverage-compare.md
- Commit: docs(glossary): checkpoint $letter migration
EOF
}

build_finalize_prompt() {
  cat <<EOF
Finalize the parallel FLS glossary migration in the main repo.

Repo: $repo_root
OPENCODE_CONFIG_DIR: $BASE_CONFIG_DIR

Start by opening:
- $BASE_CONFIG_DIR/plans/glossary-migration.md
- $BASE_CONFIG_DIR/reports/glossary-auto-generation/migration-checklist.md

Then:
- Re-run ./make.py --check-generated-glossary
- Update glossary-coverage-compare.md
- Reconcile migration-checklist.md to reflect the merged repo state

If any per-letter updates diverge, align the shared reports to the repo contents.
EOF
}

heartbeat_log="$BASE_CONFIG_DIR/reports/parallel-heartbeat-$RUN_ID.log"

fetch_session_statuses() {
  local json
  local auth_args=()

  if [[ -n "${OPENCODE_SERVER_PASSWORD:-}" ]]; then
    local user="${OPENCODE_SERVER_USERNAME:-opencode}"
    auth_args=(-u "${user}:${OPENCODE_SERVER_PASSWORD}")
  fi

  json="$(curl -fsS "${auth_args[@]}" "$attach_url/session/status" 2>/dev/null || true)"
  if [[ -z "$json" ]]; then
    return 1
  fi

  python3 - "$json" <<'PY'
import json
import sys

raw = sys.argv[1]
try:
    data = json.loads(raw) if raw.strip() else {}
except Exception:
    sys.exit(1)

for sid, status in data.items():
    if isinstance(status, dict):
        for key in ("status", "state", "phase"):
            if key in status:
                print(f"{sid}\t{status[key]}")
                break
        else:
            print(f"{sid}\tunknown")
    else:
        print(f"{sid}\t{status}")
PY
}

finalize_status="skipped"
if [[ "$finalize" -eq 1 ]]; then
  finalize_status="pending"
fi

heartbeat_done=0
heartbeat() {
  while [[ "$heartbeat_done" -eq 0 ]]; do
    local ts
    ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    local -A server_status
    if [[ -n "$attach_url" ]] && command -v curl >/dev/null 2>&1 && command -v python3 >/dev/null 2>&1; then
      while IFS=$'\t' read -r sid status; do
        [[ -n "$sid" ]] || continue
        server_status["$sid"]="$status"
      done < <(fetch_session_statuses || true)
    fi

    {
      printf '[%s] Heartbeat (interval %ss)\n' "$ts" "$heartbeat_interval"
      printf 'Letters: '
      for letter in "${letters[@]}"; do
        local status="unknown"
        if [[ -n "${exit_codes[$letter]+x}" ]]; then
          if [[ "${exit_codes[$letter]}" -eq 0 ]]; then
            status="success"
          else
            status="failed"
          fi
        elif [[ -n "${pids[$letter]+x}" ]] && kill -0 "${pids[$letter]}" 2>/dev/null; then
          status="running"
        fi

        local sid="${session_ids[$letter]:-}"
        if [[ -n "$sid" && -n "${server_status[$sid]+x}" ]]; then
          status+=" (server:${server_status[$sid]})"
        fi
        printf '%s=%s ' "$letter" "$status"
      done
      printf '\n'
      if [[ -n "$attach_url" ]]; then
        printf 'Attach: %s (%s)\n' "$attach_url" "$attach_source"
      else
        printf 'Attach: none\n'
      fi
      printf 'Finalize: %s\n' "$finalize_status"
      printf "Browser: run 'opencode web' and open the URL it prints to view sessions.\n"
      printf 'Next check in %ss\n' "$heartbeat_interval"
      printf "\n"
    } | tee -a "$heartbeat_log" >/dev/null

    sleep "$heartbeat_interval"
  done
}

for letter in "${letters[@]}"; do
  worktree_dir="$worktree_base/fls-glossary-$letter"
  ensure_worktree "$letter" "$worktree_dir"

  letter_config_dir="$BASE_CONFIG_DIR/parallel/$letter"
  seed_letter_config "$letter" "$letter_config_dir"

  session_id=""
  if [[ -n "$attach_url" ]]; then
    session_id="$(create_session "glossary-$letter-$RUN_ID" || true)"
    if [[ -n "$session_id" ]]; then
      session_ids[$letter]="$session_id"
    else
      info "warning: failed to create session for $letter; running without --session"
    fi
  fi

  prompt="$(build_letter_prompt "$letter" "$letter_config_dir" "$worktree_dir")"
  log_file="$letter_config_dir/logs/opencode-$letter-$RUN_ID.log"
  log_files[$letter]="$log_file"

  if [[ -n "$attach_url" ]]; then
    (
      cd "$worktree_dir"
      if [[ -n "$session_id" ]]; then
        OPENCODE_CONFIG_DIR="$letter_config_dir" OPENCODE_PERMISSION="$permission_json" opencode run --session "$session_id" --attach "$attach_url" "$prompt"
      else
        OPENCODE_CONFIG_DIR="$letter_config_dir" OPENCODE_PERMISSION="$permission_json" opencode run --attach "$attach_url" "$prompt"
      fi
    ) >"$log_file" 2>&1 &
  else
    (
      cd "$worktree_dir"
      OPENCODE_CONFIG_DIR="$letter_config_dir" OPENCODE_PERMISSION="$permission_json" opencode run "$prompt"
    ) >"$log_file" 2>&1 &
  fi

  pids[$letter]=$!
done

heartbeat &
heartbeat_pid=$!

set +e
for letter in "${letters[@]}"; do
  wait "${pids[$letter]}"
  exit_codes[$letter]=$?
done
set -e

all_success=1
for letter in "${letters[@]}"; do
  if [[ "${exit_codes[$letter]}" -ne 0 ]]; then
    all_success=0
  fi
done

if [[ "$all_success" -ne 1 ]]; then
  report_dir="$BASE_CONFIG_DIR/reports/migration-$RUN_ID-$letters_joined"
  mkdir -p "$report_dir"
  report_file="$report_dir/failures.md"

  {
    printf '# Glossary migration failures\n\n'
    printf '- Timestamp (UTC): %s\n' "$RUN_ID"
    printf '- Letters: %s\n' "$letters_joined"
    printf '\n## Failures\n'
    for letter in "${letters[@]}"; do
      if [[ "${exit_codes[$letter]}" -ne 0 ]]; then
        printf '\n### %s\n' "$letter"
        printf '- Exit code: %s\n' "${exit_codes[$letter]}"
        printf '- Log: %s\n' "${log_files[$letter]}"
        printf '\nLog tail:\n\n```
'
        if [[ -f "${log_files[$letter]}" ]]; then
          tail -n 80 "${log_files[$letter]}"
        else
          printf 'Log file not found.\n'
        fi
        printf '\n```\n'
      fi
    done
  } >"$report_file"

  finalize_status="skipped"
else
  if [[ "$finalize" -eq 1 ]]; then
    finalize_status="running"
    finalize_log="$BASE_CONFIG_DIR/reports/finalize-$RUN_ID.log"
    finalize_prompt="$(build_finalize_prompt)"
    finalize_session=""
    if [[ -n "$attach_url" ]]; then
      finalize_session="$(create_session "glossary-finalize-$RUN_ID" || true)"
      if [[ -z "$finalize_session" ]]; then
        info "warning: failed to create finalize session; running without --session"
      fi
      (
        cd "$repo_root"
        if [[ -n "$finalize_session" ]]; then
          OPENCODE_CONFIG_DIR="$BASE_CONFIG_DIR" OPENCODE_PERMISSION="$permission_json" opencode run --session "$finalize_session" --attach "$attach_url" "$finalize_prompt"
        else
          OPENCODE_CONFIG_DIR="$BASE_CONFIG_DIR" OPENCODE_PERMISSION="$permission_json" opencode run --attach "$attach_url" "$finalize_prompt"
        fi
      ) >"$finalize_log" 2>&1 &
    else
      (
        cd "$repo_root"
        OPENCODE_CONFIG_DIR="$BASE_CONFIG_DIR" OPENCODE_PERMISSION="$permission_json" opencode run "$finalize_prompt"
      ) >"$finalize_log" 2>&1 &
    fi
    finalize_pid=$!
    set +e
    wait "$finalize_pid"
    finalize_exit=$?
    set -e
    if [[ "$finalize_exit" -eq 0 ]]; then
      finalize_status="done"
    else
      finalize_status="failed"
    fi
  else
    finalize_status="skipped"
  fi
fi

heartbeat_done=1
wait "$heartbeat_pid" 2>/dev/null || true

info "run complete: $letters_joined"
for letter in "${letters[@]}"; do
  if [[ "${exit_codes[$letter]}" -eq 0 ]]; then
    info "- $letter: success"
  else
    info "- $letter: failed (exit ${exit_codes[$letter]})"
  fi
done
info "finalize: $finalize_status"
if [[ "$all_success" -ne 1 ]]; then
  info "failure report: $report_file"
fi
