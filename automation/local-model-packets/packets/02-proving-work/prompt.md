# Extract JATR R4 recommendation-to-mechanism evidence

Family lineage: `MD-LIN-SFQ-0001-JATR-R4-MECHANISM-EVIDENCE-EXTRACTION-01`,
opportunity 1. Begin the finished artifact immediately. Use only the frozen
official-source projection below. Do not browse, open repository files, add
facts, infer implementation or effectiveness, prescribe, or create a remedy.

Frozen source-owner evidence:

`Joint Authorities Technical Review, Boeing 737 MAX Flight Control System:
Observations, Findings, and Recommendations`, official FAA-hosted PDF
`https://www.faa.gov/sites/faa.gov/files/2022-08/Final_JATR_Submittal_to_FAA_Oct_2019.pdf`.

Frozen source projection from report pages 24-25:

- `R4.2`: policy or standards for visibility, clarity, and consistency of key
  design and compliance information, especially for new design features.
- `R4.3`: early certification-authority coordination for FHA validation, PSSA
  review, proposed system architecture, and design changes.
- `R4.4`: refuse function descriptions fragmented among several documents.
- `R4.5`: highlight and properly describe functional changes as early as
  possible regardless of preliminary hazard classification.
- `R4.6`: maintain records of interactions and agreements with certification
  authorities that affect documentation and certification deliverables.

Frozen presented mechanism: `Changed-function visibility and review timing.`

`CMD-0001` remains deferred.

Return only
`candidates/SFQ-0001-JATR-R4-MECHANISM-EVIDENCE-EXTRACTION-DRAFT.md`. Start
exactly with:

---
artifact_type: jatr_r4_mechanism_evidence_extraction_draft
status: unverified_local_candidate
source_inquiry: SFQ-0001
source_record: SF-0001
external_action: none
---

Do not use a code fence. Then return one title and exactly three `##` sections:
Boundary; R4 Mechanism Evidence; Frontier Verification And Stops.

Under `## R4 Mechanism Evidence`, return one Markdown table with exactly five
rows and this header:

`Recommendation | Frozen official-source component | Relation to presented mechanism | Unsupported extension | Source pointer | Owner boundary`

Use R4.2 through R4.6 in order. Limit each relation to visibility, review
timing, fragmentation control, change highlighting, or interaction-record
custody as supported. Keep implementation, adoption, outcome, effectiveness,
cost, enforceability, affected-party consequence, capture, and transferability
unsupported. Every source pointer names the JATR report and exact report page.
Every owner cell says `Aviation domain owners retain remedy authority and no
effect is authorized.` Maximum 900 words. No browsing, source acquisition,
proving, candidate action, contact, or external effect. Return no other text.
Return no code fence.
