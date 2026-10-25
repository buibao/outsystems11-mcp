# Setup corrections report - 2026-10-26

Scope: user-authorized correction of identified setup errors and contradictory guidance only. No new business-contract process, gate, readiness-check feature, pilot, model/settings change or O11/Sites operation. Existing historical reports remain unchanged.

## Changes

| File | Correction |
| --- | --- |
| [Project context](../project-context.md) | Current binding points to profile and selected task records; MyApp/UI-002 observations explicitly historical, not reusable authority |
| [Setup status](../setup-status.md) | Current entry point separates setup reports from dated bootstrap/MyApp instructions; old checklist must not be replayed |
| [Verification](../verification.md) | Selected task owns current evidence; MyApp verification is historical, not WHT verification |
| [Workflow instruction template](../../templates/AGENTS.workflow.template.md) | Accepted contract required before dependent O11 writes; representative-slice evidence uses existing protocol |
| [WHT spec](../../tasks/UI-001/spec.md) | Replaced duplicated progress with canonical report/state links; removed obsolete remaining-merge/readback wording. No requirements, route, acceptance criteria, spec revision or CompletionTarget changes |
| [Setup verification suite](../../scripts/verify_workflow_setup.py) | Accept UTF-8 BOM; check DRAFT rejection in disposable fixture rather than requiring real current profile to remain DRAFT |

## Checks and actual results

- PASS: direct setup suite, 9/9 cases, against current ACTIVE workspace profile with BOM; profile unchanged.
- PASS: existing package/metadata checker for WHT/UI-001 with --ready --for-o11. No semantic/readiness features added to the checker.
- Local link/syntax results: [checks](../evidence/setup-corrections/local-checks.json).
- Preservation PASS: exactly six pre-existing files changed; all others preserved, including upstream/index, official skill, configs, project profile, WHT task-state/report/proposals/evidence. [Preservation](../evidence/setup-corrections/preservation.json).
- Independent review: [result](../evidence/setup-corrections/review.md).

Evidence: [test output](../evidence/setup-corrections/test-results.json), [bounded diff](../evidence/setup-corrections/corrections.diff). Earlier setup reports correctly retain their original failed-suite observations; this later fix supersedes that limitation without rewriting history. Existing broken links to missing historical artifacts are disclosed, not restored.

## Limits

O11 model/native/runtime/visual checks and Sites: NOT_RUN, outside scope. WHT status remains unchanged; this edit reconciles recorded progress and does not reverify live merge/publication. Metadata and test-suite PASS do not prove business rules, visual fidelity, role reload or runtime behavior. Proposed business-rule contracts, new structural checks and a pilot remain unimplemented.
