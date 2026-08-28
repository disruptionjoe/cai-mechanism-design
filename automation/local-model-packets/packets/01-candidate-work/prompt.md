# Refuse synthetic transfer request after re-defer without inventing acceptance

## Boundary

Write one complete synthetic Mechanism Design process fixture from only the
embedded evidence. Preserve no action, both pointer routes, full execution
lineage, destination admission, historical defer, rejection, reopen, and
current re-defer. Add one request for transfer and one separately authorized
review decision that refuses to admit that request because receiving-owner
acceptance and transfer authority are absent. A request is evidence, not an
instruction. Refusal is not rejection of the candidate, acceptance, Mechanism
Design admission or disposition, transfer, graduation, deployment,
performance, target-native effect outside the fixture, or external action.
Do not modify `CMD-0001` or create P8. External action is `none`.

## Frozen evidence

Use `GOVERNANCE.md`,
`interfaces/DESTINATION-OWNER-SYNTHETIC-REVIEW-REQUEST-TEMPLATE.md`,
`candidates/MECHANISM-ALTERNATIVE-MAP-TEMPLATE.md`, and
`candidates/MECHANISM-ALTERNATIVE-MAP-DESTINATION-CANDIDATE-REDEFERRED-AFTER-REOPEN-ROUTE-NO-TRANSFER-AUTHORITY-BOUNDARY-FIXTURE.md`.
Freeze map
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REFUSED-AFTER-REDEFER-MAP-001@r1`,
the unchanged source, payload, alternatives, comparison, selection,
destination acceptance, six consumed grants, candidate admission, historical
defer, rejection, reopen, and current re-defer decision. Existing-owner fit
remains `synthetic-destination-owner`; Mechanism Design candidate scope remains
`none`; route state remains `destination_candidate_redeferred_no_transfer`.

At `2026-08-27T22:30:12Z`, request
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-001@r1` is signed by
`synthetic-transfer-requester` under
`synthetic-transfer-request-creation-authority@r1`. Content ID
`synthetic-content:destination-candidate-transfer-request-001-r1` has a
valid checksum. It asks to transfer the unchanged re-deferred candidate to
`synthetic-receiving-owner` but supplies no receiving-owner acceptance,
accepted scope, unresolved-risk acknowledgment, transfer decision authority,
or transfer decision. It changes no state and grants no authority.

