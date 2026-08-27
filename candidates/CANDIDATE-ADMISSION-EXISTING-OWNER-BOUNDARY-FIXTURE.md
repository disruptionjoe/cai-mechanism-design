---
artifact_type: synthetic_candidate_admission_existing_owner_boundary_fixture
status: candidate_process_fixture
external_action: none
---

# Synthetic Candidate Admission Existing-Owner Boundary Fixture

## Use Boundary

This artifact applies the candidate-admission decision boundary to supplied
synthetic evidence in which a better existing owner is found. It performs no
admission, rejection, routing, contact, acceptance, disposition, proving, or
external action. Interest, expertise, convenience, a source payload, and a
prepared decision value are not owner authority.

## Decision Header

| Field | Value |
| --- | --- |
| `decision_id` | `SYNTH-ADMISSION-DECISION-OWNED-001@r1` |
| `source_inquiry` | `SYNTH-SOURCE-OWNED-001@r1` |
| `candidate_label` | `SYNTH-CANDIDATE-OWNED-001@r1` |
| `decision_owner` | `synthetic-mechanism-decision-owner` |
| `requested_by` | `synthetic-source-intake@r1` |
| `authorization_ref` | `synthetic-admission-decision-preparation@r1` |
| `external_action` | `none` |

## Inquiry And Problem Boundary

The source-preserving inquiry asks how one synthetic correction label and its
correction owner should remain linked after the label changes. The affected
condition is loss of correction custody in a synthetic record. Real people,
institutions, field conditions, remedies, and deployment are excluded. The
source supports no effectiveness, adoption, authority, owner acceptance, or
real-world claim.

## Existing-Owner Fit

`synthetic-native-owner` has exact native authority
`synthetic://owner/SYNTH-NATIVE-OWNER@r1#correction-custody` and current native
work `synthetic://work/SYNTH-NATIVE-WORK-001@r3`. That work already links the
same synthetic label, correction owner, changed revision, stop, and return
route. These pointers are frozen fixture facts.

- Evidence for fit: the exact native-authority and current-work match.
- Evidence for non-fit: `none`.
- Missing owner-fit evidence: `none`.
- Better-existing-owner result: `found`.
- Contact, acceptance, and routing acknowledgment: `none`.

Existing-owner fit therefore defeats admission here.

## Candidate And Theory Of Change

The proposed Mechanism Design candidate would copy the same label, owner,
changed-revision, stop, and return facts into a second correction-custody card.
Its intended effect is correction visibility, but the causal proposal creates
duplicate custody and potentially conflicting correction routes. Inputs are
only the frozen inquiry and native-owner pointers. No execution is authorized.

## Alternatives And No Action

No action preserves the source and existing native work. One materially
different alternative is for `synthetic-native-owner` to revise its existing
card under its own authority. Another is to narrow the inquiry to a genuine
unowned gap, but no such gap is supplied. Stop on any change to the source,
native authority, native work, standing, custody, or risk.

## Evidence And Proving Route

All evidence is synthetic fixture evidence. The exact native-authority and
current-work match supports owner fit; the duplicate card and conflicting
custody are counterevidence to admission. Owner fit defeats admission before
proving, so there is no least-consequential proving route to prepare here. This
evidence cannot establish effectiveness, destination fit, acceptance,
authority to contact, deployment readiness, or external outcome.

## Affected Parties And Legitimacy

One synthetic reviewer role represents standing. No real person, institution,
source owner, native owner, or Mechanism Design owner is represented or spoken
for. The risk is duplicate correction custody. No consent, contact, routing,
or acceptance evidence is supplied.

## Stops, Correction, And Recovery

Stop on any source, native-authority, native-work, standing, custody, or risk
change. The correction owner is `synthetic-mechanism-decision-owner`, and the
negative-evidence return is
`synthetic://decision-evidence/SYNTH-ADMISSION-DECISION-OWNED-001@r1`.
Recovery is to preserve the source and existing native work. The exact next
wake is a new immutable native-authority or work revision that removes the fit,
or a source revision that supplies a distinct unowned gap.

## Prepared Decision

Prepared decision: `route_to_existing_owner`. The better-existing-owner result
supports only consideration of that decision by the decision owner. Preparing
it performs no routing, contact, acceptance, admission, disposition, owner
effect, or external action. The source and existing native work remain
unchanged.

## Frontier Verification

- Verify the decision, source, candidate, authority, and native-work revisions
  against this frozen fixture.
- Confirm the better-existing-owner result is `found` and that no evidence for
  non-fit or missing owner-fit evidence was supplied.
- Confirm duplicate correction custody remains the main candidate failure.
- Confirm owner fit stops admission before proving.
- Confirm `route_to_existing_owner` remains non-operative and that no contact,
  routing, acceptance, admission, disposition, or external action occurred.
