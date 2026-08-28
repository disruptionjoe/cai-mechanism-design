---
artifact_type: synthetic_candidate_revision_p8_observed_no_scoring_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Candidate Revision P8 Observed No-Scoring-Authority Boundary Fixture

## Use Boundary

This fixture preserves the complete synthetic executed-but-unobserved P8
lineage and adds one exact one-use observation authority, one authorized
observation decision, and one observation record. Only synthetic process state
changes from `synthetic_p8_executed_unobserved_unscored` to
`synthetic_p8_executed_observed_unscored`. Observation is not scoring,
disposition, real P8, transfer, graduation, deployment, publication, or
external action. `CMD-0001` is unchanged. External action is `none`.

## Frozen Execution And Predecessor Custody

The frozen predecessor is
`CANDIDATE-REVISION-SYNTHETIC-P8-EXECUTED-NO-OBSERVATION-AUTHORITY-BOUNDARY-FIXTURE.md`
under `GOVERNANCE.md`, the least-consequential proving-plan template, and the
proving-execution trace template. Its exact return acceptance, defer,
recovery, reauthorization, three revise-request and refusal,
source-evidence, disposition-revision, revision-plan, immutable before/after,
trace, receipt, validation, negative-evidence, non-operative P8 request and
refusal, frozen P8 plan, execution authority, execution decision, correction,
recovery, and non-effect custody remain frozen.

| Key | Frozen value |
| --- | --- |
| `fixture` | `SYNTH-CANDIDATE-REVISION-PLAN-AFTER-AUTHORIZED-DISPOSITION-001@r2` |
| `revision_plan` | `SYNTH-CANDIDATE-REVISION-PLAN-001@r2` |
| `validated_revision_receipt` | `SYNTH-CANDIDATE-CONTENT-REVISION-RECEIPT-001@r2` |
| `validated_revision_content` | `synthetic-content:candidate-content-revision-receipt-001-r2` |
| `validation_decision` | `SYNTH-CANDIDATE-CONTENT-REVISION-VALIDATION-DECISION-001@r2` |
| `source` | `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `candidate` | `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `score` | `SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `negative_evidence` | `synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `synthetic_disposition` | `revision_required` |
| `p8_request` | `SYNTH-P8-PROVING-REQUEST-001@r2` |
| `p8_request_content` | `synthetic-content:p8-proving-request-001-r2` |
| `request_review_refusal` | `SYNTH-P8-PROVING-REQUEST-REVIEW-DECISION-001@r2` |
| `request_review_refusal_content` | `synthetic-content:p8-proving-request-review-refusal-decision-001-r2` |
| `p8_plan` | `SYNTH-P8-PROVING-PLAN-001@r2` |
| `p8_plan_content` | `synthetic-content:p8-proving-plan-001-r2` |
| `execution_trace` | `SYNTH-P8-PROVING-EXECUTION-TRACE-001@r2` |
| `execution_receipt` | `SYNTH-P8-PROVING-EXECUTION-RECEIPT-001@r2` |
| `execution_receipt_content` | `synthetic-content:p8-proving-execution-receipt-001-r2` |
| `current_process_state` | `synthetic_p8_executed_unobserved_unscored` |

| Step | Authority; signer; scope; actor | Decision; time; content; state |
| --- | --- | --- |
| revision | `SYNTH-CANDIDATE-CONTENT-REVISION-EXECUTION-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-candidate-content-revision-execution-authority@r2`; `synthetic-candidate-content-revision-executor` | `SYNTH-CANDIDATE-CONTENT-REVISION-DECISION-001@r2`; `2026-08-27T23:12:12Z`; `synthetic-content:candidate-after-revision-basis-001-r2`; consumed |
| validation | `SYNTH-CANDIDATE-CONTENT-REVISION-VALIDATION-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-candidate-content-revision-validation-authority@r2`; `synthetic-independent-revision-validator` | `SYNTH-CANDIDATE-CONTENT-REVISION-VALIDATION-DECISION-001@r2`; `2026-08-27T23:18:12Z`; `synthetic-content:candidate-content-revision-validation-decision-001-r2`; consumed |
| P8 request | `synthetic-p8-proving-request-record-creation-authority@r2`; `synthetic-proving-requester`; record only; none | `SYNTH-P8-PROVING-REQUEST-001@r2`; `2026-08-27T23:25:12Z`; `synthetic-content:p8-proving-request-001-r2`; non-operative |
| request refusal | `SYNTH-P8-PROVING-REQUEST-REVIEW-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-p8-proving-request-review-decision-authority@r2`; `synthetic-p8-proving-request-reviewer` | `SYNTH-P8-PROVING-REQUEST-REVIEW-DECISION-001@r2`; `2026-08-27T23:30:12Z`; `synthetic-content:p8-proving-request-review-refusal-decision-001-r2`; consumed |

