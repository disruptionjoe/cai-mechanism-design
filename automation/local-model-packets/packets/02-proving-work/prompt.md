# Score valid replacements under stale supersession authority

## Boundary

Write one complete synthetic Mechanism Design score fixture from only the
embedded evidence. Preserve an authorized clean trace with one direct `equal`
observation and two direct `unequal` observations. Preserve a later immutable
record that exactly names both `unequal` observations and two checksum-valid
`equal` replacements, but whose supersession authority is limited to source
revision r1 while the frozen score and trace concern changed source revision
r2. Exact coverage and valid replacements do not make stale authority current.
The original observations therefore remain unsuperseded, the direct conflict
survives, and the result remains `unresolved` with `defer` support. Do not
create `CMD-0001-P8`, modify `CMD-0001`, choose a disposition, or authorize
contact, transfer, graduation, deployment, publication, or external action.
External action is `none`.

## Evidence

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-TEMPLATE.md">
A score keeps direct evidence visible until an applicable immutable record
explicitly supersedes it. Coverage, replacement validity, and current
supersession authority are separate checks. A bounded result and a later owner
disposition remain separate decisions.
</evidence>

<evidence path="ROADMAP.md">
`CMD-0001` remains deferred. This fixture creates no P8, proving result for
`CMD-0001`, or candidate disposition.
</evidence>

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-COMPLETE-SUPERSESSION-UNVERIFIED-REPLACEMENT-BOUNDARY-FIXTURE.md">
Complete coverage cannot manufacture valid replacement evidence; likewise,
valid replacement evidence cannot manufacture current supersession authority.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-STALE-SUPERSESSION-001-HEADER">
Score `SYNTH-SCORE-STALE-SUPERSESSION-001@r2` concerns plan
`SYNTH-PROVE-STALE-SUPERSESSION-001@r2`, candidate
`SYNTH-CANDIDATE-STALE-SUPERSESSION-001@r2`, and source
`SYNTH-SOURCE-STALE-SUPERSESSION-001@r2` at revision
`synthetic-source-revision:stale-supersession-001-r2`. Treatment is
`synthetic`; result owner is `synthetic-result-owner`; execution authority is
`synthetic://authorization/SYNTH-STALE-SUPERSESSION-001@grant-r2`; scorer is
`synthetic-proving-scorer`; scored at `2026-08-27T12:14:29Z`; external action
is `none`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-STALE-SUPERSESSION-001-PACKAGE">
Plan, trace, validation, supersession, and authority-validation pointers are
`synthetic://plan/SYNTH-PROVE-STALE-SUPERSESSION-001@r2`,
`synthetic://trace/SYNTH-TRACE-STALE-SUPERSESSION-001@r2`,
`synthetic://validation/SYNTH-STALE-SUPERSESSION-001@r2`,
`synthetic://supersession/SYNTH-STALE-SUPERSESSION-001@record-r1`, and
`synthetic://authority-validation/SYNTH-STALE-SUPERSESSION-001@r2`. Their
content identifiers are
`synthetic-content:plan-stale-supersession-001-r2`,
`synthetic-content:trace-stale-supersession-001-r2`,
`synthetic-content:validation-stale-supersession-001-r2`,
`synthetic-content:supersession-stale-supersession-001-record-r1`, and
`synthetic-content:authority-validation-stale-supersession-001-r2`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-STALE-SUPERSESSION-001-PLAN">
Claim: one authorized synthetic normalization preserves both input pointers and
their equality relation at source revision r2. Falsifier: either pointer
changes, any valid unsuperseded direct observation records `unequal`, or a
purported supersession lacks current authority for r2. `bounded_pass` requires
unchanged pointers, current applicable supersession where invoked, valid
surviving observations, and agreement on `equal`. `unresolved` applies when
valid direct evidence conflicts or supersession authority is not current. Stop
on unauthorized operation or any source, fixture, data, standing, authority,
or risk revision. Prohibited conclusions are effectiveness, destination fit,
owner acceptance, deployment readiness, and external outcome.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-STALE-SUPERSESSION-001-TRACE">
The authorized r2 normalization ran with no deviation. Both pointers remained
unchanged; stops did not trigger; final state equals initial state. Valid direct
observations are `synthetic-observation:comparison-equal-007-r2` recording
`equal`, `synthetic-observation:comparison-unequal-007a-r2` recording `unequal`
at position `a`, and
`synthetic-observation:comparison-unequal-007b-r2` recording `unequal` at
position `b`. All three are readable, in scope, and provenance-valid. No real
people, data, systems, or external actions were involved.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-STALE-SUPERSESSION-001-RECORD">
Later immutable record `SYNTH-SUPERSESSION-EQUAL-007@record-r1` is signed by
`synthetic-result-owner` under
`synthetic-result-owner-supersession-source-r1@r1`. It exactly names
`synthetic-observation:comparison-unequal-007a-r2` and
`synthetic-observation:comparison-unequal-007b-r2`, proposing replacements
`synthetic-observation:comparison-equal-007a-corrected-r2` and
`synthetic-observation:comparison-equal-007b-corrected-r2`. Both replacements
are readable, in scope, chronology-valid, checksum-valid, and record `equal` at
their respective positions. The record does not cover
`synthetic-observation:comparison-equal-007-r2`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-STALE-SUPERSESSION-001-AUTHORITY">
Immutable authority validation by `synthetic-authority-validator` shows that
`synthetic-result-owner-supersession-source-r1@r1` applies only to source
revision `synthetic-source-revision:stale-supersession-001-r1`. No delegation,
continuation, or renewed authority exists for r2. The r1 authority therefore
cannot supersede any r2 observation. All three original r2 observations remain
valid and unsuperseded; their `equal`/`unequal` conflict survives.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-STALE-SUPERSESSION-001-CONTROLS">
One synthetic reviewer role represents standing; no real party or owner is
represented. Data is synthetic input only; risk and external action are
`none`. Preserve the original conflict, stale record, valid replacement
artifacts, and authority mismatch at
`synthetic://negative-evidence/SYNTH-SCORE-STALE-SUPERSESSION-001@r2`.
Correction owner is `synthetic-proving-plan-owner`. Recovery preserves the
unchanged r2 state, all original observations, both replacement artifacts, the
stale authority record, and authority-validation result. Exact next wake is one
immutable supersession authority valid for source revision r2, an owner
decision on returned `defer` support, or a revision to source, trace,
supersession, authority validation, standing, authority, or risk.
</evidence>

