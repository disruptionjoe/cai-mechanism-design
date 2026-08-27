# Score an unauthorized reconciliation of conflicting synthetic observations

## Boundary

Write one complete synthetic Mechanism Design score fixture from only the
embedded evidence. Preserve the authorized trace, clean stop state, direct
`equal` and `unequal` comparison observations, and a later reconciliation
record that lacks authority to supersede either observation. The result remains
`unresolved` with `defer` support. Do not treat chronology, signature shape, or
validator success as reconciliation authority. Do not create `CMD-0001-P8`,
modify `CMD-0001`, choose a disposition, or authorize contact, transfer,
graduation, deployment, publication, or external action. External action is
`none`.

## Evidence

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-TEMPLATE.md">
A score compares direct observations with the frozen claim, falsifier, pass,
unresolved, stop, and prohibited-conclusion conditions. Derived validation and
later records do not erase direct evidence without applicable authority and
an explicit supersession relation.
</evidence>

<evidence path="ROADMAP.md">
`CMD-0001` remains deferred. This fixture creates no P8, proving result for
`CMD-0001`, or candidate disposition.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-UNAUTHORIZED-RECONCILIATION-001-HEADER">
Score `SYNTH-SCORE-UNAUTHORIZED-RECONCILIATION-001@r1` concerns plan
`SYNTH-PROVE-UNAUTHORIZED-RECONCILIATION-001@r1`, candidate
`SYNTH-CANDIDATE-UNAUTHORIZED-RECONCILIATION-001@r1`, and source
`SYNTH-SOURCE-UNAUTHORIZED-RECONCILIATION-001@r1`. Treatment is `synthetic`;
result owner is `synthetic-result-owner`; execution authority is
`synthetic://authorization/SYNTH-UNAUTHORIZED-RECONCILIATION-001@grant-r1`;
scorer is `synthetic-proving-scorer`; scored at `2026-08-27T08:15:26Z`;
external action is `none`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-UNAUTHORIZED-RECONCILIATION-001-PACKAGE">
Plan, request, fixture, trace, validation, and reconciliation pointers are
respectively
`synthetic://plan/SYNTH-PROVE-UNAUTHORIZED-RECONCILIATION-001@r1`,
`synthetic://request/SYNTH-REQUEST-UNAUTHORIZED-RECONCILIATION-001@r1`,
`synthetic://fixture/SYNTH-UNAUTHORIZED-RECONCILIATION-001@r1`,
`synthetic://trace/SYNTH-TRACE-UNAUTHORIZED-RECONCILIATION-001@r1`,
`synthetic://validation/SYNTH-UNAUTHORIZED-RECONCILIATION-001@r1`, and
`synthetic://reconciliation/SYNTH-UNAUTHORIZED-RECONCILIATION-001@r1`.
Their content identifiers use the same lowercase stem and respective prefixes
and are respectively
`synthetic-content:plan-unauthorized-reconciliation-001-r1`,
`synthetic-content:request-unauthorized-reconciliation-001-r1`,
`synthetic-content:fixture-unauthorized-reconciliation-001-r1`,
`synthetic-content:trace-unauthorized-reconciliation-001-r1`,
`synthetic-content:validation-unauthorized-reconciliation-001-r1`, and
`synthetic-content:reconciliation-unauthorized-reconciliation-001-r1`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-UNAUTHORIZED-RECONCILIATION-001-PLAN">
Claim: one authorized synthetic normalization preserves both input pointers and
their equality relation. Falsifier: either pointer changes or one valid direct
comparison observation records `unequal`. Bounded pass: both pointers remain
unchanged and all valid direct comparison observations agree on `equal`.
Unresolved: direct comparison evidence conflicts unless one immutable record
with applicable result-owner authority explicitly supersedes every conflicting
observation. Stop on unauthorized operation or source, fixture, data,
standing, authority, or risk revision. Prohibited conclusions are
effectiveness, destination fit, owner acceptance, deployment readiness, and
external outcome.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-UNAUTHORIZED-RECONCILIATION-001-TRACE">
The authorized normalization ran with no deviation. Both pointers remained
unchanged; stops did not trigger; final state equals initial state. The trace
contains valid direct observation
`synthetic-observation:comparison-equal-003-r1` recording `equal` and valid
direct observation `synthetic-observation:comparison-unequal-003-r1` recording
`unequal`. Both are readable, in scope, and provenance-valid. No real people,
data, systems, or external actions were involved.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-UNAUTHORIZED-RECONCILIATION-001-VALIDATION">
The validator passed structure, identifiers, execution authority, chronology,
stops, and final state. It lists both direct observations and marks
`comparison_conflict: true`. It does not reconcile or supersede them.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-UNAUTHORIZED-RECONCILIATION-001-RECONCILIATION">
The later reconciliation record cites both direct observations and asserts
`equal controls`. Its signer is `synthetic-checksum-reviewer`; signer authority
is `checksum_review_only`; result-owner or supersession authority is `none`.
The record is chronologically later and structurally valid but has no authority
to reconcile, invalidate, or supersede either direct observation.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-UNAUTHORIZED-RECONCILIATION-001-RESULT">
Direct observations remain conflicting. Validator success and the later
unauthorized reconciliation do not satisfy the plan's supersession condition.
Neither bounded pass nor bounded failure is supported. Result is `unresolved`;
evidence type is validated synthetic trace with conflicting direct
observations and unauthorized reconciliation; permitted disposition support is
`defer` only. Preserve the reconciliation authority failure as negative
evidence.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-UNAUTHORIZED-RECONCILIATION-001-CONTROLS">
One synthetic reviewer role represents standing; no real party or owner is
represented. Data is synthetic input only; risk and external action are
`none`. Preserve negative evidence at
`synthetic://negative-evidence/SYNTH-SCORE-UNAUTHORIZED-RECONCILIATION-001@r1`.
Correction owner is `synthetic-proving-plan-owner`. Recovery preserves the
unchanged frozen state. Exact next wake is an immutable reconciliation or
supersession record with applicable result-owner authority covering both
direct observations, or an owner decision on returned `defer` support.
</evidence>

## Work now

Draft
`proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-UNAUTHORIZED-RECONCILIATION-BOUNDARY-FIXTURE.md`
with YAML frontmatter (`artifact_type:
synthetic_proving_score_unauthorized_reconciliation_boundary_fixture`,
`status: candidate_process_fixture`, `external_action: none`) and exactly these
body sections: `Use Boundary`, `Score Header`, `Frozen Plan And Evidence`,
`Claim And Decision Conditions`, `Observed Trace`, `Evidence Grade And
Counterevidence`, `Affected-Party, Data, And Legitimacy Check`, `Result`,
`Residual Uncertainty, Correction, And Recovery`, `Permitted Disposition
Return`, and `Frontier Verification`.

Keep both direct observations and the later record visible. Distinguish record
validity and chronology from applicable reconciliation authority. Preserve
every identifier, content identifier, stop, correction, recovery, prohibited
conclusion, non-effect, and wake. First line must be `---`; close the YAML
frontmatter with a later line containing only `---`; use Markdown headings; do
not use a code fence. Return only the finished artifact.
