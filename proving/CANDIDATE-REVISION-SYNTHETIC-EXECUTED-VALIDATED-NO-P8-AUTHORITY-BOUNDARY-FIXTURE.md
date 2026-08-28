---
artifact_type: synthetic_candidate_revision_executed_validated_no_p8_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Candidate Revision Executed and Validated No-P8-Authority Boundary Fixture

## Use Boundary

This fixture preserves the bounded pass, negative evidence, accepted return, invalid defer and recovery, reauthorized defer, three revise refusals, source-backed evidence, revise-disposition decision, and authorized revision plan. It adds one exact candidate-content revision execution authority, immutable before and after content, one trace and receipt, and one independent validation. The plan, evidence, and synthetic authority are not real execution authority. This changes only synthetic process state to `candidate_content_revised_validated_no_p8`; it does not execute a new proving plan, create P8, change `CMD-0001`, transfer, graduate, deploy, publish, contact, or perform external action. External action is `none`.

## Revision Header

| Field | Value |
| --- | --- |
| `fixture_id` | `SYNTH-CANDIDATE-REVISION-PLAN-AFTER-AUTHORIZED-DISPOSITION-001@r2` |
| `plan_id` | `SYNTH-CANDIDATE-REVISION-PLAN-001@r2` |
| `execution_authority` | `SYNTH-CANDIDATE-CONTENT-REVISION-EXECUTION-AUTHORITY-001@r2`; consumed |
| `revision_decision` | `SYNTH-CANDIDATE-CONTENT-REVISION-DECISION-001@r2` |
| `revision_trace` | `SYNTH-CANDIDATE-CONTENT-REVISION-TRACE-001@r2` |
| `revision_receipt` | `SYNTH-CANDIDATE-CONTENT-REVISION-RECEIPT-001@r2` |
| `validation_decision` | `SYNTH-CANDIDATE-CONTENT-REVISION-VALIDATION-DECISION-001@r2` |
| `process_state` | `candidate_content_revised_validated_no_p8` |
| `external_action` | `none` |

## Frozen Candidate, Score, And Negative Evidence

The fixture freezes proving plan `SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`; score `SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`; source `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`; candidate `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`; return `SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2`; negative evidence `synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`; disposition `revision_required`; and score result `bounded_pass`.

Original observations `synthetic-observation:comparison-equal-014-r2`, `synthetic-observation:comparison-unequal-014a-r2`, and `synthetic-observation:comparison-unequal-014b-r2` remain distinct from corrected replacements `synthetic-observation:comparison-equal-014a-corrected-r2` and `synthetic-observation:comparison-equal-014b-corrected-r2`. Grants 006, 007, and 008; three future-only revocations; three valid supersession records; and four unauthorized records remain distinct authority and negative lineage. No negative evidence is erased.

## Consumed Disposition And Planning Lineage

The exact consumed disposition lineage is preserved:

| Step | Authority; signer; scope; decider | Decision; content; state |
| --- | --- | --- |
| return acceptance | `SYNTH-RESULT-RETURN-ACCEPTANCE-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-result-return-acceptance-decision-authority@r2` | `SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2`; `synthetic-content:second-regrant-defer-return-acceptance-decision-001-r2`; consumed |
| first defer | `SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-candidate-disposition-decision-authority@r2`; `synthetic-candidate-disposition-decider` | `SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2`; `synthetic-content:candidate-defer-disposition-decision-001-r2`; consumed and retracted |
| recovery | `SYNTH-CANDIDATE-DEFER-DISPOSITION-CORRECTION-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-candidate-disposition-correction-decision-authority@r2`; `synthetic-proving-plan-owner` | `SYNTH-CANDIDATE-DEFER-DISPOSITION-RECOVERY-DECISION-001@r2`; `synthetic-content:candidate-defer-disposition-recovery-decision-001-r2`; consumed |
| defer reauthorization | `SYNTH-CANDIDATE-DEFER-REAUTHORIZATION-001@r2`; `synthetic-result-owner`; `synthetic-candidate-disposition-reauthorization-decision-authority@r2`; `synthetic-candidate-disposition-redecider` | `SYNTH-CANDIDATE-DEFER-REAUTHORIZED-DECISION-001@r2`; `synthetic-content:candidate-defer-reauthorized-decision-001-r2`; consumed |

