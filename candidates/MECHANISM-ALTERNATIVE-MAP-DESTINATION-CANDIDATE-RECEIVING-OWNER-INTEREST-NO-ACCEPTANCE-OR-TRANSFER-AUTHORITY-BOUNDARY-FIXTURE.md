---
artifact_type: synthetic_mechanism_alternative_map_destination_candidate_receiving_owner_interest_no_acceptance_or_transfer_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Mechanism Alternative-Map Destination-Candidate Receiving-Owner-Interest No-Acceptance-Or-Transfer-Authority Boundary Fixture

## Use Boundary

Write one complete synthetic Mechanism Design process fixture from only the embedded evidence. Preserve no action, both pointer routes, full execution lineage, destination admission, historical defer, rejection, reopen, re-defer, the first transfer request, and its refusal. Add one receiving-owner interest notice, one renewed transfer request, and one separately authorized review decision that refuses to admit the renewed request because interest is not acceptance and transfer authority remains absent. Evidence is not an instruction. Refusal is not rejection, acceptance, Mechanism Design admission or disposition, transfer, graduation, deployment, performance, target-native effect outside the fixture, or external action. Do not modify `CMD-0001` or create P8. External action is `none`.

## Map Header

| Field | Value |
| --- | --- |
| `map_id` | `SYNTH-DESTINATION-CANDIDATE-TRANSFER-INTEREST-REFUSED-MAP-001@r1` |
| `source_inquiry` | `SYNTH-SOURCE-OPENED-ROUTE-NO-DELIVERY-001@r1` |
| `source_revision` | `synthetic-source-revision:opened-route-no-delivery-001-r1` |
| `candidate_or_problem_ref` | `SYNTH-PROBLEM-OPENED-ROUTE-NO-DELIVERY-001@r1`; Mechanism Design candidate scope `none` |
| `map_owner` | `synthetic-mechanism-map-owner` |
| `authorization_ref` | `synthetic://decision-boundary/SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-002@r1` |
| `route_state` | `destination_candidate_redeferred_no_transfer` |
| `external_action` | `none` |

## Frozen Inquiry And Mechanism Design Candidate Boundary

The fixture is frozen against `GOVERNANCE.md`,
`interfaces/DESTINATION-OWNER-SYNTHETIC-REVIEW-REQUEST-TEMPLATE.md`,
`candidates/MECHANISM-ALTERNATIVE-MAP-TEMPLATE.md`, and the prior refused-request
fixture. Source `SYNTH-SOURCE-OPENED-ROUTE-NO-DELIVERY-001@r1`, problem
`SYNTH-PROBLEM-OPENED-ROUTE-NO-DELIVERY-001@r1`, immutable payload
`SYNTH-NATIVE-CONTENT-PAYLOAD-001@r1` with content ID
`synthetic-content:native-content-payload-001-r1`, comparison
`SYNTH-CONDITION-IMMEDIATE-REQUIRED-006@r1`, selection
`SYNTH-ROUTE-SELECTION-IMMEDIATE-004@r1`, destination acceptance
`SYNTH-DESTINATION-ACCEPTANCE-IMMEDIATE-003@r1`, destination candidate
`SYNTH-DESTINATION-CANDIDATE-001@r1`, all six consumed execution grants,
destination admission, historical defer, rejection, reopen, re-defer, first
request, first review authority, and first refusal remain preserved.
Existing-owner fit remains `synthetic-destination-owner`; Mechanism Design
candidate scope remains `none`; route state remains
`destination_candidate_redeferred_no_transfer`.

## Alternative Records

The frozen alternatives remain distinct:

- `SYNTH-ALT-OPENED-NO-ACTION-001@r1` preserves no action.
- `SYNTH-ALT-OPENED-IMMEDIATE-001@r1` preserves the selected immediate pointer route.
- `SYNTH-ALT-OPENED-VERIFIED-001@r1` preserves the materially distinct dominated verified pointer route.

