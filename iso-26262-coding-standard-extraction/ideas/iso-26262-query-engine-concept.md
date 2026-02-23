# ISO 26262 Query Engine Proposal

Here’s a practical, “engineerable” way to turn your *licensed* ISO 26262 PDFs into a **local, queryable corpus** where every hit can be **cited** (part/edition, clause/table ID, page range), even when the PDFs are annoying.

The core idea:

1. **Ingest** PDFs → extract text + tables + structure
2. **Atomize** into correctly-sized “chunks” (clause/table/list item) with strong metadata
3. **Index** locally (SQLite FTS for exact search; optionally embeddings for fuzzy search)
4. **Query** → return snippets + citations + “open-at-page” pointers

---

## What “correctly sized pieces” look like (the chunk model)

Make each stored unit one of these types:

* `clause` (e.g., `6:2018 5.4.3`)
* `table` (e.g., `6:2018 Table 1`)
* `subclause` (e.g., `8.4.5` inside a clause)
* `list_item` / `requirement_atom` (split bullets/shall statements)
* `annex` sections (e.g., `Annex D` subsections)

**Chunk sizing rule of thumb**

* Prefer **semantic boundaries first** (clause/table/list item).
* If a clause is long, split into ~300–900 words with overlap (e.g., 50–100 words), but keep the same `ref` and add `chunk_seq`.

**Metadata you want on every chunk**

* `doc_id` (e.g., `ISO26262-6-2018`)
* `part`, `year`, `edition` (if relevant), `title` (optional)
* `ref` (clause/table identifier as printed)
* `ref_path` (hierarchy, e.g., `5 > 5.4 > 5.4.3`)
* `heading` (clause title)
* `page_pdf_start/end` (0-based PDF pages)
* `page_printed_start/end` (if you can map it)
* `type` (`clause`, `table`, …)
* `text` (for clauses), `table_md` + `table_csv` (for tables)
* `source_hash` (sha256 of PDF) so citations don’t drift

That metadata is what makes citations automatic.

---

## Why PDFs are “tricky” and how to handle it

### 1) Text-based vs scanned PDFs

**Best practice:** detect per page whether there’s extractable text.

* If text exists: use **pdfplumber** (built on pdfminer) for layout-aware extraction.
* If the page is image/scanned: OCR (Tesseract) **only for those pages**.

### 2) Headers/footers and hyphenation

Standards PDFs often have repeating headers like “ISO 26262-6:2018(E)” on every page.

**Best practice (simple + effective):**

* Collect top/bottom lines across all pages; remove lines that repeat on, say, **>60% of pages**.
* De-hyphenate line breaks (e.g., `func-` + `tion` → `function`) with conservative heuristics.

### 3) Clause numbering gets broken by layout

“5.4.3” might be separated across runs, or a title wraps weirdly.

**Best practice:** parse headings using **both**:

* regex on normalized text (`^\s*(\d+(\.\d+)*)\s+(.+)$`)
* font/size cues if available (pdfplumber exposes character objects)

### 4) Tables

Tables are the hardest.

Use a tiered approach:

**Tier A (best): Camelot / Tabula** (works if the PDF has real text lines)

* Camelot `lattice` mode: good when there are visible ruling lines
* Camelot `stream` mode: good when it’s whitespace-separated

**Tier B:** “table as text block”

* If Camelot fails, store the table region as a *verbatim-ish* text block and mark it `table_raw=true`.

**Tier C:** OCR + table detection

* Only when necessary. Much higher effort/noise. Use only for the few must-have tables.

Also: store tables as both **Markdown** (human readable) and **CSV** (machine queryable).

### 5) Don’t fight DRM/encryption

If the PDF is extraction-disabled or strongly protected:

* best practice is to request an “accessible text” copy from the publisher, or use an official portal export.
* don’t try to circumvent protections.

---

## A simple, robust architecture (local-only)

**SQLite + FTS5** is an underrated sweet spot: fast, local, portable, citeable.

