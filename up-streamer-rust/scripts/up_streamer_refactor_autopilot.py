#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


STATUS_MARKER_RE = re.compile(r"AUTOPILOT_STATUS:\s*(\{.*\})")
STATUS_MARKER_BLOCK_RE = re.compile(r"AUTOPILOT_STATUS:\s*(\{[\s\S]*?\})")


@dataclass(frozen=True)
class PhaseSpec:
    phase_id: int
    phase_name: str
    gate_name: str
    focus: str
    report_files: tuple[str, ...]


@dataclass(frozen=True)
class ValidationResult:
    passed: bool
    blockers: tuple[str, ...]


def utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Segmented OpenCode autopilot for up-streamer refactor master plan"
    )
    parser.add_argument(
        "--project-dir",
        type=Path,
        default=Path("/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust"),
        help="Workspace project directory",
    )
    parser.add_argument(
        "--config-dir",
        type=Path,
        default=Path(os.environ.get("OPENCODE_CONFIG_DIR", str(Path.home() / ".config" / "opencode"))),
        help="OpenCode config directory (defaults to OPENCODE_CONFIG_DIR)",
    )
    parser.add_argument(
        "--start-phase",
        type=int,
        default=None,
        help="Start phase id (0-7). Defaults to state.next_phase.",
    )
    parser.add_argument(
        "--end-phase",
        type=int,
        default=7,
        help="Inclusive final phase id to run.",
    )
    parser.add_argument(
        "--max-attempts",
        type=int,
        default=3,
        help="Max attempts per phase (first try + retries).",
    )
    parser.add_argument(
        "--agent",
        default="build",
        help="OpenCode agent to use (default: build)",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Optional model override (provider/model)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without executing opencode run",
    )
    parser.add_argument(
        "--reset-state",
        action="store_true",
        help="Reset autopilot-state.json before running",
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Run local objective validators for selected phase range and exit",
    )
    parser.add_argument(
        "--validator-script",
        type=Path,
        default=None,
        help="Path to objective validator script (defaults to $OPENCODE_CONFIG_DIR/scripts/up_streamer_refactor_validate.py)",
    )
    return parser.parse_args()


def phase_specs() -> tuple[PhaseSpec, ...]:
    return (
        PhaseSpec(
            0,
            "Phase 0 - Bootstrap",
            "Gate 0",
            "bootstrap branch/workspace baseline inventory and behavior-conservation baseline",
            (
                "baseline-inventory.md",
                "behavior-conservation-matrix.md",
                "autopilot-state.json",
                "autopilot-run-log.md",
            ),
        ),
        PhaseSpec(
            1,
            "Phase 1 - Research and Domain Model Hardening",
            "Gate 1",
            "domain mapping, behavior catalog, async/tracing audits, consumer impact pre-assessment",
            (
                "domain-concept-mapping.md",
                "behavior-conservation-matrix.md",
                "async-runtime-audit.md",
                "tracing-migration-plan.md",
                "workspace-tracing-migration-status.md",
                "consumer-impact-analysis.md",
            ),
        ),
        PhaseSpec(
            2,
            "Phase 2 - Architecture Blueprint and Refactor Design",
            "Gate 2",
            "finalize architecture blueprint, decision gates, API drift strategy",
            (
                "architecture-blueprint.md",
                "api-surface-drift-report.md",
                "domain-concept-mapping.md",
            ),
        ),
        PhaseSpec(
            3,
            "Phase 3 - Execution Waves",
            "Gate 3",
            "execute implementation waves in strict order with per-wave validation",
            (
                "refactor-wave-plan.md",
                "wave-validation-log.md",
                "architecture-blueprint.md",
                "behavior-conservation-matrix.md",
            ),
        ),
        PhaseSpec(
            4,
            "Phase 4 - Test Refactor and Expansion",
            "Gate 4",
            "refactor and strengthen tests across unit/component/api/integration layers",
            (
                "test-matrix.md",
                "behavior-owner-traceability.md",
                "behavior-conservation-matrix.md",
                "wave-validation-log.md",
            ),
        ),
        PhaseSpec(
            5,
            "Phase 5 - Rustdoc and Doctest Hardening",
            "Gate 5",
            "deliver layer-specific rustdoc and doctest coverage",
            (
                "rustdoc-doctest-plan.md",
                "test-matrix.md",
                "wave-validation-log.md",
            ),
        ),
        PhaseSpec(
            6,
            "Phase 6 - Consumer Validation and As-Needed Adaptation",
            "Gate 6",
            "validate workspace consumers and apply minimal required updates",
            (
                "consumer-impact-analysis.md",
                "workspace-tracing-migration-status.md",
                "wave-validation-log.md",
            ),
        ),
        PhaseSpec(
            7,
            "Phase 7 - Full Validation and CI Parity",
            "Gate 7",
            "run full validation/parity and finalize handoff artifacts",
            (
                "behavior-conservation-matrix.md",
                "workspace-tracing-migration-status.md",
                "api-surface-drift-report.md",
                "final-refactor-handoff.md",
                "wave-validation-log.md",
            ),
        ),
    )


