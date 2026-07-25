---
proving_id: CMD-0001-P6
candidate_id: CMD-0001
status: scored_bounded_revision_coherence_pass_deferred
created: 2026-07-24
fixture: synthetic_two_state_source_revision_trace
external_action: none
---

# CMD-0001-P6 - Source-Revision Coherence Test

## Boundary

This is a repository-local synthetic integrity test. It creates no claim that
the source inquiry changed and does not reopen, reinterpret, or add facts to
CAI Systemic Failure's source truth. `P6-SOURCE-R1` and `P6-SOURCE-R2` are
synthetic revision markers only.

The test asks whether `CMD-0001` can distinguish a current source pointer from
the source revision that actually received validation. It does not test
effectiveness, adoption, a destination-owner schema, real records, human
behavior, field conditions, deployment, or a domain remedy.

## Why The Local Integrity Gate Reopens

The candidate says that later source corrections require explicit review and
that changed evidence cannot silently inherit an old assumption. Its typed
minimum rules do not yet enforce that promise:

- `source_revision` records only the current pointer, not its predecessor;
- `validation_status` does not name the source revision it evaluated; and
- `change_event_type: none` remains formally valid after `source_revision`
  changes.

This is a concrete internal paperwork absorber, not a request for another
source fixture or another proving count.

## Frozen Adversarial Trace

The facts remain fixed across the baseline score and repaired rerun:

1. At state A, source marker `P6-SOURCE-R1` is validated.
2. At state B, the row points to `P6-SOURCE-R2`.
3. No validation has been performed against `P6-SOURCE-R2`.
4. The assumption, affected system, affected-party standing, and lower owner
   route are otherwise unchanged.

Under the pre-P6 rules, state B can be represented as:

```yaml
assumption_id: P6-ASSUMPTION-01
source_revision: P6-SOURCE-R2
assumption_owner: synthetic_source_owner
review_owner: synthetic_lower_review_owner
affected_system: synthetic_interface
affected_party_standing: synthetic_exposed_party
change_event_type: none
change_event_source: P6-STATE-B
validation_environment: baseline
validation_status: valid
contradiction_flag: none
lowest_fitting_owner_route: synthetic_lower_review_owner
correction_route: synthetic_lower_review_owner
stop_condition: defer
```

Every required field is present, and none of the pre-P6 row rules rejects this
representation, even though `valid` belongs only to `P6-SOURCE-R1`.

## Failure And Pass Conditions

The baseline fails if state B can inherit `valid` without exposing the source
transition or validation-basis mismatch.

The repaired contract passes only if it:

- records the previous and current source revisions as typed values;
- allows `initial` only on the first recorded state of the assumption;
- binds validation status to the revision actually reviewed;
- makes a source change a typed change event;
- marks unmatched validation stale or unvalidated and exposes a possible or
  active contradiction;
- preserves the lowest-fitting owner and correction or stop route; and
- adds no source fact, central review authority, destination obligation, or
  consequential action.

## Recovery And Ownership

If the repaired fields can still launder validation, invalidate the P6 pass,
preserve the failing trace, and keep the candidate revision-required or kill
it. CAI Mechanism Design owns this test, candidate repair, score, and
disposition. Source owners retain their source truth and correction authority.

## Result

`CMD-0001-P6-source-revision-coherence-score.md` preserves the baseline false
pass, applies the minimal typed repair, and reruns these same synthetic facts.
The revised contract earns a bounded coherence pass and returns the candidate
to defer.
