# Language-Specific Coding Standard - Pieces of ISO 26262 That are Important

If you’re drafting a **language-specific coding standard** “for ISO 26262”, the places you’ll keep coming back to are the clauses/tables where ISO 26262:

1. **requires/defines coding & modelling guidelines**,
2. **defines code-level design principles**, and
3. **defines how you prove compliance** (reviews/static analysis/testing/coverage + tool confidence).

Below is the “map” I typically use.

## Part 6 (software) — the core hooks for a coding standard

### 1) Language selection + “coding guidelines must cover these topics”

* **ISO 26262-6:2018, 5.4.2** — criteria for selecting a modelling/design/programming language (unambiguous definition, supports modularity/abstraction/encapsulation, structured constructs, etc.). ([Kekaoxing][1])
* **ISO 26262-6:2018, 5.4.3 + Table 1** — *the* key table for your coding standard: it says criteria not covered by the language itself must be covered by guidelines, and **Table 1 lists the topics**. ([Kekaoxing][1])
  Table 1 topics you should explicitly map into chapters/rules:

  * **Low complexity**
  * **Language subsets**
  * **Strong typing**
  * **Defensive implementation techniques**
  * **Well-trusted design principles**
  * **Unambiguous graphical representation** (if models are used)
  * **Style guides**
  * **Naming conventions**
  * **Concurrency aspects** ([Kekaoxing][1])
* **ISO 26262-6:2018, 5.5.1** — work product: *Documentation of the software development environment* (this is where your coding standard is normally referenced/controlled as part of the environment). ([Kekaoxing][1])

### 2) Code-level “design principles” to translate into language rules

* **ISO 26262-6:2018, 8.4.5 + Table 6** — design principles “at the source code level” (single entry/exit, rules about dynamic objects, initialization, globals, pointers, implicit conversions, jumps, recursion, etc.). This table is a direct seed for language-specific “shall/shall not” rules. ([Kekaoxing][1])

### 3) Proving adherence (your coding standard must be *auditable*)

* **ISO 26262-6:2018, 9.4.2 + Table 7** — methods for software unit verification, including **static code analysis**, control/data flow analysis, inspections, etc. (i.e., how you’ll enforce your coding rules). ([Kekaoxing][1])
* **ISO 26262-6:2018, 9.4.4 + Table 9** — structural coverage expectations at unit level (statement/branch/MC/DC), which often drives “what code constructs are acceptable” and how you test them. ([Kekaoxing][1])

### 4) Integration + system-level software testing (still impacts coding rules)

* **ISO 26262-6:2018, 10.4.2 + Table 10** — software integration verification methods (again includes static code analysis, control/data flow checks, etc.). ([Kekaoxing][1])
* **ISO 26262-6:2018, 10.4.5 + Table 12** — structural coverage at the software architectural level (function/call coverage). ([Kekaoxing][1])
* **ISO 26262-6:2018, 11.4 + Tables 13–15** — embedded software testing environments and test methods (HIL, ECU network envs, etc.). ([Kekaoxing][1])

### 5) Annexes that often drive “special” coding rules

* **Annex B (Model-based development approaches)** — if you use models/auto-codegen, your “coding standard” may need a model-style standard too. ([Kekaoxing][1])
* **Annex C (normative) Software configuration** — relevant if your language/environment uses configuration/calibration mechanisms that affect code generation/behavior. ([Kekaoxing][1])
* **Annex D (Freedom from interference between software elements)** — very relevant if you have mixed-ASIL / partitioning / concurrency concerns; it’s a common source for rules around timing, shared resources, communication, etc. ([Kekaoxing][1])

## Part 8 (supporting processes) — make the coding standard “usable in a safety case”

These clauses are what auditors expect you to have around the coding standard: versioning, change control, verification planning, and tool confidence.

* **ISO 26262-8:2018, Clause 7/8/10** — configuration management, change management, documentation management (your coding standard must be baselined, versioned, and change-controlled). ([Kekaoxing][2])
* **ISO 26262-8:2018, Clause 9** — verification planning/specification/execution structure (ties directly into “how do we check coding rule compliance?”). ([Kekaoxing][2])
* **ISO 26262-8:2018, Clause 11 (Tools)** — essential if you rely on linters/static analyzers/compilers/code generators to enforce rules:

  * **Table 3** (determine Tool Confidence Level) ([Kekaoxing][2])
  * **Table 4 & Table 5** (qualification methods for TCL3/TCL2 tools) ([Kekaoxing][2])
* **ISO 26262-8:2018, Clause 12** — qualification of software components (impacts “which libs/frameworks are allowed under the coding standard”). ([Kekaoxing][2])

## Part 2 (management) — where the coding standard becomes planned evidence

* **ISO 26262-2:2018, 6.4.6 (Safety plan)** — you plan the use of methods/guidelines/tools and how compliance will be shown. ([Kekaoxing][3])
* **ISO 26262-2:2018, 6.4.7.2** — requires work products in the safety plan to be under configuration/change management and documentation (ties back to Part 8 clauses 7/8/10). ([Kekaoxing][3])
* **ISO 26262-2:2018, 6.4.8 (Safety case)** — where “coding standard + compliance evidence” ends up. ([Kekaoxing][3])
* **ISO 26262-2:2018, 6.4.13 (Release for production)** — requires the safety case and evidence before release; practically, this is where coding-standard compliance gets checked as “done”. ([Kekaoxing][3])

## Part 9 (ASIL tailoring & analyses) — when your coding standard must support independence/FFI

If you rely on **ASIL decomposition**, **coexistence**, **freedom from interference**, etc., you’ll want these:

* **ISO 26262-9:2018, Clause 5** — ASIL decomposition requirements (including “sufficient independence” expectations). ([Kekaoxing][4])
* **ISO 26262-9:2018, Clause 7** — dependent failure analysis (explicitly references independence / freedom from interference requirements and change management). ([Kekaoxing][4])

---

### Practical tip for drafting the coding standard

A clean way to make auditors happy is to add an appendix that **maps your chapters/rules to ISO 26262-6 Table 1 and Table 6**, and a second mapping to **your enforcement evidence** (reviews/static analysis/tests/coverage per Tables 7–12 + tool confidence per ISO 26262-8 Clause 11). ([Kekaoxing][1])

[1]: https://www.kekaoxing.com/wp-content/uploads/standard/ISO26262-2018/ISO-26262-6-2018.pdf "ISO 26262-6:2018"
[2]: https://www.kekaoxing.com/wp-content/uploads/standard/ISO26262-2018/ISO-26262-8-2018.pdf "ISO 26262-8:2018"
[3]: https://www.kekaoxing.com/wp-content/uploads/standard/ISO26262-2018/ISO-26262-2-2018.pdf "ISO 26262-2:2018"
[4]: https://www.kekaoxing.com/wp-content/uploads/standard/ISO26262-2018/ISO-26262-9-2018.pdf "ISO 26262-9:2018"
