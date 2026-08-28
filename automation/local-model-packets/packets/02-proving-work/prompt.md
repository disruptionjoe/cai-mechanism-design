# Execute one synthetic revise disposition after exact revision authority

## Boundary

Write one complete synthetic disposition fixture from only the embedded
evidence. Preserve the bounded pass, accepted return, invalid and retracted
first defer, recovery, separately reauthorized defer, all three prior revise
requests and refusals, the unsupported concern, source-backed evidence, all
negative evidence, and current synthetic state `deferred`. Add one exact
one-use candidate-disposition revision authority and one authorized synthetic
`revise` decision. This changes only the synthetic disposition to
`revision_required`; it does not revise candidate content, execute a proving
plan, create P8, or change a real candidate. It is not transfer, graduation,
deployment, publication, contact, or external action. External action is
`none`. Do not modify `CMD-0001` or create P8.

## Frozen evidence

Use `ROADMAP.md`,
`proving/LEAST-CONSEQUENTIAL-PROVING-PLAN-TEMPLATE.md`,
`dispositions/CANDIDATE-DISPOSITION-DECISION-TEMPLATE.md`, and
`dispositions/CANDIDATE-DISPOSITION-SYNTHETIC-SOURCE-BACKED-EVIDENCE-REVISE-REQUEST-REFUSED-NO-REVISION-AUTHORITY-BOUNDARY-FIXTURE.md`.
Freeze fixture
`SYNTH-CANDIDATE-REVISE-AUTHORIZED-AFTER-SOURCE-EVIDENCE-001@r2`, plan
`SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, score
`SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, source
`SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, candidate
`SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, immutable trace and
validation, return `SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2`,
return acceptance, invalid first defer, checksum revision, correction,
recovery, reauthorization, reauthorized defer, three requests and refusals,
the unsupported concern, and source-backed evidence. The score result remains
`bounded_pass`; no real state changes.

Originals remain `synthetic-observation:comparison-equal-014-r2`,
`synthetic-observation:comparison-unequal-014a-r2`, and
`synthetic-observation:comparison-unequal-014b-r2`; replacements remain
`synthetic-observation:comparison-equal-014a-corrected-r2` and
`synthetic-observation:comparison-equal-014b-corrected-r2`. Grants 006, 007,
and 008, three future-only revocations, three valid supersession records, and
four unauthorized records remain distinct. Negative evidence remains at
`synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`.

In the section that consumes it, copy this literal authority lineage:

- return acceptance — `SYNTH-RESULT-RETURN-ACCEPTANCE-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-result-return-acceptance-decision-authority@r2`; decision `SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2`; content `synthetic-content:second-regrant-defer-return-acceptance-decision-001-r2`; consumed
- first defer — `SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-decision-authority@r2`; decider `synthetic-candidate-disposition-decider`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-decision-001-r2`; consumed and decision retracted
- recovery — `SYNTH-CANDIDATE-DEFER-DISPOSITION-CORRECTION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-correction-decision-authority@r2`; decider `synthetic-proving-plan-owner`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-RECOVERY-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-recovery-decision-001-r2`; consumed
- defer reauthorization — `SYNTH-CANDIDATE-DEFER-REAUTHORIZATION-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-reauthorization-decision-authority@r2`; decider `synthetic-candidate-disposition-redecider`; decision `SYNTH-CANDIDATE-DEFER-REAUTHORIZED-DECISION-001@r2`; content `synthetic-content:candidate-defer-reauthorized-decision-001-r2`; consumed

Preserve first request `SYNTH-CANDIDATE-REVISE-REQUEST-001@r2`, review
authority `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-001@r2`, and
refusal `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-001@r2` with record
`revise_request_not_admitted_missing_new_evidence_and_revision_authority`.
Preserve concern `SYNTH-CANDIDATE-REVISION-CONCERN-001@r2`, second request
`SYNTH-CANDIDATE-REVISE-REQUEST-002@r2`, review authority
`SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-002@r2`, and refusal
`SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-002@r2` with record
`renewed_revise_request_not_admitted_concern_is_not_source_backed_evidence_and_revision_authority_absent`.

