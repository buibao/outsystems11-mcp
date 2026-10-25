# Assignment and handoff contracts

Every worker assignment uses `templates/WORKER_ASSIGNMENT.template.md`; each result follows `templates/WORKER_RESULT.template.md`. A result identifies project/task and the exact input revision. Mismatching identity/revision is a rebase/re-read issue, not evidence for the current task.

The coordinator supplies current assumptions, scope, allowed operations/paths, snapshot subject and required output. Worker output separates observed facts, proposals and unknowns. PASS requires an actual check and evidence. PREPARED means a proposal is ready, not that the target changed.

## Work/Sites -> local O11

Freeze one design handoff revision at a time. Include brief/spec/AC, reference assets by state and viewport, Visual Contract, component/state/event/data contracts, synthetic fixtures, exclusions, unresolved decisions and known limitations. Include Sites project/version/source commit only when actually available. A live URL by itself is mutable and insufficient as the only design record.

Transport via an approved shared repo or an explicit package/ZIP. Do not assume Work can access a local Windows path or local Codex can read a Library item/Work filesystem. Verify access on the receiving side; preserve relative paths. Never transport credentials/session tokens. No bridge or automatic conversation-to-conversation invocation is installed by this kit.

Codex local checks project/task/revision, reads the handed-off contract and inspects the target. It creates the O11 plan, records native mapping gaps and preserves explicit exclusions. O11 implementation has its own readback/merge/runtime evidence.

## Control ownership between surfaces

Use `active_surface` (WORK / LOCAL / UNASSIGNED) in task state. Only the active
surface's Coordinator updates canonical task spec/state/report. Freeze the outgoing
handoff revision, record the intended next surface and stop editing that revision.
The receiver acknowledges the exact identity/revision/access before becoming the
active surface. When copies are transported by ZIP, preserve the outgoing snapshot
as immutable history and identify the receiving working copy explicitly; do not
pretend the two files synchronize themselves. This field is a coordination record,
not an atomic lock or access-control mechanism.

Other surfaces can return new proposals in separate outputs, but must route changes
back to the active Coordinator for reconciliation. Do not allow simultaneous design
baseline edits and implementation against an unacknowledged moving reference.

## Changes after handoff

If requirements/reference change, increment the affected revision and record decision/source. Mark downstream plans/results stale where impacted; do not redo unrelated completed work. Both sides acknowledge the new revision through their task state/report. A newer Site publish alone does not silently change the accepted design baseline.

For UI, the [UI design contract](../templates/UI_DESIGN_CONTRACT.template.md) is the handoff body: one canonical instance, linked from spec/plan/report. The generic handoff is only the transport/identity envelope; do not duplicate state, mapping or token tables. Record actual design acceptance and receiving acknowledgement separately. Reuse valid foundation/evidence revisions; changed decisions invalidate only affected downstream checks.
