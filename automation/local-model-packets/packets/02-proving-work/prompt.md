# Score a nonretroactive supersession grant against an earlier record

## Boundary

Write one complete synthetic Mechanism Design score fixture from only the
embedded evidence. Preserve an authorized clean r2 trace with one direct
`equal` observation and two direct `unequal` observations. Preserve a later
immutable supersession record that exactly covers both `unequal` observations
with checksum-valid `equal` replacements, but was signed before any r2
supersession authority existed. Preserve a still-later current r2 authority
grant that is explicitly nonretroactive and authorizes only future
supersession records. Current authority does not ratify an earlier unauthorized
record. All original observations remain unsuperseded, the direct conflict
survives, and the result remains `unresolved` with `defer` support. Do not
create `CMD-0001-P8`, modify `CMD-0001`, choose a disposition, or authorize
contact, transfer, graduation, deployment, publication, or external action.
External action is `none`.

## Evidence

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-TEMPLATE.md">
A score keeps direct evidence visible until an applicable immutable record
explicitly supersedes it. Exact coverage, replacement validity, authority
scope, and authority timing are separate checks. A bounded result and a later
owner disposition remain separate decisions.
</evidence>

<evidence path="ROADMAP.md">
`CMD-0001` remains deferred. This fixture creates no P8, proving result for
`CMD-0001`, or candidate disposition.
</evidence>

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-STALE-SUPERSESSION-AUTHORITY-BOUNDARY-FIXTURE.md">
Complete exact coverage and valid replacement artifacts cannot manufacture
applicable authority. An authority record must cover the source revision and
the supersession act at the time that act occurs.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-NONRETROACTIVE-SUPERSESSION-001-HEADER">
Score `SYNTH-SCORE-NONRETROACTIVE-SUPERSESSION-001@r2` concerns plan
`SYNTH-PROVE-NONRETROACTIVE-SUPERSESSION-001@r2`, candidate
`SYNTH-CANDIDATE-NONRETROACTIVE-SUPERSESSION-001@r2`, and source
`SYNTH-SOURCE-NONRETROACTIVE-SUPERSESSION-001@r2` at revision
`synthetic-source-revision:nonretroactive-supersession-001-r2`. Treatment is
`synthetic`; result owner is `synthetic-result-owner`; execution authority is
`synthetic://authorization/SYNTH-NONRETROACTIVE-SUPERSESSION-001@grant-r2`;
scorer is `synthetic-proving-scorer`; scored at `2026-08-27T13:14:19Z`;
external action is `none`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-NONRETROACTIVE-SUPERSESSION-001-PACKAGE">
Plan, trace, validation, supersession, and authority-validation pointers are
`synthetic://plan/SYNTH-PROVE-NONRETROACTIVE-SUPERSESSION-001@r2`,
`synthetic://trace/SYNTH-TRACE-NONRETROACTIVE-SUPERSESSION-001@r2`,
`synthetic://validation/SYNTH-NONRETROACTIVE-SUPERSESSION-001@r2`,
`synthetic://supersession/SYNTH-NONRETROACTIVE-SUPERSESSION-001@record-before-grant`,
and
`synthetic://authority-validation/SYNTH-NONRETROACTIVE-SUPERSESSION-001@r2`.
Their content identifiers are
`synthetic-content:plan-nonretroactive-supersession-001-r2`,
`synthetic-content:trace-nonretroactive-supersession-001-r2`,
`synthetic-content:validation-nonretroactive-supersession-001-r2`,
`synthetic-content:supersession-nonretroactive-supersession-001-record-before-grant`,
and
`synthetic-content:authority-validation-nonretroactive-supersession-001-r2`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-NONRETROACTIVE-SUPERSESSION-001-PLAN">
Claim: one authorized synthetic normalization preserves both input pointers and
their equality relation at source revision r2. Falsifier: either pointer
changes, any valid unsuperseded direct observation records `unequal`, or a
purported supersession lacked authority when signed. `bounded_pass` requires
unchanged pointers, an applicable authorized supersession where invoked,
valid surviving observations, and agreement on `equal`. `unresolved` applies
when valid direct evidence conflicts or supersession authority was absent at
the asserted act. Stop on unauthorized operation or any source, fixture, data,
standing, authority, or risk revision. Prohibited conclusions are
effectiveness, destination fit, owner acceptance, deployment readiness, and
external outcome.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-NONRETROACTIVE-SUPERSESSION-001-TRACE">
The authorized r2 normalization ran with no deviation. Both pointers remained
unchanged; stops did not trigger; final state equals initial state. Valid
direct observations are
`synthetic-observation:comparison-equal-008-r2` recording `equal`,
`synthetic-observation:comparison-unequal-008a-r2` recording `unequal` at
position `a`, and
`synthetic-observation:comparison-unequal-008b-r2` recording `unequal` at
position `b`. All three are readable, in scope, and provenance-valid. No real
people, data, systems, or external actions were involved.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-NONRETROACTIVE-SUPERSESSION-001-RECORD">
At `2026-08-27T13:05:00Z`, immutable record
`SYNTH-SUPERSESSION-EQUAL-008@record-before-grant` was signed by
`synthetic-result-owner` while no r2 supersession authority existed. It exactly
names `synthetic-observation:comparison-unequal-008a-r2` and
`synthetic-observation:comparison-unequal-008b-r2`, proposing replacements
`synthetic-observation:comparison-equal-008a-corrected-r2` and
`synthetic-observation:comparison-equal-008b-corrected-r2`. Both replacements
are readable, in scope, chronology-valid, checksum-valid, and record `equal`
at their respective positions. The record does not cover
`synthetic-observation:comparison-equal-008-r2`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-NONRETROACTIVE-SUPERSESSION-001-AUTHORITY">
At `2026-08-27T13:10:00Z`, immutable grant
`SYNTH-SUPERSESSION-AUTHORITY-R2-001@grant-after-record` was signed by
`synthetic-supersession-authority-owner` under
`synthetic-supersession-authority-issuance@r2`. Its exact scope authorizes
`synthetic-result-owner` to sign future supersession records for source
revision `synthetic-source-revision:nonretroactive-supersession-001-r2` after
the grant time. It explicitly has no retroactive or ratification effect and
does not name or validate
`SYNTH-SUPERSESSION-EQUAL-008@record-before-grant`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-NONRETROACTIVE-SUPERSESSION-001-VALIDATION">
Immutable authority validation by `synthetic-authority-validator` confirms the
supersession record predates the grant by five minutes, no earlier delegation
or authority existed, and the grant is nonretroactive. The earlier record
therefore remains unauthorized despite exact coverage and valid replacements.
All three original r2 observations remain valid and unsuperseded; their
`equal`/`unequal` conflict survives.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-NONRETROACTIVE-SUPERSESSION-001-CONTROLS">
One synthetic reviewer role represents standing; no real party or owner is
represented. Data is synthetic input only; risk and external action are
`none`. Preserve the original conflict, earlier unauthorized record, later
nonretroactive grant, valid replacement artifacts, and timing mismatch at
`synthetic://negative-evidence/SYNTH-SCORE-NONRETROACTIVE-SUPERSESSION-001@r2`.
Correction owner is `synthetic-proving-plan-owner`. Recovery preserves the
unchanged r2 state, all original observations, both replacement artifacts, the
earlier record, the later grant, and authority-validation result. Exact next
wake is one new immutable supersession record signed after and within the r2
grant, an owner decision on returned `defer` support, or a revision to source,
trace, supersession, grant, authority validation, standing, authority, or risk.
</evidence>

