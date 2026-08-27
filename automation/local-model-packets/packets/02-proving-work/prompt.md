# Score a valid post-grant supersession without erasing earlier negative evidence

## Boundary

Write one complete synthetic Mechanism Design score fixture from only the
embedded evidence. Preserve an authorized clean r2 trace with one direct
`equal` observation and two direct `unequal` observations. Preserve an earlier
unauthorized record that exactly covers both unequal observations with valid
equal replacements but predates the r2 grant. Preserve the later future-only,
nonretroactive r2 grant. Then preserve one new immutable supersession record,
signed after and within that grant, that independently names both unequal
observations and valid replacements. The new record validly supersedes both
unequal originals; the original equal observation survives; the current
surviving evidence agrees on `equal`; and the bounded score is `bounded_pass`.
The earlier unauthorized record remains negative evidence and gains no
retroactive validity. `bounded_pass` supports only `defer`; it creates no owner
disposition or stronger claim. Do not create `CMD-0001-P8`, modify `CMD-0001`,
choose a disposition, or authorize contact, transfer, graduation, deployment,
publication, or external action. External action is `none`.

## Evidence

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-TEMPLATE.md">
A score keeps original evidence and supersession lineage visible. Exact
coverage, replacement validity, authority scope, authority timing, and the
identity of each supersession record are separate checks. A bounded result and
a later owner disposition remain separate decisions.
</evidence>

<evidence path="ROADMAP.md">
`CMD-0001` remains deferred. This fixture creates no P8, proving result for
`CMD-0001`, or candidate disposition.
</evidence>

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-NONRETROACTIVE-SUPERSESSION-AUTHORITY-BOUNDARY-FIXTURE.md">
The earlier record predates the future-only r2 grant by five minutes and
supersedes nothing. Its exact next wake is a new immutable supersession record
signed after and within the r2 grant.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-POST-GRANT-SUPERSESSION-001-HEADER">
Score `SYNTH-SCORE-POST-GRANT-SUPERSESSION-001@r2` concerns plan
`SYNTH-PROVE-POST-GRANT-SUPERSESSION-001@r2`, candidate
`SYNTH-CANDIDATE-POST-GRANT-SUPERSESSION-001@r2`, and source
`SYNTH-SOURCE-POST-GRANT-SUPERSESSION-001@r2` at revision
`synthetic-source-revision:post-grant-supersession-001-r2`. Treatment is
`synthetic`; result owner is `synthetic-result-owner`; execution authority is
`synthetic://authorization/SYNTH-POST-GRANT-SUPERSESSION-001@grant-r2`;
scorer is `synthetic-proving-scorer`; scored at `2026-08-27T14:14:44Z`;
external action is `none`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-POST-GRANT-SUPERSESSION-001-PACKAGE">
Plan, trace, validation, earlier-record, grant, new-record, and
authority-validation pointers are
`synthetic://plan/SYNTH-PROVE-POST-GRANT-SUPERSESSION-001@r2`,
`synthetic://trace/SYNTH-TRACE-POST-GRANT-SUPERSESSION-001@r2`,
`synthetic://validation/SYNTH-POST-GRANT-SUPERSESSION-001@r2`,
`synthetic://supersession/SYNTH-POST-GRANT-SUPERSESSION-001@record-before-grant`,
`synthetic://authority/SYNTH-POST-GRANT-SUPERSESSION-001@grant-r2`,
`synthetic://supersession/SYNTH-POST-GRANT-SUPERSESSION-001@record-after-grant`,
and
`synthetic://authority-validation/SYNTH-POST-GRANT-SUPERSESSION-001@r2`.
Their content identifiers are
`synthetic-content:plan-post-grant-supersession-001-r2`,
`synthetic-content:trace-post-grant-supersession-001-r2`,
`synthetic-content:validation-post-grant-supersession-001-r2`,
`synthetic-content:supersession-post-grant-supersession-001-record-before-grant`,
`synthetic-content:authority-post-grant-supersession-001-grant-r2`,
`synthetic-content:supersession-post-grant-supersession-001-record-after-grant`,
and
`synthetic-content:authority-validation-post-grant-supersession-001-r2`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-POST-GRANT-SUPERSESSION-001-PLAN">
Claim: one authorized synthetic normalization preserves both input pointers and
their equality relation at source revision r2. Falsifier: either pointer
changes, any valid unsuperseded direct observation records `unequal`, or any
invoked supersession lacked applicable authority when signed. `bounded_pass`
requires unchanged pointers, exact authorized supersession where invoked,
valid replacements, valid surviving observations, and agreement on `equal`.
`unresolved` applies when valid surviving direct evidence conflicts. Stop on
unauthorized operation or any source, fixture, data, standing, authority, or
risk revision. Prohibited conclusions are effectiveness, destination fit,
owner acceptance, deployment readiness, and external outcome.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-POST-GRANT-SUPERSESSION-001-TRACE">
The authorized r2 normalization ran with no deviation. Both pointers remained
unchanged; stops did not trigger; final state equals initial state. Valid direct
observations are `synthetic-observation:comparison-equal-009-r2` recording
`equal`, `synthetic-observation:comparison-unequal-009a-r2` recording `unequal`
at position `a`, and `synthetic-observation:comparison-unequal-009b-r2`
recording `unequal` at position `b`. All three are readable, in scope, and
provenance-valid. No real people, data, systems, or external actions were
involved.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-POST-GRANT-SUPERSESSION-001-EARLIER-RECORD">
At `2026-08-27T13:05:00Z`, immutable record
`SYNTH-SUPERSESSION-EQUAL-009@record-before-grant` was signed by
`synthetic-result-owner` while no r2 supersession authority existed. It exactly
names the two unequal originals and proposes
`synthetic-observation:comparison-equal-009a-corrected-r2` and
`synthetic-observation:comparison-equal-009b-corrected-r2`. Both replacements
are readable, in scope, chronology-valid, checksum-valid, and record `equal`.
The earlier record remains unauthorized and supersedes nothing.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-POST-GRANT-SUPERSESSION-001-GRANT">
At `2026-08-27T13:10:00Z`, immutable grant
`SYNTH-SUPERSESSION-AUTHORITY-R2-002@grant-after-earlier-record` was signed by
`synthetic-supersession-authority-owner` under
`synthetic-supersession-authority-issuance@r2`. It authorizes
`synthetic-result-owner` to sign future supersession records for source
revision `synthetic-source-revision:post-grant-supersession-001-r2` after the
grant time. It is nonretroactive, has no ratification effect, and does not
validate the earlier record.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-POST-GRANT-SUPERSESSION-001-NEW-RECORD">
At `2026-08-27T13:15:00Z`, immutable record
`SYNTH-SUPERSESSION-EQUAL-009@record-after-grant` was newly signed by
`synthetic-result-owner` under
`SYNTH-SUPERSESSION-AUTHORITY-R2-002@grant-after-earlier-record`. It does not
ratify, adopt, or reuse the earlier record as authority. Its own exact scope
names `synthetic-observation:comparison-unequal-009a-r2` and
`synthetic-observation:comparison-unequal-009b-r2`, and independently names the
two valid equal replacements. It covers no other observation. The record is
readable, immutable, source-r2-matched, chronology-valid, checksum-valid, and
signed five minutes after the grant. Its exact authorized effect is to
supersede the two named unequal originals with the two named valid equal
replacements.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-POST-GRANT-SUPERSESSION-001-VALIDATION">
Immutable validation by `synthetic-authority-validator` confirms: the earlier
record predates the grant and remains unauthorized; the grant is future-only
and nonretroactive; the new record is distinct, signed five minutes after the
grant, within source-r2 scope, and exactly covers both unequal originals; both
replacement artifacts are valid; the original equal observation is not
superseded. After applying only the new authorized record, surviving current
evidence is the original equal observation plus both valid equal replacements.
There is no surviving conflict.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-POST-GRANT-SUPERSESSION-001-CONTROLS">
One synthetic reviewer role represents standing; no real party or owner is
represented. Data is synthetic input only; risk and external action are
`none`. Preserve all three originals, both replacement artifacts, the earlier
unauthorized record, the nonretroactive grant, the later authorized record,
and validation at
`synthetic://negative-evidence/SYNTH-SCORE-POST-GRANT-SUPERSESSION-001@r2`.
Correction owner is `synthetic-proving-plan-owner`. Recovery preserves the
unchanged r2 treatment state and complete lineage, reverses only the new
record's supersession effect if its authority or checksum later fails, and
restores `unresolved` without erasing evidence. Exact next wake is an owner
decision on returned `defer` support, or a revision to source, trace, either
record, grant, replacement, validation, standing, authority, or risk.
</evidence>

