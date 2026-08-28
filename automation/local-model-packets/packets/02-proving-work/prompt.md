# Observe one synthetic P8 execution without scoring authority

## Boundary

Write one compact synthetic proving-process fixture from only the embedded
evidence. Preserve the full executed-but-unobserved P8 lineage. Add one exact
one-use observation authority, one authorized observation decision, and one
observation record. Change only synthetic process state from
`synthetic_p8_executed_unobserved_unscored` to
`synthetic_p8_executed_observed_unscored`. Observation is not scoring,
disposition, real P8, transfer, graduation, deployment, publication, or
external action. Do not modify `CMD-0001`. External action is `none`. Keep the
finished artifact under 2,800 words.

## Frozen evidence

Use `GOVERNANCE.md`, `proving/PROVING-EXECUTION-TRACE-TEMPLATE.md`, and
`proving/CANDIDATE-REVISION-SYNTHETIC-P8-EXECUTED-NO-OBSERVATION-AUTHORITY-BOUNDARY-FIXTURE.md`.
Preserve its validated candidate revision, `revision_required` disposition,
prior bounded score, negative evidence, non-operative P8 request and refusal,
frozen P8 plan, consumed execution authority, execution decision, trace,
receipt, correction, recovery, and non-effect boundaries.

Freeze execution receipt `SYNTH-P8-PROVING-EXECUTION-RECEIPT-001@r2`, receipt
content `synthetic-content:p8-proving-execution-receipt-001-r2`, execution
trace `SYNTH-P8-PROVING-EXECUTION-TRACE-001@r2`, and state
`synthetic_p8_executed_unobserved_unscored`.

At `2026-08-27T23:50:12Z`, observation authority
`SYNTH-P8-PROVING-OBSERVATION-AUTHORITY-001@r2` is signed by
`synthetic-result-owner` under
`synthetic-p8-proving-observation-decision-authority@r2`. It authorizes only
`synthetic-independent-p8-observer` once to inspect the exact execution trace
and receipt for the frozen revision-basis preservation test. It permits one
no-data-mutation observation record: candidate revision basis remains pinned,
negative evidence remains visible, disposition remains `revision_required`,
and no unauthorized state field changed. It authorizes no scoring,
disposition, real-candidate, transfer, graduation, deployment, publication, or
external action.

At `2026-08-27T23:52:12Z`, all lineage, authority, receipt, trace, checksum,
negative-evidence, disposition, and no-revocation checks match. Decision
`SYNTH-P8-PROVING-OBSERVATION-DECISION-001@r2`, signed by the authorized
observer, records `observe_synthetic_p8_trace_without_scoring`. Content
`synthetic-content:p8-proving-observation-decision-001-r2` has a valid
checksum. At `2026-08-27T23:55:12Z`, observation record
`SYNTH-P8-PROVING-OBSERVATION-001@r2`, content
`synthetic-content:p8-proving-observation-001-r2`, records only that the frozen
revision basis, negative evidence, and `revision_required` remained visible
and unchanged. Authority is consumed. State becomes
`synthetic_p8_executed_observed_unscored`; prepared return is
`synthetic_p8_observation_record_only`.

Correction owner is `synthetic-proving-plan-owner`. All actors and evidence
are synthetic. Stop on any named revision, evidence, plan, authority, request,
decision, trace, receipt, observation, content, checksum, falsifier,
disposition, or revocation change. Failure modes include execution treated as
observation authority, observation treated as scoring, observer mutation,
negative evidence erased, authority reuse, or synthetic state applied to
`CMD-0001`. Failed observation recovery retracts only the observation
decision and record, preserves every predecessor, restores
`synthetic_p8_executed_unobserved_unscored`, and changes no real candidate.
Exact next wake is exact scoring authority plus an authorized score under the
frozen observation record, or any named revision.

## Work now

Draft
`proving/CANDIDATE-REVISION-SYNTHETIC-P8-OBSERVED-NO-SCORING-AUTHORITY-BOUNDARY-FIXTURE.md`
with exactly this frontmatter:

---
artifact_type: synthetic_candidate_revision_p8_observed_no_scoring_authority_boundary_fixture
status: candidate_process_fixture
external_action: none
---

Use title `# Synthetic Candidate Revision P8 Observed No-Scoring-Authority Boundary Fixture`
and exactly these `##` sections: `Use Boundary`, `Frozen Execution And
Predecessor Custody`, `P8 Observation Authority`, `Authorized Observation
Decision And Record`, `Owner Fit, Affected Parties, And Legitimacy`, `Stops,
Correction, Recovery, And Reopen`, `Prepared Return And Exact Wake`, and
`Frontier Verification`. Preserve every identifier, timestamp, signer,
authority scope, pointer, content ID, checksum assertion, negative record,
falsifier, stop, failure mode, correction, recovery, non-effect, and exact
wake.

Return only the finished artifact. First line must be `---`; do not use a code
fence; copy the frontmatter exactly; use `##` for every named section; remain
under 2,800 words.
