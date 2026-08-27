---
artifact_type: synthetic_proving_score_post_regrant_revocation_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Proving-Score Post-Regrant-Revocation-Authority Boundary Fixture

## Use Boundary

This fixture preserves the complete pre-grant, valid-record, first-revocation,
post-first-revocation negative, distinct-regrant, authorized redundant-record,
second-revocation, and post-second-revocation negative lineage. Neither
revocation retroactively invalidates a record that was valid when signed. Both
valid records remain visible, but only the first is needed for the surviving
evidence effect. Surviving evidence remains all-`equal`; the result remains
`bounded_pass`; disposition support remains `defer`. It does not modify
`CMD-0001`, create P8, or authorize external action.

## Score Header

- Score: `SYNTH-SCORE-POST-REGRANT-REVOCATION-001@r2`
- Plan: `SYNTH-PROVE-POST-REGRANT-REVOCATION-001@r2`
- Candidate: `SYNTH-CANDIDATE-POST-REGRANT-REVOCATION-001@r2`
- Source: `SYNTH-SOURCE-POST-REGRANT-REVOCATION-001@r2`
- Source revision:
  `synthetic-source-revision:post-regrant-revocation-001-r2`
- Treatment: `synthetic`
- Result owner: `synthetic-result-owner`
- Scorer: `synthetic-proving-scorer`
- External action: `none`

## Frozen Plan And Evidence

The clean trace preserves originals
`synthetic-observation:comparison-equal-012-r2`,
`synthetic-observation:comparison-unequal-012a-r2`, and
`synthetic-observation:comparison-unequal-012b-r2`, plus valid replacements
`synthetic-observation:comparison-equal-012a-corrected-r2` and
`synthetic-observation:comparison-equal-012b-corrected-r2`. Both pointers are
unchanged. All originals are readable, in scope, and provenance-valid; both
replacements are chronology- and checksum-valid.

Preserve plan, trace, validation, every authority and supersession pointer,
and matching content identifiers under the stem
`synthetic-content:post-regrant-revocation-001-r2`. Negative-evidence pointer
is
`synthetic://negative-evidence/SYNTH-SCORE-POST-REGRANT-REVOCATION-001@r2`.

## Claim And Decision Conditions

The bounded question is whether authority validation preserves every record,
keeps three unauthorized records as negative evidence, preserves grants 006
and 007 plus both future-only revocations, recognizes both valid records under
their own contemporaneous authority, and leaves only the first valid record
necessary for the all-`equal` surviving evidence effect.

The fixture cannot establish effectiveness, destination fit, owner acceptance,
deployment readiness, or external outcome.

## Observed Trace

At `2026-08-27T13:05:00Z`,
`SYNTH-SUPERSESSION-EQUAL-012@record-before-grant` is unauthorized. At
`13:10:00Z`, grant
`SYNTH-SUPERSESSION-AUTHORITY-R2-006@grant-before-valid-record` is signed by
`synthetic-supersession-authority-owner` under
`synthetic-supersession-authority-issuance@r2`; it is future-only and
nonretroactive. At `13:15:00Z`,
`SYNTH-SUPERSESSION-EQUAL-012@valid-record-before-revocation` is validly signed
within grant 006 and exactly supersedes both unequal originals with the two
valid replacements.

At `13:20:00Z`, future-only revocation
`SYNTH-SUPERSESSION-AUTHORITY-R2-006@future-revocation` ends authority only for
future records and does not undo the valid record. At `13:25:00Z`, attempted
record `SYNTH-SUPERSESSION-EQUAL-012@record-after-first-revocation` is
unauthorized and supersedes nothing.

## Supersession, Revocation, Regrant, And Second-Revocation Lineage

At `13:30:00Z`, distinct grant
`SYNTH-SUPERSESSION-AUTHORITY-R2-007@regrant-after-first-revocation` is signed
by the same authority owner under
`synthetic-supersession-authority-issuance@r2`. It authorizes only future
records for the named r2 source and does not revive grant 006 or ratify prior
records.

At `13:35:00Z`,
`SYNTH-SUPERSESSION-EQUAL-012@valid-record-after-regrant` is newly signed by
`synthetic-result-owner` under grant 007. It independently names both unequal
originals and both valid replacements, covers nothing else, and is readable,
immutable, source-matched, chronology-valid, and checksum-valid. Because the
13:15 record already validly superseded the same originals, the 13:35 record is
authorized but evidence-effect redundant and changes no surviving evidence.

At `13:40:00Z`, future-only revocation
`SYNTH-SUPERSESSION-AUTHORITY-R2-007@future-revocation` is signed by
`synthetic-supersession-authority-owner` under
`synthetic-supersession-authority-issuance@r2`. It ends grant 007 authority only
for future records and does not undo either valid record. At `13:45:00Z`,
attempted record
`SYNTH-SUPERSESSION-EQUAL-012@record-after-second-revocation` is signed by
`synthetic-result-owner` without current supersession authority. It names the
same exact originals and replacements, supersedes nothing, and remains
negative evidence.

## Affected-Party, Data, And Legitimacy Check

The treatment and all evidence are synthetic. No real affected party, field
data, deployment, destination owner, or external action is involved. Immutable
authority validation preserves all records and their chronology rather than
silently ratifying, erasing, or rewriting an unauthorized record. The
correction owner is `synthetic-proving-plan-owner`.

Stop on any source, fixture, data, standing, authority, grant, revocation,
record, replacement, validation, or risk revision. Prohibited conclusions are
effectiveness, destination fit, owner acceptance, deployment readiness, and
external outcome.

## Result

Three unauthorized records remain negative evidence. Grants 006 and 007 and
both revocations remain visible and future-only. Both valid records were signed
within their own authority. Only the 13:15 valid record is needed to establish
the surviving all-`equal` evidence. The bounded result is `bounded_pass`.

## Residual Uncertainty, Correction, And Recovery

This score does not decide candidate disposition or any destination-owner
question. Recovery preserves the complete lineage, reverses only the affected
valid record if its own authority or checksum later fails, and restores
`unresolved` only if no valid exact record remains.

Exact wake is an owner decision on returned defer support or any named revision.

## Permitted Disposition Return

`bounded_pass` supports only `defer`. It creates no owner disposition, P8,
effectiveness claim, transfer, graduation, deployment, or external action.

## Frontier Verification

Verify unchanged source, plan, score, pointers, content-identifier stem,
originals, replacements, and exact chronology. Verify pre-grant nonauthority;
grant 006 scope; the first valid record; first future-only revocation; the
post-first-revocation negative; distinct future-only grant 007; the later
record's own authority, exact coverage, and redundancy; second future-only
revocation; the post-second-revocation negative; and preservation of both valid
records. Verify all-`equal`, `bounded_pass`, `defer`, correction, recovery,
stops, prohibited conclusions, exact wake, unchanged `CMD-0001`, no P8, and
external action `none`.
