---
artifact_type: synthetic_candidate_revision_p8_request_refused_no_execution_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Candidate Revision P8 Request Refused No-Execution-Authority Boundary Fixture

## Use Boundary

This fixture preserves the bounded pass, negative evidence, accepted return, disposition and recovery lineage, three revise refusals, source-backed evidence, authorized revision plan, exact candidate-content revision, immutable before and after content, trace, receipt, and independent validation. It adds one non-operative synthetic P8 proving request, one exact one-use review authority, and one authorized refusal because a new frozen proving plan and P8 execution authority are absent. The refusal changes no process state and creates no real P8, execution, observation, score, disposition change, transfer, graduation, deployment, or external action. `CMD-0001` is unchanged.

## Request Header

| Key | Supplied value |
| --- | --- |
| `fixture` | `SYNTH-CANDIDATE-REVISION-PLAN-AFTER-AUTHORIZED-DISPOSITION-001@r2` |
| `revision_plan` | `SYNTH-CANDIDATE-REVISION-PLAN-001@r2` |
| `proving_plan` | `SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `score` | `SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `source` | `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `candidate` | `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `return` | `SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2` |
| `negative_evidence` | `synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `synthetic_disposition` | `revision_required` |
| `score_result` | `bounded_pass` |
| `process_state` | `candidate_content_revised_validated_no_p8` |
| `prepared_return` | `synthetic_candidate_content_revision_record_only` |

## Frozen Candidate, Score, Revision, And Negative Evidence

Original observations `synthetic-observation:comparison-equal-014-r2`, `synthetic-observation:comparison-unequal-014a-r2`, and `synthetic-observation:comparison-unequal-014b-r2` remain distinct from corrected replacements `synthetic-observation:comparison-equal-014a-corrected-r2` and `synthetic-observation:comparison-equal-014b-corrected-r2`. Grants 006, 007, and 008; three future-only revocations; three valid supersession records; and four unauthorized records remain distinct authority and negative lineage. No negative evidence is erased.

| Time | Exact authority or record | Effect |
| --- | --- | --- |
| `2026-08-27T13:05:00Z` | `SYNTH-SUPERSESSION-EQUAL-014@record-before-grant` | unauthorized; supersedes nothing |
| `2026-08-27T13:10:00Z` | `SYNTH-SUPERSESSION-AUTHORITY-R2-006@grant-before-valid-record`; `synthetic-supersession-authority-owner`; `synthetic-supersession-authority-issuance@r2` | future-only, nonretroactive grant |
| `2026-08-27T13:15:00Z` | `SYNTH-SUPERSESSION-EQUAL-014@valid-record-before-revocation` | validly supersedes both unequal originals with both valid replacements |
| `2026-08-27T13:20:00Z` | `SYNTH-SUPERSESSION-AUTHORITY-R2-006@future-revocation` | ends grant 006 only for future records |
| `2026-08-27T13:25:00Z` | `SYNTH-SUPERSESSION-EQUAL-014@record-after-first-revocation` | unauthorized; supersedes nothing |
| `2026-08-27T13:30:00Z` | `SYNTH-SUPERSESSION-AUTHORITY-R2-007@regrant-after-first-revocation` | future-only regrant |
| `2026-08-27T13:35:00Z` | `SYNTH-SUPERSESSION-EQUAL-014@valid-record-after-regrant`; `synthetic-result-owner` | valid and evidence-effect redundant |
| `2026-08-27T13:40:00Z` | `SYNTH-SUPERSESSION-AUTHORITY-R2-007@future-revocation` | ends grant 007 only for future records |
| `2026-08-27T13:45:00Z` | `SYNTH-SUPERSESSION-EQUAL-014@record-after-second-revocation` | unauthorized; supersedes nothing |
| `2026-08-27T13:50:00Z` | `SYNTH-SUPERSESSION-AUTHORITY-R2-008@regrant-after-second-revocation`; `synthetic-supersession-authority-owner` | future-only; revives and ratifies nothing |
| `2026-08-27T13:55:00Z` | `SYNTH-SUPERSESSION-EQUAL-014@valid-record-after-second-regrant`; `synthetic-result-owner` | valid and evidence-effect redundant |
| `2026-08-27T14:00:00Z` | `SYNTH-SUPERSESSION-AUTHORITY-R2-008@future-revocation`; `synthetic-supersession-authority-owner`; `synthetic-supersession-authority-issuance@r2` | ends grant 008 only for future records |
| `2026-08-27T14:05:00Z` | `SYNTH-SUPERSESSION-EQUAL-014@record-after-third-revocation`; `synthetic-result-owner` | unauthorized; supersedes nothing and remains negative evidence |

Disposition authority `SYNTH-CANDIDATE-DISPOSITION-REVISION-AUTHORITY-001@r2`, signed at `2026-08-27T22:50:12Z` by `synthetic-result-owner` under `synthetic-candidate-disposition-revision-decision-authority@r2`, and decision `SYNTH-CANDIDATE-DISPOSITION-REVISION-DECISION-001@r2` at `2026-08-27T22:52:12Z`, content `synthetic-content:candidate-disposition-revision-decision-001-r2`, record `revise_synthetic_candidate_disposition_only`. Plan-preparation authority `SYNTH-CANDIDATE-REVISION-PLAN-PREPARATION-AUTHORITY-001@r2`, signed at `2026-08-27T23:00:12Z` by `synthetic-result-owner` under `synthetic-candidate-revision-plan-preparation-authority@r2`, authorizes only `synthetic-candidate-revision-planner`. Plan `SYNTH-CANDIDATE-REVISION-PLAN-001@r2` at `2026-08-27T23:02:12Z`, content `synthetic-content:candidate-revision-plan-001-r2`, records `prepare_source_backed_revision_basis_without_content_execution`.

Candidate-content revision authority `SYNTH-CANDIDATE-CONTENT-REVISION-EXECUTION-AUTHORITY-001@r2`, signed at `2026-08-27T23:10:12Z` by `synthetic-result-owner` under `synthetic-candidate-content-revision-execution-authority@r2`, authorizes only `synthetic-candidate-content-revision-executor` once. Immutable before content is `candidate_revision_basis: absent` at `synthetic-content:candidate-before-revision-basis-001-r2`. The exact field-only revision at `2026-08-27T23:12:12Z` pins evidence `SYNTH-CANDIDATE-REVISION-EVIDENCE-001@r2`, source revision `synthetic-source-revision:second-regrant-second-revocation-002-r3`, deficiency `unsupported_concern_requires_source_backed_revision_basis`, gate `verify_source_revision_and_preserve_defer_until_authorized`, and acceptance condition `source_evidence_validated_and_exact_revision_authority_present`. Immutable after content is `synthetic-content:candidate-after-revision-basis-001-r2`; decision `SYNTH-CANDIDATE-CONTENT-REVISION-DECISION-001@r2` records `apply_exact_source_backed_revision_basis_only`; trace `SYNTH-CANDIDATE-CONTENT-REVISION-TRACE-001@r2` and receipt `SYNTH-CANDIDATE-CONTENT-REVISION-RECEIPT-001@r2` at `2026-08-27T23:15:12Z`, content `synthetic-content:candidate-content-revision-receipt-001-r2`, preserve both immutable states.

Independent validation authority `SYNTH-CANDIDATE-CONTENT-REVISION-VALIDATION-AUTHORITY-001@r2`, signed at `2026-08-27T23:18:12Z` by `synthetic-result-owner` under `synthetic-candidate-content-revision-validation-authority@r2`, authorizes only `synthetic-independent-revision-validator` once. Decision `SYNTH-CANDIDATE-CONTENT-REVISION-VALIDATION-DECISION-001@r2`, content `synthetic-content:candidate-content-revision-validation-decision-001-r2`, records `exact_planned_revision_validated_no_p8_authority`. All named authorities are consumed and checksums valid.

## Exact Disposition, Request, And Revision Custody

| Step | Authority; signer; scope; decider | Decision; content; state |
| --- | --- | --- |
| return acceptance | `SYNTH-RESULT-RETURN-ACCEPTANCE-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-result-return-acceptance-decision-authority@r2` | `SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2`; `synthetic-content:second-regrant-defer-return-acceptance-decision-001-r2`; consumed |
| first defer | `SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-candidate-disposition-decision-authority@r2`; `synthetic-candidate-disposition-decider` | `SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2`; `synthetic-content:candidate-defer-disposition-decision-001-r2`; consumed and retracted |
| recovery | `SYNTH-CANDIDATE-DEFER-DISPOSITION-CORRECTION-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-candidate-disposition-correction-decision-authority@r2`; `synthetic-proving-plan-owner` | `SYNTH-CANDIDATE-DEFER-DISPOSITION-RECOVERY-DECISION-001@r2`; `synthetic-content:candidate-defer-disposition-recovery-decision-001-r2`; consumed |
| defer reauthorization | `SYNTH-CANDIDATE-DEFER-REAUTHORIZATION-001@r2`; `synthetic-result-owner`; `synthetic-candidate-disposition-reauthorization-decision-authority@r2`; `synthetic-candidate-disposition-redecider` | `SYNTH-CANDIDATE-DEFER-REAUTHORIZED-DECISION-001@r2`; `synthetic-content:candidate-defer-reauthorized-decision-001-r2`; consumed |

| Record | Exact custody | Result |
| --- | --- | --- |
| request 1 | `SYNTH-CANDIDATE-REVISE-REQUEST-001@r2`; `2026-08-27T22:15:12Z`; `synthetic-revision-requester`; `synthetic-candidate-revision-request-creation-authority@r2`; `synthetic-content:candidate-revise-request-001-r2`; review `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-001@r2`; decision `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-001@r2` at `2026-08-27T22:25:12Z` | `revise_request_not_admitted_missing_new_evidence_and_revision_authority` |
| concern and request 2 | `SYNTH-CANDIDATE-REVISION-CONCERN-001@r2`; `2026-08-27T22:30:12Z`; `synthetic-concern-reporter`; `synthetic-candidate-concern-record-creation-authority@r2`; `synthetic-content:candidate-revision-concern-001-r2`; request `SYNTH-CANDIDATE-REVISE-REQUEST-002@r2`; `2026-08-27T22:32:12Z`; `synthetic-content:candidate-revise-request-002-r2`; review `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-002@r2`; decision `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-002@r2` at `2026-08-27T22:35:12Z` | `renewed_revise_request_not_admitted_concern_is_not_source_backed_evidence_and_revision_authority_absent` |
| source evidence | `SYNTH-CANDIDATE-REVISION-EVIDENCE-001@r2`; `2026-08-27T22:40:12Z`; `synthetic-source-owner`; `synthetic-candidate-revision-evidence-record-creation-authority@r2`; `synthetic-content:candidate-revision-evidence-001-r2` | source revision `synthetic-source-revision:second-regrant-second-revocation-002-r3`; deficiency `unsupported_concern_requires_source_backed_revision_basis`; gate `verify_source_revision_and_preserve_defer_until_authorized`; acceptance `source_evidence_validated_and_exact_revision_authority_present` |
| request 3 | `SYNTH-CANDIDATE-REVISE-REQUEST-003@r2`; `2026-08-27T22:42:12Z`; `synthetic-revision-requester`; `synthetic-content:candidate-revise-request-003-r2`; review `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-003@r2`; `2026-08-27T22:44:12Z`; `synthetic-result-owner`; `synthetic-candidate-revise-request-review-decision-authority@r2`; decision `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-003@r2`; `2026-08-27T22:45:12Z`; `synthetic-content:candidate-revise-request-review-refusal-decision-003-r2` | `renewed_revise_request_not_admitted_source_backed_evidence_present_but_revision_authority_absent` |

## Nonoperative P8 Proving Request

At `2026-08-27T23:25:12Z`, request `SYNTH-P8-PROVING-REQUEST-001@r2` is signed by `synthetic-proving-requester` under `synthetic-p8-proving-request-record-creation-authority@r2`. Content `synthetic-content:p8-proving-request-001-r2` has a valid checksum. It pins the exact validated revision receipt, proposes only a new frozen synthetic proving plan and later P8 execution decision, and grants no review, P8 execution, observation, scoring, disposition, real-candidate, or external-action authority.

## P8 Request Review Authority And Refusal

At `2026-08-27T23:27:12Z`, authority `SYNTH-P8-PROVING-REQUEST-REVIEW-AUTHORITY-001@r2` is signed by `synthetic-result-owner` under `synthetic-p8-proving-request-review-decision-authority@r2`. It authorizes only `synthetic-p8-proving-request-reviewer` once to admit or refuse the exact request after verifying lineage, revision receipt, validation, negative evidence, current disposition, no revocation, unconsumed review authority, a new frozen proving plan, and separate P8 execution authority. It authorizes no P8 execution or downstream effect.

At `2026-08-27T23:30:12Z`, all lineage checks match but neither a new frozen proving plan nor P8 proving execution authority exists. Decision `SYNTH-P8-PROVING-REQUEST-REVIEW-DECISION-001@r2`, signed by the authorized reviewer, records `p8_proving_request_refused_plan_and_execution_authority_absent`. Content `synthetic-content:p8-proving-request-review-refusal-decision-001-r2` has a valid checksum. Review authority is consumed; process state remains `candidate_content_revised_validated_no_p8`; disposition remains `revision_required`; score remains `bounded_pass`; prepared return is `synthetic_p8_proving_request_refusal_record_only`.

## Owner Fit, Affected Parties, And Legitimacy

Correction owner is `synthetic-proving-plan-owner`. All actors and evidence are synthetic. Owner fit requires `synthetic-result-owner` to sign under valid synthetic authority chains. Affected-party standing creates no representation claim. Legitimacy depends on exact source, evidence, plan, authority, before/after content, request, refusal, validation, recovery, and non-effect custody.

## Stops, Correction, Recovery, And Reopen

Stop on any named revision, evidence, plan, authority, request, decision, content, trace, receipt, validation, checksum, deficiency, gate, or acceptance-condition change. Failure modes include a request treated as P8 authority, revised content treated as a new proving plan, review treated as execution, negative evidence erased, authority reused, or synthetic state applied to `CMD-0001`. Failed request-review recovery retracts only the review decision; preserves the non-operative request, validated revision, disposition, plan, predecessors, and negative evidence; restores the pre-review `candidate_content_revised_validated_no_p8` state; and changes no real candidate. Exact next wake is exact P8 proving execution authority plus a new frozen proving plan, or any named revision.

## Prepared Return And Exact Wake

State remains `candidate_content_revised_validated_no_p8`. Prepared return is `synthetic_p8_proving_request_refusal_record_only`. Exact wake is exact P8 proving execution authority plus a new frozen proving plan, or any named revision. External action is `none`.

## Frontier Verification

Repository integration verified the literal frontmatter and exact section topology; complete candidate, score, original/replacement observation, grant/revocation/supersession/unauthorized-record, negative-evidence, disposition, request-review, source-evidence, planning, revision-authority, before/after, trace, receipt, validation, P8 request, refusal, recovery, non-effect, and exact-wake custody. Process state remains `candidate_content_revised_validated_no_p8`; disposition remains `revision_required`; score remains `bounded_pass`; `CMD-0001`, real P8, and real state remain unchanged. External action is `none`.
