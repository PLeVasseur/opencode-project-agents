# ISO 26262 Coding Standard “Seed → Grow” Plan (v2)
_(using `PLeVasseur/iso-26262-coding-standard-extraction` as the ISO knowledge base + query engine)_

This v2 incorporates:
- **Manual-audit enforcement** as a first-class enforcement path (MISRA/CERT style).
- **Rust docs Option A**: pin toolchain + snapshot **offline docs via rustup** as the baseline source.

---

## Goal
Create a set of **guideline categories** and a **TODO backlog of concrete guidelines** that:
- covers ISO 26262 “topics a coding standard must address” (starting from ISO tables/clauses as *seeds*),
- is **traceable** from ISO reference → guideline(s) → enforcement evidence,
- grows in a controlled way where each new rule is **useful** (not noise) and has **clear enforcement or audit evidence**.

---

## 0) Inputs and working assumptions
### Inputs you’ll need
- ISO 26262 PDFs you’re allowed to use internally (software-heavy parts like **Part 6** and supporting process parts like **Part 8** are usually central for coding standards).
- (Optional) PDFs or text exports of any reference coding standards you want to map against (MISRA / CERT / internal).
- A folder to store run outputs and a stable cache root (tool defaults to `.cache/iso26262`).

### Assumptions about the tool (from the repo)
- CLI tool name: **`iso26262`**
- Key commands: `inventory`, `ingest`, `embed`, `query`, `status`, `validate`
- Query supports retrieval modes **lexical / semantic / hybrid** and can return context (`--with-ancestors`, `--with-descendants`) and citations (`--with-pinpoint`).

---

## 1) Build the ISO corpus (inventory → ingest → embed)
### 1.1 Inventory: declare what PDFs exist
Purpose: produce/refresh a manifest of source PDFs so ingests are repeatable.

### 1.2 Ingest: parse PDFs into SQLite (structured nodes + chunks)
Purpose: load the PDFs into a local DB with enough structure to support “ISO clause/table driven” extraction.

Outcome:
- A SQLite DB under your cache root containing:
  - hierarchical nodes (parts/clauses/etc.)
  - extracted blocks/chunks and table structures
  - metadata needed for deterministic citations and later validation

### 1.3 Embed: enable semantic/hybrid retrieval
Purpose: accelerate concept search and similarity mapping (esp. when terms vary across ISO vs. your coding standard).

---

## 2) Extract “seeds” from ISO (table/clause-first strategy)
The most efficient way to generate categories that “look like ISO” is to start from ISO’s structured anchors:
- **tables** (often: “topics to be addressed” lists)
- **shall/should-like requirement atoms** (where available as structured nodes/chunks)

### 2.1 Create a seed manifest (anchor query list)
Keep a small, explicit list of anchor queries you always run, such as:
- `Table 1`, `Table X`, `Annex C`, `5.4.6`, etc.
- plus a handful of concept searches: “defensive programming”, “robustness”, “error handling”, “language subset”, “complexity”, etc.

This list is version-controlled and acts as your **seed manifest**.

### 2.2 Run anchor queries with structure + pinpoint
For each anchor query:
- Start in **lexical** mode for ISO anchors (tables/clause numbers).
- Add context and pinpointed citation units for later traceability.

Example patterns:
```bash
iso26262 query --query "Table 1" --retrieval-mode lexical --part 6   --type table --with-descendants --with-pinpoint --json

iso26262 query --query "defensive programming" --retrieval-mode semantic --part 6   --with-ancestors --with-pinpoint --json
```

### 2.3 Turn each hit into a seed record
For each ISO “seed hit,” capture:
- ISO reference: part + clause/table id
- Extracted “topic phrase” (short)
- Context text: enough to interpret meaning
- Initial category label (provisional)
- Notes on enforceability (tool-checkable vs manual-audit vs mixed)

Result: `seed_topics.yaml` (or JSON).

---

