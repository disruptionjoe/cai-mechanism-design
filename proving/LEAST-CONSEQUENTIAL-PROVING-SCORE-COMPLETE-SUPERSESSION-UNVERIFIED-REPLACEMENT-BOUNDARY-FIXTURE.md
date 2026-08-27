---
artifact_type: synthetic_proving_score_complete_supersession_unverified_replacement_boundary_fixture
status: candidate_process_fixture
external_action: none
---
# Synthetic Proving-Score Complete-Supersession Unverified-Replacement Boundary Fixture

## Use Boundary

This synthetic score keeps direct evidence visible until an applicable
immutable record explicitly supersedes it. Supersession authority and
replacement-evidence validity are separate checks. Complete supersession
coverage cannot manufacture valid replacement evidence. A bounded result and a
later owner disposition remain separate decisions. The fixture creates no
`CMD-0001-P8`, candidate disposition, transfer, graduation, deployment, or
external action.

## Score Header

- Score: `SYNTH-SCORE-UNVERIFIED-REPLACEMENT-001@r1`.
- Plan: `SYNTH-PROVE-UNVERIFIED-REPLACEMENT-001@r1`.
- Candidate: `SYNTH-CANDIDATE-UNVERIFIED-REPLACEMENT-001@r1`.
- Source: `SYNTH-SOURCE-UNVERIFIED-REPLACEMENT-001@r1`.
- Treatment: `synthetic`.
- Result owner: `synthetic-result-owner`.
- Execution authority: `synthetic://authorization/SYNTH-UNVERIFIED-REPLACEMENT-001@grant-r1`.
- Scorer: `synthetic-proving-scorer`.
- Scored at: `2026-08-27T11:16:38Z`.
- External action: `none`.

## Frozen Plan And Evidence

| Record | Pointer | Content identifier |
| --- | --- | --- |
| Plan | `synthetic://plan/SYNTH-PROVE-UNVERIFIED-REPLACEMENT-001@r1` | `synthetic-content:plan-unverified-replacement-001-r1` |
| Request | `synthetic://request/SYNTH-REQUEST-UNVERIFIED-REPLACEMENT-001@r1` | `synthetic-content:request-unverified-replacement-001-r1` |
| Fixture | `synthetic://fixture/SYNTH-UNVERIFIED-REPLACEMENT-001@r1` | `synthetic-content:fixture-unverified-replacement-001-r1` |
| Trace | `synthetic://trace/SYNTH-TRACE-UNVERIFIED-REPLACEMENT-001@r1` | `synthetic-content:trace-unverified-replacement-001-r1` |
| Validation | `synthetic://validation/SYNTH-UNVERIFIED-REPLACEMENT-001@r1` | `synthetic-content:validation-unverified-replacement-001-r1` |
| Supersession | `synthetic://supersession/SYNTH-UNVERIFIED-REPLACEMENT-001@r1` | `synthetic-content:supersession-unverified-replacement-001-r1` |
| Replacement validation | `synthetic://replacement-validation/SYNTH-UNVERIFIED-REPLACEMENT-001@r1` | `synthetic-content:replacement-validation-unverified-replacement-001-r1` |

## Claim And Decision Conditions

The claim is that one authorized synthetic normalization preserves both input
pointers and their equality relation. The falsifier is either pointer changing,
one valid unsuperseded direct comparison observation recording `unequal`, or
either named comparison position lacking a provenance-valid unsuperseded
observation. `bounded_pass` requires unchanged pointers, provenance-valid
unsuperseded observations at both named positions, and agreement on `equal`.
The result is `unresolved` when valid evidence conflicts or either position
lacks a valid surviving observation. Stop on unauthorized operation or any
source, fixture, data, standing, authority, or risk revision. Prohibited
conclusions are effectiveness, destination fit, owner acceptance, deployment
readiness, and external outcome.

## Observed Trace

The authorized normalization ran with no deviation. Both pointers remained
unchanged, stops did not trigger, and final state equals initial state. Three
original direct observations are readable, in scope, and provenance-valid:

