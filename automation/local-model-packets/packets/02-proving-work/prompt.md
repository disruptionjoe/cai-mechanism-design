# Preserve a valid supersession after future-only authority revocation

## Boundary

Write one complete synthetic Mechanism Design score fixture from only the
embedded evidence. Preserve an authorized clean r2 trace with one direct
`equal` observation and two direct `unequal` observations. Preserve the earlier
unauthorized supersession record, the future-only r2 grant, and the distinct
valid supersession record signed five minutes after that grant. Then preserve
one future-only revocation signed five minutes after the valid record and one
later attempted record signed five minutes after revocation. The revocation
ends authority only for future records; it does not retroactively invalidate
the already-valid record. The later attempted record is unauthorized and
supersedes nothing. The valid record still supersedes both unequal originals;
the original equal observation and both valid equal replacements survive; the
current evidence agrees on `equal`; and the bounded score remains
`bounded_pass`. Preserve both unauthorized records as negative evidence.
`bounded_pass` supports only `defer`; it creates no owner disposition or
stronger claim. Do not create `CMD-0001-P8`, modify `CMD-0001`, choose a
disposition, or authorize contact, transfer, graduation, deployment,
publication, or external action. External action is `none`.

## Evidence

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-TEMPLATE.md">
A score keeps original evidence and supersession lineage visible. Exact
coverage, replacement validity, authority scope, authority timing, revocation
scope, and the identity of each record are separate checks. A bounded result
and a later owner disposition remain separate decisions.
</evidence>

