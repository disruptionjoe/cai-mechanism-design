---
score_id: CMD-0001-P4-S2
candidate_id: CMD-0001
proving_id: CMD-0001-P4
status: scored_bounded_mixed_translation_pass
created: 2026-07-20
source_fixture: cai-systemic-failure/topology/SF-MIX-0001-fukushima-tsunami-design-basis.md
source_owner_revision: 19c21cadd971d11075583a681e1390a012f1c85a
source_fixture_sha256: b6f34484f75981c6285e137be063db8b91b263eda6f83d4c6e05518d0d59b890
wrapper: proving/CMD-0001-P4-typed-translation-wrapper.md
external_action: none
---

# CMD-0001-P4 Mixed-Fixture Rerun Score

## Boundary

This rerun uses the same frozen fixture, revision, and hash as P4-S1. The only
changed input is the minimal typed translation wrapper required by the revise
disposition. No source-owner artifact, source claim, operational register field,
or domain route changed.

## Wrapper Validation

| Check | Result | Reason |
|---|---|---|
| `source_owner_fit_status` is typed | Pass | The frozen row records `mixed`, within the closed enum. |
| `absorber_or_counterevidence` is typed | Pass | The frozen row carries a non-empty list of the fixture's named domain boundaries. |
| Mixed status cannot use `none_named` | Pass | Seven source-owner-scoped absorber classes remain explicit. |
| Prose cannot substitute for either field | Pass | Both values are required in the structured row and have explicit failure rules. |
| Source ownership remains intact | Pass | Values are pinned to the source-owner revision and hash and are not independent claims. |

## Frozen P4 Rerun

| P4 condition | Result | Reason |
|---|---|---|
| Preserve ambiguity rather than count ordinary positive evidence | Pass | `source_owner_fit_status: mixed` is typed and cannot disappear into narrative. |
| Tie translated values to the source fixture without adding claims | Pass | The wrapper pins the unchanged fixture path, full revision, and SHA-256. |
| Keep remedies and accountable routes outside this repository | Pass | Domain absorbers remain explicit competing explanations; the prior lower-owner routes are unchanged. |
| Expose unresolved validation and contradiction state | Pass | P4-S1's safe `unknown` validation and `possible` contradiction readings remain unchanged. |
| Create no consequential or external action | Pass | The wrapper and score are repository-local, reversible translation artifacts. |

## Result

Disposition: bounded pass and defer.

The wrapper repairs the exact translation-boundary paperwork gap exposed by
P4-S1. It does not prove the candidate, convert the Fukushima fixture into an
ordinary positive record, accept another owner's schema, or establish that the
operational register is ready for deployment.

No graduation, transfer, deployment, participation, field test, incentive,
institution, spin-out, domain remedy, destination obligation, or external
action is authorized.
