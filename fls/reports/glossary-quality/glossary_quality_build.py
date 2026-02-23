#!/usr/bin/env python3
import argparse
import json
import os
import re
from pathlib import Path


ANCHOR_RE = re.compile(r"^\.\. _fls_[A-Za-z0-9]+:")
UNDERLINE_RE = re.compile(r"^[=\-\^~`#\"]+$")
DP_RE = re.compile(r"^:dp:`[^`]+`$")
DT_RE = re.compile(r":dt:`([^`]+)`")
DC_RE = re.compile(r":dc:`([^`]+)`")
T_RE = re.compile(r":t:`([^`]+)`")


def read_lines(path: Path):
    return path.read_text(encoding="utf-8").splitlines()


def parse_glossary_file(path: Path):
    lines = read_lines(path)
    entries = []
    errors = []
    seen_terms = set()

    i = 0
    while i < len(lines):
        line = lines[i]
        if not ANCHOR_RE.match(line):
            i += 1
            continue

        anchor = line.strip()
        i += 1
        while i < len(lines) and lines[i].strip() == "":
            i += 1
        if i >= len(lines):
            errors.append({"anchor": anchor, "error": "missing term"})
            break

        term = lines[i].strip()
        i += 1
        underline = ""
        if i < len(lines):
            underline = lines[i].strip()
            if UNDERLINE_RE.match(underline):
                i += 1

        if term.lower() == "glossary" and set(underline) == {"="}:
            continue

        while i < len(lines) and lines[i].strip() == "":
            i += 1

        dp = None
        definition_lines = []
        while i < len(lines) and not ANCHOR_RE.match(lines[i]):
            line = lines[i].rstrip()
            if dp is None and DP_RE.match(line.strip()):
                dp = line.strip()
                i += 1
                continue
            definition_lines.append(line)
            i += 1

        while definition_lines and definition_lines[0].strip() == "":
            definition_lines.pop(0)
        while definition_lines and definition_lines[-1].strip() == "":
            definition_lines.pop()

        definition = "\n".join(definition_lines).strip()

        if term in seen_terms:
            errors.append({"term": term, "error": "duplicate term"})
        seen_terms.add(term)

        entries.append(
            {
                "term": term,
                "definition": definition,
                "anchor": anchor,
                "dp": dp,
            }
        )

    return entries, errors


