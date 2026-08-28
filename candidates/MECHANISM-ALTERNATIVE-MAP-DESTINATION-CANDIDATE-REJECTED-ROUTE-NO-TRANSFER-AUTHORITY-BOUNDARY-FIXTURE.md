---
artifact_type: synthetic_mechanism_alternative_map_destination_candidate_rejected_route_no_transfer_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Mechanism Alternative-Map Destination-Candidate-Rejected-Route No-Transfer-Authority Boundary Fixture

## Use Boundary

This synthetic fixture preserves no action, both pointer routes, the complete
comparison-through-native-content-copy lineage, destination candidate
admission, and the prior destination defer decision. It adds one separately
authorized destination-owner reconsideration decision that rejects only the
unchanged synthetic destination candidate. Rejection is not a Mechanism Design
candidate or disposition, result acceptance, transfer, graduation,
deployment, performance, target-native effect outside this fixture, or
external action. It does not modify `CMD-0001` or create `CMD-0001-P8`.

## Map Header

| Field | Value |
| --- | --- |
| `map_id` | `SYNTH-DESTINATION-CANDIDATE-REJECTED-NO-TRANSFER-MAP-001@r1` |
| `source_inquiry` | `SYNTH-SOURCE-OPENED-ROUTE-NO-DELIVERY-001@r1` |
| `source_revision` | `synthetic-source-revision:opened-route-no-delivery-001-r1` |
| `candidate_or_problem_ref` | `SYNTH-PROBLEM-OPENED-ROUTE-NO-DELIVERY-001@r1`; Mechanism Design candidate scope `none` |
| `map_owner` | `synthetic-mechanism-map-owner` |
| `authorization_ref` | `synthetic://decision-boundary/SYNTH-DESTINATION-CANDIDATE-REJECTED-NO-TRANSFER-001@r1` |
| `external_action` | `none` |

## Frozen Inquiry And Mechanism Design Candidate Boundary

The source inquiry, source revision, problem, payload, alternatives,
comparison, selection, destination acceptance, six consumed execution grants,
destination candidate admission, and prior defer decision remain unchanged.
Frozen evidence is `MECHANISM-ALTERNATIVE-MAP-TEMPLATE.md`, `GOVERNANCE.md`,
and
`MECHANISM-ALTERNATIVE-MAP-DESTINATION-CANDIDATE-DEFERRED-ROUTE-NO-TRANSFER-AUTHORITY-BOUNDARY-FIXTURE.md`.
Existing-owner fit remains `synthetic-destination-owner` and defeats admission
here. Mechanism Design candidate scope remains `none`; no source claim, owner
truth, or real candidate may be inferred from the rejection.

## Alternative Records

- `SYNTH-ALT-OPENED-NO-ACTION-001@r1` preserves no action.
- `SYNTH-ALT-OPENED-IMMEDIATE-001@r1` preserves the selected immediate pointer route.
- `SYNTH-ALT-OPENED-VERIFIED-001@r1` remains materially distinct dominated evidence on required timing.

The alternatives and both pointer routes remain visible. Rejection erases none
of the comparison, selection, execution, admission, or defer records and does
not convert any route into a Mechanism Design candidate.

## Material Difference And Nonduplication

Destination rejection is distinct from destination admission, destination
defer, and Mechanism Design disposition. It is also distinct from result
acceptance, transfer, graduation, deployment, performance, and external
action. The unchanged payload `SYNTH-NATIVE-CONTENT-PAYLOAD-001@r1` remains
the subject of destination candidate `SYNTH-DESTINATION-CANDIDATE-001@r1`.
Current route state is `destination_candidate_rejected_no_transfer`; prepared
return is `destination_candidate_rejection_record_only`. The prior defer
decision remains historical evidence and is superseded only for current
destination-candidate state.

## Existing-Owner Fit

Existing-owner fit remains `synthetic-destination-owner` because the staged
payload, destination candidate, defer decision, and rejection decision remain
inside that owner's native synthetic boundary. That fit defeats admission in
Mechanism Design. Rejection does not establish accepted truth or grant
Mechanism Design disposition, transfer, graduation, or deployment authority.

## Evidence, Affected Parties, And Legitimacy

