---
candidate_id: CMD-0001
status: admitted_deferred_after_p4_bounded_mixed_translation_pass
lane: "1"
source_inquiry: cai-systemic-failure/SFQ-0001
source_inquiry_revision: f9784d7484de8f0a5cfe3344ca923a77ba1d8ea8
created: 2026-07-18
external_action: none
---

# CMD-0001 - Source-Preserving Assumption-Drift Register

## Candidate

A source-preserving assumption-drift register is a review mechanism that records
load-bearing assumptions, their source evidence, affected systems, owner, change
events, validation method, counterevidence, and correction route. It is meant to
make contradiction visible when incremental design changes, delegated review, or
human-response assumptions alter the safety or legitimacy case.

This candidate is admitted only for synthetic, reversible design and testing. It
is not an aviation remedy, a compliance system, a deployment proposal, or an
obligation for any other owner.

## Source Inquiry

The source inquiry is `SFQ-0001` from CAI Systemic Failure at revision
`f9784d7484de8f0a5cfe3344ca923a77ba1d8ea8`, derived from the bounded public-
source record `SF-0001`. Later source-owner corrections do not silently change
the admitted basis; they require an explicit candidate review. The motivating
pattern is not "one more checklist"; it is that changed function authority,
delegated approval, and operator-response assumptions can become separated
across review artifacts.

## Theory Of Change

If a critical assumption has a named owner, source, validation burden,
affected-party impact, and correction route, then a later change cannot silently
depend on the old assumption. The register does not decide the technical answer.
It should route the contradiction to the correct accountable review before the
system treats the old assumption as still valid.

## Alternatives

- No action: preserve the failure record and do not design a mechanism.
- Ordinary checklist: cheaper, but may not preserve source revisions or owner
  fit.
- Post-incident review only: useful after harm, but does not test whether the
  contradiction could have been made visible earlier.
- Domain-specific safety-case tooling: likely better for aviation, medical, or
  other regulated settings, but outside this repo's authority.

## Owner Fit

CAI Mechanism Design owns this as a generic, otherwise-unowned candidate pattern
for synthetic evaluation. Existing domain owners defeat adoption for any real
setting. Aviation certification, rulemaking, training, and engineering control
remain with aviation authorities and domain experts.

## Affected Parties And Legitimacy Risks

Affected parties in real deployments would include system users, operators,
reviewers, producers, regulators, and people exposed to downstream harms.
Synthetic testing must represent those standing positions without pretending to
consent for them.

Risks:

- The register becomes compliance theater.
- Producers game the fields while preserving source-looking paperwork.
- A central reviewer gains unjustified authority over domain decisions.
- Sensitive or regulated evidence is pulled into an unsafe surface.
- The mechanism delays urgent stops by demanding more process.

## Evidence Route

Use only synthetic fixtures derived from `SF-0001`'s public pattern. The first
test asks whether the register detects three drifts:

1. changed function authority or input path;
2. reliance on unvalidated human response under interacting alerts; and
3. delegated review with insufficient visibility into the changed function.

Permitted conclusion: the candidate exposes and routes assumption drift in the
synthetic fixture, or it fails to do so.

## Stops

Stop or kill the candidate if it requires confidential data, real human
subjects, institutional deployment, external contact, regulatory authority, or
domain-specific judgment this repo cannot own. Also stop if the synthetic
fixture can pass by filling paperwork while leaving the contradiction invisible.

## Intended Disposition

After synthetic testing, choose kill, revise, defer, transfer, or propose
graduation. Graduation would require a destination owner, unresolved-risk
disclosure, and explicit acceptance; none exists now.

## First Synthetic Score

`proving/CMD-0001-P1-synthetic-score.md` scored the first synthetic fixture as
revision required. The candidate can expose changed-function, human-response,
and delegated-review contradictions only if typed drift events, validation
status, lowest-fitting owner routing, and correction routes are required fields.
Free-text completion remains a paperwork-theater absorber.

## Typed Minimum Register Revision

The candidate now requires a typed minimum register before any stronger
disposition can be considered. A narrative explanation may accompany a record,
but it cannot substitute for these typed fields.

### Required Fields

| Field | Required type | Paperwork-theater guard |
|---|---|---|
| `assumption_id` | stable identifier | No row can be scored without a traceable assumption. |
| `source_revision` | source pointer or synthetic fixture revision | "Reviewed" is invalid without a source revision. |
| `assumption_owner` | named role or owner class | The assumption cannot be ownerless. |
| `review_owner` | named role or owner class | The review owner must differ from a generic central reviewer unless justified. |
| `affected_system` | bounded system or interface | A record cannot hide the system affected by the assumption. |
| `affected_party_standing` | user, operator, reviewer, exposed party, or synthetic analogue | The record must preserve who carries downstream risk. |
| `change_event_type` | changed function, changed input path, changed environment, delegated review change, observation gap, or none | A material change cannot be buried in prose. |
| `change_event_source` | source pointer or synthetic row | Drift must tie back to a specific event. |
| `validation_environment` | baseline, changed alert/workload, changed operating environment, changed observation environment, or unknown | The environment cannot be silently inherited. |
| `validation_status` | valid, unvalidated, contradicted, stale, not_applicable, or unknown | A stale assumption cannot pass as valid by omission. |
| `contradiction_flag` | none, possible, active, or resolved_with_source | A live contradiction must remain visible as data. |
| `lowest_fitting_owner_route` | owner route or no_action route | The mechanism cannot escalate everything to itself. |
| `correction_route` | correction owner or stop path | The register does not decide the technical outcome. |
| `stop_condition` | kill, urgent_stop, transfer, revise, defer, no_action, or graduate_proposal | No-action, kill, transfer, and urgent stop remain legitimate. |

