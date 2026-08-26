# Apply the proving-execution request template to a frozen boundary fixture

## Boundary

Write one complete synthetic Mechanism Design process fixture from only the
embedded evidence. Do not authorize or execute a treatment; do not create
`CMD-0001-P8`; do not add evidence, actors, owners, authority, conditions,
observations, dates, decisions, or results; do not choose a candidate
disposition; and do not authorize contact, transfer, graduation, deployment,
publication, or external action. This tests a request boundary, not a real
proving step. External action is `none`.

## Evidence

<evidence path="proving/PROVING-EXECUTION-REQUEST-TEMPLATE.md">
A request freezes a plan, claim, source, fixture, evidence, treatment,
least-consequence case, requested authority, affected-party and data boundary,
stops, recovery, prepared state, and proposed handoff. It creates no grant or execution.
</evidence>

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-PLAN-TEMPLATE.md">
A plan freezes the exact claim, evidence, fixture, treatment, falsifier,
observable failure, bounded pass, unresolved route, stops, correction, and
permitted conclusions. It does not authorize execution.
</evidence>

<evidence fixture="SYNTHETIC-REQUEST-BOUNDARY-001">
Request `SYNTH-REQ-001` refers to proving plan `SYNTH-PROVE-001@r1`, candidate
`SYNTH-CANDIDATE-REQUEST-001@r1`, and source `SYNTH-SOURCE-REQUEST-001@r1`.
The requester is `synthetic-request-preparer`, proposed executor is
`synthetic-executor`, authority owner is `synthetic-authority-owner`, and
requested timestamp is `2026-08-26T00:00:00Z`. Exact authority evidence is
`none`, acknowledgment is `unacknowledged`, and external action is `none`.
</evidence>

<evidence fixture="SYNTHETIC-REQUEST-BOUNDARY-001-PLAN">
The claim is: copying the immutable synthetic input `alpha` to an isolated
in-memory output and relabeling the copy `beta` can test whether the trace keeps
input and output distinct. The fixture is
`synthetic://fixture/SYNTH-REQUEST-001@r1`, containing only the public labels
`alpha` and `beta`. The proposed operations are read the immutable input, copy
it in memory, relabel only the copy, emit a text diff, and discard the copy.
The falsifier is any mutation of the input or any trace that merges input and
output. Observable failure is an input change, missing diff, or merged
identity. Bounded pass is an unchanged input plus a distinct diff. The
unresolved route is real data or any persistent output. No action is the least
consequential alternative; manual comparison is equally safe but supplies less
trace discrimination. The last-known-good state is the immutable input.
</evidence>

<evidence fixture="SYNTHETIC-REQUEST-BOUNDARY-001-CONTROLS">
The requested environment is isolated volatile memory with no network,
persistence, account, or external action. The only represented standing is a
synthetic reviewer role; no real person or institution is represented. Data
retention is none after review. Pre-start stop is missing exact authorization.
Live stops are input mutation, persistence, network access, or trace ambiguity.
Any plan, actor, operation, input, output, environment, or authority change
requires a fresh decision. Correction is discard the copy and return to the
immutable input. Requested trace destination is
`synthetic://trace/SYNTH-REQUEST-001`; proposed score owner is
`synthetic-result-owner`.
</evidence>

<evidence path="ROADMAP.md">
CMD-0001 remains deferred. This fixture does not create P8 or candidate evidence.
</evidence>

## Work now

Draft the finished Markdown artifact
`proving/PROVING-EXECUTION-REQUEST-BOUNDARY-FIXTURE.md` with exactly these sections:

1. YAML frontmatter with `artifact_type: synthetic_proving_execution_request_boundary_fixture`,
   `status: candidate_process_fixture`, and `external_action: none`.
2. `# Synthetic Proving Execution Request Boundary Fixture`.
3. `## Use Boundary`.
4. `## Request Header` using only supplied fixture values.
5. `## Frozen Plan And Evidence`.
6. `## Requested Treatment And Least-Consequence Case`.
7. `## Requested Authority Scope` describing requested, not operative, authority.
8. `## Affected Parties, Data, And Legitimacy`.
9. `## Stops And Start-State Checks` preserving missing authorization as a pre-start stop.
10. `## Prepared Request` with state `ready_for_authorization_review`, exact
    non-effects, next owner `synthetic-authority-owner`, and wake only on an
    exact authorization decision or material plan change.
11. `## Proposed Execution Handoff` with acknowledgment `unacknowledged`,
    authorization pointer `none`, and handoff state `ready_for_authorization_review`.
12. `## Frontier Verification` listing only checks grounded in this fixture.

Do not use fillable placeholders and do not execute the requested treatment.
Return only the finished artifact.
