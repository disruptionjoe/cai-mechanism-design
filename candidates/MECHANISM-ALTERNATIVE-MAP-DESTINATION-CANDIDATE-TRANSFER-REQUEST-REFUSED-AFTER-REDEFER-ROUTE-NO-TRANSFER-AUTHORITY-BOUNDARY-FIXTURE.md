---
artifact_type: synthetic_mechanism_alternative_map_destination_candidate_transfer_request_refused_after_redefer_route_no_transfer_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Mechanism Alternative-Map Destination-Candidate-Transfer-Request-Refused-After-Redefer Route No-Transfer-Authority Boundary Fixture

## Use Boundary

This synthetic fixture preserves no action, both pointer routes, the complete
comparison-through-native-content-copy lineage, destination admission,
historical defer, rejection, reopen, and current re-defer. It adds one transfer
request and one separately authorized review decision that refuses to admit
the request because receiving-owner acceptance and transfer authority are
absent. A request is evidence, not an instruction. Refusal is not rejection of
the candidate, acceptance, Mechanism Design admission or disposition,
transfer, graduation, deployment, performance, target-native effect outside
this fixture, or external action. It does not modify `CMD-0001` or create P8.

## Map Header

| Field | Value |
| --- | --- |
| `map_id` | `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REFUSED-AFTER-REDEFER-MAP-001@r1` |
| `source_inquiry` | `SYNTH-SOURCE-OPENED-ROUTE-NO-DELIVERY-001@r1` |
| `source_revision` | `synthetic-source-revision:opened-route-no-delivery-001-r1` |
| `candidate_or_problem_ref` | `SYNTH-PROBLEM-OPENED-ROUTE-NO-DELIVERY-001@r1`; Mechanism Design candidate scope `none` |
| `map_owner` | `synthetic-mechanism-map-owner` |
| `authorization_ref` | `synthetic://decision-boundary/SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-001@r1` |
| `external_action` | `none` |

## Frozen Inquiry And Mechanism Design Candidate Boundary

The source, problem, immutable payload, alternatives, comparison, selection,
destination acceptance, six consumed execution grants, destination candidate
admission, historical defer, rejection, reopen, and current re-defer remain
unchanged. Destination candidate `SYNTH-DESTINATION-CANDIDATE-001@r1` retains
its checksum. Existing-owner fit remains `synthetic-destination-owner` and
defeats Mechanism Design admission; Mechanism Design candidate scope is
`none`. Historical defer, rejection, reopen, and re-defer remain visible. The
request and refusal change no candidate or route state.

## Alternative Records

- `SYNTH-ALT-OPENED-NO-ACTION-001@r1` preserves no action.
- `SYNTH-ALT-OPENED-IMMEDIATE-001@r1` preserves the selected immediate pointer route.
- `SYNTH-ALT-OPENED-VERIFIED-001@r1` remains materially distinct dominated evidence on required timing.

Both pointer routes remain visible; the request and refusal erase none of the
comparison, selection, execution, admission, defer, rejection, reopen, or
re-defer records.

## Material Difference And Nonduplication

Transfer-request review after re-defer is distinct from candidate disposition.
Request `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-001@r1` is non-operative
evidence. Decision
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-001@r1`
records
`transfer_request_not_admitted_missing_receiving_owner_acceptance_and_authority`.
One-use review authority prevents duplicate execution. Route state remains
`destination_candidate_redeferred_no_transfer`; prepared return is
`transfer_request_refusal_record_only`.

## Existing-Owner Fit

The immutable payload `SYNTH-NATIVE-CONTENT-PAYLOAD-001@r1`, content ID
`synthetic-content:native-content-payload-001-r1`, destination candidate, and
all destination dispositions remain inside `synthetic-destination-owner`.
Neither a request nor its refusal changes owner fit, grants Mechanism Design
authority, or establishes receiving-owner acceptance, accepted scope,
unresolved-risk acknowledgment, result acceptance, or transfer authority.

## Evidence, Affected Parties, And Legitimacy

At `2026-08-27T22:30:12Z`, request
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-001@r1` is signed by
`synthetic-transfer-requester` under
`synthetic-transfer-request-creation-authority@r1`. Content ID
`synthetic-content:destination-candidate-transfer-request-001-r1` has a valid
checksum. It asks to transfer the unchanged re-deferred candidate to
`synthetic-receiving-owner` but supplies no receiving-owner acceptance,
accepted scope, unresolved-risk acknowledgment, transfer decision authority,
or transfer decision. It changes no state and grants no authority.

