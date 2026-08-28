# Refuse revision after source-backed evidence without revision authority

## Boundary

Write one complete synthetic disposition fixture from only the embedded
evidence. Preserve the bounded pass, accepted return, invalid and retracted
first defer, recovery, separately reauthorized defer, both prior revise
requests and refusals, the unsupported concern, all negative evidence, and
current synthetic state `deferred`. Add one source-backed evidence record and
one separately authorized review decision that still refuses revision because
evidence is not execution authority and revision authority remains absent.
Evidence is not an instruction. Refusal is not a new candidate disposition,
P8, proving result, real candidate change, transfer, graduation, deployment,
publication, contact, or external action. External action is `none`. Do not
modify `CMD-0001` or create P8. The result remains `bounded_pass`; only
`defer` remains supported; synthetic state remains `deferred`.

## Frozen evidence

Use `ROADMAP.md`,
`proving/LEAST-CONSEQUENTIAL-PROVING-PLAN-TEMPLATE.md`,
`dispositions/CANDIDATE-DISPOSITION-DECISION-TEMPLATE.md`, and
`dispositions/CANDIDATE-DISPOSITION-SYNTHETIC-UNSUPPORTED-CONCERN-REVISE-REQUEST-REFUSED-NO-REVISION-AUTHORITY-BOUNDARY-FIXTURE.md`.
Freeze fixture
`SYNTH-CANDIDATE-SOURCE-BACKED-EVIDENCE-REVISE-REQUEST-REFUSED-001@r2`,
plan `SYNTH-PROVE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, score
`SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, source
`SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, candidate
`SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, immutable trace and
validation, return `SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2`,
return acceptance, invalid first defer, checksum revision, correction,
recovery, reauthorization, reauthorized defer, first request and refusal,
concern, second request and refusal. The result remains `bounded_pass`; only
`defer` remains supported; synthetic state remains `deferred`; no real
state changes.

Originals remain `synthetic-observation:comparison-equal-014-r2`,
`synthetic-observation:comparison-unequal-014a-r2`, and
`synthetic-observation:comparison-unequal-014b-r2`; replacements remain
`synthetic-observation:comparison-equal-014a-corrected-r2` and
`synthetic-observation:comparison-equal-014b-corrected-r2`. Grants 006, 007,
and 008, three future-only revocations, three valid supersession records, and
four unauthorized records remain distinct. Negative evidence remains at
`synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`.

Preserve this literal consumed authority lineage:

- return acceptance — `SYNTH-RESULT-RETURN-ACCEPTANCE-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-result-return-acceptance-decision-authority@r2`; decision `SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2`; content `synthetic-content:second-regrant-defer-return-acceptance-decision-001-r2`; consumed
- first defer — `SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-decision-authority@r2`; decider `synthetic-candidate-disposition-decider`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-decision-001-r2`; consumed and decision retracted
- recovery — `SYNTH-CANDIDATE-DEFER-DISPOSITION-CORRECTION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-correction-decision-authority@r2`; decider `synthetic-proving-plan-owner`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-RECOVERY-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-recovery-decision-001-r2`; consumed
- defer reauthorization — `SYNTH-CANDIDATE-DEFER-REAUTHORIZATION-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-reauthorization-decision-authority@r2`; decider `synthetic-candidate-disposition-redecider`; decision `SYNTH-CANDIDATE-DEFER-REAUTHORIZED-DECISION-001@r2`; content `synthetic-content:candidate-defer-reauthorized-decision-001-r2`; consumed

Preserve first request `SYNTH-CANDIDATE-REVISE-REQUEST-001@r2`, first refusal
`SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-001@r2`, concern
`SYNTH-CANDIDATE-REVISION-CONCERN-001@r2`, renewed request
`SYNTH-CANDIDATE-REVISE-REQUEST-002@r2`, and second refusal
`SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-002@r2`. The concern remains
a lead, not source-backed evidence. Both limited review authorities are
consumed. The second refusal record remains
`renewed_revise_request_not_admitted_concern_is_not_source_backed_evidence_and_revision_authority_absent`.

