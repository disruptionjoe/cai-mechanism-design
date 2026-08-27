# Apply the execution-trace template to a frozen denied-start boundary

## Boundary

Write one complete synthetic Mechanism Design process fixture from only the
embedded evidence. Do not authorize or execute a treatment; do not fabricate
events, observations, transformations, data handling, artifacts, authority,
actors, dates, decisions, or results; do not create `CMD-0001-P8`; do not score
or disposition a candidate; and do not authorize contact, transfer, graduation,
deployment, publication, or external action. This tests whether an execution
trace records a pre-start halt without inventing execution. External action is
`none`.

## Evidence

<evidence path="proving/PROVING-EXECUTION-TRACE-TEMPLATE.md">
An execution trace records only one exactly authorized treatment against a
frozen plan. Every observed event must be evidence-linked and separate from
inference. The trace cannot extend authority, score evidence, disposition a
candidate, or create external action.
</evidence>

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-PLAN-TEMPLATE.md">
The frozen claim, falsifier, observable failure, bounded pass, unresolved
route, stops, correction, and permitted conclusions cannot be rewritten by an
execution trace. A proving plan does not authorize execution.
</evidence>

<evidence path="proving/PROVING-AUTHORIZATION-DECISION-BOUNDARY-FIXTURE.md">
The prepared decision for request `SYNTH-REQ-001` is `defer`; exact authorized
effect is `none`. Authority evidence, authorized decision-maker, decision time,
stop-authority rule, and operative grant are missing or unresolved. The
proposed actor and treatment remain non-operative. No execution or observation
exists.
</evidence>

<evidence fixture="SYNTHETIC-DENIED-TRACE-BOUNDARY-001-HEADER">
Trace `SYNTH-TRACE-DENIED-001@r1` refers to proving plan
`SYNTH-PROVE-001@r1`, candidate `SYNTH-CANDIDATE-REQUEST-001@r1`, source
`SYNTH-SOURCE-REQUEST-001@r1`, and result owner `synthetic-result-owner`.
Treatment type is `proposed_volatile_copy_and_relabel`. Execution authority,
operator, start time, and completion time are `none`. External action is `none`.
</evidence>

<evidence fixture="SYNTHETIC-DENIED-TRACE-BOUNDARY-001-START">
Request is `SYNTH-REQ-001`; plan is `SYNTH-PROVE-001@r1`; fixture is
`synthetic://fixture/SYNTH-REQUEST-001@r1`. No path, hash, validation run,
environment instance, or execution artifact was supplied. Last-known-good state
is the immutable input `alpha`. Pre-execution authority check result is
`failed_closed`: authorization pointer `none`, exact authorized effect `none`,
stop-authority rule unresolved. No treatment began.
</evidence>

<evidence fixture="SYNTHETIC-DENIED-TRACE-BOUNDARY-001-TREATMENT">
The proposed operations were read immutable input `alpha`, copy it in volatile
memory, relabel only the copy `beta`, emit a text diff, and discard the copy.
These operations, inputs, outputs, and isolated environment were requested but
never allowed or executed. Only one synthetic reviewer role has represented
standing; no real person or institution is represented. No data was handled.
</evidence>

<evidence fixture="SYNTHETIC-DENIED-TRACE-BOUNDARY-001-STOP">
The pre-execution stop is missing exact authorization. Its status is
`triggered`, authority effect is `invalidated`, action taken is `halt`, and
execution halted is `yes`. Evidence pointer is the frozen denied decision. No
chronological execution event, deviation, correction, rollback, recovery
action, trace artifact, score package, or result exists. Recovery available is
remain at immutable input `alpha`; recovery owner is
`synthetic-authority-owner` only for a future authorized decision.
</evidence>

<evidence path="ROADMAP.md">
CMD-0001 remains deferred. This fixture does not create P8 or candidate evidence.
</evidence>

## Work now

Draft the finished Markdown artifact
`proving/PROVING-EXECUTION-TRACE-DENIED-START-BOUNDARY-FIXTURE.md` with exactly
these sections:

1. YAML frontmatter with
   `artifact_type: synthetic_proving_execution_trace_denied_start_boundary_fixture`,
   `status: candidate_process_fixture`, and `external_action: none`.
2. `# Synthetic Proving Execution Trace Denied-Start Boundary Fixture`.
3. `## Use Boundary`.
4. `## Trace Header` using `none` for every absent execution field.
5. `## Frozen Start Conditions`.
6. `## Treatment Boundary` preserving requested scope as non-operative.
7. `## Chronological Observed Trace` stating that no execution event exists.
8. `## Stop And Deviation Log` recording only the supplied triggered pre-start stop.
9. `## Evidence Integrity And Counterevidence` preserving missing hashes,
   validation, artifacts, and provenance rather than inventing them.
10. `## Affected-Party, Data, And Legitimacy Trace` stating no data handling occurred.
11. `## Correction, Rollback, And Recovery` distinguishing no action performed
    from the available last-known-good route.
12. `## Score Return Package` with state `not_created` and no score or disposition.
13. `## Frontier Verification` listing only checks grounded in this fixture.

Do not use fillable placeholders, do not convert proposed treatment into an
allowed treatment, and do not create an execution event merely to record the
halt.
Return only the finished artifact.