def ensure_exists(path: Path, label: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"{label} does not exist: {path}")


def load_json(path: Path) -> dict[str, Any]:
    ensure_exists(path, "state file")
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"invalid JSON in {path}: {exc}") from exc


def save_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n")


def fresh_state(project_dir: Path, plan_file: Path, reports_dir: Path) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "script": "up_streamer_refactor_autopilot.py",
        "status": "not-started",
        "started_at": None,
        "updated_at": None,
        "project_dir": str(project_dir),
        "plan_file": str(plan_file),
        "reports_dir": str(reports_dir),
        "last_completed_phase": None,
        "next_phase": 0,
        "phase_history": [],
        "stop_reason": None,
    }


def append_log(log_path: Path, text: str) -> None:
    with log_path.open("a", encoding="utf-8") as f:
        f.write(text)
        if not text.endswith("\n"):
            f.write("\n")


def build_permission_json(config_dir: Path) -> str:
    data: dict[str, Any] = {}
    raw = os.environ.get("OPENCODE_PERMISSION")
    if raw:
        try:
            parsed = json.loads(raw)
            if isinstance(parsed, dict):
                data = parsed
        except json.JSONDecodeError:
            # Fall back to a minimal safe override.
            data = {}

    external = data.get("external_directory")
    if not isinstance(external, dict):
        external = {}
    external[f"{config_dir}/**"] = "allow"
    data["external_directory"] = external

    return json.dumps(data)


def context_failure_detected(stdout: str, stderr: str) -> bool:
    haystack = (stdout + "\n" + stderr).lower()
    keywords = (
        "context window",
        "context length",
        "maximum context",
        "token limit",
        "too many tokens",
        "input is too long",
    )
    return any(k in haystack for k in keywords)


def run_command(
    command: list[str],
    cwd: Path,
    timeout: int = 1200,
) -> tuple[int, str, str]:
    try:
        proc = subprocess.run(
            command,
            cwd=cwd,
            text=True,
            capture_output=True,
            timeout=timeout,
        )
        return proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout if isinstance(exc.stdout, str) else ""
        stderr = exc.stderr if isinstance(exc.stderr, str) else ""
        timeout_msg = f"\ncommand timed out after {timeout}s"
        return 124, stdout, f"{stderr}{timeout_msg}"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def has_rustdoc(path: Path) -> bool:
    for line in read_text(path).splitlines():
        if line.startswith("//!") or line.startswith("///"):
            return True
    return False


def has_doctest(path: Path) -> bool:
    return "```" in read_text(path)


def code_line_count(path: Path) -> int:
    count = 0
    for line in read_text(path).splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("//") or s.startswith("/*") or s.startswith("*") or s.startswith("*/"):
            continue
        count += 1
    return count


def phase_objective_requirements(phase: PhaseSpec) -> tuple[str, ...]:
    if phase.phase_id == 3:
        return (
            "No scaffolding placeholders remain under up-streamer/src/**.",
            "`up-streamer/src/ustreamer.rs` trends toward ~500 code lines via extraction; hard fail threshold is >900 code lines.",
            "Legacy duplicate orchestration structs/types no longer exist in `ustreamer.rs`.",
            "`up-streamer/src/api/endpoint.rs` and `up-streamer/src/api/streamer.rs` contain real façade implementations (no placeholder stubs).",
        )
    if phase.phase_id == 5:
        return (
            "Every extracted module file in api/control_plane/routing/data_plane/runtime has rustdoc comments.",
            "Each layer (api/control_plane/routing/data_plane/runtime) has at least one doctest fence in that layer files.",
            "`cargo test -p up-streamer --doc` passes.",
        )
    if phase.phase_id == 7:
        return (
            "`cargo clippy --all-targets -- -W warnings -D warnings` passes.",
            "No unresolved placeholders (`TBD`, `pending`, `uncommitted`) remain in final gate artifacts.",
            "Final API drift and handoff reports are completed for Gate 7 sign-off.",
        )
    return tuple()


