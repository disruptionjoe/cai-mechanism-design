---
artifact_type: candidate_admission_decision_template
status: candidate_process_artifact
external_action: none
---

# Candidate Admission Decision Template

## Use Boundary

Use this artifact to prepare one owner decision from frozen evidence. Completing
it does not admit, reject, revise, reopen, or disposition a candidate and does
not authorize contact, research, testing, transfer, graduation, deployment, or
external action. Do not invent an inquiry, owner, source, affected party, fact,
date, authority, or result to fill a gap.

## Decision Header

| Field | Value |
| --- | --- |
| `decision_id` | `[required: unique decision identifier]` |
| `source_inquiry` | `[required: exact source-inquiry pointer]` |
| `source_revision` | `[required: immutable source revision]` |
| `candidate_label` | `[required: proposed candidate identifier or working label]` |
| `decision_owner` | `[required: repository-native decision owner]` |
| `requested_by` | `[required: request source; not authority by itself]` |
| `authorization_ref` | `[required: exact authority for preparing this decision]` |
| `external_action` | `none` |

## Inquiry And Problem Boundary

- Exact inquiry: `[required: source-preserving inquiry statement]`
- Affected condition: `[required: condition the inquiry says may warrant intervention]`
- Excluded scope: `[required: facts, owners, remedies, and populations outside the inquiry]`
- Prohibited inference: `[required: conclusions the source does not support]`

## Existing-Owner Fit

- Owners considered: `[required: candidate owners and exact native-authority pointers]`
- Evidence for fit: `[required: evidence that a named owner legitimately owns this work]`
- Evidence for non-fit: `[required: evidence that the inquiry remains otherwise unowned or integrative]`
- Missing owner-fit evidence: `[required: unresolved evidence gaps]`
- Better-existing-owner result: `[required: found, not_found, or unresolved]`
- Admission rule: a better existing owner defeats admission here; interest,
  expertise, or convenience alone does not establish fit.

## Candidate And Theory Of Change

- Candidate mechanism: `[required: bounded mechanism, not a desired outcome]`
- Inputs: `[required: evidence, actors, resources, and preconditions]`
- Causal steps: `[required: inspectable links from inputs to intended effects]`
- Intended effects: `[required: bounded changes claimed by the mechanism]`
- Assumptions: `[required: assumptions with evidence posture]`
- Failure modes: `[required: ways the mechanism, ownership, or legitimacy could fail]`

## Alternatives And No Action

- No action: `[required: consequence, rationale, and owner if monitoring is needed]`
- Materially different alternatives: `[required: one or more repeatable alternative records; do not manufacture parity]`
- For each alternative: `[required: mechanism, owner route, evidence posture, main benefit, main risk, and stop]`
- Kill or defer conditions: `[required: conditions that allow a non-admission result without forced comparison]`

## Evidence And Proving Route

- Exact source pointers: `[required: immutable evidence revisions]`
- Claim posture: `[required: observed, source-asserted, inferred, synthetic, formal, simulated, or unverified]`
- Supporting evidence: `[required: claim-level support]`
- Counterevidence: `[required: basis, claim posture, and effect on the candidate]`
- Least-consequential proving route: `[required: narrow test candidate; preparation is not execution authority]`
- Prohibited conclusions: `[required: claims no proposed evidence or test could establish]`

## Affected Parties And Legitimacy

- Parties with standing: `[required: affected parties and basis for standing]`
- Risk bearers: `[required: who bears error, delay, or intervention risk]`
- Representation limits: `[required: whose views or interests are not represented]`
- Capture risks: `[required: incentives or structures that could distort the decision]`
- Consent or authority gaps: `[required: unresolved gaps]`
- Cannot be spoken for: `[required: people or owners this decision does not represent]`

## Stops, Correction, And Recovery

- Stop conditions: `[required: conditions that halt preparation or proving]`
- Kill conditions: `[required: evidence that defeats the candidate]`
- Correction owner: `[required: owner authorized to correct each relevant truth]`
- Negative-evidence preservation: `[required: durable return location]`
- Rollback or recovery: `[required: how a reversible effect returns to the last known good state]`
- Exact next wake: `[required: evidence or owner event that warrants reconsideration]`

## Prepared Decision

- Decision: `[required: exactly one of admit_synthetic_candidate, route_to_existing_owner, request_revision, defer, reject, needs_judgment]`
- Rationale: `[required: evidence-bound reason for that decision]`
- Unresolved risks: `[required: material uncertainty and affected consequence]`
- Permitted owner effect: `[required: narrow change the decision owner may consider]`
- Prohibited interpretations: `[required: claims or actions this prepared decision does not authorize]`

## Frontier Verification

- Verify every source, revision, and authority pointer against repository truth.
- Confirm the inquiry boundary and theory of change introduce no unsupported facts.
- Re-run the better-existing-owner test and preserve unresolved owner-fit evidence.
- Confirm no action and at least one genuinely different alternative are present
  without requiring artificial parity.
- Check affected-party standing, representation limits, capture, consent,
  stops, correction, recovery, and negative-evidence preservation.
- Confirm the prepared decision uses exactly one allowed value, follows from
  the frozen evidence, and performs no admission, disposition, or external action.
