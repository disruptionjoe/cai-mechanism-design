---
disposition_id: CMD-0001-P6-D1
candidate_id: CMD-0001
proving_id: CMD-0001-P6
status: defer_after_bounded_revision_coherence_pass
supersedes: CMD-0001-P5-D1
created: 2026-07-24
external_action: none
---

# CMD-0001-P6 Disposition - Defer

The frozen synthetic trace first exposed a source-revision laundering failure:
the pre-P6 rules allowed a current source pointer to inherit `valid` from an
older source revision without a typed change event. The candidate now records
the previous source revision and validation-basis revision, types source
revision change, and rejects unmatched validation as current.

Keep `CMD-0001` admitted and deferred after the repaired trace's bounded pass.
The result improves internal contradiction visibility but does not establish
effectiveness, adoption fit, destination acceptance, graduation, transfer,
deployment readiness, or a domain remedy.

Reopen only for materially new source evidence, an explicit destination-owner
synthetic review request, or stewardship evidence that changes owner fit or
the safer home. Do not add synthetic traces merely to extend the proving count.