def validate_phase_outputs(phase: PhaseSpec, project_dir: Path, reports_dir: Path) -> ValidationResult:
    blockers: list[str] = []

    if phase.phase_id == 3:
        src_root = project_dir / "up-streamer" / "src"
        ustreamer = src_root / "ustreamer.rs"
        api_endpoint = src_root / "api" / "endpoint.rs"
        api_streamer = src_root / "api" / "streamer.rs"

        for path in (ustreamer, api_endpoint, api_streamer):
            if not path.exists():
                blockers.append(f"missing required file: {path}")

        if not blockers:
            placeholders = []
            for p in src_root.rglob("*.rs"):
                if "Wave 1 scaffolding placeholder" in read_text(p):
                    placeholders.append(p)
            if placeholders:
                blockers.append(
                    "placeholder scaffolding remains: "
                    + ", ".join(str(p.relative_to(project_dir)) for p in placeholders)
                )

            ustreamer_code = code_line_count(ustreamer)
            if ustreamer_code > 500:
                blockers.append(
                    f"ustreamer.rs code line count {ustreamer_code} exceeds hard cap 500"
                )

            legacy_markers = (
                "enum ForwardingListenerError",
                "struct TransportForwarders",
                "struct ForwardingListeners",
                "pub(crate) struct TransportForwarder",
                "pub(crate) struct ForwardingListener",
                "const FORWARDING_LISTENERS_TAG",
                "const TRANSPORT_FORWARDERS_TAG",
                "const FORWARDING_LISTENER_TAG",
                "const TRANSPORT_FORWARDER_TAG",
            )
            ustreamer_text = read_text(ustreamer)
            legacy_hits = [marker for marker in legacy_markers if marker in ustreamer_text]
            if legacy_hits:
                blockers.append(
                    "legacy duplicate orchestration definitions still in ustreamer.rs: "
                    + ", ".join(legacy_hits)
                )

            for api_file in (api_endpoint, api_streamer):
                api_code = code_line_count(api_file)
                if api_code < 12:
                    blockers.append(
                        f"{api_file.relative_to(project_dir)} appears stub-like ({api_code} code lines)"
                    )

    if phase.phase_id == 5:
        src_root = project_dir / "up-streamer" / "src"
        layer_dirs = (
            "api",
            "control_plane",
            "routing",
            "data_plane",
            "runtime",
        )
        for layer in layer_dirs:
            layer_path = src_root / layer
            if not layer_path.exists():
                blockers.append(f"missing layer directory: {layer_path}")
                continue

            rs_files = sorted(layer_path.glob("*.rs"))
            if not rs_files:
                blockers.append(f"no Rust files found in layer: {layer_path}")
                continue

            for file_path in rs_files:
                if not has_rustdoc(file_path):
                    blockers.append(
                        f"missing rustdoc comments in {file_path.relative_to(project_dir)}"
                    )

            if not any(has_doctest(file_path) for file_path in rs_files):
                blockers.append(f"missing doctest fence in layer {layer}")

        if not blockers:
            code, _stdout, stderr = run_command(
                ["cargo", "test", "-p", "up-streamer", "--doc"],
                project_dir,
                timeout=1800,
            )
            if code != 0:
                tail = "\n".join(stderr.strip().splitlines()[-20:])
                blockers.append(f"doctest command failed: cargo test -p up-streamer --doc\n{tail}")

    if phase.phase_id == 7:
        code, _stdout, stderr = run_command(
            ["cargo", "clippy", "--all-targets", "--", "-W", "warnings", "-D", "warnings"],
            project_dir,
            timeout=2400,
        )
        if code != 0:
            tail = "\n".join(stderr.strip().splitlines()[-25:])
            blockers.append(
                "clippy gate failed: cargo clippy --all-targets -- -W warnings -D warnings\n"
                + tail
            )

        report_files = (
            reports_dir / "api-surface-drift-report.md",
            reports_dir / "final-refactor-handoff.md",
            reports_dir / "behavior-conservation-matrix.md",
            reports_dir / "workspace-tracing-migration-status.md",
        )
        unresolved_tokens = ("TBD", "pending", "uncommitted")
        for report in report_files:
            if not report.exists():
                blockers.append(f"missing report required for gate 7: {report}")
                continue
            text = read_text(report)
            for token in unresolved_tokens:
                if token in text:
                    blockers.append(
                        f"unresolved token '{token}' remains in {report.relative_to(reports_dir.parent)}"
                    )
                    break

    return ValidationResult(passed=len(blockers) == 0, blockers=tuple(blockers))


