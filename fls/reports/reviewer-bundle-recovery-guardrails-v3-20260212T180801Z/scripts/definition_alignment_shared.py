#!/usr/bin/env python3

from __future__ import annotations

import re


COMPOUND_SPLIT_STOPWORDS = {
    "is",
    "are",
    "was",
    "were",
    "a",
    "an",
    "the",
    "of",
    "in",
    "that",
    "which",
    "and",
    "or",
    "for",
    "with",
    "by",
    "to",
    "from",
    "not",
    "no",
    "but",
    "as",
    "if",
    "so",
}

SIMILARITY_STOPWORDS = {
    "is",
    "are",
    "was",
    "were",
    "a",
    "an",
    "the",
    "of",
    "in",
    "that",
    "which",
    "and",
    "or",
    "for",
    "with",
    "by",
    "to",
    "from",
    "not",
    "no",
    "but",
    "as",
    "if",
    "so",
}

RST_ROLE_PREFIXES = (":t:", ":s:", ":c:", ":dp:", ":dc:", ":ds:")
ROLE_RE = re.compile(r":[A-Za-z_][A-Za-z0-9_-]*:`([^`]+)`")


def strip_roles(text: str) -> str:
    text = ROLE_RE.sub(r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_text_for_similarity(text: str) -> str:
    stripped = strip_roles(text)
    lowered = stripped.lower()
    lowered = re.sub(r"[^a-z0-9]+", " ", lowered)
    tokens = [token for token in lowered.split() if token and token not in SIMILARITY_STOPWORDS]
    return " ".join(tokens)


def jaccard_similarity(normalized_a: str, normalized_b: str) -> float:
    tokens_a = set(normalized_a.split())
    tokens_b = set(normalized_b.split())
    if not tokens_a and not tokens_b:
        return 1.0
    if not tokens_a or not tokens_b:
        return 0.0
    return len(tokens_a & tokens_b) / len(tokens_a | tokens_b)


def first_compound_split_token(paragraph: str, term: str) -> str | None:
    marker = f":dt:`{term}`"
    for match in re.finditer(re.escape(marker), paragraph):
        tail = paragraph[match.end() :].lstrip()
        if not tail:
            continue
        token_match = re.match(r"[:A-Za-z]+", tail)
        if token_match is None:
            continue
        token = token_match.group(0)
        lower = token.lower()
        if any(lower.startswith(prefix) for prefix in RST_ROLE_PREFIXES):
            continue
        if lower in COMPOUND_SPLIT_STOPWORDS:
            continue
        if not re.search(r"[A-Za-z]", token):
            continue
        return token
    return None


def is_subject_form_definition(paragraph: str, term: str) -> bool:
    subject_re = re.compile(
        rf"^(?:[-*]\s+)?(?:(?:A|An|The)\s+)?:dt:`{re.escape(term)}`(?=\s|[.,;:!?)]|$)",
        re.IGNORECASE,
    )
    return subject_re.match(paragraph.strip()) is not None


def analyze_dt_insert_patch(patch_text: str, term: str) -> dict[str, int | bool]:
    dt_marker = f":dt:`{term}`"
    t_marker = f":t:`{term}`"

    dt_added = 0
    dt_removed = 0
    t_removed = 0

    for raw_line in patch_text.splitlines():
        if raw_line.startswith("+++") or raw_line.startswith("---"):
            continue
        if raw_line.startswith("+"):
            dt_added += raw_line[1:].count(dt_marker)
            continue
        if raw_line.startswith("-"):
            removed = raw_line[1:]
            dt_removed += removed.count(dt_marker)
            t_removed += removed.count(t_marker)

    marker_removed = dt_removed + t_removed
    insert_net = dt_added - marker_removed
    has_dt_addition = dt_added > 0
    swap_detected = has_dt_addition and marker_removed > 0 and insert_net <= 0
    insert_pass = has_dt_addition and insert_net > 0

    return {
        "dt_added": dt_added,
        "dt_removed": dt_removed,
        "t_removed": t_removed,
        "marker_removed": marker_removed,
        "insert_net": insert_net,
        "has_dt_addition": has_dt_addition,
        "swap_detected": swap_detected,
        "insert_pass": insert_pass,
    }
