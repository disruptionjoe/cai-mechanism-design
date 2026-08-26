---
artifact_type: least_consequential_proving_score_template
status: candidate_process_artifact
external_action: none
---

# Least-Consequential Proving-Score Template

## Use Boundary

Use this artifact only to score an executed, exactly authorized proving trace
against its frozen plan. A plan or template does not authorize execution or
scoring. A completed score does not itself disposition, transfer, graduate,
deploy, contact, publish, or act. Human, field, institutional, incentive,
consequential, account, publication, and deployment effects remain separately
gated. A bounded pass does not establish effectiveness, destination fit,
authority, deployment readiness, or external outcome.

## Score Header

| Field | Value |
| --- | --- |
| `proving_id` | `[required: unique proving identifier]` |
| `plan_revision` | `[required: immutable plan revision]` |
| `candidate_id` | `[required: candidate identifier]` |
| `candidate_revision` | `[required: immutable candidate revision]` |
| `source_inquiry` | `[required: exact inquiry pointer]` |
| `source_revision` | `[required: immutable source revision]` |
| `treatment_type` | `[required: synthetic, formal, simulation, adversarial, or other exact plan value]` |
| `result_owner` | `[required: owner of this proving result]` |
| `execution_authority_ref` | `[required: exact authority that covered the observed trace]` |
| `scored_by` | `[required: scorer identity]` |
| `scored_at` | `[required: timestamp]` |
| `external_action` | `none` |

## Frozen Plan And Evidence

- Plan: `[required: exact path and revision]`
- Request: `[required: exact path and revision]`
- Response or execution trace: `[required: exact path and revision]`
- Evidence: `[required: exact claim-level pointers and revisions]`
- Fixture or treatment input: `[required: exact pointer and revision]`
- Validation: `[required: commands, fixtures, validators, and revisions]`
- Prohibited inference: `[required: conclusions outside the frozen plan and evidence]`

## Claim And Decision Conditions

- Exact claim: `[required: copy unchanged from the frozen plan]`
- Falsifier: `[required: copy unchanged from the frozen plan]`
- Observable failure: `[required: copy unchanged from the frozen plan]`
- Bounded pass: `[required: copy unchanged from the frozen plan]`
- Unresolved route: `[required: copy unchanged from the frozen plan]`
- Prohibited conclusions: `[required: copy unchanged from the frozen plan]`

## Observed Trace

- Facts observed: `[required: observations, separated from inference]`
- Transformations performed: `[required: exact operations and versions]`
- Stop events: `[required: triggered, not_triggered, or unknown for each stop]`
- Missing evidence: `[required: absent or unreadable required evidence]`
- Deviations from plan: `[required: deviation, authority effect, and consequence]`

## Evidence Grade And Counterevidence

- Evidence type and grade: `[required: repository-native evidence classification]`
- Supporting evidence: `[required: claim-level support]`
- Counterevidence: `[required: basis, claim posture, and effect]`
- Absorber or failure: `[required: alternative explanation, hidden failure, or none with basis]`
- Discrimination: `[required: what the result distinguishes and what it does not]`

## Affected-Party, Data, And Legitimacy Check

- Actual standing: `[required: whose standing was represented in the trace]`
- Representation limits: `[required: who was not represented or cannot be spoken for]`
- Risk encountered: `[required: observed or plausible risk within the plan]`
- Data boundary: `[required: actual data class, provenance, retention, and exposure]`
- Capture concerns: `[required: incentives or structures that could distort the result]`
- Authority or consent gap: `[required: encountered gap and its effect on scoring]`

## Result

- Result: `[required: exactly one of bounded_pass, revise, kill, defer, unresolved]`
- Rationale: `[required: one evidence-bound reason]`
- Disallowed interpretations: `[required: claims the result does not support]`

## Residual Uncertainty, Correction, And Recovery

- Residual uncertainty: `[required: unresolved claim and consequence]`
- Negative-evidence preservation: `[required: durable evidence and return pointer]`
- Correction owner: `[required: owner authorized to correct the relevant truth]`
- Rollback or recovery: `[required: executed or available recovery route]`
- Exact next wake: `[required: evidence or owner event that warrants reconsideration]`

## Permitted Disposition Return

- Supported owner disposition: `[required: exactly one of kill, revise, defer, transfer, propose_graduation, or needs_judgment]`
- Support boundary: `[required: how the score supports that narrow return]`
- Exclusions: no score automatically transfers, graduates, deploys, contacts,
  publishes, or performs external action.
- Return owner: `[required: repository-native disposition authority]`

## Frontier Verification

- Verify the plan, candidate, source, request, trace, fixture, evidence, and
  validation revisions independently.
- Confirm execution authority covered the actual treatment and every deviation;
  otherwise narrow or stop the score.
- Compare the observed trace to the frozen claim, falsifier, failure, pass,
  unresolved, stop, and prohibited-conclusion conditions without rewriting them.
- Check evidence grade, counterevidence quality, discrimination, affected-party
  standing, data boundary, legitimacy, correction, and recovery.
- Confirm the result and later owner disposition are separate allowed values
  and that neither is inferred from artifact cleanliness alone.
- Confirm no unsupported effectiveness, owner-fit, authority, transfer,
  graduation, deployment, or external-action claim enters repository truth.
