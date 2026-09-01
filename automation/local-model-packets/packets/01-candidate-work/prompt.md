# Preserve SF-0001 intervention-example custody

Family lineage:
`MD-LIN-SFQ-0001-SF0001-INTERVENTION-EXAMPLE-CUSTODY-01`, opportunity 1.
Begin the finished artifact immediately. Use only the frozen text below. Do not browse,
open repository files, add facts, rank interventions, infer an
outcome, prescribe, or create a remedy.

Frozen source-owner evidence:

Comparison:
`cai-systemic-failure#topology/SF-0001-causal-model-comparison.md` at
source-owner revision `43b0b96d483a16b872bfe754911bcf90df8b0838`.

Frozen rows:

- Intervention class `Procedure update`; source-reported example `FAA
  emergency AFM revision after Lion Air expanded runaway-stabilizer guidance
  for erroneous AOA input.`; mechanism `Late symptom recognition and
  response.`; bounded example posture `reported_implemented_response`.
- Intervention class `Safety-assessment revalidation`; source-reported example
  `NTSB recommendations A-19-10 and A-19-11 ask that pilot-response assumptions
  consider all possible flight-deck alerts and indications.`; mechanism
  `Human-response assumption validation.`; bounded example posture
  `reported_recommendation_set`.
- Intervention class `Human-factors tool development`; source-reported example
  `NTSB recommendations A-19-13 and A-19-14 ask for tools/methods and
  documentation for validating pilot recognition and response assumptions.`;
  mechanism `Repeatable validation method.`; bounded example posture
  `reported_recommendation_set`.
- Intervention class `Alert diagnostic standards`; source-reported example
  `NTSB recommendations A-19-15 and A-19-16 concern prioritization and clarity
  of failure indications.`; mechanism `Signal clarity under multiple
  indications.`; bounded example posture `reported_recommendation_set`.
- Intervention class `Certification visibility standards`; source-reported
  example `JATR R4.2 through R4.6 address clarity, consistency, early
  coordination, fragmented descriptions, functional-change highlighting, and
  records of agreements.`; mechanism `Changed-function visibility and review
  timing.`; bounded example posture `reported_recommendation_set`.
- Intervention class `Delegation pressure review`; source-reported example
  `JATR observations and recommendations on ODA environment and FAA
  communication address delegated authority pressure and visibility.`;
  mechanism `Delegated review integrity.`; bounded example posture
  `reported_observation_and_recommendation_set`.

Frozen limits:

- The posture labels describe only how the source-owner synthesis presents the
  examples. They do not establish implementation completeness, effectiveness,
  adoption, causality, cost, enforceability, affected-party consequences, or
  capture.
- Only the procedure update is presented as a reported implemented response;
  it is also described as downstream and does not prove prevention.
- The comparison is provisional public-official-source synthesis, not an
  aviation finding, remedy, recommendation, or intervention plan.
- Aviation-specific remedies remain with aviation safety authorities and
  domain experts. `CMD-0001` remains deferred.

Return only
`candidates/SFQ-0001-SF0001-INTERVENTION-EXAMPLE-CUSTODY-DRAFT.md`. The first
seven lines must be exactly:

---
artifact_type: sf0001_intervention_example_custody_draft
status: unverified_local_candidate
source_inquiry: SFQ-0001
source_record: SF-0001
external_action: none
---

Do not use a code fence. Then return one title and exactly three `##` sections:
Use Boundary; Intervention Example Custody; Frontier Verification And Stops.

Under `## Intervention Example Custody`, return one Markdown table with
exactly six rows and this literal header:

`Intervention class | Exact source-reported example | Frozen reported mechanism | Bounded example posture | Outcome and effectiveness status | Source-owner pointer | Owner boundary`

Use the exact six rows and posture labels above. Every outcome and
effectiveness cell uses literal `not_established_in_frozen_synthesis`. Every
source-owner pointer names the frozen comparison and revision. Every final
cell says `Aviation domain owners retain remedy authority and no effect is
authorized.` Maximum 1,050 words. Do not admit or reopen a candidate;
authorize research, proving, or source acquisition; contact anyone; or create
an external effect. Return no other text. Return no code fence.