def invoke_external_validator(
    validator_script: Path,
    phase_id: int,
    project_dir: Path,
    reports_dir: Path,
    dry_run: bool,
) -> ValidationResult:
    if phase_id not in (3, 4, 5, 7):
        return ValidationResult(passed=True, blockers=tuple())

    if dry_run:
        return ValidationResult(passed=True, blockers=tuple())

    command = [
        "python3",
        str(validator_script),
        "--phase",
        str(phase_id),
        "--project-dir",
        str(project_dir),
        "--reports-dir",
        str(reports_dir),
        "--json",
    ]
    code, stdout, stderr = run_command(command, project_dir, timeout=7200)

    payload = None
    for line in reversed(stdout.splitlines()):
        line = line.strip()
        if not line:
            continue
        try:
            parsed = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict) and "passed" in parsed:
            payload = parsed
            break

    if payload is None:
        details = "\n".join((stdout.strip(), stderr.strip())).strip()
        details = details or "(no validator output)"
        return ValidationResult(
            passed=False,
            blockers=(f"external validator did not return parseable JSON status. {details}",),
        )

    blockers = tuple(str(item) for item in payload.get("blockers", []))
    passed = bool(payload.get("passed", False)) and code == 0
    if code != 0 and not blockers:
        tail = "\n".join(stderr.strip().splitlines()[-20:]) if stderr.strip() else ""
        blockers = (
            f"external validator exited with code {code}. {tail}".strip(),
        )

    return ValidationResult(passed=passed, blockers=blockers)


def parse_status(stdout: str) -> tuple[dict[str, Any] | None, str | None, str]:
    session_id: str | None = None
    text_parts: list[str] = []

    for raw_line in stdout.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue

        if "sessionID" in event:
            session_id = event["sessionID"]

        if event.get("type") == "text":
            part = event.get("part", {})
            text = part.get("text", "")
            if text:
                text_parts.append(text)

    combined_text = "\n".join(text_parts)

    # Fast path: line-by-line status marker
    for part in text_parts:
        for line in part.splitlines():
            match = STATUS_MARKER_RE.search(line.strip())
            if not match:
                continue
            payload = match.group(1)
            try:
                return json.loads(payload), session_id, combined_text
            except json.JSONDecodeError:
                continue

    # Fallback: multiline JSON block
    block_match = STATUS_MARKER_BLOCK_RE.search(combined_text)
    if block_match:
        try:
            return json.loads(block_match.group(1)), session_id, combined_text
        except json.JSONDecodeError:
            pass

    return None, session_id, combined_text


def normalized_status(phase: PhaseSpec, status: dict[str, Any] | None) -> dict[str, Any]:
    if status is None:
        return {
            "phase": phase.phase_name,
            "gate": phase.gate_name,
            "gate_passed": False,
            "needs_human": True,
            "blockers": ["missing or malformed AUTOPILOT_STATUS marker"],
            "summary": "No machine-readable status marker found.",
            "next_actions": [
                "Retry phase with reduced context attachments",
                "If repeated, perform manual intervention and resume",
            ],
        }

    return {
        "phase": status.get("phase", phase.phase_name),
        "gate": status.get("gate", phase.gate_name),
        "gate_passed": bool(status.get("gate_passed", False)),
        "needs_human": bool(status.get("needs_human", False)),
        "blockers": status.get("blockers", []),
        "summary": status.get("summary", ""),
        "next_actions": status.get("next_actions", []),
    }


