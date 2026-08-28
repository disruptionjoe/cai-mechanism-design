# Execute one synthetic transfer after exact acceptance and transfer authority

## Boundary

Write one complete synthetic Mechanism Design process fixture from only the
embedded evidence. Preserve no action, both pointer routes, the complete
execution and destination-state lineage, all three prior transfer-request
reviews and refusals, the receiving-owner interest notice, the exact
receiving-owner acceptance, and current route state
`destination_candidate_redeferred_no_transfer`. Add one exact one-use transfer
execution authority, one authorized synthetic transfer decision, and its
trace and receipt. This changes only synthetic route state inside the fixture
to `destination_candidate_transferred_not_graduated`. It is not Mechanism
Design admission or disposition, graduation, deployment, performance,
publication, contact, a target-native effect outside the fixture, or external
action. Do not modify `CMD-0001` or create P8. External action is `none`.

## Frozen evidence

Use `GOVERNANCE.md`,
`interfaces/DESTINATION-OWNER-SYNTHETIC-REVIEW-REQUEST-TEMPLATE.md`,
`candidates/MECHANISM-ALTERNATIVE-MAP-TEMPLATE.md`, and
`candidates/MECHANISM-ALTERNATIVE-MAP-DESTINATION-CANDIDATE-RECEIVING-OWNER-ACCEPTANCE-NO-TRANSFER-AUTHORITY-BOUNDARY-FIXTURE.md`.
Freeze map
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-AFTER-ACCEPTANCE-MAP-001@r1`;
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
`synthetic-destination-owner`; receiving owner `synthetic-receiving-owner`;
Mechanism Design candidate scope `none`.

In the section that consumes it, copy this literal execution lineage:

- opening — `SYNTH-ROUTE-OPENING-AUTHORIZATION-002@r1`; `synthetic-route-opening-authority-owner`; `synthetic-route-opening-decision-authority@r1`; `SYNTH-ROUTE-OPENING-TRACE-001@r1`; `SYNTH-ROUTE-OPENING-RECEIPT-001@r1`; `synthetic-content:route-opening-receipt-opened-no-delivery-001-r1`
- sending — `SYNTH-ROUTE-SENDING-AUTHORIZATION-001@r1`; `synthetic-route-sending-authority-owner`; `synthetic-route-sending-decision-authority@r1`; `SYNTH-ROUTE-SENDING-TRACE-001@r1`; `SYNTH-ROUTE-SENDING-RECEIPT-001@r1`; `synthetic-content:route-sending-receipt-sent-no-delivery-001-r1`
- delivery — `SYNTH-ROUTE-DELIVERY-AUTHORIZATION-001@r1`; `synthetic-route-delivery-authority-owner`; `synthetic-route-delivery-decision-authority@r1`; `SYNTH-ROUTE-DELIVERY-TRACE-001@r1`; `SYNTH-ROUTE-DELIVERY-RECEIPT-001@r1`; `synthetic-content:route-delivery-receipt-delivered-no-acknowledgment-001-r1`
- acknowledgment — `SYNTH-ROUTE-ACKNOWLEDGMENT-AUTHORIZATION-001@r1`; `synthetic-route-acknowledgment-authority-owner`; `synthetic-route-acknowledgment-decision-authority@r1`; `SYNTH-ROUTE-ACKNOWLEDGMENT-TRACE-001@r1`; `SYNTH-ROUTE-ACKNOWLEDGMENT-RECEIPT-001@r1`; `synthetic-content:route-acknowledgment-receipt-acknowledged-no-intake-001-r1`
- intake — `SYNTH-ROUTE-INTAKE-AUTHORIZATION-001@r1`; `synthetic-destination-owner`; `synthetic-destination-pointer-intake-execution-authority@r1`; `SYNTH-ROUTE-INTAKE-TRACE-001@r1`; `SYNTH-ROUTE-INTAKE-RECEIPT-001@r1`; `synthetic-content:route-intake-receipt-intaken-no-candidate-001-r1`
- native-content copy — `SYNTH-ROUTE-NATIVE-CONTENT-COPY-AUTHORIZATION-001@r1`; `synthetic-destination-owner`; `synthetic-destination-native-content-copy-execution-authority@r1`; `SYNTH-ROUTE-NATIVE-CONTENT-COPY-TRACE-001@r1`; `SYNTH-ROUTE-NATIVE-CONTENT-COPY-RECEIPT-001@r1`; `synthetic-content:route-native-content-copy-receipt-copied-no-candidate-001-r1`

All six grants are consumed. In the section that consumes destination state,
copy this literal predecessor-custody block:

- admission — `SYNTH-DESTINATION-CANDIDATE-ADMISSION-AUTHORITY-001@r1`; signer `synthetic-destination-owner`; scope `synthetic-destination-candidate-admission-decision-authority@r1`; decider `synthetic-destination-candidate-admission-decider`; decision `SYNTH-DESTINATION-CANDIDATE-ADMISSION-DECISION-001@r1` at `2026-08-27T21:20:12Z`; content `synthetic-content:destination-candidate-admission-decision-001-r1`; consumed
- defer — `SYNTH-DESTINATION-CANDIDATE-DISPOSITION-AUTHORITY-001@r1`; signer `synthetic-destination-owner`; scope `synthetic-destination-candidate-disposition-decision-authority@r1`; decider `synthetic-destination-candidate-disposition-decider`; decision `SYNTH-DESTINATION-CANDIDATE-DISPOSITION-DECISION-001@r1` at `2026-08-27T21:35:12Z`; content `synthetic-content:destination-candidate-defer-disposition-decision-001-r1`; consumed
- rejection — `SYNTH-DESTINATION-CANDIDATE-RECONSIDERATION-AUTHORITY-001@r1`; signer `synthetic-destination-owner`; scope `synthetic-destination-candidate-reconsideration-decision-authority@r1`; decider `synthetic-destination-candidate-reconsideration-decider`; decision `SYNTH-DESTINATION-CANDIDATE-RECONSIDERATION-DECISION-001@r1` at `2026-08-27T21:50:12Z`; content `synthetic-content:destination-candidate-rejection-decision-001-r1`; consumed
- reopen — `SYNTH-DESTINATION-CANDIDATE-REOPEN-AUTHORITY-001@r1`; signer `synthetic-destination-owner`; scope `synthetic-destination-candidate-reopen-decision-authority@r1`; decider `synthetic-destination-candidate-reopen-decider`; decision `SYNTH-DESTINATION-CANDIDATE-REOPEN-DECISION-001@r1` at `2026-08-27T22:10:12Z`; content `synthetic-content:destination-candidate-reopen-decision-001-r1`; consumed
- re-defer — `SYNTH-DESTINATION-CANDIDATE-REOPEN-REVIEW-AUTHORITY-001@r1`; signer `synthetic-destination-owner`; scope `synthetic-destination-candidate-reopen-review-decision-authority@r1`; decider `synthetic-destination-candidate-reopen-review-decider`; decision `SYNTH-DESTINATION-CANDIDATE-REOPEN-REVIEW-DECISION-001@r1` at `2026-08-27T22:25:12Z`; content `synthetic-content:destination-candidate-reopen-review-redefer-decision-001-r1`; consumed

Preserve request `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-001@r1`
and refusal `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-001@r1`;
interest `SYNTH-RECEIVING-OWNER-TRANSFER-INTEREST-001@r1`, request
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-002@r1`, and refusal
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-002@r1`;
acceptance `SYNTH-RECEIVING-OWNER-TRANSFER-ACCEPTANCE-001@r1`; and refusal
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-003@r1`.
All three review authorities are consumed. The third refusal remains
`transfer_request_not_admitted_acceptance_present_but_transfer_authority_absent`.

