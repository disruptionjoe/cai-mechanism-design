---
artifact_type: synthetic_candidate_disposition_revise_request_refused_after_defer_reauthorization_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Candidate-Disposition Revise-Request-Refused-After-Defer-Reauthorization Authority Boundary Fixture

## Use Boundary

This synthetic fixture preserves the bounded pass, accepted return, invalid
and retracted first defer, recovery, separately reauthorized defer, all
negative evidence, and current synthetic state `deferred`. It adds one request
for `revise` and one separately authorized review decision that refuses to
admit the request because there is no materially new evidence or revision
authority. A request is evidence, not an instruction. Refusal is not a new
candidate disposition, P8, proving result, real candidate change, transfer,
graduation, deployment, publication, contact, or external action. It does not
treat the request, review authority, or refusal as disposition authority.

## Decision Header

| Field | Value |
| --- | --- |
| `fixture_id` | `SYNTH-CANDIDATE-REVISE-REQUEST-REFUSED-AFTER-DEFER-REAUTHORIZATION-001@r2` |
| `decision_id` | `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-001@r2` |
| `candidate_id` | `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `source_inquiry` | `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `decision_owner` | `synthetic-result-owner` |
| `decided_by` | `synthetic-candidate-disposition-request-reviewer` |
| `decided_at` | `2026-08-27T22:25:12Z` |
| `decision_record` | `revise_request_not_admitted_missing_new_evidence_and_revision_authority` |
| `external_action` | `none` |

## Frozen Candidate And Evidence

The package freezes plan `SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`,
score `SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, the named source
and candidate, immutable trace and validation, return
`SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2`, return acceptance,
the invalid and retracted first disposition, checksum revision, correction
authority, recovery decision, defer reauthorization, and reauthorized defer.

Originals remain `synthetic-observation:comparison-equal-014-r2`,
`synthetic-observation:comparison-unequal-014a-r2`, and
`synthetic-observation:comparison-unequal-014b-r2`; replacements remain
`synthetic-observation:comparison-equal-014a-corrected-r2` and
`synthetic-observation:comparison-equal-014b-corrected-r2`. Grants 006, 007,
and 008, three future-only revocations, three valid supersession records, and
four unauthorized records remain distinct. Negative evidence remains at
`synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`.
The result remains `bounded_pass`; current synthetic state is `deferred`; only
`defer` remains supported; no real state changes.

## Consumed Authority Lineage

- return acceptance — `SYNTH-RESULT-RETURN-ACCEPTANCE-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-result-return-acceptance-decision-authority@r2`; decision `SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2`; content `synthetic-content:second-regrant-defer-return-acceptance-decision-001-r2`; consumed
- first defer — `SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-decision-authority@r2`; decider `synthetic-candidate-disposition-decider`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-decision-001-r2`; consumed and decision retracted
- recovery — `SYNTH-CANDIDATE-DEFER-DISPOSITION-CORRECTION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-correction-decision-authority@r2`; decider `synthetic-proving-plan-owner`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-RECOVERY-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-recovery-decision-001-r2`; consumed
- defer reauthorization — `SYNTH-CANDIDATE-DEFER-REAUTHORIZATION-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-reauthorization-decision-authority@r2`; decider `synthetic-candidate-disposition-redecider`; decision `SYNTH-CANDIDATE-DEFER-REAUTHORIZED-DECISION-001@r2`; content `synthetic-content:candidate-defer-reauthorized-decision-001-r2`; consumed

## Revise Request

At `2026-08-27T22:15:12Z`, request
`SYNTH-CANDIDATE-REVISE-REQUEST-001@r2` is signed by
`synthetic-revision-requester` under
`synthetic-candidate-revision-request-creation-authority@r2`. Content ID
`synthetic-content:candidate-revise-request-001-r2` has a valid checksum. It
asks to change the unchanged candidate disposition to `revise` but supplies no
materially new candidate evidence, named deficiency, correction gate, revision
acceptance condition, candidate-disposition revision authority, or authorized
revision decision. It changes no state and grants no authority.

## Decision Basis

At `2026-08-27T22:20:12Z`, review authority
`SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-candidate-revise-request-review-decision-authority@r2`. It
authorizes only `synthetic-candidate-disposition-request-reviewer` once to
record request admissibility after verifying the complete frozen lineage,
current deferred state and checksum, request and checksum, unchanged supported
disposition, absent new evidence, absent deficiency/correction/acceptance
package, absent revision authority and decision, and unconsumed review
authority. It authorizes no disposition, revision, P8, transfer, graduation,
deployment, publication, contact, or external action.

At `2026-08-27T22:25:12Z`, every check matched. Decision
`SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-001@r2` is signed by
`synthetic-candidate-disposition-request-reviewer` and records
`revise_request_not_admitted_missing_new_evidence_and_revision_authority`.
Content ID
`synthetic-content:candidate-revise-request-review-refusal-decision-001-r2`
has a valid checksum; review authority is consumed. Synthetic state remains
`deferred`; the request remains non-operative evidence; no downstream record
exists.

## Negative Evidence And Reasons

All four unauthorized records and the invalid first defer remain visible and
supersede nothing. The request supplies no new evidence, deficiency,
correction package, acceptance condition, revision authority, or decision.
Neither old authority is restored. Refusal records only that the request is
not admitted; it is neither `defer` nor `revise`. The bounded pass establishes
neither effectiveness nor destination fit.

## Owner Fit, Transfer, And Graduation Boundary

Decision owner is `synthetic-result-owner`; correction owner is
`synthetic-proving-plan-owner`; request signer is
`synthetic-revision-requester`; authorized review decider is
`synthetic-candidate-disposition-request-reviewer`. Synthetic state remains
`deferred`. No real candidate change, P8, transfer, graduation, deployment,
publication, contact, or external action exists.

## Affected Parties And Legitimacy

All standing, data, actors, evidence, authority, and systems are synthetic. No
real person, institution, affected party, or owner is represented or can be
spoken for. No authority is invented. The legitimacy risk is laundering a
non-operative request or limited review authority into real disposition or
revision authority.

## Stops, Correction, Recovery, And Reopen

Stop on any source, candidate, plan, trace, validation, authority, grant,
revocation, record, replacement, score, return, acceptance, disposition,
checksum, recovery, reauthorization, request, review, decision, or risk
revision. Failure modes include request treated as instruction, refusal
treated as `defer` or `revise`, absent authority invented, prior authority
reused, retracted evidence erased, or synthetic state applied to `CMD-0001`.
Correction belongs to `synthetic-proving-plan-owner`. Failed review recovery
retracts only the request-review decision, leaves the request non-operative,
restores unreviewed-request state, and leaves synthetic disposition `deferred`.
Exact next wake is materially new synthetic candidate evidence plus exact revision authority under frozen refused-request records, or any named revision.

## Executed Synthetic Review Decision

The signed review decision records only
`revise_request_not_admitted_missing_new_evidence_and_revision_authority`.
Review authority
`SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-001@r2` is consumed. The
request remains non-operative evidence, the first invalid defer remains
retracted negative evidence, the reauthorized defer remains current, and
synthetic state remains `deferred`. No real candidate or downstream state
changes.

## Frontier Verification

Verify the plan, source, candidate, trace, score, observations, replacements,
grants, revocations, supersession attempts, return, acceptance, invalid first
defer, checksum revision, recovery, reauthorization, current defer, request,
review authority, refusal, signers, deciders, scopes, content IDs, stops,
correction, recovery, and exact wake. Confirm no `CMD-0001` change, revision,
P8, transfer, graduation, deployment, publication, contact, or external action
exists. This section records checks completed during repository integration.
