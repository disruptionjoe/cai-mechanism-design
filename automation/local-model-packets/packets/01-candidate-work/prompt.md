# Map individual NTSB recommendation actions

Family lineage:
`MD-LIN-SFQ-0001-ASR1901-INDIVIDUAL-RECOMMENDATION-ACTION-MAP-01`, opportunity
1. Begin the finished artifact immediately. Use only the frozen official-source
projection below. Do not browse, open repository files, add facts, infer
implementation or effectiveness, prescribe, rank, or create a remedy.

Frozen source-owner evidence from the official NTSB A-19-010 through A-19-016
recommendation letter, letter page 2:

1. `A-19-10`: scope `Boeing 737 MAX`; action form `require`; action object
   `Review safety assessments that assume immediate and appropriate pilot
   response against all possible flight-deck alerts and indications, then use
   design, procedure, or training changes where needed.`; dependency `none
   stated`.
2. `A-19-11`: scope `All other US type-certificated transport-category
   airplanes`; action form `require`; action object `Apply the same
   assumption, alert-and-indication, and needed-change review to other US
   transport-category airplane manufacturers.`; dependency `none stated`.
3. `A-19-12`: scope `Other international transport-airplane regulators`;
   action form `notify and encourage evaluation`; action object `Evaluate the
   relevance of A-19-11 to their processes and address applicable changes.`;
   dependency `A-19-11`.
4. `A-19-13`: scope `FAA design-certification process`; action form `develop`;
   action object `Robust tools and methods for validating pilot-recognition
   and response assumptions, with industry and human-factors input.`;
   dependency `none stated`.
5. `A-19-14`: scope `FAA regulations and guidance`; action form `revise`;
   action object `Incorporate use and documentation of the A-19-13 tools and
   methods and re-examine permitted pilot-response assumptions.`; dependency
   `A-19-13 tools and methods developed first`.
6. `A-19-15`: scope `Aircraft-system diagnostic-tool design standards`;
   action form `develop`; action object `Standards improving prioritization
   and clarity of direct and indirect failure indications presented to
   pilots, with industry and human-factors input.`; dependency `none stated`.
7. `A-19-16`: scope `Transport-category aircraft`; action form `require`;
   action object `Implement system diagnostic tools for multiple-alert and
   indication conditions.`; dependency `A-19-15 design standards developed
   first`.

For every row, evidence strength is
`official_recommendation_relation_only`. `Implementation and adoption`,
`Outcome and effectiveness`, `Cost and enforceability`, `Affected-party
consequence`, and `Capture surface` are literal `unknown`. `CMD-0001` remains
deferred.

Return only
`candidates/SFQ-0001-ASR1901-INDIVIDUAL-RECOMMENDATION-ACTION-MAP-DRAFT.md`.
Start exactly with:

---
artifact_type: asr1901_individual_recommendation_action_map_draft
status: unverified_local_candidate
source_inquiry: SFQ-0001
source_record: SF-0001
external_action: none
---

Do not use a code fence. Then return one title and exactly three `##` sections:
Boundary; Individual Recommendation Actions; Frontier Verification And Stops.

Under `## Individual Recommendation Actions`, return one Markdown table with
exactly seven rows and this header:

`Recommendation | Scope | Action form | Action object | Dependency | Evidence strength | Implementation and adoption | Outcome and effectiveness | Cost and enforceability | Affected-party consequence | Capture surface | Source pointer | Owner boundary`

Use the exact seven identifiers and literal field values above in order. Every
source pointer says `NTSB A-19-010 through A-19-016 recommendation letter,
letter page 2.` Every owner cell says `Aviation domain owners retain remedy
authority and no effect is authorized.` Maximum 1,200 words. No browsing,
source acquisition, proving, candidate action, contact, or external effect.
Return no other text. Return no code fence.
