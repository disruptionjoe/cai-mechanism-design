---
artifact_type: least_consequential_proving_plan_template
status: candidate_process_artifact
external_action: none
---

# Least-Consequential Proving-Plan Template

## Use Boundary

This template prepares a bounded proving plan. It does not authorize execution,
scoring, disposition, transfer, graduation, deployment, or external action.
Select the least-consequential treatment capable of discriminating the named
claim. Synthetic and reversible work may proceed only within an exact grant;
formal, simulation, adversarial, human, field, institutional, incentive, or
other consequential work remains subject to its own authority and safety gates.
No repository has a standing obligation to serve as a proving ground.

## Plan Header

| Field | Value |
| --- | --- |
| `proving_id` | `[required: stable proving identifier]` |
| `candidate_id` | `[required: candidate identifier]` |
| `candidate_revision` | `[required: immutable candidate revision]` |
| `source_inquiry` | `[required: exact source inquiry pointer]` |
| `source_revision` | `[required: immutable source revision]` |
| `treatment_type` | `[required: synthetic, formal, simulation, or adversarial]` |
| `result_owner` | `[required: owner of the proving result]` |
| `requested_by` | `[required: request authority]` |
| `authorization_ref` | `[required: exact authority for preparation or execution]` |
| `external_action` | `none` |

## Candidate Claim Under Test

- Exact claim: `[required: one falsifiable or discriminating claim]`
- Current posture: `[required: hypothesis, candidate, prior result, or other typed posture]`
- What this test cannot establish: `[required: effectiveness, destination fit, authority, deployment readiness, external outcome, or other excluded conclusions]`

## Frozen Evidence And Fixture

- Evidence pointers: `[required: exact source and candidate pointers]`
- Revisions: `[required: immutable revisions]`
- Fixture provenance: `[required: public, licensed, safely shareable, or synthetic provenance]`
- Allowed transformations: `[required: transformations permitted by the plan]`
- Prohibited inference: `[required: facts or conclusions that may not be added]`
- Immutable boundary: `[required: hash or equivalent boundary when available]`

## Treatment And Least-Consequence Rationale

- Primary treatment type: `[required: synthetic, formal, simulation, or adversarial]`
- Least-consequence rationale: `[required: why this treatment is sufficient and a more consequential treatment is unnecessary]`

## Falsifier, Failure, And Pass Conditions

- Discriminating falsifier: `[required: evidence that would count against the claim]`
- Observable failure: `[required: exact failure condition]`
- Bounded pass: `[required: exact pass condition and its narrow meaning]`
- `UNRESOLVED` route: `[required: result and next wake when evidence does not discriminate]`

## Affected-Party Standing And Legitimacy

- Represented standing: `[required: whose standing is present]`
- Representation limits: `[required: whose standing is absent or simulated]`
- Risk bearer: `[required: who bears error or treatment risk]`
- Capture concerns: `[required: incentives or authority that may bias the test]`
- Real-world judgment owner: `[required: owner of any later real-world judgment]`

## Data And Environment Boundary

- Permitted data: `[required: exact allowed data classes]`
- Prohibited data: `[required: confidential, personal, regulated, field, or other excluded data]`
- Environment: `[required: isolated synthetic, formal, simulation, or adversarial environment]`
- Privacy and sensitivity limits: `[required: applicable limits]`
- Retention: `[required: retention or deletion rule]`
- No-contact rule: `[required: prohibition on external contact or participation]`

## Stops, Kill Conditions, Correction, And Recovery

- Immediate stops: `[required: events that halt the treatment]`
- Kill evidence: `[required: evidence that defeats the candidate or treatment]`
- Correction owner: `[required: owner of factual, method, or artifact correction]`
- Rollback or negative-evidence preservation: `[required: exact preservation path]`
- Recovery wake: `[required: evidence or authority needed to resume]`

## Permitted Conclusions

- `bounded_pass`: `[required: narrow representation or mechanism claim supported]`
- `revise`: `[required: correctable defect]`
- `kill`: `[required: defeating evidence]`
- `defer`: `[required: current boundary remains correct]`
- `unresolved`: `[required: evidence did not discriminate]`
- Exclusions: `[required: effectiveness, destination fit, transfer, graduation, deployment, and external outcome remain unproved]`

## Score Return Contract

| Field | Value |
| --- | --- |
| `evidence_observed` | `[required: exact evidence]` |
| `result` | `[required: bounded_pass, revise, kill, defer, or unresolved]` |
| `counterevidence` | `[required: adverse or competing evidence]` |
| `residual_uncertainty` | `[required: remaining uncertainty]` |
| `permitted_disposition` | `[required: narrow disposition allowed]` |
| `owner` | `[required: result and correction owner]` |
| `validation` | `[required: validation evidence]` |
| `next_wake` | `[required: exact wake condition]` |

## Frontier Verification

- Verify source, candidate, fixture, and authorization revisions.
- Verify the treatment is the least consequential discriminating option and
  does not exceed its exact grant.
- Verify falsifier, failure, pass, and unresolved conditions are observable and
  do not smuggle in effectiveness or destination-fit claims.
- Verify affected-party standing, data, stops, correction, recovery, and
  negative-evidence preservation are complete.
- Verify no test execution, scoring, disposition, contact, transfer,
  graduation, deployment, or external action is authorized by the plan.
