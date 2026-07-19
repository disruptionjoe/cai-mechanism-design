---
proving_id: CMD-0001-P3
candidate_id: CMD-0001
status: planned_source_fixture_translation
created: 2026-07-19
source_fixture: cai-systemic-failure/topology/SF-ABS-0003-negative-absorber-station-nightclub.md
source_owner_revision: d6cf8fe
external_action: none
---

# CMD-0001-P3 - Station Negative Absorber Translation Test

## Boundary

This proving plan uses the existing CAI Systemic Failure source fixture
`SF-ABS-0003-negative-absorber-station-nightclub.md`. It does not create a new
failure record, copy source artifacts, make fire-safety findings, contact any
party, run field work, deploy a mechanism, or create a destination-owner
obligation.

The source owner keeps all source-backed systemic-failure claims. This
repository only tests whether `CMD-0001` can translate the fixture without
overclaiming that every public safety failure is an assumption-drift register
case.

## Purpose

Test the typed minimum register against a non-aerospace, public-source negative
absorber. The candidate should refuse a positive register fit when the source
fixture centers fire/life-safety code, material, sprinkler, pyrotechnic, egress,
inspection, and emergency-response protection rather than source-backed
assumption reuse under changed conditions.

## Source Fixture Assertions

These assertions are imported only as constraints from the source fixture; they
are not new source claims by this repository.

| Fixture constraint | Translation consequence |
|---|---|
| The source set is public official NIST material, with pointers stored by CAI Systemic Failure. | This plan may cite the source fixture path and revision, but must not copy source artifacts or expand source synthesis. |
| Assumption reuse under changed condition is refused as the central fit. | `CMD-0001` must not force a `change_event_type` merely because the case is severe. |
| Validation burden is refused as positive fit for the review-chain candidate. | The typed register must not relabel domain-code, material, sprinkler, pyrotechnic, egress, inspection, or emergency-response issues as generic validation burden. |
| Affected standing remains visible but is not enough by itself. | Occupant, injured-person, responder, and public-agency standing can be preserved without qualifying the mechanism. |
| Delegation or review visibility partly appears but is not central. | Organizational complexity alone cannot create an active contradiction row. |
| The fire/life-safety and protection-system account absorbs the review-chain candidate. | Any register translation must preserve the absorber or refuse the case. |
| Correction routes belong to domain owners. | This repository must not prescribe building-code, fire-safety, legal, enforcement, inspection, or emergency-response action. |

## Translation Rows

| Row | Source-fixture pressure | Expected typed behavior |
|---|---|---|
| S1 severe public harm with no source-backed changed assumption | The case is grave and public, but the fixture refuses assumption reuse as central. | Refuse positive fit; no row may pass by filling `change_event_type` from severity alone. |
| S2 affected standing plus fragmented institutions | Occupants, responders, agencies, operators, and code bodies are visible. | Preserve standing, but do not set `contradiction_flag: active` without a source-backed assumption and validation burden. |
| S3 domain-remedy absorber | The fixture centers fire/life-safety code, materials, sprinklers, pyrotechnics, egress, inspection, and emergency response. | Record the absorber or choose no-action/defer; do not convert domain remedies into this candidate's correction route. |
| S4 lower-owner routing pressure | If any route is recorded, the lowest fitting owners are domain-specific. | `lowest_fitting_owner_route` must not point to this repository unless no lower owner fits, and that reason must be explicit. |

## Pass Conditions

The P3 score may record a bounded pass only if the typed register:

- refuses the Station negative absorber as positive evidence for `CMD-0001`;
- preserves source fixture, affected standing, and absorber context without
  copying source artifacts or adding source claims;
- blocks severity-only, affected-standing-only, and complexity-only register
  completion;
- keeps domain-remedy and correction ownership outside this repository; and
- does not authorize graduation, transfer, broader proving, deployment,
  participation, field testing, incentives, spin-out, or external action.

## Permitted Conclusion

The next score may conclude only one of:

- the typed register survives this source-backed negative absorber as a bounded
  refusal;
- the typed register overgeneralizes and requires revision or kill
  disposition; or
- the fixture is not fit for this candidate and the candidate returns to defer.

No graduation, destination-owner transfer, public recommendation, deployment,
human or field testing, participation, account, incentive, spin-out, domain
remedy, or destination-owner obligation is authorized by this plan.
