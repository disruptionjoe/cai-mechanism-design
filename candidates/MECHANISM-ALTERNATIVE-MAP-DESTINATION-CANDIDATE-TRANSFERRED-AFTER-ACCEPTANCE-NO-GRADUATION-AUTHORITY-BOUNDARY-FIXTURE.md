---
artifact_type: synthetic_mechanism_alternative_map_destination_candidate_transferred_after_acceptance_no_graduation_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Mechanism Alternative-Map Destination-Candidate Transferred-After-Acceptance No-Graduation-Authority Boundary Fixture

## Use Boundary

This synthetic fixture preserves no action, both pointer routes, the complete execution and destination-state lineage, all three prior transfer-request reviews and refusals, the receiving-owner interest notice, the exact receiving-owner acceptance, and prior route state `destination_candidate_redeferred_no_transfer`. It adds one exact one-use transfer execution authority, one authorized synthetic transfer decision, and its trace and receipt. This changes only synthetic route state inside the fixture to `destination_candidate_transferred_not_graduated`. It is not Mechanism Design admission or disposition, graduation, deployment, performance, publication, contact, a target-native effect outside the fixture, or external action. Do not modify `CMD-0001` or create P8. External action is `none`.

## Map Header

| Field | Value |
| --- | --- |
| `map_id` | `SYNTH-DESTINATION-CANDIDATE-TRANSFER-AFTER-ACCEPTANCE-MAP-001@r1` |
| `source_inquiry` | `SYNTH-SOURCE-OPENED-ROUTE-NO-DELIVERY-001@r1` |
| `source_revision` | `synthetic-source-revision:opened-route-no-delivery-001-r1` |
| `candidate_or_problem_ref` | `SYNTH-PROBLEM-OPENED-ROUTE-NO-DELIVERY-001@r1`; Mechanism Design candidate scope `none` |
| `payload` | `SYNTH-NATIVE-CONTENT-PAYLOAD-001@r1`; `synthetic-content:native-content-payload-001-r1` |
| `comparison` | `SYNTH-CONDITION-IMMEDIATE-REQUIRED-006@r1` |
| `selection` | `SYNTH-ROUTE-SELECTION-IMMEDIATE-004@r1` |
| `destination_acceptance` | `SYNTH-DESTINATION-ACCEPTANCE-IMMEDIATE-003@r1` |
| `destination_candidate` | `SYNTH-DESTINATION-CANDIDATE-001@r1` |
| `existing_owner_fit` | `synthetic-destination-owner` |
| `receiving_owner` | `synthetic-receiving-owner` |
| `map_owner` | `synthetic-mechanism-map-owner` |
| `authorization_ref` | `synthetic://decision-boundary/SYNTH-DESTINATION-CANDIDATE-TRANSFER-EXECUTION-AUTHORITY-001@r1` |
| `route_state` | `destination_candidate_transferred_not_graduated` |
| `external_action` | `none` |

## Frozen Inquiry And Mechanism Design Candidate Boundary

The fixture is frozen against `GOVERNANCE.md`, `interfaces/DESTINATION-OWNER-SYNTHETIC-REVIEW-REQUEST-TEMPLATE.md`, `candidates/MECHANISM-ALTERNATIVE-MAP-TEMPLATE.md`, and `candidates/MECHANISM-ALTERNATIVE-MAP-DESTINATION-CANDIDATE-RECEIVING-OWNER-ACCEPTANCE-NO-TRANSFER-AUTHORITY-BOUNDARY-FIXTURE.md`. Source `SYNTH-SOURCE-OPENED-ROUTE-NO-DELIVERY-001@r1`, source revision `synthetic-source-revision:opened-route-no-delivery-001-r1`, problem `SYNTH-PROBLEM-OPENED-ROUTE-NO-DELIVERY-001@r1`, immutable payload `SYNTH-NATIVE-CONTENT-PAYLOAD-001@r1` with content ID `synthetic-content:native-content-payload-001-r1`, comparison `SYNTH-CONDITION-IMMEDIATE-REQUIRED-006@r1`, selection `SYNTH-ROUTE-SELECTION-IMMEDIATE-004@r1`, destination acceptance `SYNTH-DESTINATION-ACCEPTANCE-IMMEDIATE-003@r1`, and destination candidate `SYNTH-DESTINATION-CANDIDATE-001@r1` remain unchanged. Existing-owner fit remains `synthetic-destination-owner`; receiving owner remains `synthetic-receiving-owner`; Mechanism Design candidate scope remains `none`.

