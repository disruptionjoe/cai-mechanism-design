# Score complete supersession with one unverified replacement

## Boundary

Write one complete synthetic Mechanism Design score fixture from only the
embedded evidence. Preserve the authorized clean trace, one direct `equal`
observation, two direct `unequal` observations, a later immutable result-owner
supersession record with exact coverage of both `unequal` observations, and two
named `equal` replacements. One replacement is provenance-valid; the other has
an immutable checksum mismatch and is not a valid direct observation. Complete
supersession coverage does not manufacture valid replacement evidence. The
frozen plan requires a provenance-valid comparison observation for both named
positions before `bounded_pass`, so the result remains `unresolved` with
`defer` support. The supersession record does not authorize candidate
disposition, transfer, graduation, deployment, or external action. Do not
create `CMD-0001-P8`, modify `CMD-0001`, choose a disposition, or authorize
contact, transfer, graduation, deployment, publication, or external action.
External action is `none`.

## Evidence

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-TEMPLATE.md">
A score keeps direct evidence visible until an applicable immutable record
explicitly supersedes it. Supersession authority and replacement-evidence
validity are separate checks. A bounded result and a later owner disposition
remain separate decisions.
</evidence>

<evidence path="ROADMAP.md">
`CMD-0001` remains deferred. This fixture creates no P8, proving result for
`CMD-0001`, or candidate disposition.
</evidence>

<evidence path="proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-COMPLETE-SUPERSESSION-BOUNDARY-FIXTURE.md">
Complete result-owner supersession can support `bounded_pass` only when every
surviving replacement observation is valid and all required comparison
positions are covered by provenance-valid unsuperseded evidence.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-UNVERIFIED-REPLACEMENT-001-HEADER">
Score `SYNTH-SCORE-UNVERIFIED-REPLACEMENT-001@r1` concerns plan
`SYNTH-PROVE-UNVERIFIED-REPLACEMENT-001@r1`, candidate
`SYNTH-CANDIDATE-UNVERIFIED-REPLACEMENT-001@r1`, and source
`SYNTH-SOURCE-UNVERIFIED-REPLACEMENT-001@r1`. Treatment is `synthetic`;
result owner is `synthetic-result-owner`; execution authority is
`synthetic://authorization/SYNTH-UNVERIFIED-REPLACEMENT-001@grant-r1`; scorer
is `synthetic-proving-scorer`; scored at `2026-08-27T11:16:38Z`; external
action is `none`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-UNVERIFIED-REPLACEMENT-001-PACKAGE">
Plan, request, fixture, trace, validation, supersession, and replacement-
validation pointers are respectively
`synthetic://plan/SYNTH-PROVE-UNVERIFIED-REPLACEMENT-001@r1`,
`synthetic://request/SYNTH-REQUEST-UNVERIFIED-REPLACEMENT-001@r1`,
`synthetic://fixture/SYNTH-UNVERIFIED-REPLACEMENT-001@r1`,
`synthetic://trace/SYNTH-TRACE-UNVERIFIED-REPLACEMENT-001@r1`,
`synthetic://validation/SYNTH-UNVERIFIED-REPLACEMENT-001@r1`,
`synthetic://supersession/SYNTH-UNVERIFIED-REPLACEMENT-001@r1`, and
`synthetic://replacement-validation/SYNTH-UNVERIFIED-REPLACEMENT-001@r1`.
Their content identifiers are respectively
`synthetic-content:plan-unverified-replacement-001-r1`,
`synthetic-content:request-unverified-replacement-001-r1`,
`synthetic-content:fixture-unverified-replacement-001-r1`,
`synthetic-content:trace-unverified-replacement-001-r1`,
`synthetic-content:validation-unverified-replacement-001-r1`,
`synthetic-content:supersession-unverified-replacement-001-r1`, and
`synthetic-content:replacement-validation-unverified-replacement-001-r1`.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-UNVERIFIED-REPLACEMENT-001-PLAN">
Claim: one authorized synthetic normalization preserves both input pointers and
their equality relation. Falsifier: either pointer changes, one valid
unsuperseded direct comparison observation records `unequal`, or either named
comparison position lacks a provenance-valid unsuperseded observation. Bounded
pass: both pointers remain unchanged, both named comparison positions have a
provenance-valid unsuperseded observation, and all such observations agree on
`equal`. Unresolved: valid evidence conflicts or either required comparison
position lacks a valid surviving observation. Stop on unauthorized operation
or source, fixture, data, standing, authority, or risk revision. Prohibited
conclusions are effectiveness, destination fit, owner acceptance, deployment
readiness, and external outcome.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-UNVERIFIED-REPLACEMENT-001-TRACE">
The authorized normalization ran with no deviation. Both pointers remained
unchanged; stops did not trigger; final state equals initial state. The trace
contains valid direct observation
`synthetic-observation:comparison-equal-006-r1` recording `equal`, valid direct
observation `synthetic-observation:comparison-unequal-006a-r1` recording
`unequal` at comparison position `a`, and valid direct observation
`synthetic-observation:comparison-unequal-006b-r1` recording `unequal` at
comparison position `b`. All three original observations are readable, in
scope, and provenance-valid. No real people, data, systems, or external actions
were involved.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-UNVERIFIED-REPLACEMENT-001-VALIDATION">
The trace validator passed structure, identifiers, execution authority,
chronology, stops, and final state. It lists all three original direct
observations and marks `comparison_conflict: true`. It does not reconcile or
supersede them.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-UNVERIFIED-REPLACEMENT-001-SUPERSESSION">
The later immutable record is signed by `synthetic-result-owner` under
`synthetic-result-owner-supersession@r1`. Its exact coverage names
`synthetic-observation:comparison-unequal-006a-r1` and
`synthetic-observation:comparison-unequal-006b-r1`, replacing them respectively
with `synthetic-observation:comparison-equal-006a-corrected-r1` and
`synthetic-observation:comparison-equal-006b-corrected-r1`. It explicitly does
not cover, invalidate, or supersede
`synthetic-observation:comparison-equal-006-r1`. Its authority is valid only
for the two named replacement relations and supplies no candidate-disposition,
acceptance, transfer, graduation, deployment, or external-action authority.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-UNVERIFIED-REPLACEMENT-001-REPLACEMENTS">
Replacement observation `synthetic-observation:comparison-equal-006a-corrected-r1`
is readable, in scope, chronology-valid, and checksum-valid and records `equal`
at comparison position `a`. Replacement observation
`synthetic-observation:comparison-equal-006b-corrected-r1` is readable and
records `equal` at comparison position `b`, but its immutable content checksum
does not match the checksum named by the supersession record. The mismatch is
recorded by `synthetic-replacement-validator`; the second replacement is not
provenance-valid and cannot satisfy the frozen plan.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-UNVERIFIED-REPLACEMENT-001-RESULT">
The two original `unequal` observations remain visible as superseded negative
evidence. Valid surviving evidence consists of
`synthetic-observation:comparison-equal-006-r1` and
`synthetic-observation:comparison-equal-006a-corrected-r1`. Comparison position
`b` lacks a provenance-valid surviving observation because its named
replacement has a checksum mismatch. Both pointers remain unchanged, but the
frozen plan supports `unresolved`, not `bounded_pass`. Evidence type is a
validated synthetic trace with authorized complete supersession and incomplete
valid replacement evidence. Permitted disposition support is `defer` only; the
score does not choose a disposition.
</evidence>

