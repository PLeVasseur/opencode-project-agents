#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path


def normalize(text):
    if not text:
        return ""
    lines = [line.strip() for line in text.splitlines()]
    cleaned = []
    for line in lines:
        if not line:
            continue
        if line.startswith(":dp:`"):
            continue
        lower = line.lower()
        if lower.startswith("see ") or lower.startswith("see:"):
            continue
        if lower.startswith("for ") and " see " in lower:
            continue
        cleaned.append(line)
    return " ".join(cleaned)


def normalize_for_role_only(text):
    if not text:
        return ""
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith(":dp:`"):
            continue
        lines.append(stripped)
    return " ".join(lines)


def is_link_only(text):
    if not text:
        return False
    low = normalize(text).lower()
    if low.startswith("see ") or low.startswith("see:"):
        return True
    if low.startswith("for ") and " see " in low:
        return True
    if low.startswith("see :") or low.startswith("for :"):
        if "see :" in low:
            return True
    # very short single-sentence cross-reference
    if low.startswith("see") and len(low.split()) <= 6:
        return True
    return False


def is_alias_only(text):
    if not text:
        return False
    low = normalize(text).lower()
    return low.startswith("for ") and " see " in low


def extract_see_lines(text):
    if not text:
        return []
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if re.match(r"(?i)^see\b", stripped):
            lines.append(stripped)
    return lines


def is_role_only_change(gen, legacy):
    if not gen or not legacy:
        return False
    gen_norm = normalize_for_role_only(gen).replace(":dt:`", ":t:`")
    legacy_norm = normalize_for_role_only(legacy).replace(":dt:`", ":t:`")
    if not gen_norm or not legacy_norm:
        return False
    return gen_norm == legacy_norm and normalize_for_role_only(gen) != normalize_for_role_only(legacy)


def is_truncated(text):
    if not text:
        return False
    stripped = normalize(text)
    if not stripped:
        return False
    if stripped.endswith(":") or stripped.endswith(","):
        return True
    tail = stripped.split()[-1].lower()
    return tail in {"and", "or", "but", "which", "that", "where", "when"}


def rate_definition(text):
    if not text or not normalize(text):
        return 0, ["missing"], "No generated definition present."

    issues = []
    if is_alias_only(text):
        issues.append("alias-only")
    elif is_link_only(text):
        issues.append("link-only")

    if is_truncated(text):
        issues.append("truncated")

    length = len(normalize(text))
    if length < 60:
        issues.append("low-signal")
    elif length < 90:
        issues.append("missing-scope")
    elif length < 120:
        issues.append("missing-discriminator")

    # determine rating
    if "missing" in issues:
        rating = 0
    elif "alias-only" in issues or "link-only" in issues:
        rating = 1
    elif "truncated" in issues:
        rating = 2
    elif "low-signal" in issues:
        rating = 2
    elif length < 120:
        rating = 3
    elif length < 200:
        rating = 4
    else:
        rating = 5

    if rating == 0:
        note = "No generated definition present."
    elif rating == 1:
        note = "Definition is a cross-reference without standalone meaning."
    elif rating == 2:
        note = "Definition is short or fragmentary and lacks usable scope."
    elif rating == 3:
        note = "Definition states the core relationship but lacks discriminators or edge cases."
    elif rating == 4:
        note = "Definition is clear and mostly scoped with at least one discriminator."
    else:
        note = "Definition is clear, scoped, and self-contained with discriminators."

    return rating, issues, note


def legacy_comparison(gen, legacy):
    if not legacy:
        return "missing", "not in legacy glossary"
    gen_norm = normalize(gen)
    legacy_norm = normalize(legacy)
    gen_link = is_link_only(gen) or is_alias_only(gen)
    legacy_link = is_link_only(legacy) or is_alias_only(legacy)

    if legacy_link:
        if gen_link:
            return "same", "both alias-only/link-only"
        return "better", "legacy intentionally uses alias-only"

    if gen_link and not legacy_link:
        return "better", "legacy has a standalone definition"

    if gen_norm == legacy_norm:
        return "same", "same wording and scope"

    if len(legacy_norm) > len(gen_norm) * 1.2:
        return "better", "legacy is more detailed"
    if len(gen_norm) > len(legacy_norm) * 1.2:
        return "worse", "legacy is shorter or less specific"
    return "same", "similar scope and detail"


def label_for_rating(rating):
    return {
        5: "clear",
        4: "mostly-clear",
        3: "adequate",
        2: "low-signal",
        1: "alias-only",
        0: "missing",
    }[rating]


def main():
    if len(sys.argv) != 2:
        print("Usage: fill_glossary_stub.py <stub-path>")
        return 2

    stub_path = Path(sys.argv[1])
    report_dir = Path("/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-quality")

    compare_path = report_dir / "glossary-compare.json"
    compare_data = json.loads(compare_path.read_text(encoding="utf-8"))
    compare_map = {entry["term"]: entry for entry in compare_data}

    lines = stub_path.read_text(encoding="utf-8").splitlines()

    # find template end
    template_end = None
    in_template = False
    for idx, line in enumerate(lines):
        if line.strip() == "```text":
            in_template = True
        elif in_template and line.strip() == "```":
            template_end = idx
            break
    if template_end is None:
        raise RuntimeError("Template block not found")

    # gather terms after template
    terms = []
    for line in lines[template_end + 1 :]:
        if line.startswith("## "):
            term = line[3:].strip()
            if term:
                terms.append(term)

    updated = lines[: template_end + 1]
    if terms:
        updated.append("")
    for term in terms:
        compare = compare_map.get(term, {"generated": "", "legacy": None})
        gen = compare.get("generated") or ""
        legacy = compare.get("legacy")

        rating, issues, note = rate_definition(gen)
        legacy_label, legacy_reason = legacy_comparison(gen, legacy)
        if legacy_label == "better":
            issues.append("regression-vs-legacy")

        if is_role_only_change(gen, legacy):
            rating = 5
            issues = ["definition-same-role-change-expected"]
            note = "Generated definition matches legacy with :dt: -> :t: role-only change."
            legacy_label = "same"
            legacy_reason = "role-only change (:dt: to :t:)"
        else:
            legacy_see = extract_see_lines(legacy)
            gen_see = extract_see_lines(gen)
            missing_see = []
            if legacy_see:
                for line in legacy_see:
                    if not any(line.lower() == g.lower() for g in gen_see):
                        missing_see.append(line)
            if missing_see:
                rating = 3
                issues.append("missing-see-line")
                missing_joined = "; ".join(missing_see)
                note = f"{note} Missing legacy See line: {missing_joined}"

        label = label_for_rating(rating)
        issues_text = "none" if not issues else ", ".join(sorted(set(issues)))
        
        updated.append(f"## {term}")
        updated.append(f"Rating: {rating} ({label})")
        updated.append(f"Issues: {issues_text}")
        updated.append(f"Notes: {note}")
        updated.append(f"Legacy: {legacy_label} - {legacy_reason}.")
        updated.append("")

    stub_path.write_text("\n".join(updated).rstrip() + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
