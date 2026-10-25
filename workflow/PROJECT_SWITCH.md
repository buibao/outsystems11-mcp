# Switch projects without state leakage

1. Stop assigning new mutation/source tasks in the current project. Collect worker outputs and stop irrelevant workers before changing the active task.
2. Record actual pending work, target/version and next action in the old task report/state. Never auto-merge/discard/reset to make the switch convenient.
3. Dispose or release the old platform session only through the supported host lifecycle, after verifying what happens to pending work. Preserve recoverable artifacts. A metadata owner flag is a coordination convention, not a distributed lock.
4. Open the new project's own workspace/profile/task and bind the corresponding Work conversation/Site where applicable. Reuse workflow core/config templates, not old runtime identity or task state.
5. Verify the new environment/module/style/Site against current tools. Resolve collisions such as two open modules with the same name by independent environment identity.
6. Reassess authority and connection approval. Same-session token reuse follows the approved session contract; do not blindly rotate on a project switch or transfer tokens between agents. A genuinely new session needs its own approval where required.
7. Dispatch fresh scoped workers with the new project/task/revisions. Record the first observation and next operation. Different projects do not imply simultaneous writers are safe on a shared module/Site.
