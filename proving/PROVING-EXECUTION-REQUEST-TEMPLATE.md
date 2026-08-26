---
artifact_type: proving_execution_request_template
status: candidate_process_artifact
external_action: none
---

# Proving Execution Request Template

## Use Boundary

Use this artifact only to prepare one request for a proving treatment against
an exact frozen plan. Completing it does not authorize or execute the
treatment, score evidence, disposition a candidate, transfer, graduate,
deploy, contact, publish, or perform external action. Synthetic and reversible
work still requires an exact current grant before execution. Do not create a
real proving identifier or invent evidence, actors, owners, authority,
conditions, observations, dates, decisions, or results merely to fill a field.

## Request Header

| Field | Value |
| --- | --- |
| `request_id` | `[required: stable request identifier]` |
| `proving_id` | `[required: exact proving-plan identifier]` |
| `plan_revision` | `[required: immutable plan revision]` |
| `candidate_id` | `[required: exact candidate identifier and revision]` |
| `source_inquiry` | `[required: exact source-inquiry pointer and revision]` |
| `requester` | `[required: actor preparing the request]` |
| `proposed_executor` | `[required: exact proposed actor; not authorization]` |
| `authority_owner` | `[required: owner of the requested authority]` |
| `requested_at` | `[required: ISO-8601 timestamp]` |
| `external_action` | `none` |

## Frozen Plan And Evidence

- Exact plan: `[required: path, revision, and hash]`
- Claim: `[required: copied unchanged from the frozen plan]`
- Source: `[required: inquiry, revision, provenance, and hash]`
- Fixture: `[required: pointer, revision, provenance, and hash]`
- Evidence: `[required: immutable claim-level pointers]`
- Validation: `[required: checks, versions, and results]`
- Environment: `[required: exact isolated execution environment]`
- Prohibited inference: `[required: conclusions outside the request and plan]`

## Requested Treatment And Least-Consequence Case

- Requested operations: `[required: exact proposed transformations]`
- Inputs: `[required: exact data and artifact classes]`
- Outputs: `[required: exact trace and result artifacts]`
- Falsifier: `[required: copied unchanged from the frozen plan]`
- Observable failure: `[required: copied unchanged from the frozen plan]`
- Bounded pass: `[required: copied unchanged from the frozen plan]`
- Unresolved route: `[required: copied unchanged from the frozen plan]`
- Alternatives: `[required: no action and materially different treatments]`
- Discrimination value: `[required: what this treatment could distinguish]`
- Reversibility: `[required: last-known-good state and restoration path]`
- Why no less consequential treatment suffices: `[required: evidence-bound rationale]`

## Requested Authority Scope

- Proposed actor: `[required: exact executor requested]`
- Requested operations: `[required: complete operation list]`
- Requested inputs and outputs: `[required: exact classes and destinations]`
- Environment: `[required: isolated boundary and relevant versions]`
- Requested validity: `[required: interval or exact start and end conditions]`
- Deviations: `[required: prohibited, separately authorized, or exact narrow request]`
- Correction: `[required: requested correction route]`
- Rollback and recovery: `[required: exact restoration route]`
- Stop authority: `[required: who must be able to stop and under what conditions]`
- Forbidden effects: `[required: effects outside the requested grant]`

These fields describe requested authority only. They create no grant and must
not be copied into an execution trace as if authorized.

## Affected Parties, Data, And Legitimacy

- Represented standing: `[required: parties represented and evidence]`
- Representation limits: `[required: absent or simulated standing]`
- Risk bearers: `[required: who bears request or treatment risk]`
- Data boundary: `[required: provenance, class, transformation, retention, and exposure]`
- Capture concerns: `[required: incentives or structures that could distort review]`
- Consent or authority gaps: `[required: unresolved gaps and review effect]`
- Cannot be spoken for: `[required: people or owners this request does not represent]`

## Stops And Start-State Checks

- Pre-start stops: `[required: conditions that prevent execution]`
- Live stops: `[required: observable conditions that halt execution]`
- Invalidation conditions: `[required: evidence, authority, or state changes that void the request]`
- Last-known-good state: `[required: state and recovery pointer]`
- Dependencies: `[required: exact prerequisites and owners]`
- New-authorization conditions: `[required: every material change that requires a fresh decision]`

## Prepared Request

- State: `[required: exactly one of ready_for_authorization_review, request_revision, defer, reject, or needs_judgment]`
- Rationale: `[required: one evidence-bound reason]`
- Exact requested effect: `[required: narrow effect, or none]`
- Explicit non-effects: `[required: authorization, execution, scoring, disposition, transfer, graduation, deployment, publication, and external action not created]`
- Validation: `[required: independent checks and results]`
- Next owner: `[required: owner of the authorization decision; not contact authority]`
- Exact next wake: `[required: evidence or authority event that warrants reconsideration]`

## Proposed Execution Handoff

- Proposed trace destination: `[required: exact immutable path, or pending]`
- Proposed score owner: `[required: separately authorized result owner, or pending]`
- Acknowledgment state: `[required: unacknowledged, acknowledged, declined, or unresolved]`
- Authorization pointer: `[required: exact operative authorization, or none]`
- Handoff state: `[required: not_ready, ready_for_authorization_review, or authorized_elsewhere with evidence]`

Neither this request nor acknowledgment authorizes execution. Only an exact,
current, integrated authorization decision can create an operative handoff.

## Frontier Verification

- Verify the plan, candidate, source, fixture, evidence, environment,
  validation, requester, proposed executor, owner, and authority pointers independently.
- Confirm claim, falsifier, failure, bounded pass, unresolved route, stops, and
  prohibited conclusions are copied unchanged from the frozen plan.
- Verify no less consequential treatment supplies the required discrimination.
- Check requested authority, validity, deviations, correction, rollback,
  recovery, standing, data, legitimacy, and new-authorization gates.
- Confirm integration creates no grant, execution, score, disposition,
  transfer, graduation, deployment, publication, or external action.
