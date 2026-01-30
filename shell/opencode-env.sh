# OpenCode per-repo config hook (bash)

opencode_set_config() {
  local root repo config config_dir
  root="$(git rev-parse --show-toplevel 2>/dev/null)" || {
    unset OPENCODE_CONFIG
    return
  }
  repo="$(basename "$root")"
  config="$HOME/opencode-project-agents/$repo/opencode.jsonc"
  config_dir="$HOME/opencode-project-agents/$repo"
  if [ -f "$config" ]; then
    export OPENCODE_CONFIG="$config"
    if [ -d "$config_dir" ]; then
      export OPENCODE_CONFIG_DIR="$config_dir"
    else
      unset OPENCODE_CONFIG_DIR
    fi
  else
    unset OPENCODE_CONFIG
    unset OPENCODE_CONFIG_DIR
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