### Row Rules

- A row with `change_event_type` other than `none` must re-evaluate
  `validation_status`.
- A row with `validation_status: contradicted`, `stale`, or `unknown` must set
  `contradiction_flag` to `possible` or `active` unless a source-backed
  resolution exists.
- A row with `contradiction_flag: active` must name a
  `lowest_fitting_owner_route` and `correction_route`.
- A central or integrative route is valid only when no lower sovereign owner
  fits the contradiction.
- The register fails if all fields are formally filled while the contradiction
  is visible only in narrative prose.

## Second Synthetic Test

The next proving surface is
`proving/CMD-0001-P2-typed-register-hostile-paperwork-test.md`. It should test
whether the typed revision blocks a formally complete but contradiction-hiding
paperwork row before any graduation, transfer, broader proving, or destination
proposal is considered.

## Second Synthetic Score

`proving/CMD-0001-P2-synthetic-score.md` scored the typed minimum register as a
bounded pass against the hostile paperwork fixture. The candidate remains
admitted but deferred, not graduated or transferred. The next legitimate reopen
condition is a non-aerospace source-backed fixture from CAI Systemic Failure or
an explicit destination-owner request for synthetic translation review.

## Third Proving Plan

CAI Systemic Failure later supplied
`topology/SF-ABS-0003-negative-absorber-station-nightclub.md` at source-owner
revision `d6cf8fe`. That artifact is a non-aerospace, public-source negative
absorber, not a destination-owner request and not a new source claim by this
repository.

`proving/CMD-0001-P3-station-negative-absorber-translation-test.md` reopens the
candidate only for bounded source-fixture translation. The planned test asks
whether the typed register refuses the Station fixture as positive evidence
when the source-owner artifact centers fire/life-safety and protection-system
absorbers rather than source-backed assumption reuse under changed conditions.

No graduation, transfer, broader proving, deployment, participation, field
test, incentive, spin-out, domain remedy, or destination-owner obligation is
authorized by this plan.

## Third Proving Score

`proving/CMD-0001-P3-source-fixture-score.md` scored the typed register as a
bounded refusal against the Station negative absorber. The candidate survived
the test by refusing severity-only, affected-standing-only, and
complexity-only positive fit while preserving source context and keeping
domain-remedy ownership outside this repository.

`dispositions/CMD-0001-P3-defer.md` keeps `CMD-0001` admitted but deferred. The
next legitimate reopen condition is a source-backed positive or ambiguous
assumption-reuse fixture, an explicit destination-owner request for synthetic
translation review, or a later stewardship finding that identifies a narrower
owner or safer home.

No graduation, transfer, broader proving, deployment, participation, field
test, incentive, spin-out, domain remedy, or destination-owner obligation is
authorized by this score.

## Fourth Proving Plan

CAI Systemic Failure subsequently supplied the public-source mixed fixture
`topology/SF-MIX-0001-fukushima-tsunami-design-basis.md` at source-owner
revision `19c21ca`. The fixture explicitly preserves source-backed old-
assumption reuse under changed or reassessed external-hazard conditions while
refusing to count the case as an ordinary positive record.

`proving/CMD-0001-P4-fukushima-mixed-fixture-translation-test.md` therefore
reopens the candidate only for bounded translation planning. The later score
must preserve the fixture's ambiguity, source ownership, domain absorbers, and
lowest-fitting owner routes. No stronger disposition or consequential proving
is authorized.

## Fourth Proving Score

`proving/CMD-0001-P4-mixed-fixture-score.md` found a translation-boundary
failure. The register can preserve provisional validation, possible
contradiction, stop state, and lower domain-owner routes, but it has no typed
field for the source owner's mixed-fit classification or for domain absorbers
and counterevidence.

`dispositions/CMD-0001-P4-revise.md` therefore requires a separate minimal
translation wrapper before P4 is rerun. The candidate remains admitted and
revision-required; it is not graduated, transferred, deployed, or made into a
domain remedy.

## Fourth Proving Rerun

`proving/CMD-0001-P4-typed-translation-wrapper.md` adds typed
`source_owner_fit_status` and `absorber_or_counterevidence` values outside both
source truth and the operational register. The same frozen fixture then earns a
bounded translation pass in
`proving/CMD-0001-P4-mixed-fixture-rerun-score.md` because mixed status and
domain absorbers can no longer be hidden in prose.

`dispositions/CMD-0001-P4-defer.md` keeps the candidate admitted and deferred.
The wrapper does not validate deployment, change another owner's truth, or
authorize a stronger disposition.
