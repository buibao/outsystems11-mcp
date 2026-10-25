# Project context

## Current workflow binding — 2026-10-23

The VibeWorkflow setup created an intentionally unbound DRAFT [project.json](../project.json): business ID/name UNKNOWN, Site/O11 bindings null, no active task. For new work, confirm project/task/route/targets rather than inheriting historical feature context below. The live read-only setup observation is recorded separately in [VIBE-SETUP.report.md](execution/VIBE-SETUP.report.md); it does not select a business target. Existing records are retained as history; no removed feature/project is reactivated. See [quickstart](VIBEWORKFLOW_QUICKSTART.md) for Work/local responsibilities and project switching.

Latest task state (UI-002 v1.1, 2026-10-22): MyApp Reactive key `1e4623ed-64fa-4600-97f5-8a8442332e57`; Development versionSequence 135 independently identified after user manual publish. Figma hierarchy/layout correction is merged and runtime-verified with 34 successful browser checks and12 scenario comparisons. Model validation remains0 errors/4 baseline warnings. Existing Anonymous and Registered roles and the unused OnReady action are preserved. Startup and dialog/focus defects are resolved; root favicon404 and minor visual residuals are disclosed. Final read-only session closed with no pending changes. omlPublish remains disabled. See [UI-002 spec](specs/UI-002-tax-documents-visual-fidelity.md), [report](execution/UI-002.report.md) and [comparison gallery](../artifacts/ui-002/comparison.html); historical task notes below remain prior-session evidence.

## Confirmed observations

| Item | Evidence / value |
| --- | --- |
| Business workspace | `D:\OutsystemsAIAgent`, the existing user workspace |
| Upstream distribution checkout | `D:\OutsystemsAIAgent\outsystems11-mcp`; not the business repository |
| Target module | Latest UI-002 target: `MyApp`, key `1e4623ed-64fa-4600-97f5-8a8442332e57`, Reactive, Development135. Re-identify for new operations or after a host restart. |
| Style / open state | `Reactive`; `isOpen=true`, `isReference=false` from native `listApps` |
| Environment UI label | `Development - personal-g4et6y1o.outsystemscloud.com`, independently read with Windows UI Automation from Service Studio |
| Resident module references | `OutSystemsCharts`, `OutSystemsUI`, `OutSystemsMaps`, `(System)`, `Users` from `runQuery` |
| Local entities in current live model | `DocumentType`, `DocumentStatus`, both Static Entities for the Tax Documents frontend prototype; 0 ordinary persisted Entities. Bootstrap's empty collection is historical. |
| Referenced entities in MCP data model | 57; includes `(System)/User`; see [preflight evidence](evidence/preflight.json) |
| Local server actions | `DoLogin`, `DoLogout`; 23 other server actions are referenced |
| Local role names | `Anonymous`, `Registered`; future feature role/ownership requirements remain UNKNOWN |
| Representative action | `DoLogin` is private, in folder `Authentication`, and invokes resident `Users.User_Login`; its Username/Password inputs are parameter names, not recorded credential values |
| Model validation | Bootstrap baseline: 0 errors, 2 warnings. After Tax Documents merge: 0 errors, 3 warnings; new Registered-only Screen has the same Missing roles warning. See [feature evidence](evidence/tax-documents-live.json). |
| Version field | `listApps.version="0"`; this is not evidence of a published/recoverable platform version |

These are observations of the current setup, not a business architecture specification. Native module identity and the UI environment label were observed independently. Sidecar reads follow the host's current snapshot/pending-copy pointer. Bootstrap created no pending model copy; absence of unrelated pre-existing pending work is UNKNOWN.

## Unknowns to resolve for the relevant feature

| Topic | Status |
| --- | --- |
| Business purpose and first feature acceptance criteria | UNKNOWN |
| Business/application owner, module owner, reviewer, release owner | UNKNOWN |
| Application boundary beyond the observed module | UNKNOWN; do not infer it from the name MyApp |
| Authoritative environment role and permitted deployment target | UNKNOWN; the observed Development label alone is not organizational authorization |
| O11 environment/platform version | UNKNOWN; local Service Studio version is recorded separately |
| Approved dependency directions and public API policy | UNKNOWN |
| Custom roles, record ownership, tenant boundaries, sensitive data classification | UNKNOWN; inventory alone does not establish access policy |
| Expected datasets, performance budgets, retention/deletion, concurrency policy | UNKNOWN |
| Current published version, durable checkpoint and restore procedure | DEV135 verified for UI-002; prewrite OML in artifacts/ui-002. Restoration itself NOT_RUN. |
| Organization-approved AI account/data settings and documentation repository | UNKNOWN |

## Local working policy adopted for bootstrap

The original bootstrap request authorized local guidance/configuration and read-only model inspection. The user subsequently authorized the Tax Documents UI prototype and its normal manual merge through the full supplied prompt. This task is merged and read back from live; publish, runtime data access, migrations and production behavior were not part of it. See [feature report](tax-documents-preview.md).

Current feature objects: `MainFlow/TaxDocumentsPreview`, 9 reusable Blocks, 6 transient view-model Structures and native Script `TaxDocumentsPrototype`. The user confirmed manual Compare and Merge and waived a separate checkpoint for this prototype. The business architecture, backend rules and future deployment authority remain unestablished; presentation-only reviewer mode is not authorization.

CSS-001 corrective spec version 1.1 was subsequently authorized with CompletionTarget MERGED. Actual merge succeeded; fresh accepted-live readback found 0 errors / the same 3 warnings. Shared feature CSS now lives in MyApp theme under `.tax-documents-preview`, with Screen CSS empty, native btn classes, Content/Tag and native Popup inside existing Blocks. Theme prefix, primary palette/base theme and fixture/action contracts were preserved. See [execution report](execution/CSS-001.report.md). Publish/runtime remain NOT_RUN and [DEF-001](defects/DEF-001-tax-preview-reduce.md) remains OPEN. A later host restart interrupted acknowledgement of the read-only checkout's closure; current post-restart module/session state needs re-identification before further OML operations.

The official skill is project-scoped at `.agents/skills/servicestudio-mcp-oml/`. Start Codex from the business workspace. The staged skill copy inside the upstream checkout is preserved but explicitly disabled in Codex configuration to avoid competing discovery.

Do not automatically update upstream files during feature tasks. Record an explicit revision change and rerun setup verification when upgrading.
