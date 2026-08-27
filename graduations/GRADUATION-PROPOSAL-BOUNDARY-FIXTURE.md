---
artifact_type: synthetic_graduation_proposal_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Graduation Proposal Boundary Fixture

## Use Boundary

This fixture tests whether a prepared graduation proposal preserves missing
owner fit, acceptance, authority, proving returns, and alternative-map evidence.
It cannot create destination-owner fit, acceptance, contact, graduation,
transfer, publication, deployment, or external action.

## Proposal Header

| Field | Value |
| --- | --- |
| `proposal_id` | `SYNTH-GRAD-PROP-BOUNDARY-001@r1` |
| `candidate_id` | `SYNTH-CANDIDATE-GRAD-001@r1` |
| `source_inquiry` | `SYNTH-SOURCE-GRAD-001@r1` |
| `current_disposition` | `defer@r1` |
| `proposing_owner` | `synthetic-source-owner` |
| `proposed_destination_owner` | `synthetic-destination-owner` |
| `authorization_ref` | `synthetic-preparation-authority@r1` |
| `prepared_by` | `synthetic-proposal-preparer` |
| `prepared_at` | `2026-08-26T00:00:00Z` |
| `external_action` | `none` |

## Frozen Graduation Package

- Candidate: `synthetic://candidate/SYNTH-CANDIDATE-GRAD-001@r1`.
- Source inquiry: `synthetic://source/SYNTH-SOURCE-GRAD-001@r1`.
- Current disposition: `defer@r1`.
- Alternative map: none exists; no revision is inferred.
- Proving returns: none exist; no result is inferred.
- Bounded theory: a synthetic correction card could preserve one public label
  and its correction owner during a future handoff.
- Supported alternatives: continued incubation, no action, revision, defer,
  kill, and later transfer review.
- Prohibited inference: the frozen package supplies no destination-native work,
  better-owner fit, acceptance, authority, graduation, or transfer evidence.

## Earned Graduation Case

Graduation is not earned. The alternative map and proving returns are absent,
and there is no evidence that `synthetic-destination-owner` has matching native
work, better-owner fit, acceptance, or authority. Current `defer@r1` remains
stronger than a graduation claim.

## Destination-Owner Fit And Acceptance

- Native authority: not supplied.
- Better-existing-owner result: unresolved.
- Exact proposed scope: one synthetic correction card; this is proposed scope,
  not accepted scope.
- Acceptance state: `not_requested`.
- Acceptance evidence: `none`.
- Missing evidence: destination-owner-native fit, exact acceptance, and
  separate authority.
- Retained responsibility: custody, correction, and risk remain with
  `synthetic-source-owner`.

The proposed destination is a pointer to a possible next decision owner. It is
not evidence of fit, acceptance, contact authority, or transfer authority.

## Affected Parties And Legitimacy

- Represented standing: one synthetic reviewer role.
- Representation limits: no real person or institution is represented.
- Risk and responsibility bearer: `synthetic-source-owner` retains the supplied
  custody, correction, and risk boundary.
- Data boundary: one public synthetic label retained only in this fixture.
- Cannot be spoken for: any real person, institution, source owner, or
  destination owner.

## Unresolved Risks And Negative Evidence

- Unresolved risk: loss of correction context if custody changes.
- Negative evidence: no alternative-map revision, proving return, destination-
  native work, better-owner fit, acceptance evidence, or transfer authority.
- Risk allocation: all supplied responsibility, custody, correction, and risk
  remain with `synthetic-source-owner`.
- Acceptance-required risk: any future custody change would require explicit
  destination-owner acceptance plus separate authority.
- Retained risk: this proposal cannot transfer the correction-context risk.

## Stops, Correction, Recovery, And Revocation

- Stop before contact, an acceptance claim, transfer, or graduation.
- Stop if the candidate, source, disposition, proposed owner, scope, custody,
  authority, standing, or risk boundary changes.
- Correction owner: `synthetic-source-owner`.
- Recovery: return to the frozen candidate and source pointers, current
  `defer@r1`, and unchanged source-owner custody.
- Revocation: any change named above invalidates this prepared fixture and
  requires a fresh evidence-bound proposal.
- Prohibited action: contact, sending, acceptance, transfer, graduation,
  publication, deployment, or external action.

## Prepared Proposal

- State: `defer`.
- Rationale: owner fit, acceptance, alternatives, proving returns, and
  authority are not established.
- Proposed owner effect: none; this fixture prepares no operative decision.
- Explicit non-effects: no contact, acceptance, graduation, transfer,
  publication, deployment, custody change, risk transfer, or external action.
- Next owner: `synthetic-destination-owner`; this pointer creates no contact or
  decision authority.
- Exact next wake: destination-owner-native fit and acceptance evidence plus
  separate authority.

## Frontier Verification

- Confirm the proposal, candidate, source, and disposition identifiers match
  the frozen fixture.
- Confirm the alternative map and proving returns remain absent.
- Confirm destination-native work, better-owner fit, acceptance evidence, and
  transfer authority remain absent.
- Confirm represented standing is limited to one synthetic reviewer role.
- Confirm custody, correction, responsibility, and risk remain with
  `synthetic-source-owner`.
- Confirm `defer` creates no contact, acceptance, graduation, transfer,
  publication, deployment, or external action.
