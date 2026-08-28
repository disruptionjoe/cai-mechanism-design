---
artifact_type: synthetic_graduation_proposal_transferred_candidate_accepted_no_graduation_execution_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Graduation-Proposal Transferred-Candidate Accepted No-Graduation-Execution-Authority Boundary Fixture

## Use Boundary

This synthetic fixture preserves one transferred destination candidate, its complete execution and destination-state history, three refused transfer requests, receiving-owner interest and acceptance, the exact authorized transfer, one graduation proposal, and one exact destination-owner acceptance of that proposal. Synthetic process state becomes `graduation_proposal_accepted_not_graduated`. Proposal acceptance is not graduation execution, deployment, performance, publication, contact, a real owner effect, or external action. Mechanism Design candidate scope remains `none`; `CMD-0001` is unchanged and P8 is not created. External action is `none`.

## Proposal Header

| Field | Value |
| --- | --- |
| `proposal_id` | `SYNTH-GRADUATION-PROPOSAL-001@r1` |
| `destination_candidate` | `SYNTH-DESTINATION-CANDIDATE-001@r1` |
| `destination_owner` | `synthetic-destination-owner` |
| `receiving_owner` | `synthetic-receiving-owner` |
| `proposal_created_at` | `2026-08-27T23:10:12Z` |
| `proposal_created_by` | `synthetic-graduation-proposer` |
| `proposal_authority` | `synthetic-graduation-proposal-record-creation-authority@r1` |
| `proposal_content_id` | `synthetic-content:graduation-proposal-001-r1`; checksum valid |
| `process_state` | `graduation_proposal_accepted_not_graduated` |
| `external_action` | `none` |

## Frozen Candidate, Transfer, And Owner Fit

The fixture is frozen against `GOVERNANCE.md`, `interfaces/DESTINATION-OWNER-SYNTHETIC-REVIEW-REQUEST-TEMPLATE.md`, `graduations/GRADUATION-PROPOSAL-TEMPLATE.md`, `graduations/GRADUATION-TRANSFER-PLAN-TEMPLATE.md`, and `candidates/MECHANISM-ALTERNATIVE-MAP-DESTINATION-CANDIDATE-TRANSFERRED-AFTER-ACCEPTANCE-NO-GRADUATION-AUTHORITY-BOUNDARY-FIXTURE.md`. Map `SYNTH-DESTINATION-CANDIDATE-TRANSFER-AFTER-ACCEPTANCE-MAP-001@r1`, source `SYNTH-SOURCE-OPENED-ROUTE-NO-DELIVERY-001@r1`, source revision `synthetic-source-revision:opened-route-no-delivery-001-r1`, problem `SYNTH-PROBLEM-OPENED-ROUTE-NO-DELIVERY-001@r1`, payload `SYNTH-NATIVE-CONTENT-PAYLOAD-001@r1`, payload content `synthetic-content:native-content-payload-001-r1`, and destination candidate `SYNTH-DESTINATION-CANDIDATE-001@r1` remain unchanged. Existing-owner fit remains `synthetic-destination-owner`; receiving owner remains `synthetic-receiving-owner`; prior route state remains `destination_candidate_transferred_not_graduated`.

No action and alternatives `SYNTH-ALT-OPENED-NO-ACTION-001@r1`, `SYNTH-ALT-OPENED-IMMEDIATE-001@r1`, and `SYNTH-ALT-OPENED-VERIFIED-001@r1` remain visible. Comparison `SYNTH-CONDITION-IMMEDIATE-REQUIRED-006@r1`, selection `SYNTH-ROUTE-SELECTION-IMMEDIATE-004@r1`, and destination acceptance `SYNTH-DESTINATION-ACCEPTANCE-IMMEDIATE-003@r1` remain unchanged.

## Execution And Destination-State Lineage

The six consumed execution grants remain inspectable:

