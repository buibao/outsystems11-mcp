# Protocol v1.1

## Routes

The project profile supplies `default_delivery_route`. Each task records its own
`delivery_route`; that task value controls the stages. A HYBRID project can run a
small O11_ONLY fix or SITES_ONLY prototype without recreating the other platform.
Choose targets before dependent implementation/integration; an unknown later-stage
target does not block independent early discovery/design.

- HYBRID_SITES_O11: intake -> design/prototype -> versioned handoff -> O11 architecture/plan -> implementation -> review/QA -> handoff.
- O11_ONLY: small maintenance may reuse a current accepted design/foundation without generating another Site. New UI/material redesign requires Sites and accepted UI contract under the [native-first standard](../docs/standards/O11_UI_NATIVE_FIRST.md). Resolve route/spec revision before dependent work; never silently rewrite an existing task route or scope.
- SITES_ONLY: use Sites adapter and that platform's source/build/preview/deployment workflow. O11 stages N/A.

Stages describe responsibilities. Independent investigations/reviews can overlap; dependent design/implementation work waits for the relevant contract. Do not force all roles onto every task. Default: primary coordinates, plans and implements, with one independent reviewer at meaningful milestones. Additional roles need concrete independent work; no recursive spawning; smallest relevant context. Follow the [lean standard](../docs/standards/LEAN_UI_WORKFLOW.md). Reuse a role thread only while project/task/revisions remain aligned; retire irrelevant threads. When the runtime lacks subagents, say so and execute sequentially only if the user accepts that limitation for the task.

## Gates

| Gate | Required evidence | Lead/worker |
| --- | --- | --- |
| G0 Intake | Correct project/task, outcome, exclusions, delivery route, per-platform CompletionTarget, actual operation scope | Primary; analyst only if useful |
| G1 Ready | Required sources/contracts available, material decisions resolved, target/baseline/checkpoint when needed; new/material UI has versioned user-accepted Sites/UI contract, actual Screen/UI Flow foundation and resolved native map | Primary; optional focused specialist |
| G2 Representative slice | One meaningful flow/component demonstrates the chosen design/behavior; O11 UI verifies native instances/contracts and actual theme/font/token/pattern runtime evidence before dependent broad expansion | Primary; reviewer at milestone |
| G3 Model/source review | Bounded diff/readback, validation vs baseline, contract/consumer review; relevant existing source checks for Sites | reviewer + platform owner |
| G4 Integrate | Actual manual O11 merge and accepted-live readback, OR Sites source/version integration according to adapter | platform owner |
| G5 Runtime | Identified published version plus required functional/visual/access checks | QA; platform owner controls mutation/publication |
| G6 Close | MUST coverage, evidence locators, actual achieved stage, pending disposition and restartable next action | Coordinator |

G2/G3 repeat for coherent slices. A gate is not automatically a new human approval. Continue authorized work; never derive authority from a status label. If a material design conflict lacks a decision, stop only dependent changes.

## Two completion tracks

Sites prototype target: LOCAL_REVIEW / SAVED_VERSION / DEPLOYED_VERIFIED.
O11 target: MODEL_REVIEW / MERGED / RUNTIME_VERIFIED.

These are project-process labels, not tool enums. LOCAL_REVIEW needs actual available local preview/check evidence; SAVED_VERSION needs a real saved identity; DEPLOYED_VERIFIED needs deployment evidence and required runtime checks. A successful deployment alone does not pass user behavior/visual requirements.

For O11, MODEL_REVIEW requires G0-G3/G6. MERGED adds G4. RUNTIME_VERIFIED adds G5 against an identified environment/version. A prototype can be complete while O11 work is pending. Do not collapse these into one DONE flag or silently lower a target after a failure.

| Sites target | Required gates | Explicit limit |
| --- | --- | --- |
| LOCAL_REVIEW | G0-G3, G6 | No registration/save/deployment for a local-only task |
| SAVED_VERSION | G0-G4, G6 | Requires actual saved identity; G5 is not required |
| DEPLOYED_VERIFIED | G0-G6 | Requires actual deployment plus selected runtime checks |

G4 for Sites means its supported source/save workflow, not an O11 merge.

## Verification and corrections

Label evidence as pending model, accepted live model, source commit, deployed prototype or published O11 runtime. Compare the changed behavior and affected consumers. A worker assertion needs inspection of its evidence before the Coordinator adopts it. Record defects separately from harness mistakes. A reviewer does not fix the application to make its own test pass; assign a correction back to the owner/builder and retest changed cases.

If the same bounded approach fails twice for the same cause, stop blind repetition: return diagnosis/options to Coordinator, inspect source/schema/state and revise the plan. This is an escalation of diagnosis, not permission to discard, refresh or publish. Persistent blockers stay BLOCKED with next action/owner.

## Resume

Read selected task state/spec/report; confirm project/task and revisions. Check unresolved writer/session state and live identity. Historical notes are not proof of the present state. Preserve user edits and unmerged work. A new session obtains its own approval where required; an ordinary reconnect in the same approved agent session reuses that token. Never pass session tokens in the handoff.

For new/material UI, G2 runtime evidence uses the existing G4/G5 integration/runtime conditions for that slice, only within authorized operations and CompletionTarget. MODEL_REVIEW never authorizes merge; MERGED never implies publication. If the runtime dependency is unavailable, block dependent broad expansion and continue independent preparation. A task-explicit risk decision may permit expansion with the runtime gap still NOT_RUN/BLOCKED; it never changes the target or fabricates PASS. Use one canonical spec, one UI contract as handoff body, and one current report; link evidence and reuse valid checks.
