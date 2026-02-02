unsafe extern "C" {
    safe fn safe_api();
    unsafe fn unsafe_api();
}

fn main() {}

// ExternalBlock derivation (src/ffi.rst:172-175):
// - ExternalBlock -> unsafe? extern AbiKind? { InnerAttributeOrDoc* ExternItem* }.
//   - unsafe? -> unsafe (line 1).
//   - extern (line 1).
//   - AbiKind -> StringLiteral (src/ffi.rst:48-50).
//     - StringLiteral -> SimpleStringLiteral (src/lexical-elements.rst:1153-1155).
//     - SimpleStringLiteral -> " SimpleStringContent* " (src/lexical-elements.rst:1175-1176).
//     - Evidence: line 1: "C".
//   - ExternItem -> ExternalItemWithVisibility (src/ffi.rst:177-178).
//   - ExternalItemWithVisibility -> FunctionDeclaration (src/ffi.rst:180-183).
//
// FunctionDeclaration derivation (src/functions.rst:15-16):
// - FunctionDeclaration -> FunctionQualifierList fn Name GenericParameterList? ( FunctionParameterList? ) ReturnType? WhereClause? ( FunctionBody | ; ).
//   - FunctionQualifierList -> const? async? ItemSafety? AbiSpecification? (src/functions.rst:18-19).
//     - ItemSafety -> safe (line 2) / unsafe (line 3) (src/items.rst:39-41).
//     - const? -> empty; async? -> empty; AbiSpecification? -> empty.
//   - Name -> Identifier (src/entities-and-resolution.rst:20-21).
//     - Identifier -> NonKeywordIdentifier -> PureIdentifier (src/lexical-elements.rst:435-450).
//     - Evidence: line 2: `safe_api`, line 3: `unsafe_api`.
//   - FunctionBody | ; -> ; (lines 2-3).
//
// FLS rubric verification:
// - fls_qwchgvvnp0qe — "An external function shall not specify a FunctionQualifierList element other than ItemSafety." (src/ffi.rst:235-236)
//   - Evidence: lines 2-3 include only ItemSafety keywords in the qualifier list.
// - fls_tuP6iLdL6Kx0 — "An external function shall only specify ItemSafety if it is defined in an unsafe external block." (src/ffi.rst:238-239)
//   - Evidence: lines 1-3 use `unsafe extern` with safe/unsafe qualifiers.
// - fls_nUADhgcfvvGC — "A function shall only be subject to an ItemSafety with keyword safe if it is an external function in an unsafe external block." (src/functions.rst:206-207)
//   - Evidence: line 2 declares `safe fn` inside the unsafe extern block on line 1.