At `2026-08-27T23:00:12Z`, transfer execution authority
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-EXECUTION-AUTHORITY-001@r1` is signed by
`synthetic-destination-owner` under
`synthetic-destination-candidate-transfer-execution-authority@r1`. It
authorizes only `synthetic-destination-candidate-transfer-executor` once to
transfer the unchanged synthetic candidate and its frozen unresolved-risk
package to `synthetic-receiving-owner` after verifying every predecessor,
exact acceptance, both owner identifiers, unchanged scope and checksum, no
revocation, and unconsumed authority. It authorizes no graduation, deployment,
performance, publication, contact, real-owner effect, or external action.

At `2026-08-27T23:02:12Z`, decision
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-DECISION-001@r1` is signed by that
executor and records `transfer_accepted_synthetic_candidate_under_exact_authority`.
Content ID `synthetic-content:destination-candidate-transfer-decision-001-r1`
has a valid checksum. At `2026-08-27T23:05:12Z`, trace
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-TRACE-001@r1` and receipt
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-RECEIPT-001@r1` record only the synthetic
state transition; receipt content ID
`synthetic-content:destination-candidate-transfer-receipt-001-r1` has a valid
checksum. The one-use authority is consumed. Route state becomes
`destination_candidate_transferred_not_graduated`; prepared return is
`synthetic_transfer_record_only`.

Correction owner is `synthetic-mechanism-map-owner`. Stop on any named fact,
scope, acceptance, authority, trace, receipt, checksum, or risk revision.
Failure modes include acceptance treated as authority, authority reused,
transfer treated as graduation or deployment, frozen history erased, or a
real downstream effect invented. Failed transfer recovery retracts only the
transfer decision, trace, and receipt; preserves all predecessor evidence and
acceptance; restores `destination_candidate_redeferred_no_transfer`; and
changes no real owner or candidate. Exact next wake is exact graduation-review
authority and destination-owner graduation acceptance under the frozen
transfer receipt, materially new owner evidence, or any named revision.

## Work now

Draft
`candidates/MECHANISM-ALTERNATIVE-MAP-DESTINATION-CANDIDATE-TRANSFERRED-AFTER-ACCEPTANCE-NO-GRADUATION-AUTHORITY-BOUNDARY-FIXTURE.md`
with exactly this frontmatter:

---
artifact_type: synthetic_mechanism_alternative_map_destination_candidate_transferred_after_acceptance_no_graduation_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

Use title `# Synthetic Mechanism Alternative-Map Destination-Candidate Transferred-After-Acceptance No-Graduation-Authority Boundary Fixture`
and exactly these `##` sections: `Use Boundary`, `Map Header`, `Frozen
Inquiry And Mechanism Design Candidate Boundary`, `Alternative Records`,
`Material Difference And Nonduplication`, `Existing-Owner Fit`, `Evidence,
Affected Parties, And Legitimacy`, `Comparison Through Transfer-Request
Refusals`, `Authorized Transfer And Downstream Nonperformance`, `Prepared
Return And Recovery`, and `Frontier Verification`. Preserve every identifier,
timestamp, signer, decider, authority scope, trace, receipt, content ID,
checksum, historical state, stop, failure mode, correction, recovery,
non-effect, and exact wake. Return only the finished artifact. First line must
be `---`; do not use a code fence; copy the literal frontmatter exactly; and
use `##` for every named body section.
