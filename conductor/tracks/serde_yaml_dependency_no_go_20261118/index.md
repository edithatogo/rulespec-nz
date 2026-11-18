# Serde/YAML dependency disposition

[Specification](spec.md) · [Plan](plan.md) · [Metadata](metadata.json)

No source or dependency migration has been performed. The Rust crate appears to have no actual Serde/YAML consumer; eliminate direct dependencies after feature and downstream confirmation, rather than installing another YAML parser.
