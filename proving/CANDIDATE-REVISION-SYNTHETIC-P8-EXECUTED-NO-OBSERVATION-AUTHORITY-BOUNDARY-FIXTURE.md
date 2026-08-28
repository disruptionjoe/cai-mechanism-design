---
artifact_type: synthetic_candidate_revision_p8_executed_no_observation_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Candidate Revision P8 Executed No-Observation-Authority Boundary Fixture

## Use Boundary

This fixture executes one synthetic P8 trace without observation or scoring
authority. It preserves the validated candidate revision, negative evidence,
`revision_required` disposition, non-operative P8 request, authorized review,
and refusal because plan and execution authority were absent. It adds one exact
frozen synthetic P8 proving plan, one exact one-use execution authority, one
authorized execution decision, one trace, and one receipt. Only synthetic
process state changes from `candidate_content_revised_validated_no_p8` to
`synthetic_p8_executed_unobserved_unscored`. Execution is not observation,
scoring, disposition, real P8, transfer, graduation, deployment, publication,
or external action. `CMD-0001` is unchanged. External action is `none`.

## Execution Header

| Key | Supplied value |
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
| `current_process_state` | `candidate_content_revised_validated_no_p8` |

## Frozen Candidate, Revision, Score, And Negative Evidence

The frozen predecessor is
`CANDIDATE-REVISION-SYNTHETIC-P8-REQUEST-REFUSED-NO-EXECUTION-AUTHORITY-BOUNDARY-FIXTURE.md`
under `GOVERNANCE.md`, the least-consequential proving-plan template,
authorization-decision template, and execution-trace template. Its exact
return-acceptance, defer, recovery, reauthorization, three revise-request and
refusal, source-evidence, disposition-revision, revision-plan, immutable
before/after, trace, receipt, validation, and negative-evidence custody remain
frozen. The request refusal remains valid history; the later plan and execution
authority do not retroactively change it.

## Exact Revision, Request, And Refusal Custody

| Step | Authority; signer; scope; actor | Decision; time; content; state |
| --- | --- | --- |
| revision | `SYNTH-CANDIDATE-CONTENT-REVISION-EXECUTION-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-candidate-content-revision-execution-authority@r2`; `synthetic-candidate-content-revision-executor` | `SYNTH-CANDIDATE-CONTENT-REVISION-DECISION-001@r2`; `2026-08-27T23:12:12Z`; `synthetic-content:candidate-after-revision-basis-001-r2`; consumed |
| validation | `SYNTH-CANDIDATE-CONTENT-REVISION-VALIDATION-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-candidate-content-revision-validation-authority@r2`; `synthetic-independent-revision-validator` | `SYNTH-CANDIDATE-CONTENT-REVISION-VALIDATION-DECISION-001@r2`; `2026-08-27T23:18:12Z`; `synthetic-content:candidate-content-revision-validation-decision-001-r2`; consumed |
| P8 request | `synthetic-p8-proving-request-record-creation-authority@r2`; `synthetic-proving-requester`; record only; none | `SYNTH-P8-PROVING-REQUEST-001@r2`; `2026-08-27T23:25:12Z`; `synthetic-content:p8-proving-request-001-r2`; non-operative |
| request refusal | `SYNTH-P8-PROVING-REQUEST-REVIEW-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-p8-proving-request-review-decision-authority@r2`; `synthetic-p8-proving-request-reviewer` | `SYNTH-P8-PROVING-REQUEST-REVIEW-DECISION-001@r2`; `2026-08-27T23:30:12Z`; `synthetic-content:p8-proving-request-review-refusal-decision-001-r2`; consumed |

## Frozen Synthetic P8 Proving Plan

At `2026-08-27T23:35:12Z`, plan-preparation authority
`SYNTH-P8-PROVING-PLAN-PREPARATION-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-p8-proving-plan-preparation-authority@r2`. It authorizes only
`synthetic-p8-proving-planner` once. At `2026-08-27T23:37:12Z`, plan
`SYNTH-P8-PROVING-PLAN-001@r2`, content
`synthetic-content:p8-proving-plan-001-r2`, records
`prepare_synthetic_p8_revision_basis_preservation_test_without_execution`.
The permitted treatment is a reversible no-data mutation trace checking that
the validated `candidate_revision_basis` remains pinned while all negative
evidence and `revision_required` remain visible. Falsifiers are any changed
candidate field, hidden negative record, altered disposition, invented
observation, or authority mismatch. Planning authority is consumed; the plan
is not execution.

## P8 Execution Authority

At `2026-08-27T23:40:12Z`, authority
`SYNTH-P8-PROVING-EXECUTION-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-p8-proving-execution-decision-authority@r2`. It authorizes only
`synthetic-p8-proving-executor` once to execute the exact frozen plan after
verifying the validated revision receipt, validation decision, negative
evidence, current disposition, request and refusal history, no revocation, and
unconsumed authority. It authorizes no observation, scoring, disposition,
real-candidate, transfer, graduation, deployment, publication, or external
action.

## Authorized Execution Decision, Trace, And Receipt

At `2026-08-27T23:42:12Z`, every required check matches. Decision
`SYNTH-P8-PROVING-EXECUTION-DECISION-001@r2`, signed by the authorized executor,
records `execute_synthetic_p8_trace_without_observation_or_scoring`. Content
`synthetic-content:p8-proving-execution-decision-001-r2` has a valid checksum.
At `2026-08-27T23:45:12Z`, trace
`SYNTH-P8-PROVING-EXECUTION-TRACE-001@r2` and receipt
`SYNTH-P8-PROVING-EXECUTION-RECEIPT-001@r2`, content
`synthetic-content:p8-proving-execution-receipt-001-r2`, record only authorized
synthetic execution. Authority is consumed. State becomes
`synthetic_p8_executed_unobserved_unscored`; disposition remains
`revision_required`; prior score remains `bounded_pass`; prepared return is
`synthetic_p8_execution_record_only`.

## Owner Fit, Affected Parties, And Legitimacy

Correction owner is `synthetic-proving-plan-owner`. All actors and evidence
are synthetic. Owner fit requires `synthetic-result-owner` to sign under the
exact authority chain. Affected-party standing creates no representation
claim. Legitimacy depends on frozen evidence, plan, authority, execution,
negative-evidence, correction, recovery, non-observation, and non-effect
custody.

## Stops, Correction, Recovery, And Reopen

Stop on any named revision, evidence, plan, authority, request, decision,
content, trace, receipt, validation, checksum, falsifier, or disposition
change. Failure modes include plan treated as authority, execution treated as
observation or scoring, negative evidence erased, authority reused, or
synthetic state applied to `CMD-0001`. Failed execution recovery retracts only
the P8 execution decision, trace, and receipt; preserves the plan, request,
refusal, validated revision, disposition, predecessors, and negative evidence;
restores `candidate_content_revised_validated_no_p8`; and changes no real
candidate.

## Prepared Return And Exact Wake

Prepared return is `synthetic_p8_execution_record_only`. Exact next wake is
exact observation authority plus an authorized observation record under the
frozen execution receipt, or any named revision. The fixture does not supply
observation or scoring authority. No real P8 or external action occurred.

## Frontier Verification

Repository integration verified literal frontmatter and exact section
topology; supplied header and custody rows; frozen predecessor, plan,
authority, decision, trace, receipt, checksum, negative-evidence, recovery,
non-effect, and exact-wake custody. State moves only from
`candidate_content_revised_validated_no_p8` to
`synthetic_p8_executed_unobserved_unscored`; `CMD-0001`, real P8, and real
owner truth remain unchanged. External action is `none`.
