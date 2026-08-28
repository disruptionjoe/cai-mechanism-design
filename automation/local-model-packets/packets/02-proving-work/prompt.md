# Refuse one synthetic P8 proving request without P8 execution authority

## Boundary

Write one complete synthetic proving-process fixture from only the embedded
evidence. Preserve the bounded pass, negative evidence, accepted return,
disposition and recovery lineage, three revise refusals, source-backed
evidence, authorized revision plan, exact candidate-content revision,
immutable before and after content, trace, receipt, and independent validation.
Add one non-operative synthetic P8 proving request, one exact one-use authority
to review that request, and one authorized refusal because P8 proving execution
authority is absent. The refusal changes no process state and creates no P8,
new proving plan, execution, observation, score, disposition change, transfer,
graduation, deployment, real candidate effect, or external action. Do not
modify `CMD-0001`. External action is `none`.

## Frozen evidence

Use `ROADMAP.md`, `proving/LEAST-CONSEQUENTIAL-PROVING-PLAN-TEMPLATE.md`,
`proving/PROVING-EXECUTION-REQUEST-TEMPLATE.md`,
`proving/PROVING-AUTHORIZATION-DECISION-TEMPLATE.md`, and
`proving/CANDIDATE-REVISION-SYNTHETIC-EXECUTED-VALIDATED-NO-P8-AUTHORITY-BOUNDARY-FIXTURE.md`.

Copy this core block unchanged into the section that consumes it:

| Key | Supplied value |
| --- | --- |
| `fixture` | `SYNTH-CANDIDATE-REVISION-PLAN-AFTER-AUTHORIZED-DISPOSITION-001@r2` |
| `revision_plan` | `SYNTH-CANDIDATE-REVISION-PLAN-001@r2` |
| `proving_plan` | `SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `score` | `SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `source` | `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `candidate` | `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `return` | `SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2` |
| `negative_evidence` | `synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2` |
| `synthetic_disposition` | `revision_required` |
| `score_result` | `bounded_pass` |
| `process_state` | `candidate_content_revised_validated_no_p8` |
| `prepared_return` | `synthetic_candidate_content_revision_record_only` |

Preserve original observations
`synthetic-observation:comparison-equal-014-r2`,
`synthetic-observation:comparison-unequal-014a-r2`, and
`synthetic-observation:comparison-unequal-014b-r2`; corrected replacements
`synthetic-observation:comparison-equal-014a-corrected-r2` and
`synthetic-observation:comparison-equal-014b-corrected-r2`; grants 006, 007,
and 008; three future-only revocations; three valid supersession records; and
four unauthorized records as distinct negative and authority lineage.

Copy these disposition rows unchanged in the section that consumes them:

| Step | Authority; signer; scope; decider | Decision; content; state |
| --- | --- | --- |
| return acceptance | `SYNTH-RESULT-RETURN-ACCEPTANCE-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-result-return-acceptance-decision-authority@r2` | `SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2`; `synthetic-content:second-regrant-defer-return-acceptance-decision-001-r2`; consumed |
| first defer | `SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-candidate-disposition-decision-authority@r2`; `synthetic-candidate-disposition-decider` | `SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2`; `synthetic-content:candidate-defer-disposition-decision-001-r2`; consumed and retracted |
| recovery | `SYNTH-CANDIDATE-DEFER-DISPOSITION-CORRECTION-AUTHORITY-001@r2`; `synthetic-result-owner`; `synthetic-candidate-disposition-correction-decision-authority@r2`; `synthetic-proving-plan-owner` | `SYNTH-CANDIDATE-DEFER-DISPOSITION-RECOVERY-DECISION-001@r2`; `synthetic-content:candidate-defer-disposition-recovery-decision-001-r2`; consumed |
| defer reauthorization | `SYNTH-CANDIDATE-DEFER-REAUTHORIZATION-001@r2`; `synthetic-result-owner`; `synthetic-candidate-disposition-reauthorization-decision-authority@r2`; `synthetic-candidate-disposition-redecider` | `SYNTH-CANDIDATE-DEFER-REAUTHORIZED-DECISION-001@r2`; `synthetic-content:candidate-defer-reauthorized-decision-001-r2`; consumed |

Copy these request and evidence rows unchanged in the same consuming section:

| Record | Exact custody | Result |
| --- | --- | --- |
| request 1 | `SYNTH-CANDIDATE-REVISE-REQUEST-001@r2`; `2026-08-27T22:15:12Z`; `synthetic-revision-requester`; `synthetic-candidate-revision-request-creation-authority@r2`; `synthetic-content:candidate-revise-request-001-r2`; review `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-001@r2`; decision `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-001@r2` at `2026-08-27T22:25:12Z` | `revise_request_not_admitted_missing_new_evidence_and_revision_authority` |
| concern and request 2 | `SYNTH-CANDIDATE-REVISION-CONCERN-001@r2`; `2026-08-27T22:30:12Z`; `synthetic-concern-reporter`; `synthetic-candidate-concern-record-creation-authority@r2`; `synthetic-content:candidate-revision-concern-001-r2`; request `SYNTH-CANDIDATE-REVISE-REQUEST-002@r2`; `2026-08-27T22:32:12Z`; `synthetic-content:candidate-revise-request-002-r2`; review `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-002@r2`; decision `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-002@r2` at `2026-08-27T22:35:12Z` | `renewed_revise_request_not_admitted_concern_is_not_source_backed_evidence_and_revision_authority_absent` |
| source evidence | `SYNTH-CANDIDATE-REVISION-EVIDENCE-001@r2`; `2026-08-27T22:40:12Z`; `synthetic-source-owner`; `synthetic-candidate-revision-evidence-record-creation-authority@r2`; `synthetic-content:candidate-revision-evidence-001-r2` | source revision `synthetic-source-revision:second-regrant-second-revocation-002-r3`; deficiency `unsupported_concern_requires_source_backed_revision_basis`; gate `verify_source_revision_and_preserve_defer_until_authorized`; acceptance `source_evidence_validated_and_exact_revision_authority_present` |
| request 3 | `SYNTH-CANDIDATE-REVISE-REQUEST-003@r2`; `2026-08-27T22:42:12Z`; `synthetic-revision-requester`; `synthetic-content:candidate-revise-request-003-r2`; review `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-003@r2`; `2026-08-27T22:44:12Z`; `synthetic-result-owner`; `synthetic-candidate-revise-request-review-decision-authority@r2`; decision `SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-003@r2`; `2026-08-27T22:45:12Z`; `synthetic-content:candidate-revise-request-review-refusal-decision-003-r2` | `renewed_revise_request_not_admitted_source_backed_evidence_present_but_revision_authority_absent` |

Preserve disposition authority
`SYNTH-CANDIDATE-DISPOSITION-REVISION-AUTHORITY-001@r2` and decision
`SYNTH-CANDIDATE-DISPOSITION-REVISION-DECISION-001@r2`, content
`synthetic-content:candidate-disposition-revision-decision-001-r2`, which
changes only disposition to `revision_required`. Preserve plan-preparation
authority `SYNTH-CANDIDATE-REVISION-PLAN-PREPARATION-AUTHORITY-001@r2`, signed
at `2026-08-27T23:00:12Z` by `synthetic-result-owner` under
`synthetic-candidate-revision-plan-preparation-authority@r2`; planner
`synthetic-candidate-revision-planner`; and plan at `2026-08-27T23:02:12Z`,
content `synthetic-content:candidate-revision-plan-001-r2`, record
`prepare_source_backed_revision_basis_without_content_execution`.

Preserve candidate-content revision authority
`SYNTH-CANDIDATE-CONTENT-REVISION-EXECUTION-AUTHORITY-001@r2`, signed at
`2026-08-27T23:10:12Z` by `synthetic-result-owner` under
`synthetic-candidate-content-revision-execution-authority@r2`, authorizing only
`synthetic-candidate-content-revision-executor` once. Preserve immutable before
content `candidate_revision_basis: absent` at
`synthetic-content:candidate-before-revision-basis-001-r2`; exact field-only
revision at `2026-08-27T23:12:12Z`; immutable after content
`synthetic-content:candidate-after-revision-basis-001-r2`; decision
`SYNTH-CANDIDATE-CONTENT-REVISION-DECISION-001@r2` with
`apply_exact_source_backed_revision_basis_only`; trace
`SYNTH-CANDIDATE-CONTENT-REVISION-TRACE-001@r2`; and receipt
`SYNTH-CANDIDATE-CONTENT-REVISION-RECEIPT-001@r2` at
`2026-08-27T23:15:12Z`, content
`synthetic-content:candidate-content-revision-receipt-001-r2`.

