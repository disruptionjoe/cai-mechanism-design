# Refuse synthetic revise request after defer reauthorization

## Boundary

Write one complete synthetic disposition fixture from only the embedded
evidence. Preserve the bounded pass, accepted return, invalid and retracted
first defer, recovery, separately reauthorized defer, all negative evidence,
and current synthetic state `deferred`. Add one request for `revise` and one
separately authorized review decision that refuses to admit it because there
is no materially new evidence or revision authority. A request is evidence,
not an instruction. Refusal is not a new candidate disposition, P8, proving
result, real candidate change, transfer, graduation, deployment, publication,
contact, or external action. External action is `none`.
Do not treat the request, review authority, or refusal as disposition authority.

## Frozen evidence

Use `ROADMAP.md`,
`proving/LEAST-CONSEQUENTIAL-PROVING-PLAN-TEMPLATE.md`,
`dispositions/CANDIDATE-DISPOSITION-DECISION-TEMPLATE.md`, and
`dispositions/CANDIDATE-DISPOSITION-SYNTHETIC-DEFER-REAUTHORIZED-AFTER-RECOVERY-NO-REVISION-AUTHORITY-BOUNDARY-FIXTURE.md`.
Freeze fixture
`SYNTH-CANDIDATE-REVISE-REQUEST-REFUSED-AFTER-DEFER-REAUTHORIZATION-001@r2`,
the named source, candidate, plan, score, return, acceptance, invalid first
defer, checksum revision, correction authority, recovery, reauthorization,
and reauthorized defer decision. Only `defer` remains supported; no real state
changes.

At `2026-08-27T22:15:12Z`, request
`SYNTH-CANDIDATE-REVISE-REQUEST-001@r2` is signed by
`synthetic-revision-requester` under
`synthetic-candidate-revision-request-creation-authority@r2`. Content ID
`synthetic-content:candidate-revise-request-001-r2` has a valid checksum.
It asks to change the unchanged candidate disposition to `revise` but supplies
no materially new candidate evidence, named deficiency, correction gate,
revision acceptance condition, candidate-disposition revision authority, or
authorized revision decision. It changes no state and grants no authority.

At `2026-08-27T22:20:12Z`, review authority
`SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-candidate-revise-request-review-decision-authority@r2`. It
authorizes only `synthetic-candidate-disposition-request-reviewer` once to
record whether this request is admissible after verifying the complete frozen
lineage, current deferred state and checksum, request and checksum, unchanged
supported disposition, absent new evidence, absent deficiency/correction/
acceptance package, absent revision authority and decision, and unconsumed
review authority. It authorizes no disposition, revision, P8, transfer,
graduation, deployment, publication, contact, or external action.

At `2026-08-27T22:25:12Z`, every check matched. Decision
`SYNTH-CANDIDATE-REVISE-REQUEST-REVIEW-DECISION-001@r2` is signed by
`synthetic-candidate-disposition-request-reviewer` and records
`revise_request_not_admitted_missing_new_evidence_and_revision_authority`.
Content ID
`synthetic-content:candidate-revise-request-review-refusal-decision-001-r2`
has a valid checksum; review authority is consumed. Synthetic state remains
`deferred`; the request remains non-operative evidence; no downstream record exists.

Literal authority lineage to copy in the decision-basis section:

- return acceptance — `SYNTH-RESULT-RETURN-ACCEPTANCE-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-result-return-acceptance-decision-authority@r2`; decision `SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2`; content `synthetic-content:second-regrant-defer-return-acceptance-decision-001-r2`; consumed
- first defer — `SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-decision-authority@r2`; decider `synthetic-candidate-disposition-decider`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-decision-001-r2`; consumed and decision retracted
- recovery — `SYNTH-CANDIDATE-DEFER-DISPOSITION-CORRECTION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-correction-decision-authority@r2`; decider `synthetic-proving-plan-owner`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-RECOVERY-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-recovery-decision-001-r2`; consumed
- defer reauthorization — `SYNTH-CANDIDATE-DEFER-REAUTHORIZATION-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-reauthorization-decision-authority@r2`; decider `synthetic-candidate-disposition-redecider`; decision `SYNTH-CANDIDATE-DEFER-REAUTHORIZED-DECISION-001@r2`; content `synthetic-content:candidate-defer-reauthorized-decision-001-r2`; consumed

All actors and evidence are synthetic. Stop on any named revision. Failure
modes include request treated as instruction, refusal treated as `defer` or
`revise`, absent authority invented, prior authority reused, retracted
evidence erased, or synthetic state applied to `CMD-0001`. Correction owner
is `synthetic-proving-plan-owner`. Failed review recovery retracts only the
request-review decision, leaves the request non-operative, restores unreviewed-
request state, and leaves synthetic disposition `deferred`. Exact next wake is materially new synthetic candidate evidence plus exact revision authority under frozen refused-request records, or any named revision.

## Work now

Draft `dispositions/CANDIDATE-DISPOSITION-SYNTHETIC-REVISE-REQUEST-REFUSED-AFTER-DEFER-REAUTHORIZATION-AUTHORITY-BOUNDARY-FIXTURE.md`
with exactly this frontmatter:

---
artifact_type: synthetic_candidate_disposition_revise_request_refused_after_defer_reauthorization_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

Use title `# Synthetic Candidate-Disposition Revise-Request-Refused-After-Defer-Reauthorization Authority Boundary Fixture`
and exactly these `##` sections: `Use Boundary`, `Decision Header`,
`Frozen Candidate And Evidence`, `Consumed Authority Lineage`, `Revise
Request`, `Decision Basis`, `Negative Evidence And Reasons`, `Owner Fit,
Transfer, And Graduation Boundary`, `Affected Parties And Legitimacy`,
`Stops, Correction, Recovery, And Reopen`, `Executed Synthetic Review
Decision`, and `Frontier Verification`. Preserve every identifier,
timestamp, signer, decider, scope, pointer, content ID, checksum, negative
record, stop, failure mode, correction, recovery, non-effect, and exact wake.
Return only the finished artifact. First line must be `---`; do not use a
code fence; copy the literal frontmatter exactly; and use `##` for every
named body section.
