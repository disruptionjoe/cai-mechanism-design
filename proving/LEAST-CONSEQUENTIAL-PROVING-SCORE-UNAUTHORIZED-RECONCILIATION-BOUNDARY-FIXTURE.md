---
artifact_type: synthetic_proving_score_unauthorized_reconciliation_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Proving-Score Unauthorized-Reconciliation Boundary Fixture

## Use Boundary

This fixture scores one authorized synthetic trace with valid direct `equal`
and `unequal` observations plus a later reconciliation record that lacks
result-owner or supersession authority. It keeps all three records visible and
returns `unresolved` with `defer` support. It does not create `CMD-0001-P8`,
modify `CMD-0001`, choose a candidate disposition, or authorize contact,
transfer, graduation, deployment, publication, or external action.

## Score Header

- Score: `SYNTH-SCORE-UNAUTHORIZED-RECONCILIATION-001@r1`.
- Plan: `SYNTH-PROVE-UNAUTHORIZED-RECONCILIATION-001@r1`.
- Candidate: `SYNTH-CANDIDATE-UNAUTHORIZED-RECONCILIATION-001@r1`.
- Source: `SYNTH-SOURCE-UNAUTHORIZED-RECONCILIATION-001@r1`.
- Treatment: `synthetic`.
- Result owner: `synthetic-result-owner`.
- Execution authority:
  `synthetic://authorization/SYNTH-UNAUTHORIZED-RECONCILIATION-001@grant-r1`.
- Scorer and time: `synthetic-proving-scorer` at
  `2026-08-27T08:15:26Z`.
- External action: `none`.

## Frozen Plan And Evidence

- Plan: `synthetic://plan/SYNTH-PROVE-UNAUTHORIZED-RECONCILIATION-001@r1`,
  content identifier
  `synthetic-content:plan-unauthorized-reconciliation-001-r1`.
- Request:
  `synthetic://request/SYNTH-REQUEST-UNAUTHORIZED-RECONCILIATION-001@r1`,
  content identifier
  `synthetic-content:request-unauthorized-reconciliation-001-r1`.
- Fixture: `synthetic://fixture/SYNTH-UNAUTHORIZED-RECONCILIATION-001@r1`,
  content identifier
  `synthetic-content:fixture-unauthorized-reconciliation-001-r1`.
- Trace: `synthetic://trace/SYNTH-TRACE-UNAUTHORIZED-RECONCILIATION-001@r1`,
  content identifier
  `synthetic-content:trace-unauthorized-reconciliation-001-r1`.
- Validation:
  `synthetic://validation/SYNTH-UNAUTHORIZED-RECONCILIATION-001@r1`, content
  identifier `synthetic-content:validation-unauthorized-reconciliation-001-r1`.
- Reconciliation:
  `synthetic://reconciliation/SYNTH-UNAUTHORIZED-RECONCILIATION-001@r1`,
  content identifier
  `synthetic-content:reconciliation-unauthorized-reconciliation-001-r1`.

## Claim And Decision Conditions

The claim is that one authorized synthetic normalization preserves both input
pointers and their equality relation. Either pointer changing or one valid
direct comparison observation recording `unequal` is a falsifier. A bounded
pass requires both pointers unchanged and all valid direct comparison
observations agreeing on `equal`. Conflicting direct evidence remains
unresolved unless one immutable record with applicable result-owner authority
explicitly supersedes every conflicting observation. Stop on unauthorized
operation or source, fixture, data, standing, authority, or risk revision.
Prohibited conclusions are effectiveness, destination fit, owner acceptance,
deployment readiness, and external outcome.

## Observed Trace

The authorized normalization ran with no deviation. Both pointers remained
unchanged; stops did not trigger; final state equals initial state. Valid direct
observation `synthetic-observation:comparison-equal-003-r1` records `equal` and
valid direct observation `synthetic-observation:comparison-unequal-003-r1`
records `unequal`. Both are readable, in scope, and provenance-valid. No real
people, data, systems, or external actions were involved.

## Evidence Grade And Counterevidence

Evidence type is a validated synthetic trace with conflicting direct
observations and an unauthorized reconciliation. The validator passed
structure, identifiers, execution authority, chronology, stops, and final
state; it lists both observations and marks `comparison_conflict: true`. The
later reconciliation record asserts `equal controls`, but its signer is
`synthetic-checksum-reviewer`, its authority is `checksum_review_only`, and
its result-owner or supersession authority is `none`. Structural validity,
chronology, and signature shape do not confer reconciliation authority.

## Affected-Party, Data, And Legitimacy Check

One synthetic reviewer role represents standing; no real party or owner is
represented. Data is synthetic input only; risk and external action are
`none`. The evidence conflict limits the score and creates no owner or real-
world conclusion.

## Result

Result: `unresolved`. Direct observations remain conflicting. Validator
success and the later unauthorized reconciliation do not satisfy the plan's
supersession condition, so neither bounded pass nor bounded failure is
supported. Preserve the reconciliation-authority failure as negative evidence.

## Residual Uncertainty, Correction, And Recovery

Preserve negative evidence at
`synthetic://negative-evidence/SYNTH-SCORE-UNAUTHORIZED-RECONCILIATION-001@r1`.
Correction owner is `synthetic-proving-plan-owner`; recovery preserves the
unchanged frozen state. The exact next wake is an immutable reconciliation or
supersession record with applicable result-owner authority covering both
direct observations, or an owner decision on returned `defer` support.

## Permitted Disposition Return

Permitted support is `defer` only, returned to `synthetic-result-owner`. The
score creates no candidate disposition, P8, contact, transfer, graduation,
deployment, publication, or external action. `CMD-0001` remains deferred.

## Frontier Verification

- Verify every frozen pointer, content identifier, authority, and timestamp.
- Confirm both direct observations remain readable, in scope, provenance-valid,
  and unreconciled.
- Confirm the validator and later record have no authority to invalidate,
  reconcile, or supersede either direct observation.
- Confirm chronology and signature shape are not treated as authority.
- Confirm the result remains `unresolved` and supports only `defer`.
- Confirm `CMD-0001`, P7, owner truth, and external-action state are unchanged.