## Alternative Records

The alternatives remain `SYNTH-ALT-OPENED-NO-ACTION-001@r1`, `SYNTH-ALT-OPENED-IMMEDIATE-001@r1`, and `SYNTH-ALT-OPENED-VERIFIED-001@r1`. The first preserves no action; the second preserves the selected immediate pointer route; the third preserves the materially distinct dominated verified pointer route.

The literal consumed execution lineage remains:

- opening — `SYNTH-ROUTE-OPENING-AUTHORIZATION-002@r1`; `synthetic-route-opening-authority-owner`; `synthetic-route-opening-decision-authority@r1`; `SYNTH-ROUTE-OPENING-TRACE-001@r1`; `SYNTH-ROUTE-OPENING-RECEIPT-001@r1`; `synthetic-content:route-opening-receipt-opened-no-delivery-001-r1`
- sending — `SYNTH-ROUTE-SENDING-AUTHORIZATION-001@r1`; `synthetic-route-sending-authority-owner`; `synthetic-route-sending-decision-authority@r1`; `SYNTH-ROUTE-SENDING-TRACE-001@r1`; `SYNTH-ROUTE-SENDING-RECEIPT-001@r1`; `synthetic-content:route-sending-receipt-sent-no-delivery-001-r1`
- delivery — `SYNTH-ROUTE-DELIVERY-AUTHORIZATION-001@r1`; `synthetic-route-delivery-authority-owner`; `synthetic-route-delivery-decision-authority@r1`; `SYNTH-ROUTE-DELIVERY-TRACE-001@r1`; `SYNTH-ROUTE-DELIVERY-RECEIPT-001@r1`; `synthetic-content:route-delivery-receipt-delivered-no-acknowledgment-001-r1`
- acknowledgment — `SYNTH-ROUTE-ACKNOWLEDGMENT-AUTHORIZATION-001@r1`; `synthetic-route-acknowledgment-authority-owner`; `synthetic-route-acknowledgment-decision-authority@r1`; `SYNTH-ROUTE-ACKNOWLEDGMENT-TRACE-001@r1`; `SYNTH-ROUTE-ACKNOWLEDGMENT-RECEIPT-001@r1`; `synthetic-content:route-acknowledgment-receipt-acknowledged-no-intake-001-r1`
- intake — `SYNTH-ROUTE-INTAKE-AUTHORIZATION-001@r1`; `synthetic-destination-owner`; `synthetic-destination-pointer-intake-execution-authority@r1`; `SYNTH-ROUTE-INTAKE-TRACE-001@r1`; `SYNTH-ROUTE-INTAKE-RECEIPT-001@r1`; `synthetic-content:route-intake-receipt-intaken-no-candidate-001-r1`
- native-content copy — `SYNTH-ROUTE-NATIVE-CONTENT-COPY-AUTHORIZATION-001@r1`; `synthetic-destination-owner`; `synthetic-destination-native-content-copy-execution-authority@r1`; `SYNTH-ROUTE-NATIVE-CONTENT-COPY-TRACE-001@r1`; `SYNTH-ROUTE-NATIVE-CONTENT-COPY-RECEIPT-001@r1`; `synthetic-content:route-native-content-copy-receipt-copied-no-candidate-001-r1`

All six grants are consumed and all checksums remain valid. The consumed destination-state lineage remains:

