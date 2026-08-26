---
artifact_type: synthetic_graduation_transfer_plan_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Graduation Transfer Plan Boundary Fixture

## Use Boundary

This fixture tests whether a transfer plan preserves pending acceptance,
current custody, and missing authority without turning review acknowledgment
into graduation or transfer. It is non-operative. It creates no acceptance,
contact, transfer, graduation, publication, deployment, or external action.

## Plan Header

| Field | Value |
| --- | --- |
| `transfer_plan_id` | `not_set` |
| `source_inquiry` | `SYNTH-SOURCE-001@r1` |
| `candidate_id` | `SYNTH-CANDIDATE-001@r1` |
| `graduation_proposal` | `SYNTH-GRAD-PROP-001@r1` |
| `current_disposition` | `defer@r1` |
| `source_owner` | `synthetic-source-owner` |
| `proposed_destination_owner` | `synthetic-destination-owner` |
| `acceptance_revision` | `none` |
| `transfer_authority_ref` | `none` |
| `prepared_by` | `not_set` |
| `prepared_at` | `not_set` |
| `external_action` | `none` |

## Frozen Accepted Scope

- Acceptance state: `pending`.
- Acceptance evidence: `none`; `SYNTH-ACK-001@r1` is acknowledgment only.
- Exactly accepted artifacts: none.
- Proposed package: `artifact-alpha@r1`; it is not accepted scope.
- Excluded artifact: `artifact-beta`, with custody unchanged.
- Accepted responsibilities: none.
- Accepted risk: none.
- Authority boundary: no transfer authority exists.
- Prohibited inference: acknowledgment, pending review, or this fixture cannot
  establish acceptance, readiness, ownership, authority, or graduation.

## Custody And Ownership Map

| Truth or responsibility | Current owner | Proposed owner | Transfer evidence | Unresolved custody |
| --- | --- | --- | --- | --- |
| Source truth | `synthetic-source-owner` | none | none | remains with `synthetic-source-owner` |
| Incubator evidence | `synthetic-source-owner` | none | none | remains with `synthetic-source-owner` |
| Destination truth | `synthetic-destination-owner` | `synthetic-destination-owner` | none | no destination truth is transferred |
| Maintenance | `synthetic-source-owner` | none | none | remains with `synthetic-source-owner` |
| Correction | `synthetic-source-owner` | none | none | remains with `synthetic-source-owner` |
| Material risk | `synthetic-source-owner` | none | none | remains with `synthetic-source-owner` |

## Transfer Sequence And Acceptance Gates

### Step 1

- Proposed effect: review the frozen acknowledgment and acceptance fields
  without contacting either owner or changing custody.
- Preconditions: the frozen fixture remains unchanged; external action and
  transfer authority remain `none`.
- Reversibility: no state changes; the last-known-good state is current source
  custody.
- Acknowledgment: `SYNTH-ACK-001@r1`; it is not acceptance.
- Acceptance check: acceptance remains `pending` with evidence `none`.
- Abort rule: stop before contact or transfer and on any package, owner,
  acceptance, authority, custody, or risk change.
- Resulting custody: every artifact, responsibility, correction route, and
  material risk remains with `synthetic-source-owner`.
- Explicit non-effects: no contact, acceptance, transfer, graduation,
  publication, deployment, risk acceptance, or external action.

## Affected Parties, Data, And Legitimacy

- Parties with represented standing: one synthetic reviewer role.
- Representation limits: no real person or institution is represented.
- Risk bearer: `synthetic-source-owner` retains the risk of lost correction
  context if custody changes.
- Data boundary: one public synthetic label, retained only in this fixture.
- Consent and authority gap: no destination acceptance or transfer authority.
- Cannot be spoken for: any real person, institution, source owner, or
  destination owner.

## Unresolved Risks And Negative Evidence

- Unresolved risk: loss of correction context if custody changes.
- Explicit risk acceptance: none.
- Negative evidence: no artifact, responsibility, risk, or custody has been
  accepted.
- Retained risk: all material risk remains with `synthetic-source-owner`.
- No-laundering check: `pending`, acknowledgment-only evidence, missing
  acceptance, and missing authority remain explicit.

## Stops, Correction, Rollback, Recovery, And Revocation

- Pre-transfer stops: acceptance evidence is `none`; transfer authority is
  `none`; all proposed steps stop before contact or transfer.
- Live stops: any package, owner, acceptance, authority, custody, or risk
  change.
- Correction owner: `synthetic-source-owner`.
- Rollback: no transfer occurs, so rollback is restoration to unchanged source
  custody.
- Recovery: retain `artifact-alpha@r1`, evidence, correction, and risk with
  `synthetic-source-owner`.
- Revocation: no grant exists to revoke; any later acceptance or authority
  change requires a fresh decision.

## Prepared Transfer State

- State: `defer`.
- Rationale: acceptance is `pending`, acceptance evidence is `none`, and
  transfer authority is `none`.
- Exact proposed effect: none.
- Explicit non-effects: no acceptance, contact, graduation, transfer,
  operation, deployment, publication, risk acceptance, or external action.
- Next owner: `synthetic-destination-owner`; this pointer creates no contact
  authority.
- Exact next wake: exact destination-owner acceptance plus separate transfer
  authority.

## Frontier Verification

- Confirm `SYNTH-ACK-001@r1` remains acknowledgment rather than acceptance.
- Confirm accepted artifacts, responsibilities, risks, and authority remain
  empty.
- Confirm `artifact-alpha@r1` stays proposed and `artifact-beta` stays excluded.
- Confirm all current custody, correction, and material risk remain with
  `synthetic-source-owner`.
- Confirm the state is `defer` and external action is `none`.
