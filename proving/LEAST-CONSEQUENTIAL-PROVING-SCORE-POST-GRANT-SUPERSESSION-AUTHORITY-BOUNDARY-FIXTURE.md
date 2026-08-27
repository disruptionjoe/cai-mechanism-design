---
artifact_type: synthetic_proving_score_post_grant_supersession_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---
# Synthetic Proving-Score Post-Grant-Supersession-Authority Boundary Fixture

## Use Boundary

This fixture preserves original evidence and supersession lineage without
erasing earlier negative evidence. It does not create `CMD-0001-P8`, modify
`CMD-0001`, or authorize contact, transfer, graduation, deployment,
publication, or external action. External action is `none`. The bounded result
is `bounded_pass`, which supports only `defer`; it creates no owner disposition
or stronger claim. The earlier unauthorized record remains negative evidence
and gains no retroactive validity. The later future-only, nonretroactive r2
grant remains distinct from the valid record signed after it.

## Score Header

Score `SYNTH-SCORE-POST-GRANT-SUPERSESSION-001@r2` concerns plan
`SYNTH-PROVE-POST-GRANT-SUPERSESSION-001@r2`, candidate
`SYNTH-CANDIDATE-POST-GRANT-SUPERSESSION-001@r2`, and source
`SYNTH-SOURCE-POST-GRANT-SUPERSESSION-001@r2` at revision
`synthetic-source-revision:post-grant-supersession-001-r2`. Treatment is
`synthetic`; result owner is `synthetic-result-owner`; execution authority is
`synthetic://authorization/SYNTH-POST-GRANT-SUPERSESSION-001@grant-r2`;
scorer is `synthetic-proving-scorer`; scored at `2026-08-27T14:14:44Z`;
external action is `none`.

## Frozen Plan And Evidence

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
`CMD-0001` remains deferred.

## Claim And Decision Conditions

Claim: one authorized synthetic normalization preserves both input pointers
and their equality relation at source revision r2. Falsifier: either pointer
changes, any valid unsuperseded direct observation records `unequal`, or any
invoked supersession lacked applicable authority when signed. `bounded_pass`
requires unchanged pointers, exact authorized supersession where invoked,
valid replacements, valid surviving observations, and agreement on `equal`.
`unresolved` applies when valid surviving direct evidence conflicts. Stop on
unauthorized operation or any source, fixture, data, standing, authority, or
risk revision. Prohibited conclusions are effectiveness, destination fit,
owner acceptance, deployment readiness, and external outcome.

## Observed Trace

The authorized r2 normalization ran with no deviation. Both pointers remained
unchanged; stops did not trigger; final state equals initial state. Valid
direct observations are `synthetic-observation:comparison-equal-009-r2`
recording `equal`, `synthetic-observation:comparison-unequal-009a-r2`
recording `unequal` at position `a`, and
`synthetic-observation:comparison-unequal-009b-r2` recording `unequal` at
position `b`. All three are readable, in scope, and provenance-valid. No real
people, data, systems, or external actions were involved.

## Supersession Lineage And Counterevidence

At `2026-08-27T13:05:00Z`, immutable record
`SYNTH-SUPERSESSION-EQUAL-009@record-before-grant` was signed by
`synthetic-result-owner` while no r2 supersession authority existed. It
exactly names the two unequal originals and proposes
`synthetic-observation:comparison-equal-009a-corrected-r2` and
`synthetic-observation:comparison-equal-009b-corrected-r2`. Both replacements
are readable, in scope, chronology-valid, checksum-valid, and record `equal`.
The earlier record remains unauthorized and supersedes nothing, preserved as
negative evidence at
`synthetic://negative-evidence/SYNTH-SCORE-POST-GRANT-SUPERSESSION-001@r2`.

At `2026-08-27T13:10:00Z`, immutable grant
`SYNTH-SUPERSESSION-AUTHORITY-R2-002@grant-after-earlier-record` was signed by
`synthetic-supersession-authority-owner` under
`synthetic-supersession-authority-issuance@r2`. It authorizes
`synthetic-result-owner` to sign future supersession records for source
revision `synthetic-source-revision:post-grant-supersession-001-r2` after the
grant time. It is nonretroactive, has no ratification effect, and does not
validate the earlier record.

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

## Affected-Party, Data, And Legitimacy Check

One synthetic reviewer role represents standing; no real party or owner is
represented. Data is synthetic input only; risk and external action are
`none`. Preserve all three originals, both replacement artifacts, the earlier
exact but unauthorized record, the nonretroactive grant, the later authorized
record, and validation. Correction owner is
`synthetic-proving-plan-owner`. Recovery preserves the unchanged r2 treatment
state and complete lineage, reverses only the new record's supersession effect
if its authority or checksum later fails, and restores `unresolved` without
erasing evidence.

## Result

The bounded score is `bounded_pass`. This supports only `defer` and creates no
owner disposition or stronger claim. The new immutable supersession record
validly supersedes both unequal originals. The original equal observation is
not superseded, so current surviving evidence is the original equal
observation plus both valid equal replacements, with no surviving conflict.

## Residual Uncertainty, Correction, And Recovery

Exact next wake is an owner decision on returned `defer` support, or a revision
to source, trace, either record, grant, replacement, validation, standing,
authority, or risk. Recovery preserves the unchanged r2 treatment state and
complete lineage, reverses only the new record's supersession effect if its
authority or checksum later fails, and restores `unresolved` without erasing
evidence.

## Permitted Disposition Return

Disposition support is `defer`. No external action is permitted. No owner
disposition or stronger claim is created.

## Frontier Verification

Frontier Verification confirms earlier-record nonauthority, grant
nonretroactivity, the distinct post-grant record, exact coverage, valid
replacements, record-after-grant timing, preserved originals and lineage, and
the absence of surviving conflict. It confirms `bounded_pass` remains separate
from owner disposition, `CMD-0001` remains unchanged, and external-action state
is `none`.