At `2026-08-27T22:32:12Z`, review authority
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-AUTHORITY-001@r1` is
signed by `synthetic-destination-owner` under
`synthetic-destination-candidate-transfer-request-review-decision-authority@r1`.
It authorizes only `synthetic-destination-candidate-transfer-request-reviewer`
once to record request admissibility after verifying the complete frozen
lineage, unchanged candidate and checksum, request and checksum, absent
receiving-owner acceptance, absent accepted scope and risk acknowledgment,
absent transfer authority and decision, and unconsumed review authority. It
authorizes no candidate disposition, transfer, acceptance, graduation,
deployment, performance, or external action. All actors, evidence, authority,
and systems are synthetic. Correction belongs to
`synthetic-mechanism-map-owner`; the legitimacy risk is authority laundering.

## Comparison Through Destination Redefer Boundary

Comparison `SYNTH-CONDITION-IMMEDIATE-REQUIRED-006@r1`, selection
`SYNTH-ROUTE-SELECTION-IMMEDIATE-004@r1`, and destination acceptance
`SYNTH-DESTINATION-ACCEPTANCE-IMMEDIATE-003@r1` retain their original signers
and scopes. The complete consumed execution lineage is:

- opening — `SYNTH-ROUTE-OPENING-AUTHORIZATION-002@r1`; `synthetic-route-opening-authority-owner`; `synthetic-route-opening-decision-authority@r1`; `SYNTH-ROUTE-OPENING-TRACE-001@r1`; `SYNTH-ROUTE-OPENING-RECEIPT-001@r1`; `synthetic-content:route-opening-receipt-opened-no-delivery-001-r1`
- sending — `SYNTH-ROUTE-SENDING-AUTHORIZATION-001@r1`; `synthetic-route-sending-authority-owner`; `synthetic-route-sending-decision-authority@r1`; `SYNTH-ROUTE-SENDING-TRACE-001@r1`; `SYNTH-ROUTE-SENDING-RECEIPT-001@r1`; `synthetic-content:route-sending-receipt-sent-no-delivery-001-r1`
- delivery — `SYNTH-ROUTE-DELIVERY-AUTHORIZATION-001@r1`; `synthetic-route-delivery-authority-owner`; `synthetic-route-delivery-decision-authority@r1`; `SYNTH-ROUTE-DELIVERY-TRACE-001@r1`; `SYNTH-ROUTE-DELIVERY-RECEIPT-001@r1`; `synthetic-content:route-delivery-receipt-delivered-no-acknowledgment-001-r1`
- acknowledgment — `SYNTH-ROUTE-ACKNOWLEDGMENT-AUTHORIZATION-001@r1`; `synthetic-route-acknowledgment-authority-owner`; `synthetic-route-acknowledgment-decision-authority@r1`; `SYNTH-ROUTE-ACKNOWLEDGMENT-TRACE-001@r1`; `SYNTH-ROUTE-ACKNOWLEDGMENT-RECEIPT-001@r1`; `synthetic-content:route-acknowledgment-receipt-acknowledged-no-intake-001-r1`
- intake — `SYNTH-ROUTE-INTAKE-AUTHORIZATION-001@r1`; `synthetic-destination-owner`; `synthetic-destination-pointer-intake-execution-authority@r1`; `SYNTH-ROUTE-INTAKE-TRACE-001@r1`; `SYNTH-ROUTE-INTAKE-RECEIPT-001@r1`; `synthetic-content:route-intake-receipt-intaken-no-candidate-001-r1`
- native-content copy — `SYNTH-ROUTE-NATIVE-CONTENT-COPY-AUTHORIZATION-001@r1`; `synthetic-destination-owner`; `synthetic-destination-native-content-copy-execution-authority@r1`; `SYNTH-ROUTE-NATIVE-CONTENT-COPY-TRACE-001@r1`; `SYNTH-ROUTE-NATIVE-CONTENT-COPY-RECEIPT-001@r1`; `synthetic-content:route-native-content-copy-receipt-copied-no-candidate-001-r1`

All six grants are consumed and all receipt checksums remain valid. Admission
authority `SYNTH-DESTINATION-CANDIDATE-ADMISSION-AUTHORITY-001@r1` was consumed
when `synthetic-destination-candidate-admission-decider` signed
`SYNTH-DESTINATION-CANDIDATE-ADMISSION-DECISION-001@r1`; content ID
`synthetic-content:destination-candidate-admission-decision-001-r1` is valid.
The later consumed destination-state lineage is:

- defer — `SYNTH-DESTINATION-CANDIDATE-DISPOSITION-AUTHORITY-001@r1`; `synthetic-destination-owner`; `synthetic-destination-candidate-disposition-decision-authority@r1`; `synthetic-destination-candidate-disposition-decider`; `SYNTH-DESTINATION-CANDIDATE-DISPOSITION-DECISION-001@r1`; `synthetic-content:destination-candidate-defer-disposition-decision-001-r1`
- rejection — `SYNTH-DESTINATION-CANDIDATE-RECONSIDERATION-AUTHORITY-001@r1`; `synthetic-destination-owner`; its reconsideration scope and authorized decider; `SYNTH-DESTINATION-CANDIDATE-RECONSIDERATION-DECISION-001@r1`; `synthetic-content:destination-candidate-rejection-decision-001-r1`
- reopen — `SYNTH-DESTINATION-CANDIDATE-REOPEN-AUTHORITY-001@r1`; `synthetic-destination-owner`; `synthetic-destination-candidate-reopen-decision-authority@r1`; `synthetic-destination-candidate-reopen-decider`; `SYNTH-DESTINATION-CANDIDATE-REOPEN-DECISION-001@r1`; `synthetic-content:destination-candidate-reopen-decision-001-r1`
- re-defer review — `SYNTH-DESTINATION-CANDIDATE-REOPEN-REVIEW-AUTHORITY-001@r1`; `synthetic-destination-owner`; `synthetic-destination-candidate-reopen-review-decision-authority@r1`; `synthetic-destination-candidate-reopen-review-decider`; `SYNTH-DESTINATION-CANDIDATE-REOPEN-REVIEW-DECISION-001@r1`; `synthetic-content:destination-candidate-reopen-review-redefer-decision-001-r1`

## Transfer Request, Review Refusal, And Downstream Nonperformance

At `2026-08-27T22:35:12Z`, every review check matched. Decision
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-001@r1` is
signed by `synthetic-destination-candidate-transfer-request-reviewer` and
records
`transfer_request_not_admitted_missing_receiving_owner_acceptance_and_authority`.
Content ID
`synthetic-content:destination-candidate-transfer-request-review-refusal-decision-001-r1`
has a valid checksum; review authority is consumed. Route state remains
`destination_candidate_redeferred_no_transfer`; the request remains
non-operative evidence; no downstream record exists.

## Prepared Return And Recovery

Prepared return is `transfer_request_refusal_record_only`. Stop on any named
fact or risk revision. Failure modes include request treated as instruction,
refusal treated as candidate rejection, receiving-owner acceptance invented,
prior authority reused, history erased, or downstream effect invented. Failed
review recovery retracts only the request-review decision, leaves the request
as non-operative evidence, restores unreviewed-request state, and changes no
candidate. Exact next wake is exact receiving-owner acceptance plus transfer authority under frozen refused-request records, materially new destination-owner evidence, or a revision to any named fact.

## Frontier Verification

Verify every frozen map, alternative, signer, decider, authority scope, actor,
trace, receipt, content ID, checksum, consumed grant, admission, defer,
rejection, reopen, re-defer, request, review authority, and refusal. Confirm
the request remains evidence; route state remains re-deferred; and no
Mechanism Design candidate, disposition, result acceptance, transfer,
graduation, deployment, target-native effect, or external action was created.
