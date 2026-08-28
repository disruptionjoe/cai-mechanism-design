---
artifact_type: synthetic_graduation_performance_publication_request_refused_no_publication_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Graduation Performance Publication Request Refused No-Publication-Authority Boundary Fixture

## Use Boundary

This fixture preserves the complete synthetic performed-but-not-published
lineage and adds one non-operative publication request, one exact one-use
request-review authority, and one authorized refusal because publication
execution authority is absent. Process state remains
`performed_not_published`. A request and its review are not publication,
contact, a real owner effect, posting, sending, or external action. `CMD-0001`
is unchanged and P8 is not created. External action is `none`.

## Frozen Performance And Predecessor Custody

The frozen predecessor is
`GRADUATION-PERFORMANCE-AUTHORIZED-NO-PUBLICATION-AUTHORITY-BOUNDARY-FIXTURE.md`
under `GOVERNANCE.md` and the destination-owner synthetic-review request
template. Its complete route, destination, transfer, proposal, graduation,
deployment, and performance lineage remains frozen. Every named predecessor
authority remains consumed, every named checksum remains valid, and the
earlier deployment-request refusal remains valid history.

| Key | Frozen value |
| --- | --- |
| `map` | `SYNTH-DESTINATION-CANDIDATE-TRANSFER-AFTER-ACCEPTANCE-MAP-001@r1` |
| `source` | `SYNTH-SOURCE-OPENED-ROUTE-NO-DELIVERY-001@r1` |
| `source_revision` | `synthetic-source-revision:opened-route-no-delivery-001-r1` |
| `problem` | `SYNTH-PROBLEM-OPENED-ROUTE-NO-DELIVERY-001@r1` |
| `payload` | `SYNTH-NATIVE-CONTENT-PAYLOAD-001@r1` |
| `payload_content` | `synthetic-content:native-content-payload-001-r1` |
| `destination_candidate` | `SYNTH-DESTINATION-CANDIDATE-001@r1` |
| `existing_owner` | `synthetic-destination-owner` |
| `receiving_owner` | `synthetic-receiving-owner` |
| `mechanism_design_candidate_scope` | `none` |
| `transfer_receipt` | `SYNTH-DESTINATION-CANDIDATE-TRANSFER-RECEIPT-001@r1` |
| `transfer_receipt_content` | `synthetic-content:destination-candidate-transfer-receipt-001-r1` |
| `graduation_receipt` | `SYNTH-GRADUATION-EXECUTION-RECEIPT-001@r1` |
| `graduation_receipt_content` | `synthetic-content:graduation-execution-receipt-001-r1` |
| `deployment_request` | `SYNTH-DEPLOYMENT-REQUEST-001@r1` |
| `deployment_request_content` | `synthetic-content:deployment-request-001-r1` |
| `deployment_request_refusal` | `SYNTH-DEPLOYMENT-REQUEST-REVIEW-DECISION-001@r1` |
| `deployment_authority` | `SYNTH-DEPLOYMENT-EXECUTION-AUTHORITY-001@r1` |
| `deployment_decision` | `SYNTH-DEPLOYMENT-EXECUTION-DECISION-001@r1` |
| `deployment_trace` | `SYNTH-DEPLOYMENT-EXECUTION-TRACE-001@r1` |
| `deployment_receipt` | `SYNTH-DEPLOYMENT-EXECUTION-RECEIPT-001@r1` |
| `deployment_receipt_content` | `synthetic-content:deployment-execution-receipt-001-r1` |
| `performance_receipt` | `SYNTH-PERFORMANCE-EXECUTION-RECEIPT-001@r1` |
| `performance_receipt_content` | `synthetic-content:performance-execution-receipt-001-r1` |
| `current_process_state` | `performed_not_published` |

No-action and alternatives `SYNTH-ALT-OPENED-NO-ACTION-001@r1`,
`SYNTH-ALT-OPENED-IMMEDIATE-001@r1`, and
`SYNTH-ALT-OPENED-VERIFIED-001@r1` remain visible, together with comparison
`SYNTH-CONDITION-IMMEDIATE-REQUIRED-006@r1`, selection
`SYNTH-ROUTE-SELECTION-IMMEDIATE-004@r1`, and destination acceptance
`SYNTH-DESTINATION-ACCEPTANCE-IMMEDIATE-003@r1`.

