#!/usr/bin/env python3
# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Ferrocene Developers

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
import sys


DIRECTIVE_RE = re.compile(r"^(?P<indent>\s*)\.\.\s+glossary-entry::\s*(?P<term>.+?)\s*$")
CHECKLIST_RE = re.compile(r"^- \[(?P<status>[ xX])\] (?P<term>.+?)\s*$")
DP_RE = re.compile(r":dp:`(?P<id>[^`]+)`")


@dataclass
class GlossaryStaticEntry:
    term: str
    anchor: str
    body_lines: list[str]


@dataclass
class DirectiveInfo:
    term: str
    file: Path
    chapter_dp: list[str]


@dataclass
class EntryHeader:
    start: int
    term: str
    header_end: int
    anchor: str


def main() -> int:
    env_dir = os.environ.get("OPENCODE_CONFIG_DIR")
    default_term_map = None
    default_checklist = None
    if env_dir:
        default_term_map = (
            Path(env_dir) / "reports/glossary-migration-phase2/term-map.jsonl"
        )
        default_checklist = Path(env_dir) / "plans/glossary-migration-checklist.md"

    parser = argparse.ArgumentParser(
        description=(
            "Append missing glossary migration metadata entries to term-map.jsonl."
        )
    )
    parser.add_argument("--repo-root", default=".", help="Repo root directory")
    parser.add_argument("--src", default="src", help="Source directory")
    parser.add_argument(
        "--glossary",
        default="src/glossary.static.rst.inc",
        help="Static glossary file",
    )
    parser.add_argument(
        "--term-map",
        default=str(default_term_map) if default_term_map else None,
        required=default_term_map is None,
        help="Term map JSONL path",
    )
    parser.add_argument(
        "--checklist",
        default=str(default_checklist) if default_checklist else None,
        help="Checklist file for term selection",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=20,
        help="Number of unchecked terms to take from checklist",
    )
    parser.add_argument("--terms", nargs="*", help="Explicit term list")
    parser.add_argument(
        "--status",
        default="migrated",
        help="Status value for term-map entries",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print JSONL entries without writing",
    )
    args = parser.parse_args()

    terms = resolve_terms(args.terms, args.checklist, args.count)
    if not terms:
        print("error: no terms provided", file=sys.stderr)
        return 1

    repo_root = Path(args.repo_root).resolve()
    src_dir = repo_root / args.src
    glossary_path = repo_root / args.glossary
    term_map_path = Path(args.term_map)

    if not glossary_path.is_file():
        print(f"error: missing glossary file at {glossary_path}", file=sys.stderr)
        return 1

    if not src_dir.is_dir():
        print(f"error: missing src directory at {src_dir}", file=sys.stderr)
        return 1

    glossary_entries = parse_glossary_static(glossary_path)
    directive_map = collect_directive_info(src_dir, repo_root)
    existing_terms = load_existing_terms(term_map_path)

    emitted_lines: list[str] = []
    for term in terms:
        if term in existing_terms:
            warn(f"term already present in term-map: {term}")
            continue
        entry = glossary_entries.get(term)
        if entry is None:
            warn(f"term not found in static glossary: {term}")
            continue
        directive = directive_map.get(term)
        if directive is None:
            warn(f"glossary-entry not found in src files: {term}")
            continue

        glossary_dp = extract_dp(entry.body_lines)
        glossary_text_hash = hash_lines(entry.body_lines)
        chapter_file = directive.file.as_posix()

        data = {
            "chapter_dp": directive.chapter_dp,
            "chapter_file": chapter_file,
            "glossary_anchor": entry.anchor,
            "glossary_dp": glossary_dp,
            "glossary_text_hash": glossary_text_hash,
            "status": args.status,
            "term": term,
        }
        emitted_lines.append(json.dumps(data, ensure_ascii=True))

    if not emitted_lines:
        warn("no new term-map entries to write")
        return 0

    if args.dry_run:
        for line in emitted_lines:
            print(line)
        return 0

    append_jsonl(term_map_path, emitted_lines)
    return 0


def resolve_terms(terms: list[str] | None, checklist: str | None, count: int) -> list[str]:
    if terms:
        return terms
    if checklist is None:
        return []
    return parse_checklist(Path(checklist), count)


def parse_checklist(path: Path, count: int) -> list[str]:
    if not path.is_file():
        print(f"error: missing checklist at {path}", file=sys.stderr)
        return []
    lines = read_lines(path)
    terms: list[str] = []
    for line in lines:
        match = CHECKLIST_RE.match(line)
        if not match:
            continue
        if match.group("status") != " ":
            continue
        terms.append(match.group("term"))
        if count and len(terms) >= count:
            break
    return terms


def parse_glossary_static(path: Path) -> dict[str, GlossaryStaticEntry]:
    lines = read_lines(path)
    headers: list[EntryHeader] = []
    for index in range(len(lines)):
        header = parse_entry_header(lines, index)
        if header is not None:
            headers.append(header)

    entries: dict[str, GlossaryStaticEntry] = {}
    for pos, header in enumerate(headers):
        next_start = headers[pos + 1].start if pos + 1 < len(headers) else len(lines)
        body_lines = trim_trailing_blanks(lines[header.header_end:next_start])
        entries[header.term] = GlossaryStaticEntry(
            term=header.term, anchor=header.anchor, body_lines=body_lines
        )
    return entries


def parse_entry_header(lines: list[str], index: int) -> EntryHeader | None:
    line = lines[index]
    if not line.startswith(".. _fls_"):
        return None

    anchor = parse_anchor(line)
    cursor = index + 1
    while cursor < len(lines) and lines[cursor].strip() == "":
        cursor += 1
    if cursor + 1 >= len(lines):
        return None

    title = lines[cursor]
    underline = lines[cursor + 1]
    if not is_caret_underline(underline):
        return None

    header_end = cursor + 2
    if header_end < len(lines) and lines[header_end].strip() == "":
        header_end += 1

    return EntryHeader(start=index, term=title.strip(), header_end=header_end, anchor=anchor)


