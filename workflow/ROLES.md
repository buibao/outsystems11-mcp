# Role contracts

The primary Coordinator owns stage routing, canonical spec/state/report and decisions; it reconciles worker output and is accountable for the final claim. Roles do not create separate tool permissions.

| Role | Input | Output | Boundary |
| --- | --- | --- | --- |
| analyst | Brief, business references, current behavior | Testable requirements, exclusions, AC, material questions | Does not invent business policy or edit applications |
| designer | Requirements, design system, actual reference states | Visual/state contract, prototype source proposal, reference matrix | Sites owner handles checkout/native calls/publication |
| architect | Accepted design handoff, filtered target snapshots, boundaries | Screen/Block/Structure/Event mapping, reuse/dependency decisions, data/security contracts | No live O11 calls, no assumed web-to-OML import |
| planner | Spec/contracts, baseline, available capabilities | Dependency-ordered slices, checks, recovery/merge/runtime plan | No new requirements or authority |
| builder | Bounded slice, exact snapshots/revisions, assigned output paths | Source patch OR full O11 mutation lambda proposal, expected delta, guards, verification plan | No O11 MCP/session calls; no Site native calls; may edit only assigned source files |
| reviewer | Diff/proposal, spec, baseline and readback evidence | Severity-ranked reproducible findings, contract/consumer gaps, review disposition | Does not fix source or mutate target; instructions are not sandbox enforcement |
| qa | AC/check matrix, fixtures, target version and browser/test capability | Actual observed case results, evidence, regression/visual/access findings | No publication/config changes; use authorized test interactions only |

## Parallel groups

- Analyst requirements investigation and architect current-state investigation, with no implementation decisions until reconciled.
- Designer reference analysis and architect native-component feasibility.
- Reviewer contract review and QA preparation against a stable snapshot.
- Functional QA and visual QA may use separate workers only with independent browser contexts/fixtures and no shared mutable backend state.

## Serial ownership

- O11 operator: the primary local session owns all MCP calls; builder/reviewer receive snapshots. Git worktrees do not isolate a live O11 module.
- Sites owner: primary Work conversation owns checkout lifecycle, manifest/identity, native calls, synchronization and publication; workers may receive disjoint source tasks.
- Coordinator alone updates canonical task state/spec/report. Workers return results or write only assigned separate result files.

Do not send the full corpus or secrets to every role. Send scope, relevant sources, baseline subject/revision and the smallest useful snapshot. Do not allocate a distinct agent for trivial edits when it adds no independence or parallel value.

Default staffing follows the [lean UI standard](../docs/standards/LEAN_UI_WORKFLOW.md): primary coordinates, plans and implements; one independent reviewer checks meaningful milestones. The roles and parallel groups above are optional choices for bounded independent work, never a mandatory relay. UI roles use the same [native-first contract](../docs/standards/O11_UI_NATIVE_FIRST.md), with focused snapshots/deltas and raw evidence locators.
