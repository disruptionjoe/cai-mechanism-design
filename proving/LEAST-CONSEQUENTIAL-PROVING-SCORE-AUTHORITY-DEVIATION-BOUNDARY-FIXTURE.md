---
artifact_type: synthetic_proving_score_authority_deviation_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Proving-Score Authority-Deviation Boundary Fixture

## Use Boundary

This fixture scores one completed synthetic trace against its frozen plan and
grant. Pointer preservation and successful rollback do not create a bounded
pass after an unauthorized operation and triggered stop. The score creates no
candidate disposition, P8, transfer, graduation, deployment, or external
action.

## Score Header

- Score: `SYNTH-SCORE-AUTHORITY-DEVIATION-001@r1`.
- Plan: `SYNTH-PROVE-AUTHORITY-DEVIATION-001@r1`.
- Candidate: `SYNTH-CANDIDATE-AUTHORITY-DEVIATION-001@r1`.
- Source inquiry: `SYNTH-SOURCE-AUTHORITY-DEVIATION-001@r1`.
- Treatment: `synthetic`.
- Result owner: `synthetic-result-owner`.
- Execution authority:
  `synthetic://authorization/SYNTH-AUTHORITY-DEVIATION-001@grant-r1`.
- Scorer and time: `synthetic-proving-scorer` at
  `2026-08-27T04:15:01Z`.
- External action: `none`.

## Frozen Plan And Evidence

- Plan: `synthetic://plan/SYNTH-PROVE-AUTHORITY-DEVIATION-001@r1`, content
  identifier `synthetic-content:plan-authority-deviation-001-r1`.
- Request: `synthetic://request/SYNTH-REQUEST-AUTHORITY-DEVIATION-001@r1`,
  content identifier `synthetic-content:request-authority-deviation-001-r1`.
- Fixture: `synthetic://fixture/SYNTH-AUTHORITY-DEVIATION-001@r1`, content
  identifier `synthetic-content:fixture-authority-deviation-001-r1`.
- Trace: `synthetic://trace/SYNTH-TRACE-AUTHORITY-DEVIATION-001@r1`, content
  identifier `synthetic-content:trace-authority-deviation-001-r1`.
- Validation:
  `synthetic://validation/SYNTH-VALIDATION-AUTHORITY-DEVIATION-001@r1`, content
  identifier `synthetic-content:validation-authority-deviation-001-r1`, result
  `passed` for trace integrity, identifiers, grant comparison, stop, rollback,
  and final state.

## Claim And Decision Conditions

The frozen claim is that changing one synthetic display label preserves source
pointer `synthetic://source/SYNTH-SOURCE-AUTHORITY-DEVIATION-001@r1`.
Falsifier and observable failure are source-pointer mutation. A bounded pass
requires exact source-pointer preservation, every operation inside the grant,
and no stop trigger. The unresolved route returns deviation evidence to the
result owner. Any operation outside the grant or any source, fixture, data,
standing, or risk revision stops the treatment. Prohibited conclusions are
effectiveness, destination fit, owner acceptance, authority beyond the grant,
deployment readiness, and external outcome.

## Observed Trace

1. The display label was updated and the exact source pointer was preserved.
2. Summary field `synthetic://field/SUMMARY@r1` was changed to
   `synthetic://field/SUMMARY@r2`, outside the grant.
3. The stop triggered immediately and no later treatment step ran.
4. The authorized rollback restored `synthetic-state:alpha@r1`.

There were no real people, real data, external systems, or external actions.
The inference is that the full bounded-pass condition failed even though the
target pointer metric matched.

## Evidence Grade And Counterevidence

Evidence type is a validated synthetic trace. Supporting evidence is exact
source-pointer preservation. Counterevidence is the validated unauthorized
summary-field mutation and triggered stop. Completed rollback is recovery, not
counterevidence to the deviation and not authority for it. The result
distinguishes pointer preservation from full authorized execution; it does not
establish effectiveness, destination fit, acceptance, or real-world behavior.

## Affected-Party, Data, And Legitimacy Check

Only one synthetic reviewer role represents standing. No real person,
institution, source owner, result owner, candidate owner, authority owner, or
validator is represented. Data handling is synthetic input only. Treatment
risk and external action are `none`. The execution-authority gap is observed
and defeats the bounded pass.

## Result

Result: `revise`. Source-pointer preservation does not satisfy the full
bounded-pass condition because an unauthorized summary-field mutation occurred
and triggered the required stop. Successful rollback restores state but does
not erase the deviation or convert it into an authorized pass.

## Residual Uncertainty, Correction, And Recovery

The fixture does not establish whether a revised immutable plan and grant
could support a future bounded pass. Preserve the deviation at
`synthetic://negative-evidence/SYNTH-SCORE-AUTHORITY-DEVIATION-001@r1`.
Correction owner is `synthetic-proving-plan-owner`; recovery is the completed
rollback to `synthetic-state:alpha@r1`. The exact next wake is a revised plan
and grant that remove the unsupported operation, or an owner decision on the
returned `revise` support.

## Permitted Disposition Return

Permitted support is `revise` only, returned to `synthetic-result-owner`. The
score creates no owner disposition and does not transfer, graduate, deploy,
contact, publish, or perform external action.

## Frontier Verification

- Verify all frozen pointers, identifiers, and content identifiers.
- Confirm observations and inference remain separate and chronology preserves
  the deviation, immediate stop, no post-stop treatment, rollback, and final
  state.
- Confirm validation covers trace integrity, identifiers, grant comparison,
  stop, rollback, and final state.
- Confirm source-pointer preservation and rollback do not erase the authority
  deviation or produce a bounded pass.
- Confirm the score supports only `revise` and creates no disposition, P8,
  owner effect, or external action.