## Work now

Draft
`proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-POST-GRANT-SUPERSESSION-AUTHORITY-BOUNDARY-FIXTURE.md`
with YAML frontmatter (`artifact_type:
synthetic_proving_score_post_grant_supersession_authority_boundary_fixture`,
`status: candidate_process_fixture`, `external_action: none`) and exactly these
body sections: `Use Boundary`, `Score Header`, `Frozen Plan And Evidence`,
`Claim And Decision Conditions`, `Observed Trace`, `Supersession Lineage And
Counterevidence`, `Affected-Party, Data, And Legitimacy Check`, `Result`,
`Residual Uncertainty, Correction, And Recovery`, `Permitted Disposition
Return`, and `Frontier Verification`.

Keep all three originals, both valid replacement artifacts, the earlier exact
but unauthorized record, grant time, new-record time, each five-minute order,
future-only nonretroactivity, distinct new-record authority, and surviving
equal evidence visible. Preserve every pointer, content identifier, signer,
authority scope, stop, prohibited conclusion, negative-evidence pointer,
correction owner, recovery, non-effect, and wake. In `Frontier Verification`,
explicitly check earlier-record nonauthority, grant nonretroactivity, distinct
post-grant record, exact coverage, valid replacements, record-after-grant
timing, preserved originals and lineage, no surviving conflict,
`bounded_pass`, disposition separation, and unchanged `CMD-0001` and
external-action state. First line must be `---`; close frontmatter with a later
line containing only `---`; immediately after frontmatter use the title
`# Synthetic Proving-Score Post-Grant-Supersession-Authority Boundary Fixture`;
use `##` for every named body section and deeper headings only within a named
section; do not use a code fence.

Return only the finished artifact.
