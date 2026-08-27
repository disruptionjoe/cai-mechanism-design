---
artifact_type: synthetic_proving_score_post_revocation_regrant_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---
# Synthetic Proving-Score Post-Revocation-Regrant-Authority Boundary Fixture

## Use Boundary
A score preserves original evidence, exact supersession coverage, replacement validity, authority scope and timing, revocation, regrant, and negative lineage as separate checks. This fixture preserves the pre-grant unauthorized record, one valid record under a future-only grant, a later future-only revocation, one unauthorized post-revocation record, one distinct future-only regrant, and one authorized but evidence-effect-redundant record under that regrant. The regrant does not reactivate the revoked grant, ratify either unauthorized record, or erase negative evidence. Surviving evidence remains all-`equal`; `bounded_pass` supports only `defer` and creates no owner disposition or stronger claim. Do not modify `CMD-0001`, create P8, or authorize external action.

## Score Header
Score `SYNTH-SCORE-POST-REVOCATION-REGRANT-001@r2` concerns plan `SYNTH-PROVE-POST-REVOCATION-REGRANT-001@r2`, candidate `SYNTH-CANDIDATE-POST-REVOCATION-REGRANT-001@r2`, source `SYNTH-SOURCE-POST-REVOCATION-REGRANT-001@r2`, and revision `synthetic-source-revision:post-revocation-regrant-001-r2`. Treatment is `synthetic`; result owner is `synthetic-result-owner`; scorer is `synthetic-proving-scorer`; external action is `none`. Matching plan, trace, validation, authority, and supersession pointers retain content identifiers under `synthetic-content:post-revocation-regrant-001-r2`. Negative-evidence pointer is `synthetic://negative-evidence/SYNTH-SCORE-POST-REVOCATION-REGRANT-001@r2`.

## Frozen Plan And Evidence
The clean trace preserves originals `synthetic-observation:comparison-equal-011-r2`, `synthetic-observation:comparison-unequal-011a-r2`, and `synthetic-observation:comparison-unequal-011b-r2`, plus valid replacements `synthetic-observation:comparison-equal-011a-corrected-r2` and `synthetic-observation:comparison-equal-011b-corrected-r2`. Both pointers are unchanged; all originals are readable, in scope, and provenance-valid; both replacements are readable, in scope, chronology-valid, checksum-valid, and record `equal`.

## Claim And Decision Conditions
The falsifier is a changed pointer, one valid unsuperseded `unequal` observation, one invalid replacement, or any invoked supersession lacking applicable authority when signed. `bounded_pass` requires unchanged pointers, exact authorized coverage where invoked, valid replacements, valid surviving observations, and agreement on `equal`. `unresolved` applies when valid surviving direct evidence conflicts. Stops trigger on any source, fixture, data, standing, authority, grant, revocation, record, replacement, validation, or risk revision. Prohibited conclusions are effectiveness, destination fit, owner acceptance, deployment readiness, and external outcome.

## Observed Trace
At `2026-08-27T13:05:00Z`, `SYNTH-SUPERSESSION-EQUAL-011@record-before-grant` is unauthorized. At `13:10:00Z`, grant `SYNTH-SUPERSESSION-AUTHORITY-R2-004@grant-before-valid-record` is signed by `synthetic-supersession-authority-owner` under `synthetic-supersession-authority-issuance@r2`; it is future-only and nonretroactive. At `13:15:00Z`, `SYNTH-SUPERSESSION-EQUAL-011@valid-record-before-revocation` is validly signed within grant 004 and exactly supersedes both unequal originals with the two valid replacements. At `13:20:00Z`, future-only revocation `SYNTH-SUPERSESSION-AUTHORITY-R2-004@future-revocation` ends authority only for future records and does not undo the valid record. At `13:25:00Z`, `SYNTH-SUPERSESSION-EQUAL-011@record-after-revocation` is unauthorized and supersedes nothing. At `13:30:00Z`, distinct grant `SYNTH-SUPERSESSION-AUTHORITY-R2-005@regrant-after-revocation` is signed by the same authority owner under `synthetic-supersession-authority-issuance@r2`; it authorizes only future records for the named r2 source and neither revives grant 004 nor ratifies prior records. At `13:35:00Z`, `SYNTH-SUPERSESSION-EQUAL-011@valid-record-after-regrant` is newly signed by `synthetic-result-owner` under grant 005, independently names both unequal originals and both valid replacements, covers nothing else, and is readable, immutable, source-matched, chronology-valid, and checksum-valid.

## Supersession, Revocation, And Regrant Lineage
Immutable authority validation preserves every record and confirms both unauthorized records remain negative evidence, grant 004 and its revocation retain their exact history, regrant 005 is distinct and future-only, and both valid records were signed within their own authority. The `13:15:00Z` record is sufficient to supersede both unequal originals. The `13:35:00Z` record is authorized but evidence-effect redundant because it independently covers the same exact originals with the same valid replacements; it changes no surviving evidence. Only the original equal observation and two valid equal replacements survive, so there is no surviving conflict.

## Affected-Party, Data, And Legitimacy Check
One synthetic reviewer role represents standing; no real party or owner is represented. Data is synthetic input only; risk and external action are `none`. Preserve the plan, trace, validation, three originals, two replacements, two unauthorized records, grant 004, its future-only revocation, regrant 005, both valid records, every authority and supersession pointer, matching content identifiers under `synthetic-content:post-revocation-regrant-001-r2`, and the negative-evidence pointer. Correction owner is `synthetic-proving-plan-owner`.

## Result
Surviving evidence is all-`equal`. Result is `bounded_pass`; disposition support is `defer`. The authorized later record adds no evidence effect. No owner disposition, effectiveness claim, destination fit, owner acceptance, deployment readiness, external outcome, P8, or external action is created.

## Residual Uncertainty, Correction, And Recovery
Stops trigger on any source, fixture, data, standing, authority, grant, revocation, record, replacement, validation, or risk revision. Recovery preserves the complete lineage, reverses only the affected valid record if its own authority or checksum later fails, and restores `unresolved` only if no valid exact record remains. Exact wake is an owner decision on returned defer support or any named revision.

## Permitted Disposition Return
`bounded_pass` supports only `defer`. It creates no owner disposition or stronger claim.

## Frontier Verification
Verify unchanged source and pointers; three originals and two valid replacements; pre-grant nonauthority; grant 004 timing and scope; valid-record exact coverage; future-only revocation; post-revocation nonauthority; distinct future-only regrant 005; the later record's own authority, exact coverage, and redundancy; preserved negative evidence and matching content identifiers; no surviving conflict; `bounded_pass`; `defer`; correction, recovery, stops, prohibited conclusions, and exact wake; and unchanged `CMD-0001` and external-action state.