- opening — `SYNTH-ROUTE-OPENING-AUTHORIZATION-002@r1`; `synthetic-route-opening-authority-owner`; `synthetic-route-opening-decision-authority@r1`; `SYNTH-ROUTE-OPENING-TRACE-001@r1`; `SYNTH-ROUTE-OPENING-RECEIPT-001@r1`; `synthetic-content:route-opening-receipt-opened-no-delivery-001-r1`
- sending — `SYNTH-ROUTE-SENDING-AUTHORIZATION-001@r1`; `synthetic-route-sending-authority-owner`; `synthetic-route-sending-decision-authority@r1`; `SYNTH-ROUTE-SENDING-TRACE-001@r1`; `SYNTH-ROUTE-SENDING-RECEIPT-001@r1`; `synthetic-content:route-sending-receipt-sent-no-delivery-001-r1`
- delivery — `SYNTH-ROUTE-DELIVERY-AUTHORIZATION-001@r1`; `synthetic-route-delivery-authority-owner`; `synthetic-route-delivery-decision-authority@r1`; `SYNTH-ROUTE-DELIVERY-TRACE-001@r1`; `SYNTH-ROUTE-DELIVERY-RECEIPT-001@r1`; `synthetic-content:route-delivery-receipt-delivered-no-acknowledgment-001-r1`
- acknowledgment — `SYNTH-ROUTE-ACKNOWLEDGMENT-AUTHORIZATION-001@r1`; `synthetic-route-acknowledgment-authority-owner`; `synthetic-route-acknowledgment-decision-authority@r1`; `SYNTH-ROUTE-ACKNOWLEDGMENT-TRACE-001@r1`; `SYNTH-ROUTE-ACKNOWLEDGMENT-RECEIPT-001@r1`; `synthetic-content:route-acknowledgment-receipt-acknowledged-no-intake-001-r1`
- intake — `SYNTH-ROUTE-INTAKE-AUTHORIZATION-001@r1`; `synthetic-destination-owner`; `synthetic-destination-pointer-intake-execution-authority@r1`; `SYNTH-ROUTE-INTAKE-TRACE-001@r1`; `SYNTH-ROUTE-INTAKE-RECEIPT-001@r1`; `synthetic-content:route-intake-receipt-intaken-no-candidate-001-r1`
- native-content copy — `SYNTH-ROUTE-NATIVE-CONTENT-COPY-AUTHORIZATION-001@r1`; `synthetic-destination-owner`; `synthetic-destination-native-content-copy-execution-authority@r1`; `SYNTH-ROUTE-NATIVE-CONTENT-COPY-TRACE-001@r1`; `SYNTH-ROUTE-NATIVE-CONTENT-COPY-RECEIPT-001@r1`; `synthetic-content:route-native-content-copy-receipt-copied-no-candidate-001-r1`

The consumed destination-state lineage remains:

- admission — `SYNTH-DESTINATION-CANDIDATE-ADMISSION-AUTHORITY-001@r1`; signer `synthetic-destination-owner`; scope `synthetic-destination-candidate-admission-decision-authority@r1`; decider `synthetic-destination-candidate-admission-decider`; decision `SYNTH-DESTINATION-CANDIDATE-ADMISSION-DECISION-001@r1` at `2026-08-27T21:20:12Z`; content `synthetic-content:destination-candidate-admission-decision-001-r1`
- defer — `SYNTH-DESTINATION-CANDIDATE-DISPOSITION-AUTHORITY-001@r1`; signer `synthetic-destination-owner`; scope `synthetic-destination-candidate-disposition-decision-authority@r1`; decider `synthetic-destination-candidate-disposition-decider`; decision `SYNTH-DESTINATION-CANDIDATE-DISPOSITION-DECISION-001@r1` at `2026-08-27T21:35:12Z`; content `synthetic-content:destination-candidate-defer-disposition-decision-001-r1`
- rejection — `SYNTH-DESTINATION-CANDIDATE-RECONSIDERATION-AUTHORITY-001@r1`; signer `synthetic-destination-owner`; scope `synthetic-destination-candidate-reconsideration-decision-authority@r1`; decider `synthetic-destination-candidate-reconsideration-decider`; decision `SYNTH-DESTINATION-CANDIDATE-RECONSIDERATION-DECISION-001@r1` at `2026-08-27T21:50:12Z`; content `synthetic-content:destination-candidate-rejection-decision-001-r1`
- reopen — `SYNTH-DESTINATION-CANDIDATE-REOPEN-AUTHORITY-001@r1`; signer `synthetic-destination-owner`; scope `synthetic-destination-candidate-reopen-decision-authority@r1`; decider `synthetic-destination-candidate-reopen-decider`; decision `SYNTH-DESTINATION-CANDIDATE-REOPEN-DECISION-001@r1` at `2026-08-27T22:10:12Z`; content `synthetic-content:destination-candidate-reopen-decision-001-r1`
- re-defer — `SYNTH-DESTINATION-CANDIDATE-REOPEN-REVIEW-AUTHORITY-001@r1`; signer `synthetic-destination-owner`; scope `synthetic-destination-candidate-reopen-review-decision-authority@r1`; decider `synthetic-destination-candidate-reopen-review-decider`; decision `SYNTH-DESTINATION-CANDIDATE-REOPEN-REVIEW-DECISION-001@r1` at `2026-08-27T22:25:12Z`; content `synthetic-content:destination-candidate-reopen-review-redefer-decision-001-r1`

