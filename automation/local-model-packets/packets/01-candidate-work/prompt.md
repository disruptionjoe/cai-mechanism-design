# Apply the graduation-transfer plan template to a frozen boundary fixture

## Boundary

Write one complete synthetic Mechanism Design process fixture from only the
embedded evidence. Do not transfer, graduate, contact, send, publish, deploy,
or act on a real candidate; do not add facts, owners, acceptance, authority,
artifacts, obligations, risks, parties, dates, decisions, or results; do not
modify or reopen `CMD-0001`; and do not authorize external action. This tests a
process boundary, not a candidate. External action is `none`.

## Evidence

<evidence path="graduations/GRADUATION-TRANSFER-PLAN-TEMPLATE.md">
A transfer plan freezes acceptance state and evidence, accepted and excluded
scope, custody, reversible steps, affected-party and data boundaries, risk,
stops, correction, rollback, recovery, revocation, and explicit non-effects.
Pending review or acknowledgment is not acceptance, and the plan is non-operative.
</evidence>

<evidence path="interfaces/DESTINATION-OWNER-SYNTHETIC-REVIEW-REQUEST-TEMPLATE.md">
Interest, acknowledgment, or synthetic review is not destination-owner
acceptance. Preparing a review request does not authorize contact or sending.
</evidence>

<evidence fixture="SYNTHETIC-TRANSFER-BOUNDARY-001">
The synthetic source inquiry is `SYNTH-SOURCE-001@r1`; the synthetic candidate
is `SYNTH-CANDIDATE-001@r1`; the synthetic graduation proposal is
`SYNTH-GRAD-PROP-001@r1`; and current disposition is `defer@r1`. The source
owner is `synthetic-source-owner`. The proposed destination is
`synthetic-destination-owner`. Its only evidence is review acknowledgment
`SYNTH-ACK-001@r1`; acceptance state is `pending`; acceptance evidence is
`none`; transfer authority is `none`; and no artifact, responsibility, risk,
or custody has been accepted.
</evidence>

<evidence fixture="SYNTHETIC-TRANSFER-BOUNDARY-001-CONTROLS">
The frozen proposed package contains only `artifact-alpha@r1`; `artifact-beta`
is excluded. Incubator evidence, maintenance, correction, and all material risk
remain with `synthetic-source-owner`. The only affected party represented is a
synthetic reviewer role; no real person or institution is represented. Data is
one public synthetic label, retained only in this fixture. Unresolved risk is
loss of correction context if custody changes. No risk acceptance exists.
Every proposed step must stop before contact or transfer and wake only on exact
destination-owner acceptance plus separate transfer authority.
</evidence>

<evidence path="GOVERNANCE.md">
This repository permits synthetic reversible work only within an exact grant.
No contact, transfer, graduation, publication, deployment, or external action
is authorized here.
</evidence>

## Work now

Draft the finished Markdown artifact
`graduations/GRADUATION-TRANSFER-PLAN-BOUNDARY-FIXTURE.md` with exactly these sections:

1. YAML frontmatter with `artifact_type: synthetic_graduation_transfer_plan_boundary_fixture`,
   `status: candidate_process_fixture`, and `external_action: none`.
2. `# Synthetic Graduation Transfer Plan Boundary Fixture`.
3. `## Use Boundary`.
4. `## Plan Header` using only the exact fixture values above and `not_set`
   where preparer or date evidence is absent.
5. `## Frozen Accepted Scope` showing that accepted scope is empty.
6. `## Custody And Ownership Map` preserving all current custody.
7. `## Transfer Sequence And Acceptance Gates` with one proposed no-effect
   review step that stops before contact or transfer.
8. `## Affected Parties, Data, And Legitimacy`.
9. `## Unresolved Risks And Negative Evidence`.
10. `## Stops, Correction, Rollback, Recovery, And Revocation`.
11. `## Prepared Transfer State` with state `defer`, exact non-effects, next
    owner `synthetic-destination-owner`, and the supplied wake.
12. `## Frontier Verification` listing only checks grounded in this fixture.

Do not use fillable placeholders and do not turn `pending` or acknowledgment
into acceptance. Return only the finished artifact.
