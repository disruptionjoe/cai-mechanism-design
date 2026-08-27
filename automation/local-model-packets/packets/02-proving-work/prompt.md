# Score complete supersession coverage without disposition authority

## Boundary

Write one complete synthetic Mechanism Design score fixture from only the
embedded evidence. Preserve the authorized trace, clean stop state, one direct
`equal` observation, two direct `unequal` observations, and a later immutable
result-owner supersession record that exactly covers both `unequal`
observations and replaces each with `equal`. After exact supersession, every
valid unsuperseded direct observation agrees on `equal`, so the frozen plan
supports `bounded_pass`; the supersession record does not authorize a
candidate disposition, transfer, graduation, deployment, or external action.
Do not create `CMD-0001-P8`, modify `CMD-0001`, choose a disposition, or
authorize contact, transfer, graduation, deployment, publication, or external
action. External action is `none`.

## Evidence

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-TEMPLATE.md">
A score keeps direct evidence visible until an applicable immutable record
explicitly supersedes it. Valid authority operates only over the observations
and relation named in its exact scope. A bounded result and a later owner
disposition remain separate decisions.
</evidence>

<evidence path="ROADMAP.md">
`CMD-0001` remains deferred. This fixture creates no P8, proving result for
`CMD-0001`, or candidate disposition.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-COMPLETE-SUPERSESSION-001-HEADER">
Score `SYNTH-SCORE-COMPLETE-SUPERSESSION-001@r1` concerns plan
`SYNTH-PROVE-COMPLETE-SUPERSESSION-001@r1`, candidate
`SYNTH-CANDIDATE-COMPLETE-SUPERSESSION-001@r1`, and source
`SYNTH-SOURCE-COMPLETE-SUPERSESSION-001@r1`. Treatment is `synthetic`; result
owner is `synthetic-result-owner`; execution authority is
`synthetic://authorization/SYNTH-COMPLETE-SUPERSESSION-001@grant-r1`; scorer
is `synthetic-proving-scorer`; scored at `2026-08-27T10:12:50Z`; external
action is `none`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-COMPLETE-SUPERSESSION-001-PACKAGE">
Plan, request, fixture, trace, validation, and supersession pointers are
respectively `synthetic://plan/SYNTH-PROVE-COMPLETE-SUPERSESSION-001@r1`,
`synthetic://request/SYNTH-REQUEST-COMPLETE-SUPERSESSION-001@r1`,
`synthetic://fixture/SYNTH-COMPLETE-SUPERSESSION-001@r1`,
`synthetic://trace/SYNTH-TRACE-COMPLETE-SUPERSESSION-001@r1`,
`synthetic://validation/SYNTH-COMPLETE-SUPERSESSION-001@r1`, and
`synthetic://supersession/SYNTH-COMPLETE-SUPERSESSION-001@r1`. Their content
identifiers are respectively
`synthetic-content:plan-complete-supersession-001-r1`,
`synthetic-content:request-complete-supersession-001-r1`,
`synthetic-content:fixture-complete-supersession-001-r1`,
`synthetic-content:trace-complete-supersession-001-r1`,
`synthetic-content:validation-complete-supersession-001-r1`, and
`synthetic-content:supersession-complete-supersession-001-r1`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-COMPLETE-SUPERSESSION-001-PLAN">
Claim: one authorized synthetic normalization preserves both input pointers and
their equality relation. Falsifier: either pointer changes or one valid
unsuperseded direct comparison observation records `unequal`. Bounded pass:
both pointers remain unchanged and all valid unsuperseded direct comparison
observations agree on `equal`. Unresolved: valid unsuperseded direct comparison
evidence conflicts. Stop on unauthorized operation or source, fixture, data,
standing, authority, or risk revision. Prohibited conclusions are
effectiveness, destination fit, owner acceptance, deployment readiness, and
external outcome.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-COMPLETE-SUPERSESSION-001-TRACE">
The authorized normalization ran with no deviation. Both pointers remained
unchanged; stops did not trigger; final state equals initial state. The trace
contains valid direct observation
`synthetic-observation:comparison-equal-005-r1` recording `equal`, valid direct
observation `synthetic-observation:comparison-unequal-005a-r1` recording
`unequal`, and valid direct observation
`synthetic-observation:comparison-unequal-005b-r1` recording `unequal`. All
three are readable, in scope, and provenance-valid. No real people, data,
systems, or external actions were involved.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-COMPLETE-SUPERSESSION-001-VALIDATION">
The validator passed structure, identifiers, execution authority, chronology,
stops, and final state. It lists all three original direct observations and
marks `comparison_conflict: true`. It does not reconcile or supersede them.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-COMPLETE-SUPERSESSION-001-SUPERSESSION">
The later immutable record is signed by `synthetic-result-owner` under
`synthetic-result-owner-supersession@r1`. Its exact coverage names
`synthetic-observation:comparison-unequal-005a-r1` and
`synthetic-observation:comparison-unequal-005b-r1`, replacing them respectively
with `synthetic-observation:comparison-equal-005a-corrected-r1` and
`synthetic-observation:comparison-equal-005b-corrected-r1`. It explicitly does
not cover, invalidate, or supersede
`synthetic-observation:comparison-equal-005-r1`. Its authority is valid only
for the two named replacements and supplies no candidate-disposition,
acceptance, transfer, graduation, deployment, or external-action authority.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-COMPLETE-SUPERSESSION-001-RESULT">
After exact supersession, the valid unsuperseded evidence consists of
`synthetic-observation:comparison-equal-005-r1`,
`synthetic-observation:comparison-equal-005a-corrected-r1`, and
`synthetic-observation:comparison-equal-005b-corrected-r1`. All agree on
`equal`, both pointers remain unchanged, and the frozen plan supports
`bounded_pass`. Evidence type is validated synthetic trace with complete
authorized supersession. Permitted disposition support remains `defer` only;
the bounded pass does not itself choose a disposition.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-COMPLETE-SUPERSESSION-001-CONTROLS">
One synthetic reviewer role represents standing; no real party or owner is
represented. Data is synthetic input only; risk and external action are
`none`. Preserve the original conflict and its complete supersession relation
at
`synthetic://negative-evidence/SYNTH-SCORE-COMPLETE-SUPERSESSION-001@r1`.
Correction owner is `synthetic-proving-plan-owner`. Recovery preserves the
unchanged frozen state, all original observations, both replacement
observations, and the exact supersession coverage. Exact next wake is an owner
decision on returned `defer` support, or a revision to source, trace,
supersession, standing, authority, or risk.
</evidence>

