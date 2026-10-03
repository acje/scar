---
name: scar-rust
description: Review Rust domain construction and safe-client unsafe contracts.
---
# Rust subject profile

## Applicability
Use for Rust source/API/build surfaces. First read actual repository rules, toolchain and verification entry points. Record which rules bind; techniques below are provisional where no local rule is adopted.

## Techniques
1. Name the true domain invariant and caller boundary. Inventory literals/fields, constructors/builders, Default, conversions, deserialization and mutation, including defining-module routes; show valid and invalid boundary cases.
2. Prefer enums with variant-specific data when the domain has exclusive alternatives. Preserve genuine optionality and independent booleans; do not invent constraints.
3. Inventory unsafe functions/blocks/traits/implementations/FFI and safe callbacks. Trace every safe-client route against the unsafe contract; seek a safe caller that can trigger undefined behavior.
4. Run declared crate tests/lints and relevant downstream/API tests under local policy; distinguish compiler evidence from soundness reasoning. For async/resource changes obtain scoped limits, ownership/cancellation/shutdown evidence before asserting bounds.

## Evidence and output
Record source/toolchain identity, loaded local policy, construction-route witnesses, contract obligations, targeted test commands/exits and unexamined surfaces. Combine core with security or maintainability where applicable.

## Limitations
Compiler success does not prove unsafe soundness. This profile is not a universal dependency/MSRV/resource policy or comment mandate. Fleet-specific no-non-doc-comment rules bind only when applicable caller policy says so; Google comment advice cannot silently override them. Missing budgets/checks stay Unknown.

## Sources
[Rust Book: enums](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html), Defining an Enum and The Option Enum; [Rustonomicon](https://doc.rust-lang.org/nomicon/safe-unsafe-meaning.html), How Safe and Unsafe Interact; [audit](../../SOURCE-AUDIT.md) N7–N8. Route inventory/resource check selection are author adaptations, not quotations.