Every authority above is consumed and every named content checksum remains valid.

## Transfer Requests, Acceptance, And Authorized Transfer

Request `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-001@r1`, signed at `2026-08-27T22:30:12Z` by `synthetic-transfer-requester` under `synthetic-transfer-request-creation-authority@r1`, content `synthetic-content:destination-candidate-transfer-request-001-r1`, remains refused by consumed review authority `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-AUTHORITY-001@r1` and decision `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-001@r1`: `transfer_request_not_admitted_missing_receiving_owner_acceptance_and_authority`.

Interest `SYNTH-RECEIVING-OWNER-TRANSFER-INTEREST-001@r1`, signed at `2026-08-27T22:40:12Z` by `synthetic-receiving-owner-liaison` under `synthetic-receiving-owner-interest-record-creation-authority@r1`, content `synthetic-content:receiving-owner-transfer-interest-001-r1`, remains non-operative. Request `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-002@r1`, signed at `2026-08-27T22:42:12Z` by `synthetic-transfer-requester` under `synthetic-transfer-request-creation-authority@r1`, content `synthetic-content:destination-candidate-transfer-request-002-r1`, remains refused by consumed review authority `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-AUTHORITY-002@r1` and decision `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-002@r1`: `renewed_transfer_request_not_admitted_interest_is_not_acceptance_and_transfer_authority_absent`.

Acceptance `SYNTH-RECEIVING-OWNER-TRANSFER-ACCEPTANCE-001@r1`, signed at `2026-08-27T22:50:12Z` by `synthetic-receiving-owner-acceptance-decider` under `synthetic-receiving-owner-transfer-acceptance-decision-authority@r1`, content `synthetic-content:receiving-owner-transfer-acceptance-001-r1`, accepts the unchanged scope and frozen risks but grants no execution authority. Review authority `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-AUTHORITY-003@r1`, signed at `2026-08-27T22:52:12Z` by `synthetic-destination-owner` under `synthetic-destination-candidate-transfer-request-review-decision-authority@r1`, authorizes only `synthetic-destination-candidate-transfer-request-reviewer`. Its signed decision `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-003@r1` at `2026-08-27T22:55:12Z`, content `synthetic-content:destination-candidate-transfer-request-review-refusal-decision-003-r1`, records `transfer_request_not_admitted_acceptance_present_but_transfer_authority_absent`. All request, interest, acceptance, review, and refusal checksums are valid; all three review authorities are consumed.

Transfer authority `SYNTH-DESTINATION-CANDIDATE-TRANSFER-EXECUTION-AUTHORITY-001@r1`, signed at `2026-08-27T23:00:12Z` by `synthetic-destination-owner` under `synthetic-destination-candidate-transfer-execution-authority@r1`, authorizes only `synthetic-destination-candidate-transfer-executor`. Decision `SYNTH-DESTINATION-CANDIDATE-TRANSFER-DECISION-001@r1` at `2026-08-27T23:02:12Z`, content `synthetic-content:destination-candidate-transfer-decision-001-r1`, trace `SYNTH-DESTINATION-CANDIDATE-TRANSFER-TRACE-001@r1`, and receipt `SYNTH-DESTINATION-CANDIDATE-TRANSFER-RECEIPT-001@r1` at `2026-08-27T23:05:12Z`, content `synthetic-content:destination-candidate-transfer-receipt-001-r1`, are valid. The transfer authority is consumed; prepared return remains `synthetic_transfer_record_only`.

