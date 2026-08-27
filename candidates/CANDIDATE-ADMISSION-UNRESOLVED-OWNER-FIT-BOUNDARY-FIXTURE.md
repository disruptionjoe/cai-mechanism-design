---
artifact_type: synthetic_candidate_admission_unresolved_owner_fit_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Candidate Admission Unresolved Owner-Fit Boundary Fixture

## Use Boundary

This artifact applies the candidate-admission decision boundary to supplied
synthetic evidence in which existing-owner fit cannot yet be resolved. It does
not treat unresolved fit as `not_found` and performs no admission, rejection,
revision, reopening, routing, contact, acceptance, disposition, proving, or
external action. Pointer presence is not proof of fit, and unreadable pointer
content is not proof of non-fit.

## Decision Header

| Field | Value |
| --- | --- |
| `decision_id` | `SYNTH-ADMISSION-DECISION-UNRESOLVED-001@r1` |
| `source_inquiry` | `SYNTH-SOURCE-UNRESOLVED-001@r1` |
| `candidate_label` | `SYNTH-CANDIDATE-UNRESOLVED-001@r1` |
| `decision_owner` | `synthetic-mechanism-decision-owner` |
| `requested_by` | `synthetic-source-intake@r2` |
| `authorization_ref` | `synthetic-admission-decision-preparation@r2` |
| `external_action` | `none` |

## Inquiry And Problem Boundary

The source-preserving inquiry asks how a synthetic handoff checksum and its
correction owner should remain linked after a pointer changes. The affected
condition is loss of correction custody in one synthetic record. Real people,
institutions, field conditions, remedies, and deployment are excluded. The
source supports no effectiveness, adoption, authority, owner acceptance, or
real-world claim.

## Existing-Owner Fit

One possible native owner is named as `synthetic-native-owner`, with authority
pointer `synthetic://owner/SYNTH-NATIVE-OWNER@r2#handoff-custody`. The pointer
is supplied, but its referenced authority content is unavailable in this
fixture. Possible current work is supplied at
`synthetic://work/SYNTH-NATIVE-WORK-UNREADABLE-001@r1`, but that content is
also unavailable.

- Evidence for fit: `unverified pointer presence`.
- Evidence for non-fit: `none`.
- Missing owner-fit evidence: readable authoritative content and an exact
  current-work comparison.
- Better-existing-owner result: `unresolved`.
- Contact, acceptance, and routing acknowledgment: `none`.

Unresolved owner fit stops admission and proving preparation.

## Candidate And Theory Of Change

The proposed Mechanism Design candidate would create a synthetic handoff-
custody card linking the checksum, correction owner, pointer revision, stop,
and return route. Its intended effect is correction visibility. Its two main
failure modes are duplicate native work if fit exists and orphaned custody if
fit does not exist but the proposed mechanism lacks a legitimate owner. Inputs
are only the frozen inquiry and unresolved pointers. No execution is
authorized.

## Alternatives And No Action

No action preserves the source and unresolved pointers while requesting no
contact. One materially different alternative is to obtain immutable owner-
authority and current-work evidence through an authorized later owner process.
Another is to narrow the inquiry to a distinct unowned gap, but no such gap is
supplied. Stop on any source, authority, work, standing, custody, or risk
change.

## Evidence And Proving Route

All evidence is synthetic fixture evidence. Pointer presence is not proof of
fit; absence of readable pointer content is not proof of non-fit. No proving
route may be prepared until owner fit is resolved because a proving plan would
prematurely treat admission as available. No supplied evidence can establish
effectiveness, destination fit, acceptance, authority to contact, deployment
readiness, or external outcome.

## Affected Parties And Legitimacy

One synthetic reviewer role represents standing. No real person, institution,
source owner, possible native owner, or Mechanism Design owner is represented
or spoken for. No consent, authority to contact, acceptance, or routing
evidence is supplied.

## Stops, Correction, And Recovery

Stop on any source, authority, work, standing, custody, or risk change. The
correction owner is `synthetic-mechanism-decision-owner`, and the negative-
evidence return is
`synthetic://decision-evidence/SYNTH-ADMISSION-DECISION-UNRESOLVED-001@r1`.
Recovery is to preserve the source and unresolved pointers. The exact next
wake is immutable readable authority content plus an exact current-work
comparison for the supplied possible owner, or a source revision supplying a
distinct unowned gap.

## Prepared Decision

Prepared decision: `defer`. The unresolved fit supports only later
reconsideration by the decision owner at the exact wake. Preparing this value
performs no admission, routing, contact, acceptance, candidate-status change,
disposition, owner effect, or external action.

## Frontier Verification

- Verify the decision, source, candidate, authority, and current-work pointers
  against this frozen fixture.
- Confirm owner fit remains `unresolved`, evidence for non-fit remains `none`,
  and unreadable content does not become evidence of non-fit.
- Confirm both duplicate-work and orphaned-custody failure modes remain
  visible.
- Confirm unresolved owner fit stops both admission and proving preparation.
- Confirm `defer` remains non-operative and creates no admission, routing,
  contact, acceptance, candidate status, disposition, or external action.
