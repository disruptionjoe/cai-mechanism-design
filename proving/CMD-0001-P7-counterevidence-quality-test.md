---
proving_id: CMD-0001-P7
candidate_id: CMD-0001
status: scored_bounded_counterevidence_quality_pass_deferred
created: 2026-07-25
source_fixture: cai-systemic-failure/topology/SF-CEQ-0001-counterevidence-quality-asymmetry.md
source_owner_revision: 6fd348f08664a142749b0cd5e4c2697370a9284a
source_fixture_sha256: 11cebd1be0903462f30a7ce568bcb7b07fc514a2338c6774ff8ea9bcc9d9cc41
external_action: none
---

# CMD-0001-P7 - Counterevidence-Quality Test

## Boundary

This is a repository-local, synthetic integrity test prompted by the
source-owner's bounded `SF-CEQ-0001` falsifier. It does not add, reinterpret,
or rank CAI Systemic Failure records; the source fixture supplies only the
pressure that a generic alternative must not perform the appearance of
counterevidence.

The test does not examine source revisions, effectiveness, adoption,
destination-owner schemas, real records, human behavior, field conditions,
deployment, or a domain remedy.

## Why The Local Integrity Gate Reopens

`CMD-0001-P4-W1` requires a non-empty `absorber_or_counterevidence` list for a
mixed or refused translation. It calls every list entry source-backed and
owner-scoped but represents each as an untyped string. A row can therefore
name `operator error`, `resource scarcity`, or `technical defect` and claim
the counterevidence gate passed without exposing whether that alternative is
source-backed, synthetic, source-thin, contradicted, unresolved, or relevant
to the candidate residue.

This is a distinct counterevidence-quality gap, not another source-revision
test and not proving volume for its own sake.

## Frozen Adversarial Trace

The facts remain fixed across the baseline score and repaired rerun:

1. A safely shareable synthetic packet carries an apparent assumption-reuse
   fit, changed condition, validation burden, affected standing, review path,
   and correction route.
2. The row names only generic alternatives: operator error, resource scarcity,
   and technical defect.
3. No alternative has source context, synthetic basis, evidence pointer, claim
   posture, or stated effect on the apparent residue.
4. The row nevertheless marks the counterevidence gate passed.

Under the pre-P7 wrapper, this representation can pass:

```yaml
source_owner_fit_status: mixed
absorber_or_counterevidence:
  - operator_error
  - resource_scarcity
  - technical_defect
```

The required field exists and is non-empty; none of the old wrapper rules
forces its items to be inspectable counterevidence.

## Failure And Pass Conditions

The baseline fails if generic, ungraded alternatives can be treated as a
passed counterevidence gate.

The repaired contract passes only if every item names:

- its narrower explanation;
- source context, an explicit synthetic basis, or an explicit `not_available`;
- claim posture (`supported`, `source_thin`, `contradicted`, `synthetic`, or
  `unresolved`); and
- its stated effect (`absorbs`, `narrows`, `does_not_kill`, or `lead_only`) on
  the candidate residue.

An item with `not_available` basis must be `lead_only`; it cannot absorb or
narrow the residue. A source-backed mixed or refused row needs at least one
item that can be inspected; otherwise it fails rather than performing
skepticism. These rules do not require equal evidence, exhaustive search, or
that absent counterevidence imply the candidate is true.

## Recovery And Ownership

If ungraded generic alternatives can still pass, invalidate P7, preserve the
failing trace, and retain revision-required or kill disposition. CAI Mechanism
Design owns this synthetic test, wrapper repair, score, and disposition; CAI
Systemic Failure retains source truth and its falsifier verdict.

## Result

`CMD-0001-P7-counterevidence-quality-score.md` preserves the baseline false
pass, adds the minimum typed item contract, and reruns these same facts. The
repaired contract earns only a bounded pass and leaves the candidate deferred.
