# Preserve all valid records through the second regrant's revocation

## Boundary

Write one complete synthetic proving-score fixture from only the embedded
evidence. Preserve the full three-grant, three-valid-record, two-revocation,
and three-unauthorized-record lineage. Then add one future-only revocation of
the second distinct regrant and one attempted record signed after that third
revocation. The revocation does not retroactively invalidate any record that
was valid when signed. The attempted post-revocation record is unauthorized
and supersedes nothing. All records remain visible; only the first valid record
is needed for the surviving all-`equal` evidence effect. Result remains
`bounded_pass`; disposition support remains `defer`. Do not modify `CMD-0001`,
create P8, or authorize external action.

## Frozen evidence

Use `proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-TEMPLATE.md`, `ROADMAP.md`, and
`proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-SECOND-REGRANT-AFTER-REVOCATION-AUTHORITY-BOUNDARY-FIXTURE.md`.
Freeze score `SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, plan
`SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, candidate
`SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, source
`SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, and revision
`synthetic-source-revision:second-regrant-second-revocation-001-r2`.
Treatment is synthetic; result owner is `synthetic-result-owner`; scorer is
`synthetic-proving-scorer`; external action is `none`.

The clean trace preserves originals
`synthetic-observation:comparison-equal-014-r2`,
`synthetic-observation:comparison-unequal-014a-r2`, and
`synthetic-observation:comparison-unequal-014b-r2`, plus valid replacements
`synthetic-observation:comparison-equal-014a-corrected-r2` and
`synthetic-observation:comparison-equal-014b-corrected-r2`. Both pointers are
unchanged; all originals are readable, in scope, and provenance-valid; the
replacements are chronology- and checksum-valid.

At `2026-08-27T13:05:00Z`,
`SYNTH-SUPERSESSION-EQUAL-014@record-before-grant` is unauthorized. At
`13:10:00Z`, grant
`SYNTH-SUPERSESSION-AUTHORITY-R2-006@grant-before-valid-record` is signed by
`synthetic-supersession-authority-owner` under
`synthetic-supersession-authority-issuance@r2`; it is future-only and
nonretroactive. At `13:15:00Z`,
`SYNTH-SUPERSESSION-EQUAL-014@valid-record-before-revocation` is validly signed
within grant 006 and exactly supersedes both unequal originals with the two
valid replacements. At `13:20:00Z`, future-only revocation
`SYNTH-SUPERSESSION-AUTHORITY-R2-006@future-revocation` ends authority only for
future records. At `13:25:00Z`,
`SYNTH-SUPERSESSION-EQUAL-014@record-after-first-revocation` is unauthorized
and supersedes nothing.

At `13:30:00Z`, grant
`SYNTH-SUPERSESSION-AUTHORITY-R2-007@regrant-after-first-revocation` is signed
under the same issuance authority. At `13:35:00Z`,
`SYNTH-SUPERSESSION-EQUAL-014@valid-record-after-regrant` is validly signed by
`synthetic-result-owner` under grant 007 and is evidence-effect redundant. At
`13:40:00Z`, future-only revocation
`SYNTH-SUPERSESSION-AUTHORITY-R2-007@future-revocation` ends grant 007 authority
only for future records. At `13:45:00Z`,
`SYNTH-SUPERSESSION-EQUAL-014@record-after-second-revocation` is unauthorized
and supersedes nothing.

At `13:50:00Z`, grant
`SYNTH-SUPERSESSION-AUTHORITY-R2-008@regrant-after-second-revocation` is signed
by `synthetic-supersession-authority-owner` under the same issuance authority.
It is future-only and does not revive either old grant or ratify an earlier
unauthorized record. At `13:55:00Z`,
`SYNTH-SUPERSESSION-EQUAL-014@valid-record-after-second-regrant` is validly
signed by `synthetic-result-owner` under grant 008, independently names both
unequal originals and both valid replacements, and is evidence-effect
redundant.

At `14:00:00Z`, future-only revocation
`SYNTH-SUPERSESSION-AUTHORITY-R2-008@future-revocation` is signed by
`synthetic-supersession-authority-owner` under
`synthetic-supersession-authority-issuance@r2`. It ends grant 008 authority
only for future records and does not undo any of the three valid records. At
`14:05:00Z`, attempted record
`SYNTH-SUPERSESSION-EQUAL-014@record-after-third-revocation` is signed by
`synthetic-result-owner` without current supersession authority. It names the
same exact originals and replacements, supersedes nothing, and remains
negative evidence.

Immutable authority validation preserves every record, confirms the four
unauthorized records remain negative evidence, keeps grants 006, 007, and 008
plus all three revocations distinct and future-only, recognizes all three
valid records under contemporaneous authority, and confirms the later two
valid records change no surviving evidence. Preserve plan, trace, validation,
every authority and supersession pointer, and matching content identifiers
under stem `synthetic-content:second-regrant-second-revocation-001-r2`.
Negative-evidence pointer is
`synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`.
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
`proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-SECOND-REGRANT-SECOND-REVOCATION-AUTHORITY-BOUNDARY-FIXTURE.md`
with frontmatter artifact type
`synthetic_proving_score_second_regrant_second_revocation_authority_boundary_fixture`,
status `candidate_process_fixture`, and external action `none`. Use title
`# Synthetic Proving-Score Second-Regrant Second-Revocation-Authority Boundary Fixture`
and exactly these `##` sections: `Use Boundary`, `Score Header`, `Frozen Plan
And Evidence`, `Claim And Decision Conditions`, `Observed Trace`, `Three-Grant
And Three-Revocation Lineage`, `Affected-Party, Data, And Legitimacy Check`,
`Result`, `Residual Uncertainty, Correction, And Recovery`, `Permitted
Disposition Return`, and `Frontier Verification`. Preserve all identifiers,
authority scopes, timestamps, pointers, content identifiers, stops, prohibited
conclusions, correction, recovery, non-effect, and exact wake. In `Residual
Uncertainty, Correction, And Recovery`, the sentence `Exact wake is an owner
decision on returned defer support or any named revision.` must appear
verbatim. Return only the finished artifact. The first line must be `---`; do
not use a code fence. Every named body section must use `##`.