<evidence fixture="SYNTHETIC-SCORE-UNVERIFIED-REPLACEMENT-001-CONTROLS">
One synthetic reviewer role represents standing; no real party or owner is
represented. Data is synthetic input only; risk and external action are
`none`. Preserve the original conflict, exact supersession relation, valid
replacement, and checksum-mismatched replacement at
`synthetic://negative-evidence/SYNTH-SCORE-UNVERIFIED-REPLACEMENT-001@r1`.
Correction owner is `synthetic-proving-plan-owner`. Recovery preserves the
unchanged frozen state, all original observations, both named replacements,
the checksum mismatch, and exact supersession coverage. Exact next wake is one
immutable provenance-valid replacement for comparison position `b`, an owner
decision on returned `defer` support, or a revision to source, trace,
supersession, replacement validation, standing, authority, or risk.
</evidence>

## Work now

Draft
`proving/LEAST-CONSEQUENTIAL-PROVING-SCORE-COMPLETE-SUPERSESSION-UNVERIFIED-REPLACEMENT-BOUNDARY-FIXTURE.md`
with YAML frontmatter (`artifact_type:
synthetic_proving_score_complete_supersession_unverified_replacement_boundary_fixture`,
`status: candidate_process_fixture`, `external_action: none`) and exactly these
body sections: `Use Boundary`, `Score Header`, `Frozen Plan And Evidence`,
`Claim And Decision Conditions`, `Observed Trace`, `Evidence Grade And
Counterevidence`, `Affected-Party, Data, And Legitimacy Check`, `Result`,
`Residual Uncertainty, Correction, And Recovery`, `Permitted Disposition
Return`, and `Frontier Verification`.

Keep all three original direct observations, both named replacement
observations, the exact supersession coverage, and the checksum mismatch
visible. Put supersession scope, replacement validity, the negative-evidence
pointer, correction owner, recovery, and exact next wake in `Residual
Uncertainty, Correction, And Recovery`, not in the affected-party section.
Preserve every identifier, content identifier, stop, prohibited conclusion,
non-effect, and wake. In `Frontier Verification`, use bullets that explicitly
check complete exact coverage, original-observation preservation, the valid
position-`a` replacement, the invalid position-`b` replacement, `unresolved`,
disposition separation, and unchanged `CMD-0001` and external-action state.
First line must be `---`; close the YAML frontmatter with a later line
containing only `---`; immediately after frontmatter use the title
`# Synthetic Proving-Score Complete-Supersession Unverified-Replacement Boundary Fixture`;
use `##` for every named body section and deeper headings only within a named
section; do not use a code fence. Return only the finished artifact.
