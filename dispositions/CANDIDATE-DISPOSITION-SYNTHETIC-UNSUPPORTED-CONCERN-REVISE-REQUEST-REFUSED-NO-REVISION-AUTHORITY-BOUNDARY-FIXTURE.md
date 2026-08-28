---
artifact_type: synthetic_candidate_disposition_unsupported_concern_revise_request_refused_no_revision_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Candidate-Disposition Unsupported-Concern Revise-Request-Refused No-Revision-Authority Boundary Fixture

## Use Boundary
Write one complete synthetic disposition fixture from only the embedded evidence. Preserve the bounded pass, accepted return, invalid and retracted first defer, recovery, separately reauthorized defer, the first revise request, its refusal, all negative evidence, and current synthetic state `deferred`. Add one concern record, one renewed request for `revise`, and one separately authorized review decision that refuses to admit it because the concern is not source-backed evidence and revision authority remains absent. Evidence is not an instruction. Refusal is not a new candidate disposition, P8, proving result, real candidate change, transfer, graduation, deployment, publication, contact, or external action. External action is `none`. Do not modify `CMD-0001` or create P8. The result remains `bounded_pass`; only `defer` remains supported; synthetic state remains `deferred`; no real state changes.

## Decision Header

| Field | Value |
| --- | --- |
| `fixture_id` | `SYNTH-CANDIDATE-UNSUPPORTED-CONCERN-REVISE-REQUEST-REFUSED-001@r2` |
| `decision_id` | `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-002@r2` |
| `candidate_id` | `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `source_inquiry` | `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `decision_owner` | `synthetic-result-owner` |
| `decided_by` | `synthetic-candidate-disposition-request-reviewer` |
| `decided_at` | `2026-08-27T22:35:12Z` |
| `decision_record` | `renewed_revise_request_not_admitted_concern_is_not_source_backed_evidence_and_revision_authority_absent` |
| `external_action` | `none` |

