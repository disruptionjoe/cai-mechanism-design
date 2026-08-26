---
artifact_type: candidate_graduation_transfer_plan_template
status: candidate_process_artifact
external_action: none
---

# Candidate Graduation Transfer Plan Template

## Use Boundary

Use this artifact to prepare a source-, acceptance-, and revision-bound transfer
plan for a candidate with an already proposed destination. Completing it does
not create destination-owner acceptance, graduate or transfer a candidate,
authorize contact, operate or deploy anything, publish, or perform external
action. Interest, review, acknowledgment, or plan preparation is not
acceptance. Do not invent missing owners, artifacts, obligations, parties,
authority, acceptance, risks, dates, decisions, or results.

## Plan Header

| Field | Value |
| --- | --- |
| `transfer_plan_id` | `[required: stable plan identifier]` |
| `source_inquiry` | `[required: exact source-inquiry pointer and revision]` |
| `candidate_id` | `[required: exact candidate identifier and revision]` |
| `graduation_proposal` | `[required: exact proposal pointer and revision]` |
| `current_disposition` | `[required: exact decision and revision]` |
| `source_owner` | `[required: current source-truth owner]` |
| `proposed_destination_owner` | `[required: exact proposed owner; not acceptance by itself]` |
| `acceptance_revision` | `[required: immutable destination-owner acceptance evidence, or none]` |
| `transfer_authority_ref` | `[required: exact authority, pending, or none]` |
| `prepared_by` | `[required: preparer identity]` |
| `prepared_at` | `[required: ISO-8601 timestamp]` |
| `external_action` | `none` |

## Frozen Accepted Scope

- Acceptance state: `[required: not_requested, pending, accepted, rejected, withdrawn, or unresolved]`
- Acceptance evidence: `[required: immutable destination-owner-native evidence, or none]`
- Exactly accepted artifacts: `[required: artifact revisions proven accepted; none unless acceptance state is accepted]`
- Excluded artifacts: `[required: explicit exclusions and retained custody]`
- Accepted responsibilities: `[required: exact responsibilities proven accepted; none unless accepted]`
- Evidence and negative evidence: `[required: immutable package pointers]`
- Unresolved risks: `[required: material risks and current bearers]`
- Authority boundary: `[required: exact accepted authority and exclusions, or none]`
- Validation: `[required: checks, revisions, and results]`
- Prohibited inference: `[required: acceptance, authority, ownership, or readiness conclusions the evidence cannot support]`

No plan field may convert proposed, pending, acknowledged, or synthetic review
into accepted scope.

## Custody And Ownership Map

| Truth or responsibility | Current owner | Proposed owner | Transfer evidence | Unresolved custody |
| --- | --- | --- | --- | --- |
| Source truth | `[required]` | `[required or none]` | `[required or none]` | `[required]` |
| Incubator evidence | `[required]` | `[required or none]` | `[required or none]` | `[required]` |
| Destination truth | `[required]` | `[required]` | `[required or none]` | `[required]` |
| Maintenance | `[required]` | `[required or none]` | `[required or none]` | `[required]` |
| Correction | `[required]` | `[required or none]` | `[required or none]` | `[required]` |
| Material risk | `[required]` | `[required or none]` | `[required or none]` | `[required]` |

## Transfer Sequence And Acceptance Gates

Repeat the following block for every proposed step. Each step must be
reversible or identify why a separate exact authorization and recovery route
is required before it can begin.

### Step `[repeat as needed]`

- Proposed effect: `[required: exact narrow effect]`
- Preconditions: `[required: authority, acceptance, evidence, and state gates]`
- Reversibility: `[required: last-known-good state and restoration path]`
- Acknowledgment: `[required: evidence needed; acknowledgment is not acceptance unless owner-native acceptance says so]`
- Acceptance check: `[required: exact check and owner]`
- Abort rule: `[required: observable halt condition]`
- Resulting custody: `[required: owner of every changed truth or artifact]`
- Explicit non-effects: `[required: effects this step cannot create]`

## Affected Parties, Data, And Legitimacy

- Parties with standing: `[required: parties and evidence for standing]`
- Representation limits: `[required: absent or simulated standing]`
- Risk bearers: `[required: who bears transfer, delay, or intervention risk]`
- Data boundary: `[required: provenance, class, transformation, retention, and exposure]`
- Capture risks: `[required: incentives or authority that could distort transfer]`
- Consent or authority gaps: `[required: unresolved gaps and consequence]`
- Cannot be spoken for: `[required: people or owners this plan does not represent]`

## Unresolved Risks And Negative Evidence

- Durable disclosures: `[required: complete adverse evidence and risk pointers]`
- Explicit risk acceptance: `[required: exact destination-owner acceptance for each risk, or none]`
- Retained risk: `[required: risk and owner that cannot be transferred by plan language]`
- Supersession: `[required: active, superseded, or unresolved with evidence]`
- No laundering check: `[required: proof that transfer does not hide adverse evidence, uncertainty, or weak claim posture]`
- Missing acceptance: `[required: gaps that prevent transfer readiness]`

## Stops, Correction, Rollback, Recovery, And Revocation

- Pre-transfer stops: `[required: conditions that prevent any step from starting]`
- Live stops: `[required: observable conditions that halt an authorized step]`
- Correction owner: `[required: owner authorized to correct each relevant truth]`
- Rollback owner and route: `[required: exact restoration responsibility and state]`
- Recovery owner and route: `[required: exact recovery responsibility and wake]`
- Revocation owner and conditions: `[required: who may revoke what and on which evidence]`
- New-authorization conditions: `[required: every material change that needs a fresh decision]`

## Prepared Transfer State

- State: `[required: exactly one of ready_for_authorized_transfer, request_revision, defer, reject, or needs_judgment]`
- Rationale: `[required: one evidence-bound reason]`
- Exact proposed effect: `[required: narrow effect, or none]`
- Explicit non-effects: `[required: acceptance, graduation, transfer, contact, operation, deployment, publication, and external action not created]`
- Validation: `[required: independent checks and results]`
- Next owner: `[required: owner of the next decision; not contact authority]`
- Exact next wake: `[required: evidence or owner event that warrants reconsideration]`

Plan preparation does not transfer anything. `ready_for_authorized_transfer`
means only that every separately required acceptance and authority pointer has
been independently verified; the plan itself remains non-operative.

## Frontier Verification

- Verify source, candidate, proposal, disposition, acceptance, authority,
  artifact, responsibility, evidence, negative-evidence, and risk revisions independently.
- Confirm accepted scope contains only destination-owner-native acceptance
  evidence and that missing acceptance remains visible.
- Check custody, affected-party standing, data, capture, consent, stops,
  correction, rollback, recovery, revocation, and risk-retention boundaries.
- Confirm every transfer step is reversible or separately gated and no
  acknowledgment is promoted into acceptance.
- Confirm integration creates no acceptance, graduation, transfer, contact,
  operation, deployment, publication, or external action.
