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

DEFINITION_OPERATIONS = {"promote", "insert", "adapt"}


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


def percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    rank = q * (len(ordered) - 1)
    lower = int(rank)
    upper = min(lower + 1, len(ordered) - 1)
    weight = rank - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def parse_similarity(value: str) -> float | None:
    text = (value or "").strip()
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def analyze_wave(rows: list[dict[str, str]], *, min_glossary_similarity: float) -> dict:
    total = len(rows)
    pair_counts: dict[str, int] = {}
    action_types: set[str] = set()
    high_medium = 0
    deviation = 0
    pending_deviation = 0
    operation_counts = {operation: 0 for operation in sorted(DEFINITION_OPERATIONS)}
    low_similarity_ids: list[str] = []
    promote_low_similarity_ids: list[str] = []
    adapt_low_similarity_ids: list[str] = []
    insert_non_positive_net_ids: list[str] = []
    similarities: list[float] = []

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
                if (row.get("deviation_status") or "").strip().lower() == "pending":
                    pending_deviation += 1

        operation = (row.get("definition_operation") or "").strip().lower()
        if operation in operation_counts:
            operation_counts[operation] += 1

        similarity = parse_similarity(row.get("definition_similarity") or "")
        if similarity is not None:
            similarities.append(similarity)
            if checklist_id and similarity < min_glossary_similarity:
                low_similarity_ids.append(checklist_id)
                if operation == "promote":
                    promote_low_similarity_ids.append(checklist_id)
                if operation == "adapt":
                    adapt_low_similarity_ids.append(checklist_id)

        if operation == "insert":
            net_text = (row.get("insert_diff_net_delta") or "").strip()
            if net_text:
                try:
                    if int(net_text) <= 0 and checklist_id:
                        insert_non_positive_net_ids.append(checklist_id)
                except ValueError:
                    if checklist_id:
                        insert_non_positive_net_ids.append(checklist_id)

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
    similarity_stats = {
        "count": len(similarities),
        "min": min(similarities) if similarities else 0.0,
        "p50": percentile(similarities, 0.50),
        "p95": percentile(similarities, 0.95),
        "max": max(similarities) if similarities else 0.0,
    }
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
        "pending_deviation_count": pending_deviation,
        "boilerplate_hit_count": boilerplate_hits,
        "boilerplate_hit_ids": sorted(boilerplate_ids),
        "definition_operation_counts": operation_counts,
        "definition_similarity_stats": similarity_stats,
        "low_similarity_ids": sorted(low_similarity_ids),
        "promote_low_similarity_ids": sorted(promote_low_similarity_ids),
        "adapt_low_similarity_ids": sorted(adapt_low_similarity_ids),
        "insert_non_positive_net_ids": sorted(insert_non_positive_net_ids),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze rationale and definition-alignment signals for v3 ledger")
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--json-out", type=Path, required=True)
    parser.add_argument("--markdown-out", type=Path, required=True)
    parser.add_argument(
        "--min-glossary-similarity",
        type=float,
        default=0.50,
        help="Threshold used for low-similarity reporting",
    )
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
        "min_glossary_similarity": args.min_glossary_similarity,
        "waves": {
            wave: analyze_wave(items, min_glossary_similarity=args.min_glossary_similarity)
            for wave, items in sorted(waves.items())
        },
    }

    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(analysis, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "# Rationale pattern analysis (v3)",
        "",
        f"- Completed rows analyzed: `{analysis['completed_total']}`",
        f"- Low-similarity threshold: `{args.min_glossary_similarity:.2f}`",
        "",
    ]
    for wave, payload in sorted(analysis["waves"].items()):
        similarity_stats = payload["definition_similarity_stats"]
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
                f"- Pending deviation count: `{payload['pending_deviation_count']}`",
                f"- Boilerplate hit count: `{payload['boilerplate_hit_count']}`",
                f"- Definition operations: `{payload['definition_operation_counts']}`",
                (
                    "- Definition similarity stats: "
                    f"`min={similarity_stats['min']:.3f}, "
                    f"p50={similarity_stats['p50']:.3f}, "
                    f"p95={similarity_stats['p95']:.3f}, "
                    f"max={similarity_stats['max']:.3f}`"
                ),
                f"- Low similarity IDs: `{payload['low_similarity_ids']}`",
                f"- Promote low similarity IDs: `{payload['promote_low_similarity_ids']}`",
                f"- Adapt low similarity IDs: `{payload['adapt_low_similarity_ids']}`",
                f"- Insert non-positive net IDs: `{payload['insert_non_positive_net_ids']}`",
                "",
            ]
        )

    args.markdown_out.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_out.write_text("\n".join(lines), encoding="utf-8")

    print(f"ok completed={analysis['completed_total']} waves={','.join(sorted(analysis['waves'].keys()))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
