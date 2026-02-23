# Phase 1 non-obvious placement rationale

Generated from `phase1-main-text-coverage/term-inventory.json` and annotated with
placement rationale for terms that required explicit reviewer-facing explanation.

## Method

- Placement source of truth: `phase1-main-text-coverage/term-inventory.json`
- Selection set: `code point`, `plane`, `constrain`, `implementation coherence`,
  `fundamental`, `unify`, `unifiable type` (`unifiable types` in inventory),
  `structurally equal`, `object safe`, `terminated`
- Extraction command used for generated placement rows:
  `jq -r '.[] | select(.term=="code point" or .term=="plane" or .term=="constrain" or .term=="implementation coherence" or .term=="fundamental" or .term=="unify" or .term=="unifiable types" or .term=="structurally equal" or .term=="object safe" or .term=="terminated") | [.term,.term_id,.chapter_file,.chapter_line,.glossary_line] | @tsv' phase1-main-text-coverage/term-inventory.json`
- Tie-break policy: place at the first normative chapter location; if ambiguous,
  choose the chapter with the strongest subject ownership.

## Per-term rationale

| Term | Chapter placement | Alternatives considered | Rationale |
| --- | --- | --- | --- |
| `code point` | `src/lexical-elements.rst:34` | Keep glossary-only definition; place under text/identifier chapters that only consume the concept | `code point` is a Unicode character-set primitive; lexical elements defines the character set and is the first normative place where this concept is introduced. |
| `plane` | `src/lexical-elements.rst:38` | Keep glossary-only definition; place near Unicode examples outside lexical rules | `plane` is defined in terms of Unicode code-point ranges and directly follows `code point` in the character-set subsection, keeping both foundational Unicode terms co-located. |
| `constrain` | `src/generics.rst:129` | Place in implementations chapter near `impl` legality checks | The term is specifically about how generic parameters constrain an implementation; generics is the first chapter that normatively defines parameter constraints and their legality conditions. |
| `implementation coherence` | `src/implementations.rst:139` | Place in traits/type-system chapters that mention overlap constraints | Implementations has a dedicated coherence section and the term is defined exactly where overlap validity is normatively specified. |
| `fundamental` | `src/implementations.rst:167` | Place in types-and-traits because traits/types are fundamental entities | In FLS, `fundamental` is introduced as a modifier within implementation coherence/orphan-style legality rules; implementations is the owning chapter for that rule set. |
| `unify` | `src/types-and-traits.rst:2047` | Place in expressions/patterns where unifiability is used as a requirement | `unify` is the canonical type-unification relation and needs to live with the full unification algorithm and type-compatibility rules in types-and-traits. |
| `unifiable type` (`unifiable types`) | `src/types-and-traits.rst:2058` | Keep glossary-only alias; place in patterns where usage is frequent | This term is definitional shorthand derived from `unify`; keeping it adjacent to the `unify` definition avoids split ownership between core semantics and downstream usage sites. |
| `structurally equal` | `src/types-and-traits.rst:2466` | Place in patterns due const-pattern equality checks | Structural equality is a property of types and their values; the type chapter owns the predicate definition, while pattern rules consume it. |
| `object safe` | `src/types-and-traits.rst:3147` | Place in associated-items chapter due method constraints | Object safety is a trait/type-system judgment for trait-object usability; types-and-traits contains the complete normative criteria and supporting constraints. |
| `terminated` | `src/expressions.rst:3955` | Keep glossary-only definition; place under statements/control-flow intro | `terminated` is defined as loop-expression dynamic behavior; expressions is the first normative location that defines loop runtime semantics. |

## Evidence

- Placement inventory: `phase1-main-text-coverage/term-inventory.json`
- Phase 1 notes: `phase1-main-text-coverage/notes.md`
- Phase 1 strict check: `phase1-main-text-coverage/glossary-phase1-check.json`