Payload `SYNTH-NATIVE-CONTENT-PAYLOAD-001@r1`, content ID
`synthetic-content:native-content-payload-001-r1`, remains unchanged on
`synthetic-destination-staging-surface`. Evidence pointer is
`synthetic://map-evidence/SYNTH-DESTINATION-CANDIDATE-REJECTED-NO-TRANSFER-001@r1`.
All people, owners, standing, actors, data, evidence, authority, and systems
are synthetic. No real person or owner is represented or can be spoken for.
The principal legitimacy risk is authority laundering. Correction belongs to
`synthetic-mechanism-map-owner`.

## Comparison Through Destination Defer Boundary

Comparison `SYNTH-CONDITION-IMMEDIATE-REQUIRED-006@r1` is signed by
`synthetic-condition-owner` under
`synthetic-condition-comparison-authority@r1`. Selection
`SYNTH-ROUTE-SELECTION-IMMEDIATE-004@r1` is signed by
`synthetic-route-selection-owner` under
`synthetic-route-selection-authority@r1`. Destination acceptance
`SYNTH-DESTINATION-ACCEPTANCE-IMMEDIATE-003@r1` is signed by
`synthetic-destination-owner` under
`synthetic-destination-pointer-intake-acceptance@r1`.

The six exact execution grants remain valid and consumed:

| Effect | Authorization and signer scope | Trace, receipt, and receipt content ID |
| --- | --- | --- |
| opening | `SYNTH-ROUTE-OPENING-AUTHORIZATION-002@r1`, signed by `synthetic-route-opening-authority-owner` under `synthetic-route-opening-decision-authority@r1` | `SYNTH-ROUTE-OPENING-TRACE-001@r1`; `SYNTH-ROUTE-OPENING-RECEIPT-001@r1`; `synthetic-content:route-opening-receipt-opened-no-delivery-001-r1` |
| sending | `SYNTH-ROUTE-SENDING-AUTHORIZATION-001@r1`, signed by `synthetic-route-sending-authority-owner` under `synthetic-route-sending-decision-authority@r1` | `SYNTH-ROUTE-SENDING-TRACE-001@r1`; `SYNTH-ROUTE-SENDING-RECEIPT-001@r1`; `synthetic-content:route-sending-receipt-sent-no-delivery-001-r1` |
| delivery | `SYNTH-ROUTE-DELIVERY-AUTHORIZATION-001@r1`, signed by `synthetic-route-delivery-authority-owner` under `synthetic-route-delivery-decision-authority@r1` | `SYNTH-ROUTE-DELIVERY-TRACE-001@r1`; `SYNTH-ROUTE-DELIVERY-RECEIPT-001@r1`; `synthetic-content:route-delivery-receipt-delivered-no-acknowledgment-001-r1` |
| acknowledgment | `SYNTH-ROUTE-ACKNOWLEDGMENT-AUTHORIZATION-001@r1`, signed by `synthetic-route-acknowledgment-authority-owner` under `synthetic-route-acknowledgment-decision-authority@r1` | `SYNTH-ROUTE-ACKNOWLEDGMENT-TRACE-001@r1`; `SYNTH-ROUTE-ACKNOWLEDGMENT-RECEIPT-001@r1`; `synthetic-content:route-acknowledgment-receipt-acknowledged-no-intake-001-r1` |
| intake | `SYNTH-ROUTE-INTAKE-AUTHORIZATION-001@r1`, signed by `synthetic-destination-owner` under `synthetic-destination-pointer-intake-execution-authority@r1` | `SYNTH-ROUTE-INTAKE-TRACE-001@r1`; `SYNTH-ROUTE-INTAKE-RECEIPT-001@r1`; `synthetic-content:route-intake-receipt-intaken-no-candidate-001-r1` |
| native-content copy | `SYNTH-ROUTE-NATIVE-CONTENT-COPY-AUTHORIZATION-001@r1`, signed by `synthetic-destination-owner` under `synthetic-destination-native-content-copy-execution-authority@r1` | `SYNTH-ROUTE-NATIVE-CONTENT-COPY-TRACE-001@r1`; `SYNTH-ROUTE-NATIVE-CONTENT-COPY-RECEIPT-001@r1`; `synthetic-content:route-native-content-copy-receipt-copied-no-candidate-001-r1` |