* `chunks` table: canonical store of everything
* `chunks_fts` virtual table: keyword search over `text`, `heading`, `ref`

Optionally add embeddings later (FAISS/Chroma) for semantic search + reranking, but FTS alone is often enough for standards work because you typically know the vocabulary (“Table 6”, “unit verification”, “static analysis”, “shall”).

---

## Sketch: DB schema and pipeline

### SQLite schema

```sql
-- docs: one row per PDF
CREATE TABLE IF NOT EXISTS docs (
  doc_id TEXT PRIMARY KEY,
  filename TEXT NOT NULL,
  sha256 TEXT NOT NULL,
  part TEXT,
  year INTEGER,
  title TEXT
);

-- chunks: one row per extracted unit (clause/table/atom)
CREATE TABLE IF NOT EXISTS chunks (
  chunk_id TEXT PRIMARY KEY,
  doc_id TEXT NOT NULL,
  type TEXT NOT NULL,              -- clause/table/list_item/annex/...
  ref TEXT,                        -- e.g., "5.4.3", "Table 1"
  ref_path TEXT,                   -- e.g., "5>5.4>5.4.3"
  heading TEXT,
  chunk_seq INTEGER DEFAULT 0,
  page_pdf_start INTEGER,
  page_pdf_end INTEGER,
  page_printed_start TEXT,
  page_printed_end TEXT,
  text TEXT,
  table_md TEXT,
  table_csv TEXT,
  FOREIGN KEY(doc_id) REFERENCES docs(doc_id)
);

-- Full-text search index over chunk content
CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts
USING fts5(chunk_id, doc_id, ref, heading, text, content='chunks', content_rowid='rowid');

-- Triggers to keep FTS in sync are recommended (or rebuild FTS after ingest).
```

### Ingest pipeline (high level)

```
PDFs folder
  └─> identify docs + sha256
      └─> per page: extract text (pdfplumber) OR OCR if needed
          └─> clean (drop headers/footers, dehyphenate)
              └─> detect structure (clauses, annexes, tables)
                  └─> chunk + attach metadata
                      └─> store in SQLite + FTS
```

---

## Minimal working Python “sketch” (ingest + query)

This is intentionally pragmatic: it won’t perfectly reconstruct ISO’s structure on day 1, but it gets you to a usable “query + cite” loop fast.

### `ingest_iso.py`

