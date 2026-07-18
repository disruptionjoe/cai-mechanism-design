---
candidate_id: CMD-0001
status: admitted_revision_required
lane: "1"
source_inquiry: cai-systemic-failure/SFQ-0001
created: 2026-07-18
external_action: none
---

# CMD-0001 - Source-Preserving Assumption-Drift Register

## Candidate

A source-preserving assumption-drift register is a review mechanism that records
load-bearing assumptions, their source evidence, affected systems, owner, change
events, validation method, counterevidence, and correction route. It is meant to
make contradiction visible when incremental design changes, delegated review, or
human-response assumptions alter the safety or legitimacy case.

This candidate is admitted only for synthetic, reversible design and testing. It
is not an aviation remedy, a compliance system, a deployment proposal, or an
obligation for any other owner.

## Source Inquiry

The source inquiry is `SFQ-0001` from CAI Systemic Failure, derived from the
bounded public-source record `SF-0001`. The motivating pattern is not "one more
checklist"; it is that changed function authority, delegated approval, and
operator-response assumptions can become separated across review artifacts.

## Theory Of Change

If a critical assumption has a named owner, source, validation burden,
affected-party impact, and correction route, then a later change cannot silently
depend on the old assumption. The register does not decide the technical answer.
It should route the contradiction to the correct accountable review before the
system treats the old assumption as still valid.

## Alternatives

- No action: preserve the failure record and do not design a mechanism.
- Ordinary checklist: cheaper, but may not preserve source revisions or owner
  fit.
- Post-incident review only: useful after harm, but does not test whether the
  contradiction could have been made visible earlier.
- Domain-specific safety-case tooling: likely better for aviation, medical, or
  other regulated settings, but outside this repo's authority.

## Owner Fit

CAI Mechanism Design owns this as a generic, otherwise-unowned candidate pattern
for synthetic evaluation. Existing domain owners defeat adoption for any real
setting. Aviation certification, rulemaking, training, and engineering control
remain with aviation authorities and domain experts.

## Affected Parties And Legitimacy Risks

Affected parties in real deployments would include system users, operators,
reviewers, producers, regulators, and people exposed to downstream harms.
Synthetic testing must represent those standing positions without pretending to
consent for them.

Risks:

- The register becomes compliance theater.
- Producers game the fields while preserving source-looking paperwork.
- A central reviewer gains unjustified authority over domain decisions.
- Sensitive or regulated evidence is pulled into an unsafe surface.
- The mechanism delays urgent stops by demanding more process.

## Evidence Route

Use only synthetic fixtures derived from `SF-0001`'s public pattern. The first
test asks whether the register detects three drifts:

1. changed function authority or input path;
2. reliance on unvalidated human response under interacting alerts; and
3. delegated review with insufficient visibility into the changed function.

Permitted conclusion: the candidate exposes and routes assumption drift in the
synthetic fixture, or it fails to do so.

## Stops

Stop or kill the candidate if it requires confidential data, real human
subjects, institutional deployment, external contact, regulatory authority, or
domain-specific judgment this repo cannot own. Also stop if the synthetic
fixture can pass by filling paperwork while leaving the contradiction invisible.

## Intended Disposition

After synthetic testing, choose kill, revise, defer, transfer, or propose
graduation. Graduation would require a destination owner, unresolved-risk
disclosure, and explicit acceptance; none exists now.

## First Synthetic Score

`proving/CMD-0001-P1-synthetic-score.md` scored the first synthetic fixture as
revision required. The candidate can expose changed-function, human-response,
and delegated-review contradictions only if typed drift events, validation
status, lowest-fitting owner routing, and correction routes are required fields.
Free-text completion remains a paperwork-theater absorber.
