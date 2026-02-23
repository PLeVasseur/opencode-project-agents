# Coverage accounting regression evidence

## Objective

Prove glossary inventory coverage now includes multi-term glossary definitions and alias terms that were previously dropped from accounting.

## Executed assertion

Command (executed in remediation run):

```bash
jq -e 'map(select(.term_id == "cast" or .term_id == "casting" or .term_id == "path" or .term_id == "namespace_qualifier" or .term_id == "shadowing" or .term_id == "shadowed")) as $rows | ($rows | length) == 6 and all($rows[]; .chapter_file != null)' "$REMEDIATION_DIR/term-inventory.json" >/dev/null
```

Result: **pass** (exit code `0`).

## Evidence rows

```json
[
  {
    "term": "Cast",
    "term_id": "cast",
    "chapter_file": "src/expressions.rst",
    "chapter_line": 2185
  },
  {
    "term": "casting",
    "term_id": "casting",
    "chapter_file": "src/expressions.rst",
    "chapter_line": 2185
  },
  {
    "term": "path",
    "term_id": "path",
    "chapter_file": "src/entities-and-resolution.rst",
    "chapter_line": 301
  },
  {
    "term": "namespace qualifier",
    "term_id": "namespace_qualifier",
    "chapter_file": "src/entities-and-resolution.rst",
    "chapter_line": 302
  },
  {
    "term": "Shadowing",
    "term_id": "shadowing",
    "chapter_file": "src/entities-and-resolution.rst",
    "chapter_line": 41
  },
  {
    "term": "shadowed",
    "term_id": "shadowed",
    "chapter_file": "src/entities-and-resolution.rst",
    "chapter_line": 41
  }
]
```
