---
artifact_type: synthetic_candidate_disposition_revise_authorized_after_source_backed_evidence_no_p8_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Candidate-Disposition Revise-Authorized After-Source-Backed-Evidence No-P8-Authority Boundary Fixture

## Use Boundary

This synthetic fixture preserves the bounded pass, accepted return, invalid and retracted first defer, recovery, separately reauthorized defer, all three prior revise requests and refusals, the unsupported concern, source-backed evidence, all negative evidence, and prior synthetic state `deferred`. It adds one exact one-use candidate-disposition revision authority and one authorized synthetic `revise` decision. This changes only the synthetic disposition to `revision_required`; it does not revise candidate content, execute a proving plan, create P8, or change a real candidate. It is not transfer, graduation, deployment, publication, contact, or external action. External action is `none`. Do not modify `CMD-0001` or create P8.

## Decision Header

| Field | Value |
| --- | --- |
| `fixture_id` | `SYNTH-CANDIDATE-REVISE-AUTHORIZED-AFTER-SOURCE-EVIDENCE-001@r2` |
| `decision_id` | `SYNTH-CANDIDATE-DISPOSITION-REVISION-DECISION-001@r2` |
| `candidate_id` | `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `source_inquiry` | `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `decision_owner` | `synthetic-result-owner` |
| `decided_by` | `synthetic-candidate-disposition-revision-decider` |
| `decided_at` | `2026-08-27T22:52:12Z` |
| `decision_record` | `revise_synthetic_candidate_disposition_only` |
| `synthetic_disposition` | `revision_required` |
| `external_action` | `none` |

## Frozen Candidate And Evidence

The fixture is frozen against `ROADMAP.md`, `proving/LEAST-CONSEQUENTIAL-PROVING-PLAN-TEMPLATE.md`, `dispositions/CANDIDATE-DISPOSITION-DECISION-TEMPLATE.md`, and `dispositions/CANDIDATE-DISPOSITION-SYNTHETIC-SOURCE-BACKED-EVIDENCE-REVISE-REQUEST-REFUSED-NO-REVISION-AUTHORITY-BOUNDARY-FIXTURE.md`. It preserves plan `SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, score `SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, source `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, candidate `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, immutable trace and validation, return `SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2`, return acceptance, invalid first defer, checksum revision, correction, recovery, reauthorization, reauthorized defer, three requests and refusals, the unsupported concern, and source-backed evidence.

Originals remain `synthetic-observation:comparison-equal-014-r2`, `synthetic-observation:comparison-unequal-014a-r2`, and `synthetic-observation:comparison-unequal-014b-r2`; replacements remain `synthetic-observation:comparison-equal-014a-corrected-r2` and `synthetic-observation:comparison-equal-014b-corrected-r2`. Grants 006, 007, and 008, three future-only revocations, three valid supersession records, and four unauthorized records remain distinct. Negative evidence remains at `synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`. The score result remains `bounded_pass`; candidate content and all real state remain unchanged.

## Consumed Authority Lineage

- return acceptance — `SYNTH-RESULT-RETURN-ACCEPTANCE-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-result-return-acceptance-decision-authority@r2`; decision `SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2`; content `synthetic-content:second-regrant-defer-return-acceptance-decision-001-r2`; consumed
- first defer — `SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-decision-authority@r2`; decider `synthetic-candidate-disposition-decider`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-decision-001-r2`; consumed and decision retracted
- recovery — `SYNTH-CANDIDATE-DEFER-DISPOSITION-CORRECTION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-correction-decision-authority@r2`; decider `synthetic-proving-plan-owner`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-RECOVERY-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-recovery-decision-001-r2`; consumed
- defer reauthorization — `SYNTH-CANDIDATE-DEFER-REAUTHORIZATION-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-reauthorization-decision-authority@r2`; decider `synthetic-candidate-disposition-redecider`; decision `SYNTH-CANDIDATE-DEFER-REAUTHORIZED-DECISION-001@r2`; content `synthetic-content:candidate-defer-reauthorized-decision-001-r2`; consumed

The first request `SYNTH-CANDIDATE-REVISE-REQUEST-001@r2`, signed at `2026-08-27T22:15:12Z` by `synthetic-revision-requester` under `synthetic-candidate-revision-request-creation-authority@r2`, has content ID `synthetic-content:candidate-revise-request-001-r2` and a valid checksum. Review authority `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-001@r2` and refusal `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-001@r2` at `2026-08-27T22:25:12Z` are consumed; the refusal remains `revise_request_not_admitted_missing_new_evidence_and_revision_authority`.

Concern `SYNTH-CANDIDATE-REVISION-CONCERN-001@r2`, signed at `2026-08-27T22:30:12Z` by `synthetic-concern-reporter` under `synthetic-candidate-concern-record-creation-authority@r2`, has content ID `synthetic-content:candidate-revision-concern-001-r2` and a valid checksum. It remains a lead, not source-backed evidence. Second request `SYNTH-CANDIDATE-REVISE-REQUEST-002@r2`, signed at `2026-08-27T22:32:12Z` by `synthetic-revision-requester` under `synthetic-candidate-revision-request-creation-authority@r2`, has content ID `synthetic-content:candidate-revise-request-002-r2` and a valid checksum. Review authority `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-002@r2` and refusal `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-002@r2` at `2026-08-27T22:35:12Z` are consumed; the refusal remains `renewed_revise_request_not_admitted_concern_is_not_source_backed_evidence_and_revision_authority_absent`.

## Source-Backed Evidence And Prior Refusals

