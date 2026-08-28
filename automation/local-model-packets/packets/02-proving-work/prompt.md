# Execute one authorized synthetic candidate-content revision without P8 authority

## Boundary

Write one complete synthetic revision-execution proving fixture from only the
embedded evidence. Preserve the bounded pass, negative evidence, accepted
return, invalid defer and recovery, reauthorized defer, three revise refusals,
source-backed evidence, revise-disposition decision, and authorized revision
plan. Add one exact candidate-content revision execution authority, immutable
before/after content, one trace and receipt, and one independent validation.
Do not treat the plan, evidence, or synthetic authority as real execution authority.
This changes only synthetic process state to
`candidate_content_revised_validated_no_p8`; it does not execute a new proving
plan, create P8, change `CMD-0001`, transfer, graduate, deploy, publish,
contact, or perform external action. External action is `none`.

## Frozen evidence

Use `ROADMAP.md`, `proving/LEAST-CONSEQUENTIAL-PROVING-PLAN-TEMPLATE.md`,
`dispositions/CANDIDATE-DISPOSITION-DECISION-TEMPLATE.md`, and
`dispositions/CANDIDATE-DISPOSITION-SYNTHETIC-REVISION-PLAN-AUTHORIZED-NO-CONTENT-REVISION-OR-P8-AUTHORITY-BOUNDARY-FIXTURE.md`.
Freeze fixture `SYNTH-CANDIDATE-REVISION-PLAN-AFTER-AUTHORIZED-DISPOSITION-001@r2`;
plan `SYNTH-CANDIDATE-REVISION-PLAN-001@r2`; proving plan
`SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`; score
`SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`; source
`SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`; candidate
`SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`; return
`SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2`; negative evidence
`synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`;
and current synthetic disposition `revision_required`. Score remains
`bounded_pass`; all real state remains unchanged.

Preserve originals `synthetic-observation:comparison-equal-014-r2`,
`synthetic-observation:comparison-unequal-014a-r2`, and
`synthetic-observation:comparison-unequal-014b-r2`; replacements
`synthetic-observation:comparison-equal-014a-corrected-r2` and
`synthetic-observation:comparison-equal-014b-corrected-r2`; grants 006, 007,
and 008; three future-only revocations; three valid supersession records; and
four unauthorized records as distinct negative and authority lineage.

Preserve consumed authority lineage: return acceptance
`SYNTH-RESULT-RETURN-ACCEPTANCE-AUTHORITY-001@r2`; first defer
`SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2` and retracted decision;
recovery `SYNTH-CANDIDATE-DEFER-DISPOSITION-CORRECTION-AUTHORITY-001@r2`;
and defer reauthorization `SYNTH-CANDIDATE-DEFER-REAUTHORIZATION-001@r2`.

Preserve requests `SYNTH-CANDIDATE-REVISE-REQUEST-001@r2`,
`SYNTH-CANDIDATE-REVISE-REQUEST-002@r2`, and
`SYNTH-CANDIDATE-REVISE-REQUEST-003@r2`; concern
`SYNTH-CANDIDATE-REVISION-CONCERN-001@r2`; evidence
`SYNTH-CANDIDATE-REVISION-EVIDENCE-001@r2`; all three consumed review
authorities and refusal decisions; all content IDs and valid checksums. The
evidence pins source revision
`synthetic-source-revision:second-regrant-second-revocation-002-r3`, deficiency
`unsupported_concern_requires_source_backed_revision_basis`, correction gate
`verify_source_revision_and_preserve_defer_until_authorized`, and acceptance
condition `source_evidence_validated_and_exact_revision_authority_present`.

Preserve disposition revision authority
`SYNTH-CANDIDATE-DISPOSITION-REVISION-AUTHORITY-001@r2` and decision
`SYNTH-CANDIDATE-DISPOSITION-REVISION-DECISION-001@r2`, content
`synthetic-content:candidate-disposition-revision-decision-001-r2`, which
changes only disposition to `revision_required`. Preserve plan-preparation
authority `SYNTH-CANDIDATE-REVISION-PLAN-PREPARATION-AUTHORITY-001@r2`, signed
at `2026-08-27T23:00:12Z` by `synthetic-result-owner` under
`synthetic-candidate-revision-plan-preparation-authority@r2`; planner
`synthetic-candidate-revision-planner`; and plan
`SYNTH-CANDIDATE-REVISION-PLAN-001@r2` at `2026-08-27T23:02:12Z`, content
`synthetic-content:candidate-revision-plan-001-r2`, record
`prepare_source_backed_revision_basis_without_content_execution`. Planning
authority is consumed and checksums are valid.