At `2026-08-27T23:35:12Z`, plan-preparation authority
`SYNTH-P8-PROVING-PLAN-PREPARATION-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-p8-proving-plan-preparation-authority@r2` for one use by
`synthetic-p8-proving-planner`. At `2026-08-27T23:37:12Z`, plan
`SYNTH-P8-PROVING-PLAN-001@r2`, content
`synthetic-content:p8-proving-plan-001-r2`, records
`prepare_synthetic_p8_revision_basis_preservation_test_without_execution`.
The treatment is a reversible no-data-mutation trace. Falsifiers are any
changed candidate field, hidden negative record, altered disposition, invented
observation, or authority mismatch. Planning authority is consumed.

At `2026-08-27T23:40:12Z`, execution authority
`SYNTH-P8-PROVING-EXECUTION-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-p8-proving-execution-decision-authority@r2` for one use by
`synthetic-p8-proving-executor`. At `2026-08-27T23:42:12Z`, decision
`SYNTH-P8-PROVING-EXECUTION-DECISION-001@r2` records
`execute_synthetic_p8_trace_without_observation_or_scoring`; content
`synthetic-content:p8-proving-execution-decision-001-r2` has a valid checksum.
At `2026-08-27T23:45:12Z`, trace
`SYNTH-P8-PROVING-EXECUTION-TRACE-001@r2` and receipt
`SYNTH-P8-PROVING-EXECUTION-RECEIPT-001@r2`, content
`synthetic-content:p8-proving-execution-receipt-001-r2`, record only authorized
synthetic execution. Execution authority is consumed; the prior score remains
`bounded_pass`; disposition remains `revision_required`; and state becomes
`synthetic_p8_executed_unobserved_unscored`.

## P8 Observation Authority

At `2026-08-27T23:50:12Z`, observation authority
`SYNTH-P8-PROVING-OBSERVATION-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-p8-proving-observation-decision-authority@r2`. It authorizes only
`synthetic-independent-p8-observer` once to inspect the exact execution trace
and receipt for the frozen revision-basis preservation test. It permits one
no-data-mutation observation record: candidate revision basis remains pinned,
negative evidence remains visible, disposition remains `revision_required`,
and no unauthorized state field changed. It authorizes no scoring,
disposition, real-candidate, transfer, graduation, deployment, publication, or
external action.

## Authorized Observation Decision And Record

At `2026-08-27T23:52:12Z`, all lineage, authority, receipt, trace, checksum,
negative-evidence, disposition, falsifier, and no-revocation checks match.
Decision `SYNTH-P8-PROVING-OBSERVATION-DECISION-001@r2`, signed by the
authorized observer, records `observe_synthetic_p8_trace_without_scoring`.
Content `synthetic-content:p8-proving-observation-decision-001-r2` has a valid
checksum. At `2026-08-27T23:55:12Z`, observation record
`SYNTH-P8-PROVING-OBSERVATION-001@r2`, content
`synthetic-content:p8-proving-observation-001-r2`, records only that the frozen
revision basis, negative evidence, and `revision_required` remained visible
and unchanged. Authority is consumed. State becomes
`synthetic_p8_executed_observed_unscored`; prepared return is
`synthetic_p8_observation_record_only`.

## Owner Fit, Affected Parties, And Legitimacy

Correction owner is `synthetic-proving-plan-owner`. All actors and evidence
are synthetic. Owner fit requires the exact result-owner authority chain.
Affected-party standing creates no representation claim. Legitimacy depends
on frozen evidence, plan, execution, observation, negative-evidence,
correction, recovery, non-scoring, and non-effect custody.

## Stops, Correction, Recovery, And Reopen

Stop on any named revision, evidence, plan, authority, request, decision,
content, trace, receipt, observation, validation, checksum, falsifier,
disposition, or revocation change. Failure modes include execution treated as
observation authority, observation treated as scoring, observer mutation,
negative evidence erased, authority reuse, or synthetic state applied to
`CMD-0001`. Failed observation recovery retracts only the observation decision
and record, preserves every predecessor, restores
`synthetic_p8_executed_unobserved_unscored`, and changes no real candidate.

## Prepared Return And Exact Wake

Prepared return is `synthetic_p8_observation_record_only`. Exact next wake is
exact scoring authority plus an authorized score under the frozen observation
record, or any named revision. This fixture supplies no scoring or disposition
authority. No real P8 or external action occurred.

## Frontier Verification

Repository integration verifies literal frontmatter and exact section
topology; supplied header and custody rows; frozen predecessor, plan,
authority, decision, trace, receipt, observation, checksum, negative-evidence,
falsifier, recovery, non-effect, and exact-wake custody. State changes only to
`synthetic_p8_executed_observed_unscored`; `CMD-0001`, real P8, disposition,
and real owner truth remain unchanged. External action is `none`.