## Work now

Draft
`proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-COMPLETE-SUPERSESSION-BOUNDARY-FIXTURE.md`
with YAML frontmatter (`artifact_type:
synthetic_proving_score_complete_supersession_boundary_fixture`, `status:
candidate_process_fixture`, `external_action: none`) and exactly these body
sections: `Use Boundary`, `Score Header`, `Frozen Plan And Evidence`, `Claim
And Decision Conditions`, `Observed Trace`, `Evidence Grade And
Counterevidence`, `Affected-Party, Data, And Legitimacy Check`, `Result`,
`Residual Uncertainty, Correction, And Recovery`, `Permitted Disposition
Return`, and `Frontier Verification`.

Keep all three original direct observations, both replacement observations,
and the exact supersession coverage visible. Put the supersession scope,
negative-evidence pointer, correction owner, recovery, and exact next wake in
`Residual Uncertainty, Correction, And Recovery`, not in the affected-party
section. Preserve every identifier, content identifier, stop, prohibited
conclusion, non-effect, and wake. In `Frontier Verification`, use bullets that
explicitly check complete exact coverage, all three surviving `equal`
observations, `bounded_pass`, disposition separation, and unchanged `CMD-0001`
and external-action state. First line must be `---`; close the YAML frontmatter
with a later line containing only `---`; immediately after frontmatter use the
title `# Synthetic Proving-Score Complete-Supersession Boundary Fixture`; use
`##` for every named body section and deeper headings only within a named
section; do not use a code fence. Return only the finished artifact.
