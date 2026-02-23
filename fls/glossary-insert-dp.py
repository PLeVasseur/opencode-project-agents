#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

DIRECTIVE_RE = re.compile(r"^(?P<indent>\s*)\.\.\s+glossary-entry::\s*(?P<term>.+?)\s*$")
ANCHOR_RE = re.compile(r"^\.\.\s+_(?P<id>[^:]+):\s*$")
GLOSSARY_DP_RE = re.compile(r"^fls_[A-Za-z0-9]+$")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Insert :glossary-dp: options based on the glossary include file."
    )
    parser.add_argument("--repo-root", default=".", help="Repo root directory")
    parser.add_argument(
        "--glossary",
        "--static",
        dest="glossary",
        default="src/glossary.rst.inc",
        help="Glossary include file",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    glossary_path = repo_root / args.glossary
    if not glossary_path.is_file():
        print(f"error: missing glossary file at {glossary_path}", file=sys.stderr)
        return 1

    mapping = parse_glossary_mapping(glossary_path)
    src_dir = repo_root / "src"
    if not src_dir.is_dir():
        print(f"error: missing src directory at {src_dir}", file=sys.stderr)
        return 1

    rst_files = sorted(src_dir.rglob("*.rst")) + sorted(src_dir.rglob("*.rst.inc"))
    for path in rst_files:
        updated = insert_glossary_dp(path, mapping)
        if updated:
            print(f"updated {path}")
    return 0


def parse_glossary_mapping(path: Path) -> dict[str, str]:
    lines, _ = read_lines(path)
    mapping: dict[str, str] = {}
    glossary_dps: set[str] = set()

    for index, line in enumerate(lines):
        anchor_match = ANCHOR_RE.match(line)
        if anchor_match is None:
            continue
        glossary_dp = anchor_match.group("id")

        cursor = index + 1
        while cursor < len(lines) and lines[cursor].strip() == "":
            cursor += 1
        if cursor + 1 >= len(lines):
            continue
        title = lines[cursor].strip()
        underline = lines[cursor + 1].strip()
        if not is_caret_underline(underline):
            continue

        if not GLOSSARY_DP_RE.fullmatch(glossary_dp):
            print(
                f"error: invalid glossary anchor {glossary_dp} for {title}",
                file=sys.stderr,
            )
            raise SystemExit(1)

        if title in mapping:
            print(f"error: duplicate term in glossary: {title}", file=sys.stderr)
            raise SystemExit(1)
        if glossary_dp in glossary_dps:
            print(
                f"error: duplicate glossary anchor in glossary: {glossary_dp}",
                file=sys.stderr,
            )
            raise SystemExit(1)

        mapping[title] = glossary_dp
        glossary_dps.add(glossary_dp)

    if not mapping:
        print("error: no glossary entries found in glossary file", file=sys.stderr)
        raise SystemExit(1)
    return mapping


def insert_glossary_dp(path: Path, mapping: dict[str, str]) -> bool:
    lines, trailing_newline = read_lines(path)
    output: list[str] = []
    changed = False
    index = 0

    while index < len(lines):
        line = lines[index]
        match = DIRECTIVE_RE.match(line)
        if match is None:
            output.append(line)
            index += 1
            continue

        term = match.group("term").strip()
        if term not in mapping:
            print(
                f"error: glossary term not found in glossary file: {term} ({path})",
                file=sys.stderr,
            )
            raise SystemExit(1)

        glossary_dp = mapping[term]
        indent = match.group("indent")
        option_indent = indent + " " * 3
        output.append(line)
        index += 1

        saw_glossary_dp = False
        while index < len(lines):
            current = lines[index]
            if current.strip() == "":
                if not saw_glossary_dp:
                    output.append(f"{option_indent}:glossary-dp: {glossary_dp}")
                    changed = True
                output.append(current)
                index += 1
                break

            if not current.startswith(option_indent):
                if not saw_glossary_dp:
                    output.append(f"{option_indent}:glossary-dp: {glossary_dp}")
                    changed = True
                output.append(current)
                index += 1
                break

            stripped = current.strip()
            if stripped.startswith(":glossary-dp:"):
                saw_glossary_dp = True
                existing = stripped.split(":", 2)[2].strip()
                if existing != glossary_dp:
                    print(
                        f"error: glossary-dp mismatch for {term}: {existing} != {glossary_dp}",
                        file=sys.stderr,
                    )
                    raise SystemExit(1)

            output.append(current)
            index += 1

        if index >= len(lines) and not saw_glossary_dp:
            output.append(f"{option_indent}:glossary-dp: {glossary_dp}")
            changed = True

    if not changed:
        return False

    write_lines(path, output, trailing_newline)
    return True


def is_caret_underline(line: str) -> bool:
    return bool(line) and set(line) == {"^"}


def read_lines(path: Path) -> tuple[list[str], bool]:
    data = path.read_text(encoding="utf-8")
    return data.splitlines(), data.endswith("\n")


def write_lines(path: Path, lines: list[str], trailing_newline: bool) -> None:
    text = "\n".join(lines)
    if trailing_newline:
        text += "\n"
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