def write_json(path: Path, data):
    path.write_text(json.dumps(data, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def write_tsv(path: Path, entries):
    lines = ["term\tdefinition"]
    for entry in entries:
        term = entry["term"]
        definition = entry.get("definition") or ""
        lines.append(f"{term}\t{definition}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_glossaries(repo_root: Path, report_dir: Path):
    generated_path = repo_root / "build" / "glossary.generated.rst"
    legacy_path = report_dir.parent.parent / "legacy" / "origin-main" / "src" / "glossary.rst"

    generated_entries, generated_errors = parse_glossary_file(generated_path)
    legacy_entries, legacy_errors = parse_glossary_file(legacy_path)

    generated_entries_sorted = sorted(generated_entries, key=lambda e: e["term"].casefold())
    legacy_entries_sorted = sorted(legacy_entries, key=lambda e: e["term"].casefold())

    write_json(report_dir / "glossary-generated.json", generated_entries_sorted)
    write_json(report_dir / "glossary-legacy.json", legacy_entries_sorted)
    write_json(
        report_dir / "glossary-generated-summary.json",
        {"count": len(generated_entries_sorted), "errors": generated_errors},
    )
    write_json(
        report_dir / "glossary-legacy-summary.json",
        {"count": len(legacy_entries_sorted), "errors": legacy_errors},
    )
    write_tsv(report_dir / "glossary-generated.tsv", generated_entries_sorted)
    write_tsv(report_dir / "glossary-legacy.tsv", legacy_entries_sorted)

    generated_map = {entry["term"]: entry.get("definition") or "" for entry in generated_entries_sorted}
    legacy_map = {entry["term"]: entry.get("definition") or "" for entry in legacy_entries_sorted}

    compare_entries = []
    for term in sorted(generated_map.keys(), key=lambda t: t.casefold()):
        compare_entries.append(
            {
                "term": term,
                "generated": generated_map.get(term, ""),
                "legacy": legacy_map.get(term) if term in legacy_map else None,
            }
        )
    write_json(report_dir / "glossary-compare.json", compare_entries)


def parse_index(repo_root: Path):
    index_path = repo_root / "src" / "index.rst"
    lines = read_lines(index_path)
    chapters = []
    appendices = []
    current = None
    for line in lines:
        if line.strip().startswith(".. toctree::"):
            current = "chapters"
            continue
        if line.strip().startswith(".. appendices::"):
            current = "appendices"
            continue
        if current and line.strip() and not line.startswith(" "):
            current = None
        if not line.strip() or line.strip().startswith(":"):
            continue
        if not line.startswith(" "):
            continue
        if current == "chapters":
            chapters.append(line.strip())
        elif current == "appendices":
            appendices.append(line.strip())
    return chapters, appendices


def parse_dt_terms(repo_root: Path, chapters, appendices):
    term_chapter = {}
    ambiguous_terms = {}
    extra_dt_terms = set()

    for entry in chapters + appendices:
        path = repo_root / "src" / f"{entry}.rst"
        if not path.exists():
            continue
        lines = read_lines(path)
        for idx, line in enumerate(lines, start=1):
            for regex in (DT_RE, DC_RE):
                for match in regex.finditer(line):
                    term = match.group(1).strip()
                    if not term:
                        continue
                    if term in term_chapter and term_chapter[term] != entry:
                        ambiguous_terms.setdefault(term, set()).update({term_chapter[term], entry})
                    else:
                        term_chapter.setdefault(term, entry)
    return term_chapter, ambiguous_terms, extra_dt_terms


def build_chapter_mapping(repo_root: Path, report_dir: Path):
    chapters, appendices = parse_index(repo_root)
    term_chapter, ambiguous_terms, extra_dt_terms = parse_dt_terms(repo_root, chapters, appendices)

    generated_entries = json.loads((report_dir / "glossary-generated.json").read_text(encoding="utf-8"))
    generated_terms = {entry["term"] for entry in generated_entries}

    missing_terms = sorted([term for term in generated_terms if term not in term_chapter], key=str.casefold)
    for term in term_chapter:
        if term not in generated_terms:
            extra_dt_terms.add(term)

    chapter_terms = {name: [] for name in chapters + appendices}
    misc_terms = []
    for term in sorted(generated_terms, key=str.casefold):
        chapter = term_chapter.get(term)
        if chapter and chapter in chapter_terms:
            chapter_terms[chapter].append(term)
        else:
            misc_terms.append(term)

    for term, chapter in term_chapter.items():
        if chapter not in chapter_terms:
            misc_terms.append(term)

    chapter_terms["_misc"] = sorted(set(misc_terms), key=str.casefold)

    write_json(report_dir / "term-chapter.json", term_chapter)
    write_json(report_dir / "chapter-terms.json", chapter_terms)
    write_json(
        report_dir / "mapping-issues.json",
        {
            "missing_terms": missing_terms,
            "ambiguous_terms": sorted(ambiguous_terms.keys(), key=str.casefold),
            "extra_dt_terms": sorted(extra_dt_terms, key=str.casefold),
            "chapter_entries": chapters + appendices,
        },
    )


def stub_header(title, src_file, expected):
    return "\n".join(
        [
            f"# Chapter: {title} (`src/{src_file}`)",
            "",
            "Conventions",
            "- Headings: alphabetical by term",
            f"- Coverage: expected {expected} / found {expected}",
            "Rating rubric (0-5): 5=Clear, scoped, standalone definition; no ambiguity; adds discriminators and context. 4=Mostly clear; minor missing detail or slight reliance on other terms but still useful. 3=Adequate but vague; relies on multiple other terms or lacks scope/edge cases. 2=Low signal; largely tautological, circular, or too abstract; hard to apply. 1=Bare alias, link-only \"See ...\", or fragment; not independently useful. 0=Missing definition or nonsensical/incoherent text.",
            "Issue tags: missing, link-only, alias-only, tautological, circular, truncated, fragment, list-leadin-without-list, missing-scope, missing-discriminator, low-signal, regression-vs-legacy, inconsistent-term, editorial-noise, wrong-domain, missing-see-line, definition-same-role-change-expected",
            "Legacy policy: legacy link-only/alias-only definitions are intentional; if generated expands them, mark as regression-vs-legacy and set `Legacy: better`.",
            "Overrides: if legacy vs generated differs only by :dt: vs :t:, rate 5 and tag definition-same-role-change-expected (override all other criteria). If legacy had a \"See ...\" line and generated lacks it, rate 3 and tag missing-see-line; include the missing \"See ...\" line in Notes.",
            "",
            "Checklist",
            "- [ ] Read chapter/appendix and generated glossary terms linked to this file.",
            "- [ ] Compare each term to the legacy glossary.",
            "- [ ] Flag missing/red terms or missing definitions.",
            "- [ ] Flag regressions vs legacy definition quality.",
            "- [ ] Ensure `## <term>` headings are alphabetical and match mapping (expected <count> / found <count>).",
            "- [ ] Note definition issues: list lead-ins without lists, truncated/dangling sentences, alias-only definitions, circular term chains, sentence fragments, tautologies, link-only \"See ...\" definitions, missing scope/discriminators, low-signal definitions, editorial noise/typos/spacing.",
            "",
            "Per-term template (copy for each term in this file):",
            "```text",
            "## <term>",
            "Rating: <0-5> (<label>)",
            "Issues: <tags>",
            "Notes: <why helpful/unhelpful>",
            "Legacy: <better/worse + brief reason>",
            "```",
            "",
        ]
    )


def write_stub(path: Path, title: str, src_file: str, terms):
    header = stub_header(title, src_file, len(terms))
    lines = [header]
    for term in terms:
        lines.append(f"## {term}")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_chapters_readme(report_dir: Path, chapters, appendices):
    lines = [
        "# Glossary chapter stubs",
        "",
        "All sub-agent work happens in this directory: `$OPENCODE_CONFIG_DIR/reports/glossary-quality/chapters/`.",
        "Edit only the file for your assigned chapter or appendix. Each stub contains a checklist and a per-term template.",
        "",
        "Main chapters",
    ]
    for entry in chapters:
        lines.append(f"- `{entry}.md` -> `src/{entry}.rst`")
    lines.extend(["", "Appendices"])
    for entry in appendices:
        lines.append(f"- `{entry}.md` -> `src/{entry}.rst`")
    lines.extend(
        [
            "",
            "Misc bucket",
            "- `_misc.md` -> terms not mapped to a chapter or appendix",
            "",
            "Conventions",
            "- Only edit your assigned stub file.",
            "- Headings: alphabetical by term.",
            "- Coverage: fill `expected <count> / found <count>` in your stub after mapping; counts must match before consolidation.",
            "Rating rubric (0-5): 5=Clear, scoped, standalone definition; no ambiguity; adds discriminators and context. 4=Mostly clear; minor missing detail or slight reliance on other terms but still useful. 3=Adequate but vague; relies on multiple other terms or lacks scope/edge cases. 2=Low signal; largely tautological, circular, or too abstract; hard to apply. 1=Bare alias, link-only \"See ...\", or fragment; not independently useful. 0=Missing definition or nonsensical/incoherent text.",
            "Issue tags: missing, link-only, alias-only, tautological, circular, truncated, fragment, list-leadin-without-list, missing-scope, missing-discriminator, low-signal, regression-vs-legacy, inconsistent-term, editorial-noise, wrong-domain, missing-see-line, definition-same-role-change-expected",
            "Legacy policy: legacy link-only/alias-only definitions are intentional; if generated expands them, mark as regression-vs-legacy and set `Legacy: better`.",
            "Overrides: if legacy vs generated differs only by :dt: vs :t:, rate 5 and tag definition-same-role-change-expected (override all other criteria). If legacy had a \"See ...\" line and generated lacks it, rate 3 and tag missing-see-line; include the missing \"See ...\" line in Notes.",
            "",
        ]
    )
    (report_dir / "chapters" / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_stubs(repo_root: Path, report_dir: Path):
    chapters, appendices = parse_index(repo_root)
    chapter_terms = json.loads((report_dir / "chapter-terms.json").read_text(encoding="utf-8"))
    chapters_dir = report_dir / "chapters"
    chapters_dir.mkdir(parents=True, exist_ok=True)

    for entry in chapters:
        terms = chapter_terms.get(entry, [])
        write_stub(chapters_dir / f"{entry}.md", entry.replace("-", " ").title(), f"{entry}.rst", terms)
    for entry in appendices:
        terms = chapter_terms.get(entry, [])
        write_stub(chapters_dir / f"{entry}.md", entry.replace("-", " ").title(), f"{entry}.rst", terms)

    misc_terms = chapter_terms.get("_misc", [])
    write_stub(chapters_dir / "_misc.md", "Misc", "(no file)", misc_terms)
    write_chapters_readme(report_dir, chapters, appendices)


def coverage_check(report_dir: Path):
    chapters_dir = report_dir / "chapters"
    results = []
    mismatches = []

    chapter_terms = json.loads((report_dir / "chapter-terms.json").read_text(encoding="utf-8"))
    expected_files = [f"{name}.md" for name in chapter_terms.keys() if name != "_misc"] + ["_misc.md"]

    for name in sorted(expected_files, key=str.casefold):
        path = chapters_dir / name
        if not path.exists():
            results.append(
                {
                    "file": name,
                    "expected": 0,
                    "found_declared": 0,
                    "heading_count": 0,
                    "ok": False,
                }
            )
            mismatches.append(name)
            continue
        lines = read_lines(path)
        expected = 0
        found_declared = 0
        for line in lines:
            if line.startswith("- Coverage:"):
                match = re.search(r"expected\s+(\d+)\s+/\s+found\s+(\d+)", line)
                if match:
                    expected = int(match.group(1))
                    found_declared = int(match.group(2))
                break
        heading_count = 0
        in_template = False
        for line in lines:
            if line.strip() == "```text":
                in_template = True
                continue
            if in_template and line.strip() == "```":
                in_template = False
                continue
            if not in_template and line.startswith("## "):
                heading_count += 1
        ok = expected == found_declared == heading_count
        if not ok:
            mismatches.append(path.name)
        results.append(
            {
                "file": path.name,
                "expected": expected,
                "found_declared": found_declared,
                "heading_count": heading_count,
                "ok": ok,
            }
        )

    write_json(
        report_dir / "coverage-check.json",
        {
            "total_files": len(results),
            "mismatches": mismatches,
            "results": results,
        },
    )


def normalize_t_target(raw: str):
    raw = raw.strip()
    angle = re.search(r"<([^>]+)>", raw)
    if angle:
        return angle.group(1).strip()
    bracket = re.search(r"\[([^\]]+)\]", raw)
    if bracket:
        return bracket.group(1).strip()
    return raw


def parse_t_references(repo_root: Path, report_dir: Path):
    src_dir = repo_root / "src"
    entries = []
    files = sorted(src_dir.glob("*.rst"))
    for path in files:
        lines = read_lines(path)
        for idx, line in enumerate(lines, start=1):
            for match in T_RE.finditer(line):
                raw = match.group(1)
                target = normalize_t_target(raw)
                entries.append(
                    {
                        "raw": raw,
                        "target": target,
                        "file": path.name,
                        "line": idx,
                    }
                )

    write_json(report_dir / "t-references.json", entries)

    generated_entries = json.loads((report_dir / "glossary-generated.json").read_text(encoding="utf-8"))
    generated_terms = {entry["term"] for entry in generated_entries}
    generated_terms_lower = {term.casefold(): term for term in generated_terms}

    missing = {}
    for entry in entries:
        target = entry["target"]
        if target in generated_terms:
            continue
        case_match = generated_terms_lower.get(target.casefold())
        payload = missing.setdefault(
            target,
            {"count": 0, "case_match": case_match, "samples": []},
        )
        payload["count"] += 1
        payload["samples"].append(
            {"raw": entry["raw"], "file": entry["file"], "line": entry["line"]}
        )
        if payload["case_match"] is None and case_match is not None:
            payload["case_match"] = case_match

    write_json(report_dir / "missing-terms.json", dict(sorted(missing.items(), key=lambda i: i[0].casefold())))

    missing_case = {k: v for k, v in missing.items() if v.get("case_match")}
    missing_true = {k: v for k, v in missing.items() if not v.get("case_match")}
    write_json(
        report_dir / "missing-terms-case-mismatch.json",
        dict(sorted(missing_case.items(), key=lambda i: i[0].casefold())),
    )
    write_json(
        report_dir / "missing-terms-true.json",
        dict(sorted(missing_true.items(), key=lambda i: i[0].casefold())),
    )


def main():
    parser = argparse.ArgumentParser(description="Glossary quality audit helper")
    parser.add_argument("command", choices=["parse", "map", "stubs", "trefs", "coverage", "all"])
    parser.add_argument("--repo", default=None)
    args = parser.parse_args()

    config_dir = os.environ.get("OPENCODE_CONFIG_DIR")
    if not config_dir:
        raise SystemExit("OPENCODE_CONFIG_DIR is not set")
    report_dir = Path(config_dir) / "reports" / "glossary-quality"
    report_dir.mkdir(parents=True, exist_ok=True)

    repo_root = Path(args.repo) if args.repo else Path.cwd()

    if args.command in {"parse", "all"}:
        parse_glossaries(repo_root, report_dir)
    if args.command in {"map", "all"}:
        build_chapter_mapping(repo_root, report_dir)
    if args.command in {"stubs", "all"}:
        build_stubs(repo_root, report_dir)
    if args.command in {"coverage", "all"}:
        coverage_check(report_dir)
    if args.command in {"trefs", "all"}:
        parse_t_references(repo_root, report_dir)


if __name__ == "__main__":
    raise SystemExit(main())
