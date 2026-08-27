---
artifact_type: synthetic_destination_owner_review_request_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Destination-Owner Review Request Boundary Fixture

## Use Boundary

This fixture prepares one bounded, unsent synthetic-review request from frozen
synthetic evidence. It creates no destination-owner fit, acceptance, contact,
sending, transfer, graduation, deployment, publication, candidate disposition,
or external action. Responsibility, custody, correction, and risk remain with
`synthetic-source-owner`.

## Request Header

| Field | Value |
| --- | --- |
| `request_id` | `SYNTH-DEST-REVIEW-REQ-001@r1` |
| `candidate_id` | `SYNTH-CANDIDATE-GRAD-001@r1` |
| `source_inquiry` | `SYNTH-SOURCE-GRAD-001@r1` |
| `requesting_owner` | `synthetic-source-owner` |
| `proposed_destination_owner` | `synthetic-destination-owner` |
| `preparation_authority` | `synthetic-review-request-preparation@r1` |
| `preparer` | `synthetic-review-request-preparer` |
| `prepared_at` | `2026-08-27T00:00:00Z` |
| `external_action` | `none` |

## Exact Synthetic Review Question

Can the proposed destination identify exact native authority and existing work
relevant to one synthetic correction card? The only requested answer is one
permitted review response plus immutable native-authority and work pointers, or
an explicit statement that none is available. Authority, acceptance, transfer,
deployment, real-world use, and candidate disposition are excluded questions.

## Candidate Slice

The bounded theory is that preserving one public label together with its
correction owner could keep correction context visible during a possible future
handoff. Only the synthetic correction card is in scope. Current disposition is
`defer@r1`. Exact source and candidate pointers are
`synthetic://source/SYNTH-SOURCE-GRAD-001@r1` and
`synthetic://candidate/SYNTH-CANDIDATE-GRAD-001@r1`. No authority, transfer,
graduation, deployment, real-world use, or disposition change is in scope.

## Owner-Fit Check

Destination-native authority and work evidence are `not_supplied`.
Better-existing-owner result is `unresolved`. A proposed destination pointer is
not evidence of fit. Responsibility, custody, correction, risk, analysis, and
the current defer remain with `synthetic-source-owner` unless a separately
authorized owner process establishes otherwise.

## Evidence Packet

- Source pointer: `synthetic://source/SYNTH-SOURCE-GRAD-001@r1`.
- Candidate pointer: `synthetic://candidate/SYNTH-CANDIDATE-GRAD-001@r1`.
- Claim posture: one synthetic correction-card candidate at `defer@r1`.
- Destination evidence: `not_supplied`.
- Better-existing-owner result: `unresolved`.
- Alternative-map revision: `none`.
- Proving return: `none`.
- Review response: `none_received`.
- Prohibited inference: the packet cannot establish fit, acceptance, transfer,
  graduation, authority, contact, sending, deployment, or external action.

## Alternatives And No Action

- No action: preserve the frozen evidence and current defer.
- Retain or defer: keep responsibility and correction with
  `synthetic-source-owner`.
- Revise: correct the packet if source, candidate, custody, standing, or risk
  evidence changes.
- Later transfer review: reconsider only after immutable destination-native
  authority and work evidence exists.
- Kill: remains an available later owner disposition; this request supplies no
  kill decision.

## Affected Parties And Legitimacy

One synthetic reviewer role represents standing. No real person, institution,
source owner, or destination owner is represented or can be spoken for. The
named risk is loss of correction context if custody changes. No consent,
destination-native authority, acceptance, or real affected-party evidence is
supplied, so the request must remain synthetic and unsent.

## Stops, Correction, And Recovery

Stop before contact or sending and on any source, candidate, disposition,
owner, authority, standing, custody, or risk change. Correction owner and
return route are `synthetic-source-owner`. Recovery is to preserve the frozen
evidence and `defer`. Contact, sending, transfer, graduation, deployment,
publication, and all other external action are prohibited.

## Permitted Review Response

The review may return exactly one of:

- `accept_for_synthetic_review`
- `request_revision`
- `decline_owner_fit`
- `defer`
- `needs_judgment`

No response has been received. None of these values creates owner fit,
acceptance, transfer, graduation, permission to contact, or authority to act.

## Prepared Unsent Request

State is `defer`. The next review pointer is
`synthetic-destination-owner`, but it is not a fit, acceptance, contact, or
sending authority. The request remains unsent. Exact effects are `none`; no
sending or external-action authority exists.

## Frontier Verification

- Confirm all identifiers and pointers match the frozen synthetic evidence.
- Confirm destination-native authority remains `not_supplied` and owner fit
  remains `unresolved`.
- Confirm the response set contains only the five template tokens.
- Confirm one synthetic reviewer role is represented and no real party or
  owner is represented.
- Confirm stops, correction, recovery, current defer, and source custody remain
  intact.
- Confirm the fixture creates no contact, sending, fit, acceptance, transfer,
  graduation, deployment, publication, disposition, or external action.
