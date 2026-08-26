---
artifact_type: proving_execution_trace_template
status: candidate_process_artifact
external_action: none
---

# Proving Execution Trace Template

## Use Boundary

Use this artifact only to record one exactly authorized proving execution
against its frozen plan. It does not prepare or authorize a plan, extend
authority, score evidence, disposition a candidate, transfer, graduate,
deploy, contact, publish, or perform external action. Record observations
separately from inference. A clean trace does not establish effectiveness,
destination fit, authority, deployment readiness, or external outcome.

## Trace Header

| Field | Value |
| --- | --- |
| `trace_id` | `[required: unique trace identifier]` |
| `proving_id` | `[required: exact proving-plan identifier]` |
| `plan_revision` | `[required: immutable plan revision]` |
| `candidate_id` | `[required: candidate identifier]` |
| `candidate_revision` | `[required: immutable candidate revision]` |
| `source_inquiry` | `[required: exact source-inquiry pointer]` |
| `source_revision` | `[required: immutable source revision]` |
| `treatment_type` | `[required: exact treatment type from the plan]` |
| `result_owner` | `[required: owner of the proving result]` |
| `execution_authority_ref` | `[required: exact authority for this execution]` |
| `executed_by` | `[required: operator identity]` |
| `started_at` | `[required: ISO-8601 timestamp]` |
| `completed_at` | `[required: ISO-8601 timestamp or in_progress]` |
| `external_action` | `none` |

## Frozen Start Conditions

- Exact plan: `[required: path, revision, and hash]`
- Exact request: `[required: path, revision, and hash]`
- Exact fixture: `[required: path, revision, provenance, and hash]`
- Evidence set: `[required: immutable claim-level pointers]`
- Validation state: `[required: pre-execution checks and results]`
- Environment: `[required: isolated environment and relevant versions]`
- Last-known-good state: `[required: state and recovery pointer]`
- Prohibited inference: `[required: conclusions outside the frozen boundary]`
- Pre-execution authority check: `[required: authority scope, status, and verifier]`

## Treatment Boundary

- Intended operations: `[required: exact allowed transformations]`
- Least-consequence rationale: `[required: why this is the least consequential discriminating treatment]`
- Allowed inputs: `[required: exact data and artifact classes]`
- Allowed outputs: `[required: exact trace and result artifacts]`
- Affected-party boundary: `[required: represented standing and exclusions]`
- Data boundary: `[required: provenance, privacy, retention, and exposure limits]`
- Forbidden operations: `[required: actions outside authority or treatment scope]`

## Chronological Observed Trace

Repeat the block for every material event. Preserve raw observation separately
from any interpretation that belongs in later scoring.

### Event `[repeat as needed]`

- Timestamp: `[required: ISO-8601 timestamp]`
- Observation: `[required: directly observed fact]`
- Transformation: `[required: exact operation, or none]`
- Artifact or state revision: `[required: resulting revision or unchanged state]`
- Operator: `[required: actor or system component]`
- Evidence pointer: `[required: immutable pointer]`

## Stop And Deviation Log

Repeat the block for every planned stop condition and every deviation.

### Stop Or Deviation `[repeat as needed]`

- Condition or deviation: `[required: exact plan condition or observed variance]`
- Status: `[required: not_triggered, triggered, unknown, or deviation]`
- Missing evidence: `[required: missing or unreadable evidence, or none]`
- Authority effect: `[required: none, narrowed, invalidated, or unresolved]`
- Action taken: `[required: continue, narrow, correct, rollback, halt, or other exact response]`
- Execution halted: `[required: yes or no]`
- Evidence pointer: `[required: immutable pointer]`

## Evidence Integrity And Counterevidence

- Hashes or revisions: `[required: request, plan, fixture, trace, and artifact integrity values]`
- Validation results: `[required: commands or checks and results]`
- Counterevidence encountered: `[required: adverse or competing evidence and claim posture]`
- Absorber or failure: `[required: hidden failure, alternative explanation, or none with basis]`
- Unresolved provenance: `[required: gaps and their consequence]`

## Affected-Party, Data, And Legitimacy Trace

- Actual standing represented: `[required: affected-party standing present in the execution]`
- Representation limits: `[required: absent or simulated standing and who cannot be spoken for]`
- Risks encountered: `[required: observed or plausible treatment risks]`
- Actual data handling: `[required: data class, provenance, transformation, retention, and exposure]`
- Capture concerns: `[required: incentives or structures that may distort the trace]`
- Consent or authority gaps: `[required: encountered gaps and their execution effect]`

## Correction, Rollback, And Recovery

- Corrections applied: `[required: exact corrections and authority, or none]`
- Negative-evidence preservation: `[required: failures, deviations, and durable pointers]`
- Rollback or recovery performed: `[required: action and result, or none]`
- Rollback or recovery available: `[required: exact remaining route]`
- Recovery owner: `[required: owner authorized to restore the state]`
- Resulting state: `[required: exact last-known state and revision]`

## Score Return Package

- Exact trace and artifact revisions: `[required: immutable pointers]`
- Validation pointer: `[required: exact validation evidence]`
- Deviations: `[required: complete deviation pointers, or none]`
- Missing evidence: `[required: unresolved gaps, or none]`
- Unresolved uncertainty: `[required: claims the trace cannot settle]`
- Explicit prohibited conclusions: `[required: claims the later score must not make]`

This package returns evidence to a separately authorized scorer. It does not
score the trace or choose a candidate disposition.

## Frontier Verification

- Verify the plan, request, candidate, source, fixture, evidence, environment,
  and execution-authority revisions independently.
- Confirm every observed event is evidence-linked and separated from inference.
- Check every stop condition, deviation, missing-evidence item, authority
  effect, correction, rollback, and resulting state.
- Verify affected-party standing, representation limits, data handling,
  legitimacy, counterevidence, and provenance boundaries.
- Confirm the score-return package is complete but contains no score or owner
  disposition.
- Confirm no contact, transfer, graduation, deployment, publication, or other
  external action is invented or authorized.
