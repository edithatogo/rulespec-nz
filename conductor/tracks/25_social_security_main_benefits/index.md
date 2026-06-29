# Track 25 Index: Social Security Act main benefits and income tests

## Status

Active implementation track for Social Security Act 2018 main-benefit entitlement,
rate, and income-test coverage.

## Review slices

1. ACC levy and weekly compensation rules.
   - `nz/regulations/acc/earners_levy.yaml`
   - `nz/statutes/acc/weekly_compensation.yaml`
2. Jobseeker entitlement and rate rules.
   - `nz/statutes/social_security/main_benefits/entitlement.yaml`
   - `nz/statutes/social_security/main_benefits/rates.yaml`
3. Supported Living entitlement and rate rules.
   - `nz/statutes/social_security/main_benefits/entitlement.yaml`
   - `nz/statutes/social_security/main_benefits/rates.yaml`

## Notes

- Accommodation Supplement stays separate in its own surface.
- Oracle/reference comparison is captured in the local coverage manifests.
- Use the companion `.test.yaml` fixtures as the review anchor for each slice.
