---
score_id: CMD-0001-P6-S1
candidate_id: CMD-0001
proving_id: CMD-0001-P6
status: scored_bounded_revision_coherence_pass
created: 2026-07-24
fixture: synthetic_two_state_source_revision_trace
external_action: none
---

# CMD-0001-P6 Source-Revision Coherence Score

## Baseline Negative Evidence

The frozen state-B representation in the P6 plan passes every pre-P6 required
field and row rule:

| Pre-P6 check | Result | Why this is insufficient |
|---|---|---|
| Current source pointer exists | Pass | It records `P6-SOURCE-R2` but not the prior revision. |
| Changed event triggers revalidation | Not triggered | `change_event_type: none` remains allowed because revision difference is not typed. |
| Validation status is present | Pass | `valid` does not name the revision it evaluated. |
| Stale status exposes contradiction | Not triggered | The row launders the old validation as current rather than declaring it stale. |
| Lower owner and correction route exist | Pass | Correct routing does not repair the hidden validation-basis mismatch. |

Baseline disposition: revision required.

This negative result is preserved because a formally complete state-B row can
present the old validation as current. Narrative knowledge that a source
changed does not satisfy the candidate's own typed contradiction-visibility
theory.

## Minimal Contract Revision

The candidate now adds:

- `previous_source_revision`, exactly one prior source pointer or `initial`;
- `validation_basis_revision`, the source revision actually reviewed or
  `not_validated`; and
- `source_revision_change` as a typed `change_event_type`.

The row rules now require a non-initial source revision difference to emit
`source_revision_change`, and allow `validation_status: valid` only when
`validation_basis_revision` equals `source_revision`. A mismatch must be
`stale` or `unvalidated`, carry `contradiction_flag: possible` or `active`, and
retain a lower owner plus correction or stop route. `initial` is valid only for
an assumption's first recorded state; later states must name the immediately
preceding source revision.

## Frozen Trace Rerun

The underlying facts are unchanged: R1 was validated, R2 is current, and R2
has not been validated.

```yaml
assumption_id: P6-ASSUMPTION-01
previous_source_revision: P6-SOURCE-R1
source_revision: P6-SOURCE-R2
validation_basis_revision: P6-SOURCE-R1
assumption_owner: synthetic_source_owner
review_owner: synthetic_lower_review_owner
affected_system: synthetic_interface
affected_party_standing: synthetic_exposed_party
change_event_type: source_revision_change
change_event_source: P6-SOURCE-R2
validation_environment: baseline
validation_status: stale
contradiction_flag: possible
lowest_fitting_owner_route: synthetic_lower_review_owner
correction_route: synthetic_lower_review_owner
stop_condition: defer
```

| P6 pass condition | Result | Reason |
|---|---|---|
| Preserve previous and current source revisions | Pass | R1 and R2 are separate required typed values. |
| Bind validation to the reviewed revision | Pass | `validation_basis_revision: P6-SOURCE-R1` cannot masquerade as R2 validation. |
| Expose the source transition | Pass | The unequal revisions require `source_revision_change`. |
| Expose unmatched validation | Pass | The row is `stale` with a `possible` contradiction. |
| Preserve lower routing and stop | Pass | Review, correction, and defer remain with the synthetic lower owner route. |
| Avoid added authority or action | Pass | The trace is local and synthetic; no source, destination, or external effect occurs. |

## Result

Disposition: bounded pass and defer.

The repair closes the exact source-revision laundering path exposed by the
baseline trace. It does not prove real-world effectiveness, approve a schema,
establish destination fit, validate `P6-SOURCE-R2`, or authorize broader or
consequential proving.
