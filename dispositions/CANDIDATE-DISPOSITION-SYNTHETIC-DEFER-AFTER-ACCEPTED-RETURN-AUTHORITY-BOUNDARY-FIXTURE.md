---
artifact_type: synthetic_candidate_disposition_defer_after_accepted_return_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Candidate-Disposition Defer-After-Accepted-Return Authority Boundary Fixture

## Use Boundary

This synthetic fixture preserves one validated three-grant `bounded_pass`, its
accepted return and bounded `defer` support, and all negative evidence. It adds
one separately authorized disposition decision that executes `defer` only for
the named unchanged synthetic candidate. It does not modify `CMD-0001`, create
`CMD-0001-P8`, transfer, graduate, deploy, publish, contact, or perform external
action, and it creates no effectiveness or destination-fit claim.

## Decision Header

| Field | Value |
| --- | --- |
| `decision_id` | `SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2` |
| `candidate_id` | `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `source_inquiry` | `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `source_revision` | `synthetic-source-revision:second-regrant-second-revocation-001-r2` |
| `decision_owner` | `synthetic-result-owner` |
| `decision_signer` | `synthetic-candidate-disposition-decider` |
| `decision_time` | `2026-08-27T21:40:12Z` |
| `external_action` | `none` |

Decision content ID is
`synthetic-content:candidate-defer-disposition-decision-001-r2`; its checksum
is valid.

## Frozen Candidate And Evidence

The package freezes plan
`SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, score
`SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, candidate
`SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, source
`SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, source revision
`synthetic-source-revision:second-regrant-second-revocation-001-r2`, immutable
trace, validation, authority lineage, negative evidence, return
`SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2`, and acceptance decision
`SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2`.

Originals are `synthetic-observation:comparison-equal-014-r2`,
`synthetic-observation:comparison-unequal-014a-r2`, and
`synthetic-observation:comparison-unequal-014b-r2`. Valid replacements are
`synthetic-observation:comparison-equal-014a-corrected-r2` and
`synthetic-observation:comparison-equal-014b-corrected-r2`. Grants 006, 007,
and 008, three future-only revocations, three valid supersession records, and
four unauthorized records remain distinct. Only the first valid record is
needed for the surviving all-`equal` effect. Negative evidence remains at
`synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`.

Return content ID `synthetic-content:second-regrant-defer-return-001-r2` and
acceptance-decision content ID
`synthetic-content:second-regrant-defer-return-acceptance-decision-001-r2` have
valid checksums. The validated result is `bounded_pass`; acceptance state is
`return_accepted_disposition_not_decided`; return-acceptance authority is
consumed. Acceptance is not disposition authority.

## Available Dispositions

Current frozen evidence supports only `defer`. It does not support kill,
revise, transfer, or a graduation proposal. Support is not execution: before
this fixture's separate decision, `defer` remained unexecuted and candidate
state remained unchanged.

## Decision Basis

At `2026-08-27T21:35:12Z`, disposition authority
`SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-candidate-disposition-decision-authority@r2`. It authorizes only
`synthetic-candidate-disposition-decider` exactly once to decide whether to
execute `defer` for the unchanged synthetic candidate after verifying source,
candidate, plan, trace, score, validation, negative evidence, return,
acceptance, owner identity, checksum, stops, correction, recovery, and
unconsumed disposition authority. It authorizes no kill, revise, transfer,
graduation proposal, P8, deployment, publication, or external action.

At `2026-08-27T21:40:12Z`, every required check matched. Decision record
`SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2` is signed by the authorized
decider under that exact authority and records `defer`. Its checksum is valid,
and the one-use disposition authority is consumed.

## Negative Evidence And Reasons

The four unauthorized records supersede nothing and remain visible at the
negative-evidence pointer. Failure modes include return acceptance treated as
disposition authority, `defer` support treated as already executed, consumed
authority reused, synthetic state applied to `CMD-0001`, or downstream effect
invented. The bounded pass and all-`equal` synthetic effect establish neither
effectiveness nor destination fit.

## Owner Fit, Transfer, And Graduation Boundary

Decision owner is `synthetic-result-owner`; correction owner is
`synthetic-proving-plan-owner`. The synthetic candidate becomes `deferred`.
No real candidate state changes. No P8, transfer, graduation proposal,
deployment, publication, contact, or external action exists. Interest,
acceptance of the proving return, and disposition authority do not establish a
destination-owner acceptance or transfer route.

## Affected Parties And Legitimacy

All standing, data, actors, evidence, authority, and systems are synthetic.
No real person, institution, affected party, or owner is represented or can
be spoken for. The legitimacy risk is laundering a bounded synthetic decision
into real candidate or external authority.

## Stops, Correction, Recovery, And Reopen

Stop on any source, candidate, plan, trace, validation, authority, grant,
revocation, record, replacement, score, return, acceptance, disposition,
checksum, or risk revision. Recovery preserves the complete lineage, score,
return, acceptance, and negative evidence; retracts only the defer decision if
its authority or checksum fails; and restores
`return_accepted_disposition_not_decided`. Exact next wake is materially new synthetic candidate evidence under frozen current records, or any named revision.

## Executed Synthetic Decision

Decision record `SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2` records
`defer` under the exact one-use authority. Decision content ID is
`synthetic-content:candidate-defer-disposition-decision-001-r2`; its checksum
is valid. The authority is consumed and synthetic candidate state becomes
`deferred`. The prior accepted return, acceptance decision, validation, and
negative evidence remain unchanged. No real candidate or downstream state is
created.

## Frontier Verification

Verify the plan, source, trace, score, all five observations, replacements,
three grants, three revocations, seven supersession attempts, timestamps,
signers, authority scopes, validation, pointers, content IDs, return,
acceptance, disposition, stops, correction, recovery, and exact wake
independently. Confirm all four unauthorized records remain negative evidence,
only the first valid record is needed, return acceptance stays separate from
disposition, and no `CMD-0001` change, P8, transfer, graduation, deployment,
publication, contact, or external action is created.