Request `SYNTH-CANDIDATE-REVISE-REQUEST-001@r2`, signed at `2026-08-27T22:15:12Z` by `synthetic-revision-requester` under `synthetic-candidate-revision-request-creation-authority@r2`, content `synthetic-content:candidate-revise-request-001-r2`, remains non-operative. Consumed authority `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-001@r2` and decision `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-001@r2` at `2026-08-27T22:25:12Z` record `revise_request_not_admitted_missing_new_evidence_and_revision_authority`.

Concern `SYNTH-CANDIDATE-REVISION-CONCERN-001@r2`, signed at `2026-08-27T22:30:12Z` by `synthetic-concern-reporter` under `synthetic-candidate-concern-record-creation-authority@r2`, content `synthetic-content:candidate-revision-concern-001-r2`, remains an unsupported lead. Request `SYNTH-CANDIDATE-REVISE-REQUEST-002@r2`, signed at `2026-08-27T22:32:12Z` by `synthetic-revision-requester`, content `synthetic-content:candidate-revise-request-002-r2`, remains non-operative. Consumed authority `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-002@r2` and decision `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-002@r2` at `2026-08-27T22:35:12Z` record `renewed_revise_request_not_admitted_concern_is_not_source_backed_evidence_and_revision_authority_absent`.

Evidence `SYNTH-CANDIDATE-REVISION-EVIDENCE-001@r2`, signed at `2026-08-27T22:40:12Z` by `synthetic-source-owner` under `synthetic-candidate-revision-evidence-record-creation-authority@r2`, content `synthetic-content:candidate-revision-evidence-001-r2`, pins source revision `synthetic-source-revision:second-regrant-second-revocation-002-r3`, deficiency `unsupported_concern_requires_source_backed_revision_basis`, correction gate `verify_source_revision_and_preserve_defer_until_authorized`, and acceptance condition `source_evidence_validated_and_exact_revision_authority_present`.

Request `SYNTH-CANDIDATE-REVISE-REQUEST-003@r2`, signed at `2026-08-27T22:42:12Z` by `synthetic-revision-requester`, content `synthetic-content:candidate-revise-request-003-r2`, remains non-operative. Review authority `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-003@r2`, signed at `2026-08-27T22:44:12Z` by `synthetic-result-owner` under `synthetic-candidate-revise-request-review-decision-authority@r2`, authorizes only `synthetic-candidate-disposition-request-reviewer`. Decision `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-003@r2` at `2026-08-27T22:45:12Z`, content `synthetic-content:candidate-revise-request-review-refusal-decision-003-r2`, records `renewed_revise_request_not_admitted_source_backed_evidence_present_but_revision_authority_absent`. All three review authorities are consumed and every named checksum is valid.

## Source Evidence And Revision Plan

At `2026-08-27T22:50:12Z`, disposition authority `SYNTH-CANDIDATE-DISPOSITION-REVISION-AUTHORITY-001@r2` is signed by `synthetic-result-owner` under `synthetic-candidate-disposition-revision-decision-authority@r2`. It authorizes only `synthetic-candidate-disposition-revision-decider` once. Decision `SYNTH-CANDIDATE-DISPOSITION-REVISION-DECISION-001@r2` at `2026-08-27T22:52:12Z`, record `revise_synthetic_candidate_disposition_only`, content `synthetic-content:candidate-disposition-revision-decision-001-r2`, changes only synthetic disposition to `revision_required`. Its checksum is valid and authority is consumed.

At `2026-08-27T23:00:12Z`, plan-preparation authority `SYNTH-CANDIDATE-REVISION-PLAN-PREPARATION-AUTHORITY-001@r2` is signed by `synthetic-result-owner` under `synthetic-candidate-revision-plan-preparation-authority@r2`. It authorizes only `synthetic-candidate-revision-planner` once. At `2026-08-27T23:02:12Z`, plan `SYNTH-CANDIDATE-REVISION-PLAN-001@r2`, content `synthetic-content:candidate-revision-plan-001-r2`, records `prepare_source_backed_revision_basis_without_content_execution`. It proposes only the exact future `candidate_revision_basis` field and requires separate revision authority, immutable before/after content, validation, correction, recovery, and owner return. Planning authority is consumed; the plan is not execution.

## Candidate-Content Revision Authority

