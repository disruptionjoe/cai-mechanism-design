---
artifact_type: synthetic_proving_result_return_owner_defer_acceptance_no_disposition_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Proving-Result-Return Owner-Defer-Acceptance No-Disposition-Authority Boundary Fixture

## Use Boundary

This synthetic fixture returns one unchanged validated `bounded_pass` package
and its bounded `defer` support to the synthetic result owner, then records one
separately authorized acceptance decision. Acceptance does not choose, record,
or execute a candidate disposition. It creates no `CMD-0001-P8`, candidate
status change, transfer, graduation, deployment, or external action and does
not modify `CMD-0001`.

## Return Header

| Field | Value |
| --- | --- |
| `return_id` | `SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2` |
| `proving_id` | `SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `plan_revision` | `SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `candidate_id` | `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `source_inquiry` | `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `source_revision` | `synthetic-source-revision:second-regrant-second-revocation-001-r2` |
| `result_owner` | `synthetic-result-owner` |
| `prepared_by` | `synthetic-result-return-preparer` |
| `prepared_at` | `2026-08-27T21:15:12Z` |
| `external_action` | `none` |

Return content ID is
`synthetic-content:second-regrant-defer-return-001-r2`; its checksum is valid.
The returned result is `bounded_pass`; supported disposition is `defer`;
initial return status is `returned_unaccepted`. Return pointer is
`synthetic://proving-return/SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2`.

## Frozen Result Package

The package freezes plan
`SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, score
`SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, candidate
`SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, source
`SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, source revision
`synthetic-source-revision:second-regrant-second-revocation-001-r2`, immutable
trace, validation, authority lineage, and score return.

Originals are `synthetic-observation:comparison-equal-014-r2`,
`synthetic-observation:comparison-unequal-014a-r2`, and
`synthetic-observation:comparison-unequal-014b-r2`. Valid replacements are
`synthetic-observation:comparison-equal-014a-corrected-r2` and
`synthetic-observation:comparison-equal-014b-corrected-r2`. Grants 006, 007,
and 008, their three future-only revocations, three valid supersession records,
and four unauthorized records remain distinct. Matching content identifiers
use stem `synthetic-content:second-regrant-second-revocation-001-r2`.
Negative evidence remains at
`synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`.

## Tested Claim And Conditions

The bounded claim is that complete, exact, contemporaneously authorized
supersession leaves surviving evidence all `equal`. A missing exact record,
invalid replacement, stale or revoked authority at signing time, failed
checksum, or conflicting surviving observation defeats that claim. Immutable
validation confirms every valid record had contemporaneous authority, all
revocations are nonretroactive, all unauthorized records supersede nothing,
and only the first valid record is needed. Return acceptance additionally
requires the unchanged plan, trace, score, validation, lineage, checksum,
owner identity, stops, negative evidence, correction, recovery, and unconsumed
decision authority. Prohibited conclusions are effectiveness, destination fit,
candidate disposition, deployment readiness, or external outcome.

## Observed Result

At `2026-08-27T21:20:12Z`, decision authority
`SYNTH-RESULT-RETURN-ACCEPTANCE-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-result-return-acceptance-decision-authority@r2`. It authorizes
`synthetic-result-owner` exactly once to accept or decline only the unchanged
return package after every named check. It authorizes no candidate disposition,
candidate status change, P8, transfer, graduation, deployment, or external
action.

At `2026-08-27T21:25:12Z`, every required check matched. Decision record
`SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2` is signed by
`synthetic-result-owner` under that exact authority and records
`accept_return_and_defer_support_for_later_disposition`. Decision content ID is
`synthetic-content:second-regrant-defer-return-acceptance-decision-001-r2`; its
checksum is valid. The one-use decision authority is consumed. Resulting state
is `return_accepted_disposition_not_decided`; receipt acknowledgment is
`acknowledged`; supported disposition remains `defer`. No candidate-
disposition, candidate-state, P8, transfer, graduation, deployment, or
external-action record exists.

## Evidence Grade, Counterevidence, And Failure

Evidence grade is an immutable validated synthetic trace. Supporting evidence
is the complete contemporaneously authorized lineage. Counterevidence is the
four unauthorized records, which supersede nothing and remain visible negative
evidence. Failure modes include treating return acceptance as disposition,
defer support as executed defer, acknowledgment as acceptance without the
decision, regrant as retroactive authority, revocation as erasure of a valid
record, consumed decision authority reused, or a downstream effect invented.
Any named source, plan, trace, score, validation, authority, record, return,
decision, checksum, or risk revision triggers a stop.

## Affected-Party, Data, And Legitimacy Return

All affected-party standing, treatment, records, actors, data, evidence, and
authority are synthetic. No real person, institution, personal data, or
external system is involved or represented. No real affected party or owner
can be spoken for. The legitimacy risk is laundering a bounded synthetic
acceptance into disposition or real-world authority. Correction belongs to
`synthetic-proving-plan-owner`.

## Residual Uncertainty, Correction, And Recovery

Residual uncertainty is whether a later separately authorized disposition
owner will choose `defer`; this accepted return cannot decide that question.
Preserve the full lineage, score, return, decision, and negative evidence. If
the acceptance authority or decision checksum fails, retract only the
acceptance decision, restore `returned_unaccepted`, and change no candidate
state. Exact next wake is one separately authorized candidate-disposition decision under frozen current records, or any named revision.

## Permitted Disposition Support

The return supports only `defer` for later consideration by
`synthetic-result-owner`. It does not choose or execute that disposition,
create candidate state, authorize P8, or support transfer, graduation,
deployment, publication, or external action.

## Owner Return And Acceptance Decision

Receiving owner is `synthetic-result-owner`; return pointer is
`synthetic://proving-return/SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2`.
Authority `SYNTH-RESULT-RETURN-ACCEPTANCE-AUTHORITY-001@r2` and decision
`SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2` are exact, one-use, checksum-
valid, and consumed. Acceptance records only
`accept_return_and_defer_support_for_later_disposition`; disposition remains
unconsumed owner authority.

## Frontier Verification

Verify the plan, source, trace, score, all five observations, replacements,
three grants, three revocations, seven supersession records, timestamps,
signers, authority scopes, validation, pointers, content IDs, return, decision,
stops, correction, recovery, and exact wake independently. Confirm all four
unauthorized records remain negative evidence, only the first valid record is
needed, return acceptance stays separate from disposition, and no `CMD-0001`
change, P8, transfer, graduation, deployment, or external action is created.
