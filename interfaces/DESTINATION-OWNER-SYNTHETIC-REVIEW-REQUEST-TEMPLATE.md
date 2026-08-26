---
artifact_type: destination_owner_review_request_template
status: candidate_process_artifact
external_action: none
---

# Destination-Owner Synthetic-Review Request Template

## Use Boundary

This template prepares a bounded request for synthetic review. It cannot create
owner acceptance, contact, authority, transfer, graduation, or action. Preparing
the request is not authorization to send it. Existing-owner fit defeats
admission to Mechanism Design, and interest or expertise alone does not prove
destination-owner fit.

## Request Header

| Field | Value |
| --- | --- |
| `request_id` | `[required: stable request identifier]` |
| `candidate_id` | `[required: candidate identifier]` |
| `requesting_owner` | `[required: owner preparing the request]` |
| `proposed_destination_owner` | `[required: proposed owner; not yet accepted]` |
| `source_inquiry` | `[required: exact source inquiry pointer]` |
| `source_revision` | `[required: immutable source revision]` |
| `candidate_revision` | `[required: immutable candidate revision]` |
| `requested_review_type` | `[required: bounded synthetic review type]` |
| `external_action` | `none` |
| `requested_by` | `[required: request authority]` |
| `requested_at` | `[required: ISO-8601 timestamp]` |

## Exact Synthetic Review Question

- Bounded question: `[required: one answerable synthetic-review question]`
- Excluded questions: `[required: authority, transfer, deployment, real-world, or other excluded questions]`
- Exact answer requested: `[required: the evidence and response form the review may return]`

## Candidate Slice

- Theory of change: `[required: bounded theory and causal link]`
- Candidate elements in scope: `[required: exact elements]`
- Candidate elements out of scope: `[required: exact exclusions]`
- Current disposition: `[required: kill, revise, defer, transfer review, or propose-graduation posture]`

## Owner-Fit Check

- Proposed destination's native authority: `[required: exact authority and native purpose]`
- Better-existing-owner test: `[required: evidence for or against a better current owner]`
- What remains with Mechanism Design: `[required: incubator-owned analysis or disposition]`
- Evidence still missing: `[required: gaps that prevent an owner-fit conclusion]`

Do not infer fit from interest, expertise, relationship, or willingness to read.

## Evidence Packet

- Exact source pointers: `[required: paths or durable references]`
- Revisions: `[required: immutable revisions or hashes]`
- Claim posture: `[required: hypothesis, candidate, bounded pass, negative result, or other typed posture]`
- Counterevidence: `[required: relevant competing evidence]`
- Unresolved uncertainty: `[required: material unknowns]`
- Prohibited inference: `[required: conclusions the packet cannot support]`

## Alternatives And No Action

- No action: `[required: consequences and rationale]`
- Retain or defer: `[required: consequences and rationale]`
- Revise: `[required: consequences and rationale]`
- Transfer review: `[required: consequences and unmet gates]`
- Kill: `[required: applicable kill evidence]`

The alternatives need not receive equal weight, but none may be omitted merely
to force a preferred outcome.

## Affected Parties And Legitimacy

- Named standing: `[required: whose standing is represented]`
- Who bears risk: `[required: affected or burden-bearing parties]`
- Representation limits: `[required: limits of the available evidence]`
- Capture risk: `[required: incentives or authority that may distort review]`
- Who cannot be spoken for: `[required: absent or unrepresented parties]`

## Stops, Correction, And Recovery

- Stop conditions: `[required: immediate stop triggers]`
- Correction owner: `[required: owner of factual or framing correction]`
- Return route: `[required: exact destination for the review result]`
- Recovery if review fails: `[required: preserve evidence, defer, narrow, or reroute]`
- Prohibited external acts: `[required: contact, sending, publication, deployment, or other forbidden effects]`

## Permitted Review Response

The review may return exactly one of:

- `accept_for_synthetic_review`
- `request_revision`
- `decline_owner_fit`
- `defer`
- `needs_judgment`

None is transfer, graduation acceptance, permission to contact, or authority to
act. Graduation still requires destination-owner acceptance and unresolved-risk
disclosure through the repository's ordinary governance.

## Frontier Verification

- Verify exact source and candidate revisions and the bounded question.
- Verify the proposed destination's native authority rather than inferred fit.
- Verify alternatives, affected-party standing, representation limits, stops,
  correction, and recovery are usable.
- Verify no real owner, source, date, result, contact, acceptance, transfer,
  graduation, deployment, or external action was invented or authorized.
- Verify the response set and return route preserve Mechanism Design and
  destination-owner authority.