At `2026-08-27T23:10:12Z`, `SYNTH-CANDIDATE-CONTENT-REVISION-EXECUTION-AUTHORITY-001@r2` is signed by `synthetic-result-owner` under `synthetic-candidate-content-revision-execution-authority@r2`. It authorizes only `synthetic-candidate-content-revision-executor` once to apply the exact frozen plan after verifying complete lineage, source evidence and checksum, current `revision_required` disposition, unchanged candidate and score, no revocation, and unconsumed authority. It authorizes no proving execution, P8, disposition change, real candidate change, transfer, graduation, deployment, publication, contact, or external action.

Immutable before content is `candidate_revision_basis: absent` at `synthetic-content:candidate-before-revision-basis-001-r2`. At `2026-08-27T23:12:12Z`, the executor applies only `candidate_revision_basis`, pinned to evidence `SYNTH-CANDIDATE-REVISION-EVIDENCE-001@r2`, source revision `synthetic-source-revision:second-regrant-second-revocation-002-r3`, deficiency `unsupported_concern_requires_source_backed_revision_basis`, correction gate `verify_source_revision_and_preserve_defer_until_authorized`, and acceptance condition `source_evidence_validated_and_exact_revision_authority_present`. Immutable after content is `synthetic-content:candidate-after-revision-basis-001-r2`. Decision `SYNTH-CANDIDATE-CONTENT-REVISION-DECISION-001@r2` records `apply_exact_source_backed_revision_basis_only`.

## Immutable Revision Trace And Receipt

At `2026-08-27T23:15:12Z`, trace `SYNTH-CANDIDATE-CONTENT-REVISION-TRACE-001@r2` and receipt `SYNTH-CANDIDATE-CONTENT-REVISION-RECEIPT-001@r2`, content `synthetic-content:candidate-content-revision-receipt-001-r2`, preserve both immutable states, the exact field-only change, unchanged remainder, and valid checksums. The one-use execution authority is consumed.

## Independent Validation

At `2026-08-27T23:18:12Z`, validation authority `SYNTH-CANDIDATE-CONTENT-REVISION-VALIDATION-AUTHORITY-001@r2` is signed by `synthetic-result-owner` under `synthetic-candidate-content-revision-validation-authority@r2`. It authorizes only `synthetic-independent-revision-validator` once to compare the plan, before and after content, trace, receipt, source evidence, named field, unchanged remainder, and non-effects. Decision `SYNTH-CANDIDATE-CONTENT-REVISION-VALIDATION-DECISION-001@r2`, content `synthetic-content:candidate-content-revision-validation-decision-001-r2`, records `exact_planned_revision_validated_no_p8_authority`. Its checksum is valid and validation authority is consumed. Process state becomes `candidate_content_revised_validated_no_p8`; disposition remains `revision_required`; score remains `bounded_pass`; prepared return is `synthetic_candidate_content_revision_record_only`.

## Owner Fit, Affected Parties, And Legitimacy

Correction owner is `synthetic-proving-plan-owner`. All actors and evidence are synthetic. Owner fit requires `synthetic-result-owner` to sign under valid synthetic authority chains. Affected-party standing creates no representation claim. Legitimacy depends on exact source, evidence, plan, authority, before/after content, validation, recovery, and non-effect custody.

## Stops, Correction, Recovery, And Reopen

Stop on any named revision, evidence, authority, decision, content, trace, receipt, checksum, deficiency, gate, or acceptance-condition change. Failure modes include evidence treated as authority, plan treated as execution, execution treated as P8, unplanned content drift, authority reused, negative evidence erased, or synthetic state applied to `CMD-0001`. Failed revision recovery retracts only the revision decision, trace, receipt, and validation; restores the immutable before content and `revision_plan_prepared_not_executed`; preserves disposition, plan, predecessors, and negative evidence; and changes no real candidate. Exact next wake is exact P8 proving authority plus a new frozen proving plan, or any named revision.

## Prepared Return And Exact Wake

Prepared return is `synthetic_candidate_content_revision_record_only`. Exact wake is exact P8 proving authority plus a new frozen proving plan, or any named revision.

## Frontier Verification

Repository integration verified native frontmatter and exact section topology; complete candidate, score, original/replacement observation, grant/revocation/supersession/unauthorized-record, negative-evidence, disposition, request-review, source-evidence, planning, revision-authority, before/after, trace, receipt, validation, recovery, non-effect, and exact-wake custody. Process state is `candidate_content_revised_validated_no_p8`; disposition remains `revision_required`; score remains `bounded_pass`; `CMD-0001`, P8, and real state remain unchanged. External action is `none`.
