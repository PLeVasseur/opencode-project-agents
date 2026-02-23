#!/usr/bin/env python3
import difflib
import pathlib
import re
import subprocess
import sys

out = pathlib.Path(sys.argv[1])
upstream = sys.argv[2]
current = sys.argv[3]
out.mkdir(parents=True, exist_ok=True)


def git_show(ref: str, path: str) -> str:
    return subprocess.check_output(["git", "show", f"{ref}:{path}"], text=True, encoding="utf-8", errors="replace")


def list_src_files(ref: str):
    raw = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", ref, "src"], text=True)
    return [p.strip() for p in raw.splitlines() if p.strip().endswith(".rst")]


def materialize_glossary_entries(text: str) -> str:
    lines = text.splitlines()
    out_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^(\s*)\.\. glossary-entry::\s+.+$', line)
        if not m:
            out_lines.append(line)
            i += 1
            continue
        base_indent = len(m.group(1))
        j = i + 1
        block = [line]
        while j < len(lines):
            cur = lines[j]
            if cur.strip() == "":
                block.append(cur)
                j += 1
                continue
            indent = len(cur) - len(cur.lstrip(" "))
            if indent <= base_indent:
                break
            block.append(cur)
            j += 1
        chapter_idx = None
        chapter_indent = None
        for bi, bl in enumerate(block):
            sm = re.match(r'^(\s*):chapter:\s*$', bl)
            if sm:
                chapter_idx = bi
                chapter_indent = len(sm.group(1))
                break
        if chapter_idx is not None:
            for bl in block[chapter_idx + 1:]:
                if bl.strip() == "":
                    out_lines.append("")
                    continue
                indent = len(bl) - len(bl.lstrip(" "))
                if indent <= chapter_indent:
                    break
                drop = min(len(bl), chapter_indent + 2)
                dedented = bl[drop:]
                out_lines.append(" " * base_indent + dedented)
        i = j
    return "\n".join(out_lines) + "\n"


def extract_hygiene_section(text: str) -> str:
    lines = text.splitlines()
    start = None
    for i in range(len(lines) - 1):
        if lines[i].strip() == "Hygiene" and set(lines[i + 1].strip()) == {"-"}:
            start = i
            break
    if start is None:
        return text
    end = len(lines)
    for j in range(start + 2, len(lines)):
        if lines[j].startswith(".. _fls_"):
            end = j
            break
    return "\n".join(lines[start:end]).rstrip() + "\n"


def parse_entries_from_glossary_file(text: str, anchors: dict, dps: dict):
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        am = re.match(r'^\.\.\s+_(\S+):\s*$', line)
        if not am:
            i += 1
            continue
        anchor = am.group(1)
        j = i + 1
        while j < len(lines) and lines[j].strip() == "":
            j += 1
        if j >= len(lines):
            break
        term = lines[j].strip()
        if not term or term == "Glossary" or term.startswith(":"):
            i += 1
            continue
        k = j + 1
        if k < len(lines) and re.match(r'^[\^\-~=]{2,}\s*$', lines[k].strip()):
            k += 1
        first_dp = ""
        while k < len(lines):
            t = lines[k].strip()
            if t.startswith(".. _"):
                break
            dm = re.match(r'^:dp:`([^`]+)`$', t)
            if dm:
                first_dp = dm.group(1)
                break
            k += 1
        anchors.setdefault(term, anchor)
        if first_dp:
            dps.setdefault(term, first_dp)
        i = k


def parse_entries_from_glossary_directives(text: str, anchors: dict, dps: dict):
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        gm = re.match(r'^(\s*)\.\. glossary-entry::\s+(.+?)\s*$', line)
        if not gm:
            i += 1
            continue
        base_indent = len(gm.group(1))
        term = gm.group(2).strip()
        j = i + 1
        block = []
        while j < len(lines):
            cur = lines[j]
            if cur.strip() == "":
                block.append(cur)
                j += 1
                continue
            indent = len(cur) - len(cur.lstrip(" "))
            if indent <= base_indent:
                break
            block.append(cur)
            j += 1
        anchor = ""
        dp = ""
        in_glossary = False
        glossary_indent = -1
        for bl in block:
            stripped = bl.strip()
            am = re.match(r'^:glossary-dp:\s*(\S+)\s*$', stripped)
            if am:
                anchor = am.group(1)
            gm2 = re.match(r'^(\s*):glossary:\s*$', bl)
            if gm2:
                in_glossary = True
                glossary_indent = len(gm2.group(1))
                continue
            if in_glossary:
                if stripped == "":
                    continue
                indent = len(bl) - len(bl.lstrip(" "))
                if indent <= glossary_indent:
                    in_glossary = False
                    continue
                if not dp:
                    dm = re.match(r'^\s*:dp:`([^`]+)`\s*$', bl)
                    if dm:
                        dp = dm.group(1)
        if anchor:
            anchors.setdefault(term, anchor)
        if dp:
            dps.setdefault(term, dp)
        i = j


def collect_maps(ref: str):
    anchors = {}
    dps = {}
    for path in list_src_files(ref):
        text = git_show(ref, path)
        if path == "src/glossary.rst":
            parse_entries_from_glossary_file(text, anchors, dps)
        parse_entries_from_glossary_directives(text, anchors, dps)
    return anchors, dps


up_mat = extract_hygiene_section(materialize_glossary_entries(git_show(upstream, "src/macros.rst")))
cur_mat = extract_hygiene_section(materialize_glossary_entries(git_show(current, "src/macros.rst")))
(out / "chapter-macros-materialized-upstream.txt").write_text(up_mat)
(out / "chapter-macros-materialized-current.txt").write_text(cur_mat)
(out / "chapter-macros-materialized.diff").write_text(
    "".join(
        difflib.unified_diff(
            up_mat.splitlines(keepends=True),
            cur_mat.splitlines(keepends=True),
            fromfile="upstream",
            tofile="current",
        )
    )
)

up_a, up_d = collect_maps(upstream)
cu_a, cu_d = collect_maps(current)
common_anchor_terms = sorted(set(up_a).intersection(cu_a))
common_dp_terms = sorted(set(up_d).intersection(cu_d))


def write_map(path: pathlib.Path, rows):
    path.write_text("\n".join(rows) + ("\n" if rows else ""))

write_map(out / "glossary-term-anchor-map-upstream.tsv", [f"{t}\t{up_a[t]}" for t in common_anchor_terms])
write_map(out / "glossary-term-anchor-map-current.tsv", [f"{t}\t{cu_a[t]}" for t in common_anchor_terms])
write_map(out / "glossary-term-dp-map-upstream.tsv", [f"{t}\t{up_d[t]}" for t in common_dp_terms])
write_map(out / "glossary-term-dp-map-current.tsv", [f"{t}\t{cu_d[t]}" for t in common_dp_terms])

(out / "glossary-term-anchor-map.diff").write_text(
    "".join(
        difflib.unified_diff(
            (out / "glossary-term-anchor-map-upstream.tsv").read_text().splitlines(keepends=True),
            (out / "glossary-term-anchor-map-current.tsv").read_text().splitlines(keepends=True),
            fromfile="upstream",
            tofile="current",
        )
    )
)
(out / "glossary-term-dp-map.diff").write_text(
    "".join(
        difflib.unified_diff(
            (out / "glossary-term-dp-map-upstream.tsv").read_text().splitlines(keepends=True),
            (out / "glossary-term-dp-map-current.tsv").read_text().splitlines(keepends=True),
            fromfile="upstream",
            tofile="current",
        )
    )
)
