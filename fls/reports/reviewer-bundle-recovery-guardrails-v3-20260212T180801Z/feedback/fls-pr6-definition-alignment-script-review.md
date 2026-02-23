# Definition-Alignment Tooling — Script Implementation Review

## Summary

41/41 smoke tests pass. The overall implementation is solid: normalization, stopwords, role prefixes, glossary extraction, chapter extraction, compound split detection, foundational placement, wave A quality gate, post-commit flow, and analyzer metrics all look correct. One critical vulnerability and two medium issues follow.

---

## 1. CRITICAL: `git_hunk_has_dt_insertion` cannot distinguish insert from swap

This is the exact vulnerability the insert diff cross-check (feedback issue #1) was designed to prevent, and it's not caught.

### The problem

`git_hunk_has_dt_insertion` (in both orchestrator and validator) scans `git show --unified=0` output for any `+` line containing `:dt:`term``:

```python
for line in result.stdout.splitlines():
    if not line.startswith("+") or line.startswith("+++"):
        continue
    if marker in line:
        return True
```

A marker swap (`:t:` → `:dt:`) produces this diff:

```
-A :t:`value` is either a literal or the result of a computation.
+A :dt:`value` is either a literal or the result of a computation.
```

The `+` line contains `:dt:`value``, so the function returns `True`. Since hunk mode is preferred over fallback, the validator never reaches the net-delta check that would have caught it (net delta = 0).

### Attack path

1. Implementer swaps `:t:` → `:dt:` (marker swap, no text insertion).
2. Declares `definition_operation=insert`.
3. Orchestrator commits, builds diff audit: `git_hunk_has_dt_insertion` returns `True`, audit records `mode=hunk`, `hunk_dt_addition=True`.
4. Validator reads audit index, sees hunk mode with `hunk_dt_addition=True`, sets `insert_pass=True`.
5. Even without the audit index, the validator's live hunk check also returns `True`.
6. The fallback net-delta check (which would catch this with `net=0`) is never reached.
7. `FAILED_INSERT_DIFF_MISMATCH` is never emitted. The swap passes as an insert.

### The smoke test doesn't cover this

The `ledger-insert-diff-mismatch-v4.csv` fixture uses `after_commit=9393733`, which is a commit that only adds `notes.rst` and doesn't touch `values.rst` at all. The hunk check returns `False` (no diff for that file), falls back to numstat (net delta = 0), and correctly fails. But this tests "file not in commit diff" — not "swap declared as insert," which is the actual attack.

### Required fix

`git_hunk_has_dt_insertion` must verify the `:dt:` line is a net addition, not a modification of an existing `:t:` line. One approach:

```python
def git_hunk_has_dt_insertion(*, workdir, commit_hash, repo_path, term):
    # ... get diff output ...
    dt_marker = f":dt:`{term}`"
    t_marker = f":t:`{term}`"
    added_lines = []
    removed_lines = []
    for line in result.stdout.splitlines():
        if line.startswith("+++") or line.startswith("---"):
            continue
        if line.startswith("+"):
            added_lines.append(line[1:])
        elif line.startswith("-"):
            removed_lines.append(line[1:])
    
    has_dt_addition = any(dt_marker in line for line in added_lines)
    has_corresponding_removal = any(t_marker in line or dt_marker in line for line in removed_lines)
    
    # True insert: :dt: added without a corresponding :t:/:dt: removal
    return has_dt_addition and not has_corresponding_removal
```

A corresponding smoke fixture is needed: a commit that changes `:t:`value`` to `:dt:`value`` on an existing line (swap), declared as `insert`, should trigger `FAILED_INSERT_DIFF_MISMATCH`.

---

## 2. MEDIUM: `jaccard_similarity` implementations diverge between writer and validator

The writer computes:

```python
def jaccard_similarity(normalized_a: str, normalized_b: str) -> float:
    tokens_a = set(normalized_a.split())
    tokens_b = set(normalized_b.split())
```

The validator computes:

```python
def jaccard_similarity(a: str, b: str) -> float:
    tokens_a = {token for token in re.split(r"\s+", a.lower().strip()) if token}
    tokens_b = {token for token in re.split(r"\s+", b.lower().strip()) if token}
```

On normalized input (already lowered, trimmed, single-spaced), these are functionally equivalent. But the plan requires exact equality between stored and recomputed similarity, and these are structurally different code paths. A future change to normalization that introduces multi-character whitespace, mixed case, or leading/trailing spaces could make them diverge, causing `FAILED_SIMILARITY_DRIFT` on valid data.

### Required fix

Make the validator's `jaccard_similarity` identical to the writer's — just `set(a.split())` / `set(b.split())`. The extra `.lower().strip()` and `re.split` are redundant on normalized input and create a maintenance risk.

---

## 3. MEDIUM: `is_subject_form_definition` is writer-only

The writer enforces subject-form definition structure (term as grammatical subject) for `promote` and `insert` operations, and for marginal `adapt`. The validator does not re-check this. If someone bypasses the writer and manually edits the ledger CSV, the subject-form check is not enforced at validation time.

The validator independently re-checks compound split (good), re-extracts definitions (good), and re-computes similarity (good). Subject form is the one structural quality check with no validation-time enforcement.

### Required fix

Add `is_subject_form_definition` to the validator alongside the existing compound split check. Apply the same enforcement logic: hard-fail for `promote`/`insert` without subject form; hard-fail for marginal `adapt` without subject form.

---

## 4. MINOR: `normalize_text_for_similarity` reuses `COMPOUND_SPLIT_STOPWORDS`

The normalization function strips `COMPOUND_SPLIT_STOPWORDS` from the token set before computing Jaccard. This means the similarity computation and the compound term detection share a stopword list. If someone adds a word to the stopword list for compound detection purposes (e.g., adding `may` to avoid false triggers on "A `:dt:`value` may be..."), it silently changes similarity computation by removing that word from all comparisons. These serve different purposes and should ideally be separate lists. Not blocking, but worth noting for future maintenance.

---

## Verification checklist

| Check | Status |
|---|---|
| Stopwords match between writer and validator | ✅ Identical (24 words) |
| RST role prefixes match | ✅ Identical |
| `strip_roles` match | ✅ Identical |
| `normalize_text_for_similarity` match | ✅ Identical |
| `split_entry_chunks` match | ✅ Identical |
| `extract_glossary_definition` logic match | ✅ Equivalent |
| `extract_chapter_definition` logic match | ✅ Equivalent |
| `first_compound_split_token` logic match | ✅ Identical |
| `jaccard_similarity` match | ⚠️ Functionally equivalent but structurally divergent |
| `is_subject_form_definition` in validator | ❌ Missing |
| `git_hunk_has_dt_insertion` distinguishes insert from swap | ❌ Does not |
| Insert diff mismatch smoke covers swap-as-insert | ❌ Only covers file-not-in-commit |
| Similarity serialization (`:.6f`) match | ✅ Both use 6 decimal places |
| Hash targets use normalized text | ✅ Both scripts |
| Post-commit flow (commit → ledger update → diff audit → validate) | ✅ Correct ordering |
| Wave A quality gate blocks Wave B | ✅ Verified |
| Analyzer reports definition alignment metrics | ✅ operation counts, similarity stats |
| All 41 smoke tests pass | ✅ |
