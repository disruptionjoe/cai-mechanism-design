# Preserve a synthetic defer disposition after accepted return

## Boundary

Write one complete synthetic candidate-disposition process fixture from only
the embedded evidence. Preserve the validated three-grant score, accepted
return, bounded `defer` support, and all negative evidence. Add one separately
authorized disposition decision that executes `defer` only for the named
synthetic candidate. The decision does not modify `CMD-0001`, create
`CMD-0001-P8`, transfer, graduate, deploy, publish, contact, or perform external
action. It creates no effectiveness or destination-fit claim.

## Frozen evidence

Use `dispositions/CANDIDATE-DISPOSITION-DECISION-TEMPLATE.md`, `ROADMAP.md`, and
`proving/PROVING-RESULT-RETURN-OWNER-DEFER-ACCEPTANCE-NO-DISPOSITION-AUTHORITY-BOUNDARY-FIXTURE.md`.
Freeze decision `SYNTH-CANDIDATE-DEFER-DISPOSITION-001@r2`, candidate
`SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, source
`SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, source revision
`synthetic-source-revision:second-regrant-second-revocation-001-r2`, score
`SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`, return
`SYNTH-RETURN-SECOND-REGRANT-DEFER-ACCEPTANCE-001@r2`, and acceptance decision
`SYNTH-RESULT-RETURN-ACCEPTANCE-DECISION-001@r2`.

The package preserves originals
`synthetic-observation:comparison-equal-014-r2`,
`synthetic-observation:comparison-unequal-014a-r2`, and
`synthetic-observation:comparison-unequal-014b-r2`; valid replacements
`synthetic-observation:comparison-equal-014a-corrected-r2` and
`synthetic-observation:comparison-equal-014b-corrected-r2`; grants 006, 007,
and 008; three future-only revocations; three valid supersession records; and
four unauthorized records. Negative evidence remains at
`synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`.
Only the first valid record is needed for the surviving all-`equal` effect.
The validated result is `bounded_pass`; its only supported disposition is
`defer`.

Return content ID
`synthetic-content:second-regrant-defer-return-001-r2` and acceptance-decision
content ID
`synthetic-content:second-regrant-defer-return-acceptance-decision-001-r2`
have valid checksums. Acceptance state is
`return_accepted_disposition_not_decided`; the return-acceptance authority is
consumed. Acceptance is not disposition authority.

At `2026-08-27T21:35:12Z`, disposition authority
`SYNTH-CANDIDATE-DEFER-DISPOSITION-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-candidate-disposition-decision-authority@r2`. It authorizes only
`synthetic-candidate-disposition-decider` exactly once to decide whether to
execute `defer` for the unchanged synthetic candidate after verifying source,
candidate, plan, trace, score, validation, negative evidence, return,
acceptance, owner identity, checksum, stops, correction, recovery, and
unconsumed disposition authority. It authorizes no kill, revise, transfer,
graduation proposal, P8, deployment, publication, or external action.

At `2026-08-27T21:40:12Z`, every required check matched. Decision record
`SYNTH-CANDIDATE-DEFER-DISPOSITION-DECISION-001@r2` is signed by
`synthetic-candidate-disposition-decider` under the exact authority and records
`defer`. Decision content ID is
`synthetic-content:candidate-defer-disposition-decision-001-r2`; its checksum
is valid. The one-use disposition authority is consumed. Synthetic candidate
state becomes `deferred`; no real candidate state changes. No P8, transfer,
graduation proposal, deployment, publication, contact, or external action
exists.

All standing, data, actors, evidence, authority, and systems are synthetic.
Decision owner is `synthetic-result-owner`; correction owner is
`synthetic-proving-plan-owner`. Stop on any source, candidate, plan, trace,
validation, authority, grant, revocation, record, replacement, score, return,
acceptance, disposition, checksum, or risk revision. Failure modes include
return acceptance treated as disposition authority, `defer` support treated as
already executed, consumed authority reused, synthetic state applied to
`CMD-0001`, or downstream effect invented. Recovery preserves the full
lineage, score, return, acceptance, and negative evidence; retracts only the
defer decision if its authority or checksum fails; and restores
`return_accepted_disposition_not_decided`. Exact next wake is materially new
synthetic candidate evidence under frozen current records, or any named
revision.

## Work now

Draft
`dispositions/CANDIDATE-DISPOSITION-SYNTHETIC-DEFER-AFTER-ACCEPTED-RETURN-AUTHORITY-BOUNDARY-FIXTURE.md`
with exactly this frontmatter block:

---
artifact_type: synthetic_candidate_disposition_defer_after_accepted_return_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

Use title `# Synthetic Candidate-Disposition Defer-After-Accepted-Return Authority Boundary Fixture`
and exactly these `##` sections: `Use Boundary`, `Decision Header`, `Frozen
Candidate And Evidence`, `Available Dispositions`, `Decision Basis`, `Negative
Evidence And Reasons`, `Owner Fit, Transfer, And Graduation Boundary`,
`Affected Parties And Legitimacy`, `Stops, Correction, Recovery, And Reopen`,
`Executed Synthetic Decision`, and `Frontier Verification`. Preserve every
identifier, timestamp, signer, authority scope, pointer, content ID, checksum,
stop, failure mode, prohibited conclusion, correction, recovery, non-effect,
and exact wake. In `Stops, Correction, Recovery, And Reopen`, the sentence
`Exact next wake is materially new synthetic candidate evidence under frozen current records, or any named revision.` must appear verbatim. Return only the
finished artifact. The first line must be `---`; do not use a code fence. Copy
the literal frontmatter block exactly, including both delimiters and underscore
keys. Every named body section must use `##`.
