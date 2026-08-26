---
artifact_type: proving_authorization_decision_template
status: candidate_process_artifact
external_action: none
---

# Proving Authorization Decision Template

## Use Boundary

Use this artifact to prepare one decision about an exact proving request and
frozen plan. Completing it does not create a real grant, execute or score a
treatment, disposition a candidate, transfer, graduate, deploy, publish, or
perform external action. Do not invent missing evidence, parties, authority,
decisions, conditions, observations, dates, or results.

## Decision Header

| Field | Value |
| --- | --- |
| `authorization_id` | `[required: stable decision identifier]` |
| `proving_id` | `[required: exact proving identifier]` |
| `plan_revision` | `[required: immutable plan revision]` |
| `candidate_id` | `[required: exact candidate identifier]` |
| `candidate_revision` | `[required: immutable candidate revision]` |
| `source_inquiry` | `[required: exact source-inquiry pointer]` |
| `source_revision` | `[required: immutable source revision]` |
| `authority_owner` | `[required: owner of the proving authority]` |
| `authorization_ref` | `[required: exact authority for the resulting decision, or pending]` |
| `decided_by` | `[required: authorized decision-maker, or pending]` |
| `decided_at` | `[required: ISO-8601 timestamp, or pending]` |
| `external_action` | `none` |

## Frozen Request And Plan

- Request: `[required: path, revision, requester, and requested effect]`
- Plan: `[required: path, revision, and hash]`
- Candidate: `[required: path, revision, and hash]`
- Source: `[required: inquiry, revision, provenance, and hash]`
- Fixture: `[required: pointer, revision, provenance, and hash]`
- Evidence: `[required: immutable claim-level pointers]`
- Validation: `[required: checks, versions, and results]`
- Environment: `[required: exact isolated execution environment]`
- Prohibited inference: `[required: conclusions outside the frozen request and plan]`

## Claim, Treatment, And Least-Consequence Check

- Exact claim: `[required: copied unchanged from the frozen plan]`
- Falsifier: `[required: copied unchanged from the frozen plan]`
- Observable failure: `[required: copied unchanged from the frozen plan]`
- Bounded pass: `[required: copied unchanged from the frozen plan]`
- Unresolved route: `[required: copied unchanged from the frozen plan]`
- Exact treatment: `[required: operations, inputs, outputs, and exclusions]`
- Alternatives: `[required: no action and materially different treatments]`
- Discrimination value: `[required: what the treatment could distinguish]`
- Reversibility: `[required: last-known-good state and restoration path]`
- Why no less consequential treatment suffices: `[required: evidence-bound rationale]`

## Authority Scope

- Allowed actor: `[required: exact actor or executor]`
- Allowed operations: `[required: complete operation list]`
- Allowed inputs: `[required: exact data and artifact classes]`
- Allowed outputs: `[required: exact trace and result artifacts]`
- Environment: `[required: isolated boundary and relevant versions]`
- Start and end: `[required: validity interval or exact conditions]`
- Deviations: `[required: prohibited, separately authorized, or exact narrow rule]`
- Correction: `[required: authorized correction route]`
- Rollback and recovery: `[required: exact restoration route]`
- Stop authority: `[required: who may stop and under what conditions]`
- Forbidden effects: `[required: effects outside the grant]`

Authority is exact and deny-wins. A missing, expired, mismatched, or unresolved
field means the treatment is not authorized; it is not permission to infer a
narrower grant.

## Affected Parties, Data, And Legitimacy

- Represented standing: `[required: parties represented and evidence]`
- Representation limits: `[required: absent or simulated standing]`
- Risk bearers: `[required: who bears error or treatment risk]`
- Actual data boundary: `[required: provenance, class, transformation, retention, and exposure]`
- Capture concerns: `[required: incentives or structures that could distort the decision]`
- Consent or authority gaps: `[required: unresolved gaps and authorization effect]`
- Cannot be spoken for: `[required: people or owners this decision does not represent]`

## Stops And Consequence Boundary

- Pre-execution stops: `[required: conditions that prevent start]`
- Live stops: `[required: observable conditions that halt execution]`
- Invalidation conditions: `[required: evidence, authority, or state changes that void the grant]`
- Deviation handling: `[required: halt, narrow, correct, rollback, or new decision rule]`
- Escalation owner: `[required: owner of unresolved authority or safety questions]`
- New-authorization conditions: `[required: every change that requires a fresh decision]`

## Prepared Decision

- Decision: `[required: exactly one of authorize_exact_synthetic, request_revision, defer, reject, or needs_judgment]`
- Rationale: `[required: one evidence-bound reason]`
- Exact authorized effect: `[required: narrow effect, or none unless the decision is authorized and integrated]`
- Explicit non-effects: `[required: effects and conclusions not authorized]`
- Validation: `[required: independent checks and results]`
- Exact next wake: `[required: evidence or authority event that warrants reconsideration]`

Preparation does not create a real grant. Only an authorized, integrated
decision with current authority may make `authorize_exact_synthetic` operative.

## Execution Handoff

- Exact executor: `[required: actor named by the operative grant]`
- Plan and authority pointers: `[required: immutable references]`
- Start-state checks: `[required: authority, fixture, environment, stop, and last-known-good checks]`
- Trace destination: `[required: exact immutable evidence path]`
- Score owner: `[required: separately authorized result owner]`
- Acknowledgment state: `[required: unacknowledged, acknowledged, declined, or unresolved with evidence]`
- Prohibited actions: `[required: actions outside the exact grant]`

Acknowledgment confirms receipt only. It is not execution, acceptance,
candidate disposition, transfer, graduation, or deployment.

## Frontier Verification

- Verify the request, plan, candidate, source, fixture, evidence, environment,
  validation, owner, and authority revisions independently.
- Confirm claim, falsifier, failure, pass, unresolved route, stops, and
  prohibited conclusions are unchanged from the frozen plan.
- Verify no less consequential treatment supplies the required discrimination.
- Check authority status, actor, scope, validity, deviations, correction,
  rollback, recovery, standing, data, legitimacy, and new-authorization gates.
- Confirm preparation creates no grant, execution, disposition, or external action.
