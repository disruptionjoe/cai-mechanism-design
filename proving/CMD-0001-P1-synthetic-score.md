---
score_id: CMD-0001-P1-S1
candidate_id: CMD-0001
proving_id: CMD-0001-P1
status: scored_revision_required
created: 2026-07-18
external_action: none
---

# CMD-0001-P1 Synthetic Score

## Boundary

This score uses only a synthetic fixture derived from the public pattern routed
by `SFQ-0001`. It does not use accident data, confidential certification
material, human subjects, field work, deployment, account access, or external
contact. It does not claim an aviation remedy.

## Fixture Rows

| Row | Synthetic content | Expected register behavior |
|---|---|---|
| A1 baseline assumption | A derivative system has an automatic function whose authority, input path, and limits were previously reviewed under an earlier configuration. | Store the assumption, source revision, accountable design owner, review owner, affected systems, and validation method. |
| E1 changed function event | The function expands to a new operating region or uses a changed input path while retaining the old assumption record. | Flag a drift event and require integrated review before the old assumption can be reused. |
| A2 human-response assumption | The safety case assumes immediate or appropriate human corrective response. | Record the assumption as load-bearing and mark the validation environment. |
| E2 alert/workload change | Multiple alerts, ambiguous indications, or increased workload appear in the scenario. | Mark the human-response assumption as unvalidated under the changed environment. |
| D1 delegated review path | Certification or approval work is distributed so one reviewer sees only a fragmented function description. | Route to the accountable review owner while preserving the delegation path and correction route. |

## Pass-Condition Score

| Condition from plan | Score | Reason |
|---|---|---|
| Link each assumption to a source and owner. | Conditional pass | The fixture has explicit fields, but the candidate record must require them rather than describe them narratively. |
| Flag the changed function or input path as a drift event. | Pass | E1 is visible as a changed-function event tied to A1. |
| Mark the human-response assumption as unvalidated under changed alert conditions. | Pass | A2 and E2 force a validation-status change. |
| Route the contradiction to an accountable review owner. | Conditional pass | D1 routes to a review owner, but the mechanism must forbid silent escalation to a generic central reviewer. |
| Preserve a correction route without declaring the technical outcome. | Pass | The fixture can preserve correction without deciding the aviation case. |

## Hostile Paperwork Test

The current candidate can still be filled as paperwork theater if implementers
write "reviewed" or "accepted" in free-text fields while leaving the
contradiction untyped. That does not kill the candidate, because the synthetic
fixture exposes the repair: typed drift events, validation-status changes, and
lowest-fitting owner routing must be required fields.

## Disposition

Disposition for this first synthetic test: revise.

`CMD-0001` remains admitted as a synthetic-only candidate, but it is not ready
for graduation, transfer, or broader proving. The next work is to revise the
candidate into a typed minimum register with these required fields:

- assumption id;
- source revision;
- assumption owner;
- review owner;
- affected system;
- change event;
- validation environment;
- validation status;
- contradiction flag;
- lowest-fitting owner route;
- correction route;
- stop condition.

Any future pass must fail if the contradiction can be hidden while every field
is formally filled.

