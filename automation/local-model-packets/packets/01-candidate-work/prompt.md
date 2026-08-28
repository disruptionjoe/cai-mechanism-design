# Refuse transfer after receiving-owner interest without acceptance or authority

## Boundary

Write one complete synthetic Mechanism Design process fixture from only the
embedded evidence. Preserve no action, both pointer routes, full execution
lineage, destination admission, historical defer, rejection, reopen,
re-defer, the first transfer request, and its refusal. Add one receiving-owner
interest notice, one renewed transfer request, and one separately authorized
review decision that refuses to admit the renewed request because interest is
not acceptance and transfer authority remains absent. Evidence is not an
instruction. Refusal is not rejection, acceptance, Mechanism Design admission
or disposition, transfer, graduation, deployment, performance, target-native
effect outside the fixture, or external action. Do not modify `CMD-0001` or
create P8. External action is `none`.

## Frozen evidence

Use `GOVERNANCE.md`,
`interfaces/DESTINATION-OWNER-SYNTHETIC-REVIEW-REQUEST-TEMPLATE.md`,
`candidates/MECHANISM-ALTERNATIVE-MAP-TEMPLATE.md`, and
`candidates/MECHANISM-ALTERNATIVE-MAP-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REFUSED-AFTER-REDEFER-ROUTE-NO-TRANSFER-AUTHORITY-BOUNDARY-FIXTURE.md`.
Freeze map
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-INTEREST-REFUSED-MAP-001@r1`,
unchanged source, payload, alternatives, comparison, selection, destination
acceptance, all six consumed execution grants, destination admission,
historical defer, rejection, reopen, re-defer, request, review authority, and
first refusal. Existing-owner fit remains `synthetic-destination-owner`;
Mechanism Design candidate scope remains `none`; route state remains
`destination_candidate_redeferred_no_transfer`.

The complete consumed execution lineage is:

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

The first request `SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-001@r1`
and refusal
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-001@r1`
remain valid, consumed, and non-operative. The refusal record is
`transfer_request_not_admitted_missing_receiving_owner_acceptance_and_authority`.

At `2026-08-27T22:40:12Z`, interest notice
`SYNTH-RECEIVING-OWNER-TRANSFER-INTEREST-001@r1` is signed by
`synthetic-receiving-owner-liaison` under
`synthetic-receiving-owner-interest-record-creation-authority@r1`. Content ID
`synthetic-content:receiving-owner-transfer-interest-001-r1` has a valid
checksum. It records willingness to review a future transfer package. It is
not receiving-owner acceptance, accepted scope, unresolved-risk
acknowledgment, transfer authority, or a transfer decision and changes no
state.

At `2026-08-27T22:42:12Z`, renewed request
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-002@r1` is signed by
`synthetic-transfer-requester` under
`synthetic-transfer-request-creation-authority@r1`. Content ID
`synthetic-content:destination-candidate-transfer-request-002-r1` has a valid
checksum. It cites the interest notice but supplies no acceptance, accepted
scope, risk acknowledgment, transfer authority, or transfer decision.

At `2026-08-27T22:44:12Z`, review authority
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-AUTHORITY-002@r1` is
signed by `synthetic-destination-owner` under
`synthetic-destination-candidate-transfer-request-review-decision-authority@r1`.
It authorizes only `synthetic-destination-candidate-transfer-request-reviewer`
once to verify the frozen lineage, first refusal, interest notice, renewed
request, absent acceptance, absent accepted scope and risk acknowledgment,
absent transfer authority and decision, and unconsumed review authority. It
authorizes no candidate disposition, transfer, acceptance, graduation,
deployment, performance, or external action.

At `2026-08-27T22:45:12Z`, every check matched. Decision
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-002@r1` is
signed by the authorized reviewer and records
`renewed_transfer_request_not_admitted_interest_is_not_acceptance_and_transfer_authority_absent`.
Content ID
`synthetic-content:destination-candidate-transfer-request-review-refusal-decision-002-r1`
has a valid checksum; review authority is consumed. Route state remains
`destination_candidate_redeferred_no_transfer`; prepared return is
`renewed_transfer_request_refusal_record_only`; no downstream record exists.

Correction owner is `synthetic-mechanism-map-owner`. Stop on any named fact or
risk revision. Failure modes include interest treated as acceptance, request
treated as instruction, refusal treated as candidate rejection, transfer
authority invented, prior authority reused, history erased, or downstream
effect invented. Failed review recovery retracts only the second request-review
decision, leaves both requests and the interest notice non-operative, restores
second-request-unreviewed state, and changes no candidate. Exact next wake is exact receiving-owner acceptance plus transfer authority under frozen interest-and-refusal records, materially new destination-owner evidence, or a revision to any named fact.

## Work now

Draft `candidates/MECHANISM-ALTERNATIVE-MAP-DESTINATION-CANDIDATE-RECEIVING-OWNER-INTEREST-NO-ACCEPTANCE-OR-TRANSFER-AUTHORITY-BOUNDARY-FIXTURE.md`
with exactly this frontmatter:

---
artifact_type: synthetic_mechanism_alternative_map_destination_candidate_receiving_owner_interest_no_acceptance_or_transfer_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

Use title `# Synthetic Mechanism Alternative-Map Destination-Candidate Receiving-Owner-Interest No-Acceptance-Or-Transfer-Authority Boundary Fixture`
and exactly these `##` sections: `Use Boundary`, `Map Header`, `Frozen
Inquiry And Mechanism Design Candidate Boundary`, `Alternative Records`,
`Material Difference And Nonduplication`, `Existing-Owner Fit`, `Evidence,
Affected Parties, And Legitimacy`, `Comparison Through First Transfer-Request
Refusal`, `Receiving-Owner Interest, Renewed Request, Review Refusal, And
Downstream Nonperformance`, `Prepared Return And Recovery`, and `Frontier
Verification`. Preserve every identifier, timestamp, signer, decider, scope,
trace, receipt, content ID, checksum, historical state, stop, failure mode,
correction, recovery, non-effect, and exact wake. Return only the finished artifact.
First line must be `---`; do not use a code fence; copy the literal
frontmatter exactly; and use `##` for every named body section.
