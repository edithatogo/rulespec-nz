## Phase 0: Dependency Gate

- [ ] Confirm upstream issue #30 repo quality and CI scaffold is merged or locally reproducible.
- [ ] Confirm upstream issue #31 source-readiness manifests are available for this source family.
- [ ] Confirm upstream issue #32 oracle manifests are available for non-authoritative comparison.
- [ ] Confirm the existing main-benefits entitlement and rate modules are the correct canonical surface.
- [ ] Incorporate NLP pipeline extracts if available; otherwise proceed from official PCO/data.govt.nz citation paths.

## Phase 1: Coverage Gap Inventory

- [ ] Compare current Social Security outputs against the `social-security-main-benefits` backlog.
- [ ] Identify missing entitlement, rate, and income-test surfaces.
- [ ] Create or link the upstream tracking issue.

## Phase 2: Source Inventory

- [ ] Locate the Social Security Act provisions and any 2026 rate orders or MSD guidance.
- [ ] Record corpus citation paths or source manifests.

## Phase 3: RuleSpec Encoding

- [x] Fill main-benefit entitlement gaps.
- [x] Add rate and income-test coverage where missing.
- [x] Add partnered Supported Living Payment rate branches for superannuation/veterans cases.
- [x] Add Jobseeker partner-without-own-benefit rate branch coverage.
- [x] Add Jobseeker partner-without-own-benefit with-children rate branch coverage.
- [x] Add Jobseeker partner-ineligible with-children rate branch coverage.
- [x] Add Jobseeker partner-ineligible without-children rate branch coverage.
- [x] Add Jobseeker full-time-student ineligibility coverage.
- [x] Add Jobseeker available-for-work ineligibility coverage.
- [x] Add Jobseeker full-time-employment no-work-gap coverage.
- [x] Add Jobseeker income-cutout ineligibility coverage.
- [x] Add Jobseeker no-dependent-child age threshold coverage.
- [x] Add reciprocal residence entitlement coverage.
- [x] Add residence requirement failure coverage.
- [x] Add lawful-presence override coverage.
- [x] Add concurrent main-benefit exclusion coverage.
- [x] Add Supported Living caring-partner with-children rate branch coverage.
- [x] Add Supported Living restricted-or-blind partnered rate branch coverage.
- [x] Add Supported Living restricted-or-blind partnered with-children rate branch coverage.
- [x] Add Supported Living totally blind entitlement coverage.
- [x] Add Supported Living restricted-or-blind self-inflicted ineligibility coverage.
- [x] Add Supported Living open-employment-trial failure coverage.
- [x] Add Supported Living open-employment-trial grant-gate coverage.
- [x] Add Supported Living caring temporary-continuation ceiling coverage.
- [x] Add Supported Living caring no-direct-or-temporary-care coverage.
- [x] Add Supported Living caring with-dependent-child age threshold coverage.
- [x] Add Supported Living restricted-or-blind age threshold coverage.
- [x] Keep accommodation support separate from main-benefit logic.

## Phase 4: Tests and Upstream Packaging

- [x] Add companion `.test.yaml` fixtures.
- [x] Compare against pinned oracle/reference outputs as non-authoritative checks.
- [x] Prepare PR slice: ACC levy and weekly compensation rules.
- [x] Prepare PR slice: Jobseeker entitlement and rate rules.
- [x] Prepare PR slice: Supported Living entitlement and rate rules.
- [x] Prepare reviewable legal-content PR slices.