```python
#!/usr/bin/env python3
import argparse
import hashlib
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

import pdfplumber

# Optional table extraction (install if you want it):
# pip install camelot-py[cv]
try:
    import camelot  # type: ignore
except Exception:
    camelot = None


HEADING_RE = re.compile(r"^\s*(\d+(?:\.\d+)*)\s+(.+?)\s*$")
TABLE_RE = re.compile(r"^\s*Table\s+(\d+)\s*[-–—]?\s*(.*)$", re.IGNORECASE)

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def connect_db(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    return conn

def init_db(conn: sqlite3.Connection) -> None:
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS docs (
      doc_id TEXT PRIMARY KEY,
      filename TEXT NOT NULL,
      sha256 TEXT NOT NULL,
      part TEXT,
      year INTEGER,
      title TEXT
    );

    CREATE TABLE IF NOT EXISTS chunks (
      chunk_id TEXT PRIMARY KEY,
      doc_id TEXT NOT NULL,
      type TEXT NOT NULL,
      ref TEXT,
      ref_path TEXT,
      heading TEXT,
      chunk_seq INTEGER DEFAULT 0,
      page_pdf_start INTEGER,
      page_pdf_end INTEGER,
      page_printed_start TEXT,
      page_printed_end TEXT,
      text TEXT,
      table_md TEXT,
      table_csv TEXT,
      FOREIGN KEY(doc_id) REFERENCES docs(doc_id)
    );

    CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts
    USING fts5(chunk_id, doc_id, ref, heading, text, content='chunks', content_rowid='rowid');
    """)
    conn.commit()

def normalize_text(text: str) -> str:
    # Conservative cleanup: fix hyphenation at line breaks, normalize whitespace.
    text = text.replace("\r", "\n")
    text = re.sub(r"-\n(?=[a-z])", "", text)          # func-\n tion -> function (lowercase heuristic)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def remove_repeating_headers_footers(pages_text: List[str]) -> List[str]:
    # Heuristic: identify lines that repeat across many pages and remove them.
    # Works well for standards with consistent headers/footers.
    from collections import Counter
    top_lines = []
    bottom_lines = []
    for t in pages_text:
        lines = [ln.strip() for ln in t.splitlines() if ln.strip()]
        if not lines:
            continue
        top_lines.append(lines[0])
        bottom_lines.append(lines[-1])
    c = Counter(top_lines + bottom_lines)
    threshold = max(3, int(0.6 * max(1, len(pages_text))))  # repeats on >=60% of pages
    kill = {line for line, n in c.items() if n >= threshold}

    cleaned = []
    for t in pages_text:
        lines = t.splitlines()
        kept = [ln for ln in lines if ln.strip() not in kill]
        cleaned.append("\n".join(kept))
    return cleaned

@dataclass
class Chunk:
    chunk_id: str
    doc_id: str
    type: str
    ref: Optional[str]
    ref_path: Optional[str]
    heading: Optional[str]
    chunk_seq: int
    page_pdf_start: int
    page_pdf_end: int
    text: Optional[str] = None
    table_md: Optional[str] = None
    table_csv: Optional[str] = None

def extract_pages_text(pdf_path: Path) -> List[str]:
    pages = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for page in pdf.pages:
            txt = page.extract_text() or ""
            pages.append(normalize_text(txt))
    pages = remove_repeating_headers_footers(pages)
    pages = [normalize_text(t) for t in pages]
    return pages

def build_clause_chunks(doc_id: str, pages_text: List[str]) -> List[Chunk]:
    """
    Very pragmatic parser:
    - Detect headings like "5.4.3 Some title"
    - Accumulate text until next heading
    - Store clause blocks with page ranges
    You will iterate on this for your PDFs once you see how they break.
    """
    chunks: List[Chunk] = []
    current_ref = None
    current_heading = None
    current_text_parts: List[str] = []
    start_page = 0

    def flush(end_page: int):
        nonlocal current_ref, current_heading, current_text_parts, start_page
        if current_ref is None and not current_text_parts:
            return
        body = "\n\n".join([p for p in current_text_parts if p.strip()]).strip() or None
        # Make a stable chunk id: doc + ref + page start
        ref = current_ref or f"p{start_page}"
        chunk_id = f"{doc_id}::{ref}::{start_page}"
        chunks.append(Chunk(
            chunk_id=chunk_id,
            doc_id=doc_id,
            type="clause" if current_ref else "page_block",
            ref=current_ref,
            ref_path=current_ref,
            heading=current_heading,
            chunk_seq=0,
            page_pdf_start=start_page,
            page_pdf_end=end_page,
            text=body
        ))
        current_ref = None
        current_heading = None
        current_text_parts = []
        start_page = end_page + 1

    for i, page_text in enumerate(pages_text):
        lines = page_text.splitlines()
        for ln in lines:
            m = HEADING_RE.match(ln)
            if m:
                # Found a new clause heading: flush previous
                flush(i)
                current_ref = m.group(1)
                current_heading = m.group(2)
                continue
            # Otherwise accumulate
            if ln.strip():
                current_text_parts.append(ln)

    flush(len(pages_text) - 1)
    return chunks

def try_extract_tables(doc_id: str, pdf_path: Path, max_pages: Optional[int] = None) -> List[Chunk]:
    """
    Optional table extractor. You will likely need to tune per PDF.
    Stores tables as markdown + csv and tags them as type=table.
    """
    if camelot is None:
        return []

    chunks: List[Chunk] = []
    # Camelot expects 1-based page numbers in its API
    with pdfplumber.open(str(pdf_path)) as pdf:
        n_pages = len(pdf.pages)
    n_pages = min(n_pages, max_pages) if max_pages else n_pages

    for p in range(1, n_pages + 1):
        try:
            # Try lattice first; if it fails, stream may work better.
            tables = camelot.read_pdf(str(pdf_path), pages=str(p), flavor="lattice")
            if tables.n == 0:
                tables = camelot.read_pdf(str(pdf_path), pages=str(p), flavor="stream")
        except Exception:
            continue

        for idx, t in enumerate(tables):
            df = t.df
            # crude table title detection: look near top of table (often row 0)
            maybe_title = " ".join(df.iloc[0].astype(str).tolist()).strip()
            ref = None
            heading = None
            tm = TABLE_RE.match(maybe_title)
            if tm:
                ref = f"Table {tm.group(1)}"
                heading = tm.group(2) or None

            md = df.to_markdown(index=False)
            csv = df.to_csv(index=False)

            chunk_id = f"{doc_id}::table::{p-1}::{idx}"
            chunks.append(Chunk(
                chunk_id=chunk_id,
                doc_id=doc_id,
                type="table",
                ref=ref,
                ref_path=ref,
                heading=heading,
                chunk_seq=0,
                page_pdf_start=p-1,
                page_pdf_end=p-1,
                text=None,
                table_md=md,
                table_csv=csv
            ))
    return chunks

def upsert_doc(conn: sqlite3.Connection, doc_id: str, pdf_path: Path, sha: str,
               part: Optional[str], year: Optional[int], title: Optional[str]) -> None:
    conn.execute("""
      INSERT INTO docs(doc_id, filename, sha256, part, year, title)
      VALUES(?,?,?,?,?,?)
      ON CONFLICT(doc_id) DO UPDATE SET
        filename=excluded.filename, sha256=excluded.sha256, part=excluded.part, year=excluded.year, title=excluded.title
    """, (doc_id, pdf_path.name, sha, part, year, title))

def insert_chunks(conn: sqlite3.Connection, chunks: List[Chunk]) -> None:
    conn.executemany("""
      INSERT OR REPLACE INTO chunks
      (chunk_id, doc_id, type, ref, ref_path, heading, chunk_seq, page_pdf_start, page_pdf_end,
       page_printed_start, page_printed_end, text, table_md, table_csv)
      VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, [
        (c.chunk_id, c.doc_id, c.type, c.ref, c.ref_path, c.heading, c.chunk_seq,
         c.page_pdf_start, c.page_pdf_end, None, None, c.text, c.table_md, c.table_csv)
        for c in chunks
    ])

def rebuild_fts(conn: sqlite3.Connection) -> None:
    # Rebuild FTS from chunks (simple approach)
    conn.execute("DELETE FROM chunks_fts;")
    conn.execute("""
      INSERT INTO chunks_fts(chunk_id, doc_id, ref, heading, text)
      SELECT chunk_id, doc_id, COALESCE(ref,''), COALESCE(heading,''), COALESCE(text,'')
      FROM chunks
      WHERE text IS NOT NULL AND length(text) > 0;
    """)

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf_dir", required=True)
    ap.add_argument("--db", default="iso26262_index.sqlite")
    ap.add_argument("--doc_id_prefix", default="ISO26262")
    ap.add_argument("--extract_tables", action="store_true")
    args = ap.parse_args()

    pdf_dir = Path(args.pdf_dir)
    db_path = Path(args.db)

    conn = connect_db(db_path)
    init_db(conn)

    for pdf_path in sorted(pdf_dir.glob("*.pdf")):
        sha = sha256_file(pdf_path)

        # VERY simple doc_id inference; customize to your naming scheme.
        # Example filename: ISO-26262-6-2018.pdf
        name = pdf_path.stem
        doc_id = f"{args.doc_id_prefix}::{name}"

        # Optional: parse part/year from filename
        part = None
        year = None
        m = re.search(r"26262[-_ ](\d+)[-_ ](\d{4})", name)
        if m:
            part = m.group(1)
            year = int(m.group(2))

        upsert_doc(conn, doc_id, pdf_path, sha, part, year, title=None)

        pages_text = extract_pages_text(pdf_path)
        clause_chunks = build_clause_chunks(doc_id, pages_text)

        chunks = clause_chunks
        if args.extract_tables:
            chunks += try_extract_tables(doc_id, pdf_path)

        insert_chunks(conn, chunks)
        conn.commit()

    rebuild_fts(conn)
    conn.commit()
    conn.close()
    print(f"Done. Indexed PDFs from {pdf_dir} into {db_path}")

if __name__ == "__main__":
    main()
```

