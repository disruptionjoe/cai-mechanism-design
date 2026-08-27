---
artifact_type: synthetic_mechanism_alternative_map_current_condition_no_route_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Mechanism Alternative-Map Current-Condition No-Route-Authority Boundary Fixture

## Use Boundary

Use this fixture to preserve a source-current partial dominance relation while
keeping comparison authority separate from route-selection, acceptance,
admission, disposition, and execution authority. It maps synthetic evidence
only. It does not choose or perform a route, admit or disposition a candidate,
modify or reopen `CMD-0001`, or authorize external action.

## Map Header

| Field | Value |
| --- | --- |
| `map_id` | `SYNTH-CURRENT-CONDITION-NO-ROUTE-AUTHORITY-MAP-001@r2` |
| `source_inquiry` | `SYNTH-SOURCE-CURRENT-CONDITION-NO-ROUTE-001@r2` |
| `source_revision` | `synthetic-source-revision:current-condition-no-route-001-r2` |
| `candidate_or_problem_ref` | `SYNTH-PROBLEM-CURRENT-CONDITION-NO-ROUTE-001@r2` |
| `map_owner` | `synthetic-mechanism-map-owner` |
| `authorization_ref` | `synthetic-alternative-map-preparation@r2` |
| `candidate_in_scope` | `none` |
| `external_action` | `none` |

## Frozen Inquiry And Candidate Boundary

- Exact problem: one frozen synthetic correction record needs a pointer-only
  return.
- Included scope: the record's immutable pointer, checksum, acknowledgment
  state, visibility timing, verification dependency, current condition
  evidence, stops, correction, and recovery.
- Excluded scope: native content, real owners or people, effectiveness,
  adoption, deployment, and external action.
- Candidate in scope: `none`.
- Prohibited inference: the comparison cannot select, accept, route, admit,
  disposition, authorize, or execute an alternative.

## Alternative Records

### No action — `SYNTH-ALT-CURRENT-NO-ACTION-001@r2`

- Mechanism: preserve the invisible return without copied fields or
  synchronization; the correction remains orphaned.
- Owner route: unresolved.
- Intended effect: preserve the frozen record while creating no route.
- Failure mode: the correction remains invisible and orphaned.
- Stop: any source, authority, standing, custody, content, condition,
  acceptance, or risk revision.
- Correction and recovery: preserve the record and create no route.

### Immediate pointer visibility — `SYNTH-ALT-CURRENT-IMMEDIATE-001@r2`

- Mechanism: expose the immutable pointer, checksum, correction owner, stop,
  and acknowledgment state when the return surface opens.
- Data boundary: copy no native content and add no synchronization.
- Intended effect: earlier pointer-only visibility.
- Failure modes: comparison authority treated as route authority, or
  acknowledgment treated as acceptance.
- Stop: any source, authority, standing, custody, content, condition,
  acceptance, or risk revision.
- Correction and recovery: remove the proposed route and preserve the record.

### Verified pointer visibility — `SYNTH-ALT-CURRENT-VERIFIED-001@r2`

- Mechanism: expose the same pointer-only fields only after an independent
  checksum match.
- Data boundary: copy no native content and add no synchronization.
- Reviewer authority: the reviewer has no owner or acceptance authority.
- Intended effect: verified pointer-only visibility after review.
- Failure modes: review delay, false reviewer authority, or acknowledgment
  treated as acceptance.
- Stop: any source, authority, standing, custody, content, condition,
  acceptance, or risk revision.
- Correction and recovery: remove the proposed route and preserve the record.

## Material Difference And Nonduplication

No action preserves invisibility and creates no route. The immediate and
verified alternatives expose the same bounded fields but differ materially in
visibility timing and independent-checksum dependency. They remain distinct:
the current record supports immediate-route dominance over verified routing on
the required-timing dimension, while the verified route remains visible as a
dominated alternative and negative evidence. None is merged, and no broader
overall winner, parity, probability, expected value, weight, or common utility
scale is supplied.

## Existing-Owner Fit

The better-existing-owner result is `unresolved`. Interest, expertise,
convenience, mailbox material, source payloads, and the comparison record do
not create owner authority. The incubator remainder is preservation of the
bounded comparison and missing-route boundary only; existing-owner fit still
defeats admission if later established.

## Evidence, Affected Parties, And Legitimacy

All evidence is synthetic. One synthetic reviewer role represents standing;
no real affected party, route owner, destination owner, or acceptance owner is
represented. The map cannot speak for any real party or owner. Preserve the
comparison at
`synthetic://map-evidence/SYNTH-CURRENT-CONDITION-NO-ROUTE-001@r2` and the
missing-route boundary at
`synthetic://route-boundary/SYNTH-CURRENT-CONDITION-NO-ROUTE-001@r2`.
Acknowledgment is not acceptance, reviewer status is not owner authority, and
no real data, contact, deployment, or external action is in scope.

## Comparative Boundary

Immutable record `SYNTH-CONDITION-IMMEDIATE-REQUIRED-002@r2` is signed by
`synthetic-condition-owner` under
`synthetic-condition-comparison-authority@r2` and is valid for source revision
`synthetic-source-revision:current-condition-no-route-001-r2`. The current
source revision, checksum custody, pointer, and condition record all match.
The record requires visibility before independent checksum review and makes
the immediate route dominate the verified route on required timing only.

Its exact scope authorizes recording that comparison relation only. It
expressly does not select, accept, route, admit, disposition, authorize, or
execute either alternative and supplies no destination-owner acceptance. The
verified route remains visible as a materially distinct dominated alternative
on the supplied dimension. No immutable route-selection or acceptance record
exists, so no route may be chosen or performed.

## Prepared Return

- Return: `defer`.
- Rationale: current evidence supports one comparison relation but supplies no
  route-selection or acceptance authority.
- Negative-evidence preservation:
  `synthetic://map-evidence/SYNTH-CURRENT-CONDITION-NO-ROUTE-001@r2` preserves
  the dominated verified route, and
  `synthetic://route-boundary/SYNTH-CURRENT-CONDITION-NO-ROUTE-001@r2`
  preserves the missing authority boundary.
- Stops: any revision to source, pointer, checksum, custody, standing,
  condition, acceptance, authority, or risk.
- Correction and recovery: remove any proposed route, preserve the frozen
  record and both evidence pointers, and create no route.
- Exact next wake: one immutable destination-owner route-selection and
  acceptance record, or a revision to source, pointer, checksum, custody,
  standing, condition, acceptance, or risk.
- Prohibited interpretations: this return is not admission, selection,
  routing, disposition, owner acceptance, or execution.

## Frontier Verification

- Verify the current source revision, checksum custody, pointer, and condition
  record all match.
- Confirm `synthetic-condition-comparison-authority@r2` authorizes comparison
  only and does not supply route authority.
- Confirm no immutable route-selection or destination-owner acceptance record
  exists.
- Confirm the dominated verified alternative remains visible as distinct
  negative evidence on the supplied timing dimension.
- Confirm the prepared return is `defer`, with every stop, correction,
  recovery, evidence pointer, non-effect, and exact wake preserved.
- Confirm `CMD-0001`, P7 defer, candidate status, and external-action state are
  unchanged.
