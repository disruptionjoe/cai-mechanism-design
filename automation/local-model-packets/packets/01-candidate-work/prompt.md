# Record one synthetic republication request refusal after withdrawal maintenance

## Boundary

Return one compact synthetic graduation-process fixture from only the frozen
evidence below. Add one non-operative synthetic republication request, one
exact request-review authority, one refusal decision, and one receipt. Keep
state at `synthetic_publication_withdrawal_maintained_no_external_effect`
because republication execution authority is absent. This is not posting,
sending, contact, public release, deletion, real-owner acceptance, or external
action. Do not modify `CMD-0001` or create P8. External action is `none`.

## Frozen evidence

Use `GOVERNANCE.md`,
`interfaces/DESTINATION-OWNER-SYNTHETIC-REVIEW-REQUEST-TEMPLATE.md`, and
`graduations/GRADUATION-PUBLICATION-WITHDRAWAL-MAINTENANCE-AUTHORIZED-NO-EXTERNAL-EFFECT-BOUNDARY-FIXTURE.md`.
Copy each row once in the section that consumes it:

| Key | Exact value |
| --- | --- |
| `maintenance_receipt` | `SYNTH-PUBLICATION-WITHDRAWAL-MAINTENANCE-RECEIPT-001@r1` |
| `maintenance_receipt_content` | `synthetic-content:publication-withdrawal-maintenance-receipt-001-r1` |
| `withdrawal_receipt` | `SYNTH-PUBLICATION-WITHDRAWAL-RECEIPT-001@r1` |
| `current_state` | `synthetic_publication_withdrawal_maintained_no_external_effect` |
| `prior_return` | `synthetic_publication_withdrawal_maintenance_record_only` |

Every predecessor checksum is valid and prior records remain history. At
`2026-08-28T00:40:12Z`, request
`SYNTH-PUBLICATION-REPUBLICATION-REQUEST-001@r1` is prepared internally by
`synthetic-publication-requester`; it requests republication but grants no
authority and is never sent. At `2026-08-28T00:42:12Z`, authority
`SYNTH-PUBLICATION-REPUBLICATION-REQUEST-REVIEW-AUTHORITY-001@r1` is signed by
`synthetic-receiving-owner` under
`synthetic-publication-republication-request-review-decision-authority@r1` for
one use by `synthetic-publication-request-reviewer`. It permits only internal
review after lineage, maintenance-receipt, risk, no-revocation, and
unconsumed-authority checks. At `2026-08-28T00:44:12Z`, decision
`SYNTH-PUBLICATION-REPUBLICATION-REQUEST-REVIEW-DECISION-001@r1` records
`refuse_synthetic_republication_request_no_execution_authority`; content
`synthetic-content:publication-republication-request-review-decision-001-r1`
is valid. At `2026-08-28T00:45:12Z`, receipt
`SYNTH-PUBLICATION-REPUBLICATION-REQUEST-REVIEW-RECEIPT-001@r1`, content
`synthetic-content:publication-republication-request-review-receipt-001-r1`,
consumes review authority and leaves state unchanged.

Review owner is `synthetic-receiving-owner`; correction owner is
`synthetic-mechanism-map-owner`. Preserve concrete risks, stops, failure
modes, correction, recovery to the unchanged current state, non-effect, and
exact wake. Exact next wake is exact synthetic republication execution
authority under the refusal receipt, or any named revision.

## Work now

Draft
`graduations/GRADUATION-PUBLICATION-REPUBLICATION-REQUEST-REFUSED-NO-REPUBLICATION-AUTHORITY-BOUNDARY-FIXTURE.md`
with frontmatter `artifact_type:
synthetic_graduation_publication_republication_request_refused_no_republication_authority_boundary_fixture`,
`status: candidate_process_fixture`, and `external_action: none`. Use title
`# Synthetic Graduation Publication Republication Request Refused No-Republication-Authority Boundary Fixture`
and exactly these `##` sections: `Use Boundary`, `Frozen Maintenance And
Predecessor Custody`, `Non-Operative Republication Request`, `Request Review
Authority Decision And Receipt`, `Risk Owner Fit And Legitimacy`, `Stops
Correction Recovery And Reopen`, `Prepared Return And Exact Wake`, and
`Frontier Verification`.

Begin the raw artifact now. Return only the finished artifact. First line must
be `---`; close frontmatter with a second `---`; do not use a code fence; all
named sections use `##`; stay under 2,000 words; do not deliberate between
effects or restate frozen rows in verification.