## Work now

Draft
`proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-STALE-SUPERSESSION-AUTHORITY-BOUNDARY-FIXTURE.md`
with YAML frontmatter (`artifact_type:
synthetic_proving_score_stale_supersession_authority_boundary_fixture`,
`status: candidate_process_fixture`, `external_action: none`) and exactly these
body sections: `Use Boundary`, `Score Header`, `Frozen Plan And Evidence`,
`Claim And Decision Conditions`, `Observed Trace`, `Evidence Grade And
Counterevidence`, `Affected-Party, Data, And Legitimacy Check`, `Result`,
`Residual Uncertainty, Correction, And Recovery`, `Permitted Disposition
Return`, and `Frontier Verification`.

Keep all three original observations, both valid replacement artifacts, exact
coverage, r1-only authority, and r2 mismatch visible. Put record scope,
authority validation, negative-evidence pointer, correction owner, recovery,
and exact wake in `Residual Uncertainty, Correction, And Recovery`, not in the
affected-party section. Preserve every identifier, content identifier, stop,
prohibited conclusion, non-effect, and wake. In `Frontier Verification`,
explicitly check exact coverage, valid replacements, r1-only authority,
unchanged r2 originals, surviving conflict, `unresolved`, disposition
separation, and unchanged `CMD-0001` and external-action state. First line must
be `---`; close frontmatter with a later line containing only `---`;
immediately after frontmatter use the title `# Synthetic Proving-Score Stale-
Supersession-Authority Boundary Fixture`; use `##` for every named body section
and deeper headings only within a named section; do not use a code fence.
Return only the finished artifact.
