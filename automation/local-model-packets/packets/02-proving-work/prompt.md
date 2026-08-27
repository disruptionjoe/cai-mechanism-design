# Preserve distinct regrant authority after a prior revocation

## Boundary

Write one complete synthetic proving-score fixture from only the embedded
evidence. Preserve the full pre-grant, valid-record, revocation, and
post-revocation negative lineage. Then add one distinct future-only regrant and
one new record signed after that regrant. The regrant does not reactivate the
revoked grant, ratify either unauthorized record, or erase negative evidence.
The new record independently names the exact two unequal originals and two
valid equal replacements; it is redundant with the still-valid earlier record
and creates no additional evidence effect. Surviving evidence remains
all-`equal`; result remains `bounded_pass`; disposition support remains
`defer`. Do not modify `CMD-0001`, create P8, or authorize external action.

## Frozen evidence

Use `proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-TEMPLATE.md`, `ROADMAP.md`, and
`proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-POST-RECORD-REVOCATION-AUTHORITY-BOUNDARY-FIXTURE.md`.
Freeze score `SYNTH-SCORE-POST-REVOCATION-REGRANT-001@r2`, plan
`SYNTH-PROVE-POST-REVOCATION-REGRANT-001@r2`, candidate
`SYNTH-CANDIDATE-POST-REVOCATION-REGRANT-001@r2`, source
`SYNTH-SOURCE-POST-REVOCATION-REGRANT-001@r2`, and revision
`synthetic-source-revision:post-revocation-regrant-001-r2`. Treatment is
synthetic; result owner is `synthetic-result-owner`; scorer is
`synthetic-proving-scorer`; external action is `none`.

The clean trace preserves originals
`synthetic-observation:comparison-equal-011-r2`,
`synthetic-observation:comparison-unequal-011a-r2`, and
`synthetic-observation:comparison-unequal-011b-r2`, plus valid replacements
`synthetic-observation:comparison-equal-011a-corrected-r2` and
`synthetic-observation:comparison-equal-011b-corrected-r2`. Both pointers are
unchanged; all originals are readable, in scope, and provenance-valid; the
replacements are also chronology- and checksum-valid.

At `2026-08-27T13:05:00Z`,
`SYNTH-SUPERSESSION-EQUAL-011@record-before-grant` is unauthorized. At
`13:10:00Z`, grant
`SYNTH-SUPERSESSION-AUTHORITY-R2-004@grant-before-valid-record` is signed by
`synthetic-supersession-authority-owner` under
`synthetic-supersession-authority-issuance@r2`; it is future-only and
nonretroactive. At `13:15:00Z`, record
`SYNTH-SUPERSESSION-EQUAL-011@valid-record-before-revocation` is validly signed
within grant 004 and exactly supersedes both unequal originals with the two
valid replacements. At `13:20:00Z`, future-only revocation
`SYNTH-SUPERSESSION-AUTHORITY-R2-004@future-revocation` ends authority only for
future records and does not undo the valid record. At `13:25:00Z`, attempted
record `SYNTH-SUPERSESSION-EQUAL-011@record-after-revocation` is unauthorized
and supersedes nothing.

At `13:30:00Z`, distinct grant
`SYNTH-SUPERSESSION-AUTHORITY-R2-005@regrant-after-revocation` is signed by the
same authority owner under `synthetic-supersession-authority-issuance@r2`. It
authorizes only future records for the named r2 source after that time; it does
not revive grant 004 or ratify prior records. At `13:35:00Z`, record
`SYNTH-SUPERSESSION-EQUAL-011@valid-record-after-regrant` is newly signed by
`synthetic-result-owner` under grant 005. It independently names both unequal
originals and both valid replacements, covers nothing else, and is readable,
immutable, source-matched, chronology-valid, and checksum-valid. Because the
13:15 record already validly superseded the same originals, this later record
is authorized but evidence-effect redundant and changes no surviving evidence.

Immutable authority validation preserves every record and confirms both
unauthorized records remain negative evidence, grant 004 and its revocation
retain their exact history, regrant 005 is distinct and future-only, both valid
records were signed within their own authority, and only the earlier valid
record is needed for surviving all-`equal` evidence. Preserve plan, trace,
validation, every authority and supersession pointer, and matching content
identifiers under the stem
`synthetic-content:post-revocation-regrant-001-r2`. Negative-evidence pointer
is
`synthetic://negative-evidence/SYNTH-SCORE-POST-REVOCATION-REGRANT-001@r2`.
Correction owner is `synthetic-proving-plan-owner`. Stop on any source,
fixture, data, standing, authority, grant, revocation, record, replacement,
validation, or risk revision. Prohibited conclusions are effectiveness,
destination fit, owner acceptance, deployment readiness, and external outcome.
Recovery preserves the complete lineage, reverses only the affected valid
record if its own authority or checksum later fails, and restores `unresolved`
only if no valid exact record remains. Exact wake is an owner decision on
returned defer support or any named revision.

## Work now

Draft
`proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-POST-REVOCATION-REGRANT-AUTHORITY-BOUNDARY-FIXTURE.md`
with frontmatter artifact type
`synthetic_proving_score_post_revocation_regrant_authority_boundary_fixture`,
status `candidate_process_fixture`, and external action `none`. Use title
`# Synthetic Proving-Score Post-Revocation-Regrant-Authority Boundary Fixture`
and exactly these `##` sections: `Use Boundary`, `Score Header`, `Frozen Plan
And Evidence`, `Claim And Decision Conditions`, `Observed Trace`,
`Supersession, Revocation, And Regrant Lineage`, `Affected-Party, Data, And
Legitimacy Check`, `Result`, `Residual Uncertainty, Correction, And Recovery`,
`Permitted Disposition Return`, and `Frontier Verification`. Preserve all
identifiers, authority scopes, timestamps, pointers, content identifiers,
stops, prohibited conclusions, correction, recovery, non-effect, and exact
wake. Return only the finished artifact.
