---
artifact_type: synthetic_proving_score_second_regrant_second_revocation_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Proving-Score Second-Regrant Second-Revocation-Authority Boundary Fixture

## Use Boundary

This synthetic fixture scores only the frozen three-grant lineage. It preserves
three valid records, the pre-grant attempt, two earlier post-revocation
attempts, three future-only revocations, and one new attempt after the third
revocation. Revocation is nonretroactive: each record valid when signed remains
valid. The new attempted record is unauthorized, supersedes nothing, and
remains negative evidence. The result stays `bounded_pass` with `defer`
support. It does not modify `CMD-0001`, create P8, or authorize external action.

## Score Header

| Field | Value |
| --- | --- |
| `proving_id` | `SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `plan_revision` | `SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `candidate_id` | `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `source_inquiry` | `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `source_revision` | `synthetic-source-revision:second-regrant-second-revocation-001-r2` |
| `treatment_type` | `synthetic` |
| `result_owner` | `synthetic-result-owner` |
| `execution_authority_ref` | three contemporaneous supersession grants described below |
| `scored_by` | `synthetic-proving-scorer` |
| `external_action` | `none` |

## Frozen Plan And Evidence

The plan, trace, validation, authority pointers, supersession pointers, and
matching content identifiers use stem
`synthetic-content:second-regrant-second-revocation-001-r2`. The clean trace
preserves originals `synthetic-observation:comparison-equal-014-r2`,
`synthetic-observation:comparison-unequal-014a-r2`, and
`synthetic-observation:comparison-unequal-014b-r2`, plus valid replacements
`synthetic-observation:comparison-equal-014a-corrected-r2` and
`synthetic-observation:comparison-equal-014b-corrected-r2`. Both pointers are
unchanged; all originals are readable, in scope, and provenance-valid; both
replacements are chronology- and checksum-valid.

## Claim And Decision Conditions

The bounded claim is that complete, exact, contemporaneously authorized
supersession leaves surviving evidence all `equal`. A missing exact record,
invalid replacement, stale or revoked authority at signing time, failed
checksum, or conflicting surviving observation defeats that claim. Later
redundant valid records do not strengthen it, and later unauthorized records do
not weaken it. Prohibited conclusions are effectiveness, destination fit,
owner acceptance, deployment readiness, and external outcome.

## Observed Trace

At `2026-08-27T13:05:00Z`,
`SYNTH-SUPERSESSION-EQUAL-014@record-before-grant` is unauthorized. At
`13:10:00Z`, grant
`SYNTH-SUPERSESSION-AUTHORITY-R2-006@grant-before-valid-record` is signed by
`synthetic-supersession-authority-owner` under
`synthetic-supersession-authority-issuance@r2`; it is future-only and
nonretroactive. At `13:15:00Z`,
`SYNTH-SUPERSESSION-EQUAL-014@valid-record-before-revocation` is validly signed
within grant 006 and exactly supersedes both unequal originals with the two
valid replacements. At `13:20:00Z`, revocation
`SYNTH-SUPERSESSION-AUTHORITY-R2-006@future-revocation` ends authority only for
future records. At `13:25:00Z`,
`SYNTH-SUPERSESSION-EQUAL-014@record-after-first-revocation` is unauthorized
and supersedes nothing.

At `13:30:00Z`, grant
`SYNTH-SUPERSESSION-AUTHORITY-R2-007@regrant-after-first-revocation` is signed
under the same issuance authority. At `13:35:00Z`,
`SYNTH-SUPERSESSION-EQUAL-014@valid-record-after-regrant` is validly signed by
`synthetic-result-owner` under grant 007 and is evidence-effect redundant. At
`13:40:00Z`, revocation
`SYNTH-SUPERSESSION-AUTHORITY-R2-007@future-revocation` ends grant 007 authority
only for future records. At `13:45:00Z`,
`SYNTH-SUPERSESSION-EQUAL-014@record-after-second-revocation` is unauthorized
and supersedes nothing.

At `13:50:00Z`, grant
`SYNTH-SUPERSESSION-AUTHORITY-R2-008@regrant-after-second-revocation` is signed
by `synthetic-supersession-authority-owner` under the same issuance authority.
It is future-only and neither revives an old grant nor ratifies an earlier
unauthorized record. At `13:55:00Z`,
`SYNTH-SUPERSESSION-EQUAL-014@valid-record-after-second-regrant` is validly
signed by `synthetic-result-owner` under grant 008, independently names both
unequal originals and both valid replacements, and is evidence-effect
redundant.

At `14:00:00Z`, revocation
`SYNTH-SUPERSESSION-AUTHORITY-R2-008@future-revocation` is signed by
`synthetic-supersession-authority-owner` under
`synthetic-supersession-authority-issuance@r2`. It ends grant 008 authority only
for future records and does not undo any valid record. At `14:05:00Z`,
`SYNTH-SUPERSESSION-EQUAL-014@record-after-third-revocation` is signed by
`synthetic-result-owner` without current supersession authority. It names the
same originals and replacements, supersedes nothing, and remains negative
evidence.

## Three-Grant And Three-Revocation Lineage

Grants 006, 007, and 008 are distinct, future-only grants issued by
`synthetic-supersession-authority-owner` under
`synthetic-supersession-authority-issuance@r2`. Each authorizes exactly the
valid record signed while it is current. Each matching future-only revocation
ends only future authority. The three later valid records remain distinct even
though the second and third are effect-redundant. The four unauthorized
records remain distinct negative evidence and supersede nothing.

## Affected-Party, Data, And Legitimacy Check

All treatment, records, observations, actors, and authority are synthetic. No
real affected party, personal data, institution, or external system is
involved or represented. The data boundary is the immutable named fixture and
content identifiers. The legitimacy risk is retroactive authority laundering:
using a regrant to ratify an earlier unauthorized record, or a revocation to
erase an earlier valid one. Immutable validation prevents both moves.

## Result

The result is `bounded_pass`. The first valid record is sufficient for the
surviving all-`equal` evidence effect. The later two valid records change no
surviving evidence; the four unauthorized records remain visible negative
evidence and have no supersession effect. This result supports only `defer`.

## Residual Uncertainty, Correction, And Recovery

Negative evidence is preserved at
`synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`.
Correction owner is `synthetic-proving-plan-owner`. Stop on any source,
fixture, data, standing, authority, grant, revocation, record, replacement,
validation, or risk revision. Recovery preserves the complete lineage,
reverses only an affected valid record if its own authority or checksum later
fails, and restores `unresolved` only if no valid exact record remains. Exact
wake is an owner decision on returned defer support or any named revision.

## Permitted Disposition Return

Return `defer` to `synthetic-result-owner`. The score does not itself create a
disposition, modify candidate truth, transfer, graduate, deploy, contact,
publish, or perform external action.

## Frontier Verification

Verify the plan, trace, validation, all five observations, both replacements,
three grants, three revocations, seven supersession records, timestamps,
signers, authority scopes, pointers, and matching content IDs independently.
Confirm every unauthorized record remains negative evidence, all three valid
records had contemporaneous authority, later valid records are redundant, and
only the first valid record is required. Re-run stops, prohibited conclusions,
correction, recovery, non-effect, and exact-wake checks; preserve
`bounded_pass`, `defer`, no P8, and external action `none`.
