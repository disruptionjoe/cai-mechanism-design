---
artifact_type: synthetic_candidate_disposition_revision_plan_authorized_no_content_revision_or_p8_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Candidate-Disposition Revision-Plan Authorized No-Content-Revision-or-P8-Authority Boundary Fixture

## Use Boundary

This synthetic fixture preserves a bounded pass, accepted return, invalid and retracted first defer, recovery, separately reauthorized defer, three refused revise requests, unsupported concern, source-backed evidence, all negative evidence, and an exact authorized revise-disposition decision. It adds one exact one-use revision-plan preparation authority and one non-operative revision plan. Synthetic process state becomes `revision_plan_prepared_not_executed`; disposition remains `revision_required`; candidate content and score remain unchanged. No proving execution, P8, real candidate change, transfer, graduation, deployment, publication, contact, or external action occurs. External action is `none`.

## Plan Header

| Field | Value |
| --- | --- |
| `fixture_id` | `SYNTH-CANDIDATE-REVISION-PLAN-AFTER-AUTHORIZED-DISPOSITION-001@r2` |
| `plan_id` | `SYNTH-CANDIDATE-REVISION-PLAN-001@r2` |
| `candidate_id` | `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `plan_prepared_at` | `2026-08-27T23:02:12Z` |
| `plan_prepared_by` | `synthetic-candidate-revision-planner` |
| `plan_content_id` | `synthetic-content:candidate-revision-plan-001-r2`; checksum valid |
| `process_state` | `revision_plan_prepared_not_executed` |
| `synthetic_disposition` | `revision_required` |
| `external_action` | `none` |

## Frozen Candidate, Score, And Negative Evidence

The fixture is frozen against `ROADMAP.md`, `proving/LEAST-CONSEQUENTIAL-PROVING-PLAN-TEMPLATE.md`, `dispositions/CANDIDATE-DISPOSITION-DECISION-TEMPLATE.md`, and `dispositions/CANDIDATE-DISPOSITION-SYNTHETIC-REVISE-AUTHORIZED-AFTER-SOURCE-BACKED-EVIDENCE-NO-P8-AUTHORITY-BOUNDARY-FIXTURE.md`. Proving plan `SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, score `SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, source `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, candidate `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, immutable trace and validation, return `SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2`, and negative evidence `synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` remain unchanged. Score result remains `bounded_pass`.

Originals `synthetic-observation:comparison-equal-014-r2`, `synthetic-observation:comparison-unequal-014a-r2`, and `synthetic-observation:comparison-unequal-014b-r2`; replacements `synthetic-observation:comparison-equal-014a-corrected-r2` and `synthetic-observation:comparison-equal-014b-corrected-r2`; grants 006, 007, and 008; three future-only revocations; three valid supersession records; and four unauthorized records remain distinct negative and authority evidence. No record is reduced to a count or erased.

## Consumed Disposition Authority Lineage

- return acceptance — `SYNTH-RESULT-RETURN-ACCEPTANCE-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-result-return-acceptance-decision-authority@r2`; decision `SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2`; content `synthetic-content:second-regrant-defer-return-acceptance-decision-001-r2`; consumed
- first defer — `SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-decision-authority@r2`; decider `synthetic-candidate-disposition-decider`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-decision-001-r2`; consumed and decision retracted
- recovery — `SYNTH-CANDIDATE-DEFER-DISPOSITION-CORRECTION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-correction-decision-authority@r2`; decider `synthetic-proving-plan-owner`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-RECOVERY-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-recovery-decision-001-r2`; consumed
- defer reauthorization — `SYNTH-CANDIDATE-DEFER-REAUTHORIZATION-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-reauthorization-decision-authority@r2`; decider `synthetic-candidate-disposition-redecider`; decision `SYNTH-CANDIDATE-DEFER-REAUTHORIZED-DECISION-001@r2`; content `synthetic-content:candidate-defer-reauthorized-decision-001-r2`; consumed

## Source-Backed Evidence And Three Prior Refusals

Request `SYNTH-CANDIDATE-REVISE-REQUEST-001@r2`, signed at `2026-08-27T22:15:12Z` by `synthetic-revision-requester` under `synthetic-candidate-revision-request-creation-authority@r2`, content `synthetic-content:candidate-revise-request-001-r2`, remains non-operative. Consumed review authority `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-001@r2` and decision `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-001@r2` at `2026-08-27T22:25:12Z` record `revise_request_not_admitted_missing_new_evidence_and_revision_authority`.

Concern `SYNTH-CANDIDATE-REVISION-CONCERN-001@r2`, signed at `2026-08-27T22:30:12Z` by `synthetic-concern-reporter` under `synthetic-candidate-concern-record-creation-authority@r2`, content `synthetic-content:candidate-revision-concern-001-r2`, remains an unsupported lead. Request `SYNTH-CANDIDATE-REVISE-REQUEST-002@r2`, signed at `2026-08-27T22:32:12Z` by `synthetic-revision-requester` under `synthetic-candidate-revision-request-creation-authority@r2`, content `synthetic-content:candidate-revise-request-002-r2`, remains non-operative. Consumed review authority `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-002@r2` and decision `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-002@r2` at `2026-08-27T22:35:12Z` record `renewed_revise_request_not_admitted_concern_is_not_source_backed_evidence_and_revision_authority_absent`.

Evidence `SYNTH-CANDIDATE-REVISION-EVIDENCE-001@r2`, signed at `2026-08-27T22:40:12Z` by `synthetic-source-owner` under `synthetic-candidate-revision-evidence-record-creation-authority@r2`, content `synthetic-content:candidate-revision-evidence-001-r2`, pins source revision `synthetic-source-revision:second-regrant-second-revocation-002-r3`, deficiency `unsupported_concern_requires_source_backed_revision_basis`, correction gate `verify_source_revision_and_preserve_defer_until_authorized`, and acceptance condition `source_evidence_validated_and_exact_revision_authority_present`.

Request `SYNTH-CANDIDATE-REVISE-REQUEST-003@r2`, signed at `2026-08-27T22:42:12Z` by `synthetic-revision-requester`, content `synthetic-content:candidate-revise-request-003-r2`, remains non-operative. Review authority `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-003@r2`, signed at `2026-08-27T22:44:12Z` by `synthetic-result-owner` under `synthetic-candidate-revise-request-review-decision-authority@r2`, authorizes only `synthetic-candidate-disposition-request-reviewer`. Its decision `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-003@r2` at `2026-08-27T22:45:12Z`, content `synthetic-content:candidate-revise-request-review-refusal-decision-003-r2`, records `renewed_revise_request_not_admitted_source_backed_evidence_present_but_revision_authority_absent`. All request, concern, evidence, review, and refusal checksums are valid; all three review authorities are consumed.

## Authorized Revise Disposition

At `2026-08-27T22:50:12Z`, `SYNTH-CANDIDATE-DISPOSITION-REVISION-AUTHORITY-001@r2` is signed by `synthetic-result-owner` under `synthetic-candidate-disposition-revision-decision-authority@r2`. It authorizes only `synthetic-candidate-disposition-revision-decider` once. Decision `SYNTH-CANDIDATE-DISPOSITION-REVISION-DECISION-001@r2` at `2026-08-27T22:52:12Z`, record `revise_synthetic_candidate_disposition_only`, content `synthetic-content:candidate-disposition-revision-decision-001-r2`, changes only synthetic disposition from `deferred` to `revision_required`. The checksum is valid and authority is consumed. The decision does not cure the content deficiency or revise candidate content.

## Revision-Plan Preparation Authority

At `2026-08-27T23:00:12Z`, `SYNTH-CANDIDATE-REVISION-PLAN-PREPARATION-AUTHORITY-001@r2` is signed by `synthetic-result-owner` under `synthetic-candidate-revision-plan-preparation-authority@r2`. It authorizes only `synthetic-candidate-revision-planner` once to prepare a non-operative plan for the exact deficiency after verifying the complete lineage, evidence and checksum, current `revision_required` disposition, unchanged candidate and score, no revocation, and unconsumed authority. It authorizes no candidate-content edit, proving execution, P8, disposition change, transfer, graduation, deployment, publication, contact, real state change, or external action.

## Prepared Revision Plan And Nonexecution

At `2026-08-27T23:02:12Z`, `SYNTH-CANDIDATE-REVISION-PLAN-001@r2` is signed by that planner and records `prepare_source_backed_revision_basis_without_content_execution`. Content `synthetic-content:candidate-revision-plan-001-r2` has a valid checksum. The plan proposes only a future synthetic candidate-content change: add inspectable `candidate_revision_basis` pinned to `SYNTH-CANDIDATE-REVISION-EVIDENCE-001@r2`, source revision `synthetic-source-revision:second-regrant-second-revocation-002-r3`, deficiency `unsupported_concern_requires_source_backed_revision_basis`, correction gate `verify_source_revision_and_preserve_defer_until_authorized`, and acceptance condition `source_evidence_validated_and_exact_revision_authority_present`. It requires separate candidate-content revision authority, immutable before and after content, validation, correction, recovery, and owner return. Planning authority is consumed; the plan is not execution.

## Owner Fit, Affected Parties, And Legitimacy

Decision owner remains `synthetic-result-owner`; correction owner remains `synthetic-proving-plan-owner`. All actors, affected-party standing, evidence, authorities, and systems are synthetic. Legitimacy depends on preserving the complete evidence/authority distinction, negative records, and one-use custody. Transfer, graduation, deployment, publication, contact, and external action remain `none`.

## Stops, Correction, Recovery, And Reopen

Stop on any named revision, evidence, authority, decision, plan, content ID, checksum, deficiency, gate, or acceptance-condition change. Failure modes include evidence treated as authority, disposition treated as content revision, plan treated as execution, planning authority reused, negative evidence erased, or synthetic state applied to `CMD-0001`. Failed planning recovery retracts only the revision plan, restores `revision_required` with no plan, preserves every predecessor and negative record, and changes no candidate content.

## Prepared Return And Exact Wake

Return `SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2` remains preserved. Prepared return is `synthetic_revision_plan_record_only`. Exact next wake is exact candidate-content revision execution authority plus an authorized immutable revision trace, receipt, and independent validation under the frozen plan, or any named revision.

## Frontier Verification

Repository integration verified native frontmatter and exact section topology; complete candidate, score, original/replacement observation, grant/revocation/supersession/unauthorized-record, negative-evidence, disposition, request-review, source-evidence, planning-authority, plan, recovery, non-effect, and exact-wake custody. Synthetic state is `revision_plan_prepared_not_executed`; disposition remains `revision_required`; candidate content and score remain unchanged; `CMD-0001`, P8, and real state remain unchanged.
