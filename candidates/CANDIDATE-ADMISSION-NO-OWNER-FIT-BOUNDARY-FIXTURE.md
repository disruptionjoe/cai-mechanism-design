---
artifact_type: synthetic_candidate_admission_no_owner_fit_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Candidate Admission No-Owner-Fit Boundary Fixture

## Use Boundary

This artifact applies the candidate-admission decision boundary to supplied
synthetic evidence in which a complete owner comparison finds no better
existing owner for the exact relationship-level gap. It prepares one synthetic
admission value but performs no admission, candidate-status change, proving,
routing, contact, acceptance, disposition, or external action. A `not_found`
owner-fit result is not evidence of effectiveness, legitimacy, or authority.

## Decision Header

| Field | Value |
| --- | --- |
| `decision_id` | `SYNTH-ADMISSION-DECISION-NO-FIT-001@r1` |
| `source_inquiry` | `SYNTH-SOURCE-NO-FIT-001@r1` |
| `source_revision` | `r1` |
| `candidate_label` | `SYNTH-CANDIDATE-NO-FIT-001@r1` |
| `decision_owner` | `synthetic-mechanism-decision-owner` |
| `requested_by` | `synthetic-source-intake@r3` |
| `authorization_ref` | `synthetic-admission-decision-preparation@r3` |
| `external_action` | `none` |

## Inquiry And Problem Boundary

The source-preserving inquiry asks how a checksum shared across two synthetic
records can retain one visible correction route when neither record owner has
authority over their cross-record relationship. The affected condition is a
synthetic correction that can be valid in each record yet lose custody at the
relationship boundary. Real people, institutions, field conditions, remedies,
and deployment are excluded. The source supports no effectiveness, adoption,
authority, owner acceptance, or real-world claim.

## Existing-Owner Fit

The complete owner set supplied by this fixture contains two possible native
owners:

- `synthetic-record-owner-a` has readable authority
  `synthetic://owner/SYNTH-RECORD-A@r4#record-a-only` and current work
  `synthetic://work/SYNTH-RECORD-A-CORRECTION@r5`; both stop at record A and
  disclaim the cross-record relationship.
- `synthetic-record-owner-b` has readable authority
  `synthetic://owner/SYNTH-RECORD-B@r3#record-b-only` and current work
  `synthetic://work/SYNTH-RECORD-B-CORRECTION@r2`; both stop at record B and
  disclaim the cross-record relationship.

Evidence for fit is `none`. Evidence for non-fit is the two exact authority
and work exclusions. Missing owner-fit evidence is `none`, and the better-
existing-owner result is `not_found`. No contact, acceptance, routing
acknowledgment, or owner extension exists.

## Candidate And Theory Of Change

The proposed Mechanism Design candidate is a synthetic relationship-custody
card that stores only the two immutable record pointers, shared checksum,
relationship revision, correction owner, stop, and return route. Its intended
effect is relationship-level correction visibility without copying either
record's native truth.

- Inputs: only the frozen synthetic evidence and exact owner comparison.
- Causal steps: compare the immutable pointers, expose the relationship
  revision and correction owner, stop on any native revision, and return
  corrections to the named decision owner.
- Assumptions: the supplied owner set is complete for this fixture, the four
  owner and work pointers remain unchanged, and relationship custody remains
  outside both native scopes. These are synthetic fixture premises, not
  real-world findings.
- Failure modes: accidental absorption of native record truth, a false claim
  of authority over either owner, and orphaned relationship custody.

No execution is authorized.

## Alternatives And No Action

- No action preserves both native records and the unresolved relationship gap.
- One materially different alternative is for both record owners later to
  accept one owner-native extension; no such authority or acceptance exists.
- Another alternative is a source-owned pointer pair with no relationship-
  custody card; it preserves pointers but leaves correction custody implicit.

Stop comparison on any source, authority, work, standing, custody, risk, or
owner-acceptance change. These alternatives are not ranked by the fixture.

## Evidence And Proving Route

The evidence posture is synthetic. The owner comparison establishes only that
the exact relationship gap is not owned by the complete supplied owner set.
The authority and current-work exclusions support non-fit; the absence of any
accepted relationship owner remains a legitimacy and custody constraint, not
positive evidence for the mechanism.

A least-consequential proving route could later compare one frozen two-record
fixture with the proposed card for native-truth copying, visible correction
custody, revision stops, and exact return behavior. Preparing that route does
not authorize or execute it. No supplied evidence or proposed test can
establish effectiveness, destination fit, owner acceptance, authority over
native records, deployment readiness, or external outcome.

## Affected Parties And Legitimacy

Only one synthetic reviewer role represents standing. No real person,
institution, source owner, record owner, or Mechanism Design owner is
represented or spoken for. No consent, owner acceptance, or authority
extension is supplied. The principal capture risks are treating relationship
visibility as authority over native records and treating a complete synthetic
comparison as real-world legitimacy.

## Stops, Correction, And Recovery

Stop on any source, authority, native-work, standing, custody, risk, or owner-
acceptance change. The correction owner is
`synthetic-mechanism-decision-owner`, and negative evidence returns to
`synthetic://decision-evidence/SYNTH-ADMISSION-DECISION-NO-FIT-001@r1`.
Recovery is to preserve both native records and remove no relationship state,
because no candidate has been admitted or executed. The exact next wake is a
decision-owner act on the prepared decision, or a revision to any frozen
source, authority, native-work, standing, custody, risk, or owner-acceptance
fact.

## Prepared Decision

Prepared decision: `admit_synthetic_candidate`. The complete synthetic owner
comparison and bounded candidate structure support only consideration of that
value by the decision owner. Preparation creates no admission, candidate
status, proving authority, routing, contact, acceptance, disposition, owner
effect, or external action.

## Frontier Verification

- Verify the decision, source, candidate, authority, and current-work
  revisions against this frozen fixture.
- Confirm the supplied owner set is complete, evidence for fit and missing
  owner-fit evidence remain `none`, and the better-existing-owner result
  remains `not_found`.
- Confirm all three failure modes, no action, both materially different
  alternatives, standing limits, capture risks, stops, correction, and
  recovery remain visible.
- Confirm the proving route remains prospective and non-operative.
- Confirm `admit_synthetic_candidate` remains a prepared value and creates no
  admission, candidate status, disposition, proving, routing, contact,
  acceptance, owner effect, or external action.