At `2026-08-27T22:32:12Z`, review authority
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-AUTHORITY-001@r1` is
signed by `synthetic-destination-owner` under
`synthetic-destination-candidate-transfer-request-review-decision-authority@r1`.
It authorizes only `synthetic-destination-candidate-transfer-request-reviewer`
once to record whether this request is admissible after verifying the complete
frozen lineage, unchanged re-deferred candidate and checksum, request and
checksum, absent receiving-owner acceptance, absent accepted scope and risk
acknowledgment, absent transfer authority and decision, and unconsumed review
authority. It authorizes no candidate disposition, transfer, acceptance,
graduation, deployment, performance, or external action.

At `2026-08-27T22:35:12Z`, every check matched. Decision
`SYNTH-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REVIEW-DECISION-001@r1` is
signed by the authorized reviewer and records
`transfer_request_not_admitted_missing_receiving_owner_acceptance_and_authority`.
Content ID
`synthetic-content:destination-candidate-transfer-request-review-refusal-decision-001-r1`
has a valid checksum; review authority is consumed. Route state remains
`destination_candidate_redeferred_no_transfer`; prepared return is
`transfer_request_refusal_record_only`. No downstream record exists.

Literal destination-state lineage to copy in the comparison section:

- admission — `SYNTH-DESTINATION-CANDIDATE-ADMISSION-AUTHORITY-001@r1`; `synthetic-destination-owner`; `synthetic-destination-candidate-admission-decision-authority@r1`; `synthetic-destination-candidate-admission-decider`; `SYNTH-DESTINATION-CANDIDATE-ADMISSION-DECISION-001@r1`; `synthetic-content:destination-candidate-admission-decision-001-r1`; consumed
- defer — `SYNTH-DESTINATION-CANDIDATE-DISPOSITION-AUTHORITY-001@r1`; `synthetic-destination-owner`; `synthetic-destination-candidate-disposition-decision-authority@r1`; `synthetic-destination-candidate-disposition-decider`; `SYNTH-DESTINATION-CANDIDATE-DISPOSITION-DECISION-001@r1`; `synthetic-content:destination-candidate-defer-disposition-decision-001-r1`; consumed
- rejection — `SYNTH-DESTINATION-CANDIDATE-RECONSIDERATION-AUTHORITY-001@r1`; `synthetic-destination-owner`; its reconsideration scope and authorized decider; `SYNTH-DESTINATION-CANDIDATE-RECONSIDERATION-DECISION-001@r1`; `synthetic-content:destination-candidate-rejection-decision-001-r1`; consumed
- reopen — `SYNTH-DESTINATION-CANDIDATE-REOPEN-AUTHORITY-001@r1`; `synthetic-destination-owner`; `synthetic-destination-candidate-reopen-decision-authority@r1`; `synthetic-destination-candidate-reopen-decider`; `SYNTH-DESTINATION-CANDIDATE-REOPEN-DECISION-001@r1`; `synthetic-content:destination-candidate-reopen-decision-001-r1`; consumed
- re-defer review — `SYNTH-DESTINATION-CANDIDATE-REOPEN-REVIEW-AUTHORITY-001@r1`; `synthetic-destination-owner`; `synthetic-destination-candidate-reopen-review-decision-authority@r1`; `synthetic-destination-candidate-reopen-review-decider`; `SYNTH-DESTINATION-CANDIDATE-REOPEN-REVIEW-DECISION-001@r1`; `synthetic-content:destination-candidate-reopen-review-redefer-decision-001-r1`; consumed

Preserve the six-effect authorization/signer/scope/trace/receipt/content-ID
lineage exactly from the frozen fixture. Correction owner is
`synthetic-mechanism-map-owner`. Stop on any named fact or risk revision.
Failure modes include request treated as instruction, refusal treated as
candidate rejection, receiving-owner acceptance invented, prior authority
reused, history erased, or downstream effect invented. Failed review recovery
retracts only the request-review decision, leaves the request as non-operative
evidence, restores unreviewed-request state, and changes no candidate. Exact next wake is exact receiving-owner acceptance plus transfer authority under frozen refused-request records, materially new destination-owner evidence, or a revision to any named fact.

## Work now

Draft `candidates/MECHANISM-ALTERNATIVE-MAP-DESTINATION-CANDIDATE-TRANSFER-REQUEST-REFUSED-AFTER-REDEFER-ROUTE-NO-TRANSFER-AUTHORITY-BOUNDARY-FIXTURE.md`
with exactly this frontmatter:

---
artifact_type: synthetic_mechanism_alternative_map_destination_candidate_transfer_request_refused_after_redefer_route_no_transfer_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

Use title `# Synthetic Mechanism Alternative-Map Destination-Candidate-Transfer-Request-Refused-After-Redefer Route No-Transfer-Authority Boundary Fixture`
and exactly these `##` sections: `Use Boundary`, `Map Header`, `Frozen
Inquiry And Mechanism Design Candidate Boundary`, `Alternative Records`,
`Material Difference And Nonduplication`, `Existing-Owner Fit`, `Evidence,
Affected Parties, And Legitimacy`, `Comparison Through Destination Redefer
Boundary`, `Transfer Request, Review Refusal, And Downstream Nonperformance`,
`Prepared Return And Recovery`, and `Frontier Verification`. Preserve every
identifier, timestamp, signer, decider, scope, trace, receipt, content ID,
checksum, historical state, stop, failure mode, correction, recovery,
non-effect, and exact wake. Return only the finished artifact. First line must
be `---`; do not use a code fence; copy the literal frontmatter exactly; and
use `##` for every named body section.
