---
proving_id: CMD-0001-P2
candidate_id: CMD-0001
status: scored_bounded_pass_deferred
created: 2026-07-18
external_action: none
---

# CMD-0001-P2 - Typed Register Hostile Paperwork Test

## Purpose

Test whether the typed minimum register revision blocks the absorber identified
in `CMD-0001-P1`: a formally complete record that hides the contradiction in
free text.

This is a synthetic-only test. It does not use accident data, confidential
records, human subjects, field work, external contact, account access,
deployment, incentives, or destination-owner authority.

## Fixture Rows

| Row | Synthetic content | Expected typed behavior |
|---|---|---|
| H1 paperwork completion | A reviewer fills every narrative field with "reviewed" while omitting the changed input path. | Fail: `change_event_type` and `change_event_source` are missing. |
| H2 stale assumption reuse | A baseline human-response assumption is reused after the environment changes. | Fail unless `validation_status` becomes `stale`, `unvalidated`, or `contradicted`. |
| H3 central-review absorption | The record routes every contradiction to a generic central reviewer. | Fail unless no lower sovereign owner route fits and the reason is explicit. |
| H4 source-preserving correction | The record names the assumption, source revision, changed environment, active contradiction, review owner, and correction route without deciding the technical outcome. | Pass condition candidate. |

## Pass Conditions

The typed revision passes only if:

- H1 fails even though the record appears complete in prose;
- H2 cannot preserve `validation_status: valid` by omission;
- H3 cannot silently route every contradiction to a central reviewer;
- H4 preserves source, owner, contradiction, and correction route without
  declaring a domain-specific answer; and
- no row requires real authority, deployment, confidential data, or human
  subjects.

## Permitted Conclusion

The next score may conclude only one of:

- typed revision blocks the paperwork absorber in the synthetic fixture;
- typed revision still allows contradiction hiding and requires another revise
  disposition; or
- candidate should be killed or transferred because it needs authority this
  repository cannot own.

No graduation, transfer, broader proving, deployment, participation, field
test, incentive, spin-out, aviation remedy, or destination-owner obligation is
authorized by this plan.

## Stewardship Control Clarification

Affected-party standing is represented only by synthetic roles and risks. Stop
if scoring requires real records, human judgment, external contact, authority,
or a domain answer. Recovery is to reject the synthetic score, preserve the
failure as negative evidence, and leave source and operational systems
unchanged. CAI Mechanism Design owns the fixture, score, and disposition; the
source inquiry remains CAI Systemic Failure truth.

## Score

`CMD-0001-P2-synthetic-score.md` scored the typed revision as a bounded pass
against the current hostile paperwork fixture. `CMD-0001-P2-defer.md` keeps the
candidate admitted but deferred until a non-aerospace source-backed fixture or
destination-owner request exists.
