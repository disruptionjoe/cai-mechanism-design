# Refuse transfer after receiving-owner acceptance without transfer authority

## Boundary

Write one complete synthetic Mechanism Design process fixture from only the
embedded evidence. Preserve no action, both pointer routes, the complete
execution and destination-state lineage, both prior transfer requests and
refusals, the receiving-owner interest notice, and current route state
`destination_candidate_redeferred_no_transfer`. Add one exact receiving-owner
acceptance record and one separately authorized transfer-request review
decision that still refuses transfer because acceptance is not execution
authority and transfer authority remains absent. Evidence and acceptance are
not instructions. Refusal is not rejection, acceptance revocation, Mechanism
Design admission or disposition, transfer, graduation, deployment,
performance, target-native effect outside the fixture, or external action.
Do not modify `CMD-0001` or create P8. External action is `none`.

## Frozen evidence

Use `GOVERNANCE.md`,
`interfaces/DESTINATION-OWNER-SYNTHETIC-REVIEW-REQUEST-TEMPLATE.md`,
`candidates/MECHANISM-ALTERNATIVE-MAP-TEMPLATE.md`, and
`candidates/MECHANISM-ALTERNATIVE-MAP-DESTINATION-CANDIDATE-RECEIVING-OWNER-INTEREST-NO-ACCEPTANCE-OR-TRANSFER-AUTHORITY-BOUNDARY-FIXTURE.md`.
Freeze map `SYNTH-DESTINATION-CANDIDATE-TRANSFER-ACCEPTANCE-NO-AUTHORITY-MAP-001@r1`;
source `SYNTH-SOURCE-OPENED-ROUTE-NO-DELIVERY-001@r1`; source revision
`synthetic-source-revision:opened-route-no-delivery-001-r1`; problem
`SYNTH-PROBLEM-OPENED-ROUTE-NO-DELIVERY-001@r1`; payload
`SYNTH-NATIVE-CONTENT-PAYLOAD-001@r1` and content ID
`synthetic-content:native-content-payload-001-r1`; alternatives
`SYNTH-ALT-OPENED-NO-ACTION-001@r1`,
`SYNTH-ALT-OPENED-IMMEDIATE-001@r1`, and
`SYNTH-ALT-OPENED-VERIFIED-001@r1`; comparison
`SYNTH-CONDITION-IMMEDIATE-REQUIRED-006@r1`; selection
`SYNTH-ROUTE-SELECTION-IMMEDIATE-004@r1`; destination acceptance
`SYNTH-DESTINATION-ACCEPTANCE-IMMEDIATE-003@r1`; destination candidate
`SYNTH-DESTINATION-CANDIDATE-001@r1`; existing-owner fit
`synthetic-destination-owner`; Mechanism Design candidate scope `none`.

Preserve this literal consumed execution lineage:

- opening — `SYNTH-ROUTE-OPENING-AUTHORIZATION-002@r1`; `synthetic-route-opening-authority-owner`; `synthetic-route-opening-decision-authority@r1`; `SYNTH-ROUTE-OPENING-TRACE-001@r1`; `SYNTH-ROUTE-OPENING-RECEIPT-001@r1`; `synthetic-content:route-opening-receipt-opened-no-delivery-001-r1`
- sending — `SYNTH-ROUTE-SENDING-AUTHORIZATION-001@r1`; `synthetic-route-sending-authority-owner`; `synthetic-route-sending-decision-authority@r1`; `SYNTH-ROUTE-SENDING-TRACE-001@r1`; `SYNTH-ROUTE-SENDING-RECEIPT-001@r1`; `synthetic-content:route-sending-receipt-sent-no-delivery-001-r1`
- delivery — `SYNTH-ROUTE-DELIVERY-AUTHORIZATION-001@r1`; `synthetic-route-delivery-authority-owner`; `synthetic-route-delivery-decision-authority@r1`; `SYNTH-ROUTE-DELIVERY-TRACE-001@r1`; `SYNTH-ROUTE-DELIVERY-RECEIPT-001@r1`; `synthetic-content:route-delivery-receipt-delivered-no-acknowledgment-001-r1`
- acknowledgment — `SYNTH-ROUTE-ACKNOWLEDGMENT-AUTHORIZATION-001@r1`; `synthetic-route-acknowledgment-authority-owner`; `synthetic-route-acknowledgment-decision-authority@r1`; `SYNTH-ROUTE-ACKNOWLEDGMENT-TRACE-001@r1`; `SYNTH-ROUTE-ACKNOWLEDGMENT-RECEIPT-001@r1`; `synthetic-content:route-acknowledgment-receipt-acknowledged-no-intake-001-r1`
- intake — `SYNTH-ROUTE-INTAKE-AUTHORIZATION-001@r1`; `synthetic-destination-owner`; `synthetic-destination-pointer-intake-execution-authority@r1`; `SYNTH-ROUTE-INTAKE-TRACE-001@r1`; `SYNTH-ROUTE-INTAKE-RECEIPT-001@r1`; `synthetic-content:route-intake-receipt-intaken-no-candidate-001-r1`
- native-content copy — `SYNTH-ROUTE-NATIVE-CONTENT-COPY-AUTHORIZATION-001@r1`; `synthetic-destination-owner`; `synthetic-destination-native-content-copy-execution-authority@r1`; `SYNTH-ROUTE-NATIVE-CONTENT-COPY-TRACE-001@r1`; `SYNTH-ROUTE-NATIVE-CONTENT-COPY-RECEIPT-001@r1`; `synthetic-content:route-native-content-copy-receipt-copied-no-candidate-001-r1`