## 3) Convert seeds into categories + TODO guidelines
### 3.1 Build the initial category taxonomy (from seeds)
Start with categories that drop out naturally from ISO tables/clauses.

Practical starter taxonomy (tailor to your codebase + ASIL scope):
1. Complexity & structure  
2. Language subset / forbidden constructs  
3. Type safety & conversions  
4. Defensive programming & contracts  
5. Control-flow clarity  
6. Data-flow clarity (globals/aliasing/side effects)  
7. Initialization & lifetime rules  
8. Robustness & error handling  
9. Style guide & formatting  
10. Naming conventions  
11. Architecture/design principles (enforceable subset)  
12. Tooling, compliance evidence, and deviations/waivers

### 3.2 Guideline TODO template (v2: enforcement includes manual audit)
Each guideline TODO should be a structured record:

- **ID**: stable (e.g., `RUST-CTRL-001`)
- **Category**
- **Rule statement**: “shall/should” wording
- **Rationale**: ISO seed reference(s) + short defect/safety reasoning
- **Scope**: language, subsystem, ASIL, `no_std`, `unsafe`-only, etc.
- **Enforcement mode** *(required)*:
  - `AUTO` (tool-checked)
  - `AUDIT` (manual audit / review checklist)
  - `HYBRID` (tool check + audit for the residual)
- **Enforcement details**:
  - `AUTO`: which tool(s), config, and failure behavior (warn/deny)
  - `AUDIT`: audit checklist item(s), evidence requirements, reviewer role
  - `HYBRID`: what the tool covers vs. what audit must cover
- **Evidence artifact(s)**:
  - `AUTO`: CI logs, static analysis reports, lint summaries
  - `AUDIT`: review sign-off, checklist record, annotated code links, test evidence
- **Deviation process**: what is required to waive + who approves
- **Toolchain/config versions**: particularly important for Rust (`rustc`, clippy, rustfmt versions)

Result: `todo_guidelines.yaml` ready to expand.

---

## 4) “Grow” process: from seed → candidate rule → proven rule
### 4.1 The growth loop
1) **Pick a seed**
   - Use ISO pinpoint + surrounding context (`--with-ancestors/descendants`).

2) **Draft a guideline candidate**
   - One clear rule statement
   - Targeted scope
   - Define intended enforcement mode (`AUTO`, `AUDIT`, or `HYBRID`)

3) **Design enforcement**
   - If `AUTO`: prototype with rustc/clippy/rustfmt/custom lint or CI script
   - If `AUDIT`: write the checklist entry + evidence expectations
   - If `HYBRID`: explicitly list what automation catches and what humans must confirm

4) **Trial on real code**
   - Run on representative modules (esp. safety-related)
   - Measure noise, false positives, fix cost, and “real findings”
   - For `AUDIT`: run a pilot audit pass on a sample set of changes

5) **Adopt / revise / drop**
   - Adopt if it reliably reduces defect risk or ambiguity *and* has practical evidence
   - Revise if it’s unclear or too noisy
   - Drop if it’s not paying for itself

6) **Backfill traceability**
   - Update coverage matrix: ISO seed → guideline → evidence location(s)

### 4.2 How we ensure what we grow is helpful
Use explicit acceptance criteria before anything becomes “enforced”:

**Rule quality**
- Unambiguous: developers rarely argue interpretation
- Actionable: there is a clear “how to comply”
- Defect-oriented: maps to a defect class / safety failure mode / verification goal

**Evidence quality**
- `AUTO`: check is deterministic and stable across builds
- `AUDIT`: checklist is specific and produces a review record a third party can audit
- `HYBRID`: the boundary between automation vs audit is explicit

**Cost and noise**
- False positive rate is acceptable
- Remediation cost is proportional to risk reduction
- Waivers are rare and well-justified