def parse_anchor(line: str) -> str:
    anchor = line[len(".. ") :]
    if anchor.endswith(":"):
        anchor = anchor[:-1]
    return anchor


def is_caret_underline(line: str) -> bool:
    stripped = line.strip()
    return bool(stripped) and set(stripped) == {"^"}


def collect_directive_info(src_dir: Path, repo_root: Path) -> dict[str, DirectiveInfo]:
    directives: dict[str, DirectiveInfo] = {}
    for path in sorted(src_dir.glob("*.rst")):
        for directive in parse_glossary_directives(path):
            term = directive.term
            if term in directives:
                warn(f"duplicate glossary-entry in src for term: {term}")
                continue
            directives[term] = DirectiveInfo(
                term=term,
                file=path.relative_to(repo_root),
                chapter_dp=directive.chapter_dp,
            )
    return directives


def parse_glossary_directives(path: Path) -> list[DirectiveInfo]:
    lines = read_lines(path)
    results: list[DirectiveInfo] = []
    index = 0
    while index < len(lines):
        match = DIRECTIVE_RE.match(lines[index])
        if not match:
            index += 1
            continue

        base_indent = len(match.group("indent"))
        term = match.group("term").strip()
        block_lines, next_index = read_indented_block(lines, index + 1, base_indent)
        _, content_lines = split_options(block_lines)
        _, chapter_lines = parse_section_blocks(content_lines)
        chapter_dp = extract_dp(chapter_lines or [])
        results.append(
            DirectiveInfo(term=term, file=path, chapter_dp=chapter_dp)
        )

        index = max(next_index, index + 1)
    return results


def read_indented_block(
    lines: list[str], start_index: int, base_indent: int
) -> tuple[list[str], int]:
    index = start_index
    block_indent = None

    while index < len(lines):
        line = lines[index]
        if line.strip() == "":
            if count_indent(line) <= base_indent:
                return [], index
            index += 1
            continue

        indent = count_indent(line)
        if indent <= base_indent:
            return [], index
        block_indent = indent
        break

    if block_indent is None:
        return [], index

    block_lines: list[str] = []
    while index < len(lines):
        line = lines[index]
        if line.strip() == "":
            if count_indent(line) <= base_indent:
                break
            block_lines.append("")
            index += 1
            continue

        indent = count_indent(line)
        if indent < block_indent:
            break

        block_lines.append(line[block_indent:])
        index += 1

    return block_lines, index


def split_options(block_lines: list[str]) -> tuple[dict[str, object], list[str]]:
    options: dict[str, object] = {}
    content: list[str] = []
    in_options = True

    for line in block_lines:
        if in_options:
            if line.strip() == "":
                in_options = False
                continue

            if line.startswith(":") and ":" in line[1:]:
                name, value = parse_option_line(line)
                options[name] = value
                continue

            in_options = False

        content.append(line)

    return options, content


def parse_option_line(line: str) -> tuple[str, str]:
    parts = line.split(":", 2)
    name = parts[1].strip() if len(parts) > 1 else ""
    value = parts[2].strip() if len(parts) > 2 else ""
    return name, value


def parse_section_blocks(content_lines: list[str]) -> tuple[list[str] | None, list[str] | None]:
    sections: dict[str, list[str] | None] = {"glossary": None, "chapter": None}
    current = None
    buffer: list[str] = []

    for line in content_lines:
        stripped = line.strip()
        if stripped in (":glossary:", ":chapter:") and line.startswith(":"):
            if current is not None:
                sections[current] = dedent_block(buffer)
            current = stripped.strip(":")
            buffer = []
            continue

        if current is None:
            continue

        buffer.append(line)

    if current is not None:
        sections[current] = dedent_block(buffer)

    return sections["glossary"], sections["chapter"]


def dedent_block(lines: list[str]) -> list[str]:
    indents = [len(line) - len(line.lstrip(" ")) for line in lines if line.strip()]
    indent = min(indents) if indents else 0
    return [line[indent:] if len(line) >= indent else "" for line in lines]


def extract_dp(lines: list[str]) -> list[str]:
    dps: list[str] = []
    for line in lines:
        for match in DP_RE.finditer(line):
            dps.append(match.group("id"))
    return dps


def hash_lines(lines: list[str]) -> str:
    text = "\n".join(lines)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def trim_trailing_blanks(lines: list[str]) -> list[str]:
    trimmed = list(lines)
    while trimmed and trimmed[-1].strip() == "":
        trimmed.pop()
    return trimmed


def count_indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def load_existing_terms(path: Path) -> set[str]:
    if not path.exists():
        return set()
    terms: set[str] = set()
    for line in read_lines(path):
        if not line.strip():
            continue
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            warn(f"skipping invalid JSONL in term-map: {path}")
            continue
        term = data.get("term")
        if isinstance(term, str):
            terms.add(term)
    return terms


def append_jsonl(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    needs_newline = False
    if path.exists() and path.stat().st_size > 0:
        with path.open("rb") as handle:
            handle.seek(-1, os.SEEK_END)
            last = handle.read(1)
            if last != b"\n":
                needs_newline = True
    with path.open("a", encoding="utf-8") as handle:
        if needs_newline:
            handle.write("\n")
        for line in lines:
            handle.write(line + "\n")


def warn(message: str) -> None:
    print(f"warning: {message}", file=sys.stderr)


if __name__ == "__main__":
    raise SystemExit(main())
