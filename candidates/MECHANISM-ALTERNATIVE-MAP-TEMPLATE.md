---
artifact_type: mechanism_alternative_map_template
status: candidate_process_artifact
external_action: none
---

# Mechanism Alternative Map Template

## Use Boundary

Use this artifact to map materially different responses to one frozen inquiry
or candidate boundary. Completing it does not compare alternatives conclusively,
admit, reject, revise, reopen, or disposition a real candidate and does not
authorize research, testing, contact, transfer, graduation, deployment, or
external action. Do not invent an inquiry, owner, source, affected party,
mechanism, fact, date, authority, or result to fill a gap.

## Map Header

| Field | Value |
| --- | --- |
| `map_id` | `[required: unique map identifier]` |
| `source_inquiry` | `[required: exact source-inquiry pointer]` |
| `source_revision` | `[required: immutable source revision]` |
| `candidate_or_problem_ref` | `[required: exact candidate revision or frozen problem reference]` |
| `map_owner` | `[required: repository-native owner of this map]` |
| `authorization_ref` | `[required: exact authority for preparing this map]` |
| `external_action` | `none` |

## Frozen Inquiry And Candidate Boundary

- Exact problem: `[required: source-preserving problem statement]`
- Candidate in scope: `[required: exact candidate and revision, or none]`
- Included scope: `[required: facts, populations, mechanisms, and effects that may be mapped]`
- Excluded scope: `[required: owners, remedies, facts, populations, and effects outside the map]`
- Prohibited inference: `[required: conclusions the source or candidate does not support]`

## Alternative Records

Include no action and one or more genuinely different alternatives. Repeat the
block below for each. Do not require arbitrary cardinality or manufacture
parity when evidence supports only a dominated, incommensurable, or incomplete
alternative.

### Alternative Record `[repeat as needed]`

- Alternative ID: `[required: stable identifier]`
- Alternative type: `[required: no_action or mechanism]`
- Mechanism: `[required: bounded mechanism, or the explicit no-action posture]`
- Owner route: `[required: owner with native authority, or unresolved]`
- Inputs: `[required: evidence, actors, resources, and preconditions]`
- Causal steps: `[required: inspectable links from inputs to intended effect]`
- Assumptions: `[required: assumptions with claim posture]`
- Evidence posture: `[required: observed, source-asserted, inferred, synthetic, formal, simulated, or unverified]`
- Intended effect: `[required: bounded effect claimed by the alternative]`
- Failure modes: `[required: mechanism, ownership, legitimacy, and evidence failures]`
- Affected parties: `[required: parties with standing and risk bearers]`
- Stops: `[required: evidence or events that halt or defeat the alternative]`
- Correction: `[required: authorized correction and recovery route]`

## Material Difference And Nonduplication

- Load-bearing distinctions: `[required: causal, owner, evidence, legitimacy, risk, or reversibility differences]`
- Duplicate or absorber checks: `[required: exact comparison against existing alternatives and owner-native remedies]`
- Merged variants: `[required: variants merged and why their differences were not material, or none]`
- Remaining overlap: `[required: unresolved overlap and its consequence]`

## Existing-Owner Fit And Routing

- Native authority considered: `[required: proposed owners and exact authority pointers]`
- Evidence for fit: `[required: claim-level fit evidence]`
- Evidence for non-fit: `[required: limits or conflicts defeating fit]`
- Missing evidence: `[required: unresolved owner-fit evidence]`
- Better-existing-owner result: `[required: found, not_found, or unresolved]`
- Incubator remainder: `[required: work that remains with Mechanism Design]`

A better existing owner defeats admission here. Interest, expertise, or
convenience alone does not establish fit, and preparing a route does not
authorize contact or sending.

## Evidence, Counterevidence, And Proving Needs

- Exact evidence pointers: `[required: immutable source, candidate, and alternative revisions]`
- Claim posture: `[required: posture for each material claim]`
- Counterevidence: `[required: basis, claim posture, and effect on the alternative]`
- Discriminatory questions: `[required: questions that distinguish alternatives without forced ranking]`
- Least-consequential proving needs: `[required: narrow tests that could discriminate; preparation is not execution authority]`
- Prohibited conclusions: `[required: claims the current evidence or proposed tests cannot establish]`

## Affected Parties And Legitimacy

- Parties with standing: `[required: affected parties and basis for standing]`
- Risk bearers: `[required: who bears error, delay, or intervention risk]`
- Representation limits: `[required: absent or simulated standing]`
- Capture risks: `[required: incentives or structures that could distort the map]`
- Consent or authority gaps: `[required: unresolved gaps]`
- Cannot be spoken for: `[required: people or owners this map does not represent]`

## Comparative Boundary

- Comparable dimensions: `[required: dimensions supported by the frozen evidence]`
- Incommensurable dimensions: `[required: values or consequences that cannot yet be compared]`
- Dominated alternatives: `[required: alternatives that may remain visible as negative evidence]`
- Ranking boundary: `[required: why ranking is supported, partial, prohibited, or unresolved]`
- Missing evidence: `[required: evidence needed before stronger comparison]`

Do not fabricate precision, parity, or ranking merely to complete the map.

## Prepared Return

- Return: `[required: exactly one of retain_for_admission_review, route_to_existing_owner, request_revision, defer, reject, or needs_judgment]`
- Rationale: `[required: evidence-bound reason for the return]`
- Negative-evidence preservation: `[required: durable pointer and reason]`
- Exact next wake: `[required: evidence or owner event that warrants reconsideration]`
- Prohibited interpretations: `[required: decisions or actions this return does not authorize]`

This is a map return, not a candidate disposition. Any later kill, revise,
defer, transfer, or graduation proposal remains a separate owner decision.

## Frontier Verification

- Verify every source, revision, candidate, owner, and authority pointer.
- Confirm no action and every genuinely different alternative remain visible
  without arbitrary cardinality, forced parity, or fabricated ranking.
- Re-run nonduplication, absorber, and better-existing-owner checks.
- Check causal steps, evidence posture, counterevidence, affected-party
  standing, legitimacy, stops, correction, and recovery.
- Confirm the prepared return uses one allowed value and remains separate from
  candidate disposition.
- Confirm no research, testing, contact, transfer, graduation, deployment, or
  external action is invented or authorized.
