#[target_feature(enable = "sse2")]
pub fn fast() {}

fn main() {
    let _f: fn() = fast;
}

// Attribute grammar derivation (src/attributes.rst:473-476):
// - TargetFeatureContent -> target_feature ( enable = " FeatureList " ).
// - FeatureList -> Feature (, Feature)* (src/attributes.rst:478-479).
// - Evidence: line 1: #[target_feature(enable = "sse2")].
//
// Coercion restriction rubric verification:
// - fls_ReYuWzijQ1aL — A safe target_feature function only coerces to a non-unsafe function pointer type when the coercion site is within a function that enables all required target features; otherwise only unsafe function pointer types are allowed (src/attributes.rst:538-542).
//   - Evidence: line 5 attempts `fn()` coercion outside a target_feature-enabled context.
//
// Expected result (negative example): rustc rejects the coercion to `fn()`.
