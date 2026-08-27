---
artifact_type: synthetic_proving_execution_trace_denied_start_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Proving Execution Trace Denied-Start Boundary Fixture

## Use Boundary

This fixture records a frozen pre-start halt. It does not authorize or execute
a treatment, fabricate an event or observation, score evidence, create a
candidate disposition, create `CMD-0001-P8`, or authorize contact, transfer,
graduation, deployment, publication, or external action. The prepared decision
for request `SYNTH-REQ-001` remains `defer`, with exact authorized effect
`none`.

## Trace Header

| Field | Value |
| --- | --- |
| `trace_id` | `SYNTH-TRACE-DENIED-001@r1` |
| `proving_plan` | `SYNTH-PROVE-001@r1` |
| `candidate_id` | `SYNTH-CANDIDATE-REQUEST-001@r1` |
| `source_inquiry` | `SYNTH-SOURCE-REQUEST-001@r1` |
| `result_owner` | `synthetic-result-owner` |
| `treatment_type` | `proposed_volatile_copy_and_relabel` |
| `execution_authority` | `none` |
| `operator` | `none` |
| `started_at` | `none` |
| `completed_at` | `none` |
| `external_action` | `none` |

## Frozen Start Conditions

- Request: `SYNTH-REQ-001`.
- Plan: `SYNTH-PROVE-001@r1`.
- Fixture: `synthetic://fixture/SYNTH-REQUEST-001@r1`.
- Path, hash, validation run, environment instance, and execution artifact:
  `not_supplied`.
- Last-known-good state: immutable input `alpha`.
- Pre-execution authority check: `failed_closed`.
- Authorization pointer: `none`.
- Exact authorized effect: `none`.
- Stop-authority rule: `unresolved`.
- Treatment start: `none`; no treatment began.

## Treatment Boundary

The requested operations were to read immutable input `alpha`, copy it in
volatile memory, relabel only the copy `beta`, emit a text diff, and discard the
copy. Those operations, inputs, outputs, and an isolated environment were
requested but never authorized or executed. Allowed operations, inputs,
outputs, and environment under the operative authority are `none`. One
synthetic reviewer role represents standing; no real person or institution is
represented. No data was handled.

## Chronological Observed Trace

No execution event exists. No transformation, data handling, observation,
artifact, operator action, start, completion, correction, rollback, recovery
action, score package, or result exists. The pre-start halt is not converted
into an execution event.

## Stop And Deviation Log

| Field | Value |
| --- | --- |
| condition | missing exact authorization |
| status | `triggered` |
| missing evidence | authority evidence, authorized decision-maker, decision time, stop-authority rule, and operative grant |
| authority effect | `invalidated` |
| action taken | `halt` |
| execution halted | `yes` |
| evidence pointer | frozen denied decision for `SYNTH-REQ-001` |

No execution occurred, so no execution deviation exists.

## Evidence Integrity And Counterevidence

Request, plan, fixture, candidate, source, and denied-decision identifiers are
preserved. No path, content hash, validation run, environment instance,
execution artifact, observed-event evidence, or score evidence was supplied.
The denied decision is direct counterevidence to any claim that treatment was
authorized or executed. Missing authority and execution provenance prevent an
execution result, score, or candidate-evidence claim.

## Affected-Party, Data, And Legitimacy Trace

One synthetic reviewer role represents standing. No real person, institution,
source owner, result owner, or authority owner is represented or can be spoken
for. Actual data handling, transformation, retention, and exposure are `none`.
The unresolved authority and stop-authority evidence caused the failed-closed
halt before any treatment or risk-bearing effect.

## Correction, Rollback, And Recovery

No correction, rollback, or recovery action was performed because no action or
state change occurred. The available last-known-good route is to remain at
immutable input `alpha`. `synthetic-authority-owner` is named only as owner of
a possible future authorized decision; that pointer creates no current grant
or recovery action.

## Score Return Package

State is `not_created`. No execution trace artifact beyond this denied-start
boundary record, validation pointer, observed treatment, score, result, P8
evidence, or candidate disposition exists. The separately existing
`CMD-0001` defer remains unchanged and is not evidence for this synthetic
request.

## Frontier Verification

- Confirm the authority check is `failed_closed`, authorization pointer is
  `none`, and exact authorized effect is `none`.
- Confirm the stop is `triggered`, authority effect is `invalidated`, action is
  `halt`, and execution halted is `yes`.
- Confirm no execution event, operation, data handling, transformation,
  artifact, score, result, or candidate disposition is claimed.
- Confirm the one represented synthetic reviewer role is not erased or turned
  into representation of a real party or owner.
- Confirm recovery remains only the unchanged input `alpha` and a future-owner
  pointer creates no authority.
- Confirm no P8, contact, transfer, graduation, deployment, publication, or
  external action is created.