### `query_iso.py`

```python
#!/usr/bin/env python3
import argparse
import sqlite3
from pathlib import Path
from textwrap import shorten

def connect_db(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn

def format_citation(row) -> str:
    # Customize to your preferred citation format
    # Example: "ISO26262::ISO-26262-6-2018, ref 5.4.3, PDF pages 31–32"
    p0 = row["page_pdf_start"]
    p1 = row["page_pdf_end"]
    pages = f"{p0}" if p0 == p1 else f"{p0}–{p1}"
    ref = row["ref"] or "(no ref)"
    return f'{row["doc_id"]}, {ref}, PDF pages {pages}'

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="iso26262_index.sqlite")
    ap.add_argument("query", nargs="+")
    ap.add_argument("--k", type=int, default=8)
    args = ap.parse_args()

    q = " ".join(args.query)

    conn = connect_db(Path(args.db))
    cur = conn.execute("""
      SELECT c.chunk_id, c.doc_id, c.ref, c.heading, c.page_pdf_start, c.page_pdf_end,
             snippet(chunks_fts, 4, '[', ']', '…', 16) AS snip
      FROM chunks_fts
      JOIN chunks c ON c.chunk_id = chunks_fts.chunk_id
      WHERE chunks_fts MATCH ?
      ORDER BY rank
      LIMIT ?;
    """, (q, args.k))

    rows = cur.fetchall()
    if not rows:
        print("No results.")
        return

    for i, r in enumerate(rows, 1):
        print(f"\n#{i}  {format_citation(r)}")
        if r["heading"]:
            print(f"    Heading: {r['heading']}")
        print(f"    {r['snip']}")

if __name__ == "__main__":
    main()
```

