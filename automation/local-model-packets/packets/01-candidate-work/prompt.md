# Extract NTSB recommendation-to-mechanism evidence

Family lineage: `MD-LIN-SFQ-0001-ASR1901-MECHANISM-EVIDENCE-EXTRACTION-01`,
opportunity 1. Begin the finished artifact immediately. Use only the frozen
official-source projection below. Do not browse, open repository files, add
facts, infer implementation or effectiveness, prescribe, or create a remedy.

Frozen source-owner evidence:

`NTSB Safety Recommendation Report ASR-19-01, Assumptions Used in the Safety
Assessment Process and the Effects of Multiple Alerts and Indications on Pilot
Performance`, official PDF
`https://www.ntsb.gov/investigations/AccidentReports/Reports/ASR1901.pdf`.

Frozen source projection:

- Report pages 8-9: A-19-10 and A-19-11 require safety assessments to consider
  all possible flight-deck alerts and indications when evaluating assumed
  immediate and appropriate pilot response, with design, procedure, or training
  changes where needed.
- Report pages 9-10: A-19-13 calls for robust tools and methods to validate
  pilot-recognition and response assumptions; A-19-14 calls for incorporating
  their use and documentation into regulation and guidance.
- Report page 11: A-19-15 calls for diagnostic-tool design standards improving
  prioritization and clarity of failure indications; A-19-16 calls for
  implementation of those tools on transport-category aircraft.

Frozen presented relations:

1. `A-19-10 and A-19-11` -> `Human-response assumption validation.`
2. `A-19-13 and A-19-14` -> `Repeatable validation method.`
3. `A-19-15 and A-19-16` -> `Signal clarity under multiple indications.`

`CMD-0001` remains deferred.

Return only
`candidates/SFQ-0001-ASR1901-MECHANISM-EVIDENCE-EXTRACTION-DRAFT.md`. Start
exactly with:

---
artifact_type: asr1901_mechanism_evidence_extraction_draft
status: unverified_local_candidate
source_inquiry: SFQ-0001
source_record: SF-0001
external_action: none
---

Do not use a code fence. Then return one title and exactly three `##` sections:
Boundary; Recommendation-Mechanism Evidence; Frontier Verification And Stops.

Under `## Recommendation-Mechanism Evidence`, return one Markdown table with
exactly three rows and this header:

`Recommendation group | Frozen presented mechanism | Official report location | Directly supported relation | Unsupported extension | Source pointer | Owner boundary`

For each row, state only the narrow relation directly supported by the frozen
projection and keep implementation, adoption, outcome, effectiveness, cost,
enforceability, affected-party consequence, and capture unsupported. Every
source pointer names ASR-19-01 and the exact report pages. Every owner cell says
`Aviation domain owners retain remedy authority and no effect is authorized.`
Maximum 900 words. No browsing, source acquisition, proving, candidate action,
contact, or external effect. Return no other text. Return no code fence.
