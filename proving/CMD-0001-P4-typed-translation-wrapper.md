---
wrapper_id: CMD-0001-P4-W1
candidate_id: CMD-0001
proving_id: CMD-0001-P4
status: active_bounded_wrapper
created: 2026-07-20
source_fixture: cai-systemic-failure/topology/SF-MIX-0001-fukushima-tsunami-design-basis.md
source_owner_revision: 19c21cadd971d11075583a681e1390a012f1c85a
source_fixture_sha256: b6f34484f75981c6285e137be063db8b91b263eda6f83d4c6e05518d0d59b890
external_action: none
---

# CMD-0001-P4 Typed Translation Wrapper

## Boundary

This wrapper is separate from CAI Systemic Failure source truth and from the
operational assumption-drift register. It carries only the source owner's fit
classification and source-backed competing explanations needed to prevent a
translation row from hiding mixed status in prose.

It cannot change the source classification, add source claims, prescribe a
domain remedy, select a destination owner, or authorize consequential proving.

## Required Typed Fields

| Field | Type | Failure rule |
|---|---|---|
| `source_owner_fit_status` | exactly one of `positive`, `mixed`, `refused`, or `unresolved` | Fail if absent, outside the enum, or supplied only in prose. |
| `absorber_or_counterevidence` | non-empty list of typed competing-explanation objects, or exactly `none_named` | Each object requires `explanation`, `basis`, `claim_posture`, and `residue_effect`. `basis` is source context, an explicit synthetic basis, or `not_available`; `not_available` requires `residue_effect: lead_only`. `claim_posture` is `supported`, `source_thin`, `contradicted`, `synthetic`, or `unresolved`; `residue_effect` is `absorbs`, `narrows`, `does_not_kill`, or `lead_only`. Fail if absent, supplied only in prose, or represented as an ungraded string. `mixed` and `refused` may not use `none_named`. |

The wrapper fails if it restates a domain absorber as a generic mechanism claim
or changes a source-owner classification without a new pinned source-owner
revision.

## Frozen P4 Wrapper Row

```yaml
wrapper_id: CMD-0001-P4-W1
register_row_ref: CMD-0001-P4-FUKUSHIMA-MIXED-01
source_fixture: cai-systemic-failure/topology/SF-MIX-0001-fukushima-tsunami-design-basis.md
source_owner_revision: 19c21cadd971d11075583a681e1390a012f1c85a
source_fixture_sha256: b6f34484f75981c6285e137be063db8b91b263eda6f83d4c6e05518d0d59b890
source_owner_fit_status: mixed
absorber_or_counterevidence:
  - {explanation: nuclear_safety, basis: "SF-MIX-0001 named boundary", claim_posture: supported, residue_effect: absorbs}
  - {explanation: tsunami_hazard, basis: "SF-MIX-0001 named boundary", claim_posture: supported, residue_effect: absorbs}
  - {explanation: severe_accident, basis: "SF-MIX-0001 named boundary", claim_posture: supported, residue_effect: absorbs}
  - {explanation: emergency_response, basis: "SF-MIX-0001 named boundary", claim_posture: supported, residue_effect: absorbs}
  - {explanation: regulatory, basis: "SF-MIX-0001 named boundary", claim_posture: supported, residue_effect: absorbs}
  - {explanation: health, basis: "SF-MIX-0001 named boundary", claim_posture: supported, residue_effect: absorbs}
  - {explanation: legal, basis: "SF-MIX-0001 named boundary", claim_posture: supported, residue_effect: absorbs}
```

These values translate the pinned fixture's own mixed classification and named
domain boundaries. They are not independent findings by this repository.