Preserve source-backed evidence `SYNTH-CANDIDATE-REVISION-EVIDENCE-001@r2`,
signed at `2026-08-27T22:40:12Z` by `synthetic-source-owner` under
`synthetic-candidate-revision-evidence-record-creation-authority@r2`, with
content ID `synthetic-content:candidate-revision-evidence-001-r2` and valid
checksum. It names source revision
`synthetic-source-revision:second-regrant-second-revocation-002-r3`,
deficiency `unsupported_concern_requires_source_backed_revision_basis`,
correction gate `verify_source_revision_and_preserve_defer_until_authorized`,
and acceptance condition
`source_evidence_validated_and_exact_revision_authority_present`.

Preserve third request `SYNTH-CANDIDATE-REVISE-REQUEST-003@r2`, review
authority `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-003@r2`, and
refusal `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-003@r2` at
`2026-08-27T22:45:12Z` with record
`renewed_revise_request_not_admitted_source_backed_evidence_present_but_revision_authority_absent`
and content ID
`synthetic-content:candidate-revise-request-review-refusal-decision-003-r2`.
All three review authorities are consumed; all requests remain non-operative.

At `2026-08-27T22:50:12Z`, candidate-disposition revision authority
`SYNTH-CANDIDATE-DISPOSITION-REVISION-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-candidate-disposition-revision-decision-authority@r2`. It
authorizes only `synthetic-candidate-disposition-revision-decider` once to
change the synthetic disposition from `deferred` to `revision_required` after
verifying the entire lineage, source-backed evidence and checksum, named
deficiency/correction/acceptance package, unchanged candidate and score,
current defer, all consumed prior authorities, and unconsumed revision
authority. It authorizes no candidate-content revision, P8, proving execution,
transfer, graduation, deployment, publication, contact, real state change, or
external action.

At `2026-08-27T22:52:12Z`, every check matched. Decision
`SYNTH-CANDIDATE-DISPOSITION-REVISION-DECISION-001@r2` is signed by that
decider and records `revise_synthetic_candidate_disposition_only` with
deficiency `unsupported_concern_requires_source_backed_revision_basis`,
correction gate `verify_source_revision_and_preserve_defer_until_authorized`,
and acceptance condition
`source_evidence_validated_and_exact_revision_authority_present`. Content ID
`synthetic-content:candidate-disposition-revision-decision-001-r2` has a valid
checksum; the one-use authority is consumed. Synthetic disposition becomes
`revision_required`. Candidate content, score result `bounded_pass`, negative
evidence, and all real state remain unchanged.

All actors and evidence are synthetic. Correction owner is
`synthetic-proving-plan-owner`. Stop on any named revision, evidence,
authority, decision, checksum, deficiency, gate, or acceptance-condition
change. Failure modes include evidence treated as authority, authority reused,
the disposition decision treated as candidate revision or P8, prior negative
evidence erased, or synthetic state applied to `CMD-0001`. Failed disposition
recovery retracts only the revision decision, restores synthetic disposition
`deferred`, preserves the source-backed evidence and all three requests and
refusals, and changes no candidate content. Exact next wake is an authorized
synthetic candidate-revision plan under the frozen disposition decision, or
any named revision.

## Work now

Draft
`dispositions/CANDIDATE-DISPOSITION-SYNTHETIC-REVISE-AUTHORIZED-AFTER-SOURCE-BACKED-EVIDENCE-NO-P8-AUTHORITY-BOUNDARY-FIXTURE.md`
with exactly this frontmatter:

---
artifact_type: synthetic_candidate_disposition_revise_authorized_after_source_backed_evidence_no_p8_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

Use title `# Synthetic Candidate-Disposition Revise-Authorized After-Source-Backed-Evidence No-P8-Authority Boundary Fixture`
and exactly these `##` sections: `Use Boundary`, `Decision Header`, `Frozen
Candidate And Evidence`, `Consumed Authority Lineage`, `Source-Backed Evidence
And Prior Refusals`, `Revision Authority And Decision Basis`, `Negative
Evidence And Reasons`, `Owner Fit, Transfer, And Graduation Boundary`,
`Affected Parties And Legitimacy`, `Stops, Correction, Recovery, And Reopen`,
`Executed Synthetic Revision Disposition`, and `Frontier Verification`.
Preserve every identifier, timestamp, signer, decider, scope, pointer, content
ID, checksum, negative record, stop, failure mode, correction, recovery,
non-effect, and exact wake. Return only the finished artifact. First line must
be `---`; do not use a code fence; copy the literal frontmatter exactly; and
use `##` for every named body section.
