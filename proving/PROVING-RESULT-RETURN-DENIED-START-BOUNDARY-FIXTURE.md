---
artifact_type: synthetic_proving_result_return_denied_start_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Proving Result Return Denied-Start Boundary Fixture

## Use Boundary

This artifact applies the proving-result return boundary after a denied start.
It performs no treatment, scoring, result creation, return, acknowledgment,
candidate disposition, transfer, graduation, deployment, publication, or
external action. The denied-start trace is preserved as pre-start evidence; it
is not an authorized observed execution trace.

## Return Header

| Field | Value |
| --- | --- |
| `return_id` | `SYNTH-RETURN-DENIED-001@r1` |
| `proving_id` | `SYNTH-PROVE-001@r1` |
| `trace_revision` | `SYNTH-TRACE-DENIED-001@r1` |
| `score_revision` | `none` |
| `candidate_id` | `SYNTH-CANDIDATE-REQUEST-001@r1` |
| `source_inquiry` | `SYNTH-SOURCE-REQUEST-001@r1` |
| `result_owner` | `synthetic-result-owner` |
| `prepared_by` | `synthetic-return-preparer` |
| `prepared_at` | `2026-08-27T01:14:29Z` |
| `external_action` | `none` |

## Frozen Result Package

- Plan: `synthetic://plan/SYNTH-PROVE-001@r1`.
- Request and decision:
  `synthetic://decision/SYNTH-REQ-001@defer-r1`.
- Fixture: `synthetic://fixture/SYNTH-REQUEST-001@r1`.
- Denied-start trace:
  `synthetic://trace/SYNTH-TRACE-DENIED-001@r1`.
- Content hashes, authorized observed execution evidence, score, score
  revision, validation, operative authority, and result package: `none`.

No tested claim, falsifier, observable failure, bounded-pass condition,
unresolved route, or prohibited-conclusion set was supplied as an authorized
completed package.

## Result-Return Gate

- Gate: `failed_closed`.
- Required execution-trace status: `denied_start_only`.
- Required score status: `missing`.
- Result state: `not_created`.
- Result value: `none`.
- Permitted disposition support: `none`.
- Owner return: `not_sent`.
- Receipt acknowledgment: `unacknowledged`.

The denial and missing package support no bounded pass, revise, kill,
defer-result, unresolved-result, candidate disposition, or owner acceptance
claim.

## Tested Claim And Conditions

No authorized completed claim-and-conditions set was supplied. No claim,
falsifier, observable failure, bounded-pass condition, unresolved route, stop
status, or prohibited-conclusion set is copied into a result return.

## Observed Result

Result: `none`. The denied-start record proves only the failed-closed pre-start
boundary. No authorized observed execution trace and score support selection
of a result value.

## Evidence Grade, Counterevidence, And Failure

The evidence is synthetic pre-start denial evidence. Authority evidence,
authorized decision-maker, decision time, stop-authority rule, operative
grant, observed execution evidence, score, and validation are missing or
unresolved. The proposed actor and treatment remain non-operative. The
authority gap caused the pre-start halt. Actual data handling, treatment risk,
deviation, and execution effect are `none`.

## Affected-Party, Data, And Legitimacy Return

One synthetic reviewer role represents standing. No real person, institution,
source owner, result owner, candidate owner, or authority owner is represented
or spoken for. Actual data handling and treatment risk are `none`; no consent,
authority, contact, or external-action effect occurred.

## Residual Uncertainty, Correction, And Recovery

Operative authority and every execution-to-result prerequisite remain
unresolved. No correction, rollback, or recovery action occurred. The
available recovery route is to remain at immutable input `alpha`. The exact
next wake is an immutable operative authorization plus an authorized observed
trace, score, and validation package for this exact frozen plan.

## Permitted Disposition Support

Support: `none`. This fixture creates no owner disposition and does not convert
the authorization decision's `defer` value into a proving-result disposition.

## Owner Return

State: `not_sent`. Acknowledgment: `unacknowledged`. The intended result-owner
pointer creates no return, receipt, acceptance, disposition, or owner effect.

## Frontier Verification

- Verify gate `failed_closed`, trace `denied_start_only`, score `missing`,
  result state `not_created`, result value `none`, and external action `none`.
- Verify the plan, decision, fixture, and denied-trace pointers exactly.
- Confirm the denied-start trace is preserved without becoming authorized
  observed execution evidence.
- Confirm no score, result, disposition support, owner return,
  acknowledgment, P8, or external action exists.
- Confirm the recovery state remains immutable input `alpha` and `CMD-0001`
  remains deferred.