**Lifecycle discipline**
- Rules go through states: `DRAFT → TRIAL → ENFORCED → (optional) DEPRECATED`
- `TRIAL` rules collect metrics for a defined period/number of PRs before enforcement

### 4.3 Manual-audit enforcement (how to do it “like MISRA/CERT”)
Manual-audit rules are valid and often necessary, but they must be *bounded and auditable*.

**Define an audit protocol per rule**
- What the auditor must check (specific conditions)
- What evidence is required (link to code, test results, design note)
- When it triggers (all PRs touching safety modules? only when `unsafe` used?)
- Who can sign off (role requirements; independence expectations)

**Sampling strategy**
- Prefer “trigger-based” audits over random sampling:
  - any `unsafe` block
  - FFI boundaries
  - concurrency primitives / atomics
  - numeric conversions on safety signals
  - changes to error handling paths
- For high criticality areas, use **100% audit** on triggering constructs.

**Make audits exportable**
- Store audit checklists and sign-offs in the repo (e.g., PR template + required checkboxes)
- Persist evidence summaries (e.g., `audit_records/PR-1234.md`) so audits aren’t lost in chat logs

**Keep the manual set small**
- A healthy target: the majority of rules `AUTO`, a smaller but meaningful subset `AUDIT/HYBRID`
- If the audit set grows, treat it as a signal to invest in automation or refactor patterns

### 4.4 Proving rules work (AUTO / AUDIT / HYBRID)
Every guideline should come with a small, versioned **validation set** (“guideline tests”) so you can show—concretely—that:
- the rule is **real** (it catches something meaningful),
- the enforcement path is **reliable** (tools or reviewers can consistently detect it),
- the rule is **not redundant** (e.g., an `AUDIT` rule isn’t already fully covered by clippy), and
- baseline rotations (Rust toolchain/lints) don’t silently change coverage.

This is the same idea as “negative/positive tests” for compilers and linters, but applied to your coding standard.

#### Recommended folder layout
Create one top-level folder and split by rule and enforcement mode:

```
tests/guidelines/
  README.md
  <RULE_ID>/
    metadata.yaml
    auto/
      violating.rs
      compliant.rs
      expected_tool_output.txt
    audit/
      violating.rs
      compliant.rs
      audit_steps.md
      expected_finding.md
      tool_outputs/
        clippy.txt
        rustc_warnings.txt
    hybrid/
      tool_violation.rs
      residual_violation.rs
      compliant.rs
      expected_tool_output.txt
      audit_steps.md
      expected_finding.md
      tool_outputs/
        clippy.txt
        rustc_warnings.txt
```

Notes:
- `metadata.yaml` should include: rule ID, enforcement mode, toolchain + edition, and what “pass/fail” means.
- Keep cases **minimal** and **representative** (one defect class per test).

#### What “proof” looks like for each enforcement mode

**AUTO (tool-enforced)**
- Goal: demonstrate the tool **does** catch violations and **does not** flag compliant code.
- How:
  1) Write a minimal `violating.rs` that triggers the lint/check.
  2) Write a `compliant.rs` that represents the approved pattern.
  3) Capture the exact tool output (or a stable excerpt) in `expected_tool_output.txt`.
  4) Ensure the check is deterministic in CI (same command line, same config).
- Evidence:
  - CI logs + stored expected outputs for the fixture.
- Regression signal:
  - if a toolchain bump changes whether the violation is detected, you have a concrete diff to review.

**AUDIT (manual-enforced)**
- Goal: show the rule adds coverage **beyond automation** and the checklist is usable.
- How:
  1) Design `violating.rs` so it represents a real issue and is **not reliably detected** by your current automation (the “clippy doesn’t catch it” constraint).
  2) Run automated checks and store outputs under `tool_outputs/` to demonstrate the gap.
  3) Have one or more reviewers run the audit using only `audit_steps.md` and record the finding in `expected_finding.md` (or a signed audit record).
  4) If reviewers miss it, tighten the checklist/guidance or reconsider the rule.