---

## Best practices that will save you pain later

### Keep ingestion reproducible

* Store `sha256` of each PDF and include it in citations/logs.
* Version your extraction code and DB migrations.

### Maintain a “quality loop”

Pick 10–20 known references you care about (e.g., “Table 1”, “8.4.5”, “Table 6”), then:

* run extraction
* query for them
* verify page ranges match the PDF visually
* tweak parsing heuristics until it’s stable

### Treat tables as first-class objects

* Store tables in their own chunks (type `table`)
* Add “nearby clause context” by linking tables to the closest preceding heading (optional but very useful)

### Don’t rely on only one retrieval method

* Start with **FTS exact search** (great for clause numbers, table numbers, ISO-specific terms)
* Add embeddings later if you want “find me the section about language subsets” when wording differs

### Keep outputs “citation-ready”

Your query tool should always emit:

* `doc_id + ref + pages`
* and optionally a `--open` helper you can implement later (e.g., print a command to open the PDF at that page)

### Licensing hygiene

Since these are licensed standards:

* keep the DB local/private
* avoid sharing the extracted corpus

---

## If you tell me your PDF quirks, I can tighten the parser quickly

Without you uploading anything, the most useful details are:

* Are the PDFs text-based or scanned?
* Do headings appear as `5.4.3 Title` on one line, or split?
* Are tables ruled (grid lines) or whitespace-separated?

But even without that, the approach above will get you a working local “search + cite” system you can iterate into something very reliable for drafting your coding standard.
