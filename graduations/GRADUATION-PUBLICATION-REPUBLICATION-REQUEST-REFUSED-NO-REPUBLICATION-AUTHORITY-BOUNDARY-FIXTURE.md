---
artifact_type: synthetic_graduation_publication_republication_request_refused_no_republication_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Graduation Publication Republication Request Refused No-Republication-Authority Boundary Fixture

## Use Boundary

This fixture records one non-operative synthetic republication request and its
authorized internal review after a maintained publication withdrawal. The
review refuses the request because republication execution authority is
absent. State remains
`synthetic_publication_withdrawal_maintained_no_external_effect`. The request,
review authority, decision, and receipt create no posting, sending, contact,
public release, deletion, real-owner acceptance, modification of `CMD-0001`,
P8, or external action.

## Frozen Maintenance And Predecessor Custody

| Key | Exact value |
| --- | --- |
| `maintenance_receipt` | `SYNTH-PUBLICATION-WITHDRAWAL-MAINTENANCE-RECEIPT-001@r1` |
| `maintenance_receipt_content` | `synthetic-content:publication-withdrawal-maintenance-receipt-001-r1` |
| `withdrawal_receipt` | `SYNTH-PUBLICATION-WITHDRAWAL-RECEIPT-001@r1` |
| `current_state` | `synthetic_publication_withdrawal_maintained_no_external_effect` |
| `prior_return` | `synthetic_publication_withdrawal_maintenance_record_only` |

Every predecessor checksum is valid. The maintained-withdrawal state and its
receipts remain immutable history. This fixture neither replaces their
content nor enlarges their authority.

## Non-Operative Republication Request

At `2026-08-28T00:40:12Z`,
`SYNTH-PUBLICATION-REPUBLICATION-REQUEST-001@r1` is prepared internally by
`synthetic-publication-requester`. It requests republication but grants no
authority, is never sent, and creates no destination-owner or public-endpoint
event. It is review input only.

## Request Review Authority Decision And Receipt

At `2026-08-28T00:42:12Z`,
`SYNTH-PUBLICATION-REPUBLICATION-REQUEST-REVIEW-AUTHORITY-001@r1` is signed by
`synthetic-receiving-owner` under
`synthetic-publication-republication-request-review-decision-authority@r1` for
one use by `synthetic-publication-request-reviewer`. It permits only internal
review after exact lineage, maintenance-receipt, risk, no-revocation, and
unconsumed-authority checks. At `2026-08-28T00:44:12Z`, decision
`SYNTH-PUBLICATION-REPUBLICATION-REQUEST-REVIEW-DECISION-001@r1`, content
`synthetic-content:publication-republication-request-review-decision-001-r1`,
records `refuse_synthetic_republication_request_no_execution_authority`. At
`2026-08-28T00:45:12Z`, receipt
`SYNTH-PUBLICATION-REPUBLICATION-REQUEST-REVIEW-RECEIPT-001@r1`, content
`synthetic-content:publication-republication-request-review-receipt-001-r1`,
consumes the review authority and leaves state unchanged.

## Risk Owner Fit And Legitimacy

The review owner is `synthetic-receiving-owner`; the correction owner is
`synthetic-mechanism-map-owner`. The principal risks are mistaking a prepared
request or review receipt for republication authority, treating the unsent
request as contact, or using review to bypass the maintained withdrawal. The
one-use review scope, unchanged state, explicit refusal, and separate
correction owner contain those risks. This fixture represents no affected
person, destination owner, publisher, or public endpoint and supplies none of
their standing, consent, acceptance, or authority.

## Stops Correction Recovery And Reopen

Stop before review if any predecessor identifier or content ID differs, the
maintenance receipt is invalid, the request was sent, the review authority is
missing, revoked, out of scope, or already consumed, the reviewer differs
from `synthetic-publication-request-reviewer`, or review would imply
republication or another external effect. Treat duplicate authority use,
missing risk custody, an altered refusal, or any claim that request or receipt
authorizes execution as failure modes. The correction owner preserves the
failed record as negative evidence and restores the unchanged current state
`synthetic_publication_withdrawal_maintained_no_external_effect`; it does not
erase the attempt or predecessor history. Reopen only on exact synthetic
republication execution authority under the refusal receipt, or a named
revision.

## Prepared Return And Exact Wake

Return only the refusal decision and receipt, unchanged maintained-withdrawal
state, immutable predecessor pointers, consumed review-authority fact, named
owners, risks, non-effects, and exact wake. No republication, destination
acceptance, graduation, public release, or external-action return is created.
Exact next wake is exact synthetic republication execution authority under the
refusal receipt, or any named revision.

## Frontier Verification

Verify the exact predecessor rows, request preparer and non-transmission,
authority signer, scope and reviewer, decision, receipt, one-use consumption,
unchanged state, owner fit, risk custody, stops, correction, recovery, and
wake. Confirm the record remains an internal synthetic fixture and creates no
real publication, deletion, contact, owner acceptance, candidate, P8, or
external effect.