At `2026-08-27T23:10:12Z`, candidate-content revision authority
`SYNTH-CANDIDATE-CONTENT-REVISION-EXECUTION-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-candidate-content-revision-execution-authority@r2`. It authorizes
only `synthetic-candidate-content-revision-executor` once to apply the exact
frozen plan after verifying complete lineage, source evidence and checksum,
current `revision_required` disposition, unchanged candidate and score, no
revocation, and unconsumed authority. It authorizes no proving execution, P8,
disposition change, real candidate change, transfer, graduation, deployment,
publication, contact, or external action.

Immutable before content is
`candidate_revision_basis: absent` at content ID
`synthetic-content:candidate-before-revision-basis-001-r2`. At
`2026-08-27T23:12:12Z`, the executor applies only the planned field:
`candidate_revision_basis` pins evidence
`SYNTH-CANDIDATE-REVISION-EVIDENCE-001@r2`, source revision
`synthetic-source-revision:second-regrant-second-revocation-002-r3`, deficiency
`unsupported_concern_requires_source_backed_revision_basis`, correction gate
`verify_source_revision_and_preserve_defer_until_authorized`, and acceptance
condition `source_evidence_validated_and_exact_revision_authority_present`.
Immutable after content is
`synthetic-content:candidate-after-revision-basis-001-r2`. Decision
`SYNTH-CANDIDATE-CONTENT-REVISION-DECISION-001@r2` records
`apply_exact_source_backed_revision_basis_only`. Trace
`SYNTH-CANDIDATE-CONTENT-REVISION-TRACE-001@r2` and receipt
`SYNTH-CANDIDATE-CONTENT-REVISION-RECEIPT-001@r2` at
`2026-08-27T23:15:12Z`, content
`synthetic-content:candidate-content-revision-receipt-001-r2`, preserve both
states and valid checksums. The one-use execution authority is consumed.

At `2026-08-27T23:18:12Z`, independent validation authority
`SYNTH-CANDIDATE-CONTENT-REVISION-VALIDATION-AUTHORITY-001@r2`, signed by
`synthetic-result-owner` under
`synthetic-candidate-content-revision-validation-authority@r2`, authorizes only
`synthetic-independent-revision-validator` once to compare the plan, before
and after content, trace, receipt, source evidence, named field, unchanged
remainder, and non-effects. Validation decision
`SYNTH-CANDIDATE-CONTENT-REVISION-VALIDATION-DECISION-001@r2`, content
`synthetic-content:candidate-content-revision-validation-decision-001-r2`,
records `exact_planned_revision_validated_no_p8_authority`. Its checksum is
valid and validation authority is consumed. Process state becomes
`candidate_content_revised_validated_no_p8`; disposition remains
`revision_required`; score remains `bounded_pass`; prepared return is
`synthetic_candidate_content_revision_record_only`.

All actors and evidence are synthetic. Correction owner is
`synthetic-proving-plan-owner`. Stop on any named revision, evidence,
authority, decision, content, trace, receipt, checksum, deficiency, gate, or
acceptance-condition change. Failure modes include evidence treated as
authority, plan treated as execution, execution treated as P8, unplanned
content drift, authority reused, negative evidence erased, or synthetic state
applied to `CMD-0001`. Failed revision recovery retracts only the revision
decision, trace, receipt, and validation; restores the immutable before
content and `revision_plan_prepared_not_executed`; preserves disposition,
plan, predecessors, and negative evidence; and changes no real candidate.
Exact next wake is exact P8 proving authority plus a new frozen proving plan,
or any named revision.

## Work now

Draft
`proving/CANDIDATE-REVISION-SYNTHETIC-EXECUTED-VALIDATED-NO-P8-AUTHORITY-BOUNDARY-FIXTURE.md`
with exactly this frontmatter:

---
artifact_type: synthetic_candidate_revision_executed_validated_no_p8_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

Use title `# Synthetic Candidate Revision Executed and Validated No-P8-Authority Boundary Fixture`
and exactly these `##` sections: `Use Boundary`, `Revision Header`, `Frozen
Candidate, Score, And Negative Evidence`, `Consumed Disposition And Planning
Lineage`, `Source Evidence And Revision Plan`, `Candidate-Content Revision
Authority`, `Immutable Revision Trace And Receipt`, `Independent Validation`,
`Owner Fit, Affected Parties, And Legitimacy`, `Stops, Correction, Recovery,
And Reopen`, `Prepared Return And Exact Wake`, and `Frontier Verification`.
Preserve every identifier, timestamp, signer, decider, authority scope,
pointer, content ID, checksum assertion, negative record, stop, failure mode,
correction, recovery, non-effect, and exact wake.
Return only the finished artifact. First line must be `---`; do not use a code fence; copy the literal
frontmatter exactly; and use `##` for every named body section.