## Work now

Draft
`proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-NONRETROACTIVE-SUPERSESSION-AUTHORITY-BOUNDARY-FIXTURE.md`
with YAML frontmatter (`artifact_type:
synthetic_proving_score_nonretroactive_supersession_authority_boundary_fixture`,
`status: candidate_process_fixture`, `external_action: none`) and exactly these
body sections: `Use Boundary`, `Score Header`, `Frozen Plan And Evidence`,
`Claim And Decision Conditions`, `Observed Trace`, `Evidence Grade And
Counterevidence`, `Affected-Party, Data, And Legitimacy Check`, `Result`,
`Residual Uncertainty, Correction, And Recovery`, `Permitted Disposition
Return`, and `Frontier Verification`.

Keep all three original observations, both valid replacement artifacts, exact
coverage, record time, grant time, the five-minute order, the future-only
scope, and nonretroactivity visible. Put record scope, grant scope, authority
validation, negative-evidence pointer, correction owner, recovery, and exact
wake in `Residual Uncertainty, Correction, And Recovery`, not in the
affected-party section. Preserve every identifier, content identifier, stop,
prohibited conclusion, non-effect, and wake. In `Frontier Verification`,
explicitly check exact coverage, valid replacements, record-before-grant
timing, nonretroactive future-only r2 authority, unchanged r2 originals,
surviving conflict, `unresolved`, disposition separation, and unchanged
`CMD-0001` and external-action state. First line must be `---`; close
frontmatter with a later line containing only `---`; immediately after
frontmatter use the title `# Synthetic Proving-Score Nonretroactive-Supersession-Authority Boundary Fixture`;
use `##` for every named body section
and deeper headings only within a named section; do not use a code fence.
Return only the finished artifact.
