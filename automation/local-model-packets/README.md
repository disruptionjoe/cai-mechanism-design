# Mechanism Design local-model packets

Status: `operational_pilot`

This directory is the target-owned interface for two rolling local-model work
slots. It reuses the shared Mac packet executor and the CapacityOS Repository
Operating Cycle. It is not a queue, a second workflow system, or owner truth.

The stable slot paths are:

- `packets/01-candidate-work/prompt.md`
- `packets/02-proving-work/prompt.md`

Both slots are live. The Mac launches candidate work at minute 00 and proving
work at minute 30. The local model writes immutable candidate output outside
this repository; the hourly Frontier Repository Operating Cycle at minute 12
dispositions completed work, verifies any useful material through Prepared
Progress, and replenishes terminally handled slots. A shared four-hour review
compares actual Frontier leverage across this repository and System Failures;
it cannot edit either active prompt or gate integration.

Systemic Repository Stewardship prepares each complete replacement prompt
through normal Progress. A missing, empty, placeholder, self-selecting, or
`nothing to do` prompt is not a successful run and must not be scheduled.

Suitable local work includes alternative and mechanism comparisons, first
drafts from frozen evidence, synthetic fixture construction, application of an
explicit proving test, and reconciliation or crosswalks. Frontier retains
source and inquiry admission, existing-owner fit, materially new source claims,
hard mechanism architecture, consequential proving, disposition, graduation,
destination-owner acceptance, external action, and final integration.

The initial packets create process-progress candidates: a reusable destination-
owner synthetic-review intake template and a reusable least-consequential
proving-plan template. They do not reopen deferred `CMD-0001`, increase its
proving count, or manufacture the new source, owner-fit, or destination-owner
evidence named in `ROADMAP.md`.
