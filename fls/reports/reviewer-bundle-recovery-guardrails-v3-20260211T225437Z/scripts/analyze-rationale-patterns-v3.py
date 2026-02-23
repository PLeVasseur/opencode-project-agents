#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import itertools
import json
import re
from pathlib import Path


BOILERPLATE_PATTERNS = [
    re.compile(r"Before .+\(.+\) used :dt:`.+`.+After .+uses :t:`", re.IGNORECASE | re.DOTALL),
    re.compile(r"retained .* paragraph .* rewrote term markup", re.IGNORECASE),
]


def is_completed(row: dict[str, str]) -> bool:
    phase1 = (row.get("phase1_status") or "").strip().lower()
    final_quality = (row.get("final_quality") or "").strip().lower()
    return phase1 == "completed" or final_quality in {"resolved-high", "resolved-exception", "blocked"}


def jaccard(a: str, b: str) -> float:
    tokens_a = {token for token in re.split(r"\s+", a.lower().strip()) if token}
    tokens_b = {token for token in re.split(r"\s+", b.lower().strip()) if token}
    if not tokens_a and not tokens_b:
        return 1.0
    if not tokens_a or not tokens_b:
        return 0.0
    return len(tokens_a & tokens_b) / len(tokens_a | tokens_b)


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def analyze_wave(rows: list[dict[str, str]]) -> dict:
    total = len(rows)
    pair_counts: dict[str, int] = {}
    action_types: set[str] = set()
    high_medium = 0
    deviation = 0

    reasons = []
    boilerplate_hits = 0
    boilerplate_ids: list[str] = []
    for row in rows:
        action = (row.get("action_type") or "").strip()
        reason_code = (row.get("reason_code") or "").strip()
        pair = f"{action}|{reason_code}"
        pair_counts[pair] = pair_counts.get(pair, 0) + 1
        if action:
            action_types.add(action)

        checklist_id = (row.get("checklist_id") or "").strip()
        reason_why = (row.get("reason_why") or "").strip()
        reasons.append((checklist_id, reason_why))

        if any(pattern.search(reason_why) for pattern in BOILERPLATE_PATTERNS):
            boilerplate_hits += 1
            if checklist_id:
                boilerplate_ids.append(checklist_id)

        priority = (row.get("recommendation_priority") or "").strip().lower()
        used = (row.get("recommendation_used") or "").strip().lower()
        if priority in {"high", "medium"}:
            high_medium += 1
            if used != "yes":
                deviation += 1

    max_pair = None
    max_pair_fraction = 0.0
    if pair_counts and total > 0:
        max_pair = max(pair_counts, key=lambda key: pair_counts[key])
        max_pair_fraction = pair_counts[max_pair] / total

    max_similarity = 0.0
    max_similarity_pair: tuple[str, str] | None = None
    for (id_a, text_a), (id_b, text_b) in itertools.combinations(reasons, 2):
        score = jaccard(text_a, text_b)
        if score > max_similarity:
            max_similarity = score
            max_similarity_pair = (id_a, id_b)

    deviation_fraction = deviation / high_medium if high_medium else 0.0
    return {
        "completed_rows": total,
        "unique_action_types": sorted(action_types),
        "action_reason_counts": pair_counts,
        "max_action_reason_pair": max_pair,
        "max_action_reason_fraction": max_pair_fraction,
        "max_reason_jaccard": max_similarity,
        "max_reason_jaccard_pair": max_similarity_pair,
        "high_medium_count": high_medium,
        "deviation_count": deviation,
        "deviation_fraction": deviation_fraction,
        "deviation_permit_count": deviation,
        "boilerplate_hit_count": boilerplate_hits,
        "boilerplate_hit_ids": sorted(boilerplate_ids),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze rationale monoculture signals for v3 ledger")
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--json-out", type=Path, required=True)
    parser.add_argument("--markdown-out", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    rows = load_rows(args.ledger)
    completed = [row for row in rows if is_completed(row)]

    waves: dict[str, list[dict[str, str]]] = {}
    for row in completed:
        wave = (row.get("wave") or "").strip().upper()
        waves.setdefault(wave, []).append(row)

    analysis = {
        "completed_total": len(completed),
        "waves": {wave: analyze_wave(items) for wave, items in sorted(waves.items())},
    }

    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(analysis, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "# Rationale pattern analysis (v3)",
        "",
        f"- Completed rows analyzed: `{analysis['completed_total']}`",
        "",
    ]
    for wave, payload in sorted(analysis["waves"].items()):
        lines.extend(
            [
                f"## {wave}",
                "",
                f"- Completed rows: `{payload['completed_rows']}`",
                f"- Unique action types: `{len(payload['unique_action_types'])}`",
                f"- Max action+reason fraction: `{payload['max_action_reason_fraction']:.3f}`",
                f"- Max reason Jaccard: `{payload['max_reason_jaccard']:.3f}`",
                f"- Deviation fraction: `{payload['deviation_fraction']:.3f}`",
                f"- Deviation permit count: `{payload['deviation_permit_count']}`",
                f"- Boilerplate hit count: `{payload['boilerplate_hit_count']}`",
                "",
            ]
        )

    args.markdown_out.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_out.write_text("\n".join(lines), encoding="utf-8")

    print(f"ok completed={analysis['completed_total']} waves={','.join(sorted(analysis['waves'].keys()))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
