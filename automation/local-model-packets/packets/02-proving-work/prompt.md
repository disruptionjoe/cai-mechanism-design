# Score a synthetic trace whose authority deviation defeats the pass

## Boundary

Write one complete synthetic Mechanism Design process fixture from only the
embedded evidence. Preserve the supplied plan, grant, trace, deviation, stop,
rollback, validation, and `revise` score as frozen synthetic facts, but do not
treat pointer preservation as a bounded pass after the authority deviation;
do not invent events, evidence, hashes, authority, owners, dates, results,
decisions, or observations; do not create `CMD-0001-P8`; do not modify or
reopen `CMD-0001`; and do not authorize contact, transfer, graduation,
deployment, publication, or external action. External action is `none`.

## Evidence

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-TEMPLATE.md">
A score compares one executed, exactly authorized trace to its frozen claim,
falsifier, failure, pass, unresolved, stop, and prohibited-conclusion
conditions. Execution authority must cover the actual treatment and every
deviation; otherwise the score narrows or stops. A score does not choose or
execute a candidate disposition.
</evidence>

<evidence path="proving/PROVING-EXECUTION-TRACE-DENIED-START-BOUNDARY-FIXTURE.md">
The denied-start boundary records a triggered pre-start halt without
inventing execution, observation, score, result, disposition, or P8.
</evidence>

<evidence path="ROADMAP.md">
CMD-0001 remains deferred. This fixture creates no P8, proving result for
CMD-0001, or candidate disposition.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-AUTHORITY-DEVIATION-001-HEADER">
Score `SYNTH-SCORE-AUTHORITY-DEVIATION-001@r1` concerns proving plan
`SYNTH-PROVE-AUTHORITY-DEVIATION-001@r1`, candidate
`SYNTH-CANDIDATE-AUTHORITY-DEVIATION-001@r1`, and source inquiry
`SYNTH-SOURCE-AUTHORITY-DEVIATION-001@r1`. Treatment type is `synthetic`;
result owner is `synthetic-result-owner`; execution authority is
`synthetic://authorization/SYNTH-AUTHORITY-DEVIATION-001@grant-r1`; scorer is
`synthetic-proving-scorer`; scored at `2026-08-27T04:15:01Z`. External action
is `none`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-AUTHORITY-DEVIATION-001-PACKAGE">
Plan pointer is
`synthetic://plan/SYNTH-PROVE-AUTHORITY-DEVIATION-001@r1` with content
identifier `synthetic-content:plan-authority-deviation-001-r1`. Request pointer
is `synthetic://request/SYNTH-REQUEST-AUTHORITY-DEVIATION-001@r1` with content
identifier `synthetic-content:request-authority-deviation-001-r1`. Fixture
pointer is `synthetic://fixture/SYNTH-AUTHORITY-DEVIATION-001@r1` with content
identifier `synthetic-content:fixture-authority-deviation-001-r1`. Trace
pointer is `synthetic://trace/SYNTH-TRACE-AUTHORITY-DEVIATION-001@r1` with
content identifier `synthetic-content:trace-authority-deviation-001-r1`.
Validation pointer is
`synthetic://validation/SYNTH-VALIDATION-AUTHORITY-DEVIATION-001@r1` with
content identifier `synthetic-content:validation-authority-deviation-001-r1`
and result `passed` for trace integrity, identifiers, grant comparison, stop,
rollback, and final state.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-AUTHORITY-DEVIATION-001-PLAN">
The frozen claim is that changing one synthetic display label preserves source
pointer `synthetic://source/SYNTH-SOURCE-AUTHORITY-DEVIATION-001@r1`.
Falsifier is any source-pointer mutation. Observable failure is a source
pointer different from the frozen input. Bounded-pass condition is exact
source-pointer preservation with every operation inside the grant and no stop
trigger. Unresolved route is return deviation evidence to the result owner.
Stop on any operation outside the grant or any source, fixture, data, standing,
or risk revision. Prohibited conclusions are effectiveness, destination fit,
owner acceptance, authority beyond the grant, deployment readiness, or
external outcome.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-AUTHORITY-DEVIATION-001-GRANT">
The grant authorizes exactly one display-label update, comparison of the
unchanged source pointer, immediate stop on any other field mutation, and
rollback to `synthetic-state:alpha@r1` after a deviation. It does not authorize
changing summary field `synthetic://field/SUMMARY@r1`, continuing after a stop,
or treating rollback as permission for the unauthorized mutation.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-AUTHORITY-DEVIATION-001-TRACE">
The synthetic trace updated the display label and preserved the exact source
pointer. It then changed summary field `synthetic://field/SUMMARY@r1` to
`synthetic://field/SUMMARY@r2`, an operation outside the grant. The stop
triggered immediately; no later treatment step ran. The trace executed the
authorized rollback and restored final state `synthetic-state:alpha@r1`.
There were no real people, real data, external systems, or external actions.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-AUTHORITY-DEVIATION-001-RESULT">
Direct observations are exact source-pointer preservation, one unauthorized
summary-field mutation, triggered stop, no post-stop treatment, completed
rollback, and restored final state. The target pointer metric alone would have
matched the pass condition, but the bounded-pass condition also requires every
operation to remain inside the grant and no stop to trigger. Result is
`revise`; evidence type is validated synthetic trace; permitted disposition
support is `revise` only. The score creates no owner disposition.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-AUTHORITY-DEVIATION-001-CONTROLS">
Only one synthetic reviewer role represents standing. No real person,
institution, source owner, result owner, candidate owner, authority owner, or
validator is represented. Actual data handling is synthetic input only;
treatment risk and external action are `none`. Preserve the deviation at
`synthetic://negative-evidence/SYNTH-SCORE-AUTHORITY-DEVIATION-001@r1`;
correction owner is `synthetic-proving-plan-owner`; recovery is the completed
rollback to `synthetic-state:alpha@r1`. Exact next wake is a revised immutable
plan and grant that remove the unsupported operation, or an owner decision on
the returned `revise` support.
</evidence>

## Work now

Draft the finished Markdown artifact
`proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-AUTHORITY-DEVIATION-BOUNDARY-FIXTURE.md`
with exactly these sections:

1. YAML frontmatter with
   `artifact_type: synthetic_proving_score_authority_deviation_boundary_fixture`,
   `status: candidate_process_fixture`, and `external_action: none`.
2. `# Synthetic Proving-Score Authority-Deviation Boundary Fixture`.
3. `## Use Boundary`.
4. `## Score Header` using only supplied fixture values.
5. `## Frozen Plan And Evidence` preserving every supplied pointer and content
   identifier.
6. `## Claim And Decision Conditions`.
7. `## Observed Trace` separating observations from inference and preserving
   the stop and rollback chronology.
8. `## Evidence Grade And Counterevidence`.
9. `## Affected-Party, Data, And Legitimacy Check`.
10. `## Result` using `revise` and stating why source-pointer preservation does
    not satisfy the full bounded-pass condition.
11. `## Residual Uncertainty, Correction, And Recovery`.
12. `## Permitted Disposition Return` with `revise` support and no owner
    disposition.
13. `## Frontier Verification` listing only checks grounded in this fixture.

Do not use fillable placeholders. Do not turn an unauthorized operation into a
pass because rollback succeeded, turn a score into a disposition, or turn a
synthetic trace into real-world evidence. Return only the finished artifact.