- admission — `SYNTH-DESTINATION-CANDIDATE-ADMISSION-AUTHORITY-001@r1`; signer `synthetic-destination-owner`; scope `synthetic-destination-candidate-admission-decision-authority@r1`; decider `synthetic-destination-candidate-admission-decider`; decision `SYNTH-DESTINATION-CANDIDATE-ADMISSION-DECISION-001@r1` at `2026-08-27T21:20:12Z`; content `synthetic-content:destination-candidate-admission-decision-001-r1`; consumed
- defer — `SYNTH-DESTINATION-CANDIDATE-DISPOSITION-AUTHORITY-001@r1`; signer `synthetic-destination-owner`; scope `synthetic-destination-candidate-disposition-decision-authority@r1`; decider `synthetic-destination-candidate-disposition-decider`; decision `SYNTH-DESTINATION-CANDIDATE-DISPOSITION-DECISION-001@r1` at `2026-08-27T21:35:12Z`; content `synthetic-content:destination-candidate-defer-disposition-decision-001-r1`; consumed
- rejection — `SYNTH-DESTINATION-CANDIDATE-RECONSIDERATION-AUTHORITY-001@r1`; signer `synthetic-destination-owner`; scope `synthetic-destination-candidate-reconsideration-decision-authority@r1`; decider `synthetic-destination-candidate-reconsideration-decider`; decision `SYNTH-DESTINATION-CANDIDATE-RECONSIDERATION-DECISION-001@r1` at `2026-08-27T21:50:12Z`; content `synthetic-content:destination-candidate-rejection-decision-001-r1`; consumed
- reopen — `SYNTH-DESTINATION-CANDIDATE-REOPEN-AUTHORITY-001@r1`; signer `synthetic-destination-owner`; scope `synthetic-destination-candidate-reopen-decision-authority@r1`; decider `synthetic-destination-candidate-reopen-decider`; decision `SYNTH-DESTINATION-CANDIDATE-REOPEN-DECISION-001@r1` at `2026-08-27T22:10:12Z`; content `synthetic-content:destination-candidate-reopen-decision-001-r1`; consumed
- re-defer — `SYNTH-DESTINATION-CANDIDATE-REOPEN-REVIEW-AUTHORITY-001@r1`; signer `synthetic-destination-owner`; scope `synthetic-destination-candidate-reopen-review-decision-authority@r1`; decider `synthetic-destination-candidate-reopen-review-decider`; decision `SYNTH-DESTINATION-CANDIDATE-REOPEN-REVIEW-DECISION-001@r1` at `2026-08-27T22:25:12Z`; content `synthetic-content:destination-candidate-reopen-review-redefer-decision-001-r1`; consumed

## Material Difference And Nonduplication

This fixture changes only synthetic route state from `destination_candidate_redeferred_no_transfer` to `destination_candidate_transferred_not_graduated`. Receiving-owner acceptance differs from transfer authority; transfer authority differs from graduation or deployment authority. The transfer decision, trace, and receipt do not repeat any prior request review. All predecessor records remain visible, and no consumed authority is reused.

## Existing-Owner Fit

Existing-owner fit remains `synthetic-destination-owner`; the receiving owner remains `synthetic-receiving-owner`. The exact transfer moves only the unchanged synthetic candidate and its frozen unresolved-risk package between those synthetic custodians. It creates no Mechanism Design candidate, real-owner transfer, or authority outside the fixture. Correction remains with `synthetic-mechanism-map-owner`.

## Evidence, Affected Parties, And Legitimacy

The first request `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-001@r1`, signed at `2026-08-27T22:30:12Z` by `synthetic-transfer-requester` under `synthetic-transfer-request-creation-authority@r1`, has content ID `synthetic-content:destination-candidate-transfer-request-001-r1` and a valid checksum. Review authority `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-AUTHORITY-001@r1` and refusal `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-001@r1` are consumed; the refusal remains `transfer_request_not_admitted_missing_receiving_owner_acceptance_and_authority`.

Interest `SYNTH-RECEIVING-OWNER-TRANSFER-INTEREST-001@r1`, signed at `2026-08-27T22:40:12Z` by `synthetic-receiving-owner-liaison` under `synthetic-receiving-owner-interest-record-creation-authority@r1`, has content ID `synthetic-content:receiving-owner-transfer-interest-001-r1` and a valid checksum. Renewed request `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-002@r1`, signed at `2026-08-27T22:42:12Z` by `synthetic-transfer-requester` under `synthetic-transfer-request-creation-authority@r1`, has content ID `synthetic-content:destination-candidate-transfer-request-002-r1` and a valid checksum. Review authority `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-AUTHORITY-002@r1` and refusal `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-002@r1` are consumed; the refusal remains `renewed_transfer_request_not_admitted_interest_is_not_acceptance_and_transfer_authority_absent`.

At `2026-08-27T22:50:12Z`, acceptance `SYNTH-RECEIVING-OWNER-TRANSFER-ACCEPTANCE-001@r1` is signed by `synthetic-receiving-owner-acceptance-decider` under `synthetic-receiving-owner-transfer-acceptance-decision-authority@r1`. Content ID `synthetic-content:receiving-owner-transfer-acceptance-001-r1` has a valid checksum. It accepts the unchanged scope and frozen risks for transfer review but grants no execution authority.

