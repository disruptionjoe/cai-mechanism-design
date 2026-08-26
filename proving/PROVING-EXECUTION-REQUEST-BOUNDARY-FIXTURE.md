---
artifact_type: synthetic_proving_execution_request_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Proving Execution Request Boundary Fixture

## Use Boundary

This fixture freezes a synthetic proving request for authorization review. It
does not grant or execute the treatment, score evidence, disposition a
candidate, create `CMD-0001-P8`, or authorize contact, transfer, graduation,
deployment, publication, or external action.

## Request Header

| Field | Value |
| --- | --- |
| `request_id` | `SYNTH-REQ-001` |
| `proving_id` | `SYNTH-PROVE-001` |
| `plan_revision` | `r1` |
| `candidate_id` | `SYNTH-CANDIDATE-REQUEST-001@r1` |
| `source_inquiry` | `SYNTH-SOURCE-REQUEST-001@r1` |
| `requester` | `synthetic-request-preparer` |
| `proposed_executor` | `synthetic-executor` |
| `authority_owner` | `synthetic-authority-owner` |
| `requested_at` | `2026-08-26T00:00:00Z` |
| `external_action` | `none` |

## Frozen Plan And Evidence

- Exact plan: `SYNTH-PROVE-001@r1`; no path or hash was supplied, so none is
  inferred.
- Claim: copying immutable synthetic input `alpha` to an isolated in-memory
  output and relabeling only the copy `beta` can test whether the trace keeps
  input and output distinct.
- Source: `SYNTH-SOURCE-REQUEST-001@r1`.
- Fixture: `synthetic://fixture/SYNTH-REQUEST-001@r1`, containing only the
  public labels `alpha` and `beta`.
- Evidence: the frozen request, plan, and control fixtures embedded in the
  source packet; no execution evidence exists.
- Environment: requested isolated volatile memory with no network,
  persistence, account, or external action.
- Prohibited inference: this request supports no execution, observation,
  bounded pass, score, candidate evidence, disposition, or real-data claim.

## Requested Treatment And Least-Consequence Case

- Requested operations: read the immutable input, copy it in memory, relabel
  only the copy, emit a text diff, and discard the copy.
- Inputs: the immutable public synthetic label `alpha`.
- Outputs: an in-memory copy labeled `beta` and a text diff, both without
  persistence after review.
- Falsifier: any mutation of the input or any trace that merges input and
  output.
- Observable failure: an input change, missing diff, or merged identity.
- Bounded pass: an unchanged input plus a distinct diff.
- Unresolved route: real data or any persistent output.
- Alternatives: no action; or manual comparison, which is equally safe but
  supplies less trace discrimination.
- Discrimination value: whether a trace can keep immutable input and derived
  output distinct.
- Reversibility: discard the copy and return to the immutable input.

## Requested Authority Scope

- Proposed actor: `synthetic-executor`.
- Requested operations: only the five operations listed in the treatment.
- Requested inputs and outputs: public labels `alpha` and `beta`, one volatile
  copy, and one non-persistent text diff.
- Environment: isolated volatile memory with no network, persistence, account,
  or external action.
- Requested validity: only while the frozen plan, actors, operations, inputs,
  outputs, environment, and authority remain unchanged.
- Deviations: prohibited without a fresh decision.
- Correction, rollback, and recovery: discard the copy and return to the
  immutable input.
- Stop authority: not supplied; this remains an authorization-review gap.
- Forbidden effects: input mutation, persistence, network use, account use,
  real data, contact, transfer, graduation, deployment, publication, and
  external action.

## Affected Parties, Data, And Legitimacy

- Represented standing: one synthetic reviewer role.
- Representation limits: no real person or institution is represented.
- Risk bearer: only the synthetic fixture boundary; no real risk bearer is
  represented.
- Data boundary: two public synthetic labels, a volatile copy, no retention,
  and no exposure outside the isolated environment.
- Capture concerns: none supplied; no absence is treated as a positive claim.
- Authority gap: exact authorization evidence is `none`.
- Cannot be spoken for: any real person, institution, candidate owner, or
  destination owner.

## Stops And Start-State Checks

- Pre-start stop: missing exact authorization.
- Live stops: input mutation, persistence, network access, or trace ambiguity.
- Invalidation: any plan, actor, operation, input, output, environment, or
  authority change.
- Last-known-good state: the immutable input.
- Dependencies: an exact decision from `synthetic-authority-owner` and a
  supplied stop-authority rule.
- New-authorization condition: every material change requires a fresh decision.

## Prepared Request

- State: `ready_for_authorization_review`.
- Rationale: the bounded treatment and stops are frozen, while exact authority
  remains absent and execution stays stopped.
- Exact requested effect: the volatile synthetic transformation described
  above, if separately authorized.
- Explicit non-effects: no grant, execution, observation, score, disposition,
  transfer, graduation, deployment, publication, or external action.
- Next owner: `synthetic-authority-owner`; this pointer creates no contact
  authority.
- Exact next wake: an exact authorization decision or material plan change.

## Proposed Execution Handoff

- Proposed trace destination: `synthetic://trace/SYNTH-REQUEST-001`.
- Proposed score owner: `synthetic-result-owner`.
- Acknowledgment state: `unacknowledged`.
- Authorization pointer: `none`.
- Handoff state: `ready_for_authorization_review`.

## Frontier Verification

- Verify the request preserves the frozen claim, falsifier, failure, bounded
  pass, unresolved route, stops, environment, and recovery route.
- Confirm the represented standing is only a synthetic reviewer role.
- Confirm authorization evidence and pointer remain `none` and the pre-start
  stop remains active.
- Confirm no treatment event, observation, score, P8 record, disposition, or
  external action is claimed.
