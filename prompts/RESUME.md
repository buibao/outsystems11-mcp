# Resume / switch

Resume project <project-id>, task <task-id> at <workspace/package>.
Re-read task state/spec/report and reconcile their revisions with the actual
platform state. Collect/retire old workers as needed; preserve pending user work.
Do not replay completed mutations or merges to repair missing acknowledgements.
Continue from the next safe authorized operation, using actual subagents only
for bounded independent work. When switching projects first follow
workflow/PROJECT_SWITCH.md. Report any mismatch and block only dependent actions.