<evidence path="ROADMAP.md">
`CMD-0001` remains deferred. This fixture creates no P8, proving result for
`CMD-0001`, or candidate disposition.
</evidence>

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-POST-GRANT-SUPERSESSION-AUTHORITY-BOUNDARY-FIXTURE.md">
The earlier record at `2026-08-27T13:05:00Z` predates the future-only r2 grant
at `2026-08-27T13:10:00Z` and supersedes nothing. The distinct record at
`2026-08-27T13:15:00Z` was signed after and within the grant, validly
supersedes both unequal originals, and yields surviving all-`equal` evidence.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-POST-RECORD-REVOCATION-001-HEADER">
Score `SYNTH-SCORE-POST-RECORD-REVOCATION-001@r2` concerns plan
`SYNTH-PROVE-POST-RECORD-REVOCATION-001@r2`, candidate
`SYNTH-CANDIDATE-POST-RECORD-REVOCATION-001@r2`, and source
`SYNTH-SOURCE-POST-RECORD-REVOCATION-001@r2` at revision
`synthetic-source-revision:post-record-revocation-001-r2`. Treatment is
`synthetic`; result owner is `synthetic-result-owner`; execution authority is
`synthetic://authorization/SYNTH-POST-RECORD-REVOCATION-001@grant-r2`;
scorer is `synthetic-proving-scorer`; scored at `2026-08-27T15:13:59Z`;
external action is `none`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-POST-RECORD-REVOCATION-001-PACKAGE">
Plan, trace, validation, pre-grant record, grant, valid record, revocation,
post-revocation attempted record, and authority-validation pointers are
`synthetic://plan/SYNTH-PROVE-POST-RECORD-REVOCATION-001@r2`,
`synthetic://trace/SYNTH-TRACE-POST-RECORD-REVOCATION-001@r2`,
`synthetic://validation/SYNTH-POST-RECORD-REVOCATION-001@r2`,
`synthetic://supersession/SYNTH-POST-RECORD-REVOCATION-001@record-before-grant`,
`synthetic://authority/SYNTH-POST-RECORD-REVOCATION-001@grant-r2`,
`synthetic://supersession/SYNTH-POST-RECORD-REVOCATION-001@valid-record`,
`synthetic://authority/SYNTH-POST-RECORD-REVOCATION-001@future-revocation`,
`synthetic://supersession/SYNTH-POST-RECORD-REVOCATION-001@record-after-revocation`,
and
`synthetic://authority-validation/SYNTH-POST-RECORD-REVOCATION-001@r2`.
Their content identifiers are
`synthetic-content:plan-post-record-revocation-001-r2`,
`synthetic-content:trace-post-record-revocation-001-r2`,
`synthetic-content:validation-post-record-revocation-001-r2`,
`synthetic-content:supersession-post-record-revocation-001-record-before-grant`,
`synthetic-content:authority-post-record-revocation-001-grant-r2`,
`synthetic-content:supersession-post-record-revocation-001-valid-record`,
`synthetic-content:authority-post-record-revocation-001-future-revocation`,
`synthetic-content:supersession-post-record-revocation-001-record-after-revocation`,
and
`synthetic-content:authority-validation-post-record-revocation-001-r2`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-POST-RECORD-REVOCATION-001-PLAN">
Claim: one authorized synthetic normalization preserves both input pointers and
their equality relation at source revision r2. Falsifier: either pointer
changes, any valid unsuperseded direct observation records `unequal`, or any
invoked supersession lacked applicable authority when signed. `bounded_pass`
requires unchanged pointers, exact authorized supersession where invoked,
valid replacements, valid surviving observations, and agreement on `equal`.
`unresolved` applies when valid surviving direct evidence conflicts. Stop on
unauthorized operation or any source, fixture, data, standing, authority,
revocation, or risk revision. Prohibited conclusions are effectiveness,
destination fit, owner acceptance, deployment readiness, and external outcome.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-POST-RECORD-REVOCATION-001-TRACE">
The authorized r2 normalization ran with no deviation. Both pointers remained
unchanged; stops did not trigger; final state equals initial state. Valid
direct observations are `synthetic-observation:comparison-equal-010-r2`
recording `equal`, `synthetic-observation:comparison-unequal-010a-r2`
recording `unequal` at position `a`, and
`synthetic-observation:comparison-unequal-010b-r2` recording `unequal` at
position `b`. All three are readable, in scope, and provenance-valid. Valid
replacement artifacts are
`synthetic-observation:comparison-equal-010a-corrected-r2` and
`synthetic-observation:comparison-equal-010b-corrected-r2`; both are readable,
in scope, chronology-valid, checksum-valid, and record `equal`. No real people,
data, systems, or external actions were involved.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-POST-RECORD-REVOCATION-001-LINEAGE">
At `2026-08-27T13:05:00Z`, immutable record
`SYNTH-SUPERSESSION-EQUAL-010@record-before-grant` was signed by
`synthetic-result-owner` while no r2 supersession authority existed. It exactly
names both unequal originals and both valid equal replacements but remains
unauthorized and supersedes nothing. At `2026-08-27T13:10:00Z`, immutable grant
`SYNTH-SUPERSESSION-AUTHORITY-R2-003@grant-before-valid-record` was signed by
`synthetic-supersession-authority-owner` under
`synthetic-supersession-authority-issuance@r2`. It authorizes
`synthetic-result-owner` to sign future supersession records for source
revision `synthetic-source-revision:post-record-revocation-001-r2` after grant
time until a valid future revocation. It is nonretroactive and does not ratify
the earlier record. At `2026-08-27T13:15:00Z`, immutable record
`SYNTH-SUPERSESSION-EQUAL-010@valid-record-before-revocation` was newly signed
by `synthetic-result-owner` under
`SYNTH-SUPERSESSION-AUTHORITY-R2-003@grant-before-valid-record`. Its own exact
scope independently names both unequal originals and both valid equal
replacements, covers no other observation, and is readable, immutable,
source-r2-matched, chronology-valid, checksum-valid, and signed five minutes
after grant. Its exact authorized effect is to supersede the two named unequal
originals with the two named valid equal replacements.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-POST-RECORD-REVOCATION-001-REVOCATION">
At `2026-08-27T13:20:00Z`, immutable revocation
`SYNTH-SUPERSESSION-AUTHORITY-R2-003@future-revocation` was signed by
`synthetic-supersession-authority-owner` under
`synthetic-supersession-authority-issuance@r2`. It ends
`synthetic-result-owner` authority to sign new supersession records for the
named r2 source after revocation time. It is future-only, nonretroactive, has
no undo or invalidation effect on the valid `13:15:00Z` record, and does not
erase any original, replacement, or negative evidence. At
`2026-08-27T13:25:00Z`, immutable attempted record
`SYNTH-SUPERSESSION-EQUAL-010@record-after-revocation` was signed by
`synthetic-result-owner`. It exactly names the same unequal originals and
valid replacements, but the signer lacks authority at its signing time. It
supersedes nothing, changes no surviving evidence, and remains negative
evidence distinct from both the pre-grant record and valid record.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-POST-RECORD-REVOCATION-001-VALIDATION">
Immutable validation by `synthetic-authority-validator` confirms: the pre-grant
record remains unauthorized; the grant is future-only and nonretroactive; the
valid record is distinct, exactly covers both unequal originals, names two
valid replacements, and was signed within authority; the later revocation is
future-only and does not undo that record; the post-revocation attempted
record is unauthorized and supersedes nothing; the original equal observation
is not superseded. Applying only the valid record leaves the original equal
observation plus both valid equal replacements. There is no surviving conflict.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-POST-RECORD-REVOCATION-001-CONTROLS">
One synthetic reviewer role represents standing; no real party or owner is
represented. Data is synthetic input only; risk and external action are
`none`. Preserve all three originals, both replacement artifacts, both
unauthorized records, the nonretroactive grant, the valid record, the
future-only revocation, and validation at
`synthetic://negative-evidence/SYNTH-SCORE-POST-RECORD-REVOCATION-001@r2`.
Correction owner is `synthetic-proving-plan-owner`. Recovery preserves the
unchanged r2 treatment state and complete lineage, reverses only the valid
record's effect if its original authority or checksum later fails, and restores
`unresolved` without erasing evidence. Exact next wake is an owner decision on
returned `defer` support, or a revision to source, trace, any record, grant,
revocation, replacement, validation, standing, authority, or risk.
</evidence>

