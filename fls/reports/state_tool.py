#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path


def parse_env(path: Path):
    data = {}
    if not path.exists():
        return data
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, v = line.split('=', 1)
        k = k.strip()
        v = v.strip()
        if v.startswith('"') and v.endswith('"') and len(v) >= 2:
            try:
                v = bytes(v[1:-1], 'utf-8').decode('unicode_escape')
            except Exception:
                v = v[1:-1]
        data[k] = v
    return data


def write_env(path: Path, data: dict):
    tmp = path.with_suffix(path.suffix + '.tmp')
    lines = []
    for k in sorted(data.keys()):
        v = '' if data[k] is None else str(data[k])
        v = v.replace('\\', '\\\\').replace('"', '\\"')
        lines.append(f'{k}="{v}"')
    tmp.write_text('\n'.join(lines) + ('\n' if lines else ''))
    subprocess.run(['bash', '-n', str(tmp)], check=True)
    os.replace(tmp, path)


def main(argv):
    if len(argv) < 3 or argv[1] not in {'write', 'update'}:
        print('usage: state_tool.py <write|update> <file> key=value ...', file=sys.stderr)
        return 2
    mode = argv[1]
    path = Path(argv[2])
    data = {} if mode == 'write' else parse_env(path)
    for pair in argv[3:]:
        if '=' not in pair:
            print(f'invalid pair: {pair}', file=sys.stderr)
            return 2
        k, v = pair.split('=', 1)
        data[k] = v
    write_env(path, data)
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
