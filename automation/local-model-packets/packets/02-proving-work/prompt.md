# Preserve disposition recovery without inventing revision

## Boundary

Write one complete synthetic candidate-disposition recovery fixture from only
the embedded evidence. Preserve the validated three-grant score, accepted
return, executed synthetic `defer`, and all negative evidence. Add one
separately authorized correction decision that retracts only the synthetic
defer decision after a named checksum revision proves its checksum invalid,
then restores `return_accepted_disposition_not_decided`. Recovery is not a
`revise` disposition, new proving result, real candidate change, P8, transfer,
graduation, deployment, publication, contact, or external action. It creates
no effectiveness or destination-fit claim and does not modify `CMD-0001`.

## Frozen evidence

Use `dispositions/CANDIDATE-DISPOSITION-DECISION-TEMPLATE.md`, `ROADMAP.md`,
`proving/PROVING-RESULT-RETURN-OWNER-DEFER-ACCEPTANCE-NO-DISPOSITION-AUTHORITY-BOUNDARY-FIXTURE.md`,
and
`dispositions/CANDIDATE-DISPOSITION-SYNTHETIC-DEFER-AFTER-ACCEPTED-RETURN-AUTHORITY-BOUNDARY-FIXTURE.md`.
Freeze recovery `SYNTH-CANDIDATE-DEFER-DISPOSITION-RECOVERY-001@r2`, candidate
`SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, source
`SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, source revision
`synthetic-source-revision:second-regrant-second-revocation-001-r2`, score
`SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, return
`SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2`, acceptance decision
`SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2`, disposition authority
`SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2`, and disposition decision
`SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2`.

The package preserves originals
`synthetic-observation:comparison-equal-014-r2`,
`synthetic-observation:comparison-unequal-014a-r2`, and
`synthetic-observation:comparison-unequal-014b-r2`; valid replacements
`synthetic-observation:comparison-equal-014a-corrected-r2` and
`synthetic-observation:comparison-equal-014b-corrected-r2`; grants 006, 007,
and 008; three future-only revocations; three valid supersession records; and
four unauthorized records. Negative evidence remains at
`synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`.
The validated result remains `bounded_pass`; its only supported disposition
remains `defer`. The accepted return and acceptance-decision content IDs keep
valid checksums. Acceptance authority remains consumed and distinct from
disposition authority.

At `2026-08-27T21:45:12Z`, checksum revision record
`SYNTH-CANDIDATE-DEFER-DISPOSITION-CHECKSUM-REVISION-001@r2` is signed by
`synthetic-checksum-evidence-owner` under
`synthetic-disposition-checksum-evidence-authority@r2`. Its content ID is
`synthetic-content:candidate-defer-disposition-checksum-revision-001-r2`; its
checksum is valid. It proves only that decision content ID
`synthetic-content:candidate-defer-disposition-decision-001-r2` no longer
matches the frozen disposition decision. It changes no source, candidate,
score, return, acceptance, supported disposition, or real state and grants no
correction authority.

At `2026-08-27T21:50:12Z`, correction authority
`SYNTH-CANDIDATE-DEFER-DISPOSITION-CORRECTION-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-candidate-disposition-correction-decision-authority@r2`. It
authorizes only `synthetic-proving-plan-owner` exactly once to verify the named
checksum revision, retract only the invalid synthetic defer decision, and
restore the prior accepted-return state. It authorizes no new disposition,
revision of the candidate or score, P8, transfer, graduation, deployment,
publication, contact, or external action.

At `2026-08-27T21:55:12Z`, every required check matched. Recovery decision
`SYNTH-CANDIDATE-DEFER-DISPOSITION-RECOVERY-DECISION-001@r2` is signed by
`synthetic-proving-plan-owner` under the exact correction authority and records
`retract_defer_restore_return_accepted_disposition_not_decided`. Decision
content ID is
`synthetic-content:candidate-defer-disposition-recovery-decision-001-r2`; its
checksum is valid. The one-use correction authority is consumed. The invalid
defer decision remains preserved as retracted negative evidence; its consumed
disposition authority is not restored. Synthetic state becomes
`return_accepted_disposition_not_decided`; no real candidate state changes.

All standing, data, actors, evidence, authority, and systems are synthetic.
Decision owner is `synthetic-result-owner`; correction owner is
`synthetic-proving-plan-owner`. Stop on any source, candidate, plan, trace,
validation, authority, grant, revocation, record, replacement, score, return,
acceptance, disposition, checksum-revision, recovery, checksum, or risk
revision. Failure modes include checksum evidence treated as correction
authority, recovery treated as `revise`, consumed authority restored, retracted
evidence erased, synthetic state applied to `CMD-0001`, or downstream effect
invented. Recovery from a failed correction decision preserves all prior
records, retracts only the recovery decision, and restores synthetic state
`deferred`. Exact next wake is one separately authorized synthetic candidate-disposition decision under frozen recovered records, or any named revision.

## Work now

Draft
`dispositions/CANDIDATE-DISPOSITION-SYNTHETIC-DEFER-RECOVERY-NO-REVISION-AUTHORITY-BOUNDARY-FIXTURE.md`
with exactly this frontmatter block:

---
artifact_type: synthetic_candidate_disposition_defer_recovery_no_revision_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

Use title `# Synthetic Candidate-Disposition Defer-Recovery No-Revision-Authority Boundary Fixture`
and exactly these `##` sections: `Use Boundary`, `Recovery Header`, `Frozen
Candidate And Evidence`, `Checksum Revision Evidence`, `Correction Authority`,
`Recovery Decision Basis`, `Negative Evidence And Reasons`, `Owner Fit,
Transfer, And Graduation Boundary`, `Affected Parties And Legitimacy`, `Stops,
Correction, Recovery, And Reopen`, `Executed Synthetic Recovery`, and
`Frontier Verification`. Preserve every identifier, timestamp, signer,
authority scope, pointer, content ID, checksum, stop, failure mode, prohibited
conclusion, correction, recovery, retracted evidence, non-effect, and exact
wake. In `Stops, Correction, Recovery, And Reopen`, the sentence
`Exact next wake is one separately authorized synthetic candidate-disposition decision under frozen recovered records, or any named revision.` must appear
verbatim. Return only the finished artifact. The first line must be `---`; do
not use a code fence. Copy the literal frontmatter block exactly, including
both delimiters and underscore keys. Every named body section must use `##`.
