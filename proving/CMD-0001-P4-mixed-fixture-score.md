---
score_id: CMD-0001-P4-S1
candidate_id: CMD-0001
proving_id: CMD-0001-P4
status: scored_revision_required
created: 2026-07-20
source_fixture: cai-systemic-failure/topology/SF-MIX-0001-fukushima-tsunami-design-basis.md
source_owner_revision: 19c21cadd971d11075583a681e1390a012f1c85a
source_fixture_sha256: b6f34484f75981c6285e137be063db8b91b263eda6f83d4c6e05518d0d59b890
external_action: none
---

# CMD-0001-P4 Mixed-Fixture Score

## Boundary

This score uses only the source-owner mixed-case artifact and the P4
translation plan. It does not audit or restate the underlying official source
set, add a Fukushima or nuclear-safety claim, prescribe a remedy, route another
owner's work, or authorize consequential proving.

CAI Systemic Failure retains the fixture verdict: mixed pressure, not a sixth
positive record and not a clean negative absorber. This score asks only whether
the current typed register can preserve that status without prose doing hidden
work.

## Bounded Translation

| Register concern | Safe bounded reading | Score |
|---|---|---|
| Source and changed condition | Pin the source-owner artifact and its revision; record only its old-design-basis and later-reassessment pressure. | Pass |
| Validation and contradiction | Use provisional values such as `validation_status: unknown` and `contradiction_flag: possible`; do not assert a resolved technical contradiction. | Pass |
| Lowest-fitting route | Preserve operator, regulator, oversight, reassessment, site-protection, and accident-management route classes as source-visible domain routes; do not route authority to this repository. | Pass |
| Domain absorbers | Nuclear-safety, tsunami-hazard, severe-accident, emergency, regulatory, health, and legal accounts must remain visible as competing explanations and remedy boundaries. | Fail typed preservation |
| Mixed-fit status | The translated row must remain mixed rather than becoming ordinary positive evidence. | Fail typed preservation |

The last two rows fail for the same structural reason. The typed minimum
register has no typed `absorber_or_counterevidence` field and no translation-
level fit-status field. `stop_condition: defer`, provisional validation, and a
possible contradiction do not preserve why the source owner calls the fixture
mixed. A formally complete row could therefore hide the domain absorbers in
narrative prose and later be counted as positive evidence.

## Pass-Condition Score

| P4 condition | Score | Reason |
|---|---|---|
| Preserve ambiguity rather than count ordinary positive evidence. | Fail | No typed field carries the source owner's mixed-fit classification. |
| Tie every translated field to the source fixture without adding claims. | Pass | The bounded readings above use only the hash-pinned source-owner artifact. |
| Keep remedies and accountable routes outside this repository. | Pass | The lowest-fitting routes remain domain-specific and non-prescriptive. |
| Expose unresolved validation and contradiction state. | Pass | Existing typed values can preserve `unknown` and `possible`. |
| Create no consequential or external action. | Pass | This is a repository-local score only. |

## Result

Disposition: revise.

`CMD-0001` is not killed: its source, provisional-status, contradiction, stop,
and lower-owner-routing controls all survive the fixture. It does not earn a
bounded pass because the exact P4 ambiguity and absorber requirements can still
be hidden while every current register field is formally complete.

The smallest admissible repair is a translation wrapper, separate from source
truth and the operational register, with typed fields for:

- `source_owner_fit_status`: positive, mixed, refused, or unresolved; and
- `absorber_or_counterevidence`: one or more source-backed, owner-scoped
  competing explanations or `none_named`.

The wrapper must fail if either value is supplied only in prose. It must not
change the source owner's classification, convert an absorber into a generic
mechanism claim, or prescribe any domain remedy.

## Next Condition

Keep the candidate admitted and revision-required. Draft the minimal
translation wrapper, then rerun P4 against the same frozen fixture. Do not seek
another case merely to avoid the exposed field gap.

No graduation, transfer, deployment, participation, field test, incentive,
institution, spin-out, domain remedy, destination obligation, or external
action is authorized.