- Evidence:
  - captured tool outputs + a persistent audit record/checklist sign-off.

**HYBRID (tool + audit residual)**
- Goal: show exactly what automation covers and what remains for humans.
- How:
  1) Provide **two violations**:
     - `tool_violation.rs`: the case automation must catch (proves tool coverage),
     - `residual_violation.rs`: a realistic case automation does **not** catch reliably (proves audit adds value).
  2) Store tool outputs for both, and ensure the audit checklist explicitly targets the residual.
  3) Keep the boundary explicit: “tool catches X; audit checks Y.”
- Evidence:
  - tool output snapshots + audit record for the residual case.

#### Where these tests live (so they don’t pollute production)
- Prefer a small **fixture crate** in a workspace (e.g., `guideline_fixtures/`) or synthetic PRs.
- Do not rely on historical production violations as proof (those are hard to re-run deterministically).

#### Run them continuously
- Run the guideline test suite in CI:
  - on every PR (at least for `AUTO` and `HYBRID` tool portions),
  - on baseline rotations (toolchain/clippy changes),
  - periodically for audit calibration (e.g., quarterly or onboarding reviewers).
- Treat failures as a **signal**:
  - the rule is unclear,
  - the tool configuration drifted,
  - or the toolchain changed semantics.


---

## 5) Rust “freshness” (Option A: rustup offline docs + pinned toolchain)
Rust changes quickly, so you want rules to be **versioned** and evidence to be reproducible.

### 5.1 Pin the toolchain baseline
- Keep a pinned `rust-toolchain.toml` (channel + components).
- Treat toolchain upgrades as a controlled change (“baseline rotation”).

### 5.2 Snapshot the exact documentation for that toolchain (offline docs)
Use rustup to install the docs that correspond to your pinned compiler/stdlib.

Core steps:
1) Install the toolchain and docs:
```bash
rustup toolchain install <toolchain>
rustup component add rust-docs --toolchain <toolchain>
```
(You may also install `clippy` and `rustfmt` as components if your environment doesn’t include them by default.)

2) Find the local doc root path:
```bash
rustup doc --path --toolchain <toolchain>
```
`--path` prints the path to the documentation root on disk.

3) Snapshot into your repo (or an internal artifact store):
- Copy the whole doc tree (or a curated subset) from:
  - `<toolchain>/share/doc/rust/html/`
- Store under something like:
  - `docs_snapshots/rust/<toolchain>/html/...`

Benefits:
- Auditable: you can always answer “which docs did this guideline reference?”
- Consistent: matches your exact `std` and compiler behavior

### 5.3 What to snapshot first (minimum viable Rust corpus)
Start with the high-safety leverage docs (small, high value):
- Rust Reference (language rules)
- Rustonomicon (unsafe/FFI/layout/concurrency hazards)
- rustc book lints (compiler lint semantics)
- Standard library docs for the risk-heavy modules you actually use (targeted subset)

Avoid ingesting the entire stdlib docs into your PDF-first pipeline on day one; it’s huge.
Instead:
- keep the full HTML snapshot for offline lookup
- convert **selected chapters/pages** (Reference/Nomicon/lints + key std modules) into PDFs for ingestion and pinpointing

### 5.4 Enforcers are versioned APIs (record their inventories)
For each baseline rotation, capture:
- `rustc` lint inventory (e.g., `rustc -W help`)
- clippy lint inventory (and configuration in `clippy.toml` / cargo config)
- rustfmt configuration

Store:
- tool versions
- enabled lint groups
- any “deny/warn/allow” policy maps
- the resulting CI evidence output

### 5.5 Treat baseline rotation like a mini safety case update
When bumping toolchain:
1) rotate toolchain in a controlled branch
2) re-run lint inventories + capture diffs
3) re-run CI checks for all enforced rules
4) evaluate whether any rule semantics changed (esp. clippy lints)
5) update guideline metadata and evidence baselines as needed
6) record a short “baseline rotation note” (what changed and why it’s acceptable)

