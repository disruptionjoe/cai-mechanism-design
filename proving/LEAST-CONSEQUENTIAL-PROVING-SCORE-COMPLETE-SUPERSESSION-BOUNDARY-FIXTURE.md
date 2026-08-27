---
artifact_type: synthetic_proving_score_complete_supersession_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Proving-Score Complete-Supersession Boundary Fixture

## Use Boundary

Use this fixture to score one exactly authorized synthetic trace when a later
immutable result-owner record completely supersedes two conflicting direct
observations. Keep every original and replacement observation visible. Valid
supersession can resolve the bounded trace relation, but it does not create
candidate-disposition, acceptance, transfer, graduation, deployment, or
external-action authority.

## Score Header

| Field | Value |
| --- | --- |
| `proving_id` | `SYNTH-SCORE-COMPLETE-SUPERSESSION-001@r1` |
| `plan_revision` | `SYNTH-PROVE-COMPLETE-SUPERSESSION-001@r1` |
| `candidate_id` | `SYNTH-CANDIDATE-COMPLETE-SUPERSESSION-001@r1` |
| `source_inquiry` | `SYNTH-SOURCE-COMPLETE-SUPERSESSION-001@r1` |
| `treatment_type` | `synthetic` |
| `result_owner` | `synthetic-result-owner` |
| `execution_authority_ref` | `synthetic://authorization/SYNTH-COMPLETE-SUPERSESSION-001@grant-r1` |
| `scored_by` | `synthetic-proving-scorer` |
| `scored_at` | `2026-08-27T10:12:50Z` |
| `external_action` | `none` |

## Frozen Plan And Evidence

| Package item | Immutable pointer | Content identifier |
| --- | --- | --- |
| Plan | `synthetic://plan/SYNTH-PROVE-COMPLETE-SUPERSESSION-001@r1` | `synthetic-content:plan-complete-supersession-001-r1` |
| Request | `synthetic://request/SYNTH-REQUEST-COMPLETE-SUPERSESSION-001@r1` | `synthetic-content:request-complete-supersession-001-r1` |
| Fixture | `synthetic://fixture/SYNTH-COMPLETE-SUPERSESSION-001@r1` | `synthetic-content:fixture-complete-supersession-001-r1` |
| Trace | `synthetic://trace/SYNTH-TRACE-COMPLETE-SUPERSESSION-001@r1` | `synthetic-content:trace-complete-supersession-001-r1` |
| Validation | `synthetic://validation/SYNTH-COMPLETE-SUPERSESSION-001@r1` | `synthetic-content:validation-complete-supersession-001-r1` |
| Supersession | `synthetic://supersession/SYNTH-COMPLETE-SUPERSESSION-001@r1` | `synthetic-content:supersession-complete-supersession-001-r1` |

The package is synthetic and frozen. Prohibited conclusions are effectiveness,
destination fit, owner acceptance, deployment readiness, and external outcome.

## Claim And Decision Conditions

- Exact claim: one authorized synthetic normalization preserves both input
  pointers and their equality relation.
- Falsifier: either pointer changes or one valid unsuperseded direct comparison
  observation records `unequal`.
- Bounded pass: both pointers remain unchanged and all valid unsuperseded
  direct comparison observations agree on `equal`.
- Unresolved route: valid unsuperseded direct comparison evidence conflicts.
- Stops: unauthorized operation or a source, fixture, data, standing,
  authority, or risk revision.
- Prohibited conclusions: effectiveness, destination fit, owner acceptance,
  deployment readiness, and external outcome.

## Observed Trace

The authorized normalization ran with no deviation. Both pointers remained
unchanged, stops did not trigger, and final state equals initial state. The
trace contains three readable, in-scope, provenance-valid direct observations:

- `synthetic-observation:comparison-equal-005-r1` records `equal`;
- `synthetic-observation:comparison-unequal-005a-r1` records `unequal`; and
- `synthetic-observation:comparison-unequal-005b-r1` records `unequal`.

No real people, data, systems, or external actions were involved.

## Evidence Grade And Counterevidence

The validator passed structure, identifiers, execution authority, chronology,
stops, and final state. It lists all three original direct observations and
marks `comparison_conflict: true`; it does not reconcile or supersede them.
Evidence grade is a validated synthetic trace plus the separately authorized
immutable supersession record. The two original `unequal` observations remain
visible as counterevidence and negative history even after supersession.

## Affected-Party, Data, And Legitimacy Check

One synthetic reviewer role represents standing; no real party or owner is
represented. Data is synthetic input only. No real consent, adoption, owner
acceptance, or destination fit is tested. Risk and external action are `none`.

## Result

After exact supersession, the valid unsuperseded evidence consists of
`synthetic-observation:comparison-equal-005-r1`,
`synthetic-observation:comparison-equal-005a-corrected-r1`, and
`synthetic-observation:comparison-equal-005b-corrected-r1`. All agree on
`equal`, both pointers remain unchanged, and the frozen plan supports
`bounded_pass`. The bounded pass does not establish effectiveness,
destination fit, owner acceptance, deployment readiness, disposition, or
external outcome.

## Residual Uncertainty, Correction, And Recovery

The later immutable record is signed by `synthetic-result-owner` under
`synthetic-result-owner-supersession@r1`. Its exact coverage names
`synthetic-observation:comparison-unequal-005a-r1` and
`synthetic-observation:comparison-unequal-005b-r1`, replacing them respectively
with `synthetic-observation:comparison-equal-005a-corrected-r1` and
`synthetic-observation:comparison-equal-005b-corrected-r1`. It explicitly does
not cover, invalidate, or supersede
`synthetic-observation:comparison-equal-005-r1`.

The authority is valid only for the two named replacements and supplies no
candidate-disposition, acceptance, transfer, graduation, deployment, or
external-action authority. Preserve the original conflict and complete
supersession relation at
`synthetic://negative-evidence/SYNTH-SCORE-COMPLETE-SUPERSESSION-001@r1`.
Correction owner is `synthetic-proving-plan-owner`. Recovery preserves the
unchanged frozen state, all three original observations, both replacement
observations, and exact supersession coverage. Exact next wake is an owner
decision on returned `defer` support, or a revision to source, trace,
supersession, standing, authority, or risk.

## Permitted Disposition Return

- Supported owner disposition: `defer`.
- Support boundary: the score supports only returning bounded evidence to the
  owner; it does not choose a disposition.
- Return owner: the repository-native candidate disposition authority.
- Exclusions: do not create `CMD-0001-P8`, modify `CMD-0001`, choose a
  disposition, or authorize contact, transfer, graduation, deployment,
  publication, or external action.

## Frontier Verification

- Verify complete exact supersession coverage of both original `unequal`
  observations and no coverage of the original `equal` observation.
- Confirm all three surviving observations are provenance-valid and record
  `equal`.
- Confirm unchanged pointers and the frozen plan support `bounded_pass`.
- Confirm result-owner supersession authority remains separate from candidate
  disposition, acceptance, transfer, graduation, deployment, and external
  action.
- Confirm the negative-evidence pointer, correction owner, recovery, exact
  wake, all original observations, and both replacements remain visible.
- Confirm `CMD-0001`, P7 defer, P8, and external-action state are unchanged.
