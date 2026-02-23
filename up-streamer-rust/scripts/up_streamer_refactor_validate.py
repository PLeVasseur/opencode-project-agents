#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


PHASE_NAMES = {
    3: "Phase 3 - Execution Waves",
    4: "Phase 4 - Test Refactor and Expansion",
    5: "Phase 5 - Rustdoc and Doctest Hardening",
    7: "Phase 7 - Full Validation and CI Parity",
}


@dataclass
class ValidationOutcome:
    phase_id: int
    phase_name: str
    passed: bool
    blockers: list[str]
    warnings: list[str]
    metrics: dict[str, Any]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Objective validator for up-streamer domain refactor phases"
    )
    parser.add_argument("--phase", type=int, required=True, choices=sorted(PHASE_NAMES.keys()))
    parser.add_argument(
        "--project-dir",
        type=Path,
        default=Path("/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust"),
    )
    parser.add_argument(
        "--reports-dir",
        type=Path,
        default=Path(
            "/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/up-streamer-domain-refactor"
        ),
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON only")
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def run_command(command: list[str], cwd: Path, timeout: int = 1800) -> tuple[int, str, str]:
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
        return 124, stdout, f"{stderr}\ncommand timed out after {timeout}s"


def strip_comments_and_blank_lines(lines: list[str]) -> list[str]:
    result: list[str] = []
    in_block = False

    for line in lines:
        i = 0
        n = len(line)
        out: list[str] = []
        in_string = False
        in_char = False
        escape = False

        while i < n:
            ch = line[i]
            nxt = line[i + 1] if i + 1 < n else ""

            if in_block:
                if ch == "*" and nxt == "/":
                    in_block = False
                    i += 2
                else:
                    i += 1
                continue

            if in_string:
                out.append(ch)
                if escape:
                    escape = False
                elif ch == "\\":
                    escape = True
                elif ch == '"':
                    in_string = False
                i += 1
                continue

            if in_char:
                out.append(ch)
                if escape:
                    escape = False
                elif ch == "\\":
                    escape = True
                elif ch == "'":
                    in_char = False
                i += 1
                continue

            if ch == "\"":
                in_string = True
                out.append(ch)
                i += 1
                continue

            if ch == "'":
                in_char = True
                out.append(ch)
                i += 1
                continue

            if ch == "/" and nxt == "/":
                break

            if ch == "/" and nxt == "*":
                in_block = True
                i += 2
                continue

            out.append(ch)
            i += 1

        stripped = "".join(out).strip()
        if stripped:
            result.append(stripped)

    return result


def code_line_count(path: Path) -> int:
    lines = read_text(path).splitlines()
    return len(strip_comments_and_blank_lines(lines))


def file_rustdoc_present(path: Path) -> bool:
    for line in read_text(path).splitlines():
        if line.startswith("//!") or line.startswith("///"):
            return True
    return False


def file_has_doctest(path: Path) -> bool:
    return "```" in read_text(path)


def count_tests_in_file(path: Path) -> int:
    text = read_text(path)
    return len(re.findall(r"#\[(?:tokio::)?test", text))


def test_function_lengths(path: Path) -> list[tuple[str, int]]:
    lines = read_text(path).splitlines()
    results: list[tuple[str, int]] = []

    i = 0
    while i < len(lines):
        line = lines[i]
        if "#[test" not in line and "#[tokio::test" not in line:
            i += 1
            continue

        j = i + 1
        fn_line = None
        while j < len(lines):
            if re.search(r"\bfn\s+[A-Za-z0-9_]+\s*\(", lines[j]):
                fn_line = j
                break
            j += 1

        if fn_line is None:
            i += 1
            continue

        fn_name_match = re.search(r"\bfn\s+([A-Za-z0-9_]+)\s*\(", lines[fn_line])
        fn_name = fn_name_match.group(1) if fn_name_match else f"unknown_{fn_line + 1}"

        brace_depth = 0
        started = False
        k = fn_line
        while k < len(lines):
            for ch in lines[k]:
                if ch == "{":
                    brace_depth += 1
                    started = True
                elif ch == "}":
                    brace_depth -= 1
            if started and brace_depth == 0:
                break
            k += 1

        snippet = lines[fn_line : min(k + 1, len(lines))]
        results.append((fn_name, len(strip_comments_and_blank_lines(snippet))))
        i = k + 1

    return results


def unresolved_tokens(report: Path, tokens: tuple[str, ...]) -> list[str]:
    if not report.exists():
        return [f"missing report: {report}"]
    text = read_text(report)
    hits = [token for token in tokens if token in text]
    return [f"unresolved token '{token}' in {report.name}" for token in hits]


def validate_phase_3(project_dir: Path) -> ValidationOutcome:
    blockers: list[str] = []
    warnings: list[str] = []

    src_root = project_dir / "up-streamer" / "src"
    ustreamer = src_root / "ustreamer.rs"
    api_endpoint = src_root / "api" / "endpoint.rs"
    api_streamer = src_root / "api" / "streamer.rs"

    for path in (ustreamer, api_endpoint, api_streamer):
        if not path.exists():
            blockers.append(f"missing required file: {path}")

    placeholders = []
    for path in src_root.rglob("*.rs"):
        if "Wave 1 scaffolding placeholder" in read_text(path):
            placeholders.append(path)
    if placeholders:
        blockers.append(
            "placeholder scaffolding remains: "
            + ", ".join(str(p.relative_to(project_dir)) for p in placeholders)
        )

    if ustreamer.exists():
        ustreamer_code = code_line_count(ustreamer)
        if ustreamer_code > 900:
            blockers.append(
                f"ustreamer.rs code line count {ustreamer_code} exceeds hard fail threshold 900"
            )
        elif ustreamer_code > 500:
            warnings.append(
                f"ustreamer.rs code line count {ustreamer_code} is above recommended target ~500"
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
        if api_file.exists() and code_line_count(api_file) < 20:
            blockers.append(
                f"{api_file.relative_to(project_dir)} appears stub-like ({code_line_count(api_file)} code lines)"
            )

    # File-scoping quality: any single source file above 900 code lines is a fail.
    oversized = []
    for path in src_root.rglob("*.rs"):
        loc = code_line_count(path)
        if loc > 900:
            oversized.append((path, loc))
        elif loc > 500:
            warnings.append(
                f"{path.relative_to(project_dir)} has {loc} code lines (recommend keeping closer to ~500 or below)"
            )
    if oversized:
        blockers.append(
            "oversized source files (>900 code lines): "
            + ", ".join(f"{p.relative_to(project_dir)}={n}" for p, n in oversized)
        )

    metrics = {
        "ustreamer_code_lines": code_line_count(ustreamer) if ustreamer.exists() else None,
        "placeholder_count": len(placeholders),
    }
    return ValidationOutcome(3, PHASE_NAMES[3], len(blockers) == 0, blockers, warnings, metrics)


def validate_phase_4(project_dir: Path, reports_dir: Path) -> ValidationOutcome:
    blockers: list[str] = []
    warnings: list[str] = []

    required_module_test_files = (
        project_dir / "up-streamer" / "src" / "control_plane" / "route_lifecycle.rs",
        project_dir / "up-streamer" / "src" / "control_plane" / "route_table.rs",
        project_dir / "up-streamer" / "src" / "routing" / "publish_resolution.rs",
        project_dir / "up-streamer" / "src" / "data_plane" / "ingress_registry.rs",
        project_dir / "up-streamer" / "src" / "data_plane" / "egress_pool.rs",
    )
    for path in required_module_test_files:
        if not path.exists():
            blockers.append(f"missing module test file: {path.relative_to(project_dir)}")
            continue
        if "#[cfg(test)]" not in read_text(path):
            blockers.append(f"missing #[cfg(test)] section in {path.relative_to(project_dir)}")

    api_contract_test = project_dir / "up-streamer" / "tests" / "api_contract_forwarding_rules.rs"
    if not api_contract_test.exists():
        blockers.append("missing API contract integration test: up-streamer/tests/api_contract_forwarding_rules.rs")

    ustreamer = project_dir / "up-streamer" / "src" / "ustreamer.rs"
    if ustreamer.exists():
        in_file_tests = count_tests_in_file(ustreamer)
        if in_file_tests > 12:
            blockers.append(
                f"ustreamer.rs still carries too many in-file tests ({in_file_tests}); move tests to domain modules/integration files"
            )

    # Readability heuristic: flag very long test functions.
    test_files = list((project_dir / "up-streamer" / "tests").glob("*.rs"))
    test_files += [
        project_dir / "up-streamer" / "src" / "control_plane" / "route_lifecycle.rs",
        project_dir / "up-streamer" / "src" / "control_plane" / "route_table.rs",
        project_dir / "up-streamer" / "src" / "routing" / "publish_resolution.rs",
        project_dir / "up-streamer" / "src" / "data_plane" / "ingress_registry.rs",
        project_dir / "up-streamer" / "src" / "data_plane" / "egress_pool.rs",
    ]
    overly_long: list[str] = []
    for file_path in test_files:
        if not file_path.exists():
            continue
        for fn_name, code_len in test_function_lengths(file_path):
            if code_len > 90:
                overly_long.append(f"{file_path.relative_to(project_dir)}::{fn_name} ({code_len} code lines)")
    if overly_long:
        blockers.append(
            "test readability issue (very long tests; extract helpers/fixtures): "
            + ", ".join(overly_long[:10])
        )

    # Reports should not contain placeholder relocation rows.
    test_matrix = reports_dir / "test-matrix.md"
    if test_matrix.exists() and "|  |  |  |  |" in read_text(test_matrix):
        blockers.append("test-matrix.md still contains placeholder relocation rows")

    behavior_owner = reports_dir / "behavior-owner-traceability.md"
    if behavior_owner.exists() and "|  |  |  |  |  |" in read_text(behavior_owner):
        blockers.append("behavior-owner-traceability.md still contains placeholder rows")

    code, _stdout, stderr = run_command(
        ["cargo", "test", "-p", "up-streamer", "--", "--nocapture"],
        project_dir,
        timeout=2400,
    )
    if code != 0:
        tail = "\n".join(stderr.strip().splitlines()[-20:])
        blockers.append(f"phase 4 required test command failed: cargo test -p up-streamer -- --nocapture\n{tail}")

    return ValidationOutcome(4, PHASE_NAMES[4], len(blockers) == 0, blockers, warnings, {})


def validate_phase_5(project_dir: Path) -> ValidationOutcome:
    blockers: list[str] = []
    warnings: list[str] = []

    src_root = project_dir / "up-streamer" / "src"
    layer_dirs = ("api", "control_plane", "routing", "data_plane", "runtime")

    for layer in layer_dirs:
        layer_path = src_root / layer
        if not layer_path.exists():
            blockers.append(f"missing layer directory: {layer_path.relative_to(project_dir)}")
            continue

        files = sorted(layer_path.glob("*.rs"))
        if not files:
            blockers.append(f"no rust files found in {layer_path.relative_to(project_dir)}")
            continue

        for file_path in files:
            if not file_rustdoc_present(file_path):
                blockers.append(f"missing rustdoc comments in {file_path.relative_to(project_dir)}")

        if not any(file_has_doctest(file_path) for file_path in files):
            blockers.append(f"missing doctest fence in layer {layer}")

    code, _stdout, stderr = run_command(
        ["cargo", "test", "-p", "up-streamer", "--doc"],
        project_dir,
        timeout=1800,
    )
    if code != 0:
        tail = "\n".join(stderr.strip().splitlines()[-20:])
        blockers.append(f"phase 5 required doctest command failed: cargo test -p up-streamer --doc\n{tail}")

    return ValidationOutcome(5, PHASE_NAMES[5], len(blockers) == 0, blockers, warnings, {})


def validate_phase_7(project_dir: Path, reports_dir: Path) -> ValidationOutcome:
    blockers: list[str] = []
    warnings: list[str] = []

    commands = [
        ["cargo", "build"],
        ["cargo", "fmt", "--", "--check"],
        ["cargo", "clippy", "--all-targets", "--", "-W", "warnings", "-D", "warnings"],
        ["cargo", "test", "-p", "up-streamer", "--", "--nocapture"],
        ["cargo", "test", "-p", "subscription-cache", "--", "--nocapture"],
        ["cargo", "test", "-p", "integration-test-utils", "--", "--nocapture"],
        ["cargo", "check", "--workspace", "--all-targets"],
        ["cargo", "test", "--workspace"],
    ]

    for command in commands:
        code, _stdout, stderr = run_command(command, project_dir, timeout=3600)
        if code != 0:
            tail = "\n".join(stderr.strip().splitlines()[-25:])
            blockers.append(f"command failed: {' '.join(command)}\n{tail}")
            break

    token_reports = (
        reports_dir / "api-surface-drift-report.md",
        reports_dir / "final-refactor-handoff.md",
        reports_dir / "behavior-conservation-matrix.md",
        reports_dir / "workspace-tracing-migration-status.md",
        reports_dir / "refactor-wave-plan.md",
        reports_dir / "wave-validation-log.md",
    )
    for report in token_reports:
        blockers.extend(unresolved_tokens(report, ("TBD", "pending", "uncommitted")))

    return ValidationOutcome(7, PHASE_NAMES[7], len(blockers) == 0, blockers, warnings, {})


def validate(phase_id: int, project_dir: Path, reports_dir: Path) -> ValidationOutcome:
    if phase_id == 3:
        return validate_phase_3(project_dir)
    if phase_id == 4:
        return validate_phase_4(project_dir, reports_dir)
    if phase_id == 5:
        return validate_phase_5(project_dir)
    if phase_id == 7:
        return validate_phase_7(project_dir, reports_dir)
    return ValidationOutcome(phase_id, PHASE_NAMES.get(phase_id, f"Phase {phase_id}"), True, [], [], {})


def main() -> int:
    args = parse_args()
    outcome = validate(args.phase, args.project_dir, args.reports_dir)

    if args.json:
        print(json.dumps(asdict(outcome)))
    else:
        print(f"{outcome.phase_name}: {'PASS' if outcome.passed else 'FAIL'}")
        for blocker in outcome.blockers:
            print(f"- blocker: {blocker}")
        for warning in outcome.warnings:
            print(f"- warning: {warning}")

    return 0 if outcome.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