At `2026-08-27T22:40:12Z`, source-backed evidence `SYNTH-CANDIDATE-REVISION-EVIDENCE-001@r2` is signed by `synthetic-source-owner` under `synthetic-candidate-revision-evidence-record-creation-authority@r2`. Content ID `synthetic-content:candidate-revision-evidence-001-r2` has a valid checksum. It names source revision `synthetic-source-revision:second-regrant-second-revocation-002-r3`, deficiency `unsupported_concern_requires_source_backed_revision_basis`, correction gate `verify_source_revision_and_preserve_defer_until_authorized`, and acceptance condition `source_evidence_validated_and_exact_revision_authority_present`. It changes no candidate or disposition and grants no revision authority.

At `2026-08-27T22:42:12Z`, third request `SYNTH-CANDIDATE-REVISE-REQUEST-003@r2` is signed by `synthetic-revision-requester` under `synthetic-candidate-revision-request-creation-authority@r2`. Content ID `synthetic-content:candidate-revise-request-003-r2` has a valid checksum. At `2026-08-27T22:44:12Z`, review authority `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-003@r2` is signed by `synthetic-result-owner` under `synthetic-candidate-revise-request-review-decision-authority@r2`; it authorizes only `synthetic-candidate-disposition-request-reviewer` once to review, not revise. At `2026-08-27T22:45:12Z`, refusal `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-003@r2` is signed by that reviewer and records `renewed_revise_request_not_admitted_source_backed_evidence_present_but_revision_authority_absent`. Content ID `synthetic-content:candidate-revise-request-review-refusal-decision-003-r2` has a valid checksum. All three review authorities are consumed; all three requests remain non-operative.

## Revision Authority And Decision Basis

At `2026-08-27T22:50:12Z`, candidate-disposition revision authority `SYNTH-CANDIDATE-DISPOSITION-REVISION-AUTHORITY-001@r2` is signed by `synthetic-result-owner` under `synthetic-candidate-disposition-revision-decision-authority@r2`. It authorizes only `synthetic-candidate-disposition-revision-decider` once to change the synthetic disposition from `deferred` to `revision_required` after verifying the entire lineage, source-backed evidence and checksum, named deficiency/correction/acceptance package, unchanged candidate and score, current defer, all consumed prior authorities, and unconsumed revision authority. It authorizes no candidate-content revision, P8, proving execution, transfer, graduation, deployment, publication, contact, real state change, or external action.

At `2026-08-27T22:52:12Z`, every check matched. Decision `SYNTH-CANDIDATE-DISPOSITION-REVISION-DECISION-001@r2` is signed by that decider and records `revise_synthetic_candidate_disposition_only`, deficiency `unsupported_concern_requires_source_backed_revision_basis`, correction gate `verify_source_revision_and_preserve_defer_until_authorized`, and acceptance condition `source_evidence_validated_and_exact_revision_authority_present`. Content ID `synthetic-content:candidate-disposition-revision-decision-001-r2` has a valid checksum; the one-use authority is consumed. The decision authorizes and records only the disposition change. It does not cure the content deficiency or revise the candidate.

## Negative Evidence And Reasons

Negative evidence remains at `synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`. The unsupported concern remains preserved as a lead. The first refusal lacked both new evidence and revision authority; the second established that the concern was not source-backed evidence; the third established that source-backed evidence still was not revision authority. Exact revision authority now permits the synthetic disposition change, but the named deficiency remains to be corrected by a separately authorized candidate-content revision. The score remains `bounded_pass` and no negative evidence is erased.

## Owner Fit, Transfer, And Graduation Boundary

Decision owner remains `synthetic-result-owner`; correction owner remains `synthetic-proving-plan-owner`. Transfer is `none`; graduation is `none`; deployment is `none`; publication is `none`; contact is `none`; external action is `none`. `CMD-0001` is not modified and P8 is not created. The candidate process fixture status remains `candidate_process_fixture`.

## Affected Parties And Legitimacy

All actors, standing, evidence, authorities, and systems are synthetic. Legitimacy derives only from the frozen evidence and exact one-use authority lineage. The decision represents neither affected people nor any real owner. The core risks are evidence laundered into authority, disposition authority laundered into candidate-content revision, or synthetic state applied to a real candidate.

## Stops, Correction, Recovery, And Reopen

Stop on any named revision, evidence, authority, decision, checksum, deficiency, gate, or acceptance-condition change. Failure modes include evidence treated as authority, authority reused, the disposition decision treated as candidate revision or P8, prior negative evidence erased, or synthetic state applied to `CMD-0001`. Failed disposition recovery retracts only the revision decision, restores synthetic disposition `deferred`, preserves the source-backed evidence and all three requests and refusals, and changes no candidate content. Exact next wake is an authorized synthetic candidate-revision plan under the frozen disposition decision, or any named revision.

## Executed Synthetic Revision Disposition

The exact decision changes only synthetic disposition from `deferred` to `revision_required`. Candidate content, score result `bounded_pass`, negative evidence, and all real state remain unchanged. The deficiency `unsupported_concern_requires_source_backed_revision_basis` remains open for separately authorized content correction. The one-use authority `SYNTH-CANDIDATE-DISPOSITION-REVISION-AUTHORITY-001@r2` is consumed. Content ID `synthetic-content:candidate-disposition-revision-decision-001-r2` has a valid checksum. External action is `none`.

## Frontier Verification

Repository integration verified native frontmatter and section topology; the complete frozen candidate and evidence package; original and replacement observations; grants, revocations, supersessions, and unauthorized records; negative evidence; consumed authority lineage; all three requests and refusals; unsupported concern and source-backed evidence; exact revision authority and decision; content IDs, checksum assertions, recovery, non-effects, and exact wake. Synthetic disposition is `revision_required`; candidate content remains unchanged; `CMD-0001`, P8, and real repository state remain unchanged.
