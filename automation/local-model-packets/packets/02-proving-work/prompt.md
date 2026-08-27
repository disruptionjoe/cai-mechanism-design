# Apply the result-return template to a frozen denied-start boundary

## Boundary

Write one complete synthetic Mechanism Design process fixture from only the
embedded evidence. Do not create a proving result or return where no authorized
execution trace and score exist; do not authorize or execute a treatment; do
not invent events, observations, evidence, hashes, validation, authority,
owners, dates, results, scores, acknowledgments, or dispositions; do not create
`CMD-0001-P8`; do not modify or reopen `CMD-0001`; and do not authorize contact,
transfer, graduation, deployment, publication, or external action. This tests
whether the return boundary fails closed after a denied start. External action
is `none`.

## Evidence

<evidence path="proving/PROVING-RESULT-RETURN-TEMPLATE.md">
A proving result return requires a completed exactly authorized plan, observed
trace, score, immutable evidence, validation, and authority. It cannot plan,
authorize, execute, score, choose a candidate disposition, or create transfer,
graduation, contact, deployment, publication, or external action.
</evidence>

<evidence path="proving/PROVING-EXECUTION-TRACE-DENIED-START-BOUNDARY-FIXTURE.md">
Trace `SYNTH-TRACE-DENIED-001@r1` records only a failed-closed pre-start
authority check. Exact authorized effect is `none`; no execution event,
operation, data handling, artifact, score package, result, disposition, or P8
exists. Last-known-good state remains immutable input `alpha`.
</evidence>

<evidence path="proving/PROVING-AUTHORIZATION-DECISION-BOUNDARY-FIXTURE.md">
Request `SYNTH-REQ-001` remains `defer`. Authority evidence, authorized
decision-maker, decision time, stop-authority rule, and operative grant are
missing or unresolved. The proposed actor and treatment remain non-operative.
</evidence>

<evidence fixture="SYNTHETIC-DENIED-RETURN-BOUNDARY-001-HEADER">
Return record `SYNTH-RETURN-DENIED-001@r1` refers to proving plan
`SYNTH-PROVE-001@r1`, denied trace `SYNTH-TRACE-DENIED-001@r1`, candidate
`SYNTH-CANDIDATE-REQUEST-001@r1`, source
`SYNTH-SOURCE-REQUEST-001@r1`, and intended result owner
`synthetic-result-owner`. Prepared by `synthetic-return-preparer` at
`2026-08-27T01:14:29Z`. Score revision is `none`. External action is `none`.
</evidence>

<evidence fixture="SYNTHETIC-DENIED-RETURN-BOUNDARY-001-PACKAGE">
Plan pointer is `synthetic://plan/SYNTH-PROVE-001@r1`; request and decision
pointer is `synthetic://decision/SYNTH-REQ-001@defer-r1`; fixture pointer is
`synthetic://fixture/SYNTH-REQUEST-001@r1`; trace pointer is
`synthetic://trace/SYNTH-TRACE-DENIED-001@r1`. Content hashes, observed
execution evidence, score, score revision, validation, operative authority,
and result package are `none`. No tested claim, falsifier, observable failure,
bounded-pass condition, unresolved route, or prohibited-conclusion set was
supplied as an authorized completed package.
</evidence>

<evidence fixture="SYNTHETIC-DENIED-RETURN-BOUNDARY-001-GATE">
The return gate is `failed_closed`. Required execution trace status is
`denied_start_only`; required score status is `missing`; result state is
`not_created`; result value is `none`; permitted disposition support is
`none`; owner return is `not_sent`; receipt acknowledgment is
`unacknowledged`. The denial and missing package support no bounded pass,
revise, kill, defer-result, unresolved-result, candidate disposition, or owner
acceptance claim.
</evidence>

<evidence fixture="SYNTHETIC-DENIED-RETURN-BOUNDARY-001-CONTROLS">
Only one synthetic reviewer role represents standing; no real person,
institution, source owner, result owner, candidate owner, or authority owner is
represented. Actual data handling and treatment risk are `none` because no
execution occurred. The authority gap caused the pre-start halt. No correction,
rollback, recovery action, result return, acknowledgment, or external action
occurred. Available recovery is remain at immutable input `alpha`. Exact next
wake is an immutable operative authorization plus an authorized observed trace,
score, and validation package for this exact frozen plan.
</evidence>

<evidence path="ROADMAP.md">
CMD-0001 remains deferred. This fixture creates no P8, proving result, or
candidate evidence.
</evidence>

## Work now

Draft the finished Markdown artifact
`proving/PROVING-RESULT-RETURN-DENIED-START-BOUNDARY-FIXTURE.md` with exactly
these sections:

1. YAML frontmatter with
   `artifact_type: synthetic_proving_result_return_denied_start_boundary_fixture`,
   `status: candidate_process_fixture`, and `external_action: none`.
2. `# Synthetic Proving Result Return Denied-Start Boundary Fixture`.
3. `## Use Boundary`.
4. `## Return Header` using `none` for the absent score revision.
5. `## Frozen Result Package` preserving every supplied pointer and missing
   required component.
6. `## Result-Return Gate` with `failed_closed`, `not_created`, and exact missing
   prerequisites.
7. `## Tested Claim And Conditions` stating that no authorized completed set
   was supplied and copying none.
8. `## Observed Result` with result `none`; do not select one of the template's
   result values when no trace and score support it.
9. `## Evidence Grade, Counterevidence, And Failure`.
10. `## Affected-Party, Data, And Legitimacy Return`.
11. `## Residual Uncertainty, Correction, And Recovery`.
12. `## Permitted Disposition Support` with support `none` and no owner
    disposition.
13. `## Owner Return` with state `not_sent` and acknowledgment
    `unacknowledged`.
14. `## Frontier Verification` listing only checks grounded in this fixture.

Do not use fillable placeholders. Do not turn a denial record into an observed
trace, a missing score into a result, `defer` from the authorization decision
into a proving-result disposition, or a result-owner pointer into return or
acceptance. Return only the finished artifact.