| Step | Authority; signer; scope; actor | Decision; time; trace; receipt; content |
| --- | --- | --- |
| graduation | `SYNTH-GRADUATION-EXECUTION-AUTHORITY-001@r1`; `synthetic-receiving-owner`; `synthetic-graduation-execution-decision-authority@r1`; `synthetic-graduation-executor` | `SYNTH-GRADUATION-EXECUTION-DECISION-001@r1`; `2026-08-27T23:22:12Z`; `SYNTH-GRADUATION-EXECUTION-TRACE-001@r1`; `SYNTH-GRADUATION-EXECUTION-RECEIPT-001@r1`; `synthetic-content:graduation-execution-receipt-001-r1` |
| deployment request | `synthetic-deployment-request-record-creation-authority@r1`; `synthetic-deployment-requester`; record only; none | `SYNTH-DEPLOYMENT-REQUEST-001@r1`; `2026-08-27T23:30:12Z`; none; none; `synthetic-content:deployment-request-001-r1` |
| request refusal | `SYNTH-DEPLOYMENT-REQUEST-REVIEW-AUTHORITY-001@r1`; `synthetic-receiving-owner`; `synthetic-deployment-request-review-decision-authority@r1`; `synthetic-deployment-request-reviewer` | `SYNTH-DEPLOYMENT-REQUEST-REVIEW-DECISION-001@r1`; `2026-08-27T23:35:12Z`; none; none; `synthetic-content:deployment-request-review-refusal-decision-001-r1` |
| deployment | `SYNTH-DEPLOYMENT-EXECUTION-AUTHORITY-001@r1`; `synthetic-receiving-owner`; `synthetic-deployment-execution-decision-authority@r1`; `synthetic-deployment-executor` | `SYNTH-DEPLOYMENT-EXECUTION-DECISION-001@r1`; `2026-08-27T23:42:12Z`; `SYNTH-DEPLOYMENT-EXECUTION-TRACE-001@r1`; `SYNTH-DEPLOYMENT-EXECUTION-RECEIPT-001@r1`; `synthetic-content:deployment-execution-receipt-001-r1` |
| performance | `SYNTH-PERFORMANCE-EXECUTION-AUTHORITY-001@r1`; `synthetic-receiving-owner`; `synthetic-performance-execution-decision-authority@r1`; `synthetic-performance-executor` | `SYNTH-PERFORMANCE-EXECUTION-DECISION-001@r1`; `2026-08-27T23:52:12Z`; `SYNTH-PERFORMANCE-EXECUTION-TRACE-001@r1`; `SYNTH-PERFORMANCE-EXECUTION-RECEIPT-001@r1`; `synthetic-content:performance-execution-receipt-001-r1` |

Performance authority was issued at `2026-08-27T23:50:12Z`; its decision
content `synthetic-content:performance-execution-decision-001-r1` has a valid
checksum, and its trace and receipt were recorded at
`2026-08-27T23:55:12Z`. Performance authority remains consumed. Performance
did not create publication authority.

## Nonoperative Publication Request

At `2026-08-28T00:00:12Z`, request
`SYNTH-PUBLICATION-REQUEST-001@r1` is signed by
`synthetic-publication-requester` under
`synthetic-publication-request-record-creation-authority@r1`. Content
`synthetic-content:publication-request-001-r1` has a valid checksum. It pins
the frozen performance receipt and requests only a later synthetic publication
decision. It grants no review, publication execution, contact, real-owner,
posting, sending, or external-action authority.

## Publication Request Review Authority And Refusal

At `2026-08-28T00:02:12Z`, review authority
`SYNTH-PUBLICATION-REQUEST-REVIEW-AUTHORITY-001@r1` is signed by
`synthetic-receiving-owner` under
`synthetic-publication-request-review-decision-authority@r1`. It authorizes
only `synthetic-publication-request-reviewer` once to admit or refuse the exact
request after verifying full lineage, performance receipt, unresolved risks,
no revocation, unconsumed review authority, and separate publication execution
authority. It authorizes no publication or downstream action.

At `2026-08-28T00:05:12Z`, lineage checks match but no publication execution
authority exists. Decision
`SYNTH-PUBLICATION-REQUEST-REVIEW-DECISION-001@r1`, signed by the authorized
reviewer, records
`publication_request_refused_publication_execution_authority_absent`. Content
`synthetic-content:publication-request-review-refusal-decision-001-r1` has a
valid checksum. Review authority is consumed. State remains
`performed_not_published`; prepared return is
`synthetic_publication_request_refusal_record_only`.

## Risk, Maintenance, And Legitimacy

Authority-laundering, scope-drift, custody-loss, premature-publication, and
unvalidated-outcome risks remain explicit. Maintenance owner is
`synthetic-receiving-owner`; correction owner is
`synthetic-mechanism-map-owner`. All actors and evidence are synthetic.
Affected-party standing creates no representation claim. Legitimacy depends
on exact lineage, authority, risk, correction, recovery, nonpublication, and
non-effect custody.

## Stops, Correction, Recovery, And Reopen

Stop on any named predecessor, source, candidate, owner, risk, proposal,
transfer receipt, graduation receipt, deployment request, refusal, authority,
decision, trace, performance receipt, publication request, content ID,
checksum, or revocation change. Failure modes include request treated as
publication authority, review treated as execution, performance treated as
publication, authority reuse, erased risk, custody loss, or invented real
effect. Failed review recovery retracts only the publication-request review
decision, preserves the request and every predecessor, restores the pre-review
`performed_not_published` state, and changes no real owner or candidate.

## Prepared Return And Exact Wake

Prepared return is `synthetic_publication_request_refusal_record_only`. Exact
next wake is exact publication execution authority under the frozen
performance receipt, or any named revision. This fixture supplies neither
publication execution authority nor a publication decision. No publication,
contact, real owner effect, posting, sending, or external action occurred.

## Frontier Verification

Repository integration verifies literal frontmatter and exact section
topology; the complete route, destination, transfer, proposal, graduation,
deployment, performance, request, review, refusal, risk, stop, correction,
recovery, checksum, non-effect, and exact-wake custody. State remains
`performed_not_published`; `CMD-0001`, real P8, and real owner truth remain
unchanged. External action is `none`.
