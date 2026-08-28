# Reauthorize synthetic defer after recovery without inventing revision

## Boundary

Write one complete synthetic disposition fixture from only the embedded
evidence. Preserve the bounded pass, accepted return, invalid and retracted
first defer, recovery, all negative evidence, and restored
`return_accepted_disposition_not_decided`. Add one new, separately authorized
decision that again executes only `defer` for the unchanged synthetic
candidate. New authority does not restore or reuse either consumed prior
authority. It is not `revise`, P8, a new proving result, real candidate change,
transfer, graduation, deployment, publication, contact, or external action.

## Frozen evidence

Use `ROADMAP.md`, `dispositions/CANDIDATE-DISPOSITION-DECISION-TEMPLATE.md`, and
`dispositions/CANDIDATE-DISPOSITION-SYNTHETIC-DEFER-RECOVERY-NO-REVISION-AUTHORITY-BOUNDARY-FIXTURE.md`.
Freeze fixture `SYNTH-CANDIDATE-DEFER-REAUTHORIZED-AFTER-RECOVERY-001@r2`, the
named source, candidate, plan, score, return, acceptance, first disposition,
checksum revision, correction authority, and recovery decision. Only `defer`
remains supported; no real state changes.

Literal authority lineage to copy in the decision-basis section:

- return acceptance — `SYNTH-RESULT-RETURN-ACCEPTANCE-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-result-return-acceptance-decision-authority@r2`; decision `SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2`; content `synthetic-content:second-regrant-defer-return-acceptance-decision-001-r2`; consumed
- first defer — `SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-decision-authority@r2`; decider `synthetic-candidate-disposition-decider`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-decision-001-r2`; consumed and decision retracted
- recovery — `SYNTH-CANDIDATE-DEFER-DISPOSITION-CORRECTION-AUTHORITY-001@r2`; signer `synthetic-result-owner`; scope `synthetic-candidate-disposition-correction-decision-authority@r2`; decider `synthetic-proving-plan-owner`; decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-RECOVERY-DECISION-001@r2`; content `synthetic-content:candidate-defer-disposition-recovery-decision-001-r2`; consumed

At `2026-08-27T22:05:12Z`, new authority
`SYNTH-CANDIDATE-DEFER-REAUTHORIZATION-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-candidate-disposition-reauthorization-decision-authority@r2`. It
authorizes only `synthetic-candidate-disposition-redecider` once to execute
`defer` after verifying the complete frozen lineage, retracted invalid
decision, consumed old authorities, recovered state, unchanged supported
disposition, checksums, negative evidence, and unconsumed new authority. It
authorizes no other disposition or downstream effect.

At `2026-08-27T22:10:12Z`, every check matched. Decision
`SYNTH-CANDIDATE-DEFER-REAUTHORIZED-DECISION-001@r2` is signed by that decider
and records `defer_after_recovery`. Content ID
`synthetic-content:candidate-defer-reauthorized-decision-001-r2` has a valid
checksum; new authority is consumed. Synthetic state becomes `deferred` again.
The first invalid defer remains retracted negative evidence and neither old
authority is restored.

All actors and evidence are synthetic. Stop on any named revision. Failure
modes include new authority treated as restoration, retracted evidence erased,
re-defer treated as revise, or synthetic state applied to `CMD-0001`.
Correction owner is `synthetic-proving-plan-owner`. Recovery from a failed new
decision retracts only it and restores
`return_accepted_disposition_not_decided`. Exact next wake is materially new synthetic candidate evidence under frozen reauthorized records, or any named revision.

## Work now

Draft `dispositions/CANDIDATE-DISPOSITION-SYNTHETIC-DEFER-REAUTHORIZED-AFTER-RECOVERY-NO-REVISION-AUTHORITY-BOUNDARY-FIXTURE.md`
with exactly this frontmatter:

---
artifact_type: synthetic_candidate_disposition_defer_reauthorized_after_recovery_no_revision_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

Use title `# Synthetic Candidate-Disposition Defer-Reauthorized-After-Recovery No-Revision-Authority Boundary Fixture`
and exactly these `##` sections: `Use Boundary`, `Decision Header`, `Frozen
Candidate And Evidence`, `Consumed Authority Lineage`, `New Reauthorization`,
`Decision Basis`, `Negative Evidence And Reasons`, `Owner Fit, Transfer, And
Graduation Boundary`, `Affected Parties And Legitimacy`, `Stops, Correction,
Recovery, And Reopen`, `Executed Synthetic Decision`, and `Frontier
Verification`. Preserve every identifier, timestamp, signer, scope, pointer,
content ID, checksum, negative record, stop, failure mode, correction,
recovery, non-effect, and exact wake. Return only the finished artifact; first
line `---`, no code fence, literal frontmatter exactly, and every named body
section uses `##`.
