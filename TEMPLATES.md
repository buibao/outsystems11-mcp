# Task package minimum

Copy templates into `tasks/<task-id>/` and replace required fields. For a small
task, keep brief/spec/report short and mark nonapplicable sections N/A with a
reason. For a complex UI/data/integration task expand the same contract.

Always: brief.md, spec.md, task-state.json, report.md.
New/material O11 UI: one [UI design contract](templates/UI_DESIGN_CONTRACT.template.md) is the handoff body before dependent O11 writes; link it from the spec and optional transport envelope. Use a focused [foundation catalog](templates/UI_FOUNDATION.template.json). Keep the bounded plan in the spec or a linked O11 plan, without copying mapping/state/token tables. Small maintenance may reuse current accepted design/foundation. See [design start](prompts/UI_DESIGN_START.md) and [UI apply](prompts/O11_UI_APPLY.md).
Worker assignments/results may be session records; save material outputs under
worker-results/ with project/task/revision. Keep actual tool evidence and required
assets under evidence/ or an approved durable external locator.

The Coordinator owns canonical files; workers write only separately assigned
outputs. The state is not a credential store or live connection manager.
