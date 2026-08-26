---
artifact_type: candidate_disposition_decision_template
status: candidate_process_artifact
external_action: none
---

# Candidate Disposition Decision Template

## Use Boundary

Use this artifact to prepare one source- and revision-bound candidate
disposition for the repository's decision authority. Completing the template
does not itself kill, revise, defer, transfer, graduate, contact, deploy, or
otherwise act on a candidate. The real disposition requires its exact owner
authority and normal repository integration. Transfer requires receiving-owner
acceptance, while graduation requires destination-owner acceptance and
unresolved-risk disclosure. Do not invent a source, owner, affected party,
fact, authority, decision, acceptance, date, or result to fill a gap.

## Decision Header

| Field | Value |
| --- | --- |
| `decision_id` | `[required: stable disposition identifier]` |
| `candidate_id` | `[required: exact candidate identifier]` |
| `candidate_revision` | `[required: immutable candidate revision]` |
| `source_inquiry` | `[required: exact source-inquiry pointer]` |
| `source_revision` | `[required: immutable source revision]` |
| `decision_owner` | `[required: repository-native disposition authority]` |
| `authorization_ref` | `[required: exact authority for making this disposition]` |
| `decided_by` | `[required: authorized decision-maker, or pending]` |
| `decided_at` | `[required: ISO-8601 timestamp, or pending]` |
| `external_action` | `none` |

## Frozen Candidate And Evidence

- Candidate: `[required: path, revision, and hash]`
- Source inquiry: `[required: path, revision, provenance, and hash]`
- Alternative map: `[required: exact map revision, or none with reason]`
- Proving plans: `[required: exact plan revisions, or none with reason]`
- Execution traces: `[required: exact trace revisions, or none with reason]`
- Scores and result returns: `[required: exact revisions, or none with reason]`
- Validation: `[required: validators, commands, revisions, and results]`
- Current disposition: `[required: exact current state and revision]`
- Prohibited inference: `[required: conclusions the frozen package cannot support]`

## Available Dispositions

Choose exactly one only after the later owner decision gate. None is automatic.

- `kill`: close the candidate as an active path while preserving its adverse
  evidence, reasons, and recovery pointers.
- `revise`: return the candidate to one named correction gate with an exact
  deficiency, owner, and acceptance condition.
- `defer`: preserve the current state without stronger conclusion until an
  exact evidence or owner wake occurs.
- `transfer`: move accepted responsibility only after a rightful receiving
  owner accepts the exact scope, return boundary, and unresolved risks.
- `propose_graduation`: prepare a graduation proposal for destination-owner
  acceptance; it is not graduation or transfer.

## Decision Basis

- Theory-of-change status: `[required: supported, contradicted, incomplete, or unresolved with basis]`
- Alternatives including no action: `[required: exact map pointers and remaining options]`
- Supporting evidence: `[required: claim-level evidence and posture]`
- Counterevidence: `[required: basis, claim posture, and effect]`
- Residual uncertainty: `[required: unresolved claims and consequence]`
- Existing-owner fit: `[required: native-authority and better-existing-owner result]`
- Nonduplication: `[required: compared artifacts, mechanisms, and owner-native remedies]`
- Permitted conclusions: `[required: narrow conclusions supported by the frozen evidence]`
- Prohibited conclusions: `[required: effectiveness, authority, fit, deployment, or other unsupported claims]`

## Negative Evidence And Reasons

Repeat the record for each material adverse result or rejected path.

### Negative-Evidence Record `[repeat as needed]`

- Evidence pointer: `[required: immutable pointer]`
- Failed, contradicted, or absorbed path: `[required: exact path]`
- Reason and consequence: `[required: evidence-bound explanation]`
- Supersession status: `[required: current, narrowed, or superseded with pointer]`
- Preservation pointer: `[required: durable repository location]`

## Owner Fit, Transfer, And Graduation Boundary

- Native authority considered: `[required: exact owner-purpose and authority pointers]`
- Better-existing-owner result: `[required: found, not_found, or unresolved with basis]`
- Receiving or destination owner: `[required: proposed owner, or none]`
- Acceptance state: `[required: absent, requested, received, declined, or unresolved with evidence]`
- Accepted scope: `[required: exact accepted responsibility, or none]`
- What remains with Mechanism Design: `[required: incubator-owned evidence, analysis, or disposition duty]`
- Unresolved risks: `[required: risks disclosed to any receiving owner]`
- Missing evidence: `[required: evidence still needed before transfer or graduation]`

Interest, expertise, relationship, or willingness to review does not establish
owner fit. Preparing this section does not authorize contact or sending.

## Affected Parties And Legitimacy

- Parties with standing: `[required: affected parties and basis for standing]`
- Risk bearers: `[required: who bears error, delay, transfer, or intervention risk]`
- Representation limits: `[required: absent or simulated standing]`
- Capture risks: `[required: incentives or structures that may distort the decision]`
- Consent or authority gaps: `[required: unresolved gaps and consequence]`
- Cannot be spoken for: `[required: people or owners this decision does not represent]`

## Stops, Correction, Recovery, And Reopen

- Stop conditions: `[required: conditions that halt preparation or invalidate the decision basis]`
- Kill conditions: `[required: evidence that defeats continued incubation]`
- Correction owner: `[required: owner authorized to correct the relevant truth]`
- Rollback or recovery: `[required: route if integration or later handling fails]`
- Exact reopen condition: `[required: evidence or owner event that warrants reconsideration]`
- Prohibited action: `[required: contact, research, testing, transfer, graduation, deployment, or other forbidden effects]`

## Prepared Decision

- Prepared disposition: `[required: exactly one of kill, revise, defer, transfer, or propose_graduation]`
- Evidence-bound rationale: `[required: one bounded reason tied to the frozen package]`
- Proposed owner effect: `[required: exact state and artifact changes, or none]`
- Explicit non-effects: `[required: decisions, claims, and actions not created]`
- Next owner: `[required: decision, correction, receiving, destination, or evidence owner]`
- Validation: `[required: exact checks required before owner integration]`
- Exact next wake: `[required: evidence or owner event, not a generic date]`

This is a prepared decision, not an executed disposition. The repository's
authorized owner must independently verify and integrate any real disposition.

## Frontier Verification

- Verify every candidate, source, evidence, validation, owner, authority, and
  current-disposition revision independently.
- Confirm alternatives include no action and negative evidence remains durable.
- Re-run nonduplication, native-authority, better-existing-owner, affected-party,
  legitimacy, stop, correction, recovery, and reopen checks.
- Confirm the prepared disposition uses one allowed value and that transfer or
  graduation still depends on exact receiving-owner acceptance.
- Confirm no contact, research, testing, transfer, graduation, deployment,
  publication, or external action is invented or authorized.
