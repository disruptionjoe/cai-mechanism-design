---
artifact_type: proving_result_return_template
status: candidate_process_artifact
external_action: none
---

# Proving Result Return Template

## Use Boundary

Use this artifact to return one completed, exactly authorized proving result
from its frozen plan, observed trace, and score to the result owner. It does not
plan, authorize, execute, or score a treatment and does not choose or execute a
candidate disposition. It cannot transfer, graduate, contact, deploy, publish,
or perform external action. A bounded pass does not establish effectiveness,
destination fit, authority, deployment readiness, or external outcome. Do not
invent evidence, observation, owner, authority, acceptance, or result.

## Return Header

| Field | Value |
| --- | --- |
| `return_id` | `[required: stable return identifier]` |
| `proving_id` | `[required: exact proving identifier]` |
| `plan_revision` | `[required: immutable plan revision]` |
| `trace_revision` | `[required: immutable execution-trace revision]` |
| `score_revision` | `[required: immutable score revision]` |
| `candidate_id` | `[required: exact candidate identifier]` |
| `candidate_revision` | `[required: immutable candidate revision]` |
| `source_inquiry` | `[required: exact source-inquiry pointer]` |
| `source_revision` | `[required: immutable source revision]` |
| `result_owner` | `[required: repository-native owner of the proving result]` |
| `prepared_by` | `[required: preparer identity]` |
| `prepared_at` | `[required: ISO-8601 timestamp]` |
| `external_action` | `none` |

## Frozen Result Package

- Plan: `[required: path, revision, and hash]`
- Execution request or authorization: `[required: exact pointer and revision]`
- Fixture or treatment input: `[required: pointer, provenance, revision, and hash]`
- Execution trace: `[required: path, revision, and hash]`
- Score: `[required: path, revision, and hash]`
- Evidence package: `[required: claim-level pointers and revisions]`
- Validation: `[required: commands, validators, revisions, and results]`
- Authority: `[required: exact authority covering the observed treatment and deviations]`
- Prohibited inference: `[required: conclusions outside the frozen result package]`

## Tested Claim And Conditions

- Exact claim: `[required: copied unchanged from the frozen plan]`
- Falsifier: `[required: copied unchanged from the frozen plan]`
- Observable failure: `[required: copied unchanged from the frozen plan]`
- Bounded-pass condition: `[required: copied unchanged from the frozen plan]`
- Unresolved route: `[required: copied unchanged from the frozen plan]`
- Stop conditions: `[required: each planned stop and observed status]`
- Prohibited conclusions: `[required: copied unchanged from the frozen plan]`

## Observed Result

- Result: `[required: exactly one of bounded_pass, revise, kill, defer, or unresolved]`
- Observed facts: `[required: direct evidence-linked observations]`
- Inference: `[required: bounded interpretation separated from observation]`
- Evidence-bound rationale: `[required: one reason tied to the trace and score]`
- Disallowed interpretations: `[required: effectiveness, destination fit, authority, deployment readiness, external outcome, or other unsupported claims]`

## Evidence Grade, Counterevidence, And Failure

- Evidence type and grade: `[required: repository-native classification]`
- Supporting evidence: `[required: claim-level support]`
- Counterevidence: `[required: basis, claim posture, and effect]`
- Absorber or failure: `[required: hidden failure, alternative explanation, or none with basis]`
- Deviations: `[required: each deviation, authority effect, and consequence]`
- Missing evidence: `[required: absent or unreadable required evidence]`
- Provenance gaps: `[required: unresolved gaps and their consequence]`

## Affected-Party, Data, And Legitimacy Return

- Actual standing represented: `[required: affected-party standing present in the trace]`
- Representation limits: `[required: absent or simulated standing and who cannot be spoken for]`
- Risk encountered: `[required: observed or plausible risk within the treatment]`
- Actual data handling: `[required: data class, provenance, transformation, retention, and exposure]`
- Capture concerns: `[required: incentives or structures that may distort the result]`
- Consent or authority gaps: `[required: encountered gaps and their effect]`

## Residual Uncertainty, Correction, And Recovery

- Residual uncertainty: `[required: unresolved claims and consequence]`
- Negative-evidence preservation: `[required: durable adverse evidence and pointers]`
- Correction owner: `[required: owner authorized to correct the relevant truth]`
- Rollback or recovery: `[required: performed or available recovery route]`
- Resulting state: `[required: exact last-known state and revision]`
- Exact next wake: `[required: evidence or owner event that warrants reconsideration]`

## Permitted Disposition Support

- Supported owner disposition: `[required: exactly one of kill, revise, defer, transfer, propose_graduation, or needs_judgment]`
- Support boundary: `[required: what this result supports and why]`
- Exclusions: `[required: decisions, claims, and effects this return does not create]`
- Disposition owner: `[required: repository-native decision authority]`

This field supplies bounded evidence for a later owner decision. It does not
choose or execute the disposition. Graduation still requires destination-owner
acceptance and unresolved-risk disclosure.

## Owner Return

- Receiving owner: `[required: exact result owner]`
- Return pointer: `[required: immutable pointer to this return]`
- Validation pointer: `[required: immutable validation evidence]`
- Explicit non-effects: `[required: state changes and claims not created]`
- Prohibited actions: `[required: contact, transfer, graduation, deployment, publication, or other forbidden effects]`
- Receipt acknowledgment: `[required: unacknowledged, acknowledged, declined, or unresolved with evidence]`

Acknowledgment confirms receipt only. Do not infer result acceptance,
candidate disposition, transfer, or graduation from it.

## Frontier Verification

- Verify the plan, authority, request, candidate, source, fixture, trace,
  score, evidence, validation, and result-owner revisions independently.
- Confirm the observed result matches one allowed value and remains separated
  from the later owner disposition.
- Check evidence grade, counterevidence, failure, deviations, standing, data,
  legitimacy, correction, recovery, residual uncertainty, and negative-evidence
  preservation.
- Confirm no unsupported effectiveness, owner-fit, authority, acceptance,
  transfer, graduation, deployment, publication, or external-action claim
  enters repository truth.
