#!/usr/bin/env python3
"""Bootstrap durable run files for the Sphinx traceability migration plan.

This helper creates (or updates) a run root with M-stage durable keys,
checklist keys, and a run log entry so fresh-session execution starts from a
deterministic contract.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


TASK_NAME = "sphinx-traceability-migration"
PLAN_FILE = "plans/2026-02-15-sphinx-traceability-migration-plan.md"
TRACE_PLAN_FILE = "plans/2026-02-14-iso26262-traceability-anchor-plan.md"
CRITIQUE_PLAN_FILE = "plans/2026-02-14-critique-remediation-plan.md"


def parse_env(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    if not path.exists():
        return data

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith('"') and value.endswith('"') and len(value) >= 2:
            try:
                value = bytes(value[1:-1], "utf-8").decode("unicode_escape")
            except Exception:
                value = value[1:-1]
        data[key] = value

    return data


def write_env(path: Path, data: dict[str, str]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    lines = []
    for key in sorted(data.keys()):
        value = "" if data[key] is None else str(data[key])
        value = value.replace("\\", "\\\\").replace('"', '\\"')
        lines.append(f'{key}="{value}"')

    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    subprocess.run(["bash", "-n", str(tmp)], check=True)
    os.replace(tmp, path)


def _utc_now_id() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _git_value(repo_root: Path, args: list[str], fallback: str) -> str:
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=str(repo_root),
            check=True,
            capture_output=True,
            text=True,
        )
        value = completed.stdout.strip()
        return value or fallback
    except Exception:
        return fallback


def _ensure_file(src: Path, dst: Path) -> None:
    if dst.exists():
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def _bootstrap_state(
    state_path: Path,
    run_id: str,
    run_root: Path,
    repo_root: Path,
    base_branch: str,
    target_branch: str,
    base_pin_sha: str,
    expected_old_remote_sha: str,
    plan_path: Path,
    trace_plan_path: Path,
    critique_plan_path: Path,
) -> None:
    state = parse_env(state_path)

    for key in list(state.keys()):
        if key.startswith("S") and (key.endswith("_DONE") or key.endswith("_CHECKLIST_DONE")):
            state.pop(key, None)

    state["STATE_SCHEMA_VERSION"] = state.get("STATE_SCHEMA_VERSION", "1") or "1"

    state["RUN_ID"] = run_id
    state["TASK_NAME"] = TASK_NAME
    state["RUN_ROOT"] = str(run_root)
    state["REPO_ROOT"] = str(repo_root)
    state["TARGET_REMOTE"] = state.get("TARGET_REMOTE", "origin") or "origin"
    state["BASE_BRANCH"] = base_branch
    state["TARGET_BRANCH"] = target_branch
    state["BASE_PIN_SHA"] = base_pin_sha
    state["EXPECTED_OLD_REMOTE_SHA"] = expected_old_remote_sha
    state["PLAN_PATH"] = str(plan_path)
    state["REPORT_FILE"] = str(run_root / "artifacts" / "disposition" / "final-ledger.md")
    state["ARTIFACT_ROOT"] = str(run_root / "artifacts")
    state["LOCK_FILE"] = str(run_root / "run.lock")
    state["COMMIT_LEDGER_FILE"] = str(run_root / "artifacts" / "commits" / "commit-ledger.md")
    state["COMMIT_LEDGER_JSON_FILE"] = str(run_root / "artifacts" / "commits" / "commit-ledger.json")
    state["STARTED_AT_UTC"] = state.get("STARTED_AT_UTC", run_id) or run_id

    state["CURRENT_STAGE"] = "M0"
    state["LAST_COMPLETED_STAGE"] = state.get("LAST_COMPLETED_STAGE", "")
    state["STAGE_STATUS"] = "in_progress"
    state["LAST_GATE_RESULT"] = state.get("LAST_GATE_RESULT", "unknown")
    state["LAST_GATE_FAILURE_REASON"] = state.get("LAST_GATE_FAILURE_REASON", "")
    state["LAST_ARTIFACT_UPDATE_UTC"] = run_id
    state["LAST_RESUME_HINT"] = "Resume from M0"
    state["LAST_UPDATED_AT_UTC"] = run_id
    state["RESUME_TARGET_STAGE"] = "M0"

    state["TRACEABILITY_PLAN_PATH"] = str(trace_plan_path)
    state["CRITIQUE_PLAN_PATH"] = str(critique_plan_path)

    state["SOURCE_PDFSET_ID"] = state.get("SOURCE_PDFSET_ID", "")
    state["P06_SHA256"] = state.get("P06_SHA256", "")
    state["P08_SHA256"] = state.get("P08_SHA256", "")
    state["P09_SHA256"] = state.get("P09_SHA256", "")
    state["SPHINX_VERSION_PIN"] = state.get("SPHINX_VERSION_PIN", "")
    state["MYST_VERSION_PIN"] = state.get("MYST_VERSION_PIN", "")

    for idx in range(15):
        state[f"M{idx}_DONE"] = "0"
        state[f"M{idx}_CHECKLIST_DONE"] = "0"

    write_env(state_path, state)


def _bootstrap_checklist(checklist_path: Path) -> None:
    checklist = parse_env(checklist_path)

    for key in list(checklist.keys()):
        if key.startswith("CB_S"):
            checklist.pop(key, None)
    checklist["CHECKLIST_SCHEMA_VERSION"] = checklist.get("CHECKLIST_SCHEMA_VERSION", "1") or "1"
    checklist["CB_SCHEMA_SYNC"] = "1"

    for idx in range(15):
        checklist[f"CB_M{idx}_STAGE_START"] = "0"
        checklist[f"CB_M{idx}_STAGE_COMPLETE"] = "0"

    for key in (
        "CB_M2_PATH_CONTRACT_LOCKED",
        "CB_M3_NO_LEGACY_TOKENS",
        "CB_M6_SCHEMA_TRACE_MIGRATED",
        "CB_M6_TABLE_PRECEDENCE_GREEN",
        "CB_M8_LINT_STRICT_GREEN",
        "CB_M8_TRACEABLE_TABLE_USAGE_GREEN",
        "CB_M13_CLEAN_ROOM_VERIFY_GREEN",
    ):
        checklist[key] = checklist.get(key, "0") or "0"

    write_env(checklist_path, checklist)


def _append_run_log(run_log_path: Path, run_id: str, run_root: Path) -> None:
    ts = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    run_log_path.parent.mkdir(parents=True, exist_ok=True)
    with run_log_path.open("a", encoding="utf-8") as fh:
        fh.write(f"[{ts}] bootstrap RUN_ID={run_id} RUN_ROOT={run_root}\n")


def _write_bootstrap_artifacts(run_root: Path, run_id: str, state_path: Path, checklist_path: Path, base_branch: str, target_branch: str, base_pin_sha: str) -> None:
    created_at_utc = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    bootstrap_dir = run_root / "artifacts" / "bootstrap"
    bootstrap_dir.mkdir(parents=True, exist_ok=True)

    summary_path = bootstrap_dir / "run-bootstrap-summary.json"
    summary = {
        "run_id": run_id,
        "run_root": str(run_root),
        "state_file": str(state_path),
        "checklist_file": str(checklist_path),
        "created_at_utc": created_at_utc,
        "stage_schema": "M0..M14",
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lock_check_path = bootstrap_dir / "lock-contract-check.md"
    lock_check_path.write_text(
        "\n".join(
            [
                "# Lock Contract Check",
                "",
                f"- run_id: `{run_id}`",
                f"- lock_file: `{run_root / 'run.lock'}`",
                "- required fields: `pid`, `host`, `user`, `run_id`, `acquired_at_utc`",
                "- stale-lock policy: append stale contents to `run.log` before replacing lock",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    branch_contract_path = bootstrap_dir / "branch-contract.json"
    branch_contract = {
        "run_id": run_id,
        "base_branch": base_branch,
        "target_branch": target_branch,
        "base_pin_sha": base_pin_sha,
        "target_not_base": target_branch != base_branch,
    }
    branch_contract_path.write_text(
        json.dumps(branch_contract, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    commits_dir = run_root / "artifacts" / "commits"
    commits_dir.mkdir(parents=True, exist_ok=True)

    commit_ledger_md = commits_dir / "commit-ledger.md"
    if not commit_ledger_md.exists():
        commit_ledger_md.write_text(
            "\n".join(
                [
                    "# Commit Ledger",
                    "",
                    "- run_id: `%s`" % run_id,
                    "- base_branch: `%s`" % base_branch,
                    "- target_branch: `%s`" % target_branch,
                    "",
                    "| stage_checkpoint | commit_sha | subject | timestamp_utc |",
                    "| --- | --- | --- | --- |",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

    commit_ledger_json = commits_dir / "commit-ledger.json"
    if not commit_ledger_json.exists():
        commit_ledger_json.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "run_id": run_id,
                    "base_branch": base_branch,
                    "target_branch": target_branch,
                    "entries": [],
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Bootstrap durable migration run state")
    parser.add_argument("--repo-root", required=True)
    parser.add_argument("--run-id", default="")
    parser.add_argument("--base-branch", default="main")
    parser.add_argument("--target-branch", default="")
    parser.add_argument("--base-pin-sha", default="")
    parser.add_argument("--expected-old-remote-sha", default="UNKNOWN")
    args = parser.parse_args(argv)

    opencode_dir_raw = os.environ.get("OPENCODE_CONFIG_DIR", "").strip()
    if not opencode_dir_raw:
        print("error: OPENCODE_CONFIG_DIR is not set", file=sys.stderr)
        return 2

    opencode_dir = Path(opencode_dir_raw)
    repo_root = Path(args.repo_root).resolve()
    run_id = args.run_id or _utc_now_id()
    run_root = opencode_dir / "reports" / f"{TASK_NAME}-{run_id}"

    run_root.mkdir(parents=True, exist_ok=True)
    (run_root / "artifacts").mkdir(parents=True, exist_ok=True)

    run_state_template = opencode_dir / "skills" / "resumable-execution" / "run-state.template.env"
    checklist_template = opencode_dir / "skills" / "resumable-execution" / "checklist-state.template.env"

    state_path = run_root / "state.env"
    checklist_path = run_root / "checklist.state.env"
    run_log_path = run_root / "run.log"

    _ensure_file(run_state_template, state_path)
    _ensure_file(checklist_template, checklist_path)

    target_branch = args.target_branch or _git_value(repo_root, ["rev-parse", "--abbrev-ref", "HEAD"], "")
    base_pin_sha = args.base_pin_sha or _git_value(repo_root, ["rev-parse", "HEAD"], "")
    base_branch = args.base_branch or "main"

    if target_branch == base_branch:
        print(
            f"error: target branch must differ from base branch (base={base_branch}, target={target_branch})",
            file=sys.stderr,
        )
        return 2

    plan_path = opencode_dir / PLAN_FILE
    trace_plan_path = opencode_dir / TRACE_PLAN_FILE
    critique_plan_path = opencode_dir / CRITIQUE_PLAN_FILE

    _bootstrap_state(
        state_path=state_path,
        run_id=run_id,
        run_root=run_root,
        repo_root=repo_root,
        base_branch=base_branch,
        target_branch=target_branch,
        base_pin_sha=base_pin_sha,
        expected_old_remote_sha=args.expected_old_remote_sha,
        plan_path=plan_path,
        trace_plan_path=trace_plan_path,
        critique_plan_path=critique_plan_path,
    )
    _bootstrap_checklist(checklist_path)
    _append_run_log(run_log_path, run_id, run_root)
    _write_bootstrap_artifacts(
        run_root,
        run_id,
        state_path,
        checklist_path,
        base_branch,
        target_branch,
        base_pin_sha,
    )

    print(f"RUN_ID={run_id}")
    print(f"RUN_ROOT={run_root}")
    print(f"STATE_FILE={state_path}")
    print(f"CHECKLIST_FILE={checklist_path}")
    print(f"RUN_LOG={run_log_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
