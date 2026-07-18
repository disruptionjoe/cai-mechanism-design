---
score_id: CMD-0001-P2-S1
candidate_id: CMD-0001
proving_id: CMD-0001-P2
status: scored_bounded_pass_defer
created: 2026-07-18
external_action: none
---

# CMD-0001-P2 Synthetic Score

## Boundary

This score uses only the synthetic rows in
`CMD-0001-P2-typed-register-hostile-paperwork-test.md`. It does not use
accident records, confidential material, human subjects, field work, account
access, external contact, deployment, incentives, or destination-owner
authority.

The score asks whether the typed minimum register blocks the paperwork absorber
identified by `CMD-0001-P1`: a record that appears complete in prose while the
contradiction remains invisible in data.

## Row Scores

| Row | Expected behavior | Score | Reason |
|---|---|---|---|
| H1 paperwork completion | Fail when changed input path is omitted. | Pass | A row cannot pass without `change_event_type` and `change_event_source`; prose-only "reviewed" is insufficient. |
| H2 stale assumption reuse | Fail unless validation status changes. | Pass | The row rule forces re-evaluation after a changed environment and prevents silent `valid` status by omission. |
| H3 central-review absorption | Fail unless lower-owner route is impossible and explicit. | Pass | The typed revision requires `lowest_fitting_owner_route`; generic central routing is valid only with a stated no-lower-owner reason. |
| H4 source-preserving correction | Pass without deciding technical outcome. | Pass | The typed fields can preserve assumption, source revision, owner, contradiction, and correction route without claiming the domain answer. |

## Result

Disposition for this second synthetic test: bounded pass, defer.

The typed minimum register blocks the specific hostile paperwork absorber in
this synthetic fixture. It is stronger than the P1 narrative version because a
formally complete row still fails when contradiction visibility exists only in
free text.

This result does not justify graduation, transfer, broader proving, deployment,
or destination-owner obligations. It proves only that the current typed row
rules survive the named synthetic absorber.

## Residual Risks

- A bad actor can still fill typed fields with weak but plausible-looking
  routes; source and correction quality need later tests.
- A real setting may have an existing domain owner whose tools defeat this
  candidate.
- The current source pattern is still mostly aerospace-derived through
  `SF-0001` and `SF-0002`; a third non-aerospace fixture is needed before
  stronger claims.
- A central reviewer could still accumulate too much interpretive power if
  owner-route justifications are not audited.

## Next Condition

Keep `CMD-0001` admitted but deferred. Reopen it only when CAI Systemic Failure
supplies a non-aerospace source-backed record or when a destination owner
explicitly asks for synthetic translation review.

No external action, human or field testing, deployment, participation, account,
incentive, spin-out, aviation remedy, or destination-owner obligation is
authorized.

