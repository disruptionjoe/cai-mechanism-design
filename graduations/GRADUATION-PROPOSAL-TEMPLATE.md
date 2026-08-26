---
artifact_type: candidate_graduation_proposal_template
status: candidate_process_artifact
external_action: none
---

# Candidate Graduation Proposal Template

## Use Boundary

Use this artifact to prepare a source- and revision-bound graduation proposal.
Completing it does not create destination-owner acceptance, graduate or transfer
a candidate, authorize contact, deploy, publish, or perform external action.
Do not invent missing owners, parties, facts, acceptance, authority, risks,
decisions, dates, or results.

## Proposal Header

| Field | Value |
| --- | --- |
| `proposal_id` | `[required: stable proposal identifier]` |
| `candidate_id` | `[required: exact candidate identifier]` |
| `candidate_revision` | `[required: immutable candidate revision]` |
| `source_inquiry` | `[required: exact source-inquiry pointer]` |
| `source_revision` | `[required: immutable source revision]` |
| `proposing_owner` | `[required: repository-native proposal owner]` |
| `proposed_destination_owner` | `[required: exact proposed owner; not acceptance by itself]` |
| `authorization_ref` | `[required: authority for preparing this proposal]` |
| `prepared_by` | `[required: preparer identity]` |
| `prepared_at` | `[required: ISO-8601 timestamp]` |
| `external_action` | `none` |

## Frozen Graduation Package

- Candidate: `[required: path, revision, and hash]`
- Source inquiry: `[required: path, revision, provenance, and hash]`
- Current disposition: `[required: exact decision and revision]`
- Alternative map: `[required: exact revision, or none with reason]`
- Proving returns: `[required: exact revisions, or none with reason]`
- Negative evidence: `[required: durable adverse evidence and pointers]`
- Validation: `[required: checks, revisions, and results]`
- Prohibited inference: `[required: claims this package cannot support]`

## Earned Graduation Case

- Theory of change: `[required: bounded causal account]`
- Bounded evidence: `[required: claim-level evidence and posture]`
- Counterevidence: `[required: basis, claim posture, and effect]`
- Residual uncertainty: `[required: unresolved claims and consequence]`
- Nonduplication: `[required: exact comparison with owner-native work]`
- Alternatives: `[required: continued incubation, no action, revision, defer, kill, and transfer review]`
- Graduation rationale: `[required: why graduation review is stronger than the supported alternatives without fabricated parity]`

## Destination-Owner Fit And Acceptance

- Native authority: `[required: exact destination purpose and authority pointers]`
- Better-existing-owner result: `[required: found, not_found, or unresolved]`
- Exact scope proposed: `[required: artifacts, responsibilities, and exclusions]`
- Acceptance state: `[required: not_requested, pending, accepted, rejected, withdrawn, or unresolved]`
- Acceptance evidence: `[required: immutable destination-owner evidence, or none]`
- Missing evidence: `[required: gaps blocking an acceptance conclusion]`
- What remains with Mechanism Design: `[required: incubator-owned evidence, correction, or disposition work]`

Interest, expertise, relationship, or willingness to review does not establish
fit or acceptance. `accepted` requires destination-owner-native evidence for
the exact accepted scope; this proposal cannot create that value.

## Affected Parties And Legitimacy

- Parties with standing: `[required: parties and basis for standing]`
- Risk bearers: `[required: who bears transfer, delay, or intervention risk]`
- Representation limits: `[required: absent or simulated standing]`
- Capture risks: `[required: incentives or authority that could distort the proposal]`
- Consent or authority gaps: `[required: unresolved gaps and consequence]`
- Cannot be spoken for: `[required: people or owners this proposal does not represent]`

## Unresolved Risks And Negative Evidence

- Durable adverse evidence: `[required: immutable pointers and relevance]`
- Risk allocation: `[required: current and proposed bearer for each material risk]`
- Disclosure pointer: `[required: complete unresolved-risk disclosure]`
- Supersession status: `[required: active, superseded, or unresolved with evidence]`
- Acceptance-required risks: `[required: risks the destination owner must explicitly accept before graduation, or none with basis]`
- Retained risks: `[required: risks that cannot be transferred by acceptance]`

## Stops, Correction, Recovery, And Revocation

- Stop conditions: `[required: evidence or authority events that halt preparation]`
- Revocation conditions: `[required: events that invalidate a prepared or accepted route]`
- Correction owner: `[required: owner authorized to correct each relevant truth]`
- Rollback or recovery: `[required: route to the last known valid state]`
- Return boundary: `[required: when work returns to Mechanism Design or another owner]`
- Prohibited action: `[required: contact, sending, transfer, deployment, publication, or other forbidden effects]`

## Prepared Proposal

- State: `[required: exactly one of ready_for_owner_review, request_revision, defer, reject, or needs_judgment]`
- Rationale: `[required: one evidence-bound reason]`
- Proposed owner effect: `[required: narrow owner decision this artifact prepares]`
- Explicit non-effects: `[required: acceptance, graduation, transfer, deployment, publication, and other effects not created]`
- Validation: `[required: independent checks and results]`
- Next owner: `[required: owner of the next decision; not contact authority]`
- Exact next wake: `[required: evidence or owner event that warrants reconsideration]`

## Frontier Verification

- Verify every source, candidate, disposition, alternative, proving, evidence,
  validation, owner, authority, acceptance, and risk pointer independently.
- Re-run nonduplication and better-existing-owner checks against native owner truth.
- Confirm any `accepted` state is destination-owner evidence rather than
  interest, synthetic review, relationship, or this proposal's assertion.
- Check standing, capture, consent, stops, correction, recovery, revocation,
  risk disclosure, and retained-risk boundaries.
- Confirm the prepared state creates no contact, acceptance, graduation,
  transfer, deployment, publication, or external action.