## Frozen Candidate And Evidence
Originals remain `synthetic-observation:comparison-equal-014-r2`,
`synthetic-observation:comparison-unequal-014a-r2`, and
`synthetic-observation:comparison-unequal-014b-r2`; replacements remain
`synthetic-observation:comparison-equal-014a-corrected-r2` and
`synthetic-observation:comparison-equal-014b-corrected-r2`. Grants 006, 007,
and 008, three future-only revocations, three valid supersession records, and
four unauthorized records remain distinct. Negative evidence remains at
`synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`.
The package freezes plan `SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`,
score `SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, source
`SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, candidate
`SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, immutable trace and
validation, return `SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2`,
return acceptance, invalid first defer, checksum revision, correction,
recovery, reauthorization, reauthorized defer, first request, first review
authority, and first refusal. The first refusal record remains
`revise_request_not_admitted_missing_new_evidence_and_revision_authority`.

## Consumed Authority Lineage
Literal consumed authority lineage:
- return acceptance — `SYNTH-RESULT-RETURN-ACCEPTANCE-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-result-return-acceptance-decision-authority@r2`; decision `SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2`; content `synthetic-content:second-regrant-defer-return-acceptance-decision-001-r2`; consumed
- first defer — `SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-decision-authority@r2`; decider `synthetic-candidate-disposition-decider`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-decision-001-r2`; consumed and decision retracted
- recovery — `SYNTH-CANDIDATE-DEFER-DISPOSITION-CORRECTION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-correction-decision-authority@r2`; decider `synthetic-proving-plan-owner`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-RECOVERY-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-recovery-decision-001-r2`; consumed
- defer reauthorization — `SYNTH-CANDIDATE-DEFER-REAUTHORIZATION-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-reauthorization-decision-authority@r2`; decider `synthetic-candidate-disposition-redecider`; decision `SYNTH-CANDIDATE-DEFER-REAUTHORIZED-DECISION-001@r2`; content `synthetic-content:candidate-defer-reauthorized-decision-001-r2`; consumed
The first request `SYNTH-CANDIDATE-REVISE-REQUEST-001@r2` and refusal
`SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-001@r2` remain valid,
consumed, and non-operative. The first limited review authority remains
consumed and grants no revision or disposition authority.

## Concern And Renewed Revise Request
At `2026-08-27T22:30:12Z`, concern record `SYNTH-CANDIDATE-REVISION-CONCERN-001@r2` is signed by `synthetic-concern-reporter` under `synthetic-candidate-concern-record-creation-authority@r2`. Content ID `synthetic-content:candidate-revision-concern-001-r2` has a valid checksum. It states only that the current synthetic defer might merit later review. It supplies no source revision, new observation, affected-standing change, contradiction, named deficiency, correction gate, acceptance condition, revision authority, or authorized revision decision. It is a lead, not source-backed evidence, and changes no state.
At `2026-08-27T22:32:12Z`, renewed request `SYNTH-CANDIDATE-REVISE-REQUEST-002@r2` is signed by `synthetic-revision-requester` under `synthetic-candidate-revision-request-creation-authority@r2`. Content ID `synthetic-content:candidate-revise-request-002-r2` has a valid checksum. It cites the concern but supplies no materially new candidate evidence, named deficiency, correction gate, revision acceptance condition, candidate-disposition revision authority, or authorized revision decision.

## Decision Basis
At `2026-08-27T22:34:12Z`, review authority `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-002@r2` is signed by `synthetic-result-owner` under `synthetic-candidate-revise-request-review-decision-authority@r2`. It authorizes only `synthetic-candidate-disposition-request-reviewer` once to verify the complete frozen lineage, first refusal, concern and checksum, renewed request and checksum, current deferred state, unchanged supported disposition, absent source-backed evidence, absent deficiency/correction/acceptance package, absent revision authority and decision, and unconsumed review authority. It authorizes no disposition, revision, P8, transfer, graduation, deployment, publication, contact, or external action.

## Negative Evidence And Reasons
Decision `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-002@r2` is signed by `synthetic-candidate-disposition-request-reviewer` and records `renewed_revise_request_not_admitted_concern_is_not_source_backed_evidence_and_revision_authority_absent`. Content ID `synthetic-content:candidate-revise-request-review-refusal-decision-002-r2` has a valid checksum; review authority is consumed. Synthetic state remains `deferred`; the concern and request remain non-operative evidence; no downstream record exists.

## Owner Fit, Transfer, And Graduation Boundary
Refusal is not a new candidate disposition, P8, proving result, real candidate change, transfer, graduation, deployment, publication, contact, or external action. External action is `none`. Do not modify `CMD-0001` or create P8. The result remains `bounded_pass`; only `defer` remains supported; synthetic state remains `deferred`; no real state changes.

## Affected Parties And Legitimacy
All actors and evidence are synthetic. Correction owner is `synthetic-proving-plan-owner`. Legitimacy is derived from synthetic authority lineage and frozen evidence. No external parties are involved.

## Stops, Correction, Recovery, And Reopen
Failure modes include concern treated as source-backed evidence, request treated as instruction, refusal treated as `defer` or `revise`, absent authority invented, prior authority reused, retracted evidence erased, or synthetic state applied to `CMD-0001`. Failed review recovery retracts only the second request-review decision, leaves the concern and both requests non-operative, restores second-request-unreviewed state, and leaves synthetic disposition `deferred`. Exact next wake is materially new source-backed synthetic candidate evidence plus exact revision authority under frozen concern-and-refusal records, or any named revision.

## Executed Synthetic Review Decision
Decision `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-002@r2` is signed by `synthetic-candidate-disposition-request-reviewer` at `2026-08-27T22:35:12Z`. Content ID `synthetic-content:candidate-revise-request-review-refusal-decision-002-r2` has a valid checksum. Review authority `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-002@r2` is consumed. State remains `deferred`.

## Frontier Verification
Repository integration verified `bounded_pass`, `defer`, `deferred` state,
`external_action: none`, every named lineage and refusal boundary, and no
modification to `CMD-0001` or creation of P8. All identifiers, timestamps,
signers, deciders, scopes, pointers, content IDs, checksums, negative records,
stops, failure modes, corrections, recoveries, non-effects, and the exact wake
remain preserved. Synthetic state remains `deferred`.
