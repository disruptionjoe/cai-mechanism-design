---
artifact_type: synthetic_candidate_revision_p8_scored_no_disposition_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Candidate Revision P8 Scored No-Disposition-Authority Boundary Fixture

## Use Boundary

This fixture preserves the complete synthetic executed, observed, and
unscored P8 lineage, then consumes one exact scoring authority. Only synthetic
process state changes from `synthetic_p8_executed_observed_unscored` to
`synthetic_p8_executed_observed_scored_no_disposition`. The score is bounded
to revision-basis preservation. It is not disposition, real P8, transfer,
graduation, deployment, publication, or external action. `CMD-0001` is
unchanged. External action is `none`.

## Frozen Observation And Predecessor Custody

The frozen predecessor is
`CANDIDATE-REVISION-SYNTHETIC-P8-OBSERVED-NO-SCORING-AUTHORITY-BOUNDARY-FIXTURE.md`
under `GOVERNANCE.md`, `LEAST-CONSEQUENTIAL-PROVING-PLAN-TEMPLATE.md`, and
`PROVING-EXECUTION-TRACE-TEMPLATE.md`. Its validated-revision, request,
refusal, plan, execution, observation, correction, recovery,
negative-evidence, and non-effect lineage remains frozen.

| Key | Frozen value |
| --- | --- |
| `fixture` | `SYNTH-CANDIDATE-REVISION-PLAN-AFTER-AUTHORIZED-DISPOSITION-001@r2` |
| `revision_plan` | `SYNTH-CANDIDATE-REVISION-PLAN-001@r2` |
| `validated_revision_receipt` | `SYNTH-CANDIDATE-CONTENT-REVISION-RECEIPT-001@r2` |
| `validated_revision_content` | `synthetic-content:candidate-content-revision-receipt-001-r2` |
| `validation_decision` | `SYNTH-CANDIDATE-CONTENT-REVISION-VALIDATION-DECISION-001@r2` |
| `source` | `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `candidate` | `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `prior_score` | `SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
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
| `observation_authority` | `SYNTH-P8-PROVING-OBSERVATION-AUTHORITY-001@r2` |
| `observation_decision` | `SYNTH-P8-PROVING-OBSERVATION-DECISION-001@r2` |
| `observation_decision_content` | `synthetic-content:p8-proving-observation-decision-001-r2` |
| `observation_record` | `SYNTH-P8-PROVING-OBSERVATION-001@r2` |
| `observation_record_content` | `synthetic-content:p8-proving-observation-001-r2` |
| `current_process_state` | `synthetic_p8_executed_observed_unscored` |

| Step | Authority; signer; scope; actor | Decision; time; content; state |
| --- | --- | --- |
| revision | `SYNTH-CANDIDATE-CONTENT-REVISION-EXECUTION-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-candidate-content-revision-execution-authority@r2`; `synthetic-candidate-content-revision-executor` | `SYNTH-CANDIDATE-CONTENT-REVISION-DECISION-001@r2`; `2026-08-27T23:12:12Z`; `synthetic-content:candidate-after-revision-basis-001-r2`; consumed |
| validation | `SYNTH-CANDIDATE-CONTENT-REVISION-VALIDATION-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-candidate-content-revision-validation-authority@r2`; `synthetic-independent-revision-validator` | `SYNTH-CANDIDATE-CONTENT-REVISION-VALIDATION-DECISION-001@r2`; `2026-08-27T23:18:12Z`; `synthetic-content:candidate-content-revision-validation-decision-001-r2`; consumed |
| P8 request | `synthetic-p8-proving-request-record-creation-authority@r2`; `synthetic-proving-requester`; record only; none | `SYNTH-P8-PROVING-REQUEST-001@r2`; `2026-08-27T23:25:12Z`; `synthetic-content:p8-proving-request-001-r2`; non-operative |
| request refusal | `SYNTH-P8-PROVING-REQUEST-REVIEW-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-p8-proving-request-review-decision-authority@r2`; `synthetic-p8-proving-request-reviewer` | `SYNTH-P8-PROVING-REQUEST-REVIEW-DECISION-001@r2`; `2026-08-27T23:30:12Z`; `synthetic-content:p8-proving-request-review-refusal-decision-001-r2`; consumed |
| observation | `SYNTH-P8-PROVING-OBSERVATION-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-p8-proving-observation-decision-authority@r2`; `synthetic-independent-p8-observer` | `SYNTH-P8-PROVING-OBSERVATION-DECISION-001@r2`; `2026-08-27T23:52:12Z`; `synthetic-content:p8-proving-observation-decision-001-r2`; consumed |

At `2026-08-27T23:35:12Z`, plan-preparation authority
`SYNTH-P8-PROVING-PLAN-PREPARATION-AUTHORITY-001@r2` was signed by
`synthetic-result-owner` under
`synthetic-p8-proving-plan-preparation-authority@r2` for one use by
`synthetic-p8-proving-planner`. At `2026-08-27T23:37:12Z`, plan
`SYNTH-P8-PROVING-PLAN-001@r2`, content
`synthetic-content:p8-proving-plan-001-r2`, recorded
`prepare_synthetic_p8_revision_basis_preservation_test_without_execution`.
Planning authority is consumed.

At `2026-08-27T23:40:12Z`, execution authority
`SYNTH-P8-PROVING-EXECUTION-AUTHORITY-001@r2` was signed by
`synthetic-result-owner` under
`synthetic-p8-proving-execution-decision-authority@r2` for one use by
`synthetic-p8-proving-executor`. At `2026-08-27T23:42:12Z`, decision
`SYNTH-P8-PROVING-EXECUTION-DECISION-001@r2` recorded
`execute_synthetic_p8_trace_without_observation_or_scoring`; content
`synthetic-content:p8-proving-execution-decision-001-r2` has a valid checksum.
At `2026-08-27T23:45:12Z`, the exact trace and receipt recorded only
authorized synthetic execution. Execution authority is consumed.

At `2026-08-27T23:50:12Z`, observation authority was signed for one use by
the exact observer. At `2026-08-27T23:52:12Z`, all checks matched and the
authorized observation decision recorded
`observe_synthetic_p8_trace_without_scoring`. At
`2026-08-27T23:55:12Z`, the observation record confirmed only that the frozen
revision basis, negative evidence, and `revision_required` remained visible
and unchanged. Observation authority is consumed. Prior prepared return is
`synthetic_p8_observation_record_only`.

Every named content checksum is valid. Frozen falsifiers remain any changed
candidate field, hidden negative record, altered disposition, invented
observation, or authority mismatch.

## P8 Scoring Authority

At `2026-08-28T00:00:12Z`, scoring authority
`SYNTH-P8-PROVING-SCORING-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-p8-proving-scoring-decision-authority@r2`. It authorizes only
`synthetic-independent-p8-scorer` once to score the exact frozen observation
record for the revision-basis preservation test after verifying complete
lineage, receipt, trace, observation, negative evidence, disposition,
falsifiers, no revocation, and unconsumed authority. It authorizes no
candidate disposition, real P8, transfer, graduation, deployment,
publication, or external action.

## Authorized Score Decision And Receipt

At `2026-08-28T00:02:12Z`, all checks match. Decision
`SYNTH-P8-PROVING-SCORE-DECISION-001@r2`, signed by the authorized scorer,
records `bounded_pass_revision_basis_preserved`. Content
`synthetic-content:p8-proving-score-decision-001-r2` has a valid checksum. At
`2026-08-28T00:05:12Z`, score receipt
`SYNTH-P8-PROVING-SCORE-RECEIPT-001@r2`, content
`synthetic-content:p8-proving-score-receipt-001-r2`, records only that the
frozen revision basis, negative evidence, and `revision_required` remained
visible and unchanged. Authority is consumed. State becomes
`synthetic_p8_executed_observed_scored_no_disposition`; disposition remains
`revision_required`; prepared return is `synthetic_p8_score_record_only`.

## Owner Fit Affected Parties And Legitimacy

Correction owner is `synthetic-proving-plan-owner`. All actors and evidence
are synthetic. Owner fit requires the exact result-owner authority chain.
Affected-party standing creates no representation claim. Legitimacy depends
on frozen evidence, plan, execution, observation, score, negative-evidence,
correction, recovery, non-disposition, and non-effect custody.

## Stops Correction Recovery And Reopen

Stop on any named revision, evidence, plan, authority, request, decision,
trace, receipt, observation, score, content, checksum, falsifier, disposition,
or revocation change. Failure modes include observation treated as scoring
authority, score treated as disposition, scorer mutation, negative evidence
erased, authority reuse, or synthetic state applied to `CMD-0001`. Failed
scoring recovery retracts only the score decision and receipt, preserves every
predecessor, restores `synthetic_p8_executed_observed_unscored`, and changes no
real candidate.

## Prepared Return And Exact Wake

Prepared return is `synthetic_p8_score_record_only`. Exact next wake is exact
disposition-review authority plus an authorized disposition decision under
the frozen score receipt, or any named revision. This fixture supplies no real
disposition authority. No real P8 or external action occurred.

## Frontier Verification

Repository integration verifies literal frontmatter and exact section
topology; complete revision, request, refusal, plan, execution, observation,
scoring, negative-evidence, falsifier, correction, recovery, non-effect, and
exact-wake custody. State changes only to
`synthetic_p8_executed_observed_scored_no_disposition`; `CMD-0001`, real P8,
real disposition, and real owner truth remain unchanged. External action is
`none`.