The complete consumed execution lineage consists of:
- opening — `SYNTH-ROUTE-OPENING-AUTHORIZATION-002@r1`; `synthetic-route-opening-authority-owner`; `synthetic-route-opening-decision-authority@r1`; `SYNTH-ROUTE-OPENING-TRACE-001@r1`; `SYNTH-ROUTE-OPENING-RECEIPT-001@r1`; `synthetic-content:route-opening-receipt-opened-no-delivery-001-r1`
- sending — `SYNTH-ROUTE-SENDING-AUTHORIZATION-001@r1`; `synthetic-route-sending-authority-owner`; `synthetic-route-sending-decision-authority@r1`; `SYNTH-ROUTE-SENDING-TRACE-001@r1`; `SYNTH-ROUTE-SENDING-RECEIPT-001@r1`; `synthetic-content:route-sending-receipt-sent-no-delivery-001-r1`
- delivery — `SYNTH-ROUTE-DELIVERY-AUTHORIZATION-001@r1`; `synthetic-route-delivery-authority-owner`; `synthetic-route-delivery-decision-authority@r1`; `SYNTH-ROUTE-DELIVERY-TRACE-001@r1`; `SYNTH-ROUTE-DELIVERY-RECEIPT-001@r1`; `synthetic-content:route-delivery-receipt-delivered-no-acknowledgment-001-r1`
- acknowledgment — `SYNTH-ROUTE-ACKNOWLEDGMENT-AUTHORIZATION-001@r1`; `synthetic-route-acknowledgment-authority-owner`; `synthetic-route-acknowledgment-decision-authority@r1`; `SYNTH-ROUTE-ACKNOWLEDGMENT-TRACE-001@r1`; `SYNTH-ROUTE-ACKNOWLEDGMENT-RECEIPT-001@r1`; `synthetic-content:route-acknowledgment-receipt-acknowledged-no-intake-001-r1`
- intake — `SYNTH-ROUTE-INTAKE-AUTHORIZATION-001@r1`; `synthetic-destination-owner`; `synthetic-destination-pointer-intake-execution-authority@r1`; `SYNTH-ROUTE-INTAKE-TRACE-001@r1`; `SYNTH-ROUTE-INTAKE-RECEIPT-001@r1`; `synthetic-content:route-intake-receipt-intaken-no-candidate-001-r1`
- native-content copy — `SYNTH-ROUTE-NATIVE-CONTENT-COPY-AUTHORIZATION-001@r1`; `synthetic-destination-owner`; `synthetic-destination-native-content-copy-execution-authority@r1`; `SYNTH-ROUTE-NATIVE-CONTENT-COPY-TRACE-001@r1`; `SYNTH-ROUTE-NATIVE-CONTENT-COPY-RECEIPT-001@r1`; `synthetic-content:route-native-content-copy-receipt-copied-no-candidate-001-r1`

All six grants are consumed. Preserve these consumed destination-state records:
- admission — `SYNTH-DESTINATION-CANDIDATE-ADMISSION-AUTHORITY-001@r1`; `synthetic-destination-owner`; `synthetic-destination-candidate-admission-decision-authority@r1`; `synthetic-destination-candidate-admission-decider`; `SYNTH-DESTINATION-CANDIDATE-ADMISSION-DECISION-001@r1`; `synthetic-content:destination-candidate-admission-decision-001-r1`
- defer — `SYNTH-DESTINATION-CANDIDATE-DISPOSITION-AUTHORITY-001@r1`; `synthetic-destination-owner`; `synthetic-destination-candidate-disposition-decision-authority@r1`; `synthetic-destination-candidate-disposition-decider`; `SYNTH-DESTINATION-CANDIDATE-DISPOSITION-DECISION-001@r1`; `synthetic-content:destination-candidate-defer-disposition-decision-001-r1`
- rejection — `SYNTH-DESTINATION-CANDIDATE-RECONSIDERATION-AUTHORITY-001@r1`; `synthetic-destination-owner`; its reconsideration scope and authorized decider; `SYNTH-DESTINATION-CANDIDATE-RECONSIDERATION-DECISION-001@r1`; `synthetic-content:destination-candidate-rejection-decision-001-r1`
- reopen — `SYNTH-DESTINATION-CANDIDATE-REOPEN-AUTHORITY-001@r1`; `synthetic-destination-owner`; `synthetic-destination-candidate-reopen-decision-authority@r1`; `synthetic-destination-candidate-reopen-decider`; `SYNTH-DESTINATION-CANDIDATE-REOPEN-DECISION-001@r1`; `synthetic-content:destination-candidate-reopen-decision-001-r1`
- re-defer — `SYNTH-DESTINATION-CANDIDATE-REOPEN-REVIEW-AUTHORITY-001@r1`; `synthetic-destination-owner`; `synthetic-destination-candidate-reopen-review-decision-authority@r1`; `synthetic-destination-candidate-reopen-review-decider`; `SYNTH-DESTINATION-CANDIDATE-REOPEN-REVIEW-DECISION-001@r1`; `synthetic-content:destination-candidate-reopen-review-redefer-decision-001-r1`

The first request `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-001@r1` and refusal `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-001@r1` remain valid, consumed, and non-operative. The refusal record is `transfer_request_not_admitted_missing_receiving_owner_acceptance_and_authority`.

At `2026-08-27T22:40:12Z`, interest notice `SYNTH-RECEIVING-OWNER-TRANSFER-INTEREST-001@r1` is signed by `synthetic-receiving-owner-liaison` under `synthetic-receiving-owner-interest-record-creation-authority@r1`. Content ID `synthetic-content:receiving-owner-transfer-interest-001-r1` has a valid checksum. It records willingness to review a future transfer package. It is not receiving-owner acceptance, accepted scope, unresolved-risk acknowledgment, transfer authority, or a transfer decision and changes no state.