## Graduation Proposal

At `2026-08-27T23:10:12Z`, `SYNTH-GRADUATION-PROPOSAL-001@r1` is signed by `synthetic-graduation-proposer` under `synthetic-graduation-proposal-record-creation-authority@r1`. Content `synthetic-content:graduation-proposal-001-r1` has a valid checksum. The proposal pins the unchanged candidate, transfer receipt, both owners, source and evidence provenance, unresolved authority-laundering, scope-drift, custody-loss, and premature-deployment risks, maintenance owner `synthetic-receiving-owner`, correction owner `synthetic-mechanism-map-owner`, revocation, no action, and an explicit no-graduation-execution boundary. Proposal creation grants no acceptance or execution authority.

## Destination-Owner Review Authority And Acceptance

At `2026-08-27T23:12:12Z`, review authority `SYNTH-DESTINATION-OWNER-GRADUATION-PROPOSAL-REVIEW-AUTHORITY-001@r1` is signed by `synthetic-receiving-owner` under `synthetic-destination-owner-graduation-proposal-review-decision-authority@r1`. It authorizes only `synthetic-destination-owner-graduation-proposal-reviewer` once to accept or refuse the proposal after verifying the full lineage, transfer receipt and checksum, destination-owner fit, unresolved risks, maintenance and correction custody, no revocation, and unconsumed authority. It authorizes no graduation execution, deployment, performance, publication, contact, real-owner effect, or external action.

At `2026-08-27T23:15:12Z`, every check matched. Decision `SYNTH-DESTINATION-OWNER-GRADUATION-PROPOSAL-REVIEW-DECISION-001@r1` is signed by that reviewer and records `graduation_proposal_accepted_execution_authority_absent`. Content `synthetic-content:destination-owner-graduation-proposal-review-decision-001-r1` has a valid checksum. The one-use review authority is consumed. Process state becomes `graduation_proposal_accepted_not_graduated`; prepared return is `synthetic_graduation_proposal_acceptance_record_only`.

## Unresolved Risk, Maintenance, And Legitimacy

Unresolved authority-laundering, scope-drift, custody-loss, and premature-deployment risks remain explicit. `synthetic-receiving-owner` owns maintenance; `synthetic-mechanism-map-owner` owns correction. Affected-party standing is synthetic and creates no representation claim. Legitimacy depends on exact source, candidate, transfer, risk, owner, proposal, authority, decision, content, checksum, revocation, and no-action custody. Acceptance cannot erase risk or grant execution.

## Stops, Correction, Recovery, And Reopen

Stop on any named source, candidate, owner, risk, proposal, transfer receipt, authority, decision, content ID, checksum, or revocation change. Failure modes include transfer treated as graduation, proposal treated as acceptance, acceptance treated as execution, review authority reused, risks erased, or a real downstream effect invented. Failed review recovery retracts only the proposal-review decision, preserves the proposal and all transfer evidence, restores `destination_candidate_transferred_not_graduated`, and changes no real owner or candidate. Exact next wake is exact graduation execution authority and an authorized graduation decision under the frozen accepted proposal, or any named revision.

## Prepared Return And Downstream Nonperformance

Prepared return is `synthetic_graduation_proposal_acceptance_record_only`. No graduation execution authority, graduation decision, graduation trace, graduation receipt, deployment, performance, publication, contact, real-owner effect, or external action exists.

## Frontier Verification

Repository integration verified native frontmatter and exact section topology; no action and both pointer routes; complete execution, destination-state, request-review, acceptance, and transfer custody; concrete unresolved-risk custody; exact proposal and review authority; acceptance decision; recovery; non-effects; and exact wake. `CMD-0001`, P8, real candidate status, real disposition, transfer, graduation, deployment, schedule, and external-action state remain unchanged.
