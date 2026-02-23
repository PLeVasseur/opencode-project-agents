#!/usr/bin/env bash
set -u -o pipefail

REPO_ROOT="/home/pete.levasseur/project/fls"
REPORT_ROOT="/home/pete.levasseur/opencode-project-agents/fls/reports/system-abi-variadic-dedupe-base-integration-20260207T042229Z"
TS="20260207T042229Z"

DEDUPE_BRANCH="dedupe-paragraph-ids-mainline"
ANCHOR_SOURCE_BRANCH="changelog-assistant-upstream-pr-anchor"
ABI_SOURCE_BRANCH="system-abi-variadic"

ANCHOR_REBASED_BRANCH="changelog-assistant-upstream-pr-anchor-on-dedupe"
ABI_REBASED_BRANCH="system-abi-variadic-on-dedupe"
INTEGRATION_BRANCH="system-abi-variadic-anchor-integration-on-dedupe-${TS}"

ANCHOR_REBASED_WT="/home/pete.levasseur/project/fls-anchor-on-dedupe-${TS}"
ABI_REBASED_WT="/home/pete.levasseur/project/fls-system-abi-on-dedupe-${TS}"
INTEGRATION_WT="/home/pete.levasseur/project/fls-system-abi-anchor-integration-${TS}"

CANONICAL_UPSTREAM_PR="https://github.com/rust-lang/rust/pull/145954"
MISSING_UPSTREAM_PR="https://github.com/rust-lang/rust/pull/999999"
ENTRY_TITLE="Anchor replace validation (abi-on-dedupe integration)"

LEDGER="${REPORT_ROOT}/command-exit-codes.tsv"
: > "${LEDGER}"

run_cmd() {
    local label="$1"
    shift
    local cmd="$*"
    local stdout_file="${REPORT_ROOT}/${label}.stdout.txt"
    local stderr_file="${REPORT_ROOT}/${label}.stderr.txt"

    bash -lc "${cmd}" >"${stdout_file}" 2>"${stderr_file}"
    local ec=$?
    printf '%s\n' "${ec}" > "${REPORT_ROOT}/${label}.exitcode"
    printf '%s\t%s\t%s\n' "${label}" "${ec}" "${cmd}" >> "${LEDGER}"
    return "${ec}"
}

ec_of() {
    local label="$1"
    local path="${REPORT_ROOT}/${label}.exitcode"
    if [[ -f "${path}" ]]; then
        local ec
        read -r ec < "${path}"
        printf '%s' "${ec}"
    else
        printf 'missing'
    fi
}

status_zero() {
    local label="$1"
    if [[ "$(ec_of "${label}")" == "0" ]]; then
        printf 'PASS'
    else
        printf 'FAIL'
    fi
}

status_nonzero() {
    local label="$1"
    if [[ "$(ec_of "${label}")" != "0" ]]; then
        printf 'PASS'
    else
        printf 'FAIL'
    fi
}

extract_count() {
    local path="$1"
    local count=""
    if [[ -f "${path}" ]]; then
        while IFS= read -r line; do
            case "${line}" in
                count=*)
                    count="${line#count=}"
                    break
                    ;;
            esac
        done < "${path}"
    fi
    if [[ -z "${count}" ]]; then
        printf '0'
    else
        printf '%s' "${count}"
    fi
}

write_anchor_report() {
    local scan_label="$1"
    local destination="$2"
    local source="${REPORT_ROOT}/${scan_label}.stdout.txt"
    local count=0

    if [[ -s "${source}" ]]; then
        while IFS= read -r _line; do
            count=$((count + 1))
        done < "${source}"
    fi

    {
        printf 'url=%s\n' "${CANONICAL_UPSTREAM_PR}"
        printf 'count=%s\n' "${count}"
        printf 'lines:\n'
        if [[ -s "${source}" ]]; then
            while IFS= read -r line; do
                printf '%s\n' "${line}"
            done < "${source}"
        else
            printf '(none)\n'
        fi
    } > "${destination}"
}

