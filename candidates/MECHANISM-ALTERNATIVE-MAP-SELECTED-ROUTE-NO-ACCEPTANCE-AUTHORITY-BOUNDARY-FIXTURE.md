---
artifact_type: synthetic_mechanism_alternative_map_selected_route_no_acceptance_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---
# Synthetic Mechanism Alternative-Map Selected-Route No-Acceptance-Authority Boundary Fixture

## Use Boundary

This synthetic fixture preserves a supported partial dominance relation and an
authorized prepared selection while keeping comparison, selection, destination-
owner acceptance, admission, disposition, and execution separate. Authority
operates only over the decision and effect named in its exact scope. The map
does not admit, reject, revise, contact, route, test, execute, or disposition a
candidate. It does not modify or reopen `CMD-0001`. External action is `none`.

## Map Header

- Map: `SYNTH-SELECTED-ROUTE-NO-ACCEPTANCE-MAP-001@r1`.
- Inquiry: `SYNTH-SOURCE-SELECTED-ROUTE-NO-ACCEPTANCE-001@r1`.
- Source revision: `synthetic-source-revision:selected-route-no-acceptance-001-r1`.
- Problem: `SYNTH-PROBLEM-SELECTED-ROUTE-NO-ACCEPTANCE-001@r1`.
- Map owner: `synthetic-mechanism-map-owner`.
- Preparation authority: `synthetic-alternative-map-preparation@r1`.
- Candidate in scope: `none`.
- External action: `none`.

## Frozen Inquiry And Candidate Boundary

One frozen synthetic correction record needs a pointer-only return. Included
scope is its immutable pointer, checksum, acknowledgment state, visibility
timing, independent-verification dependency, comparison record, route-selection
record, stops, correction, and recovery. Native content, real owners or people,
destination-owner acceptance, route opening, effectiveness, adoption,
deployment, and external action are excluded.

## Alternative Records

### No action

`SYNTH-ALT-SELECTED-NO-ACTION-001@r1` preserves the invisible return, adds no
copied fields or synchronization, and leaves the correction orphaned. Its owner
route is unresolved. It stops on any source, authority, standing, custody,
content, condition, selection, acceptance, or risk revision. Recovery preserves
the record and creates no route.

### Immediate pointer-only route

`SYNTH-ALT-SELECTED-IMMEDIATE-001@r1` would expose the immutable pointer,
checksum, correction owner, stop, and acknowledgment state when the return
surface opens. It copies no native content and adds no synchronization. Its
failure modes are selection treated as acceptance, a prepared pointer treated
as an opened route, and acknowledgment treated as acceptance. Recovery removes
the prepared route and preserves the record.

### Independently verified pointer-only route

`SYNTH-ALT-SELECTED-VERIFIED-001@r1` would expose the same pointer-only fields
only after an independent checksum match. It copies no native content and adds
no synchronization. The reviewer has no owner or acceptance authority. Its
failure modes are review delay, false reviewer authority, and acknowledgment
treated as acceptance. Recovery removes the prepared route and preserves the
record.

## Material Difference And Nonduplication

The immediate and verified routes share the same pointer-only payload but
differ on a load-bearing mechanism: whether visibility precedes or follows an
independent checksum match. The verified route therefore remains materially
distinct and visible as dominated negative evidence on the supplied timing
dimension. No probability, expected value, parity, weight, common utility
scale, affected-party preference, or overall outcome is inferred.

## Existing-Owner Fit

Better-existing-owner fit is `unresolved`. A selected prepared route, interest,
expertise, convenience, mailbox material, and source payloads do not create an
owner or acceptance authority. The map supports `defer`, not admission,
routing, execution, or disposition.

## Evidence, Affected Parties, And Legitimacy

All evidence is synthetic. One synthetic reviewer role represents standing;
no real affected party, route owner, or destination owner is represented. The
comparison and selected-route evidence is preserved at
`synthetic://map-evidence/SYNTH-SELECTED-ROUTE-NO-ACCEPTANCE-001@r1`. The
missing-acceptance boundary is preserved at
`synthetic://acceptance-boundary/SYNTH-SELECTED-ROUTE-NO-ACCEPTANCE-001@r1`.
Neither pointer supplies consent, standing, owner fit, acceptance, or action.

## Comparative Boundary

Immutable record `SYNTH-CONDITION-IMMEDIATE-REQUIRED-003@r1` is signed by
`synthetic-condition-owner` under
`synthetic-condition-comparison-authority@r1` and is valid for source revision
`synthetic-source-revision:selected-route-no-acceptance-001-r1`. It requires
visibility before independent checksum review and makes the immediate route
dominate the verified route on required timing. Its exact scope authorizes only
recording that comparison relation; it supplies no route-selection,
acceptance, admission, disposition, or execution authority.

Later immutable record `SYNTH-ROUTE-SELECTION-IMMEDIATE-001@r1` is signed by
`synthetic-route-selection-owner` under
`synthetic-route-selection-authority@r1`. Its exact scope selects
`SYNTH-ALT-SELECTED-IMMEDIATE-001@r1` for one prepared pointer-only handoff and
rejects no alternative. It does not supply destination-owner acceptance, open
or perform a route, authorize contact, copy native content, admit or
disposition a candidate, or execute any effect. Selection expires on any
source, pointer, checksum, custody, standing, comparison, selection,
acceptance, authority, or risk revision.

The current source revision, checksum custody, pointer, comparison record, and
selection record all match. No immutable destination-owner route-acceptance
record exists. The selected immediate route therefore remains a non-operative
prepared pointer and may not be opened, sent, contacted, or performed.

## Prepared Return

The supported prepared return is `defer`. Stop on any source, authority,
standing, custody, content, condition, selection, acceptance, or risk revision.
Correction ownership remains with the frozen correction record; the map does
not reassign it. Recovery removes the prepared route, preserves the frozen
record and all alternatives, and performs nothing. The exact next wake is one
immutable destination-owner route-acceptance record, or a revision to source,
pointer, checksum, custody, standing, comparison, selection, acceptance,
authority, or risk.

## Frontier Verification

- Confirm the current source revision, checksum custody, pointer, comparison
  record, and selection record all match.
- Confirm comparison authority is limited to the supplied dominance relation.
- Confirm selection authority is limited to one prepared pointer-only handoff.
- Confirm destination-owner acceptance is missing.
- Confirm the materially distinct dominated verified route remains visible.
- Confirm the prepared return remains `defer` and no route is opened.
- Confirm `CMD-0001` and P7 defer remain unchanged.
- Confirm external action remains `none`.
