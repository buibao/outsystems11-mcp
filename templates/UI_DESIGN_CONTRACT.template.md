# Versioned O11 UI design contract

Project/task/spec/contract revisions: <IDs>
Status: DRAFT / REVIEW_READY / ACCEPTED / SUPERSEDED
Foundation ID/revision/hash: <actual>
Sites project/version/commit/URL: <actual or unavailable>
Source references + state/viewports/zoom/DPR: <actual and limits>
Design acceptance: <actual user decision, revision and date; never invented>

## Outcome and boundary

<One observable outcome; reused/changed objects; exclusions. Separate UI state, mocked transitions and real operations.>

## Canonical native component map

Canonical source: <this contract path/revision/hash>. Sites Review view: <consumer/projection locator and exact source revision>. App-to-Review UI-ID navigation: <overlay/highlight/anchor mechanism including conditional states>. Candidate sources: <DEV-CS page / UI-CS section from [source index](../docs/references/cheatsheets/README.md)>.

| UI ID | UI region / responsibility | Classification | O11 widget/pattern + module | Availability / version evidence | Inputs / events / public actions | Classes / tokens (IDs) | Custom gap (exception ID) | Rationale | Acceptance status / decision | Candidate source / installed signature locator | Critical / resolution |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <stable ID> | <region and relevant states> | Unverified | <exact candidate or none/unknown> | <resident/available-not-referenced/unavailable/unknown; version evidence> | <supported contracts or unknown> | <observed names / token IDs> | <none or exception ID> | <why chosen; alternatives inspected> | <pending/accepted/rejected + revision/decision> | <reference provenance separate from installed evidence> | <yes/no; evidence/owner> |

Allowed classification: Native / Native + custom CSS / Native + custom behavior / Fully custom / Unverified. Combined CSS/behavior extensions use Native + custom behavior and describe both. Classification describes the proposed O11 implementation; Sites rendering remains explicitly labeled web simulation. Fully custom requires an accepted evidenced gap. Critical Unverified must be resolved before dependent O11 writes; user design acceptance alone is not installed evidence.

This is the only editable component map. Sites Review view uses or references these rows and the token/exception sections below; no independently maintained mapping tables. Generated projections record source revision/hash and check missing/extra IDs plus field drift after regeneration. Prototype, acceptance and handoff must identify the same revision.

Calling a Button “tabs” does not satisfy a Tabs pattern decision. A CSS selector is not a pattern instance. Resolve critical UNKNOWN before dependent writes; do not invent signatures from web documentation.

## Token and style map

| Token ID / semantic purpose | Existing utility/variable | Observed value/source | Prototype use | O11 application | Accepted deviation |
| --- | --- | --- | --- | --- | --- |
| <e.g. error surface> | <actual variable> | <foundation locator> | <exact/simulated> | <theme/class/parameter> | <none or decision> |

<Actual Screen/UI Flow theme and layout; font family/weight/size; width; spacing; border; icon source; default/hover/focus/disabled. New token only when missing and accepted, with owner and reuse scope.>

## Blocks, state and interactions

<Screen vs Block responsibilities, inputs/events, stable keys, source of truth, local resets/cancel. Do not convert screenshot variants into business rules. Do not add backend/CRUD under a UI-only scope.>

| State / AC | Reference | Sites preview evidence | Required O11 outcome | Check and layer |
| --- | --- | --- | --- | --- |
| <all required references remain covered> | <asset> | <observed/not run> | <outcome> | <model/runtime/visual> |

Scenario switcher location: Sites/test harness / explicitly required O11 control.
Native-vs-preview labels: <actual assets vs web simulations; unverified behavior>

## Custom exceptions

| Exception ID / UI IDs | Native alternative inspected | Exact unsupported gap and evidence | Proposed minimal extension | CSS/token/JS ownership | Acceptance |
| --- | --- | --- | --- | --- | --- |
| <ID> | <parameters/actions included> | <not just initial parameter limits> | <scope> | <owner> | <actual or pending> |

## Receiving acknowledgement and application readiness

<Local operator confirms identity, foundation revision, accessible design assets, native feasibility and exact accepted contract revision. Stale foundation requires targeted recheck. State live-write authorization, review setting, checkpoint and pending work independently.>

Next slice: <smallest representative native slice, checks and expected delta>.
Critical unknowns/blockers: <owner/next action>.
