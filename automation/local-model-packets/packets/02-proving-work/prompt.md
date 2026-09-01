# Separate JATR implementation scopes

Family lineage:
`MD-LIN-SFQ-0001-JATR-IMPLEMENTATION-SCOPE-BOUNDARY-01`, opportunity 1. Begin
the finished artifact immediately. Use only the frozen official-source
projection below. Do not browse, open repository files, add facts, infer
individual implementation, prescribe, rank, or create a remedy.

Frozen source-owner evidence:

1. Evidence object `737_max_return_to_service_scope`.
   Source: `FAA 737 MAX Timeline, document page 3 of 4.`
   Direct support: `The FAA stated that it addressed all JATR recommendations
   that applied to the 737 MAX before approving the aircraft for return to
   service.`
   Scope limit: `This statement does not identify R4.2 through R4.6
   individually and does not establish systemwide certification-process
   implementation.`
2. Evidence object `changed_product_rule_reform_scope`.
   Source: `FAA Changed Product Rule Recommendations, document page 4 of 10.`
   Direct support: `The FAA-led IAWG charter included reviewing JATR
   recommendations related to the Changed Product Rule and developing
   proposals for FAA review and approval.`
   Scope limit: `This establishes reform activity, not adoption or
   implementation of R4.2 through R4.6 individually.`
3. Evidence object `r4_2_to_r4_6_systemwide_status`.
   Source: `The two official FAA documents above.`
   Direct support: `not established by frozen sources`.
   Scope limit: `The individual, systemwide adoption, implementation,
   outcome, effectiveness, cost, enforceability, affected-party consequence,
   and capture status of R4.2 through R4.6 remain unknown.`

For every row, `Evidence posture` is
`official_scope_relation_only`. `Implementation status`, `Outcome and
effectiveness`, `Cost and enforceability`, `Affected-party consequence`, and
`Capture surface` are literal `unknown`; do not replace those values with the
broader FAA statements. `CMD-0001` remains deferred.

Return only
`candidates/SFQ-0001-JATR-IMPLEMENTATION-SCOPE-BOUNDARY-DRAFT.md`. Start
exactly with:

---
artifact_type: jatr_implementation_scope_boundary_draft
status: unverified_local_candidate
source_inquiry: SFQ-0001
source_record: SF-0001
external_action: none
---

Do not use a code fence. Then return one title and exactly three `##` sections:
Boundary; Official Implementation-Scope Evidence; Frontier Verification And
Stops.

Under `## Official Implementation-Scope Evidence`, return one Markdown table
with exactly three rows and this header:

`Evidence object | Directly supported relation | Scope limit | Evidence posture | Implementation status | Outcome and effectiveness | Cost and enforceability | Affected-party consequence | Capture surface | Source pointer | Owner boundary`

Use the exact three IDs and literal direct-support and scope-limit values
above. Every owner cell says `Aviation domain owners retain remedy authority
and no effect is authorized.` Maximum 900 words. No browsing, source
acquisition, proving, candidate action, contact, or external effect. Return no
other text. Return no code fence.