def build_prompt(
    phase: PhaseSpec,
    plan_file: Path,
    reports_dir: Path,
    attempt: int,
    max_attempts: int,
    reduced_context: bool,
    prior_blockers: tuple[str, ...],
) -> str:
    strictness = (
        "This is a retry due to missing/malformed status or context failure; keep output concise and prioritize emitting valid AUTOPILOT_STATUS."
        if reduced_context
        else ""
    )

    objective_lines = phase_objective_requirements(phase)
    objective_block = ""
    if objective_lines:
        objective_block = "\nObjective completion requirements (must be satisfied before gate_passed=true):\n"
        objective_block += "\n".join(f"- {line}" for line in objective_lines)

    blocker_block = ""
    if prior_blockers:
        blocker_block = "\nPrevious attempt blockers to resolve before declaring success:\n"
        blocker_block += "\n".join(f"- {b}" for b in prior_blockers)

    return (
        f"Execute ONLY {phase.phase_name} and {phase.gate_name} from the master plan at {plan_file}.\n"
        f"Do not execute work for later phases.\n"
        f"Focus: {phase.focus}.\n"
        f"Do not trust stale checkboxes blindly; re-evaluate this phase and correct checkboxes when earlier runs were inaccurate.\n"
        f"Update plan checkboxes continuously for completed items in this phase/gate.\n"
        f"Update relevant report artifacts under {reports_dir}.\n"
        f"{objective_block}{blocker_block}\n"
        f"If blocked, stop and set needs_human=true with concrete blockers.\n"
        f"Attempt {attempt}/{max_attempts}. {strictness}\n"
        "At the very end, output EXACTLY one status line in this format and valid JSON:\n"
        "AUTOPILOT_STATUS: {\"phase\":\"Phase X\",\"gate\":\"Gate X\",\"gate_passed\":true|false,\"needs_human\":true|false,\"blockers\":[],\"summary\":\"...\",\"next_actions\":[\"...\"]}\n"
        "Do not omit the marker line."
    )


def run_opencode(
    project_dir: Path,
    files: list[Path],
    prompt: str,
    agent: str,
    model: str | None,
    permission_json: str,
    dry_run: bool,
) -> tuple[int, str, str, list[str]]:
    cmd = ["opencode", "run", "--agent", agent, "--format", "json"]
    if model:
        cmd.extend(["--model", model])
    for file_path in files:
        cmd.extend(["--file", str(file_path)])
    cmd.append("--")
    cmd.append(prompt)

    if dry_run:
        return 0, "", "", cmd

    env = os.environ.copy()
    env["OPENCODE_PERMISSION"] = permission_json

    proc = subprocess.run(
        cmd,
        cwd=project_dir,
        text=True,
        capture_output=True,
        env=env,
    )
    return proc.returncode, proc.stdout, proc.stderr, cmd


def phase_files(
    phase: PhaseSpec,
    plan_file: Path,
    reports_dir: Path,
    reduced_context: bool,
) -> list[Path]:
    files: list[Path] = [
        plan_file,
        reports_dir / "autopilot-run-log.md",
        reports_dir / "autopilot-state.json",
    ]

    phase_paths = [reports_dir / rel for rel in phase.report_files]

    if reduced_context:
        # Keep context tight on retries.
        files.extend(phase_paths[:3])
    else:
        files.extend(phase_paths)

    # preserve order, unique
    deduped: list[Path] = []
    seen: set[Path] = set()
    for f in files:
        if f in seen:
            continue
        deduped.append(f)
        seen.add(f)
    return deduped


def log_attempt(
    log_path: Path,
    phase: PhaseSpec,
    attempt: int,
    max_attempts: int,
    files: list[Path],
    cmd: list[str],
    session_id: str | None,
    status: dict[str, Any],
    return_code: int,
    context_failure: bool,
    stderr_excerpt: str,
    local_validation: ValidationResult | None,
) -> None:
    attached = "\n".join(f"  - `{path}`" for path in files)
    status_json = json.dumps(status, indent=2)
    command_str = " ".join(cmd)
    local_validation_text = "(not-run)"
    if local_validation is not None:
        if local_validation.passed:
            local_validation_text = "passed"
        else:
            local_validation_text = "failed: " + "; ".join(local_validation.blockers)

    entry = f"""
### {utc_now()} - {phase.phase_name}

- Timestamp: {utc_now()}
- Phase: {phase.phase_name}
- Gate: {phase.gate_name}
- Opencode session id: `{session_id or 'unknown'}`
- Attempt: {attempt}/{max_attempts}
- Retries used: {attempt - 1}
- Return code: {return_code}
- Context failure detected: {context_failure}
- Local validator: {local_validation_text}
- Stderr excerpt:

```text
{stderr_excerpt}
```
- Attached files:
{attached}
- Command:

```text
{command_str}
```

Status:

```json
{status_json}
```

Outcome:

- [ ] proceed to next phase
- [ ] stop for human intervention

---

"""
    append_log(log_path, entry)