At `2026-08-27T22:40:12Z`, source-backed evidence
`SYNTH-CANDIDATE-REVISION-EVIDENCE-001@r2` is signed by
`synthetic-source-owner` under
`synthetic-candidate-revision-evidence-record-creation-authority@r2`.
Content ID `synthetic-content:candidate-revision-evidence-001-r2` has a valid
checksum. It names source revision
`synthetic-source-revision:second-regrant-second-revocation-002-r3`,
deficiency `unsupported_concern_requires_source_backed_revision_basis`,
correction gate `verify_source_revision_and_preserve_defer_until_authorized`,
and acceptance condition
`source_evidence_validated_and_exact_revision_authority_present`. It changes
no candidate or disposition and grants no revision authority or authorized
revision decision.

At `2026-08-27T22:42:12Z`, request
`SYNTH-CANDIDATE-REVISE-REQUEST-003@r2` is signed by
`synthetic-revision-requester` under
`synthetic-candidate-revision-request-creation-authority@r2`. Content ID
`synthetic-content:candidate-revise-request-003-r2` has a valid checksum. It
cites the source-backed evidence but supplies no candidate-disposition revision
authority and no authorized revision decision.

At `2026-08-27T22:44:12Z`, review authority
`SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-003@r2` is signed by
`synthetic-result-owner` under
`synthetic-candidate-revise-request-review-decision-authority@r2`. It
authorizes only `synthetic-candidate-disposition-request-reviewer` once to
verify the frozen lineage, both prior refusals, current evidence and checksum,
named deficiency/correction/acceptance package, third request and checksum,
current deferred state, unchanged supported disposition, absent revision
authority and decision, and unconsumed review authority. It authorizes no
disposition, revision, P8, transfer, graduation, deployment, publication,
contact, or external action.

At `2026-08-27T22:45:12Z`, every check matched. Decision
`SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-003@r2` is signed by
`synthetic-candidate-disposition-request-reviewer` and records
`renewed_revise_request_not_admitted_source_backed_evidence_present_but_revision_authority_absent`.
Content ID
`synthetic-content:candidate-revise-request-review-refusal-decision-003-r2`
has a valid checksum; review authority is consumed. Synthetic state remains
`deferred`; evidence and request remain non-operative; no downstream record
exists.

All actors and evidence are synthetic. Correction owner is
`synthetic-proving-plan-owner`. Stop on any named revision. Failure modes
include evidence treated as revision authority, request treated as instruction,
review authority treated as disposition authority, refusal treated as
`defer` or `revise`, prior authority reused, retracted evidence erased, or
synthetic state applied to `CMD-0001`. Failed review recovery retracts only
the third request-review decision, preserves the source-backed evidence and
third request as non-operative, restores evidence-present/unreviewed state, and
leaves synthetic disposition `deferred`. Exact next wake is exact
candidate-disposition revision authority plus an authorized revision decision
under frozen source-backed evidence-and-refusal records, or any named revision.

## Work now

Draft
`dispositions/CANDIDATE-DISPOSITION-SYNTHETIC-SOURCE-BACKED-EVIDENCE-REVISE-REQUEST-REFUSED-NO-REVISION-AUTHORITY-BOUNDARY-FIXTURE.md`
with exactly this frontmatter:

---
artifact_type: synthetic_candidate_disposition_source_backed_evidence_revise_request_refused_no_revision_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

Use title `# Synthetic Candidate-Disposition Source-Backed-Evidence Revise-Request-Refused No-Revision-Authority Boundary Fixture`
and exactly these `##` sections: `Use Boundary`, `Decision Header`,
`Frozen Candidate And Evidence`, `Consumed Authority Lineage`, `Source-Backed
Evidence And Renewed Revise Request`, `Decision Basis`, `Negative Evidence
And Reasons`, `Owner Fit, Transfer, And Graduation Boundary`, `Affected
Parties And Legitimacy`, `Stops, Correction, Recovery, And Reopen`, `Executed
Synthetic Review Decision`, and `Frontier Verification`. Preserve every
identifier, timestamp, signer, decider, scope, pointer, content ID, checksum,
negative record, stop, failure mode, correction, recovery, non-effect, and
exact wake. Return only the finished artifact.
First line must be `---`; do not use a code fence; copy the literal
frontmatter exactly; and use `##` for every named body section.
