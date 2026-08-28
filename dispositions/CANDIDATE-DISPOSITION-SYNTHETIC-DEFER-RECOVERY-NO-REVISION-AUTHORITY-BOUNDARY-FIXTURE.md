---
artifact_type: synthetic_candidate_disposition_defer_recovery_no_revision_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Candidate-Disposition Defer-Recovery No-Revision-Authority Boundary Fixture

## Use Boundary

This fixture preserves the validated three-grant score, accepted return,
executed synthetic `defer`, and all negative evidence. A separately authorized
correction retracts only the defer decision after its named checksum revision
proves it invalid and restores `return_accepted_disposition_not_decided`.
Recovery is not `revise`, a new result, real candidate change, P8, transfer,
graduation, deployment, publication, contact, or external action and creates
no effectiveness or destination-fit claim.

## Recovery Header

| Field | Value |
| --- | --- |
| `recovery_id` | `SYNTH-CANDIDATE-DEFER-DISPOSITION-RECOVERY-001@r2` |
| `candidate_id` | `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `source_inquiry` | `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `source_revision` | `synthetic-source-revision:second-regrant-second-revocation-001-r2` |
| `decision_owner` | `synthetic-result-owner` |
| `correction_owner` | `synthetic-proving-plan-owner` |
| `external_action` | `none` |

## Frozen Candidate And Evidence

The package freezes plan `SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`,
score `SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, the named
candidate and source, immutable trace and validation, return
`SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2`, acceptance decision
`SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2`, disposition authority
`SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2`, and decision
`SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2`.

Originals are `synthetic-observation:comparison-equal-014-r2`,
`synthetic-observation:comparison-unequal-014a-r2`, and
`synthetic-observation:comparison-unequal-014b-r2`; replacements are
`synthetic-observation:comparison-equal-014a-corrected-r2` and
`synthetic-observation:comparison-equal-014b-corrected-r2`. Grants 006, 007,
and 008, three future-only revocations, three valid supersession records, and
four unauthorized records remain distinct. Negative evidence remains at
`synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`.
The result remains `bounded_pass`; only `defer` is supported.

Return content ID `synthetic-content:second-regrant-defer-return-001-r2` and
acceptance content ID
`synthetic-content:second-regrant-defer-return-acceptance-decision-001-r2` have
valid checksums. Acceptance authority remains consumed and distinct from
disposition authority. The latter was signed at `2026-08-27T21:35:12Z` by
`synthetic-result-owner` under
`synthetic-candidate-disposition-decision-authority@r2`, authorized only
`synthetic-candidate-disposition-decider`, and was consumed when that decider
signed the valid `defer` decision at `2026-08-27T21:40:12Z`. Decision content
ID was `synthetic-content:candidate-defer-disposition-decision-001-r2`.

## Checksum Revision Evidence

At `2026-08-27T21:45:12Z`, record
`SYNTH-CANDIDATE-DEFER-DISPOSITION-CHECKSUM-REVISION-001@r2` is signed by
`synthetic-checksum-evidence-owner` under
`synthetic-disposition-checksum-evidence-authority@r2`. Content ID
`synthetic-content:candidate-defer-disposition-checksum-revision-001-r2` has a
valid checksum. It proves only that the defer decision content ID no longer
matches the frozen decision; it changes no source, candidate, score, return,
acceptance, supported disposition, or real state and grants no correction authority.

## Correction Authority

At `2026-08-27T21:50:12Z`, authority
`SYNTH-CANDIDATE-DEFER-DISPOSITION-CORRECTION-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-candidate-disposition-correction-decision-authority@r2`. It
authorizes only `synthetic-proving-plan-owner` exactly once to verify the named
revision, retract only the invalid defer decision, and restore the accepted-
return state. It authorizes no new disposition, candidate or score revision,
P8, transfer, graduation, deployment, publication, contact, or external action.

## Recovery Decision Basis

At `2026-08-27T21:55:12Z`, every required check matched. Recovery decision
`SYNTH-CANDIDATE-DEFER-DISPOSITION-RECOVERY-DECISION-001@r2` is signed by
`synthetic-proving-plan-owner` under the exact correction authority and records
`retract_defer_restore_return_accepted_disposition_not_decided`. Content ID
`synthetic-content:candidate-defer-disposition-recovery-decision-001-r2` has a
valid checksum. The correction authority is consumed; the invalid defer
decision remains retracted negative evidence and its consumed disposition
authority is not restored.

## Negative Evidence And Reasons

All four unauthorized records remain visible and supersede nothing. The
invalid defer decision remains preserved as retracted negative evidence.
Failure modes include checksum evidence treated as correction authority,
recovery treated as `revise`, consumed authority restored, retracted evidence
erased, synthetic state applied to `CMD-0001`, or downstream effect invented.
The bounded pass establishes neither effectiveness nor destination fit.

## Owner Fit, Transfer, And Graduation Boundary

Decision owner is `synthetic-result-owner`; correction owner is
`synthetic-proving-plan-owner`. Synthetic state becomes
`return_accepted_disposition_not_decided`; no real candidate changes. No P8,
transfer, graduation, deployment, publication, contact, or external action exists.

## Affected Parties And Legitimacy

All standing, data, actors, evidence, authority, and systems are synthetic. No
real person, institution, affected party, or owner is represented or can be
spoken for. The legitimacy risk is laundering recovery into real disposition
or revision authority.

## Stops, Correction, Recovery, And Reopen

Stop on any source, candidate, plan, trace, validation, authority, grant,
revocation, record, replacement, score, return, acceptance, disposition,
checksum-revision, recovery, checksum, or risk revision. Failed correction
recovery preserves all prior records, retracts only the recovery decision, and
restores synthetic state `deferred`. Exact next wake is one separately authorized synthetic candidate-disposition decision under frozen recovered records, or any named revision.

## Executed Synthetic Recovery

The signed recovery decision is executed. State becomes
`return_accepted_disposition_not_decided`; correction authority is consumed;
the invalid defer decision remains retracted negative evidence; its consumed
disposition authority is not restored. No real candidate state changes.

## Frontier Verification

Verify plan, source, trace, score, all observations and replacements, three
grants, three revocations, seven supersession attempts, timestamps, signers,
authority scopes, validation, pointers, content IDs, return, acceptance,
disposition, checksum revision, recovery, stops, correction, and exact wake.
Confirm the decision signer is `synthetic-proving-plan-owner`, all negative
evidence remains visible, and no `CMD-0001` change or downstream effect exists.
