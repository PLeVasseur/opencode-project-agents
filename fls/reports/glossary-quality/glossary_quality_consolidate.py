#!/usr/bin/env python3
import json
import os
from pathlib import Path


def read_lines(path: Path):
    return path.read_text(encoding="utf-8").splitlines()


def parse_stub(path: Path):
    lines = read_lines(path)
    entries = []
    in_template = False
    current = None

    def push_current():
        nonlocal current
        if current:
            entries.append(current)
            current = None

    for line in lines:
        if line.strip() == "```text":
            in_template = True
            continue
        if in_template and line.strip() == "```":
            in_template = False
            continue
        if in_template:
            continue

        if line.startswith("## "):
            push_current()
            term = line[3:].strip()
            current = {
                "term": term,
                "rating": None,
                "label": None,
                "issues": [],
                "notes": "",
                "legacy": "",
            }
            continue
        if current is None:
            continue
        if line.startswith("Rating:"):
            raw = line.split(":", 1)[1].strip()
            if raw:
                parts = raw.split(" ", 1)
                try:
                    current["rating"] = int(parts[0])
                except ValueError:
                    current["rating"] = None
                if len(parts) > 1 and parts[1].startswith("(") and parts[1].endswith(")"):
                    current["label"] = parts[1].strip("()").strip()
            continue
        if line.startswith("Issues:"):
            raw = line.split(":", 1)[1].strip()
            if raw and raw != "none":
                current["issues"] = [tag.strip() for tag in raw.split(",") if tag.strip()]
            else:
                current["issues"] = []
            continue
        if line.startswith("Notes:"):
            current["notes"] = line.split(":", 1)[1].strip()
            continue
        if line.startswith("Legacy:"):
            current["legacy"] = line.split(":", 1)[1].strip()
            continue

    push_current()
    return entries


def format_terms_line(label, terms):
    if not terms:
        return [f"{label}: none"]
    line = f"{label}: "
    lines = []
    for term in terms:
        if len(line) + len(term) + 2 > 120:
            lines.append(line.rstrip(", "))
            line = "  " + term + ", "
        else:
            line += term + ", "
    lines.append(line.rstrip(", "))
    return lines


def main():
    config_root = os.environ.get("OPENCODE_CONFIG_DIR", "/home/pete.levasseur/opencode-project-agents/fls")
    config_dir = Path(config_root)
    report_dir = config_dir / "reports" / "glossary-quality"
    chapters_dir = report_dir / "chapters"
    output_path = config_dir / "reports" / "glossary-quality-report.md"

    chapter_terms = json.loads((report_dir / "chapter-terms.json").read_text(encoding="utf-8"))
    stub_files = [chapters_dir / f"{name}.md" for name in chapter_terms.keys() if name != "_misc"]
    stub_files.append(chapters_dir / "_misc.md")

    entries = []
    for stub in stub_files:
        if stub.exists():
            entries.extend(parse_stub(stub))

    entry_map = {entry["term"]: entry for entry in entries}

    generated_entries = json.loads((report_dir / "glossary-generated.json").read_text(encoding="utf-8"))
    generated_terms = sorted({entry["term"] for entry in generated_entries}, key=str.casefold)

    missing_terms = [term for term in generated_terms if term not in entry_map]
    extra_terms = [term for term in entry_map.keys() if term not in generated_terms]

    missing_refs_true = json.loads((report_dir / "missing-terms-true.json").read_text(encoding="utf-8"))
    missing_refs_case = json.loads((report_dir / "missing-terms-case-mismatch.json").read_text(encoding="utf-8"))

    issue_counts = {}
    for entry in entry_map.values():
        for issue in entry.get("issues", []):
            issue_counts[issue] = issue_counts.get(issue, 0) + 1

    rating_groups = {i: [] for i in range(6)}
    for entry in entry_map.values():
        rating = entry.get("rating")
        if isinstance(rating, int):
            rating_groups.setdefault(rating, []).append(entry["term"])

    missing_see_terms = sorted(
        [term for term, entry in entry_map.items() if "missing-see-line" in entry.get("issues", [])],
        key=str.casefold,
    )
    regression_terms = sorted(
        [term for term, entry in entry_map.items() if "regression-vs-legacy" in entry.get("issues", [])],
        key=str.casefold,
    )
    tautological_terms = sorted(
        [
            term
            for term, entry in entry_map.items()
            if any(tag in entry.get("issues", []) for tag in ("tautological", "circular"))
        ],
        key=str.casefold,
    )

    lines = ["# Glossary quality report", ""]
    lines.append(f"Generated terms: {len(generated_terms)}")
    lines.append(f"Reviewed terms: {len(entry_map)}")
    lines.append(
        f"Missing :t: references: {len(missing_refs_true)} true missing; {len(missing_refs_case)} case mismatches"
    )
    if missing_terms:
        lines.append(f"WARNING: missing term entries in report: {len(missing_terms)}")
    if extra_terms:
        lines.append(f"WARNING: extra term entries in report: {len(extra_terms)}")
    lines.append("")

    lines.append("## Priority index")
    lines.extend(format_terms_line("Rating 0 (missing definitions)", sorted(rating_groups.get(0, []), key=str.casefold)))
    lines.extend(format_terms_line("Rating 1 (alias/link-only)", sorted(rating_groups.get(1, []), key=str.casefold)))
    lines.extend(format_terms_line("Rating 2 (low-signal/truncated/fragment)", sorted(rating_groups.get(2, []), key=str.casefold)))
    lines.extend(format_terms_line("Missing legacy See line", missing_see_terms))
    lines.extend(format_terms_line("Regression vs legacy", regression_terms))
    lines.extend(format_terms_line("Tautological/circular", tautological_terms))
    lines.append("")

    lines.append("## Systemic issues")
    for tag in sorted(issue_counts.keys(), key=str.casefold):
        lines.append(f"- {tag}: {issue_counts[tag]}")
    lines.append("")

    lines.append("## Missing :t: references")
    if missing_refs_true:
        lines.append("True missing terms:")
        for term in sorted(missing_refs_true.keys(), key=str.casefold):
            lines.append(f"- {term}")
    else:
        lines.append("True missing terms: none")
    lines.append("")
    if missing_refs_case:
        lines.append("Case mismatches:")
        for term, payload in sorted(missing_refs_case.items(), key=lambda i: i[0].casefold()):
            case_match = payload.get("case_match")
            if case_match:
                lines.append(f"- {term} -> {case_match}")
            else:
                lines.append(f"- {term}")
    else:
        lines.append("Case mismatches: none")
    lines.append("")

    lines.append("## Term reviews")
    for term in generated_terms:
        entry = entry_map.get(term)
        if not entry:
            continue
        rating = entry.get("rating")
        label = entry.get("label") or ""
        issues = entry.get("issues") or []
        notes = entry.get("notes") or ""
        legacy = entry.get("legacy") or ""

        lines.append("")
        lines.append(f"## {term}")
        if rating is not None:
            label_text = f" ({label})" if label else ""
            lines.append(f"Rating: {rating}{label_text}")
        else:
            lines.append("Rating: ")
        lines.append("Issues: " + (", ".join(issues) if issues else "none"))
        lines.append("Notes: " + notes)
        lines.append("Legacy: " + legacy)

    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
