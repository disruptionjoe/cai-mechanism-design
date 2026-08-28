---
artifact_type: synthetic_candidate_disposition_source_backed_evidence_revise_request_refused_no_revision_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Candidate-Disposition Source-Backed-Evidence Revise-Request-Refused No-Revision-Authority Boundary Fixture

## Use Boundary

This synthetic fixture preserves the bounded pass, accepted return, invalid and retracted first defer, recovery, separately reauthorized defer, both prior revise requests and refusals, the unsupported concern, all negative evidence, and current synthetic state `deferred`. It adds one source-backed evidence record and one separately authorized review decision that still refuses revision because evidence is not execution authority and revision authority remains absent. Evidence is not an instruction. Refusal is not a new candidate disposition, P8, proving result, real candidate change, transfer, graduation, deployment, publication, contact, or external action. External action is `none`. Do not modify `CMD-0001` or create P8. The result remains `bounded_pass`; only `defer` remains supported; synthetic state remains `deferred`.

## Decision Header

| Field | Value |
| --- | --- |
| `fixture_id` | `SYNTH-CANDIDATE-SOURCE-BACKED-EVIDENCE-REVISE-REQUEST-REFUSED-001@r2` |
| `decision_id` | `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-003@r2` |
| `candidate_id` | `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `source_inquiry` | `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `decision_owner` | `synthetic-result-owner` |
| `decided_by` | `synthetic-candidate-disposition-request-reviewer` |
| `decided_at` | `2026-08-27T22:45:12Z` |
| `decision_record` | `renewed_revise_request_not_admitted_source_backed_evidence_present_but_revision_authority_absent` |
| `external_action` | `none` |

## Frozen Candidate And Evidence

The fixture is frozen against `ROADMAP.md`, `proving/LEAST-CONSEQUENTIAL-PROVING-PLAN-TEMPLATE.md`, `dispositions/CANDIDATE-DISPOSITION-DECISION-TEMPLATE.md`, and `dispositions/CANDIDATE-DISPOSITION-SYNTHETIC-UNSUPPORTED-CONCERN-REVISE-REQUEST-REFUSED-NO-REVISION-AUTHORITY-BOUNDARY-FIXTURE.md`. It preserves plan `SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, score `SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, source `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, candidate `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, immutable trace and validation, return `SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2`, return acceptance, invalid first defer, checksum revision, correction, recovery, reauthorization, reauthorized defer, first request and refusal, concern, second request and refusal.

Originals remain `synthetic-observation:comparison-equal-014-r2`, `synthetic-observation:comparison-unequal-014a-r2`, and `synthetic-observation:comparison-unequal-014b-r2`; replacements remain `synthetic-observation:comparison-equal-014a-corrected-r2` and `synthetic-observation:comparison-equal-014b-corrected-r2`. Grants 006, 007, and 008, three future-only revocations, three valid supersession records, and four unauthorized records remain distinct. Negative evidence remains at `synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`. The result remains `bounded_pass`; only `defer` remains supported; no real state changes.

## Consumed Authority Lineage

- return acceptance — `SYNTH-RESULT-RETURN-ACCEPTANCE-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-result-return-acceptance-decision-authority@r2`; decision `SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2`; content `synthetic-content:second-regrant-defer-return-acceptance-decision-001-r2`; consumed
- first defer — `SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-decision-authority@r2`; decider `synthetic-candidate-disposition-decider`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-decision-001-r2`; consumed and decision retracted
- recovery — `SYNTH-CANDIDATE-DEFER-DISPOSITION-CORRECTION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-correction-decision-authority@r2`; decider `synthetic-proving-plan-owner`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-RECOVERY-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-recovery-decision-001-r2`; consumed
- defer reauthorization — `SYNTH-CANDIDATE-DEFER-REAUTHORIZATION-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-reauthorization-decision-authority@r2`; decider `synthetic-candidate-disposition-redecider`; decision `SYNTH-CANDIDATE-DEFER-REAUTHORIZED-DECISION-001@r2`; content `synthetic-content:candidate-defer-reauthorized-decision-001-r2`; consumed

The first request `SYNTH-CANDIDATE-REVISE-REQUEST-001@r2`, signed at `2026-08-27T22:15:12Z` by `synthetic-revision-requester` under `synthetic-candidate-revision-request-creation-authority@r2`, has content ID `synthetic-content:candidate-revise-request-001-r2` and a valid checksum. Review authority `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-001@r2` and refusal `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-001@r2` at `2026-08-27T22:25:12Z` are consumed; the refusal remains `revise_request_not_admitted_missing_new_evidence_and_revision_authority`.

