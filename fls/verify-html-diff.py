#!/usr/bin/env -S uv run
# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Ferrocene Developers

from __future__ import annotations

from pathlib import Path
import json
import os
import shutil
import subprocess
import sys
import filecmp


def main() -> int:
    config_dir = Path(os.environ.get("OPENCODE_CONFIG_DIR", ""))
    if not config_dir:
        print("error: OPENCODE_CONFIG_DIR is not set", file=sys.stderr)
        return 1

    repo_root = Path.cwd()
    if not (repo_root / "make.py").is_file():
        print("error: run from the repo root", file=sys.stderr)
        return 1

    reports_dir = config_dir / "reports"
    baseline_dir = reports_dir / "html-baseline"
    generated_dir = reports_dir / "html-generated"
    report_path = reports_dir / "html-diff.txt"
    reports_dir.mkdir(parents=True, exist_ok=True)

    run(["./make.py", "--clear"], repo_root)
    copy_tree(repo_root / "build" / "html", baseline_dir)

    run([sys.executable, repo_root / "generate-glossary.py"], repo_root)
    run(["./make.py", "--use-generated-glossary", "--clear"], repo_root)
    copy_tree(repo_root / "build" / "html", generated_dir)

    diff = diff_trees(baseline_dir, generated_dir)
    write_report(report_path, diff)

    if diff["only_left"] or diff["only_right"] or diff["changed"]:
        print(f"warning: differences found; see {report_path}")
    else:
        print(f"no differences; report written to {report_path}")

    return 0


def run(command: list[object], cwd: Path) -> None:
    subprocess.run([str(part) for part in command], check=True, cwd=cwd)


def copy_tree(source: Path, destination: Path) -> None:
    if not source.is_dir():
        raise RuntimeError(f"missing build output at {source}")
    shutil.copytree(source, destination, dirs_exist_ok=True)


def diff_trees(left: Path, right: Path) -> dict[str, list[str]]:
    left_files = list_files(left)
    right_files = list_files(right)

    only_left = []
    only_right = []
    changed = []
    comparisons = []

    for rel in sorted(set(left_files) | set(right_files)):
        if rel not in right_files:
            only_left.append(rel)
            continue
        if rel not in left_files:
            only_right.append(rel)
            continue
        special = compare_special(rel, left_files[rel], right_files[rel])
        if special is not None:
            comparisons.append(special["message"])
            if not special["equal"]:
                changed.append(rel)
            continue
        if not filecmp.cmp(left_files[rel], right_files[rel], shallow=False):
            changed.append(rel)

    return {
        "only_left": only_left,
        "only_right": only_right,
        "changed": changed,
        "comparisons": comparisons,
    }


def compare_special(rel: str, left: Path, right: Path) -> dict[str, object] | None:
    name = os.path.basename(rel)
    if name == "paragraph-ids.json":
        return compare_paragraph_ids(left, right)
    if name == ".buildinfo":
        return compare_buildinfo(left, right)
    return None


def compare_paragraph_ids(left: Path, right: Path) -> dict[str, object]:
    left_data = normalize_paragraph_ids(left)
    right_data = normalize_paragraph_ids(right)
    if left_data == right_data:
        return {"equal": True, "message": "paragraph-ids.json: normalized content matches"}
    return {"equal": False, "message": "paragraph-ids.json: normalized content differs"}


def normalize_paragraph_ids(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    documents = []
    for doc in data.get("documents", []):
        sections = []
        for section in doc.get("sections", []):
            paragraphs = sorted(
                section.get("paragraphs", []),
                key=lambda paragraph: paragraph.get("id", ""),
            )
            section_data = dict(section)
            section_data["paragraphs"] = paragraphs
            sections.append(section_data)
        sections.sort(key=lambda item: item.get("id", ""))
        doc_data = dict(doc)
        doc_data["sections"] = sections
        documents.append(doc_data)
    documents.sort(key=lambda item: item.get("link", ""))
    return {"documents": documents}


def compare_buildinfo(left: Path, right: Path) -> dict[str, object]:
    left_info = read_buildinfo(left)
    right_info = read_buildinfo(right)
    left_config = left_info.get("config")
    right_config = right_info.get("config")
    if left_config != right_config:
        return {"equal": False, "message": ".buildinfo: config hash differs"}

    left_tags = left_info.get("tags")
    right_tags = right_info.get("tags")
    if left_tags != right_tags:
        return {
            "equal": True,
            "message": ".buildinfo: config matches; tags differ (ignored)",
        }
    return {"equal": True, "message": ".buildinfo: config matches"}


def read_buildinfo(path: Path) -> dict[str, str]:
    info: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        info[key.strip()] = value.strip()
    return info


def list_files(root: Path) -> dict[str, Path]:
    files: dict[str, Path] = {}
    for dirpath, _, filenames in os.walk(root):
        base = Path(dirpath)
        for name in filenames:
            rel = str((base / name).relative_to(root))
            files[rel] = base / name
    return files


def write_report(path: Path, diff: dict[str, list[str]]) -> None:
    lines: list[str] = []
    lines.append("HTML diff summary")
    lines.append("")
    lines.append("Only in baseline:")
    lines.extend(format_list(diff["only_left"]))
    lines.append("")
    lines.append("Only in generated:")
    lines.extend(format_list(diff["only_right"]))
    lines.append("")
    lines.append("Changed files:")
    lines.extend(format_list(diff["changed"]))
    lines.append("")
    lines.append("Special comparisons:")
    lines.extend(format_list(diff["comparisons"]))
    lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def format_list(values: list[str]) -> list[str]:
    if not values:
        return ["- (none)"]
    return [f"- {value}" for value in values]


if __name__ == "__main__":
    raise SystemExit(main())
