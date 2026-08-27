---
artifact_type: synthetic_proving_score_validation_conflict_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Proving-Score Validation-Conflict Boundary Fixture

## Use Boundary

This fixture scores one authorized synthetic trace against its frozen plan.
The direct `unequal` comparison observation controls the bounded result;
validator success and a clean final state cannot overwrite it. The fixture
creates no `CMD-0001-P8`, candidate disposition, contact, transfer, graduation,
deployment, publication, or external action.

## Score Header

- Score: `SYNTH-SCORE-VALIDATION-CONFLICT-001@r1`.
- Plan: `SYNTH-PROVE-VALIDATION-CONFLICT-001@r1`.
- Candidate: `SYNTH-CANDIDATE-VALIDATION-CONFLICT-001@r1`.
- Source: `SYNTH-SOURCE-VALIDATION-CONFLICT-001@r1`.
- Treatment: `synthetic`.
- Result owner: `synthetic-result-owner`.
- Execution authority:
  `synthetic://authorization/SYNTH-VALIDATION-CONFLICT-001@grant-r1`.
- Scorer and time: `synthetic-proving-scorer` at
  `2026-08-27T06:15:38Z`.
- External action: `none`.

## Frozen Plan And Evidence

- Plan: `synthetic://plan/SYNTH-PROVE-VALIDATION-CONFLICT-001@r1`, content
  identifier `synthetic-content:plan-validation-conflict-001-r1`.
- Request: `synthetic://request/SYNTH-REQUEST-VALIDATION-CONFLICT-001@r1`,
  content identifier `synthetic-content:request-validation-conflict-001-r1`.
- Fixture: `synthetic://fixture/SYNTH-VALIDATION-CONFLICT-001@r1`, content
  identifier `synthetic-content:fixture-validation-conflict-001-r1`.
- Trace: `synthetic://trace/SYNTH-TRACE-VALIDATION-CONFLICT-001@r1`, content
  identifier `synthetic-content:trace-validation-conflict-001-r1`.
- Validation:
  `synthetic://validation/SYNTH-VALIDATION-CONFLICT-001@r1`, content identifier
  `synthetic-content:validation-validation-conflict-001-r1`.

## Claim And Decision Conditions

The exact claim is that one authorized synthetic normalization preserves both
input pointers and their equality relation. A changed pointer or a separate
comparison observation of `unequal` is a falsifier and observable failure. A
bounded pass requires both pointers observed unchanged and a separate
comparison observation of `equal`. Unreadable or absent comparison evidence
returns unresolved. Any unauthorized operation or source, fixture, data,
standing, or risk revision stops the treatment. Prohibited conclusions are
effectiveness, destination fit, owner acceptance, deployment readiness, and
external outcome.

## Observed Trace

The authorized normalization ran with no deviation. Both pointer values were
recorded unchanged. Stops did not trigger, and final state equals the frozen
initial state. A separate direct comparison observation recorded `unequal`
with content identifier
`synthetic-observation:comparison-unequal-001-r1`. No real people, data,
systems, or external actions were involved.

## Evidence Grade And Counterevidence

Evidence type is a validated synthetic trace with a conflicting validator
summary. The validator passed structure, identifiers, authorization,
chronology, stops, and final state. Its summary says
`comparison_preserved: true`, but its evidence list contains no comparison-
observation pointer and does not cite
`synthetic-observation:comparison-unequal-001-r1`. The summary is a derived
assertion, not a direct observation. The direct `unequal` observation is
counterevidence that satisfies the frozen falsifier and defeats bounded pass.

## Affected-Party, Data, And Legitimacy Check

One synthetic reviewer role represents standing; no real party, source owner,
candidate owner, result owner, authority owner, scorer, or validator is
represented. Data is synthetic input only; risk and external action are
`none`. The evidence conflict limits the bounded score and creates no owner or
real-world conclusion.

## Result

Result: `revise`. Authorized execution, unchanged pointers, no stop, no
deviation, restored-equivalent final state, and validator success do not
override the direct `unequal` observation. The unequal observation satisfies
the falsifier and defeats bounded pass. Preserve the validator conflict as
negative evidence rather than silently reconciling it.

## Residual Uncertainty, Correction, And Recovery

Preserve the conflict at
`synthetic://negative-evidence/SYNTH-SCORE-VALIDATION-CONFLICT-001@r1`.
Correction owner is `synthetic-proving-plan-owner`; recovery preserves the
unchanged frozen state. The exact next wake is a corrected immutable validator
result that cites the comparison observation, or an owner decision on the
returned `revise` support.

## Permitted Disposition Return

Permitted support is `revise` only, returned to `synthetic-result-owner`. The
score creates no owner disposition and does not create P8, contact, transfer,
graduation, deployment, publication, or external action. `CMD-0001` remains
deferred.

## Frontier Verification

- Verify every frozen pointer, content identifier, authority, and timestamp.
- Confirm the direct trace records unchanged pointers and comparison
  `unequal`.
- Confirm the validator summary lacks the cited comparison observation and is
  not treated as direct evidence.
- Confirm the result remains `revise` and supports only `revise`.
- Confirm `CMD-0001`, P7, owner truth, and external-action state are unchanged.
