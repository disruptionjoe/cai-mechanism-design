# Score one observed synthetic P8 without disposition authority

## Boundary

Write one compact synthetic proving-process fixture from only the embedded
evidence. Preserve the complete executed, observed, and unscored P8 lineage.
Add one exact one-use scoring authority, one authorized score decision, and one
score receipt. Change only synthetic process state from
`synthetic_p8_executed_observed_unscored` to
`synthetic_p8_executed_observed_scored_no_disposition`. The score is bounded
only to revision-basis preservation. It is not disposition, real P8, transfer,
graduation, deployment, publication, or external action. Do not modify
`CMD-0001`. External action is `none`. Keep the finished artifact under
2,800 words.

## Frozen evidence

Use `GOVERNANCE.md`, `proving/LEAST-CONSEQUENTIAL-PROVING-PLAN-TEMPLATE.md`,
`proving/PROVING-EXECUTION-TRACE-TEMPLATE.md`, and
`proving/CANDIDATE-REVISION-SYNTHETIC-P8-OBSERVED-NO-SCORING-AUTHORITY-BOUNDARY-FIXTURE.md`.
Preserve its complete validated-revision, request, refusal, plan, execution,
observation, correction, recovery, negative-evidence, and non-effect lineage.
Copy these current consuming-section values unchanged:

- source: `SYNTH-SOURCE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`;
  candidate: `SYNTH-CANDIDATE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`;
- prior score: `SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`;
  negative evidence:
  `synthetic://negative-evidence/SYNTH-SCORE-SECOND-REGRANT-SECOND-REVOCATION-001@r2`;
  disposition: `revision_required`;
- execution receipt: `SYNTH-P8-PROVING-EXECUTION-RECEIPT-001@r2`;
  content `synthetic-content:p8-proving-execution-receipt-001-r2`; trace
  `SYNTH-P8-PROVING-EXECUTION-TRACE-001@r2`;
- observation authority:
  `SYNTH-P8-PROVING-OBSERVATION-AUTHORITY-001@r2`; signed at
  `2026-08-27T23:50:12Z` by `synthetic-result-owner` under
  `synthetic-p8-proving-observation-decision-authority@r2` for one use by
  `synthetic-independent-p8-observer`;
- observation decision:
  `SYNTH-P8-PROVING-OBSERVATION-DECISION-001@r2`; content
  `synthetic-content:p8-proving-observation-decision-001-r2`; signed at
  `2026-08-27T23:52:12Z`; decision
  `observe_synthetic_p8_trace_without_scoring`;
- observation record: `SYNTH-P8-PROVING-OBSERVATION-001@r2`; content
  `synthetic-content:p8-proving-observation-001-r2`; recorded at
  `2026-08-27T23:55:12Z`;
- observation authority is consumed; current state is
  `synthetic_p8_executed_observed_unscored`; prior prepared return is
  `synthetic_p8_observation_record_only`.

Every named content checksum is valid. Frozen falsifiers remain any changed
candidate field, hidden negative record, altered disposition, invented
observation, or authority mismatch.

At `2026-08-28T00:00:12Z`, scoring authority
`SYNTH-P8-PROVING-SCORING-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-p8-proving-scoring-decision-authority@r2`. It authorizes only
`synthetic-independent-p8-scorer` once to score the exact frozen observation
record for the revision-basis preservation test after verifying complete
lineage, receipt, trace, observation, negative evidence, disposition,
falsifiers, no revocation, and unconsumed authority. It authorizes no candidate
disposition, real P8, transfer, graduation, deployment, publication, or
external action.

At `2026-08-28T00:02:12Z`, all checks match. Decision
`SYNTH-P8-PROVING-SCORE-DECISION-001@r2`, signed by the authorized scorer,
records `bounded_pass_revision_basis_preserved`. Content
`synthetic-content:p8-proving-score-decision-001-r2` has a valid checksum.
At `2026-08-28T00:05:12Z`, score receipt
`SYNTH-P8-PROVING-SCORE-RECEIPT-001@r2`, content
`synthetic-content:p8-proving-score-receipt-001-r2`, records only that the
frozen revision basis, negative evidence, and `revision_required` remained
visible and unchanged. Authority is consumed. State becomes
`synthetic_p8_executed_observed_scored_no_disposition`; disposition remains
`revision_required`; prepared return is
`synthetic_p8_score_record_only`.

Correction owner is `synthetic-proving-plan-owner`. All actors and evidence
are synthetic. Stop on any named revision, evidence, plan, authority, request,
decision, trace, receipt, observation, score, content, checksum, falsifier,
disposition, or revocation change. Failure modes include observation treated as
scoring authority, score treated as disposition, scorer mutation, negative
evidence erased, authority reuse, or synthetic state applied to `CMD-0001`.
Failed scoring recovery retracts only the score decision and receipt, preserves
every predecessor, restores `synthetic_p8_executed_observed_unscored`, and
changes no real candidate. Exact next wake is exact disposition-review
authority plus an authorized disposition decision under the frozen score
receipt, or any named revision.

## Work now

Draft
`proving/CANDIDATE-REVISION-SYNTHETIC-P8-SCORED-NO-DISPOSITION-AUTHORITY-BOUNDARY-FIXTURE.md`
with exactly this frontmatter:

---
artifact_type: synthetic_candidate_revision_p8_scored_no_disposition_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

Use title `# Synthetic Candidate Revision P8 Scored No-Disposition-Authority Boundary Fixture`
and exactly these `##` sections: `Use Boundary`, `Frozen Observation And
Predecessor Custody`, `P8 Scoring Authority`, `Authorized Score Decision
And Receipt`, `Owner Fit Affected Parties And Legitimacy`, `Stops
Correction Recovery And Reopen`, `Prepared Return And Exact Wake`, and
`Frontier Verification`. Preserve every identifier, timestamp, signer,
authority scope, pointer, content ID, checksum assertion, negative record,
falsifier, stop, failure mode, correction, recovery, non-effect, and exact
wake.

Return only the finished artifact. First line must be `---`; do not use a code
fence; copy the frontmatter exactly; use `##` for every named section; remain
under 2,800 words.
