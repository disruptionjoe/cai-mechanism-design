---
artifact_type: synthetic_candidate_disposition_defer_reauthorized_after_recovery_no_revision_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Candidate-Disposition Defer-Reauthorized-After-Recovery No-Revision-Authority Boundary Fixture

## Use Boundary

This synthetic fixture preserves the bounded pass, accepted return, invalid
and retracted first defer, recovery, all negative evidence, and restored
`return_accepted_disposition_not_decided`. One new, separately authorized
decision again executes only `defer` for the unchanged synthetic candidate.
New authority does not restore or reuse either consumed prior authority. It is
not `revise`, P8, a new proving result, real candidate change, transfer,
graduation, deployment, publication, contact, or external action.

## Decision Header

| Field | Value |
| --- | --- |
| `fixture_id` | `SYNTH-CANDIDATE-DEFER-REAUTHORIZED-AFTER-RECOVERY-001@r2` |
| `decision_id` | `SYNTH-CANDIDATE-DEFER-REAUTHORIZED-DECISION-001@r2` |
| `candidate_id` | `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `source_inquiry` | `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `decision_owner` | `synthetic-result-owner` |
| `decided_by` | `synthetic-candidate-disposition-redecider` |
| `decided_at` | `2026-08-27T22:10:12Z` |
| `external_action` | `none` |

## Frozen Candidate And Evidence

The package freezes plan `SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`,
score `SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, the named source
and candidate, immutable trace and validation, return
`SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2`, return acceptance,
the invalid and retracted first disposition, checksum revision, correction
authority, and recovery decision.

Originals remain `synthetic-observation:comparison-equal-014-r2`,
`synthetic-observation:comparison-unequal-014a-r2`, and
`synthetic-observation:comparison-unequal-014b-r2`; replacements remain
`synthetic-observation:comparison-equal-014a-corrected-r2` and
`synthetic-observation:comparison-equal-014b-corrected-r2`. Grants 006, 007,
and 008, three future-only revocations, three valid supersession records, and
four unauthorized records remain distinct. Negative evidence remains at
`synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`.
The result remains `bounded_pass`; only `defer` is supported. No real state changes.

## Consumed Authority Lineage

- return acceptance — `SYNTH-RESULT-RETURN-ACCEPTANCE-AUTHORITY-001@r2`;
  signer `synthetic-result-owner`; scope
  `synthetic-result-return-acceptance-decision-authority@r2`; decision
  `SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2`; content
  `synthetic-content:second-regrant-defer-return-acceptance-decision-001-r2`;
  consumed.
- first defer — `SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2`;
  signer `synthetic-result-owner`; scope
  `synthetic-candidate-disposition-decision-authority@r2`; decider
  `synthetic-candidate-disposition-decider`; decision
  `SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2`; content
  `synthetic-content:candidate-defer-disposition-decision-001-r2`; consumed
  and decision retracted.
- recovery — `SYNTH-CANDIDATE-DEFER-DISPOSITION-CORRECTION-AUTHORITY-001@r2`;
  signer `synthetic-result-owner`; scope
  `synthetic-candidate-disposition-correction-decision-authority@r2`; decider
  `synthetic-proving-plan-owner`; decision
  `SYNTH-CANDIDATE-DEFER-DISPOSITION-RECOVERY-DECISION-001@r2`; content
  `synthetic-content:candidate-defer-disposition-recovery-decision-001-r2`;
  consumed.

## New Reauthorization

At `2026-08-27T22:05:12Z`, authority
`SYNTH-CANDIDATE-DEFER-REAUTHORIZATION-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-candidate-disposition-reauthorization-decision-authority@r2`. It
authorizes only `synthetic-candidate-disposition-redecider` once to execute
`defer` after verifying the complete frozen lineage, retracted invalid
decision, consumed old authorities, recovered state, unchanged supported
disposition, checksums, negative evidence, and unconsumed new authority. It
authorizes no other disposition or downstream effect.

## Decision Basis

At `2026-08-27T22:10:12Z`, every required check matched. The accepted-return
authority, invalid first-defer authority, and correction authority remain
consumed; the invalid decision remains retracted; state before the new decision
is `return_accepted_disposition_not_decided`; only `defer` remains supported;
and the new authority was unconsumed. Decision
`SYNTH-CANDIDATE-DEFER-REAUTHORIZED-DECISION-001@r2` is signed by
`synthetic-candidate-disposition-redecider` and records
`defer_after_recovery`. Content ID
`synthetic-content:candidate-defer-reauthorized-decision-001-r2` has a valid
checksum; new authority is consumed.

## Negative Evidence And Reasons

All four unauthorized records remain visible and supersede nothing. The first
invalid defer remains preserved as retracted negative evidence. Neither old
authority is restored. Failure modes include new authority treated as
restoration, retracted evidence erased, re-defer treated as `revise`, synthetic
state applied to `CMD-0001`, or downstream effect invented. The bounded pass
establishes neither effectiveness nor destination fit.

## Owner Fit, Transfer, And Graduation Boundary

Decision owner is `synthetic-result-owner`; correction owner is
`synthetic-proving-plan-owner`; authorized decider is
`synthetic-candidate-disposition-redecider`. Synthetic state becomes
`deferred` again. No real candidate changes, P8, transfer, graduation,
deployment, publication, contact, or external action exists.

## Affected Parties And Legitimacy

All standing, data, actors, evidence, authority, and systems are synthetic. No
real person, institution, affected party, or owner is represented or can be
spoken for. The legitimacy risk is laundering synthetic reauthorization into
real disposition or revision authority.

## Stops, Correction, Recovery, And Reopen

Stop on any source, candidate, plan, trace, validation, authority, grant,
revocation, record, replacement, score, return, acceptance, disposition,
checksum, recovery, reauthorization, decision, or risk revision. Correction
belongs to `synthetic-proving-plan-owner`. Recovery from a failed new decision
preserves every predecessor, retracts only
`SYNTH-CANDIDATE-DEFER-REAUTHORIZED-DECISION-001@r2`, and restores
`return_accepted_disposition_not_decided`; it restores no consumed authority.
Exact next wake is materially new synthetic candidate evidence under frozen reauthorized records, or any named revision.

## Executed Synthetic Decision

The signed decision executes only `defer_after_recovery` for the unchanged
synthetic candidate. State becomes `deferred`; new authority
`SYNTH-CANDIDATE-DEFER-REAUTHORIZATION-001@r2` is consumed; the first invalid
defer remains retracted negative evidence; neither prior authority is restored.
No real candidate or downstream state changes.

## Frontier Verification

Verify the plan, source, candidate, trace, score, observations, replacements,
grants, revocations, supersession attempts, return, acceptance, invalid first
defer, checksum revision, recovery, new authority, decision, signers, deciders,
scopes, content IDs, stops, correction, recovery, and exact wake. Confirm no
`CMD-0001` change, revision, P8, transfer, graduation, deployment, publication,
contact, or external action exists. This section defines required Frontier
checks; it does not claim they occurred before repository integration.
