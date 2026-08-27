# Score a validated synthetic trace whose observation contradicts the summary

## Boundary

Write one complete synthetic Mechanism Design score fixture from only the
embedded evidence. Preserve the authorized trace, clean stop state, direct
`unequal` comparison observation, validator summary conflict, `revise` result,
and `revise` support. Direct observation controls the bounded result; validator
success cannot overwrite it. Do not invent equality, infer a pass, create
`CMD-0001-P8`, modify `CMD-0001`, choose a disposition, or authorize any
contact, transfer, graduation, deployment, publication, or external action.
External action is `none`.

## Evidence

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-TEMPLATE.md">
A score compares the observed trace with the frozen claim, falsifier, failure,
pass, unresolved, stop, and prohibited-conclusion conditions. Validation and
artifact cleanliness do not replace direct observations or create a pass.
</evidence>

<evidence path="ROADMAP.md">
CMD-0001 remains deferred. This fixture creates no P8, proving result for
CMD-0001, or candidate disposition.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-VALIDATION-CONFLICT-001-HEADER">
Score `SYNTH-SCORE-VALIDATION-CONFLICT-001@r1` concerns plan
`SYNTH-PROVE-VALIDATION-CONFLICT-001@r1`, candidate
`SYNTH-CANDIDATE-VALIDATION-CONFLICT-001@r1`, and source
`SYNTH-SOURCE-VALIDATION-CONFLICT-001@r1`. Treatment is `synthetic`; result
owner is `synthetic-result-owner`; authority is
`synthetic://authorization/SYNTH-VALIDATION-CONFLICT-001@grant-r1`; scorer is
`synthetic-proving-scorer`; scored at `2026-08-27T06:15:38Z`; external action
is `none`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-VALIDATION-CONFLICT-001-PACKAGE">
Plan, request, fixture, trace, and validation pointers are respectively
`synthetic://plan/SYNTH-PROVE-VALIDATION-CONFLICT-001@r1`,
`synthetic://request/SYNTH-REQUEST-VALIDATION-CONFLICT-001@r1`,
`synthetic://fixture/SYNTH-VALIDATION-CONFLICT-001@r1`,
`synthetic://trace/SYNTH-TRACE-VALIDATION-CONFLICT-001@r1`, and
`synthetic://validation/SYNTH-VALIDATION-CONFLICT-001@r1`. Their content
identifiers are respectively
`synthetic-content:plan-validation-conflict-001-r1`,
`synthetic-content:request-validation-conflict-001-r1`,
`synthetic-content:fixture-validation-conflict-001-r1`,
`synthetic-content:trace-validation-conflict-001-r1`, and
`synthetic-content:validation-validation-conflict-001-r1`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-VALIDATION-CONFLICT-001-PLAN">
Claim: one authorized synthetic normalization preserves both input pointers and
their equality relation. Falsifier and observable failure: either pointer
changes or a separate comparison observation records `unequal`. Bounded pass:
both pointers are observed unchanged and the separate comparison observation
records `equal`. Unresolved route: return unreadable or absent comparison
evidence. Stop on any unauthorized operation or source, fixture, data,
standing, or risk revision. Prohibited conclusions are effectiveness,
destination fit, owner acceptance, deployment readiness, and external outcome.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-VALIDATION-CONFLICT-001-TRACE">
The authorized normalization ran with no deviation. Both pointer values were
recorded unchanged. Stops did not trigger and final state equals the frozen
initial state. A separate comparison observation recorded `unequal` with
content identifier `synthetic-observation:comparison-unequal-001-r1`. No real
people, data, systems, or external actions were involved.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-VALIDATION-CONFLICT-001-VALIDATION">
The validator passed structure, identifiers, authorization, chronology, stops,
and final state. Its summary field says `comparison_preserved: true`, but its
own evidence list contains no comparison-observation pointer and does not cite
`synthetic-observation:comparison-unequal-001-r1`. The validator summary is a
derived assertion, not a direct observation, and conflicts with the frozen
trace.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-VALIDATION-CONFLICT-001-RESULT">
Direct observations are authorized execution, unchanged pointer values, no
stop, no deviation, restored-equivalent final state, and comparison `unequal`.
The unequal observation satisfies the falsifier and defeats bounded pass.
Result is `revise`; evidence type is validated synthetic trace with a
conflicting validator summary; permitted disposition support is `revise` only.
The summary conflict must be preserved as negative evidence rather than
silently reconciled.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-VALIDATION-CONFLICT-001-CONTROLS">
One synthetic reviewer role represents standing; no real party or owner is
represented. Data is synthetic input only; risk and external action are
`none`. Preserve negative evidence at
`synthetic://negative-evidence/SYNTH-SCORE-VALIDATION-CONFLICT-001@r1`.
Correction owner is `synthetic-proving-plan-owner`. Recovery preserves the
unchanged frozen state. Exact next wake is a corrected immutable validator
result that cites the comparison observation, or an owner decision on the
returned `revise` support.
</evidence>

## Work now

Draft
`proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-VALIDATION-CONFLICT-BOUNDARY-FIXTURE.md`
with YAML frontmatter (`artifact_type:
synthetic_proving_score_validation_conflict_boundary_fixture`, `status:
candidate_process_fixture`, `external_action: none`) and exactly these body
sections: `Use Boundary`, `Score Header`, `Frozen Plan And Evidence`, `Claim And
Decision Conditions`, `Observed Trace`, `Evidence Grade And Counterevidence`,
`Affected-Party, Data, And Legitimacy Check`, `Result`, `Residual Uncertainty,
Correction, And Recovery`, `Permitted Disposition Return`, and `Frontier
Verification`.

Preserve direct observation separately from validator inference and keep the
conflict visible as negative evidence. First line must be `---`; do not use a code fence. Return only the finished artifact.
