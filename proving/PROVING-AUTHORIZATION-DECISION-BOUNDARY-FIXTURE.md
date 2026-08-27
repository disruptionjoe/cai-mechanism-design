---
artifact_type: synthetic_proving_authorization_decision_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Proving Authorization Decision Boundary Fixture

## Use Boundary

This fixture prepares a denied-start decision from frozen synthetic evidence.
Missing authority remains a pre-start stop. The fixture creates no grant,
execution, observation, score, candidate evidence, disposition, transfer,
graduation, deployment, publication, or external action.

## Decision Header

| Field | Value |
| --- | --- |
| `authorization_id` | `pending` |
| `proving_id` | `SYNTH-PROVE-001` |
| `plan_revision` | `r1` |
| `candidate_id` | `SYNTH-CANDIDATE-REQUEST-001@r1` |
| `source_inquiry` | `SYNTH-SOURCE-REQUEST-001@r1` |
| `authority_owner` | `synthetic-authority-owner` |
| `authorization_ref` | `pending` |
| `decided_by` | `pending` |
| `decided_at` | `pending` |
| `external_action` | `none` |

## Frozen Request And Plan

- Request: `SYNTH-REQ-001`; no path or hash was supplied, so none is inferred.
- Plan: `SYNTH-PROVE-001@r1`; no path or hash was supplied, so none is inferred.
- Candidate: `SYNTH-CANDIDATE-REQUEST-001@r1`.
- Source: `SYNTH-SOURCE-REQUEST-001@r1`.
- Fixture: `synthetic://fixture/SYNTH-REQUEST-001@r1`.
- Proposed executor: `synthetic-executor`; this is not an operative actor.
- Authorization pointer: `none`.
- Acknowledgment: `unacknowledged`.
- Execution evidence: none; no execution or result is recorded.
- Prohibited inference: this decision supports no execution, observation,
  bounded pass, score, candidate evidence, disposition, or real-data claim.

## Claim, Treatment, And Least-Consequence Check

- Claim: copying immutable synthetic input `alpha` to an isolated in-memory
  output and relabeling only the copy `beta` can test whether the trace keeps
  input and output distinct.
- Proposed operations: read the immutable input, copy it in memory, relabel
  only the copy, emit a text diff, and discard the copy.
- Falsifier: input mutation or merged identity.
- Observable failure: input change, missing diff, or merged identity.
- Bounded pass: unchanged input plus a distinct diff.
- Unresolved route: real data or any persistent output.
- Least-consequence result: no action is least consequential; manual comparison
  is equally safe but supplies less trace discrimination.
- Last-known-good state: the immutable input.

The claim, treatment, falsifier, failure, pass, and unresolved route remain
requested plan fields. None is executed or observed by this fixture.

## Authority Scope

- Requested actor: `synthetic-executor`; non-operative.
- Requested operations: the five proposed operations above; non-operative.
- Requested inputs and outputs: immutable `alpha`, a proposed volatile copy
  labeled `beta`, and a proposed text diff; non-operative.
- Requested environment: isolated volatile memory with no network,
  persistence, account, or external action; non-operative.
- Requested validity: only while the plan, actor, operation, input, output,
  environment, and authority remain unchanged; non-operative.
- Deviations: any deviation would require a fresh decision.
- Authority evidence: none.
- Authorized decision-maker: pending.
- Decision timestamp: pending.
- Stop-authority rule: unresolved.
- Exact authorized effect: none.
- Correction and recovery: discard any copy and return to the immutable input;
  no copy has been created.

Missing or unresolved authority fields deny the start. They do not imply a
narrower grant.

## Affected Parties, Data, And Legitimacy

- Represented standing: one synthetic reviewer role.
- Representation limits: no real person or institution is represented.
- Risk bearers: not supplied; no real risk bearer is inferred.
- Proposed data boundary: public synthetic labels `alpha` and `beta`, a
  proposed volatile copy, no retention, and no external exposure.
- Actual data handling: none; the treatment did not start.
- Capture concerns: not supplied; absence is not treated as a positive claim.
- Consent or authority gap: exact authorization and a stop-authority rule are
  missing, so the treatment is not authorized.
- Cannot be spoken for: any real person, institution, candidate owner, or
  destination owner.

## Stops And Consequence Boundary

- Pre-execution stop: missing exact authorization.
- Live stops if a future grant exists: input mutation, persistence, network
  access, or trace ambiguity.
- Invalidation: any plan, actor, operation, input, output, environment, or
  authority change.
- Deviation handling: do not start; a material change requires a fresh decision.
- Escalation owner: `synthetic-authority-owner`; this pointer creates no contact
  authority.
- Correction and recovery: discard any copy and return to the immutable input.

## Prepared Decision

- Decision: `defer`.
- Rationale: no authority evidence, authorized decision-maker, decision time,
  stop-authority rule, or operative grant exists.
- Exact authorized effect: none.
- Explicit non-effects: no grant, execution, observation, score, candidate
  evidence, disposition, transfer, graduation, deployment, publication, or
  external action.
- Validation: the frozen request, plan, authority gaps, stops, correction, and
  acknowledgment boundary are preserved; no treatment check was executed.
- Exact next wake: an exact authority decision or material plan change.

## Execution Handoff

- Exact executor: none; `synthetic-executor` remains only the proposed actor.
- Plan and authority pointers: `SYNTH-PROVE-001@r1` and authorization `none`.
- Start-state checks: not run because the pre-execution authority stop remains active.
- Trace destination: none is operative.
- Score owner: none is operative.
- Acknowledgment state: `unacknowledged`.
- Prohibited actions: treatment execution, real data, persistence, network or
  account use, contact, transfer, graduation, deployment, publication, or
  external action.

## Frontier Verification

- Confirm request, plan, candidate, source, fixture, proposed actor, authority
  owner, and acknowledgment match the frozen evidence.
- Confirm claim, falsifier, failure, pass, unresolved route, and last-known-good
  state remain requested plan fields rather than completed observations.
- Confirm requested actor, operations, inputs, outputs, and environment remain
  non-operative and exact authorized effect remains none.
- Confirm authority evidence, authorized decision-maker, decision time,
  stop-authority rule, and operative grant remain missing or unresolved.
- Confirm no treatment, data handling, observation, score, candidate evidence,
  disposition, P8 record, or external action is claimed.
