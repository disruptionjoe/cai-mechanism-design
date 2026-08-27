---
artifact_type: synthetic_proving_score_stale_supersession_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---
# Synthetic Proving-Score Stale-Supersession-Authority Boundary Fixture

## Use Boundary

A score keeps direct evidence visible until an applicable immutable record
explicitly supersedes it. Exact coverage, replacement validity, and current
supersession authority are separate checks. Complete coverage cannot
manufacture current authority, and valid replacement evidence cannot make
stale authority current. A bounded result and a later owner disposition remain
separate decisions.

`CMD-0001` remains deferred. This synthetic fixture creates no P8, proving
result for `CMD-0001`, candidate disposition, contact, transfer, graduation,
deployment, publication, or external action.

## Score Header

Score `SYNTH-SCORE-STALE-SUPERSESSION-001@r2` concerns plan
`SYNTH-PROVE-STALE-SUPERSESSION-001@r2`, candidate
`SYNTH-CANDIDATE-STALE-SUPERSESSION-001@r2`, and source
`SYNTH-SOURCE-STALE-SUPERSESSION-001@r2` at revision
`synthetic-source-revision:stale-supersession-001-r2`. Treatment is
`synthetic`; result owner is `synthetic-result-owner`; execution authority is
`synthetic://authorization/SYNTH-STALE-SUPERSESSION-001@grant-r2`; scorer is
`synthetic-proving-scorer`; scored at `2026-08-27T12:14:29Z`; external action
is `none`.

## Frozen Plan And Evidence

Plan, trace, validation, supersession, and authority-validation pointers are
`synthetic://plan/SYNTH-PROVE-STALE-SUPERSESSION-001@r2`,
`synthetic://trace/SYNTH-TRACE-STALE-SUPERSESSION-001@r2`,
`synthetic://validation/SYNTH-STALE-SUPERSESSION-001@r2`,
`synthetic://supersession/SYNTH-STALE-SUPERSESSION-001@record-r1`, and
`synthetic://authority-validation/SYNTH-STALE-SUPERSESSION-001@r2`.

Their content identifiers are
`synthetic-content:plan-stale-supersession-001-r2`,
`synthetic-content:trace-stale-supersession-001-r2`,
`synthetic-content:validation-stale-supersession-001-r2`,
`synthetic-content:supersession-stale-supersession-001-record-r1`, and
`synthetic-content:authority-validation-stale-supersession-001-r2`.

## Claim And Decision Conditions

Claim: one authorized synthetic normalization preserves both input pointers
and their equality relation at source revision r2. Falsifier: either pointer
changes, any valid unsuperseded direct observation records `unequal`, or a
purported supersession lacks current authority for r2. `bounded_pass` requires
unchanged pointers, current applicable supersession where invoked, valid
surviving observations, and agreement on `equal`. `unresolved` applies when
valid direct evidence conflicts or supersession authority is not current.

Stop on unauthorized operation or any source, fixture, data, standing,
authority, or risk revision. Prohibited conclusions are effectiveness,
destination fit, owner acceptance, deployment readiness, and external outcome.

## Observed Trace

The authorized r2 normalization ran with no deviation. Both pointers remained
unchanged; stops did not trigger; final state equals initial state. Valid
direct observations are `synthetic-observation:comparison-equal-007-r2`
recording `equal`,
`synthetic-observation:comparison-unequal-007a-r2` recording `unequal` at
position `a`, and `synthetic-observation:comparison-unequal-007b-r2` recording
`unequal` at position `b`. All three are readable, in scope, and
provenance-valid. No real people, data, systems, or external actions were
involved.

## Evidence Grade And Counterevidence

Later immutable record `SYNTH-SUPERSESSION-EQUAL-007@record-r1` is signed by
`synthetic-result-owner` under
`synthetic-result-owner-supersession-source-r1@r1`. It exactly names both
`synthetic-observation:comparison-unequal-007a-r2` and
`synthetic-observation:comparison-unequal-007b-r2`, proposing respective
replacements `synthetic-observation:comparison-equal-007a-corrected-r2` and
`synthetic-observation:comparison-equal-007b-corrected-r2`. Both replacements
are readable, in scope, chronology-valid, checksum-valid, and record `equal`
at their respective positions. The record does not cover
`synthetic-observation:comparison-equal-007-r2` because that observation does
not assert `unequal` and needs no replacement.

The record therefore has exact coverage of both direct `unequal` observations,
and both proposed replacements are valid artifacts. Those facts do not resolve
whether the signer possessed current supersession authority for r2.

## Affected-Party, Data, And Legitimacy Check

One synthetic reviewer role represents standing; no real party or owner is
represented. Data is synthetic input only; risk and external action are
`none`.

## Result

Immutable authority validation by `synthetic-authority-validator` proves that
`synthetic-result-owner-supersession-source-r1@r1` applies only to source
revision `synthetic-source-revision:stale-supersession-001-r1`. No delegation,
continuation, or renewed authority exists for r2. The r1 authority cannot
supersede any r2 observation. All three original r2 observations remain valid
and unsuperseded; their direct `equal`/`unequal` conflict survives. The result
is `unresolved` with `defer` support.

## Residual Uncertainty, Correction, And Recovery

The record scope exactly names both r2 `unequal` observations, both replacement
artifacts validate, and the authority mismatch alone prevents supersession.
Preserve the original conflict, stale record, valid replacement artifacts, and
authority mismatch at
`synthetic://negative-evidence/SYNTH-SCORE-STALE-SUPERSESSION-001@r2`.

Correction owner is `synthetic-proving-plan-owner`. Recovery preserves the
unchanged r2 state, all three original observations, both replacement
artifacts, the stale authority record, and the authority-validation result.
Exact next wake is one immutable supersession authority valid for source
revision r2, an owner decision on returned `defer` support, or a revision to
source, trace, supersession, authority validation, standing, authority, or
risk.

## Permitted Disposition Return

Return only `defer` support to the result owner. Do not create
`CMD-0001-P8`, modify `CMD-0001`, choose a disposition, or authorize contact,
transfer, graduation, deployment, publication, or external action. External
action is `none`.

## Frontier Verification

- Verify `SYNTH-SUPERSESSION-EQUAL-007@record-r1` exactly covers both r2
  `unequal` observations and both named `equal` replacements are valid.
- Verify `synthetic-result-owner-supersession-source-r1@r1` is limited to
  source revision r1 and has no delegation, continuation, or renewal for r2.
- Verify all three original r2 observations remain unchanged, valid, and
  unsuperseded, so their direct conflict survives.
- Verify the result remains `unresolved` with `defer` support and is separate
  from any later owner disposition.
- Verify `CMD-0001`, P7 defer, candidate state, and external-action state remain
  unchanged.
