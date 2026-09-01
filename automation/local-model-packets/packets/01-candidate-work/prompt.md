# Compare official recommendation control points

Family lineage:
`MD-LIN-SFQ-0001-ASR1901-JATR-CONTROL-POINT-COMPARISON-01`, opportunity 1.
Begin the finished artifact immediately. Use only the frozen official-source
projection below. Do not browse, open repository files, add facts, infer
implementation or effectiveness, prescribe, rank, or create a remedy.

Frozen source-owner evidence:

1. NTSB ASR-19-01, report pages 8-9, A-19-10 and A-19-11: safety
   assessments that assume immediate and appropriate pilot response are to
   consider all possible flight-deck alerts and indications, with design,
   procedure, or training changes where needed.
2. NTSB ASR-19-01, report pages 9-10, A-19-13 and A-19-14: robust tools and
   methods are recommended to validate pilot-recognition and response
   assumptions, followed by incorporation of their use and documentation into
   regulation and guidance.
3. NTSB ASR-19-01, report page 11, A-19-15 and A-19-16: diagnostic-tool design
   standards are recommended to improve prioritization and clarity of failure
   indications, followed by a recommendation to require those tools on
   transport-category aircraft.
4. FAA-hosted JATR report, pages 24-25, R4.2 through R4.6: recommendations
   address visibility, clarity, and consistency of design and compliance
   information; early certification-authority review; fragmentation control;
   early highlighting of functional changes; and records of interactions and
   agreements affecting certification deliverables.

The four frozen control-point labels, in order, are:

1. `Pilot-response assumptions in safety assessment.`
2. `Repeatable assumption-validation method and documentation.`
3. `Pilot-facing failure-indication prioritization and clarity.`
4. `Certification-facing design-information visibility and review timing.`

For every row, use evidence strength
`official_recommendation_relation_only`. Use literal `unknown` for
implementation status; outcome and effectiveness; cost and enforceability;
affected-party consequence; and capture surface. `CMD-0001` remains deferred.

Return only
`candidates/SFQ-0001-ASR1901-JATR-CONTROL-POINT-COMPARISON-DRAFT.md`. Start
exactly with:

---
artifact_type: asr1901_jatr_control_point_comparison_draft
status: unverified_local_candidate
source_inquiry: SFQ-0001
source_record: SF-0001
external_action: none
---

Do not use a code fence. Then return one title and exactly three `##` sections:
Boundary; Official Recommendation Control Points; Frontier Verification And
Stops.

Under `## Official Recommendation Control Points`, return one Markdown table
with exactly four rows and this header:

`Source component | Frozen control point | Directly supported relation | Evidence strength | Implementation status | Outcome and effectiveness | Cost and enforceability | Affected-party consequence | Capture surface | Source pointer | Owner boundary`

Use A-19-10/11, A-19-13/14, A-19-15/16, and JATR R4.2-R4.6 in order. Every
source pointer names the report and exact page or pages above. Every owner cell
says `Aviation domain owners retain remedy authority and no effect is
authorized.` Keep alternatives, success conditions, prerequisites, adoption,
implementation, outcomes, effectiveness, cost, enforceability, affected-party
consequence, capture, transferability, and remedy unsupported beyond the
frozen relations. Maximum 1,000 words. No browsing, source acquisition,
proving, candidate action, contact, or external effect. Return no other text.
Return no code fence.
