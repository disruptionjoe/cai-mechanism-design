# Mechanism Design local-model packets

Status: `ready_dormant`

This directory is the target-owned interface for two rolling local-model work
slots. It reuses the shared Mac packet executor and the CapacityOS Repository
Operating Cycle. It is not a queue, a second workflow system, or owner truth.

The stable slot paths are:

- `packets/01-candidate-work/prompt.md`
- `packets/02-proving-work/prompt.md`

The slot directories and `prompt.md` files are intentionally absent while no
exact bounded work is admitted. A missing prompt is not a successful run and
must not be scheduled. Systemic Repository Stewardship prepares a complete
prompt through normal Progress; the Mac schedule points directly to that slot;
the local model writes immutable candidate output outside this repository; and
Frontier Prepared Progress independently verifies anything proposed for owner
truth.

Suitable local work includes alternative and mechanism comparisons, first
drafts from frozen evidence, synthetic fixture construction, application of an
explicit proving test, and reconciliation or crosswalks. Frontier retains
source and inquiry admission, existing-owner fit, materially new source claims,
hard mechanism architecture, consequential proving, disposition, graduation,
destination-owner acceptance, external action, and final integration.

Current target truth still controls. In particular, this interface does not
reopen deferred `CMD-0001`, increase its proving count, or manufacture the new
source, owner-fit, or destination-owner evidence named in `ROADMAP.md`.