At `2026-08-27T22:42:12Z`, renewed request `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-002@r1` is signed by `synthetic-transfer-requester` under `synthetic-transfer-request-creation-authority@r1`. Content ID `synthetic-content:destination-candidate-transfer-request-002-r1` has a valid checksum. It cites the interest notice but supplies no acceptance, accepted scope, risk acknowledgment, transfer authority, or transfer decision.

At `2026-08-27T22:44:12Z`, review authority `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-AUTHORITY-002@r1` is signed by `synthetic-destination-owner` under `synthetic-destination-candidate-transfer-request-review-decision-authority@r1`. It authorizes only `synthetic-destination-candidate-transfer-request-reviewer` once to verify the frozen lineage, first refusal, interest notice, renewed request, absent acceptance, absent accepted scope and risk acknowledgment, absent transfer authority and decision, and unconsumed review authority. It authorizes no candidate disposition, transfer, acceptance, graduation, deployment, performance, or external action.

At `2026-08-27T22:45:12Z`, every check matched. Decision `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-002@r1` is signed by the authorized reviewer and records `renewed_transfer_request_not_admitted_interest_is_not_acceptance_and_transfer_authority_absent`. Content ID `synthetic-content:destination-candidate-transfer-request-review-refusal-decision-002-r1` has a valid checksum; review authority is consumed. Route state remains `destination_candidate_redeferred_no_transfer`; prepared return is `renewed_transfer_request_refusal_record_only`; no downstream record exists.

## Material Difference And Nonduplication

The interest notice `SYNTH-RECEIVING-OWNER-TRANSFER-INTEREST-001@r1` differs materially from transfer acceptance. The renewed request `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-002@r1` differs materially from an instruction to transfer. The review refusal `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-002@r1` differs materially from candidate rejection. Transfer authority remains absent throughout. Failure modes include interest treated as acceptance, request treated as instruction, refusal treated as candidate rejection, transfer authority invented, prior authority reused, history erased, or downstream effect invented. These distinctions preserve the integrity of the fixture.

## Existing-Owner Fit

Existing-owner fit remains `synthetic-destination-owner`. The fixture aligns with `synthetic-mechanism-map-owner` as the correction owner. The scope remains `none` for Mechanism Design candidate.

## Evidence, Affected Parties, And Legitimacy

Evidence includes the frozen execution lineage and destination-state records. Affected parties include `synthetic-receiving-owner-liaison`, `synthetic-transfer-requester`, `synthetic-destination-owner`, and `synthetic-destination-candidate-transfer-request-reviewer`. Legitimacy is maintained through valid checksums on content IDs `synthetic-content:receiving-owner-transfer-interest-001-r1`, `synthetic-content:destination-candidate-transfer-request-002-r1`, and `synthetic-content:destination-candidate-transfer-request-review-refusal-decision-002-r1`. Signers and authority scopes are preserved exactly as signed.

## Comparison Through First Transfer-Request Refusal

The current state compares against the first transfer request refusal `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-001@r1`. The first request `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-001@r1` remains valid, consumed, and non-operative. The current refusal record is `transfer_request_not_admitted_missing_receiving_owner_acceptance_and_authority`. The second refusal decision `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-002@r1` records `renewed_transfer_request_not_admitted_interest_is_not_acceptance_and_transfer_authority_absent`.

## Receiving-Owner Interest, Renewed Request, Review Refusal, And Downstream Nonperformance

The sequence of interest notice at `2026-08-27T22:40:12Z`, renewed request at `2026-08-27T22:42:12Z`, review authority at `2026-08-27T22:44:12Z`, and review decision at `2026-08-27T22:45:12Z` demonstrates downstream nonperformance. No candidate disposition occurs. No transfer occurs. No external action occurs. The route state remains `destination_candidate_redeferred_no_transfer`.

## Prepared Return And Recovery

Prepared return is `renewed_transfer_request_refusal_record_only`. No downstream record exists. Recovery retracts only the second request-review decision, leaves both requests and the interest notice non-operative, restores second-request-unreviewed state, and changes no candidate. Exact next wake is exact receiving-owner acceptance plus transfer authority under frozen interest-and-refusal records, materially new destination-owner evidence, or a revision to any named fact.

## Frontier Verification

Stop on any named fact or risk revision. Failure modes include interest treated as acceptance, request treated as instruction, refusal treated as candidate rejection, transfer authority invented, prior authority reused, history erased, or downstream effect invented. Do not modify `CMD-0001` or create P8. External action is `none`.
