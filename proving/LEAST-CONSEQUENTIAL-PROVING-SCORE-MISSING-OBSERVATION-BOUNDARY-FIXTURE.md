---
artifact_type: synthetic_proving_score_missing_observation_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Proving-Score Missing-Observation Boundary Fixture

## Use Boundary

This fixture scores one authorized synthetic trace against its frozen plan.
Clean execution, restored-equivalent final state, and validator success cannot
supply a separately required comparison observation. The fixture preserves an
`unresolved` result with `defer` support and creates no candidate disposition,
P8, contact, transfer, graduation, deployment, publication, or external action.

## Score Header

- Score: `SYNTH-SCORE-MISSING-OBSERVATION-001@r1`.
- Plan: `SYNTH-PROVE-MISSING-OBSERVATION-001@r1`.
- Candidate: `SYNTH-CANDIDATE-MISSING-OBSERVATION-001@r1`.
- Source: `SYNTH-SOURCE-MISSING-OBSERVATION-001@r1`.
- Treatment: `synthetic`.
- Result owner: `synthetic-result-owner`.
- Execution authority:
  `synthetic://authorization/SYNTH-MISSING-OBSERVATION-001@grant-r1`.
- Scorer and time: `synthetic-proving-scorer` at
  `2026-08-27T05:13:54Z`.
- External action: `none`.

## Frozen Plan And Evidence

- Plan: `synthetic://plan/SYNTH-PROVE-MISSING-OBSERVATION-001@r1`, content
  identifier `synthetic-content:plan-missing-observation-001-r1`.
- Request: `synthetic://request/SYNTH-REQUEST-MISSING-OBSERVATION-001@r1`,
  content identifier `synthetic-content:request-missing-observation-001-r1`.
- Fixture: `synthetic://fixture/SYNTH-MISSING-OBSERVATION-001@r1`, content
  identifier `synthetic-content:fixture-missing-observation-001-r1`.
- Trace: `synthetic://trace/SYNTH-TRACE-MISSING-OBSERVATION-001@r1`, content
  identifier `synthetic-content:trace-missing-observation-001-r1`.
- Validation:
  `synthetic://validation/SYNTH-VALIDATION-MISSING-OBSERVATION-001@r1`, content
  identifier `synthetic-content:validation-missing-observation-001-r1`;
  validation passed for structure, identifiers, authorization, chronology,
  stops, and final state but did not and could not supply the absent comparison
  observation.

## Claim And Decision Conditions

The exact claim is that one authorized synthetic normalization preserves both
input pointers and their equality relation. Falsifier and observable failure
are a changed pointer or an observed unequal relation. A bounded pass requires
both pointers observed unchanged and a separate comparison observation of
`equal`. The unresolved route returns incomplete evidence to the result owner.
Any unauthorized operation or source, fixture, data, standing, or risk revision
stops the treatment. Prohibited conclusions are effectiveness, destination fit,
owner acceptance, deployment readiness, and external outcome.

## Observed Trace

The authorized normalization ran with no deviation. Both pointer values were
recorded unchanged. Stops did not trigger, and final state equals the frozen
initial state. The required separate equality-comparison observation is absent:
the trace records neither `equal` nor `unequal`. No real people, real data,
external systems, or external actions were involved.

## Evidence Grade And Counterevidence

Evidence type is a validated but incomplete synthetic trace. Direct support is
limited to authorized execution, unchanged pointer values, no stop, no
deviation, and restored-equivalent final state. Counterevidence is the missing
plan-required comparison observation. The inference is that the bounded-pass
condition remains unmet; validator success is not an observation of equality.

## Affected-Party, Data, And Legitimacy Check

One synthetic reviewer role represents standing. No real party, source owner,
candidate owner, result owner, authority owner, or validator is represented.
Data is synthetic input only; risk and external action are `none`. No authority
or consent gap occurred inside the authorized trace, but missing standing and
the absent comparison observation limit the result.

## Result

Result: `unresolved`. The required equality observation is missing, so clean
execution, unchanged pointers, final-state restoration, and validation cannot
produce a bounded pass.

## Residual Uncertainty, Correction, And Recovery

The equality relation remains unobserved. Preserve the incomplete trace at
`synthetic://negative-evidence/SYNTH-SCORE-MISSING-OBSERVATION-001@r1`.
Correction owner is `synthetic-proving-plan-owner`; recovery preserves the
unchanged frozen state. The exact next wake is an immutable authorized trace
with the separate equality observation, or an owner decision on the returned
`defer` support.

## Permitted Disposition Return

Permitted support is `defer` only, returned to `synthetic-result-owner`. The
score creates no owner disposition and does not create P8, contact, transfer,
graduation, deployment, publication, or external action.

## Frontier Verification

- Verify all frozen pointers, revisions, content identifiers, and authority.
- Confirm the observed trace contains unchanged pointers but no separate
  equality observation.
- Confirm validation covers structure and execution integrity without being
  treated as the missing observation.
- Confirm the result remains `unresolved` and supports only `defer`.
- Confirm `CMD-0001`, P7, owner truth, and external-action state are unchanged.
