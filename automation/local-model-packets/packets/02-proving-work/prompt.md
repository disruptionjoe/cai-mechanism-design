# Score a validated synthetic trace with conflicting direct observations

## Boundary

Write one complete synthetic Mechanism Design score fixture from only the
embedded evidence. Preserve the authorized trace, clean stop state, one direct
`equal` comparison observation, one direct `unequal` comparison observation,
the validator's one-sided summary, an `unresolved` result, and `defer` support.
Neither direct observation may be silently discarded, averaged, or selected by
the validator summary. Do not infer a pass or failure, create `CMD-0001-P8`,
modify `CMD-0001`, choose a disposition, or authorize contact, transfer,
graduation, deployment, publication, or external action. External action is
`none`.

## Evidence

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-TEMPLATE.md">
A score compares direct observations with the frozen claim, falsifier, pass,
unresolved, stop, and prohibited-conclusion conditions. Validation and artifact
cleanliness do not replace, reconcile, or choose between direct observations.
</evidence>

<evidence path="ROADMAP.md">
`CMD-0001` remains deferred. This fixture creates no P8, proving result for
`CMD-0001`, or candidate disposition.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-CONFLICTING-OBSERVATIONS-001-HEADER">
Score `SYNTH-SCORE-CONFLICTING-OBSERVATIONS-001@r1` concerns plan
`SYNTH-PROVE-CONFLICTING-OBSERVATIONS-001@r1`, candidate
`SYNTH-CANDIDATE-CONFLICTING-OBSERVATIONS-001@r1`, and source
`SYNTH-SOURCE-CONFLICTING-OBSERVATIONS-001@r1`. Treatment is `synthetic`;
result owner is `synthetic-result-owner`; authority is
`synthetic://authorization/SYNTH-CONFLICTING-OBSERVATIONS-001@grant-r1`;
scorer is `synthetic-proving-scorer`; scored at `2026-08-27T07:16:57Z`;
external action is `none`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-CONFLICTING-OBSERVATIONS-001-PACKAGE">
Plan, request, fixture, trace, and validation pointers are respectively
`synthetic://plan/SYNTH-PROVE-CONFLICTING-OBSERVATIONS-001@r1`,
`synthetic://request/SYNTH-REQUEST-CONFLICTING-OBSERVATIONS-001@r1`,
`synthetic://fixture/SYNTH-CONFLICTING-OBSERVATIONS-001@r1`,
`synthetic://trace/SYNTH-TRACE-CONFLICTING-OBSERVATIONS-001@r1`, and
`synthetic://validation/SYNTH-CONFLICTING-OBSERVATIONS-001@r1`. Their content
identifiers are respectively
`synthetic-content:plan-conflicting-observations-001-r1`,
`synthetic-content:request-conflicting-observations-001-r1`,
`synthetic-content:fixture-conflicting-observations-001-r1`,
`synthetic-content:trace-conflicting-observations-001-r1`, and
`synthetic-content:validation-conflicting-observations-001-r1`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-CONFLICTING-OBSERVATIONS-001-PLAN">
Claim: one authorized synthetic normalization preserves both input pointers and
their equality relation. Falsifier and observable failure: either pointer
changes or a valid separate comparison observation records `unequal`. Bounded
pass: both pointers are observed unchanged and all valid separate comparison
observations agree on `equal`. Unresolved route: comparison evidence is absent,
unreadable, or internally conflicting. Stop on any unauthorized operation or
source, fixture, data, standing, or risk revision. Prohibited conclusions are
effectiveness, destination fit, owner acceptance, deployment readiness, and
external outcome.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-CONFLICTING-OBSERVATIONS-001-TRACE">
The authorized normalization ran with no deviation. Both pointer values were
recorded unchanged. Stops did not trigger and final state equals the frozen
initial state. The same immutable trace contains direct observation
`synthetic-observation:comparison-equal-002-r1`, which records `equal`, and
direct observation `synthetic-observation:comparison-unequal-002-r1`, which
records `unequal`. Both are readable, in scope, and provenance-valid; the
frozen evidence supplies no authorized reconciliation or supersession relation.
No real people, data, systems, or external actions were involved.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-CONFLICTING-OBSERVATIONS-001-VALIDATION">
The validator passed structure, identifiers, authorization, chronology, stops,
and final state. Its summary field says `comparison_preserved: true` and cites
only `synthetic-observation:comparison-equal-002-r1`. It does not invalidate,
supersede, or cite `synthetic-observation:comparison-unequal-002-r1`. The
summary is derived and has no authority to select between the direct
observations.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-CONFLICTING-OBSERVATIONS-001-RESULT">
Direct observations are authorized execution, unchanged pointer values, no
stop, no deviation, restored-equivalent final state, comparison `equal`, and
comparison `unequal`. Because both comparison observations remain valid and
unreconciled, neither bounded pass nor bounded failure is supported. Result is
`unresolved`; evidence type is validated synthetic trace with conflicting
direct observations; permitted disposition support is `defer` only. Preserve
the conflict as negative evidence rather than silently choosing one record.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-CONFLICTING-OBSERVATIONS-001-CONTROLS">
One synthetic reviewer role represents standing; no real party or owner is
represented. Data is synthetic input only; risk and external action are
`none`. Preserve negative evidence at
`synthetic://negative-evidence/SYNTH-SCORE-CONFLICTING-OBSERVATIONS-001@r1`.
Correction owner is `synthetic-proving-plan-owner`. Recovery preserves the
unchanged frozen state. Exact next wake is an immutable authorized
reconciliation or supersession record covering both direct comparison
observations, or an owner decision on returned `defer` support.
</evidence>

## Work now

Draft
`proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-CONFLICTING-OBSERVATIONS-BOUNDARY-FIXTURE.md`
with YAML frontmatter (`artifact_type:
synthetic_proving_score_conflicting_observations_boundary_fixture`, `status:
candidate_process_fixture`, `external_action: none`) and exactly these body
sections: `Use Boundary`, `Score Header`, `Frozen Plan And Evidence`, `Claim And
Decision Conditions`, `Observed Trace`, `Evidence Grade And Counterevidence`,
`Affected-Party, Data, And Legitimacy Check`, `Result`, `Residual Uncertainty,
Correction, And Recovery`, `Permitted Disposition Return`, and `Frontier
Verification`.

Preserve both direct observations separately from validator inference and keep
their unreconciled conflict visible as negative evidence. First line must be
`---`; close the YAML frontmatter with a second `---`; use Markdown headings;
do not use a code fence. Return only the finished artifact.
