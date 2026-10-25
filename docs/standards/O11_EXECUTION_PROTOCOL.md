# O11 execution protocol — version 1.0

This is the proposed team process for feature implementation through O11 MCP. It complements the official installed skill; it does not replace that skill's API contract, applicable policies or actual permissions.

## Operating rules

Read the selected feature spec, relevant AGENTS.md files and the official O11 skill. Use the tool catalog and references matching the installed version. Do not hard-code outdated tool envelopes from this process document.

Treat the spec and execution report as restartable working records. Keep the next step, observed state and unresolved decisions current. On resume, revalidate the live target and pending-change state; old notes are not proof that the module is unchanged.

Only one writer should own a live module at a time. Local Git/worktrees isolate documents or code files, not concurrent edits to one Service Studio module. On unexpected user edits, re-read before continuing.

Do not fetch all reference documents or module settings into context. Read the relevant slice. Keep credentials, tokens and personal data out of evidence.

## Gate matrix

| Gate | Entry and required work | Exit evidence | If it cannot pass |
| --- | --- | --- | --- |
| G0 Target/baseline | Read the target identity/style, installed skill, effective operations and relevant existing model | Identified target; baseline validation; current edit/checkpoint state | Continue safe discovery/docs; block dependent writes |
| G1 Ready to implement | Resolve scope-critical unknowns; map MUST requirements to objects and checks; plan bounded milestones | Spec READY or explicitly recorded nonblocking unknowns; operation scope grounded in user instructions | Ask only the missing material decision; do independent work |
| G2 Build slice | Implement one coherent authorized slice with relevant official API guidance | Actual changed objects and readable flows | Diagnose exact failure; preserve recoverable work |
| G3 Verify model | Read back changed elements, compare baseline validation, verify bindings/contracts and relevant callers | Intended changes observed; no new unresolved errors; warnings assessed | Fix within scope; do not merge invalid work to claim progress |
| G4 Merge | If included, present validated work using current manual review settings | Actual merge outcome and post-merge read-back | Report pending/rejected/failed/unknown; never infer acceptance |
| G5 Runtime | If included and authorized, identify published version/environment and execute applicable checks | Publish identity plus behavior/visual evidence for required runtime checks | Mark blocked/not run; never equate model validation with runtime success |
| G6 Handoff | Reconcile requirement coverage, actual stage, deviations and report | All selected-target obligations accounted for; precise next step | Report partial or blocked, not blanket DONE |

G2/G3 may repeat for slices. Merge the coherent final change at the feature boundary unless the spec calls for intermediate integration. A gate is not a mandatory human meeting or fresh approval request. Proceed automatically when its conditions are satisfied and the work is already authorized.

## Completion-target rules

| Target | Required gates | Claims that remain excluded unless separately evidenced |
| --- | --- | --- |
| MODEL_REVIEW | G0, G1, G2, G3, G6 | Accepted merge, successful publish, runtime correctness |
| MERGED | G0–G4 and G6 | Successful publish and runtime correctness |
| RUNTIME_VERIFIED | G0–G6 | Production release if only DEV was tested |

Record every stage independently. If a request requires runtime behavior but publishing/testing is unavailable, the result is partial/blocked even when model work is ready. A narrower target must have been selected honestly before completion; do not downgrade it after failure merely to claim success.

## Verification principles

- A successful mutation response needs a targeted read-back and validation assessment.
- Design-time validation does not demonstrate business correctness, performance, runtime authorization, visual fidelity or external side effects.
- A pending snapshot, the accepted live model and the published application are different evidence subjects. Label which one was checked.
- Compare affected-object details against the baseline, not only aggregate error counts. A stable count can hide one fixed error and one new error.
- Test changed behavior and its meaningful failure cases. Select appropriate existing tooling or reproducible manual checks; do not invent a conventional test runner for OML-only work.
- Visual evidence needs the state, viewport and version under test. Missing browser access means NOT_RUN, not inferred PASS.
- Requirements with no applicable section may use N/A with a concrete reason. N/A is not a way to bypass a failed check.

## Exceptions and recovery

Classify failures before retrying: connectivity/authorization; unsupported API/compilation; invalid resulting model; merge rejection; timeout/unknown outcome; runtime defect.

After a timeout or interrupted write, inspect state before replaying the operation. Recover from the installed skill's supported mechanisms. Do not repeatedly issue the same mutation, merge, refresh or publish to obtain a clean response. Never discard unexplained pending work as a troubleshooting shortcut.

If a required dependency cannot be added through available tools, record its exact name/version and the manual step. Refreshing existing references is a separate operation and may affect staged changes; do it only when in scope.

Preserve a recoverable O11 checkpoint before material writes. A Git commit of Markdown does not preserve the live module. Temporary snapshots are not a durable backup. Restoring an O11 model version does not undo database migrations, data writes or external operations.

On changing user instructions, keep completed valid work, revise only the affected requirements/milestones/checks and record the decision. Never self-authorize extra deployment or convert an unconfirmed business rule into an accepted requirement.

## Report rules

Use the report template. Store check results as PASS, FAIL, NOT_RUN, BLOCKED or N/A. A PASS needs an evidence ID. NOT_RUN and BLOCKED need a reason and next action. Track baseline issues separately.

Evidence should identify object/state, actual observation, version/snapshot when available, method and time. Local tool-result summaries are acceptable if the host exposes no permanent log ID; say so. Do not fabricate log paths, timestamps, screenshots, approval records or artifact hashes.

On handoff, state the achieved stage, selected CompletionTarget, unmet checks, merge/publish/runtime states and exact next action. Do not hide a required failed check in a footnote under “completed.”

## Reference basis and limits

OpenAI Docs recommends durable project guidance and verification; its execution-plan guidance supports maintained progress/decision records. This protocol adapts those ideas to O11 and adds team-specific gate/traceability policy. It is not the official OpenAI ExecPlan template or an ISO/IEEE conformance claim.

OutSystems documents snapshot-based changes, a separate merge operation and configurable manual review. The host's installed version and current product guidance govern API behavior. If upstream reference notes conflict, record the discrepancy and check actual supported behavior rather than bypassing restrictions.

- https://developers.openai.com/codex/learn/best-practices
- https://developers.openai.com/codex/guides/agents-md
- https://developers.openai.com/cookbook/articles/codex_exec_plans
- https://success.outsystems.com/documentation/11/outsystems_mcp/security_and_data_handling/
- https://success.outsystems.com/documentation/11/outsystems_mcp/outsystems_mcp_capabilities/
- https://github.com/OutSystems/outsystems11-mcp

## Native UI refinement (v1.1)

Apply the [native-first](O11_UI_NATIVE_FIRST.md) and [lean](LEAN_UI_WORKFLOW.md) standards within existing gates. O11 G0/G1 resolve actual Screen/UI Flow theme/layout, installed native contracts/public actions and tokens, plus user-accepted Sites/UI contract for new/material UI before dependent writes. G2/G3 establish a representative native slice; necessary runtime evidence uses authorized G4/G5 for that slice before dependent expansion. No merge at MODEL_REVIEW and no implied publish authority. If blocked, continue independent preparation and preserve the selected target; a task-explicit expansion risk decision retains NOT_RUN/BLOCKED evidence. Small maintenance can reuse valid accepted design/foundation. No additional gate system is introduced.
