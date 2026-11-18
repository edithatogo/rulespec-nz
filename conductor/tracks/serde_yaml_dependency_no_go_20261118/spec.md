# Spec: remove or justify unused Serde/YAML dependencies in the Rust crate

**Date:** 18 November 2026 · **Status:** planning, not implemented.

## Source-based finding
`rulespec-nz/Cargo.toml` directly declares `serde` derive and `serde_yaml = "0.9"`; search of current Rust source `rulespec-nz/src/lib.rs` and indexed code found no `serde`/`serde_yaml` consumer. The only `serde_yaml` hits are the manifest, lockfile and archived Conductor evidence. The existing `rulespec-nz` Rust layer principally exposes Arrow/Polars and Python/WASM bridging, not parsing RuleSpec YAML. YAML ProgramSpec law/policy authoring and extraction are owned by the Axiom encoder/provider, not a new internal Rust parser.

## Decision
**Prefer removal, not parser replacement**, if exact-head `cargo tree` and feature-matrix builds confirm both direct dependencies are unused. A maintained YAML adapter is justified only after identifying an actual Rust YAML consumer with a frozen schema and authority. Do not add one solely because YAML fixtures exist in the repo. Avoid automatic source conversion or rewrites of official legislation, RuleSpec, Python or SQL. Keep state-law/source-oracle provenance independent of serialization.

## Acceptance
For any removal: compare resolved dependency graph and features, `cargo test --locked` on all enabled Rust/WASM/Python profiles, any installed Python ABI testing, audit/license reports and policy oracle fixtures. Confirm no downstream/public API expects a Serde impl. Existing law provenance, official sources, exact oracle revisions and archival status remain unchanged.