Every receipt checksum remains valid. Candidate-admission authority
`SYNTH-DESTINATION-CANDIDATE-ADMISSION-AUTHORITY-001@r1` is signed by
`synthetic-destination-owner` under
`synthetic-destination-candidate-admission-decision-authority@r1`. It was
consumed by `synthetic-destination-candidate-admission-decider` when decision
`SYNTH-DESTINATION-CANDIDATE-ADMISSION-DECISION-001@r1` admitted destination
candidate `SYNTH-DESTINATION-CANDIDATE-001@r1` at `2026-08-27T21:20:12Z`.
Decision content ID is
`synthetic-content:destination-candidate-admission-decision-001-r1`; its
checksum is valid.

Disposition authority
`SYNTH-DESTINATION-CANDIDATE-DISPOSITION-AUTHORITY-001@r1` is signed by
`synthetic-destination-owner` under
`synthetic-destination-candidate-disposition-decision-authority@r1`. It was
consumed by `synthetic-destination-candidate-disposition-decider` when decision
`SYNTH-DESTINATION-CANDIDATE-DISPOSITION-DECISION-001@r1` recorded
`defer_destination_candidate` at `2026-08-27T21:35:12Z`. Decision content ID
is `synthetic-content:destination-candidate-defer-disposition-decision-001-r1`;
its checksum is valid. That defer remains historical evidence.

## Destination Candidate-Rejection Decision And Downstream Nonperformance

At `2026-08-27T21:45:12Z`, reconsideration authority
`SYNTH-DESTINATION-CANDIDATE-RECONSIDERATION-AUTHORITY-001@r1` is signed by
`synthetic-destination-owner` under
`synthetic-destination-candidate-reconsideration-decision-authority@r1`. It
authorizes only `synthetic-destination-candidate-reconsideration-decider`
exactly once to decide whether to reject the unchanged deferred destination
candidate after verifying every predecessor record, current candidate and
checksum, unresolved owner-fit objection, no accepted result, no transfer
acceptance, the consumed prior disposition authority, and the then-unconsumed
reconsideration authority. It authorizes no acceptance, Mechanism Design
admission or disposition, transfer, graduation, deployment, performance, or
external action.

At `2026-08-27T21:50:12Z`, every required check matched. Decision record
`SYNTH-DESTINATION-CANDIDATE-RECONSIDERATION-DECISION-001@r1` is signed by the
authorized reconsideration decider and records `reject_destination_candidate`.
Decision content ID is
`synthetic-content:destination-candidate-rejection-decision-001-r1`; its
checksum is valid. The one-use reconsideration authority is consumed. Route
state is `destination_candidate_rejected_no_transfer`; prepared return is
`destination_candidate_rejection_record_only`. No result-acceptance, transfer,
graduation, deployment, performance, or external-action record exists.

## Prepared Return And Recovery

Prepared return is `destination_candidate_rejection_record_only`. Preserve
every predecessor record and alternative. Stop on any named source, payload,
record, receipt, actor, authority, standing, route, copy, candidate,
admission, disposition, reconsideration, transfer, or risk revision. Failure
modes include rejection treated as Mechanism Design disposition, rejection
treated as transfer, prior consumed authority reused, historical defer erased,
or downstream effect invented. If the rejection authority or checksum fails,
retract only the rejection, restore `destination_candidate_deferred_no_transfer`,
and change no Mechanism Design candidate. Exact next wake is materially new destination-owner reconsideration evidence under frozen current records, or a revision to any named fact.

## Frontier Verification

Verify every frozen source, map, alternative, signer, authority scope, actor,
trace, receipt, content ID, checksum, consumed grant, admission, defer,
reconsideration, rejection, and absent downstream record independently.
Re-run existing-owner fit, nonduplication, affected-party, legitimacy, stop,
correction, and recovery checks. Confirm rejection changes only the synthetic
destination-candidate state and authorizes no Mechanism Design candidate,
disposition, result acceptance, transfer, graduation, deployment,
target-native effect, or external action.
