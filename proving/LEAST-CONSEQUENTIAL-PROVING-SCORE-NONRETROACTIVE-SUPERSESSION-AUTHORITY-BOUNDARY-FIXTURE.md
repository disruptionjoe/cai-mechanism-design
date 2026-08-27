---
artifact_type: synthetic_proving_score_nonretroactive_supersession_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---
# Synthetic Proving-Score Nonretroactive-Supersession-Authority Boundary Fixture

## Use Boundary

A score keeps direct evidence visible until an applicable immutable record
explicitly supersedes it. Exact coverage, replacement validity, authority
scope, and authority timing are separate checks. Complete coverage and valid
replacement artifacts cannot manufacture authority, and current authority
cannot silently ratify an earlier act when its grant is future-only.

## Score Header

Score `SYNTH-SCORE-NONRETROACTIVE-SUPERSESSION-001@r2` concerns plan
`SYNTH-PROVE-NONRETROACTIVE-SUPERSESSION-001@r2`, candidate
`SYNTH-CANDIDATE-NONRETROACTIVE-SUPERSESSION-001@r2`, and source
`SYNTH-SOURCE-NONRETROACTIVE-SUPERSESSION-001@r2` at revision
`synthetic-source-revision:nonretroactive-supersession-001-r2`. Treatment is
`synthetic`; result owner is `synthetic-result-owner`; execution authority is
`synthetic://authorization/SYNTH-NONRETROACTIVE-SUPERSESSION-001@grant-r2`;
scorer is `synthetic-proving-scorer`; scored at `2026-08-27T13:14:19Z`; and
external action is `none`.

## Frozen Plan And Evidence

Plan, trace, validation, supersession, and authority-validation pointers are
`synthetic://plan/SYNTH-PROVE-NONRETROACTIVE-SUPERSESSION-001@r2`,
`synthetic://trace/SYNTH-TRACE-NONRETROACTIVE-SUPERSESSION-001@r2`,
`synthetic://validation/SYNTH-NONRETROACTIVE-SUPERSESSION-001@r2`,
`synthetic://supersession/SYNTH-NONRETROACTIVE-SUPERSESSION-001@record-before-grant`,
and
`synthetic://authority-validation/SYNTH-NONRETROACTIVE-SUPERSESSION-001@r2`.
Their content identifiers are
`synthetic-content:plan-nonretroactive-supersession-001-r2`,
`synthetic-content:trace-nonretroactive-supersession-001-r2`,
`synthetic-content:validation-nonretroactive-supersession-001-r2`,
`synthetic-content:supersession-nonretroactive-supersession-001-record-before-grant`,
and
`synthetic-content:authority-validation-nonretroactive-supersession-001-r2`.

## Claim And Decision Conditions

Claim: one authorized synthetic normalization preserves both input pointers
and their equality relation at source revision r2. Falsifier: either pointer
changes, any valid unsuperseded direct observation records `unequal`, or a
purported supersession lacked authority when signed. `bounded_pass` requires
unchanged pointers, an applicable authorized supersession where invoked,
valid surviving observations, and agreement on `equal`. `unresolved` applies
when valid direct evidence conflicts or supersession authority was absent at
the asserted act.

Stop on unauthorized operation or any source, fixture, data, standing,
authority, or risk revision. Prohibited conclusions are effectiveness,
destination fit, owner acceptance, deployment readiness, and external outcome.

## Observed Trace

The authorized r2 normalization ran with no deviation. Both pointers remained
unchanged; stops did not trigger; and final state equals initial state. Valid
direct observations are
`synthetic-observation:comparison-equal-008-r2` recording `equal`,
`synthetic-observation:comparison-unequal-008a-r2` recording `unequal` at
position `a`, and
`synthetic-observation:comparison-unequal-008b-r2` recording `unequal` at
position `b`. All three are readable, in scope, and provenance-valid. No real
people, data, systems, or external actions were involved.

## Evidence Grade And Counterevidence

At `2026-08-27T13:05:00Z`, immutable record
`SYNTH-SUPERSESSION-EQUAL-008@record-before-grant` was signed by
`synthetic-result-owner` while no r2 supersession authority existed. It exactly
names `synthetic-observation:comparison-unequal-008a-r2` and
`synthetic-observation:comparison-unequal-008b-r2`, proposing replacements
`synthetic-observation:comparison-equal-008a-corrected-r2` and
`synthetic-observation:comparison-equal-008b-corrected-r2`. Both replacements
are readable, in scope, chronology-valid, checksum-valid, and record `equal` at
their respective positions. The record does not cover
`synthetic-observation:comparison-equal-008-r2`.

At `2026-08-27T13:10:00Z`, immutable grant
`SYNTH-SUPERSESSION-AUTHORITY-R2-001@grant-after-record` was signed by
`synthetic-supersession-authority-owner` under
`synthetic-supersession-authority-issuance@r2`. It authorizes
`synthetic-result-owner` to sign future supersession records for source
revision `synthetic-source-revision:nonretroactive-supersession-001-r2` only
after the grant time. It explicitly has no retroactive or ratification effect
and does not name or validate the earlier record.

Immutable authority validation by `synthetic-authority-validator` confirms the
record predates the grant by five minutes, no earlier delegation or authority
existed, and the grant is nonretroactive. The earlier record is unauthorized
despite exact coverage and valid replacements. All three original r2
observations remain valid and unsuperseded; their `equal`/`unequal` conflict
survives.

## Affected-Party, Data, And Legitimacy Check

One synthetic reviewer role represents standing. No real party or owner is
represented. Data is synthetic input only; risk and external action are
`none`.

## Result

The score is `unresolved`. The unauthorized earlier record supersedes nothing,
all three original observations survive, and their direct conflict remains.
The score supports `defer` only; it does not choose a candidate disposition.

## Residual Uncertainty, Correction, And Recovery

The record scope exactly covers only the two unequal observations and was
signed at `2026-08-27T13:05:00Z`. The grant scope is future-only for r2 and was
signed five minutes later at `2026-08-27T13:10:00Z`. Authority validation
confirms no earlier authority, no retroactivity, and no ratification. Negative
evidence is preserved at
`synthetic://negative-evidence/SYNTH-SCORE-NONRETROACTIVE-SUPERSESSION-001@r2`.

Correction owner is `synthetic-proving-plan-owner`. Recovery preserves the
unchanged r2 state, all three original observations, both valid replacement
artifacts, the earlier unauthorized record, the later grant, and the
authority-validation result. Exact next wake is one new immutable supersession
record signed after and within the r2 grant, an owner decision on returned
`defer` support, or a revision to source, trace, supersession, grant, authority
validation, standing, authority, or risk.

## Permitted Disposition Return

Return only `defer` support to `synthetic-result-owner`. No disposition is
chosen; no `CMD-0001-P8` is created; `CMD-0001` remains unchanged; and contact,
transfer, graduation, deployment, publication, and external action remain
unauthorized.

## Frontier Verification

- The earlier record exactly covers both unequal observations and both
  replacement artifacts are valid.
- Exact coverage and replacement validity remain separate from authority.
- Record-before-grant timing is five minutes; the current r2 grant is
  nonretroactive and future-only.
- All three r2 originals remain valid and unsuperseded, so the direct conflict
  survives and the result remains `unresolved`.
- Score and owner disposition remain separate; `CMD-0001`, P7 defer, and
  external-action state remain unchanged.
