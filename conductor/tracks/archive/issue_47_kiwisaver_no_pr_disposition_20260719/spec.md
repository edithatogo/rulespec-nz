# Specification: Issue 47 KiwiSaver No-PR Disposition

## Purpose

Create a retrospective, evidence-backed Conductor record for fork issue #47.
The record must explain why no code pull request was required without inventing
an association between issue #47 and any historical pull request.

## Scope

- Identify the audited fork `main` commit and current KiwiSaver module blob.
- Verify that `5e67c161a9a00a6d2b45b09fddb3b9371974bf6d` is in current history.
- Verify that historical proposal commit
  `ecdc2e30d9c6bff6a4e8ed52d4395d79cd3c88da` is not in current history.
- Record the current indexed parameter representation and relevant hosted checks.
- Record the current reusable-validation limitation separately from disposition.

## Non-goals

- No RuleSpec implementation changes.
- No pull request association for the superseded historical proposal.
- No upstream repository changes, issue updates, or review dependencies.
- No claim that the current reusable validation workflow is fully green.

## Acceptance Criteria

- The evidence ledger cites immutable commit, blob, issue, check-run, and job URLs.
- The metadata says `pull_request_disposition: no_pr_required` and has no
  implementation PR field.
- The plan is complete and the registry links to this archived track.
- Conductor setup and full validation pass locally.
