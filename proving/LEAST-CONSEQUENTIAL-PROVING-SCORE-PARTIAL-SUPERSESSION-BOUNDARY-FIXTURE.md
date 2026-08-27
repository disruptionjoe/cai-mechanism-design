---
artifact_type: synthetic_proving_score_partial_supersession_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Proving-Score Partial-Supersession Boundary Fixture

## Use Boundary

This fixture scores one authorized synthetic trace with one direct `equal`
observation, two direct `unequal` observations, and a later immutable
result-owner supersession record that covers only one `unequal` observation.
The uncovered `equal` and `unequal` observations remain conflicting, so the
result remains `unresolved` with `defer` support. It does not treat otherwise-
valid authority as broader than its explicit coverage, create `CMD-0001-P8`,
modify `CMD-0001`, choose a candidate disposition, or authorize contact,
transfer, graduation, deployment, publication, or external action.

## Score Header

- Score: `SYNTH-SCORE-PARTIAL-SUPERSESSION-001@r1`.
- Plan: `SYNTH-PROVE-PARTIAL-SUPERSESSION-001@r1`.
- Candidate: `SYNTH-CANDIDATE-PARTIAL-SUPERSESSION-001@r1`.
- Source: `SYNTH-SOURCE-PARTIAL-SUPERSESSION-001@r1`.
- Treatment: `synthetic`.
- Result owner: `synthetic-result-owner`.
- Execution authority:
  `synthetic://authorization/SYNTH-PARTIAL-SUPERSESSION-001@grant-r1`.
- Scorer and time: `synthetic-proving-scorer` at
  `2026-08-27T09:13:57Z`.
- External action: `none`.

## Frozen Plan And Evidence

- Plan: `synthetic://plan/SYNTH-PROVE-PARTIAL-SUPERSESSION-001@r1`,
  content identifier `synthetic-content:plan-partial-supersession-001-r1`.
- Request: `synthetic://request/SYNTH-REQUEST-PARTIAL-SUPERSESSION-001@r1`,
  content identifier `synthetic-content:request-partial-supersession-001-r1`.
- Fixture: `synthetic://fixture/SYNTH-PARTIAL-SUPERSESSION-001@r1`,
  content identifier `synthetic-content:fixture-partial-supersession-001-r1`.
- Trace: `synthetic://trace/SYNTH-TRACE-PARTIAL-SUPERSESSION-001@r1`,
  content identifier `synthetic-content:trace-partial-supersession-001-r1`.
- Validation: `synthetic://validation/SYNTH-PARTIAL-SUPERSESSION-001@r1`,
  content identifier `synthetic-content:validation-partial-supersession-001-r1`.
- Supersession:
  `synthetic://supersession/SYNTH-PARTIAL-SUPERSESSION-001@r1`, content
  identifier `synthetic-content:supersession-partial-supersession-001-r1`.

## Claim And Decision Conditions

The claim is that one authorized synthetic normalization preserves both input
pointers and their equality relation. The falsifier is either pointer changing
or one valid direct comparison observation recording `unequal`. A bounded pass
requires both pointers to remain unchanged and all valid unsuperseded direct
comparison observations to agree on `equal`. The unresolved route applies when
valid unsuperseded direct comparison evidence conflicts. Stop on unauthorized
operation or source, fixture, data, standing, authority, or risk revision.
Prohibited conclusions are effectiveness, destination fit, owner acceptance,
deployment readiness, and external outcome.

## Observed Trace

The authorized normalization ran with no deviation. Both pointers remained
unchanged; stops did not trigger; final state equals initial state. The trace
contains valid direct observation
`synthetic-observation:comparison-equal-004-r1` recording `equal`, valid direct
observation `synthetic-observation:comparison-unequal-004a-r1` recording
`unequal`, and valid direct observation
`synthetic-observation:comparison-unequal-004b-r1` recording `unequal`. All
three are readable, in scope, and provenance-valid. No real people, data,
systems, or external actions were involved.

## Evidence Grade And Counterevidence

The validator passed structure, identifiers, execution authority, chronology,
stops, and final state. It lists all three direct observations and marks
`comparison_conflict: true`. It does not reconcile or supersede them. The
otherwise-valid supersession record is counterevidence only within its exact
coverage.

## Affected-Party, Data, And Legitimacy Check

One synthetic reviewer role represents standing; no real party or owner is
represented. Data is synthetic input only; risk and external action are
`none`. No effectiveness, destination-fit, acceptance, deployment-readiness,
or external-outcome conclusion is available.

## Result

After exact supersession, the valid unsuperseded evidence still includes
`equal` and `unequal`. Neither bounded pass nor bounded failure is supported.
Result is `unresolved`; evidence type is validated synthetic trace with partial
authorized supersession and residual conflicting direct observations.
Preserve incomplete coverage as negative evidence.

## Residual Uncertainty, Correction, And Recovery

The later immutable record is signed by `synthetic-result-owner` under
`synthetic-result-owner-supersession@r1`. Its exact coverage names only
`synthetic-observation:comparison-unequal-004a-r1` and replaces that record
with `synthetic-observation:comparison-equal-004a-corrected-r1`. It explicitly
does not cover, invalidate, or supersede
`synthetic-observation:comparison-equal-004-r1` or
`synthetic-observation:comparison-unequal-004b-r1`. The authority is valid for
its named record and has no blanket reconciliation scope.

Preserve negative evidence at
`synthetic://negative-evidence/SYNTH-SCORE-PARTIAL-SUPERSESSION-001@r1`.
Correction owner is `synthetic-proving-plan-owner`. Recovery preserves the
unchanged frozen state and the exact supersession relation. The exact next wake
is one immutable result-owner record covering every remaining conflicting
direct observation, or an owner decision on returned `defer` support.

## Permitted Disposition Return

Permitted support is `defer` only, returned to `synthetic-result-owner`. The
score creates no candidate disposition, P8, contact, transfer, graduation,
deployment, publication, or external action. `CMD-0001` remains deferred.

## Frontier Verification

- Verify every frozen pointer, content identifier, authority, and timestamp.
- Confirm all three direct observations and the corrected replacement
  observation remain visible and provenance-bound.
- Confirm the result-owner supersession record covers only
  `synthetic-observation:comparison-unequal-004a-r1` and cannot erase either
  uncovered direct observation.
- Confirm the residual valid `equal` and `unequal` observations keep the result
  `unresolved` with `defer` support only.
- Confirm every stop, prohibited conclusion, negative-evidence pointer,
  correction owner, recovery route, non-effect, and exact wake remains intact.
- Confirm `CMD-0001`, P7, owner truth, and external-action state are unchanged.