At `2026-08-27T22:52:12Z`, review authority `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-AUTHORITY-003@r1` is signed by `synthetic-destination-owner` under `synthetic-destination-candidate-transfer-request-review-decision-authority@r1`. It authorizes only `synthetic-destination-candidate-transfer-request-reviewer` once to review the frozen acceptance-and-refusal record, not to transfer. At `2026-08-27T22:55:12Z`, decision `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-003@r1` is signed by that reviewer and records `transfer_request_not_admitted_acceptance_present_but_transfer_authority_absent`. Content ID `synthetic-content:destination-candidate-transfer-request-review-refusal-decision-003-r1` has a valid checksum; the third review authority is consumed.

All actors, standing, evidence, authorities, and systems are synthetic. The legitimacy risk is authority laundering: acceptance, evidence, a request, or review authority must not be made operative beyond its exact scope.

## Comparison Through Transfer-Request Refusals

All three requests remain non-operative. The first refusal proves that a request cannot substitute for receiving-owner acceptance or authority. The second proves that receiving-owner interest cannot substitute for acceptance or authority. The third proves that receiving-owner acceptance cannot substitute for transfer execution authority. The third refusal remains `transfer_request_not_admitted_acceptance_present_but_transfer_authority_absent`; all three review authorities remain consumed. None changes the historical defer, rejection, reopen, or re-defer sequence.

## Authorized Transfer And Downstream Nonperformance

At `2026-08-27T23:00:12Z`, transfer execution authority `SYNTH-DESTINATION-CANDIDATE-TRANSFER-EXECUTION-AUTHORITY-001@r1` is signed by `synthetic-destination-owner` under `synthetic-destination-candidate-transfer-execution-authority@r1`. It authorizes only `synthetic-destination-candidate-transfer-executor` once to transfer the unchanged synthetic candidate and its frozen unresolved-risk package to `synthetic-receiving-owner` after verifying every predecessor, exact acceptance, both owner identifiers, unchanged scope and checksum, no revocation, and unconsumed authority. It authorizes no graduation, deployment, performance, publication, contact, real-owner effect, or external action.

At `2026-08-27T23:02:12Z`, every check matched. Decision `SYNTH-DESTINATION-CANDIDATE-TRANSFER-DECISION-001@r1` is signed by that executor and records `transfer_accepted_synthetic_candidate_under_exact_authority`. Content ID `synthetic-content:destination-candidate-transfer-decision-001-r1` has a valid checksum.

At `2026-08-27T23:05:12Z`, trace `SYNTH-DESTINATION-CANDIDATE-TRANSFER-TRACE-001@r1` and receipt `SYNTH-DESTINATION-CANDIDATE-TRANSFER-RECEIPT-001@r1` record only the synthetic state transition. Receipt content ID `synthetic-content:destination-candidate-transfer-receipt-001-r1` has a valid checksum. The one-use transfer authority is consumed. Route state becomes `destination_candidate_transferred_not_graduated`; prepared return is `synthetic_transfer_record_only`. No graduation, deployment, performance, publication, contact, real-owner effect, or external action follows.

## Prepared Return And Recovery

Correction owner is `synthetic-mechanism-map-owner`. Stop on any named fact, scope, acceptance, authority, trace, receipt, checksum, or risk revision. Failure modes include acceptance treated as authority, authority reused, transfer treated as graduation or deployment, frozen history erased, or a real downstream effect invented. Failed transfer recovery retracts only the transfer decision, trace, and receipt; preserves all predecessor evidence and acceptance; restores `destination_candidate_redeferred_no_transfer`; and changes no real owner or candidate. Exact next wake is exact graduation-review authority and destination-owner graduation acceptance under the frozen transfer receipt, materially new owner evidence, or any named revision.

## Frontier Verification

Repository integration verified native frontmatter and section topology; no action and both pointer routes; the complete consumed execution and destination-state lineage; all three request reviews and refusals; interest and acceptance; exact transfer authority, decision, trace, receipt, content IDs, checksum assertions, recovery, non-effects, and exact wake. Route state is `destination_candidate_transferred_not_graduated`. `CMD-0001`, P8, real disposition, transfer, graduation, deployment, and external-action state remain unchanged.