def main() -> int:
    args = parse_args()

    if args.max_attempts < 1:
        print("--max-attempts must be >= 1", file=sys.stderr)
        return 2

    config_dir = args.config_dir
    plan_file = config_dir / "plans" / "up-streamer-domain-refactor-master-plan.md"
    reports_dir = config_dir / "reports" / "up-streamer-domain-refactor"
    log_file = reports_dir / "autopilot-run-log.md"
    state_file = reports_dir / "autopilot-state.json"
    validator_script = args.validator_script or (config_dir / "scripts" / "up_streamer_refactor_validate.py")

    ensure_exists(args.project_dir, "project dir")
    ensure_exists(plan_file, "master plan")
    ensure_exists(reports_dir, "reports dir")
    ensure_exists(log_file, "autopilot run log")
    ensure_exists(state_file, "autopilot state")
    ensure_exists(validator_script, "validator script")

    state = fresh_state(args.project_dir, plan_file, reports_dir) if args.reset_state else load_json(state_file)
    if args.reset_state:
        save_json(state_file, state)
    phases = {p.phase_id: p for p in phase_specs()}
    permission_json = build_permission_json(config_dir)

    default_start = 3 if args.validate_only else state.get("next_phase", 0)
    start_phase = args.start_phase if args.start_phase is not None else default_start
    end_phase = args.end_phase

    if start_phase not in phases:
        print(f"invalid start phase: {start_phase}", file=sys.stderr)
        return 2
    if end_phase not in phases:
        print(f"invalid end phase: {end_phase}", file=sys.stderr)
        return 2
    if end_phase < start_phase:
        print("end phase must be >= start phase", file=sys.stderr)
        return 2

    if args.validate_only:
        all_passed = True
        for phase_id in range(start_phase, end_phase + 1):
            phase = phases[phase_id]
            result = invoke_external_validator(
                validator_script,
                phase.phase_id,
                args.project_dir,
                reports_dir,
                args.dry_run,
            )
            print(
                f"[validate] {phase.phase_name}: {'PASS' if result.passed else 'FAIL'} ({len(result.blockers)} blockers)"
            )
            for blocker in result.blockers:
                print(f"  - {blocker}")
            if not result.passed:
                all_passed = False
        return 0 if all_passed else 1

    state["status"] = "running"
    state["started_at"] = state.get("started_at") or utc_now()
    state["updated_at"] = utc_now()
    state["project_dir"] = str(args.project_dir)
    state["plan_file"] = str(plan_file)
    state["reports_dir"] = str(reports_dir)
    state["next_phase"] = start_phase
    state["stop_reason"] = None
    state.setdefault("phase_history", [])
    save_json(state_file, state)

    for phase_id in range(start_phase, end_phase + 1):
        phase = phases[phase_id]
        print(f"[autopilot] starting {phase.phase_name}")

        phase_success = False
        prior_blockers: tuple[str, ...] = tuple()
        for attempt in range(1, args.max_attempts + 1):
            reduced = attempt > 1
            files = phase_files(phase, plan_file, reports_dir, reduced)
            prompt = build_prompt(
                phase,
                plan_file,
                reports_dir,
                attempt,
                args.max_attempts,
                reduced,
                prior_blockers,
            )

            return_code, stdout, stderr, cmd = run_opencode(
                args.project_dir,
                files,
                prompt,
                args.agent,
                args.model,
                permission_json,
                args.dry_run,
            )

            raw_status, session_id, _combined_text = parse_status(stdout)
            marker_missing = raw_status is None
            status = normalized_status(phase, raw_status)
            context_failure = context_failure_detected(stdout, stderr)
            stderr_excerpt = "\n".join(stderr.strip().splitlines()[:20]) if stderr.strip() else "(none)"
            local_validation: ValidationResult | None = None

            if not marker_missing and status["gate_passed"] and not status["needs_human"]:
                local_validation = invoke_external_validator(
                    validator_script,
                    phase.phase_id,
                    args.project_dir,
                    reports_dir,
                    args.dry_run,
                )
                if not local_validation.passed:
                    status = {
                        "phase": phase.phase_name,
                        "gate": phase.gate_name,
                        "gate_passed": False,
                        "needs_human": True,
                        "blockers": list(local_validation.blockers),
                        "summary": "Objective local validator failed for this phase.",
                        "next_actions": [
                            "Resolve validator blockers and re-run this phase",
                            "Do not mark gate complete until validator passes",
                        ],
                    }

            log_attempt(
                log_file,
                phase,
                attempt,
                args.max_attempts,
                files,
                cmd,
                session_id,
                status,
                return_code,
                context_failure,
                stderr_excerpt,
                local_validation,
            )

            state["phase_history"].append(
                {
                    "timestamp": utc_now(),
                    "phase_id": phase.phase_id,
                    "phase_name": phase.phase_name,
                    "gate": phase.gate_name,
                    "attempt": attempt,
                    "max_attempts": args.max_attempts,
                    "session_id": session_id,
                    "return_code": return_code,
                    "context_failure_detected": context_failure,
                    "local_validation": (
                        {
                            "passed": local_validation.passed,
                            "blockers": list(local_validation.blockers),
                        }
                        if local_validation is not None
                        else None
                    ),
                    "status": status,
                }
            )
            state["updated_at"] = utc_now()
            save_json(state_file, state)

            if local_validation is not None and not local_validation.passed:
                prior_blockers = local_validation.blockers
                if attempt < args.max_attempts:
                    print(
                        f"[autopilot] {phase.phase_name}: objective validator failed on attempt {attempt}, retrying"
                    )
                    continue
                state["status"] = "stopped"
                state["stop_reason"] = (
                    f"{phase.phase_name} failed objective validator after {args.max_attempts} attempts"
                )
                state["updated_at"] = utc_now()
                save_json(state_file, state)
                print(f"[autopilot] stopped on {phase.phase_name}: {state['stop_reason']}")
                return 1

            if marker_missing:
                prior_blockers = ("missing or malformed AUTOPILOT_STATUS marker",)
                if attempt < args.max_attempts:
                    print(
                        f"[autopilot] {phase.phase_name}: missing status marker on attempt {attempt}, retrying with reduced context"
                    )
                    continue
                state["status"] = "stopped"
                state["stop_reason"] = (
                    f"{phase.phase_name} missing status marker after {args.max_attempts} attempts"
                )
                state["updated_at"] = utc_now()
                save_json(state_file, state)
                print(f"[autopilot] stopped on {phase.phase_name}: {state['stop_reason']}")
                return 1

            if status["gate_passed"] and not status["needs_human"]:
                phase_success = True
                state["last_completed_phase"] = phase.phase_id
                state["next_phase"] = phase.phase_id + 1
                state["updated_at"] = utc_now()
                save_json(state_file, state)
                print(f"[autopilot] completed {phase.phase_name}")
                break

            # Hard stop conditions from model.
            if status["needs_human"] or not status["gate_passed"]:
                state["status"] = "stopped"
                state["stop_reason"] = (
                    f"{phase.phase_name} reported gate failure or needs_human=true"
                )
                state["updated_at"] = utc_now()
                save_json(state_file, state)
                print(f"[autopilot] stopped on {phase.phase_name}: {state['stop_reason']}")
                return 1

        if not phase_success:
            state["status"] = "stopped"
            state["stop_reason"] = (
                f"{phase.phase_name} exhausted attempts without valid success marker"
            )
            state["updated_at"] = utc_now()
            save_json(state_file, state)
            print(f"[autopilot] stopped on {phase.phase_name}: {state['stop_reason']}")
            return 1

    state["status"] = "completed"
    state["updated_at"] = utc_now()
    state["stop_reason"] = None
    save_json(state_file, state)
    print("[autopilot] completed requested phase range")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
