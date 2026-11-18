# Plan — bounded dependency disposition

- [ ] Check current repository/Conductor ownership and open PRs, reproduce the exact Cargo/features/lock baseline.
- [ ] Search all active Rust sources and generated/default feature paths for `serde` and `serde_yaml`; trace `cargo tree -i` and `cargo tree -e features`.
- [ ] If genuinely unused, remove *direct* `serde` and `serde_yaml` dependencies with isolated Rust/lock PR and qualify all supported feature targets (native/Python/WASM). Do not remove transitive crates merely to game counts.
- [ ] If a real Rust YAML consumer is discovered, instead compare maintained Serde-compatible YAML parsers with a strict corpus including duplicate keys, tags, anchors/aliases, date/number typing, malformed/hostile inputs and source/error fidelity. Record explicit adopt/defer/no-go before dependency change.
- [ ] Run exact-head builds/locked tests, Python/WASM interfaces where applicable, release/security and cross-repo Axiom RuleSpec oracle checks. The integration owner accepts or declines the change without claiming legal correctness from a serializer.
