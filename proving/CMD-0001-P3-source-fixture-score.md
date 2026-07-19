---
score_id: CMD-0001-P3-S1
candidate_id: CMD-0001
proving_id: CMD-0001-P3
status: scored_bounded_refusal_defer
created: 2026-07-19
source_fixture: cai-systemic-failure/topology/SF-ABS-0003-negative-absorber-station-nightclub.md
source_owner_revision: d6cf8fe
external_action: none
---

# CMD-0001-P3 Source Fixture Score

## Boundary

This score uses only the P3 translation constraints imported from CAI Systemic
Failure's `SF-ABS-0003` source fixture. It does not copy source artifacts,
expand source synthesis, make fire-safety findings, contact parties, run field
work, deploy a mechanism, or create a destination-owner obligation.

The question is not whether the Station nightclub record matters. The question
is whether `CMD-0001` overgeneralizes by treating severe public harm, affected
standing, or institutional complexity as positive evidence for an
assumption-drift register when the source fixture centers a different absorber.

## Row Scores

| Row | Expected typed behavior | Score | Reason |
|---|---|---|---|
| S1 severe public harm with no source-backed changed assumption | Refuse positive fit; no row may pass by filling `change_event_type` from severity alone. | Pass | The typed register requires a source-backed change event. The fixture pressure is grave, but severity alone is not a valid `change_event_type`. |
| S2 affected standing plus fragmented institutions | Preserve standing, but do not set `contradiction_flag: active` without a source-backed assumption and validation burden. | Pass | Occupant, injured-person, responder, and public-agency standing can remain visible as affected-party context without becoming an active assumption-drift contradiction row. |
| S3 domain-remedy absorber | Record the absorber or choose no-action/defer; do not convert domain remedies into this candidate's correction route. | Pass | Fire/life-safety code, materials, sprinklers, pyrotechnics, egress, inspection, and emergency-response issues remain outside this repository's correction authority. |
| S4 lower-owner routing pressure | If any route is recorded, the lowest fitting owners are domain-specific. | Pass | The fixture gives no source-backed reason that no lower owner fits, so `lowest_fitting_owner_route` cannot point to this repository as the accountable route. |

## Pass-Condition Score

| Condition from plan | Score | Reason |
|---|---|---|
| Refuse the Station negative absorber as positive evidence for `CMD-0001`. | Pass | The typed register refuses positive fit unless the source fixture supplies assumption reuse under changed conditions. |
| Preserve source fixture, affected standing, and absorber context without copying artifacts or adding source claims. | Pass | The score cites only the fixture path, source-owner revision, and imported P3 constraints. |
| Block severity-only, affected-standing-only, and complexity-only register completion. | Pass | None of those pressures can fill `change_event_type`, `validation_status`, and `contradiction_flag` as a positive row. |
| Keep domain-remedy and correction ownership outside this repository. | Pass | The score treats domain correction as belonging to domain owners, not to CAI Mechanism Design. |
| Avoid graduation, transfer, broader proving, deployment, participation, field testing, incentives, spin-out, or external action. | Pass | This score records only a bounded refusal and defer disposition. |

## Result

Disposition for this third proving test: bounded refusal, defer.

The typed minimum register survives this source-backed negative absorber by
refusing to absorb the Station fixture as positive evidence. That is useful
negative evidence against overgeneralization, not positive evidence that the
candidate should graduate, transfer, deploy, or become a domain remedy.

## Residual Risks

- The result depends on the P3 imported fixture constraints and does not audit
  the source owner's source set.
- A future ambiguous fixture could include both domain-remedy pressure and a
  source-backed changed assumption; this score does not settle that case.
- Bad implementers could still fill typed fields with low-quality source or
  owner routes; this test checks refusal of a negative absorber, not source
  quality.

## Next Condition

Keep `CMD-0001` admitted but deferred. Reopen only if a source-backed positive
or ambiguous assumption-reuse fixture exists, a destination owner explicitly
asks for synthetic translation review, or stewardship finds a narrower owner or
safer home.

No external action, human or field testing, deployment, participation, account,
incentive, spin-out, domain remedy, transfer, graduation, or destination-owner
obligation is authorized.