Concern `SYNTH-CANDIDATE-REVISION-CONCERN-001@r2`, signed at `2026-08-27T22:30:12Z` by `synthetic-concern-reporter` under `synthetic-candidate-concern-record-creation-authority@r2`, has content ID `synthetic-content:candidate-revision-concern-001-r2` and a valid checksum. It remains a lead, not source-backed evidence. Second request `SYNTH-CANDIDATE-REVISE-REQUEST-002@r2`, signed at `2026-08-27T22:32:12Z` by `synthetic-revision-requester` under `synthetic-candidate-revision-request-creation-authority@r2`, has content ID `synthetic-content:candidate-revise-request-002-r2` and a valid checksum. Review authority `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-002@r2` and refusal `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-002@r2` at `2026-08-27T22:35:12Z` are consumed; the refusal remains `renewed_revise_request_not_admitted_concern_is_not_source_backed_evidence_and_revision_authority_absent`.

## Source-Backed Evidence And Renewed Revise Request

At `2026-08-27T22:40:12Z`, source-backed evidence `SYNTH-CANDIDATE-REVISION-EVIDENCE-001@r2` is signed by `synthetic-source-owner` under `synthetic-candidate-revision-evidence-record-creation-authority@r2`. Content ID `synthetic-content:candidate-revision-evidence-001-r2` has a valid checksum. It names source revision `synthetic-source-revision:second-regrant-second-revocation-002-r3`, deficiency `unsupported_concern_requires_source_backed_revision_basis`, correction gate `verify_source_revision_and_preserve_defer_until_authorized`, and acceptance condition `source_evidence_validated_and_exact_revision_authority_present`. It changes no candidate or disposition and grants no revision authority or authorized revision decision.

At `2026-08-27T22:42:12Z`, request `SYNTH-CANDIDATE-REVISE-REQUEST-003@r2` is signed by `synthetic-revision-requester` under `synthetic-candidate-revision-request-creation-authority@r2`. Content ID `synthetic-content:candidate-revise-request-003-r2` has a valid checksum. It cites the source-backed evidence but supplies no candidate-disposition revision authority and no authorized revision decision.

## Decision Basis

At `2026-08-27T22:44:12Z`, review authority `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-003@r2` is signed by `synthetic-result-owner` under `synthetic-candidate-revise-request-review-decision-authority@r2`. It authorizes only `synthetic-candidate-disposition-request-reviewer` once to verify the frozen lineage, both prior refusals, current evidence and checksum, named deficiency/correction/acceptance package, third request and checksum, current deferred state, unchanged supported disposition, absent revision authority and decision, and unconsumed review authority. It authorizes no disposition, revision, P8, transfer, graduation, deployment, publication, contact, or external action.

## Negative Evidence And Reasons

Negative evidence remains at `synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`. The unsupported concern remains a lead. The first and second refusal records remain valid and consumed. The third decision records `renewed_revise_request_not_admitted_source_backed_evidence_present_but_revision_authority_absent`. Source-backed evidence narrows the basis for a possible future correction but is neither instruction nor execution authority. Revision authority remains absent, so only the existing `defer` remains supported.

## Owner Fit, Transfer, And Graduation Boundary

Decision owner remains `synthetic-result-owner`; correction owner remains `synthetic-proving-plan-owner`. Refusal is not a new candidate disposition, P8, proving result, real candidate change, transfer, graduation, deployment, publication, contact, or external action. External action is `none`.

## Affected Parties And Legitimacy

All actors, standing, evidence, and systems are synthetic. Legitimacy derives only from the frozen evidence and exact one-use authority lineage. The review decision represents neither affected people nor any real owner. The core risk is evidence or review authority being laundered into revision authority.

## Stops, Correction, Recovery, And Reopen

Stop on any named revision. Failure modes include evidence treated as revision authority, request treated as instruction, review authority treated as disposition authority, refusal treated as `defer` or `revise`, prior authority reused, retracted evidence erased, or synthetic state applied to `CMD-0001`. Failed review recovery retracts only the third request-review decision, preserves the source-backed evidence and third request as non-operative, restores evidence-present/unreviewed state, and leaves synthetic disposition `deferred`. Exact next wake is exact candidate-disposition revision authority plus an authorized revision decision under frozen source-backed evidence-and-refusal records, or any named revision.

## Executed Synthetic Review Decision

At `2026-08-27T22:45:12Z`, every check matched. Decision `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-003@r2` is signed by `synthetic-candidate-disposition-request-reviewer` and records `renewed_revise_request_not_admitted_source_backed_evidence_present_but_revision_authority_absent`. Content ID `synthetic-content:candidate-revise-request-review-refusal-decision-003-r2` has a valid checksum; review authority is consumed. Synthetic state remains `deferred`; evidence and request remain non-operative; no downstream record exists.

## Frontier Verification

Repository integration verified the complete frozen candidate and evidence package, original and replacement observations, grants, revocations, supersessions, unauthorized records, negative evidence, consumed authority lineage, both prior requests and refusals, unsupported concern, source-backed evidence, third request, third review authority and refusal, checksums, recovery, non-effects, and exact wake. The result remains `bounded_pass`; only `defer` remains supported; synthetic state remains `deferred`; `CMD-0001`, P8, and real repository state remain unchanged.
