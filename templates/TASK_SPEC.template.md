# Task specification

Project/task/spec revision: <IDs/version>
Status: DRAFT / READY / IN_PROGRESS / BLOCKED / CLOSED
Mode: UI_PROTOTYPE / FUNCTIONAL / REFACTOR / FIX
Detail: LIGHT / FULL
Route: HYBRID_SITES_O11 / O11_ONLY / SITES_ONLY
Sites target / O11 target: <targets or N/A>

## Outcome and boundaries

<Current behavior, requested outcome, in/out scope and protected consumers.>

## Sources and decisions

<Selected reference revisions; CONFIRMED/OBSERVED/PROPOSED/UNKNOWN; precedence for design vs theme.>

## Requirements and acceptance

| Req | Observable requirement | Source | Objects/contracts | AC/check/layer |
| --- | --- | --- | --- | --- |
| R-001 | <requirement> | <source> | <object> | <check> |

## Contracts and Visual Contract

<Link the single UI design contract and foundation revision; use [UI contract template](UI_DESIGN_CONTRACT.template.md). It contains state/native/token/custom-exception tables and actual design acceptance; do not duplicate them here. Small maintenance: name the unchanged accepted revision and delta.>

## Conditional engineering

<Authorization/access, queries, persistence, transactions/concurrency, integrations/timers/performance/recovery if applicable; N/A requires reason.>

## Target, baseline and execution

<Observed environment/module/Site, actual tool/skill revisions, writer/session state and checkpoint. Dependency-ordered slices, exact permitted operations and authorization source. No inferred publish permission.>

## Check matrix

| Check | Version/fixture/role | Steps | Expected | Required target |
| --- | --- | --- | --- | --- |
| TC-001 | <case> | <reproducible steps> | <result> | <target> |

## Recovery, changes and open decisions

<Checkpoint/restore limits, interrupted-write inspection, material spec changes/revisions, blocker owner/next action.>