find_branch_worktree() {
    local branch="$1"
    local current_worktree=""
    local found_worktree=""

    while IFS= read -r line; do
        case "${line}" in
            worktree\ *)
                current_worktree="${line#worktree }"
                ;;
            branch\ refs/heads/*)
                if [[ "${line#branch refs/heads/}" == "${branch}" ]]; then
                    found_worktree="${current_worktree}"
                fi
                ;;
        esac
    done < <(git -C "${REPO_ROOT}" worktree list --porcelain)

    printf '%s' "${found_worktree}"
}

run_cmd verify_project_parent "ls /home/pete.levasseur/project"

# Bootstrap checklist.
run_cmd bootstrap_printenv "printenv OPENCODE_CONFIG_DIR"
run_cmd bootstrap_fetch_origin "git -C \"${REPO_ROOT}\" fetch origin"
run_cmd bootstrap_uv_sync "uv sync --project \"${REPO_ROOT}\""

UTC_TIMESTAMP="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
CURRENT_BRANCH="$(git -C "${REPO_ROOT}" branch --show-current)"
HEAD_SHA="$(git -C "${REPO_ROOT}" rev-parse HEAD)"
ORIGIN_MAIN_SHA="$(git -C "${REPO_ROOT}" rev-parse origin/main)"
ORIGIN_DEDUPE_SHA="$(git -C "${REPO_ROOT}" rev-parse origin/${DEDUPE_BRANCH})"

{
    printf 'UTC_TIMESTAMP=%s\n' "${UTC_TIMESTAMP}"
    printf 'REPO_PATH=%s\n' "${REPO_ROOT}"
    printf 'CURRENT_BRANCH=%s\n' "${CURRENT_BRANCH}"
    printf 'HEAD_SHA=%s\n' "${HEAD_SHA}"
    printf 'ORIGIN_MAIN_SHA=%s\n' "${ORIGIN_MAIN_SHA}"
    printf 'ORIGIN_DEDUPE_SHA=%s\n' "${ORIGIN_DEDUPE_SHA}"
} > "${REPORT_ROOT}/bootstrap-metadata.txt"

# Step 1: Base branch prerequisites.
run_cmd step1_verify_local_dedupe "git -C \"${REPO_ROOT}\" show-ref --verify -- refs/heads/${DEDUPE_BRANCH}"
run_cmd step1_verify_remote_dedupe "git -C \"${REPO_ROOT}\" show-ref --verify -- refs/remotes/origin/${DEDUPE_BRANCH}"
run_cmd step1_dedupe_commit_reachable "git -C \"${REPO_ROOT}\" log ${DEDUPE_BRANCH} --grep='fix(paragraph-ids): deduplicate reused glossary IDs' --format='%H %s' -n 1"

LOCAL_DEDUPE_SHA="$(git -C "${REPO_ROOT}" rev-parse "${DEDUPE_BRANCH}")"
REMOTE_DEDUPE_SHA="$(git -C "${REPO_ROOT}" rev-parse "origin/${DEDUPE_BRANCH}")"

{
    printf 'local_branch=%s\n' "${DEDUPE_BRANCH}"
    printf 'local_sha=%s\n' "${LOCAL_DEDUPE_SHA}"
    printf 'remote_branch=origin/%s\n' "${DEDUPE_BRANCH}"
    printf 'remote_sha=%s\n' "${REMOTE_DEDUPE_SHA}"
} > "${REPORT_ROOT}/base-branch-shas.txt"

# Step 2: Assistant branch worktree and rebase.
run_cmd step2_anchor_branch_exists_check "git -C \"${REPO_ROOT}\" show-ref --verify --quiet refs/heads/${ANCHOR_REBASED_BRANCH}"

if [[ "$(ec_of step2_anchor_branch_exists_check)" == "0" ]]; then
    EXISTING_ANCHOR_WT="$(find_branch_worktree "${ANCHOR_REBASED_BRANCH}")"
    if [[ -n "${EXISTING_ANCHOR_WT}" ]]; then
        run_cmd step2_anchor_existing_status "git -C \"${EXISTING_ANCHOR_WT}\" status --porcelain"
        if [[ -s "${REPORT_ROOT}/step2_anchor_existing_status.stdout.txt" ]]; then
            ANCHOR_REBASED_BRANCH="${ANCHOR_REBASED_BRANCH}-${TS}"
            ANCHOR_REBASED_WT="/home/pete.levasseur/project/fls-anchor-on-dedupe-${TS}-fresh"
            run_cmd step2_anchor_worktree_add "git -C \"${REPO_ROOT}\" worktree add -b \"${ANCHOR_REBASED_BRANCH}\" \"${ANCHOR_REBASED_WT}\" \"${ANCHOR_SOURCE_BRANCH}\""
        else
            ANCHOR_REBASED_WT="${EXISTING_ANCHOR_WT}"
        fi
    else
        run_cmd step2_anchor_worktree_add_existing_branch "git -C \"${REPO_ROOT}\" worktree add \"${ANCHOR_REBASED_WT}\" \"${ANCHOR_REBASED_BRANCH}\""
    fi
else
    run_cmd step2_anchor_worktree_add "git -C \"${REPO_ROOT}\" worktree add -b \"${ANCHOR_REBASED_BRANCH}\" \"${ANCHOR_REBASED_WT}\" \"${ANCHOR_SOURCE_BRANCH}\""
fi

run_cmd step2_anchor_pre_sha "git -C \"${ANCHOR_REBASED_WT}\" rev-parse HEAD"
run_cmd step2_anchor_pre_base_main "git -C \"${ANCHOR_REBASED_WT}\" merge-base HEAD origin/main"
run_cmd step2_anchor_pre_divergence "git -C \"${ANCHOR_REBASED_WT}\" rev-list --left-right --count origin/main...HEAD"

read -r ANCHOR_PRE_SHA < "${REPORT_ROOT}/step2_anchor_pre_sha.stdout.txt"
read -r ANCHOR_PRE_BASE_MAIN < "${REPORT_ROOT}/step2_anchor_pre_base_main.stdout.txt"

run_cmd step2_anchor_rebase "git -C \"${ANCHOR_REBASED_WT}\" rebase --onto ${DEDUPE_BRANCH} ${ANCHOR_PRE_BASE_MAIN}"

run_cmd step2_anchor_post_sha "git -C \"${ANCHOR_REBASED_WT}\" rev-parse HEAD"
run_cmd step2_anchor_post_base_dedupe "git -C \"${ANCHOR_REBASED_WT}\" merge-base HEAD ${DEDUPE_BRANCH}"
run_cmd step2_anchor_post_divergence "git -C \"${ANCHOR_REBASED_WT}\" rev-list --left-right --count ${DEDUPE_BRANCH}...HEAD"
run_cmd step2_anchor_verify_ancestor "git -C \"${ANCHOR_REBASED_WT}\" merge-base --is-ancestor ${DEDUPE_BRANCH} HEAD"

read -r ANCHOR_POST_SHA < "${REPORT_ROOT}/step2_anchor_post_sha.stdout.txt"
read -r ANCHOR_POST_BASE_DEDUPE < "${REPORT_ROOT}/step2_anchor_post_base_dedupe.stdout.txt"

{
    printf 'branch=%s\n' "${ANCHOR_REBASED_BRANCH}"
    printf 'worktree=%s\n' "${ANCHOR_REBASED_WT}"
    printf 'pre_sha=%s\n' "${ANCHOR_PRE_SHA}"
    printf 'pre_base_main=%s\n' "${ANCHOR_PRE_BASE_MAIN}"
    printf 'pre_divergence=%s\n' "$(<"${REPORT_ROOT}/step2_anchor_pre_divergence.stdout.txt")"
    printf 'post_sha=%s\n' "${ANCHOR_POST_SHA}"
    printf 'post_base_dedupe=%s\n' "${ANCHOR_POST_BASE_DEDUPE}"
    printf 'post_divergence=%s\n' "$(<"${REPORT_ROOT}/step2_anchor_post_divergence.stdout.txt")"
    printf 'dedupe_ancestor_check=%s\n' "$(status_zero step2_anchor_verify_ancestor)"
} > "${REPORT_ROOT}/assistant-rebase-evidence.txt"

# Step 3: ABI branch worktree and rebase.
run_cmd step3_abi_branch_exists_check "git -C \"${REPO_ROOT}\" show-ref --verify --quiet refs/heads/${ABI_REBASED_BRANCH}"

if [[ "$(ec_of step3_abi_branch_exists_check)" == "0" ]]; then
    EXISTING_ABI_WT="$(find_branch_worktree "${ABI_REBASED_BRANCH}")"
    if [[ -n "${EXISTING_ABI_WT}" ]]; then
        run_cmd step3_abi_existing_status "git -C \"${EXISTING_ABI_WT}\" status --porcelain"
        if [[ -s "${REPORT_ROOT}/step3_abi_existing_status.stdout.txt" ]]; then
            ABI_REBASED_BRANCH="${ABI_REBASED_BRANCH}-${TS}"
            ABI_REBASED_WT="/home/pete.levasseur/project/fls-system-abi-on-dedupe-${TS}-fresh"
            run_cmd step3_abi_worktree_add "git -C \"${REPO_ROOT}\" worktree add -b \"${ABI_REBASED_BRANCH}\" \"${ABI_REBASED_WT}\" \"${ABI_SOURCE_BRANCH}\""
        else
            ABI_REBASED_WT="${EXISTING_ABI_WT}"
        fi
    else
        run_cmd step3_abi_worktree_add_existing_branch "git -C \"${REPO_ROOT}\" worktree add \"${ABI_REBASED_WT}\" \"${ABI_REBASED_BRANCH}\""
    fi
else
    run_cmd step3_abi_worktree_add "git -C \"${REPO_ROOT}\" worktree add -b \"${ABI_REBASED_BRANCH}\" \"${ABI_REBASED_WT}\" \"${ABI_SOURCE_BRANCH}\""
fi

run_cmd step3_abi_pre_sha "git -C \"${ABI_REBASED_WT}\" rev-parse HEAD"
run_cmd step3_abi_pre_base_main "git -C \"${ABI_REBASED_WT}\" merge-base HEAD origin/main"
run_cmd step3_abi_pre_divergence "git -C \"${ABI_REBASED_WT}\" rev-list --left-right --count origin/main...HEAD"

read -r ABI_PRE_SHA < "${REPORT_ROOT}/step3_abi_pre_sha.stdout.txt"
read -r ABI_PRE_BASE_MAIN < "${REPORT_ROOT}/step3_abi_pre_base_main.stdout.txt"

run_cmd step3_abi_rebase "git -C \"${ABI_REBASED_WT}\" rebase --onto ${DEDUPE_BRANCH} ${ABI_PRE_BASE_MAIN}"

run_cmd step3_abi_post_sha "git -C \"${ABI_REBASED_WT}\" rev-parse HEAD"
run_cmd step3_abi_post_base_dedupe "git -C \"${ABI_REBASED_WT}\" merge-base HEAD ${DEDUPE_BRANCH}"
run_cmd step3_abi_post_divergence "git -C \"${ABI_REBASED_WT}\" rev-list --left-right --count ${DEDUPE_BRANCH}...HEAD"
run_cmd step3_abi_verify_ancestor "git -C \"${ABI_REBASED_WT}\" merge-base --is-ancestor ${DEDUPE_BRANCH} HEAD"

read -r ABI_POST_SHA < "${REPORT_ROOT}/step3_abi_post_sha.stdout.txt"
read -r ABI_POST_BASE_DEDUPE < "${REPORT_ROOT}/step3_abi_post_base_dedupe.stdout.txt"

{
    printf 'branch=%s\n' "${ABI_REBASED_BRANCH}"
    printf 'worktree=%s\n' "${ABI_REBASED_WT}"
    printf 'pre_sha=%s\n' "${ABI_PRE_SHA}"
    printf 'pre_base_main=%s\n' "${ABI_PRE_BASE_MAIN}"
    printf 'pre_divergence=%s\n' "$(<"${REPORT_ROOT}/step3_abi_pre_divergence.stdout.txt")"
    printf 'post_sha=%s\n' "${ABI_POST_SHA}"
    printf 'post_base_dedupe=%s\n' "${ABI_POST_BASE_DEDUPE}"
    printf 'post_divergence=%s\n' "$(<"${REPORT_ROOT}/step3_abi_post_divergence.stdout.txt")"
    printf 'dedupe_ancestor_check=%s\n' "$(status_zero step3_abi_verify_ancestor)"
} > "${REPORT_ROOT}/abi-rebase-evidence.txt"

# Step 4: Integration branch setup and cherry-pick.
run_cmd step4_integration_worktree_add "git -C \"${REPO_ROOT}\" worktree add -b \"${INTEGRATION_BRANCH}\" \"${INTEGRATION_WT}\" \"${ABI_REBASED_BRANCH}\""
run_cmd step4_integration_base_sha "git -C \"${INTEGRATION_WT}\" rev-parse HEAD"
read -r INTEGRATION_BASE_SHA < "${REPORT_ROOT}/step4_integration_base_sha.stdout.txt"

run_cmd step4_assistant_commit_manifest "git -C \"${REPO_ROOT}\" log --reverse --format='%H %s' ${DEDUPE_BRANCH}..${ANCHOR_REBASED_BRANCH}"

FULL_MANIFEST="${REPORT_ROOT}/assistant-commit-manifest-full.txt"
: > "${FULL_MANIFEST}"
if [[ -f "${REPORT_ROOT}/step4_assistant_commit_manifest.stdout.txt" ]]; then
    while IFS= read -r line; do
        printf '%s\n' "${line}" >> "${FULL_MANIFEST}"
    done < "${REPORT_ROOT}/step4_assistant_commit_manifest.stdout.txt"
fi

run_cmd step4_intro_commit_lookup "git -C \"${REPO_ROOT}\" log --reverse --diff-filter=A --format='%H %s' ${DEDUPE_BRANCH}..${ANCHOR_REBASED_BRANCH} -- tools/changelog_assistant.py"
run_cmd step4_anchor_fix_lookup "git -C \"${REPO_ROOT}\" log --reverse --format='%H %s' ${DEDUPE_BRANCH}..${ANCHOR_REBASED_BRANCH} --grep='^fix(changelog-assistant): anchor updates to existing upstream PR entries$'"
run_cmd step4_assistant_ci_lookup "git -C \"${REPO_ROOT}\" log --reverse --format='%H %s' ${DEDUPE_BRANCH}..${ANCHOR_REBASED_BRANCH} --grep='^ci(changelog-assistant): run coverage checks in pull requests$'"

INTRO_SHA=""
ANCHOR_FIX_SHA=""
ASSISTANT_CI_SHA=""

if [[ -s "${REPORT_ROOT}/step4_intro_commit_lookup.stdout.txt" ]]; then
    while IFS= read -r line; do
        INTRO_SHA="${line%% *}"
        break
    done < "${REPORT_ROOT}/step4_intro_commit_lookup.stdout.txt"
fi

if [[ -s "${REPORT_ROOT}/step4_anchor_fix_lookup.stdout.txt" ]]; then
    while IFS= read -r line; do
        ANCHOR_FIX_SHA="${line%% *}"
        break
    done < "${REPORT_ROOT}/step4_anchor_fix_lookup.stdout.txt"
fi

if [[ -s "${REPORT_ROOT}/step4_assistant_ci_lookup.stdout.txt" ]]; then
    while IFS= read -r line; do
        ASSISTANT_CI_SHA="${line%% *}"
        break
    done < "${REPORT_ROOT}/step4_assistant_ci_lookup.stdout.txt"
fi

SELECTED_MANIFEST="${REPORT_ROOT}/assistant-commit-manifest-selected.txt"
: > "${SELECTED_MANIFEST}"

declare -a SELECTED_SHAS
IN_RANGE=0

if [[ -n "${INTRO_SHA}" && -n "${ASSISTANT_CI_SHA}" ]]; then
    while IFS= read -r line; do
        SHA="${line%% *}"
        SUBJECT="${line#* }"

        if [[ "${SHA}" == "${INTRO_SHA}" ]]; then
            IN_RANGE=1
        fi

        if [[ "${IN_RANGE}" == "1" ]]; then
            SELECTED_SHAS+=("${SHA}")
            printf '%s %s\n' "${SHA}" "${SUBJECT}" >> "${SELECTED_MANIFEST}"
        fi

        if [[ "${SHA}" == "${ASSISTANT_CI_SHA}" && "${IN_RANGE}" == "1" ]]; then
            break
        fi
    done < "${FULL_MANIFEST}"
fi

HAS_INTRO=0
HAS_ANCHOR_FIX=0
HAS_ASSISTANT_CI=0

for SHA in "${SELECTED_SHAS[@]:-}"; do
    if [[ "${SHA}" == "${INTRO_SHA}" ]]; then
        HAS_INTRO=1
    fi
    if [[ "${SHA}" == "${ANCHOR_FIX_SHA}" ]]; then
        HAS_ANCHOR_FIX=1
    fi
    if [[ "${SHA}" == "${ASSISTANT_CI_SHA}" ]]; then
        HAS_ASSISTANT_CI=1
    fi
done

{
    printf 'intro_sha=%s\n' "${INTRO_SHA}"
    printf 'anchor_fix_sha=%s\n' "${ANCHOR_FIX_SHA}"
    printf 'assistant_ci_sha=%s\n' "${ASSISTANT_CI_SHA}"
    printf 'selected_count=%s\n' "${#SELECTED_SHAS[@]}"
    if [[ "${#SELECTED_SHAS[@]}" -gt 3 ]]; then
        printf 'rationale=Included intermediate prerequisite assistant commits to preserve test/CI context and reduce cherry-pick conflicts.\n'
    else
        printf 'rationale=Selected only required assistant commits.\n'
    fi
} > "${REPORT_ROOT}/assistant-commit-selection-rationale.txt"

STACK_MANIFEST="${REPORT_ROOT}/integration-stack-manifest.txt"
: > "${STACK_MANIFEST}"
printf 'old_sha\tnew_sha\tsubject\n' >> "${STACK_MANIFEST}"

CHERRY_PICK_FAILED=0
INDEX=1

for OLD_SHA in "${SELECTED_SHAS[@]:-}"; do
    LABEL=$(printf 'step4_cherry_pick_%02d' "${INDEX}")
    run_cmd "${LABEL}" "git -C \"${INTEGRATION_WT}\" cherry-pick ${OLD_SHA}"
    CHERRY_EC="$(ec_of "${LABEL}")"

    if [[ "${CHERRY_EC}" == "0" ]]; then
        run_cmd "${LABEL}_new_sha" "git -C \"${INTEGRATION_WT}\" rev-parse HEAD"
        read -r NEW_SHA < "${REPORT_ROOT}/${LABEL}_new_sha.stdout.txt"
        SUBJECT="$(git -C "${INTEGRATION_WT}" show -s --format=%s "${NEW_SHA}")"
        printf '%s\t%s\t%s\n' "${OLD_SHA}" "${NEW_SHA}" "${SUBJECT}" >> "${STACK_MANIFEST}"
    else
        CHERRY_PICK_FAILED=1
        {
            printf 'cherry-pick failed for old_sha=%s\n' "${OLD_SHA}"
            printf 'label=%s\n' "${LABEL}"
            printf 'exit_code=%s\n' "${CHERRY_EC}"
        } >> "${REPORT_ROOT}/cherry-pick-conflicts.txt"

        run_cmd "${LABEL}_status" "git -C \"${INTEGRATION_WT}\" status --short"
        run_cmd "${LABEL}_conflicts" "git -C \"${INTEGRATION_WT}\" diff --name-only --diff-filter=U"

        {
            printf '\nstatus:\n'
            while IFS= read -r line; do
                printf '%s\n' "${line}"
            done < "${REPORT_ROOT}/${LABEL}_status.stdout.txt"
            printf '\nconflicted_files:\n'
            while IFS= read -r line; do
                printf '%s\n' "${line}"
            done < "${REPORT_ROOT}/${LABEL}_conflicts.stdout.txt"
        } >> "${REPORT_ROOT}/cherry-pick-conflicts.txt"

        run_cmd "${LABEL}_abort" "git -C \"${INTEGRATION_WT}\" cherry-pick --abort"
        break
    fi

    INDEX=$((INDEX + 1))
done

run_cmd step4_integration_head_sha "git -C \"${INTEGRATION_WT}\" rev-parse HEAD"
read -r INTEGRATION_HEAD_SHA < "${REPORT_ROOT}/step4_integration_head_sha.stdout.txt"

# Step 5: Readiness checks.
run_cmd step5_tool_exists "test -f \"${INTEGRATION_WT}/tools/changelog_assistant.py\""
run_cmd step5_help_output "uv run --project \"${INTEGRATION_WT}\" python \"${INTEGRATION_WT}/tools/changelog_assistant.py\" --help"
run_cmd step5_help_has_require_anchor "rg --fixed-strings -- '--require-anchor' \"${REPORT_ROOT}/step5_help_output.stdout.txt\""

run_cmd step5_field_update_action "rg -n --fixed-strings 'update_action' \"${INTEGRATION_WT}/tools/changelog_assistant.py\""
run_cmd step5_field_anchored_pr_url "rg -n --fixed-strings 'anchored_pr_url' \"${INTEGRATION_WT}/tools/changelog_assistant.py\""
run_cmd step5_field_anchored_entry_line "rg -n --fixed-strings 'anchored_entry_line' \"${INTEGRATION_WT}/tools/changelog_assistant.py\""
run_cmd step5_field_anchored_entry_index "rg -n --fixed-strings 'anchored_entry_index' \"${INTEGRATION_WT}/tools/changelog_assistant.py\""

run_cmd step5_py_compile "uv run --project \"${INTEGRATION_WT}\" python -m py_compile \"${INTEGRATION_WT}/tools/changelog_assistant.py\""

{
    printf 'tools/changelog_assistant.py exists: %s\n' "$(status_zero step5_tool_exists)"
    printf '--require-anchor in --help: %s\n' "$(status_zero step5_help_has_require_anchor)"
    printf 'metadata field update_action: %s\n' "$(status_zero step5_field_update_action)"
    printf 'metadata field anchored_pr_url: %s\n' "$(status_zero step5_field_anchored_pr_url)"
    printf 'metadata field anchored_entry_line: %s\n' "$(status_zero step5_field_anchored_entry_line)"
    printf 'metadata field anchored_entry_index: %s\n' "$(status_zero step5_field_anchored_entry_index)"
    printf 'py_compile: %s\n' "$(status_zero step5_py_compile)"
} > "${REPORT_ROOT}/readiness.txt"

# Step 6: Validation setup.
run_cmd step6_base_ref "git -C \"${INTEGRATION_WT}\" merge-base HEAD origin/main"
read -r BASE_REF < "${REPORT_ROOT}/step6_base_ref.stdout.txt"

run_cmd step6_release "uv run --project \"${INTEGRATION_WT}\" python -c \"import re,pathlib; text=pathlib.Path('${INTEGRATION_WT}/version.rst').read_text(encoding='utf-8'); m=re.search(r'\\|spec_version\\|\\s+replace::\\s+([0-9]+\\.[0-9]+\\.[0-9]+)', text); print(m.group(1) if m else '')\""
read -r RELEASE < "${REPORT_ROOT}/step6_release.stdout.txt"

{
    printf 'BASE_REF=%s\n' "${BASE_REF}"
    printf 'RELEASE=%s\n' "${RELEASE}"
    printf 'ENTRY_TITLE=%s\n' "${ENTRY_TITLE}"
    printf 'CANONICAL_UPSTREAM_PR=%s\n' "${CANONICAL_UPSTREAM_PR}"
    printf 'MISSING_UPSTREAM_PR=%s\n' "${MISSING_UPSTREAM_PR}"
} > "${REPORT_ROOT}/validation-setup.txt"

# Step 7: Verification flow.
run_cmd step7_anchor_before_scan "rg -n '^- .*<${CANONICAL_UPSTREAM_PR}>' \"${INTEGRATION_WT}/src/changelog.rst\""
write_anchor_report step7_anchor_before_scan "${REPORT_ROOT}/anchor-before.txt"

run_cmd step7_pre_check "uv run --project \"${INTEGRATION_WT}\" python \"${INTEGRATION_WT}/tools/changelog_assistant.py\" --check --base \"${BASE_REF}\" --emit-report \"${REPORT_ROOT}/pre-check\""
run_cmd step7_pre_check_artifacts "test -f \"${REPORT_ROOT}/pre-check.json\" && test -f \"${REPORT_ROOT}/pre-check.md\""

run_cmd step7_update_first "uv run --project \"${INTEGRATION_WT}\" python \"${INTEGRATION_WT}/tools/changelog_assistant.py\" --update --base \"${BASE_REF}\" --title \"${ENTRY_TITLE}\" --upstream-pr \"${CANONICAL_UPSTREAM_PR}\" --emit-report \"${REPORT_ROOT}/update\""
run_cmd step7_update_first_artifacts "test -f \"${REPORT_ROOT}/update.json\" && test -f \"${REPORT_ROOT}/update.md\""
run_cmd step7_update_first_metadata "uv run --project \"${INTEGRATION_WT}\" python -c \"import json; d=json.load(open('${REPORT_ROOT}/update.json')); print('update_action=' + str(d.get('update_action'))); print('anchored_pr_url=' + str(d.get('anchored_pr_url'))); print('anchored_entry_line=' + str(d.get('anchored_entry_line'))); print('anchored_entry_index=' + str(d.get('anchored_entry_index')));\""

run_cmd step7_diff_after_first "git -C \"${INTEGRATION_WT}\" diff -- src/changelog.rst"
: > "${REPORT_ROOT}/changelog-after-first.diff"
while IFS= read -r line; do
    printf '%s\n' "${line}" >> "${REPORT_ROOT}/changelog-after-first.diff"
done < "${REPORT_ROOT}/step7_diff_after_first.stdout.txt"

run_cmd step7_anchor_after_first_scan "rg -n '^- .*<${CANONICAL_UPSTREAM_PR}>' \"${INTEGRATION_WT}/src/changelog.rst\""
write_anchor_report step7_anchor_after_first_scan "${REPORT_ROOT}/anchor-after-first.txt"

run_cmd step7_update_second "uv run --project \"${INTEGRATION_WT}\" python \"${INTEGRATION_WT}/tools/changelog_assistant.py\" --update --base \"${BASE_REF}\" --title \"${ENTRY_TITLE}\" --upstream-pr \"${CANONICAL_UPSTREAM_PR}\" --emit-report \"${REPORT_ROOT}/update-second\""
run_cmd step7_update_second_artifacts "test -f \"${REPORT_ROOT}/update-second.json\" && test -f \"${REPORT_ROOT}/update-second.md\""

run_cmd step7_diff_after_second "git -C \"${INTEGRATION_WT}\" diff -- src/changelog.rst"
: > "${REPORT_ROOT}/changelog-after-second.diff"
while IFS= read -r line; do
    printf '%s\n' "${line}" >> "${REPORT_ROOT}/changelog-after-second.diff"
done < "${REPORT_ROOT}/step7_diff_after_second.stdout.txt"

run_cmd step7_anchor_after_second_scan "rg -n '^- .*<${CANONICAL_UPSTREAM_PR}>' \"${INTEGRATION_WT}/src/changelog.rst\""
write_anchor_report step7_anchor_after_second_scan "${REPORT_ROOT}/anchor-after-second.txt"

run_cmd step7_update_missing_default "uv run --project \"${INTEGRATION_WT}\" python \"${INTEGRATION_WT}/tools/changelog_assistant.py\" --update --base \"${BASE_REF}\" --title \"${ENTRY_TITLE}\" --upstream-pr \"${MISSING_UPSTREAM_PR}\" --emit-report \"${REPORT_ROOT}/update-missing-default\""
run_cmd step7_update_missing_default_artifacts "test -f \"${REPORT_ROOT}/update-missing-default.json\" && test -f \"${REPORT_ROOT}/update-missing-default.md\""
run_cmd step7_update_missing_default_metadata "uv run --project \"${INTEGRATION_WT}\" python -c \"import json; d=json.load(open('${REPORT_ROOT}/update-missing-default.json')); print('update_action=' + str(d.get('update_action')));\""

run_cmd step7_update_missing_strict "uv run --project \"${INTEGRATION_WT}\" python \"${INTEGRATION_WT}/tools/changelog_assistant.py\" --update --base \"${BASE_REF}\" --title \"${ENTRY_TITLE}\" --upstream-pr \"${MISSING_UPSTREAM_PR}\" --require-anchor --emit-report \"${REPORT_ROOT}/update-missing-strict\""
run_cmd step7_update_missing_strict_error_text "rg --fixed-strings -- 'anchor required but no matching entry was found' \"${REPORT_ROOT}/step7_update_missing_strict.stdout.txt\" \"${REPORT_ROOT}/step7_update_missing_strict.stderr.txt\""

run_cmd step7_post_check "uv run --project \"${INTEGRATION_WT}\" python \"${INTEGRATION_WT}/tools/changelog_assistant.py\" --check --base \"${BASE_REF}\" --emit-report \"${REPORT_ROOT}/post-check\""
run_cmd step7_post_check_artifacts "test -f \"${REPORT_ROOT}/post-check.json\" && test -f \"${REPORT_ROOT}/post-check.md\""

UPDATE_ACTION=""
ANCHORED_PR_URL=""
ANCHORED_ENTRY_LINE=""
ANCHORED_ENTRY_INDEX=""
MISSING_DEFAULT_ACTION=""

if [[ -f "${REPORT_ROOT}/update.json" ]]; then
    UPDATE_ACTION="$(uv run --project "${INTEGRATION_WT}" python -c "import json; d=json.load(open('${REPORT_ROOT}/update.json')); print(d.get('update_action'))")"
    ANCHORED_PR_URL="$(uv run --project "${INTEGRATION_WT}" python -c "import json; d=json.load(open('${REPORT_ROOT}/update.json')); print(d.get('anchored_pr_url'))")"
    ANCHORED_ENTRY_LINE="$(uv run --project "${INTEGRATION_WT}" python -c "import json; d=json.load(open('${REPORT_ROOT}/update.json')); print(d.get('anchored_entry_line'))")"
    ANCHORED_ENTRY_INDEX="$(uv run --project "${INTEGRATION_WT}" python -c "import json; d=json.load(open('${REPORT_ROOT}/update.json')); print(d.get('anchored_entry_index'))")"
fi

if [[ -f "${REPORT_ROOT}/update-missing-default.json" ]]; then
    MISSING_DEFAULT_ACTION="$(uv run --project "${INTEGRATION_WT}" python -c "import json; d=json.load(open('${REPORT_ROOT}/update-missing-default.json')); print(d.get('update_action'))")"
fi

ANCHOR_COUNT_BEFORE="$(extract_count "${REPORT_ROOT}/anchor-before.txt")"
ANCHOR_COUNT_AFTER_FIRST="$(extract_count "${REPORT_ROOT}/anchor-after-first.txt")"
ANCHOR_COUNT_AFTER_SECOND="$(extract_count "${REPORT_ROOT}/anchor-after-second.txt")"

ANCHOR_BRANCH_SHA="$(git -C "${ANCHOR_REBASED_WT}" rev-parse HEAD)"
ABI_BRANCH_SHA="$(git -C "${ABI_REBASED_WT}" rev-parse HEAD)"
INTEGRATION_BRANCH_SHA="$(git -C "${INTEGRATION_WT}" rev-parse HEAD)"

{
    printf 'ANCHOR_REBASED_BRANCH=%s\n' "${ANCHOR_REBASED_BRANCH}"
    printf 'ANCHOR_REBASED_SHA=%s\n' "${ANCHOR_BRANCH_SHA}"
    printf 'ANCHOR_REBASED_WT=%s\n' "${ANCHOR_REBASED_WT}"
    printf 'ABI_REBASED_BRANCH=%s\n' "${ABI_REBASED_BRANCH}"
    printf 'ABI_REBASED_SHA=%s\n' "${ABI_BRANCH_SHA}"
    printf 'ABI_REBASED_WT=%s\n' "${ABI_REBASED_WT}"
    printf 'INTEGRATION_BRANCH=%s\n' "${INTEGRATION_BRANCH}"
    printf 'INTEGRATION_SHA=%s\n' "${INTEGRATION_BRANCH_SHA}"
    printf 'INTEGRATION_WT=%s\n' "${INTEGRATION_WT}"
    printf 'BASE_REF=%s\n' "${BASE_REF}"
    printf 'RELEASE=%s\n' "${RELEASE}"
    printf 'CANONICAL_UPDATE_ACTION=%s\n' "${UPDATE_ACTION}"
    printf 'CANONICAL_ANCHORED_PR_URL=%s\n' "${ANCHORED_PR_URL}"
    printf 'CANONICAL_ANCHORED_ENTRY_LINE=%s\n' "${ANCHORED_ENTRY_LINE}"
    printf 'CANONICAL_ANCHORED_ENTRY_INDEX=%s\n' "${ANCHORED_ENTRY_INDEX}"
    printf 'MISSING_DEFAULT_ACTION=%s\n' "${MISSING_DEFAULT_ACTION}"
    printf 'ANCHOR_COUNT_BEFORE=%s\n' "${ANCHOR_COUNT_BEFORE}"
    printf 'ANCHOR_COUNT_AFTER_FIRST=%s\n' "${ANCHOR_COUNT_AFTER_FIRST}"
    printf 'ANCHOR_COUNT_AFTER_SECOND=%s\n' "${ANCHOR_COUNT_AFTER_SECOND}"
} > "${REPORT_ROOT}/branch-and-validation-values.env"

BOOTSTRAP_PRINTENV_STATUS="$(status_zero bootstrap_printenv)"
BOOTSTRAP_FETCH_STATUS="$(status_zero bootstrap_fetch_origin)"
BOOTSTRAP_UV_SYNC_STATUS="$(status_zero bootstrap_uv_sync)"

BASE_LOCAL_STATUS="$(status_zero step1_verify_local_dedupe)"
BASE_REMOTE_STATUS="$(status_zero step1_verify_remote_dedupe)"
BASE_COMMIT_STATUS="$(status_zero step1_dedupe_commit_reachable)"

STEP2_STATUS="FAIL"
if [[ "$(status_zero step2_anchor_worktree_add)" == "PASS" || "$(status_zero step2_anchor_worktree_add_existing_branch)" == "PASS" ]]; then
    if [[ "$(status_zero step2_anchor_rebase)" == "PASS" && "$(status_zero step2_anchor_verify_ancestor)" == "PASS" ]]; then
        STEP2_STATUS="PASS"
    fi
fi

STEP3_STATUS="FAIL"
if [[ "$(status_zero step3_abi_worktree_add)" == "PASS" || "$(status_zero step3_abi_worktree_add_existing_branch)" == "PASS" ]]; then
    if [[ "$(status_zero step3_abi_rebase)" == "PASS" && "$(status_zero step3_abi_verify_ancestor)" == "PASS" ]]; then
        STEP3_STATUS="PASS"
    fi
fi

REQUIRED_COMMITS_STATUS="FAIL"
if [[ -n "${INTRO_SHA}" && -n "${ANCHOR_FIX_SHA}" && -n "${ASSISTANT_CI_SHA}" && "${HAS_INTRO}" == "1" && "${HAS_ANCHOR_FIX}" == "1" && "${HAS_ASSISTANT_CI}" == "1" ]]; then
    REQUIRED_COMMITS_STATUS="PASS"
fi

CHERRY_PICK_STATUS="FAIL"
if [[ "${CHERRY_PICK_FAILED}" == "0" ]]; then
    CHERRY_PICK_STATUS="PASS"
fi

READINESS_STATUS="FAIL"
if [[ "$(status_zero step5_tool_exists)" == "PASS" && "$(status_zero step5_help_has_require_anchor)" == "PASS" && "$(status_zero step5_field_update_action)" == "PASS" && "$(status_zero step5_field_anchored_pr_url)" == "PASS" && "$(status_zero step5_field_anchored_entry_line)" == "PASS" && "$(status_zero step5_field_anchored_entry_index)" == "PASS" && "$(status_zero step5_py_compile)" == "PASS" ]]; then
    READINESS_STATUS="PASS"
fi

PRE_POST_STATUS="FAIL"
if [[ "$(status_zero step7_pre_check)" == "PASS" && "$(status_zero step7_post_check)" == "PASS" ]]; then
    PRE_POST_STATUS="PASS"
fi

CANONICAL_REPLACE_STATUS="FAIL"
if [[ "${UPDATE_ACTION}" == "replace" ]]; then
    CANONICAL_REPLACE_STATUS="PASS"
fi

CANONICAL_COUNT_STATUS="FAIL"
if [[ "${ANCHOR_COUNT_BEFORE}" == "1" && "${ANCHOR_COUNT_AFTER_FIRST}" == "1" && "${ANCHOR_COUNT_AFTER_SECOND}" == "1" ]]; then
    CANONICAL_COUNT_STATUS="PASS"
fi

MISSING_DEFAULT_STATUS="FAIL"
if [[ "$(status_zero step7_update_missing_default)" == "PASS" && "${MISSING_DEFAULT_ACTION}" == "append" ]]; then
    MISSING_DEFAULT_STATUS="PASS"
fi

MISSING_STRICT_STATUS="FAIL"
if [[ "$(status_nonzero step7_update_missing_strict)" == "PASS" && "$(status_zero step7_update_missing_strict_error_text)" == "PASS" ]]; then
    MISSING_STRICT_STATUS="PASS"
fi

ACCEPTANCE_1="FAIL"
if [[ "$(status_zero step2_anchor_verify_ancestor)" == "PASS" && "$(status_zero step3_abi_verify_ancestor)" == "PASS" ]]; then
    ACCEPTANCE_1="PASS"
fi

ACCEPTANCE_2="FAIL"
if [[ "${CHERRY_PICK_STATUS}" == "PASS" && "${REQUIRED_COMMITS_STATUS}" == "PASS" && "${INTEGRATION_BASE_SHA}" == "${ABI_POST_SHA}" ]]; then
    ACCEPTANCE_2="PASS"
fi

ACCEPTANCE_3="${CANONICAL_REPLACE_STATUS}"
ACCEPTANCE_4="${CANONICAL_COUNT_STATUS}"

ACCEPTANCE_5="FAIL"
if [[ "${MISSING_DEFAULT_STATUS}" == "PASS" && "${MISSING_STRICT_STATUS}" == "PASS" ]]; then
    ACCEPTANCE_5="PASS"
fi

ACCEPTANCE_6="FAIL"
if [[ "$(status_zero step7_pre_check_artifacts)" == "PASS" && "$(status_zero step7_update_first_artifacts)" == "PASS" && "$(status_zero step7_update_second_artifacts)" == "PASS" && "$(status_zero step7_post_check_artifacts)" == "PASS" && -f "${REPORT_ROOT}/summary.md" ]]; then
    ACCEPTANCE_6="PASS"
fi

REMEDIATION_NOTES=()
if [[ "${STEP2_STATUS}" == "FAIL" ]]; then
    REMEDIATION_NOTES+=("Recreate assistant derived branch/worktree and rerun rebase onto dedupe base.")
fi
if [[ "${STEP3_STATUS}" == "FAIL" ]]; then
    REMEDIATION_NOTES+=("Recreate ABI derived branch/worktree and rerun rebase onto dedupe base.")
fi
if [[ "${CHERRY_PICK_STATUS}" == "FAIL" ]]; then
    REMEDIATION_NOTES+=("Resolve cherry-pick conflicts in integration worktree and rebuild old->new SHA manifest.")
fi
if [[ "${READINESS_STATUS}" == "FAIL" ]]; then
    REMEDIATION_NOTES+=("Fix changelog assistant readiness issues (--require-anchor/help/metadata fields/py_compile).")
fi
if [[ "${CANONICAL_REPLACE_STATUS}" == "FAIL" ]]; then
    REMEDIATION_NOTES+=("Investigate canonical anchor matching so canonical URL updates report update_action=replace.")
fi
if [[ "${CANONICAL_COUNT_STATUS}" == "FAIL" ]]; then
    REMEDIATION_NOTES+=("Inspect changelog entry duplication/removal and enforce canonical top-level count of exactly 1.")
fi
if [[ "${MISSING_DEFAULT_STATUS}" == "FAIL" || "${MISSING_STRICT_STATUS}" == "FAIL" ]]; then
    REMEDIATION_NOTES+=("Fix missing-URL handling so default update appends and strict mode exits non-zero with anchor-miss message.")
fi
if [[ "${PRE_POST_STATUS}" == "FAIL" ]]; then
    REMEDIATION_NOTES+=("Address changelog coverage errors reported by pre-check/post-check outputs.")
fi

SUMMARY_PATH="${REPORT_ROOT}/summary.md"

{
    printf '# Integration Validation Summary\n\n'

    printf '## Report root\n\n'
    printf '- REPORT_ROOT: `%s`\n\n' "${REPORT_ROOT}"

    printf '## Bootstrap checklist\n\n'
    printf '- `printenv OPENCODE_CONFIG_DIR`: %s\n' "${BOOTSTRAP_PRINTENV_STATUS}"
    printf '- `git fetch origin`: %s\n' "${BOOTSTRAP_FETCH_STATUS}"
    printf '- `uv sync`: %s\n' "${BOOTSTRAP_UV_SYNC_STATUS}"
    printf '- Metadata recorded: %s\n\n' "PASS"

    printf '## Branch topology and SHAs\n\n'
    printf '- `%s`: `%s`\n' "${ANCHOR_REBASED_BRANCH}" "${ANCHOR_BRANCH_SHA}"
    printf '- `%s`: `%s`\n' "${ABI_REBASED_BRANCH}" "${ABI_BRANCH_SHA}"
    printf '- `%s`: `%s`\n' "${INTEGRATION_BRANCH}" "${INTEGRATION_BRANCH_SHA}"
    printf '- Integration base SHA (from ABI-on-dedupe): `%s`\n\n' "${INTEGRATION_BASE_SHA}"

    printf '## Rebase evidence\n\n'
    printf '- Assistant pre SHA: `%s`\n' "${ANCHOR_PRE_SHA}"
    printf '- Assistant post SHA: `%s`\n' "${ANCHOR_POST_SHA}"
    printf '- Assistant dedupe ancestor check: %s\n' "$(status_zero step2_anchor_verify_ancestor)"
    printf '- ABI pre SHA: `%s`\n' "${ABI_PRE_SHA}"
    printf '- ABI post SHA: `%s`\n' "${ABI_POST_SHA}"
    printf '- ABI dedupe ancestor check: %s\n\n' "$(status_zero step3_abi_verify_ancestor)"

    printf '## Cherry-pick manifest\n\n'
    printf '- Required commits resolved: %s\n' "${REQUIRED_COMMITS_STATUS}"
    printf '- Cherry-pick execution: %s\n' "${CHERRY_PICK_STATUS}"
    printf '- Manifest: `%s`\n\n' "${STACK_MANIFEST}"

    printf '## Readiness checks\n\n'
    printf '- Readiness status: %s\n' "${READINESS_STATUS}"
    printf '- Details: `%s`\n\n' "${REPORT_ROOT}/readiness.txt"

    printf '## Validation outcomes\n\n'
    printf '- Base ref used for all assistant invocations: `%s`\n' "${BASE_REF}"
    printf '- Canonical URL update action: `%s` (%s)\n' "${UPDATE_ACTION}" "${CANONICAL_REPLACE_STATUS}"
    printf '- Canonical anchor counts (before/after1/after2): `%s/%s/%s` (%s)\n' "${ANCHOR_COUNT_BEFORE}" "${ANCHOR_COUNT_AFTER_FIRST}" "${ANCHOR_COUNT_AFTER_SECOND}" "${CANONICAL_COUNT_STATUS}"
    printf '- Missing URL default action: `%s` (%s)\n' "${MISSING_DEFAULT_ACTION}" "${MISSING_DEFAULT_STATUS}"
    printf '- Missing URL strict mode non-zero: %s\n' "${MISSING_STRICT_STATUS}"
    printf '- Pre-check vs post-check: %s\n\n' "${PRE_POST_STATUS}"

    printf '## Command exit ledger\n\n'
    printf '- `%s`\n\n' "${LEDGER}"

    printf '## Acceptance criteria\n\n'
    printf '- Derived `*-on-dedupe` branches have dedupe as ancestor: %s\n' "${ACCEPTANCE_1}"
    printf '- Integration branch based on ABI-on-dedupe with selected assistant commits in order: %s\n' "${ACCEPTANCE_2}"
    printf '- Canonical URL update reports `update_action="replace"`: %s\n' "${ACCEPTANCE_3}"
    printf '- Canonical top-level count remains exactly `1` before/after/after-second: %s\n' "${ACCEPTANCE_4}"
    printf '- Missing URL behavior validated (`append` default, strict non-zero): %s\n' "${ACCEPTANCE_5}"
    printf '- Artifacts sufficient for fresh-session review: %s\n\n' "${ACCEPTANCE_6}"

    printf '## Remediation\n\n'
    if [[ "${#REMEDIATION_NOTES[@]}" -eq 0 ]]; then
        printf '- None required.\n'
    else
        for NOTE in "${REMEDIATION_NOTES[@]}"; do
            printf '- %s\n' "${NOTE}"
        done
    fi
} > "${SUMMARY_PATH}"

# Recompute acceptance criterion 6 after summary exists.
ACCEPTANCE_6="FAIL"
if [[ "$(status_zero step7_pre_check_artifacts)" == "PASS" && "$(status_zero step7_update_first_artifacts)" == "PASS" && "$(status_zero step7_update_second_artifacts)" == "PASS" && "$(status_zero step7_post_check_artifacts)" == "PASS" && -f "${REPORT_ROOT}/summary.md" ]]; then
    ACCEPTANCE_6="PASS"
fi

printf 'REPORT_ROOT=%s\n' "${REPORT_ROOT}"
printf 'ANCHOR_REBASED_BRANCH=%s\n' "${ANCHOR_REBASED_BRANCH}"
printf 'ANCHOR_REBASED_SHA=%s\n' "${ANCHOR_BRANCH_SHA}"
printf 'ABI_REBASED_BRANCH=%s\n' "${ABI_REBASED_BRANCH}"
printf 'ABI_REBASED_SHA=%s\n' "${ABI_BRANCH_SHA}"
printf 'INTEGRATION_BRANCH=%s\n' "${INTEGRATION_BRANCH}"
printf 'INTEGRATION_SHA=%s\n' "${INTEGRATION_BRANCH_SHA}"
printf 'INTEGRATION_WT=%s\n' "${INTEGRATION_WT}"
printf 'BASE_REF=%s\n' "${BASE_REF}"
printf 'CANONICAL_UPDATE_ACTION=%s\n' "${UPDATE_ACTION}"
printf 'MISSING_DEFAULT_ACTION=%s\n' "${MISSING_DEFAULT_ACTION}"
printf 'STRICT_EXIT_CODE=%s\n' "$(ec_of step7_update_missing_strict)"
printf 'PRE_CHECK_EXIT_CODE=%s\n' "$(ec_of step7_pre_check)"
printf 'POST_CHECK_EXIT_CODE=%s\n' "$(ec_of step7_post_check)"
printf 'SUMMARY_PATH=%s\n' "${SUMMARY_PATH}"