- `synthetic-observation:comparison-equal-006-r1` records `equal`.
- `synthetic-observation:comparison-unequal-006a-r1` records `unequal` at
  comparison position `a`.
- `synthetic-observation:comparison-unequal-006b-r1` records `unequal` at
  comparison position `b`.

No real people, data, systems, or external actions were involved.

## Evidence Grade And Counterevidence

The trace validator passed structure, identifiers, execution authority,
chronology, stops, and final state. It lists all three original direct
observations and marks `comparison_conflict: true`. It does not reconcile or
supersede them. The two original `unequal` observations remain visible as
superseded negative evidence after the later record is applied.

## Affected-Party, Data, And Legitimacy Check

One synthetic reviewer role represents standing; no real party or owner is
represented. Data is synthetic input only. Risk and external action are
`none`. This representation supplies no consent, owner acceptance, candidate
authority, or disposition authority.

## Result

Valid surviving evidence consists of
`synthetic-observation:comparison-equal-006-r1` and
`synthetic-observation:comparison-equal-006a-corrected-r1`. Comparison position
`b` lacks a provenance-valid surviving observation because its named
replacement has a checksum mismatch. Both pointers remain unchanged, but the
frozen plan supports `unresolved`, not `bounded_pass`. Evidence type is a
validated synthetic trace with authorized complete supersession and incomplete
valid replacement evidence. Permitted disposition support is `defer` only; the
score does not choose a disposition.

## Residual Uncertainty, Correction, And Recovery

The later immutable supersession record is signed by
`synthetic-result-owner` under
`synthetic-result-owner-supersession@r1`. Its exact scope covers
`synthetic-observation:comparison-unequal-006a-r1` and
`synthetic-observation:comparison-unequal-006b-r1`, replacing them respectively
with `synthetic-observation:comparison-equal-006a-corrected-r1` and
`synthetic-observation:comparison-equal-006b-corrected-r1`. It explicitly does
not cover, invalidate, or supersede
`synthetic-observation:comparison-equal-006-r1`. Its authority is valid only
for those two named replacement relations and supplies no candidate-
disposition, acceptance, transfer, graduation, deployment, or external-action
authority.

Replacement `synthetic-observation:comparison-equal-006a-corrected-r1` is
readable, in scope, chronology-valid, checksum-valid, and records `equal` at
position `a`. Replacement
`synthetic-observation:comparison-equal-006b-corrected-r1` is readable and
records `equal` at position `b`, but its immutable content checksum does not
match the checksum named by the supersession record. The mismatch recorded by
`synthetic-replacement-validator` makes the second replacement invalid.

Preserve the original conflict, exact supersession relation, valid replacement,
and checksum-mismatched replacement at
`synthetic://negative-evidence/SYNTH-SCORE-UNVERIFIED-REPLACEMENT-001@r1`.
Correction owner is `synthetic-proving-plan-owner`. Recovery preserves the
unchanged frozen state, all original observations, both named replacements,
the checksum mismatch, and exact supersession coverage. The exact next wake is
one immutable provenance-valid replacement for comparison position `b`, an
owner decision on returned `defer` support, or a revision to source, trace,
supersession, replacement validation, standing, authority, or risk.

## Permitted Disposition Return

The score returns `unresolved` with `defer` support. It does not choose a
disposition. The supersession record does not authorize candidate disposition,
acceptance, transfer, graduation, deployment, publication, or external action.
`CMD-0001`, P7 defer, and external-action state remain unchanged.

## Frontier Verification

- Confirm complete exact supersession coverage for positions `a` and `b`.
- Confirm all three original observations remain preserved.
- Confirm the position-`a` replacement is provenance-valid.
- Confirm the position-`b` replacement records `equal` but is invalid because
  of its immutable checksum mismatch.
- Confirm the result remains `unresolved`, not `bounded_pass`.
- Confirm bounded result and owner disposition remain separate.
- Confirm `CMD-0001`, P7 defer, and external-action state remain unchanged.
