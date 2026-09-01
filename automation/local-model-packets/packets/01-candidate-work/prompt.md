# Separate NTSB recommendation action sequences

Family lineage:
`MD-LIN-SFQ-0001-ASR1901-RECOMMENDATION-SEQUENCE-BOUNDARY-01`, opportunity
1. Begin the finished artifact immediately. Use only the frozen official-source
projection below. Do not browse, open repository files, add facts, infer
implementation or effectiveness, prescribe, rank, or create a remedy.

Frozen source-owner evidence:

The following projection is from the official NTSB A-19-010 through A-19-016
recommendation letter, letter page 2.

1. Sequence `direct_assessment_and_scope_diffusion`; recommendations
   `A-19-10; A-19-11; A-19-12`; action roles `require 737 MAX review and needed
   changes; require the same review for other US transport-category airplanes;
   notify international regulators and encourage relevance evaluation`;
   explicit dependency `A-19-12 names A-19-11`; supported boundary `the same
   assessment-and-needed-change concern expands across named regulatory
   audiences; implementation and equivalence of resulting remedies are not
   established`.
2. Sequence `method_to_rule_incorporation`; recommendations
   `A-19-13; A-19-14`; action roles `develop robust assumption-validation tools
   and methods; then revise FAA regulations and guidance to incorporate and
   document their use`; explicit dependency `A-19-14 follows development under
   A-19-13`; supported boundary `the recommendation text states a method-to-
   rule sequence; development, adoption, use, and results are not established`.
3. Sequence `standards_to_required_diagnostics`; recommendations
   `A-19-15; A-19-16`; action roles `develop diagnostic-tool design standards;
   then require system diagnostic tools on transport-category aircraft`;
   explicit dependency `A-19-16 follows development under A-19-15`; supported
   boundary `the recommendation text states a standards-to-requirement
   sequence; development, implementation, and results are not established`.

For every row, evidence strength is
`official_recommendation_relation_only`. `Implementation and adoption`,
`Outcome and effectiveness`, `Cost and enforceability`, `Affected-party
consequence`, and `Capture surface` are literal `unknown`.
`CMD-0001` remains deferred.

Return only
`candidates/SFQ-0001-ASR1901-RECOMMENDATION-SEQUENCE-BOUNDARY-DRAFT.md`.
Start exactly with:

---
artifact_type: asr1901_recommendation_sequence_boundary_draft
status: unverified_local_candidate
source_inquiry: SFQ-0001
source_record: SF-0001
external_action: none
---

Do not use a code fence. Then return one title and exactly three `##` sections:
Boundary; Recommendation Action Sequences; Frontier Verification And Stops.

Under `## Recommendation Action Sequences`, return one Markdown table with
exactly three rows and this header:

`Sequence | Recommendations | Action roles | Explicit dependency | Supported boundary | Evidence strength | Implementation and adoption | Outcome and effectiveness | Cost and enforceability | Affected-party consequence | Capture surface | Source pointer | Owner boundary`

Use the exact three identifiers and literal field values above in order. Every
source pointer says `NTSB A-19-010 through A-19-016 recommendation letter,
letter page 2.` Every owner cell says `Aviation domain owners retain remedy
authority and no effect is authorized.` Maximum 1,200 words. No browsing,
source acquisition, proving, candidate action, contact, or external effect.
Return no other text. Return no code fence.
