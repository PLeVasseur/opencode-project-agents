# OpenCode per-repo config hook (bash)

opencode_set_config() {
  local root repo config config_dir
  root="$(git rev-parse --show-toplevel 2>/dev/null)" || {
    unset OPENCODE_CONFIG
    unset OPENCODE_CONFIG_DIR
    return
  }
  repo="$(basename "$root")"
  config_dir="$HOME/opencode-project-agents/$repo"
  config="$config_dir/opencode.jsonc"

  if command -v opencode-bootstrap >/dev/null 2>&1; then
    opencode-bootstrap
  fi

  if [ -d "$config_dir" ]; then
    export OPENCODE_CONFIG_DIR="$config_dir"
  else
    unset OPENCODE_CONFIG_DIR
  fi

  if [ -f "$config" ]; then
    export OPENCODE_CONFIG="$config"
  else
    unset OPENCODE_CONFIG
  fi
}

opencode_prompt_hook() {
  if [ "${OPENCODE_PWD_LAST:-}" = "$PWD" ]; then
    return
  fi
  OPENCODE_PWD_LAST="$PWD"
  opencode_set_config
}

case ";${PROMPT_COMMAND:-};" in
  *";opencode_prompt_hook;"*)
    ;;
  ";;")
    PROMPT_COMMAND="opencode_prompt_hook"
    ;;
  *)
    PROMPT_COMMAND="opencode_prompt_hook;${PROMPT_COMMAND}"
    ;;
esac

opencode_set_config
