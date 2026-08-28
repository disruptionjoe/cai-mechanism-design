# Graduations

Graduation is a proposal, not self-authorization. It requires destination-owner
acceptance, source and evidence provenance, unresolved-risk disclosure,
maintenance and correction ownership, authority boundaries, and a scoped
transfer plan. No destination acceptance means no graduation.

## Process artifacts

- `GRADUATION-PROPOSAL-TEMPLATE.md` prepares one evidence-bound graduation
  proposal with destination-owner fit and acceptance, affected-party,
  unresolved-risk, correction, revocation, and explicit non-effect controls;
  completing it does not create acceptance, graduation, transfer, contact,
  deployment, publication, or external action.
- `GRADUATION-TRANSFER-PLAN-TEMPLATE.md` prepares one accepted-scope and
  custody-bound transfer sequence with reversible gates, affected-party, risk,
  correction, recovery, revocation, and explicit non-effect controls; plan
  preparation cannot create acceptance, graduation, transfer, contact,
  operation, deployment, publication, or external action.
- `GRADUATION-TRANSFER-PLAN-BOUNDARY-FIXTURE.md` applies that template to a
  frozen synthetic pending-acceptance case and preserves empty accepted scope,
  source custody, missing authority, retained risk, and a `defer` state without
  creating contact, transfer, or graduation.
- `GRADUATION-PROPOSAL-BOUNDARY-FIXTURE.md` applies the proposal template to a
  frozen synthetic case with no alternative-map revision, proving return,
  destination-native fit, acceptance, or transfer authority and preserves
  source custody, correction, retained risk, and `defer` without creating
  contact, graduation, or transfer.
- `GRADUATION-PROPOSAL-TRANSFERRED-CANDIDATE-ACCEPTED-NO-GRADUATION-EXECUTION-AUTHORITY-BOUNDARY-FIXTURE.md`
  preserves the full synthetic transfer lineage, concrete unresolved-risk
  custody, one graduation proposal, and destination-owner acceptance while
  holding process state at `graduation_proposal_accepted_not_graduated`
  without graduation execution, deployment, performance, publication,
  contact, real-owner effect, or external action.
- `GRADUATION-EXECUTION-AUTHORIZED-AFTER-ACCEPTED-PROPOSAL-NO-DEPLOYMENT-AUTHORITY-BOUNDARY-FIXTURE.md`
  preserves that full transfer and proposal-acceptance lineage, then consumes
  one exact graduation authority to reach `graduated_not_deployed` while
  withholding deployment, performance, publication, contact, real-owner
  effect, and external action.
- `GRADUATION-POST-EXECUTION-DEPLOYMENT-REQUEST-REFUSED-NO-DEPLOYMENT-AUTHORITY-BOUNDARY-FIXTURE.md`
  preserves the exact graduated-but-not-deployed lineage, records one
  non-operative deployment request, and consumes one request-review authority
  to refuse it because deployment authority is absent; process state remains
  `graduated_not_deployed` with no performance, publication, contact,
  real-owner effect, or external action.
- `GRADUATION-DEPLOYMENT-AUTHORIZED-NO-PERFORMANCE-AUTHORITY-BOUNDARY-FIXTURE.md`
  preserves that request and refusal history, then consumes one exact
  deployment authority to reach `deployed_not_performed` while withholding
  performance, publication, contact, real-owner effect, and external action.
- `GRADUATION-PERFORMANCE-AUTHORIZED-NO-PUBLICATION-AUTHORITY-BOUNDARY-FIXTURE.md`
  preserves the complete deployment lineage and consumes one exact synthetic
  performance authority to reach `performed_not_published` while withholding
  publication, contact, real-owner effect, and external action.
- `GRADUATION-PERFORMANCE-PUBLICATION-REQUEST-REFUSED-NO-PUBLICATION-AUTHORITY-BOUNDARY-FIXTURE.md`
  preserves that complete performance lineage, records one non-operative
  publication request, and consumes one request-review authority to refuse it
  because publication execution authority is absent; state remains
  `performed_not_published` with no posting, sending, contact, real-owner
  effect, or external action.
- `GRADUATION-PUBLICATION-EXECUTION-AUTHORIZED-NO-EXTERNAL-EFFECT-BOUNDARY-FIXTURE.md`
  preserves that complete request-and-refusal lineage, then consumes one exact
  synthetic publication execution authority to record an internal process
  transition without an endpoint, posting, sending, contact, public release,
  real-owner effect, or external action.
- `GRADUATION-PUBLICATION-WITHDRAWAL-AUTHORIZED-NO-EXTERNAL-EFFECT-BOUNDARY-FIXTURE.md`
  preserves that publication-process receipt and prior refusal, then consumes
  one exact synthetic withdrawal authority to record an internal withdrawal
  transition without deletion, actual unpublishing, contact, posting, sending,
  public release, real-owner effect, or external action.