---

## 6) Feeding Rust docs into this query workflow (PDF-first reality)
Because your current ingestion pipeline is PDF-oriented, you have three pragmatic options:

### Option 1 (recommended early): convert curated Rust docs to PDFs and ingest
- Convert:
  - Rust Reference (chapters)
  - Nomicon
  - rustc lints pages
  - targeted std module docs
- Ingest PDFs into a separate “Rust docs” dataset or naming convention, so you can query both ISO and Rust docs with the same engine.

### Option 2: keep Rust docs as HTML snapshot + separate search
- Use local HTML search (browser search or a lightweight indexer)
- Only convert pages to PDF when you need stable citations for an audit trail

### Option 3 (longer-term): extend ingestion to accept HTML/Markdown
- Add an `inventory/ingest` path for `.html`/`.md`
- Chunk like ISO: headings become node boundaries; paragraphs become chunks; code blocks become separate chunk types
- This yields a single unified query surface.

---

## 7) Evidence + determinism: make it auditable
### 7.1 Deterministic extraction and quality gates
Use the tool’s validation steps (and CI) to keep outputs stable across runs:
- smoke tests for core extraction correctness
- benchmark query modes to ensure retrieval quality is stable
- “refresh artifacts” pipeline: ingest → embed → query → validate

### 7.2 Coverage matrix and gap report
Maintain a matrix that links:
- ISO seed reference → guideline(s) → enforcement evidence

Also produce a “gap report”:
- ISO seed has no mapped guideline coverage
- guideline exists but has no enforceable/auditable evidence defined

---

## Deliverables checklist (v2)
- `seed_topics.yaml` (ISO-derived seed set + references)
- `guideline_categories.yaml` (taxonomy)
- `todo_guidelines.yaml` (structured TODO backlog; includes enforcement mode)
- `coverage_matrix.csv` (ISO seed → guideline → evidence)
- `audit_checklists/` (markdown checklists; PR template hooks)
- `audit_records/` (persistent evidence records for audit-enforced items)
- `deviation_process.md` (waiver workflow + evidence expectations)
- Rust docs snapshot location + manifest:
  - `docs_snapshots/rust/<toolchain>/...`
  - `docs_snapshots/rust/manifest.yaml` (toolchain version, retrieval date, hashes)

---

## Appendix: example command snippets (adjust to your environment)
```bash
# Inventory ISO PDFs
iso26262 inventory --cache-root .cache/iso26262

# Ingest (example: Part 6 + Part 8)
iso26262 ingest --cache-root .cache/iso26262 --target-part 6 --target-part 8 --ocr-mode auto

# Create/refresh embeddings
iso26262 embed --cache-root .cache/iso26262 --model-id miniLM-L6-v2-local-v1

# Query: exact table anchor with context + pinpoint
iso26262 query --cache-root .cache/iso26262 --query "Table 1" --retrieval-mode lexical --part 6   --type table --with-descendants --with-pinpoint --json

# Validate quality gates
iso26262 validate --cache-root .cache/iso26262

# Rust docs snapshot (Option A)
rustup toolchain install <toolchain>
rustup component add rust-docs --toolchain <toolchain>
rustup doc --path --toolchain <toolchain>
```

---

## Resource pointers (Rust Option A baseline)
- Rust docs front page (online mirror of what rustup installs): https://doc.rust-lang.org/
- Rust Reference: https://doc.rust-lang.org/reference/
- Standard library docs: https://doc.rust-lang.org/std/
- Rustonomicon: https://doc.rust-lang.org/nomicon/
- rustc lints: https://doc.rust-lang.org/rustc/lints/
- Clippy lint list: https://doc.rust-lang.org/stable/clippy/lints.html
- rustup book (components/docs install concepts): https://rust-lang.github.io/rustup/
