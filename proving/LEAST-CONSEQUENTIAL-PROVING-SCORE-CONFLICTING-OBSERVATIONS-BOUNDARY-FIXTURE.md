---
artifact_type: synthetic_proving_score_conflicting_observations_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Proving-Score Conflicting-Observations Boundary Fixture

## Use Boundary

This fixture scores one authorized synthetic trace that contains two valid,
conflicting direct comparison observations. It keeps both observations
separate from the validator's one-sided summary and returns `unresolved` with
`defer` support. It creates no pass, failure, `CMD-0001-P8`, candidate
disposition, contact, transfer, graduation, deployment, publication, or
external action.

## Score Header

- Score: `SYNTH-SCORE-CONFLICTING-OBSERVATIONS-001@r1`.
- Plan: `SYNTH-PROVE-CONFLICTING-OBSERVATIONS-001@r1`.
- Candidate: `SYNTH-CANDIDATE-CONFLICTING-OBSERVATIONS-001@r1`.
- Source: `SYNTH-SOURCE-CONFLICTING-OBSERVATIONS-001@r1`.
- Treatment: `synthetic`.
- Result owner: `synthetic-result-owner`.
- Execution authority:
  `synthetic://authorization/SYNTH-CONFLICTING-OBSERVATIONS-001@grant-r1`.
- Scorer and time: `synthetic-proving-scorer` at
  `2026-08-27T07:16:57Z`.
- External action: `none`.

## Frozen Plan And Evidence

- Plan: `synthetic://plan/SYNTH-PROVE-CONFLICTING-OBSERVATIONS-001@r1`,
  content identifier
  `synthetic-content:plan-conflicting-observations-001-r1`.
- Request:
  `synthetic://request/SYNTH-REQUEST-CONFLICTING-OBSERVATIONS-001@r1`,
  content identifier
  `synthetic-content:request-conflicting-observations-001-r1`.
- Fixture: `synthetic://fixture/SYNTH-CONFLICTING-OBSERVATIONS-001@r1`,
  content identifier
  `synthetic-content:fixture-conflicting-observations-001-r1`.
- Trace: `synthetic://trace/SYNTH-TRACE-CONFLICTING-OBSERVATIONS-001@r1`,
  content identifier
  `synthetic-content:trace-conflicting-observations-001-r1`.
- Validation:
  `synthetic://validation/SYNTH-CONFLICTING-OBSERVATIONS-001@r1`, content
  identifier `synthetic-content:validation-conflicting-observations-001-r1`.

## Claim And Decision Conditions

The claim is that one authorized synthetic normalization preserves both input
pointers and their equality relation. Either pointer changing or a valid
separate comparison observation recording `unequal` is a falsifier and
observable failure. A bounded pass requires both pointers observed unchanged
and every valid separate comparison observation agreeing on `equal`.
Comparison evidence that is absent, unreadable, or internally conflicting
returns unresolved. Any unauthorized operation or source, fixture, data,
standing, or risk revision stops the treatment. Prohibited conclusions are
effectiveness, destination fit, owner acceptance, deployment readiness, and
external outcome.

## Observed Trace

The authorized normalization ran with no deviation. Both pointer values were
recorded unchanged. Stops did not trigger, and final state equals the frozen
initial state. The same immutable trace contains direct observation
`synthetic-observation:comparison-equal-002-r1`, which records `equal`, and
direct observation `synthetic-observation:comparison-unequal-002-r1`, which
records `unequal`. Both are readable, in scope, and provenance-valid. The
frozen evidence supplies no authorized reconciliation or supersession
relation. No real people, data, systems, or external actions were involved.

## Evidence Grade And Counterevidence

Evidence type is a validated synthetic trace with conflicting direct
observations. The validator passed structure, identifiers, authorization,
chronology, stops, and final state. Its summary says
`comparison_preserved: true` and cites only
`synthetic-observation:comparison-equal-002-r1`. It does not invalidate,
supersede, or cite `synthetic-observation:comparison-unequal-002-r1`. The
summary is derived and has no authority to select between the direct
observations. Preserve the conflict as negative evidence.

## Affected-Party, Data, And Legitimacy Check

One synthetic reviewer role represents standing; no real party, source owner,
candidate owner, result owner, authority owner, scorer, or validator is
represented. Data is synthetic input only; risk and external action are
`none`. The evidence conflict limits the bounded score and creates no owner or
real-world conclusion.

## Result

Result: `unresolved`. Direct observations are authorized execution, unchanged
pointer values, no stop, no deviation, restored-equivalent final state,
comparison `equal`, and comparison `unequal`. Because both comparison
observations remain valid and unreconciled, neither bounded pass nor bounded
failure is supported.

## Residual Uncertainty, Correction, And Recovery

Preserve the conflict at
`synthetic://negative-evidence/SYNTH-SCORE-CONFLICTING-OBSERVATIONS-001@r1`.
Correction owner is `synthetic-proving-plan-owner`; recovery preserves the
unchanged frozen state. The exact next wake is an immutable authorized
reconciliation or supersession record covering both direct comparison
observations, or an owner decision on returned `defer` support.

## Permitted Disposition Return

Permitted support is `defer` only, returned to `synthetic-result-owner`. The
score creates no owner disposition and does not create P8, contact, transfer,
graduation, deployment, publication, or external action. `CMD-0001` remains
deferred.

## Frontier Verification

- Verify every frozen pointer, content identifier, authority, and timestamp.
- Confirm both direct comparison observations are readable, in scope, and
  provenance-valid.
- Confirm the validator cites only the `equal` observation and is not allowed
  to invalidate, reconcile, or supersede the `unequal` observation.
- Confirm the result remains `unresolved` and supports only `defer`.
- Confirm `CMD-0001`, P7, owner truth, and external-action state are unchanged.
