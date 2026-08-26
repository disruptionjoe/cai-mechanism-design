# Apply the graduation-proposal template to a frozen negative boundary

## Boundary

Write one complete synthetic Mechanism Design process fixture from only the
embedded evidence. Do not contact, send, transfer, graduate, publish, deploy,
or act on a real candidate; do not add facts, acceptance, authority, parties,
dates, decisions, or results; do not modify or reopen `CMD-0001`; and do not
authorize external action. This tests a proposal boundary, not a candidate.
External action is `none`.

## Evidence

<evidence path="graduations/GRADUATION-PROPOSAL-TEMPLATE.md">
A graduation proposal freezes the candidate, source, disposition, alternatives,
proving returns, evidence, owner fit, acceptance, affected-party standing,
risk, stops, correction, recovery, and prepared state. It cannot create
destination-owner fit, acceptance, graduation, contact, transfer, deployment,
publication, or external action.
</evidence>

<evidence path="interfaces/DESTINATION-OWNER-SYNTHETIC-REVIEW-REQUEST-TEMPLATE.md">
Interest, acknowledgment, or synthetic review is not destination-owner
acceptance. Preparing a review request does not authorize contact or sending.
</evidence>

<evidence fixture="SYNTHETIC-GRADUATION-PROPOSAL-BOUNDARY-001">
Proposal `SYNTH-GRAD-PROP-BOUNDARY-001@r1` refers to candidate
`SYNTH-CANDIDATE-GRAD-001@r1`, source inquiry `SYNTH-SOURCE-GRAD-001@r1`, and
current disposition `defer@r1`. The proposing and source owner is
`synthetic-source-owner`; the proposed destination is
`synthetic-destination-owner`. Preparation authority is
`synthetic-preparation-authority@r1`, preparer is
`synthetic-proposal-preparer`, and prepared time is
`2026-08-26T00:00:00Z`. External action is `none`.
</evidence>

<evidence fixture="SYNTHETIC-GRADUATION-PROPOSAL-BOUNDARY-001-PACKAGE">
The frozen candidate pointer is
`synthetic://candidate/SYNTH-CANDIDATE-GRAD-001@r1`; the frozen source pointer
is `synthetic://source/SYNTH-SOURCE-GRAD-001@r1`. No alternative-map revision
or proving return exists. The bounded theory is that a synthetic correction
card could preserve one public label and its correction owner during a future
handoff. There is no evidence that the proposed destination has matching native
work, better-owner fit, acceptance, or authority. The supported alternatives
are continued incubation, no action, revision, defer, kill, and later transfer
review; current disposition remains `defer@r1`.
</evidence>

<evidence fixture="SYNTHETIC-GRADUATION-PROPOSAL-BOUNDARY-001-CONTROLS">
Acceptance state is `not_requested`; acceptance evidence is `none`; exact
proposed scope is the one synthetic correction card, with all responsibility,
custody, correction, and risk retained by `synthetic-source-owner`. Only a
synthetic reviewer role has represented standing; no real person or institution
is represented. Data is one public synthetic label retained only in this
fixture. Unresolved risk is loss of correction context if custody changes.
Stop before contact, acceptance claims, transfer, or graduation. Wake only on
destination-owner-native fit and acceptance evidence plus separate authority.
</evidence>

<evidence path="GOVERNANCE.md">
Synthetic reversible work may proceed only within an exact grant. No contact,
transfer, graduation, publication, deployment, or external action is authorized.
</evidence>

## Work now

Draft the finished Markdown artifact
`graduations/GRADUATION-PROPOSAL-BOUNDARY-FIXTURE.md` with exactly these sections:

1. YAML frontmatter with
   `artifact_type: synthetic_graduation_proposal_boundary_fixture`,
   `status: candidate_process_fixture`, and `external_action: none`.
2. `# Synthetic Graduation Proposal Boundary Fixture`.
3. `## Use Boundary`.
4. `## Proposal Header` using only supplied fixture values.
5. `## Frozen Graduation Package` preserving absent alternatives and returns.
6. `## Earned Graduation Case` showing that graduation is not earned.
7. `## Destination-Owner Fit And Acceptance` preserving `not_requested` and
   acceptance evidence `none`.
8. `## Affected Parties And Legitimacy`.
9. `## Unresolved Risks And Negative Evidence`.
10. `## Stops, Correction, Recovery, And Revocation`.
11. `## Prepared Proposal` with state `defer`, exact non-effects, next owner
    `synthetic-destination-owner`, and the supplied wake.
12. `## Frontier Verification` listing only checks grounded in this fixture.

Do not use fillable placeholders and do not turn a proposed destination into
fit, acceptance, or contact authority. Return only the finished artifact.
