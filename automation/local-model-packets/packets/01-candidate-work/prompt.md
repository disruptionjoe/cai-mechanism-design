# Preserve current individual recommendation classifications

Family lineage:
`MD-LIN-SFQ-0001-ASR1901-INDIVIDUAL-STATUS-CLASSIFICATION-BOUNDARY-01`,
opportunity 1. Begin the finished artifact immediately. Use only the frozen
official NTSB CAROL projection below. Do not browse, add facts, infer
implementation or effectiveness, prescribe, rank, or create a remedy.

Frozen source-owner evidence:

Each line is
`recommendation | current overall status | overall date closed | official detail`:

1. `A-19-010 | Closed - Acceptable Action | 01/05/2023 | https://data.ntsb.gov/carol-main-public/sr-details/A-19-010`
2. `A-19-011 | Open - Acceptable Response | unknown | https://data.ntsb.gov/carol-main-public/sr-details/A-19-011`
3. `A-19-012 | Closed - Acceptable Action | 01/05/2023 | https://data.ntsb.gov/carol-main-public/sr-details/A-19-012`
4. `A-19-013 | Open - Acceptable Response | unknown | https://data.ntsb.gov/carol-main-public/sr-details/A-19-013`
5. `A-19-014 | Open - Acceptable Response | unknown | https://data.ntsb.gov/carol-main-public/sr-details/A-19-014`
6. `A-19-015 | Open - Acceptable Response | unknown | https://data.ntsb.gov/carol-main-public/sr-details/A-19-015`
7. `A-19-016 | Open - Acceptable Response | unknown | https://data.ntsb.gov/carol-main-public/sr-details/A-19-016`

Return only
`candidates/SFQ-0001-ASR1901-INDIVIDUAL-STATUS-CLASSIFICATION-BOUNDARY-DRAFT.md`,
without a code fence. Begin exactly:

---
artifact_type: asr1901_individual_status_classification_boundary_draft
status: unverified_local_candidate
source_inquiry: SFQ-0001
source_record: SF-0001
external_action: none
---

Then return one `#` title and exactly three sections: `## Boundary`, `##
Individual Recommendation Classifications`, and `## Frontier Verification And
Stops`. Under the middle section return exactly seven rows in the frozen order
with this header:

`Recommendation | Current overall status | Overall date closed | Classification-to-implementation boundary | Evidence posture | Implementation | Outcome and effectiveness | Cost and enforceability | Affected-party consequence | Capture surface | Source pointer | Owner boundary`

Copy each frozen recommendation, status, close date, and detail URL exactly.
Every other cell is literal:

- Classification-to-implementation boundary: `Current NTSB classification does not by itself establish complete implementation, outcome, or effectiveness.`
- Evidence posture: `official_current_classification_only`
- Each of the five consequence/effect fields: `unknown`
- Owner boundary: `Aviation domain owners retain remedy authority and no effect is authorized.`

State that the classifications are current only to Frontier inspection on
2026-09-01 and establish no implementation, outcome, effectiveness, cost,
enforceability, affected-party consequence, capture, transferability, remedy,
candidate action, contact, or external effect; `CMD-0001` remains deferred.
Maximum 1,400 words. Return no code fence. Return no other text.
