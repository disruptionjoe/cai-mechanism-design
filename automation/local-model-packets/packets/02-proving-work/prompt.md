# Score incomplete supersession coverage across conflicting observations

## Boundary

Write one complete synthetic Mechanism Design score fixture from only the
embedded evidence. Preserve the authorized trace, clean stop state, one direct
`equal` observation, two direct `unequal` observations, and a later immutable
result-owner supersession record that covers only one `unequal` observation.
The uncovered `equal` and `unequal` observations remain conflicting, so the
result remains `unresolved` with `defer` support. Do not treat otherwise-valid
authority as broader than its explicit coverage. Do not create `CMD-0001-P8`,
modify `CMD-0001`, choose a disposition, or authorize contact, transfer,
graduation, deployment, publication, or external action. External action is
`none`.

## Evidence

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-TEMPLATE.md">
A score keeps direct evidence visible until an applicable immutable record
explicitly supersedes it. Valid authority operates only over the observations
and relation named in its exact scope.
</evidence>

<evidence path="ROADMAP.md">
`CMD-0001` remains deferred. This fixture creates no P8, proving result for
`CMD-0001`, or candidate disposition.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-PARTIAL-SUPERSESSION-001-HEADER">
Score `SYNTH-SCORE-PARTIAL-SUPERSESSION-001@r1` concerns plan
`SYNTH-PROVE-PARTIAL-SUPERSESSION-001@r1`, candidate
`SYNTH-CANDIDATE-PARTIAL-SUPERSESSION-001@r1`, and source
`SYNTH-SOURCE-PARTIAL-SUPERSESSION-001@r1`. Treatment is `synthetic`; result
owner is `synthetic-result-owner`; execution authority is
`synthetic://authorization/SYNTH-PARTIAL-SUPERSESSION-001@grant-r1`; scorer is
`synthetic-proving-scorer`; scored at `2026-08-27T09:13:57Z`; external action
is `none`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-PARTIAL-SUPERSESSION-001-PACKAGE">
Plan, request, fixture, trace, validation, and supersession pointers are
respectively `synthetic://plan/SYNTH-PROVE-PARTIAL-SUPERSESSION-001@r1`,
`synthetic://request/SYNTH-REQUEST-PARTIAL-SUPERSESSION-001@r1`,
`synthetic://fixture/SYNTH-PARTIAL-SUPERSESSION-001@r1`,
`synthetic://trace/SYNTH-TRACE-PARTIAL-SUPERSESSION-001@r1`,
`synthetic://validation/SYNTH-PARTIAL-SUPERSESSION-001@r1`, and
`synthetic://supersession/SYNTH-PARTIAL-SUPERSESSION-001@r1`. Their content
identifiers are respectively
`synthetic-content:plan-partial-supersession-001-r1`,
`synthetic-content:request-partial-supersession-001-r1`,
`synthetic-content:fixture-partial-supersession-001-r1`,
`synthetic-content:trace-partial-supersession-001-r1`,
`synthetic-content:validation-partial-supersession-001-r1`, and
`synthetic-content:supersession-partial-supersession-001-r1`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-PARTIAL-SUPERSESSION-001-PLAN">
Claim: one authorized synthetic normalization preserves both input pointers and
their equality relation. Falsifier: either pointer changes or one valid direct
comparison observation records `unequal`. Bounded pass: both pointers remain
unchanged and all valid unsuperseded direct comparison observations agree on
`equal`. Unresolved: valid unsuperseded direct comparison evidence conflicts.
Stop on unauthorized operation or source, fixture, data, standing, authority,
or risk revision. Prohibited conclusions are effectiveness, destination fit,
owner acceptance, deployment readiness, and external outcome.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-PARTIAL-SUPERSESSION-001-TRACE">
The authorized normalization ran with no deviation. Both pointers remained
unchanged; stops did not trigger; final state equals initial state. The trace
contains valid direct observation `synthetic-observation:comparison-equal-004-r1`
recording `equal`, valid direct observation
`synthetic-observation:comparison-unequal-004a-r1` recording `unequal`, and
valid direct observation `synthetic-observation:comparison-unequal-004b-r1`
recording `unequal`. All three are readable, in scope, and provenance-valid.
No real people, data, systems, or external actions were involved.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-PARTIAL-SUPERSESSION-001-VALIDATION">
The validator passed structure, identifiers, execution authority, chronology,
stops, and final state. It lists all three direct observations and marks
`comparison_conflict: true`. It does not reconcile or supersede them.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-PARTIAL-SUPERSESSION-001-SUPERSESSION">
The later immutable record is signed by `synthetic-result-owner` under
`synthetic-result-owner-supersession@r1`. Its exact coverage names only
`synthetic-observation:comparison-unequal-004a-r1` and replaces that record
with `synthetic-observation:comparison-equal-004a-corrected-r1`. It explicitly
does not cover, invalidate, or supersede
`synthetic-observation:comparison-equal-004-r1` or
`synthetic-observation:comparison-unequal-004b-r1`. The authority is valid for
its named record and has no blanket reconciliation scope.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-PARTIAL-SUPERSESSION-001-RESULT">
After exact supersession, the valid unsuperseded evidence still includes
`equal` and `unequal`. Neither bounded pass nor bounded failure is supported.
Result is `unresolved`; evidence type is validated synthetic trace with partial
authorized supersession and residual conflicting direct observations;
permitted disposition support is `defer` only. Preserve incomplete coverage as
negative evidence.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-PARTIAL-SUPERSESSION-001-CONTROLS">
One synthetic reviewer role represents standing; no real party or owner is
represented. Data is synthetic input only; risk and external action are
`none`. Preserve negative evidence at
`synthetic://negative-evidence/SYNTH-SCORE-PARTIAL-SUPERSESSION-001@r1`.
Correction owner is `synthetic-proving-plan-owner`. Recovery preserves the
unchanged frozen state and the exact supersession relation. Exact next wake is
one immutable result-owner record covering every remaining conflicting direct
observation, or an owner decision on returned `defer` support.
</evidence>

## Work now

Draft
`proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-PARTIAL-SUPERSESSION-BOUNDARY-FIXTURE.md`
with YAML frontmatter (`artifact_type:
synthetic_proving_score_partial_supersession_boundary_fixture`, `status:
candidate_process_fixture`, `external_action: none`) and exactly these body
sections: `Use Boundary`, `Score Header`, `Frozen Plan And Evidence`, `Claim
And Decision Conditions`, `Observed Trace`, `Evidence Grade And
Counterevidence`, `Affected-Party, Data, And Legitimacy Check`, `Result`,
`Residual Uncertainty, Correction, And Recovery`, `Permitted Disposition
Return`, and `Frontier Verification`.

Keep all three direct observations, the replacement observation, and the exact
supersession coverage visible. Preserve every identifier, content identifier,
stop, correction, recovery, prohibited conclusion, non-effect, and wake. First
line must be `---`; close the YAML frontmatter with a later line containing
only `---`; immediately after frontmatter use the title
`# Synthetic Proving-Score Partial-Supersession Boundary Fixture`; use `##` for
every named body section and deeper headings only within a named section; do
not use a code fence. Return only the finished artifact.
