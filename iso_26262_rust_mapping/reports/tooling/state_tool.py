#!/usr/bin/env python3
"""Minimal helper for durable run state files.

Usage:
  state_tool.py write <file> key=value [key=value ...]
  state_tool.py update <file> key=value [key=value ...]

`write` starts from an empty map.
`update` loads existing key/value pairs, then applies updates.

Writes are atomic: <file>.tmp -> parse check -> rename.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def parse_env(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    if not path.exists():
        return data

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith('"') and value.endswith('"') and len(value) >= 2:
            try:
                value = bytes(value[1:-1], "utf-8").decode("unicode_escape")
            except Exception:
                value = value[1:-1]
        data[key] = value

    return data


def write_env(path: Path, data: dict[str, str]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    lines = []
    for key in sorted(data.keys()):
        value = "" if data[key] is None else str(data[key])
        value = value.replace("\\", "\\\\").replace('"', '\\"')
        lines.append(f'{key}="{value}"')

    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    subprocess.run(["bash", "-n", str(tmp)], check=True)
    os.replace(tmp, path)


def main(argv: list[str]) -> int:
    if len(argv) < 3 or argv[1] not in {"write", "update"}:
        print("usage: state_tool.py <write|update> <file> key=value ...", file=sys.stderr)
        return 2

    mode = argv[1]
    path = Path(argv[2])
    data = {} if mode == "write" else parse_env(path)

    for pair in argv[3:]:
        if "=" not in pair:
            print(f"invalid pair: {pair}", file=sys.stderr)
            return 2
        key, value = pair.split("=", 1)
        data[key] = value

    write_env(path, data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
