# Start a project/task after setup

Historical v1.0 installation evidence is in the [report](execution/VIBE-SETUP.report.md); current native-first integration and limitations are in the [v1.1 setup report](execution/NATIVE-FIRST-SETUP.report.md). Setup evidence does not verify a feature end to end.

## Select the project and task

Start from the business workspace and read [AGENTS](../AGENTS.md), [current profile](../project.json), and the explicitly selected task. Preserve an existing binding; new project values stay UNKNOWN/null until confirmed. Do not inherit a historical target. Read [protocol](../workflow/PROTOCOL.md), [roles](../workflow/ROLES.md) and [contracts](../workflow/CONTRACTS.md). Existing WHT/UI-001 is not rewritten by setup.

Primary coordinates, plans and implements. One independent reviewer at meaningful milestones is the default; other roles need concrete independent outputs. Use real available agent controls; do not infer discovery from TOML alone. No Service Studio restart, duplicate server or settings change is required by this guidance.

## Design before dependent O11 UI writes

Use [UI design start](../prompts/UI_DESIGN_START.md). Primary local performs focused read-only O11 foundation discovery; Work cannot assume access to local Windows MCP. New/material O11 UI requires the installed Sites skill, review states, native component/public-action mapping, token/class map, justified custom exceptions and honest web simulation labels. Sites preview/save/deploy operations need their actual task scope.

Use one [UI contract](../templates/UI_DESIGN_CONTRACT.template.md) as handoff body. Record actual user acceptance of its revision; reuse valid same-scope acceptance. Freeze and transfer through an accessible approved ZIP/repo, without credentials. Local receiver acknowledges identity/revision/access and native feasibility before dependent implementation. A web source/URL is not OML or O11 runtime proof.

Small O11_ONLY maintenance may reuse valid accepted design/foundation without regenerating Sites. New/material UI must resolve the applicable route/revision before dependent work; do not silently change existing task scope. SITES_ONLY has null O11 target.

## Implement within the selected target

Use [templates](../TEMPLATES.md) for brief/spec/task-state/report. Link the UI contract; keep the plan in the spec or a linked plan without duplicated tables. Only the active-surface Coordinator updates canonical records. A copied state file is not synchronization or a lock.

Run `python scripts/check_workspace.py` and, for a selected filled task, `python scripts/check_workspace.py --ready --task tasks/<task-id> --for-o11`. These check metadata only, not authorization, native usage or runtime.

Use [Work-to-local](../prompts/WORK_TO_LOCAL.md) and [UI apply](../prompts/O11_UI_APPLY.md). Primary alone owns all O11 MCP calls and keeps its approved token in memory, reusing it on reconnect in the same session. A genuinely new session gets one new token. Resolve actual target/pending state, review setting, checkpoint and baseline before writes. Preserve manual Compare and Merge. MODEL_REVIEW stops before merge; publication requires its own authority; never enable disabled tools.

Verify a representative native slice through existing gates before dependent expansion; blocked runtime does not block independent documentation. Preserve CompletionTarget and report model, accepted-live, published and runtime evidence separately.

## Resume or switch

Follow [project switch](../workflow/PROJECT_SWITCH.md) and [resume](../prompts/RESUME.md). Settle pending state and old writers before binding another project. Never copy Site IDs, tokens, runtime bindings or old task state as new authority. Reuse the generic workflow and role guidance with deliberate project-specific integration; preserve upstream and official skill.
