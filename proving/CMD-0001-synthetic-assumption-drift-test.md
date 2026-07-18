---
proving_id: CMD-0001-P1
candidate_id: CMD-0001
status: drafted_synthetic_plan
created: 2026-07-18
external_action: none
---

# CMD-0001-P1 - Synthetic Assumption-Drift Test

## Purpose

Test whether `CMD-0001` exposes and routes assumption drift in a synthetic case
without claiming to solve a real aviation, safety, or regulatory problem.

## Fixture

The synthetic fixture uses four public-pattern fields derived from `SF-0001`:

1. A derivative system introduces changed function authority or a changed input
   path.
2. The safety case assumes immediate or appropriate human corrective response.
3. The operating environment includes multiple alerts, workload, or ambiguous
   indications.
4. Approval is delegated or distributed so the changed function details can be
   missed by at least one accountable reviewer.

No real accident data, confidential certification file, personal data, or
external contact is used.

## Pass Condition

The mechanism passes this first synthetic test only if the register:

- links each assumption to a source and owner;
- flags the changed function or input path as a drift event;
- marks the human-response assumption as unvalidated under the changed alert
  environment;
- routes the contradiction to an accountable review owner; and
- preserves a correction route without declaring the technical outcome.

## Kill Conditions

Kill or revise the candidate if:

- the contradiction can remain hidden while every field is formally filled;
- the mechanism needs real authority, deployment, confidential data, or human
  subjects to produce evidence;
- it routes every case to a central reviewer instead of the lowest fitting
  owner;
- it cannot represent no-action, transfer, or urgent stop as legitimate
  outcomes; or
- it turns the source-backed failure record into a generic blame narrative.

## Permitted Output

The next run may create a synthetic fixture table and score it against these
conditions. It may not contact parties, publish externally, create accounts,
deploy tools, recruit participants, change another owner's work, or claim an
aviation remedy.