## Work now

Draft
`proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-POST-RECORD-REVOCATION-AUTHORITY-BOUNDARY-FIXTURE.md`
with YAML frontmatter (`artifact_type:
synthetic_proving_score_post_record_revocation_authority_boundary_fixture`,
`status: candidate_process_fixture`, `external_action: none`) and exactly these
body sections: `Use Boundary`, `Score Header`, `Frozen Plan And Evidence`,
`Claim And Decision Conditions`, `Observed Trace`, `Supersession And Revocation
Lineage`, `Affected-Party, Data, And Legitimacy Check`, `Result`, `Residual
Uncertainty, Correction, And Recovery`, `Permitted Disposition Return`, and
`Frontier Verification`.

Keep all three originals, both valid replacements, both unauthorized records,
grant, valid record, future-only revocation, every five-minute order, and
surviving equal evidence visible. Preserve every pointer, content identifier,
signer, authority scope, stop, prohibited conclusion, negative-evidence
pointer, correction owner, recovery, non-effect, and exact wake. In `Frontier
Verification`, explicitly check pre-grant nonauthority, grant timing, valid-
record authority, exact coverage, valid replacements, revocation timing and
nonretroactivity, post-revocation nonauthority, preserved originals and
lineage, no surviving conflict, `bounded_pass`, disposition separation, and
unchanged `CMD-0001` and external-action state. First line must be `---`; close
frontmatter with a later line containing only `---`; immediately after
frontmatter use the title `# Synthetic Proving-Score Post-Record-Revocation-
Authority Boundary Fixture`; use `##` for every named body section and deeper
headings only within a named section; do not use a code fence.

Return only the finished artifact.