Preserve independent validation authority
`SYNTH-CANDIDATE-CONTENT-REVISION-VALIDATION-AUTHORITY-001@r2`, signed at
`2026-08-27T23:18:12Z` by `synthetic-result-owner` under
`synthetic-candidate-content-revision-validation-authority@r2`, authorizing only
`synthetic-independent-revision-validator` once; and decision
`SYNTH-CANDIDATE-CONTENT-REVISION-VALIDATION-DECISION-001@r2`, content
`synthetic-content:candidate-content-revision-validation-decision-001-r2`,
recording `exact_planned_revision_validated_no_p8_authority`. All prior
authorities are consumed and all checksums valid.

At `2026-08-27T23:25:12Z`, request `SYNTH-P8-PROVING-REQUEST-001@r2` is signed
by `synthetic-proving-requester` under
`synthetic-p8-proving-request-record-creation-authority@r2`. Content
`synthetic-content:p8-proving-request-001-r2` has a valid checksum. It pins the
exact validated revision receipt, proposes only a new frozen synthetic proving
plan and later P8 execution decision, and grants no review, P8 execution,
observation, scoring, disposition, real-candidate, or external-action authority.

At `2026-08-27T23:27:12Z`, request-review authority
`SYNTH-P8-PROVING-REQUEST-REVIEW-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-p8-proving-request-review-decision-authority@r2`. It authorizes only
`synthetic-p8-proving-request-reviewer` once to admit or refuse the exact
request after verifying lineage, revision receipt, validation, negative
evidence, current disposition, no revocation, unconsumed review authority, a
new frozen proving plan, and separate P8 proving execution authority. It
authorizes no P8 execution or downstream effect.

At `2026-08-27T23:30:12Z`, all lineage checks match but neither a new frozen
proving plan nor P8 proving execution authority exists. Decision
`SYNTH-P8-PROVING-REQUEST-REVIEW-DECISION-001@r2` is signed by that reviewer and
records `p8_proving_request_refused_plan_and_execution_authority_absent`.
Content `synthetic-content:p8-proving-request-review-refusal-decision-001-r2`
has a valid checksum. Review authority is consumed; process state remains
`candidate_content_revised_validated_no_p8`; disposition remains
`revision_required`; score remains `bounded_pass`; prepared return is
`synthetic_p8_proving_request_refusal_record_only`.

All actors and evidence are synthetic. Correction owner is
`synthetic-proving-plan-owner`. Stop on any named revision, evidence, plan,
authority, request, decision, content, trace, receipt, validation, checksum,
deficiency, gate, or acceptance-condition change. Failure modes include a
request treated as P8 authority, revised content treated as a new proving
plan, review treated as execution, negative evidence erased, authority reused,
or synthetic state applied to `CMD-0001`. Failed request-review recovery
retracts only the review decision; preserves the non-operative request,
validated revision, disposition, plan, predecessors, and negative evidence;
restores the pre-review `candidate_content_revised_validated_no_p8` state; and
changes no real candidate. Exact next wake is exact P8 proving execution
authority plus a new frozen proving plan, or any named revision.

## Work now

Draft
`proving/CANDIDATE-REVISION-SYNTHETIC-P8-REQUEST-REFUSED-NO-EXECUTION-AUTHORITY-BOUNDARY-FIXTURE.md`
with exactly this frontmatter:

---
artifact_type: synthetic_candidate_revision_p8_request_refused_no_execution_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

Use title `# Synthetic Candidate Revision P8 Request Refused No-Execution-Authority Boundary Fixture`
and exactly these `##` sections: `Use Boundary`, `Request Header`, `Frozen
Candidate, Score, Revision, And Negative Evidence`, `Exact Disposition,
Request, And Revision Custody`, `Nonoperative P8 Proving Request`, `P8 Request
Review Authority And Refusal`, `Owner Fit, Affected Parties, And Legitimacy`,
`Stops, Correction, Recovery, And Reopen`, `Prepared Return And Exact Wake`,
and `Frontier Verification`. Copy every supplied keyed-row value unchanged
into the named consuming section. Preserve every identifier, timestamp,
signer, decider, authority scope, pointer, content ID, checksum assertion,
negative record, stop, failure mode, correction, recovery, non-effect, and
exact wake.

Return only the finished artifact. First line must be `---`; do not use a code
fence; copy the literal frontmatter exactly; and use `##` for every named body
section.