All six grants are consumed. Preserve admission, defer, rejection, reopen, and
re-defer authorities, authorized deciders, decisions, content IDs, checksums,
and historical states exactly from the frozen fixture. Preserve first request
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-001@r1`, first refusal
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-001@r1`,
interest `SYNTH-RECEIVING-OWNER-TRANSFER-INTEREST-001@r1`, renewed request
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-002@r1`, and second refusal
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-002@r1`.
Both limited review authorities are consumed. Both requests remain
non-operative. The second refusal record remains
`renewed_transfer_request_not_admitted_interest_is_not_acceptance_and_transfer_authority_absent`.

At `2026-08-27T22:50:12Z`, receiving-owner acceptance
`SYNTH-RECEIVING-OWNER-TRANSFER-ACCEPTANCE-001@r1` is signed by
`synthetic-receiving-owner-acceptance-decider` under
`synthetic-receiving-owner-transfer-acceptance-decision-authority@r1`.
Content ID `synthetic-content:receiving-owner-transfer-acceptance-001-r1` has
a valid checksum. It accepts the unchanged candidate scope and acknowledges
the frozen unresolved risks for possible transfer review. It expressly grants
no transfer execution authority, no permission to change either owner's state,
and no transfer decision.

At `2026-08-27T22:52:12Z`, review authority
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-AUTHORITY-003@r1` is
signed by `synthetic-destination-owner` under
`synthetic-destination-candidate-transfer-request-review-decision-authority@r1`.
It authorizes only
`synthetic-destination-candidate-transfer-request-reviewer` once to verify
the complete frozen lineage, both prior refusals, current acceptance and
checksum, accepted scope and risk acknowledgment, absent transfer execution
authority, absent transfer decision, and unconsumed review authority. It
authorizes no candidate disposition, transfer, acceptance change, graduation,
deployment, performance, or external action.

At `2026-08-27T22:55:12Z`, every check matched. Decision
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-003@r1` is
signed by the authorized reviewer and records
`transfer_request_not_admitted_acceptance_present_but_transfer_authority_absent`.
Content ID
`synthetic-content:destination-candidate-transfer-request-review-refusal-decision-003-r1`
has a valid checksum; review authority is consumed. Route state remains
`destination_candidate_redeferred_no_transfer`; prepared return is
`acceptance_present_transfer_authority_absent_refusal_record_only`; no
downstream record exists.

Correction owner is `synthetic-mechanism-map-owner`. Stop on any named fact or
risk revision. Failure modes include acceptance treated as transfer authority,
review authority treated as execution authority, refusal treated as candidate
rejection or acceptance revocation, prior authority reused, history erased, or
downstream effect invented. Failed review recovery retracts only the third
request-review decision, preserves acceptance as non-operative transfer
evidence, restores acceptance-present/unreviewed state, and changes no
candidate. Exact next wake is exact transfer execution authority plus an
authorized transfer decision under frozen acceptance-and-refusal records,
materially new destination-owner evidence, or a revision to any named fact.

## Work now

Draft
`candidates/MECHANISM-ALTERNATIVE-MAP-DESTINATION-CANDIDATE-RECEIVING-OWNER-ACCEPTANCE-NO-TRANSFER-AUTHORITY-BOUNDARY-FIXTURE.md`
with exactly this frontmatter:

---
artifact_type: synthetic_mechanism_alternative_map_destination_candidate_receiving_owner_acceptance_no_transfer_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

Use title `# Synthetic Mechanism Alternative-Map Destination-Candidate Receiving-Owner-Acceptance No-Transfer-Authority Boundary Fixture`
and exactly these `##` sections: `Use Boundary`, `Map Header`, `Frozen
Inquiry And Mechanism Design Candidate Boundary`, `Alternative Records`,
`Material Difference And Nonduplication`, `Existing-Owner Fit`, `Evidence,
Affected Parties, And Legitimacy`, `Comparison Through Prior Transfer-Request
Refusals`, `Receiving-Owner Acceptance, Review Refusal, And Downstream
Nonperformance`, `Prepared Return And Recovery`, and `Frontier Verification`.
Preserve every identifier, signer, decider, authority scope, trace, receipt,
content ID, checksum, historical state, stop, failure mode, correction,
recovery, non-effect, and exact wake. Return only the finished artifact.
First line must be `---`; do not use a code fence; copy the literal
frontmatter exactly; and use `##` for every named body section.
