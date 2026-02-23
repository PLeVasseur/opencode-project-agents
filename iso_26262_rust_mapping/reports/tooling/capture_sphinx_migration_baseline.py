#!/usr/bin/env python3
"""Capture M1 baseline artifacts for Sphinx migration runs."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import yaml


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


def _count_narrative(text: str) -> tuple[int, int, int]:
    lines = text.splitlines()
    heading_count = sum(1 for line in lines if re.match(r"^\s{0,3}#{1,6}\s+\S", line))
    list_item_count = sum(1 for line in lines if re.match(r"^\s*([-*+]\s+|\d+[.)]\s+)", line))

    blocks = [block.strip() for block in re.split(r"\n\s*\n", text) if block.strip()]
    paragraph_block_count = 0
    for block in blocks:
        first = block.splitlines()[0].strip()
        if first.startswith("#"):
            continue
        if first.startswith("{{TABLE:") or first == "{{PAGE_BREAK}}" or first == "{{BLANK}}":
            continue
        if re.match(r"^([-*+]|\d+[.)])\s+", first):
            continue
        paragraph_block_count += 1

    return heading_count, paragraph_block_count, list_item_count


def _collect_table_inventory(repo_root: Path) -> tuple[dict[str, int], list[dict[str, object]]]:
    tables_dir = repo_root / "src" / "tables"
    table_files = sorted(tables_dir.glob("table-*.yaml"))
    table_stats: list[dict[str, object]] = []

    total_rows = 0
    total_cell_entries = 0
    total_row_trace_units = 0
    total_cell_trace_units = 0

    for table_file in table_files:
        raw = table_file.read_text(encoding="utf-8")
        data = yaml.safe_load(raw) or {}
        columns = [
            col.get("key")
            for col in (data.get("columns") or [])
            if isinstance(col, dict) and col.get("key")
        ]
        rows = data.get("rows") or []

        row_count = len(rows) if isinstance(rows, list) else 0
        total_rows += row_count

        cell_entries = 0
        row_trace_units = 0
        cell_trace_units = 0

        if isinstance(rows, list):
            for row in rows:
                if not isinstance(row, dict):
                    continue
                if isinstance(row.get("_trace"), dict):
                    row_trace_units += 1
                cell_trace = row.get("cell_trace")
                if isinstance(cell_trace, dict):
                    cell_trace_units += len([k for k, v in cell_trace.items() if isinstance(v, dict)])

                for col in columns:
                    value = row.get(col)
                    if value is None:
                        continue
                    if isinstance(value, str) and value.strip() == "":
                        continue
                    cell_entries += 1

        total_cell_entries += cell_entries
        total_row_trace_units += row_trace_units
        total_cell_trace_units += cell_trace_units

        table_stats.append(
            {
                "table_file": str(table_file.relative_to(repo_root)),
                "table_id": data.get("id", table_file.stem),
                "column_count": len(columns),
                "row_count": row_count,
                "non_empty_cell_entries": cell_entries,
                "row_trace_units": row_trace_units,
                "cell_trace_units": cell_trace_units,
            }
        )

    totals = {
        "table_file_count": len(table_files),
        "total_rows": total_rows,
        "total_non_empty_cell_entries": total_cell_entries,
        "total_row_trace_units": total_row_trace_units,
        "total_cell_trace_units": total_cell_trace_units,
    }
    return totals, table_stats


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Capture baseline artifacts for M1")
    parser.add_argument("--run-root", required=True)
    parser.add_argument("--repo-root", default="")
    parser.add_argument("--opencode-config-dir", default=os.environ.get("OPENCODE_CONFIG_DIR", ""))
    args = parser.parse_args(argv)

    run_root = Path(args.run_root).resolve()
    state_path = run_root / "state.env"
    if not state_path.exists():
        print(f"error: missing state file: {state_path}", file=sys.stderr)
        return 2

    state = parse_env(state_path)
    repo_root = Path(args.repo_root or state.get("REPO_ROOT", "")).resolve()
    if not str(repo_root):
        print("error: repo root is unavailable", file=sys.stderr)
        return 2

    opencode_dir = Path(args.opencode_config_dir).resolve() if args.opencode_config_dir else None
    artifact_root = Path(state.get("ARTIFACT_ROOT", run_root / "artifacts"))
    baseline_dir = artifact_root / "baseline"
    baseline_dir.mkdir(parents=True, exist_ok=True)

    run_id = state.get("RUN_ID", "")
    target_branch = state.get("TARGET_BRANCH", "")

    narrative_path = repo_root / "src" / "iso26262_rust_mapping.md"
    text = narrative_path.read_text(encoding="utf-8")
    heading_count, paragraph_block_count, list_item_count = _count_narrative(text)

    placeholder_table_count = text.count("{{TABLE:")
    placeholder_page_break_count = text.count("{{PAGE_BREAK}}")
    placeholder_blank_count = text.count("{{BLANK}}")
    dp_role_count = len(re.findall(r"\{dp\}`", text))
    ts_role_count = len(re.findall(r"\{ts\}`", text))

    table_totals, table_items = _collect_table_inventory(repo_root)

    make_help = subprocess.run(
        ["uv", "run", "python", "make.py", "--help"],
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        check=False,
    )
    make_help_text = (make_help.stdout + ("\n" + make_help.stderr if make_help.stderr else "")).strip()

    reports_root = opencode_dir / "reports" if opencode_dir else None
    paragraph_ids_exists = (repo_root / "build" / "html" / "paragraph-ids.json").exists()
    coverage_latest_json_exists = bool(reports_root and (reports_root / "traceability-statement-coverage-latest.json").exists())
    coverage_latest_md_exists = bool(reports_root and (reports_root / "traceability-statement-coverage-latest.md").exists())

    ledger_entries = 0
    ledger_path = Path(state.get("COMMIT_LEDGER_JSON_FILE", run_root / "artifacts" / "commits" / "commit-ledger.json"))
    if ledger_path.exists():
        try:
            ledger_data = json.loads(ledger_path.read_text(encoding="utf-8"))
            ledger_entries = len(ledger_data.get("entries") or [])
        except Exception:
            ledger_entries = 0

    generated_at_utc = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    inventory = {
        "run_id": run_id,
        "generated_at_utc": generated_at_utc,
        "narrative": {
            "path": str(narrative_path.relative_to(repo_root)),
            "heading_count": heading_count,
            "paragraph_block_count": paragraph_block_count,
            "list_item_count": list_item_count,
            "legacy_tokens": {
                "table_placeholder": placeholder_table_count,
                "page_break": placeholder_page_break_count,
                "blank": placeholder_blank_count,
            },
            "trace_roles": {
                "dp_role_count": dp_role_count,
                "ts_role_count": ts_role_count,
            },
        },
        "tables": {
            **table_totals,
            "items": table_items,
        },
        "tooling_snapshot": {
            "make_help_exit_code": make_help.returncode,
            "has_trace_validate_command": "trace-validate" in make_help_text,
            "has_trace_report_command": "trace-report" in make_help_text,
            "has_verify_command": "verify" in make_help_text,
            "paragraph_ids_json_exists": paragraph_ids_exists,
            "coverage_latest_json_exists": coverage_latest_json_exists,
            "coverage_latest_md_exists": coverage_latest_md_exists,
            "commit_ledger_entry_count": ledger_entries,
        },
    }

    inventory_path = baseline_dir / "source-statement-inventory.json"
    inventory_path.write_text(json.dumps(inventory, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    baseline_md_path = baseline_dir / "current-state-baseline.md"
    baseline_md_path.write_text(
        "\n".join(
            [
                "# Current State Baseline",
                "",
                f"- run_id: `{run_id}`",
                f"- generated_at_utc: `{generated_at_utc}`",
                f"- repo_root: `{repo_root}`",
                f"- target_branch: `{target_branch}`",
                "",
                "## Source inventory snapshot",
                f"- narrative headings: {heading_count}",
                f"- narrative paragraph blocks: {paragraph_block_count}",
                f"- narrative list items: {list_item_count}",
                f"- table files: {table_totals['table_file_count']}",
                f"- table rows: {table_totals['total_rows']}",
                f"- non-empty table cell entries: {table_totals['total_non_empty_cell_entries']}",
                "",
                "## Legacy token baseline",
                f"- `{{{{TABLE:` occurrences: {placeholder_table_count}",
                f"- `{{{{PAGE_BREAK}}}}` occurrences: {placeholder_page_break_count}",
                f"- `{{{{BLANK}}}}` occurrences: {placeholder_blank_count}",
                "",
                "## Traceability baseline snapshot",
                f"- markdown `{{dp}}` role markers: {dp_role_count}",
                f"- markdown `{{ts}}` role markers: {ts_role_count}",
                f"- YAML row `_trace` units: {table_totals['total_row_trace_units']}",
                f"- YAML `cell_trace` units: {table_totals['total_cell_trace_units']}",
                f"- `build/html/paragraph-ids.json` exists: {paragraph_ids_exists}",
                f"- latest coverage JSON exists: {coverage_latest_json_exists}",
                f"- latest coverage Markdown exists: {coverage_latest_md_exists}",
                f"- commit ledger entries: {ledger_entries}",
                "",
                "## Existing make.py command behavior",
                f"- `make.py --help` exit code: {make_help.returncode}",
                f"- has `trace-validate`: {'trace-validate' in make_help_text}",
                f"- has `trace-report`: {'trace-report' in make_help_text}",
                "",
                "```text",
                make_help_text,
                "```",
                "",
                "## Artifact references",
                f"- `{inventory_path}`",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"RUN_ID={run_id}")
    print(f"RUN_ROOT={run_root}")
    print(f"BASELINE_MD={baseline_md_path}")
    print(f"BASELINE_JSON={inventory_path}")
    print(f"STATEMENTS_TOTAL={paragraph_block_count + list_item_count + table_totals['total_non_empty_cell_entries']}")
    print(f"MARKDOWN_PREFACE_UNITS={dp_role_count}")
    print(f"TABLE_CELL_UNITS={table_totals['total_cell_trace_units']}")
    print(f"TABLE_ROW_UNITS={table_totals['total_row_trace_units']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
