# Preserve individual recommendation status evidence requirements

Family lineage:
`MD-LIN-SFQ-0001-ASR1901-INDIVIDUAL-STATUS-EVIDENCE-REQUIREMENTS-01`,
opportunity 1. Begin the finished artifact immediately. Use only the frozen
official-source projection below. Do not browse, acquire records, add facts,
infer a classification or implementation, prescribe, rank, or create a remedy.

Frozen source-owner evidence:

- The NTSB investigation page for Lion Air Flight 610 and Ethiopian Airlines
  Flight 302 labels the investigation `Completed` and lists A-19-010 through
  A-19-016.
- The NTSB Safety Recommendations Data Field Descriptions page explains that
  individual recommendations receive distinct open or closed classifications
  determined by the Board.
- Neither frozen page states the individual classification of A-19-010 through
  A-19-016. Every classification and implementation value is `unknown`.
- The recommendation-specific evidence required for each row is the
  corresponding official `NTSB CAROL recommendation detail for <ID>`.
- `CMD-0001` remains deferred.

Return only
`candidates/SFQ-0001-ASR1901-INDIVIDUAL-STATUS-EVIDENCE-REQUIREMENTS-DRAFT.md`,
without a code fence. Begin exactly:

---
artifact_type: asr1901_individual_status_evidence_requirements_draft
status: unverified_local_candidate
source_inquiry: SFQ-0001
source_record: SF-0001
external_action: none
---

Then return one `#` title and exactly three sections: `## Boundary`, `##
Individual Status Evidence Requirements`, and `## Frontier Verification And
Stops`. Under the middle section return exactly seven rows, A-19-010 through
A-19-016 in order, with this header:

`Recommendation | Listed on investigation page | Individual classification | Required official record | Classification-to-implementation boundary | Evidence posture | Implementation | Outcome and effectiveness | Cost and enforceability | Affected-party consequence | Capture surface | Source pointer | Owner boundary`

For every row use: `yes`; `unknown`; `NTSB CAROL recommendation detail for
<ID>`; `A recommendation classification does not by itself establish complete
implementation, outcome, or effectiveness.`; `official_status_requirement_only`;
five literal `unknown` values; `NTSB investigation page and Safety
Recommendations Data Field Descriptions page.`; and `Aviation domain owners
retain remedy authority and no effect is authorized.`

State that only the recommendation-specific official record can support a
later classification claim and that no record acquisition, classification,
implementation, outcome, effectiveness, cost, enforceability, affected-party
consequence, capture, remedy, candidate action, contact, or external effect is
authorized. Maximum 1,200 words. Return no code fence. Return no other text.
