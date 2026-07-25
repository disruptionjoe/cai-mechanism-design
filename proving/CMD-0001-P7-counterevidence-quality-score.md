---
score_id: CMD-0001-P7-S1
candidate_id: CMD-0001
proving_id: CMD-0001-P7
status: scored_bounded_counterevidence_quality_pass
created: 2026-07-25
fixture: synthetic_generic_alternative_trace
external_action: none
---

# CMD-0001-P7 Counterevidence-Quality Score

## Baseline Negative Evidence

The frozen trace passes the pre-P7 wrapper solely because a non-empty string
list exists:

| Pre-P7 check | Result | Why this is insufficient |
|---|---|---|
| Counterevidence list is present | Pass | Generic alternatives can be named without an inspectable basis. |
| Source-backed wording exists | Claimed, not tested | The wrapper holds no source or synthetic-basis field. |
| Alternative has a claim posture | Not required | A reader cannot distinguish lead, contradiction, or support. |
| Effect on residue is stated | Not required | An alternative can look absorbing without saying whether it absorbs anything. |

Baseline disposition: revision required. A generic alternative is a legitimate
lead, but it cannot be recorded as counterevidence that narrows or absorbs the
candidate residue.

## Minimal Contract Revision

The P4 translation wrapper now represents each `absorber_or_counterevidence`
item as a typed object containing `explanation`, `basis`, `claim_posture`, and
`residue_effect`. `basis` is source context, an explicit synthetic basis, or
`not_available`; `not_available` forces `lead_only`. A mixed or refused row
must have one or more objects, and the wrapper rejects generic string items.

## Frozen Trace Rerun

The underlying facts are unchanged; no evidence has been invented. The generic
alternatives remain possible but become explicit leads:

```yaml
source_owner_fit_status: mixed
absorber_or_counterevidence:
  - explanation: operator_error
    basis: not_available
    claim_posture: unresolved
    residue_effect: lead_only
  - explanation: resource_scarcity
    basis: not_available
    claim_posture: unresolved
    residue_effect: lead_only
  - explanation: technical_defect
    basis: not_available
    claim_posture: unresolved
    residue_effect: lead_only
```

| P7 pass condition | Result | Reason |
|---|---|---|
| Generic alternatives remain visible | Pass | Each remains a named unresolved lead. |
| Basis is inspectable | Pass | `not_available` makes the missing basis visible rather than implied. |
| Claim posture is visible | Pass | None silently becomes supported counterevidence. |
| Residue effect is bounded | Pass | `lead_only` cannot absorb or narrow the candidate. |
| No authority or action is added | Pass | The trace is local and synthetic; source truth and all domain remedies remain outside this repository. |

## Result

Disposition: bounded pass and defer. The repair closes the exact
counterevidence-quality asymmetry while preserving generic alternatives as
uncertainty rather than overclaiming their force. It does not prove
effectiveness, validate a real record, establish destination fit, authorize
transfer or graduation, or authorize consequential proving.
