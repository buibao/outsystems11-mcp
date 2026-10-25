# Verification

Current feature evidence belongs to the selected task report referenced by [project.json](../project.json); for the recorded WHT binding see [UI-001 report](../tasks/UI-001/report.md). The dated MyApp baselines below are historical and do not establish WHT validation/runtime results. Current local setup corrections are recorded [here](execution/SETUP-CORRECTIONS.report.md).

## Historical setup verification — 2026-10-23

VibeWorkflow SETUP_ONLY verification is in [VIBE-SETUP.report.md](execution/VIBE-SETUP.report.md). Actual checks: package/metadata validation (nine cases), effective config loading, native analyst/reviewer role discovery and exact instruction loading, real result contracts, primary-only O11 identity/environment/validation/restrictions. Baseline is the current MCP view, 0 errors/4 warnings. No feature changes, merge, publication, Site or runtime checks were executed by this setup. Historical feature verification below does not establish the behavior or target of a future task.

Historical MyApp feature verification (2026-10-22): UI-002 reached RUNTIME_VERIFIED on Development MyApp135. 34 successful browser checks,12 reference scenario captures and 0-error/4-baseline-warning live validation are documented in [UI-002 report](execution/UI-002.report.md). Startup and dialog defects resolved; favicon404 recorded. Bootstrap/prototype NOT_RUN statements below are historical and do not override this feature evidence.

## Bootstrap baseline

The read-only preflight targets `MyApp` (Reactive), through `servicestudio`. The endpoint is `http://127.0.0.1:41820/mcp`, previously confirmed by the user and by the owning Service Studio listener.

`getValidationMessages` with an empty filter returned all message types:

| Severity | Count |
| --- | --- |
| Error | 0 |
| Warning | 2 |
| Info | 0 |

| Path | Rule | Message |
| --- | --- | --- |
| `/Common/InvalidPermissions` | `AnonymousAccess_NoPermissionsNoRoles` | Missing roles |
| `/Common/Login` | `AnonymousAccess_NoPermissionsNoRoles` | Missing roles |

The tool says these screens are authenticated-only without assigned roles. This is an existing design-time baseline, not a finding to fix during bootstrap or proof of a runtime security defect. Investigate it when a relevant feature is scoped; do not change accessible roles merely to clear warnings.

Evidence: [preflight.json](evidence/preflight.json). The representative read was `getServerAction("DoLogin")`; no action was executed. Entity queries returned an empty local collection and the data-model read returned 57 referenced entities.

## Available checks and their limits

The 2026-10-22 Tax Documents prototype has since been manually merged and read back from a fresh live checkout: 0 errors, 3 warnings. The new warning is the same Missing roles rule on the Registered-only TaxDocumentsPreview Screen, in a module with no app roles. Its pure transient-data interaction checks passed locally; browser interaction, published CSS, visual comparison, responsive/keyboard behavior and runtime allowed/denied access are NOT RUN. See the [feature report](tax-documents-preview.md) and [live evidence](evidence/tax-documents-live.json). The original two-warning bootstrap baseline above remains the before-change comparison.

| Mechanism | What it establishes | Limits |
| --- | --- | --- |
| `listApps` | Open module identity/style | Does not establish deployed version or environment identity |
| `runQuery`, `getDataModel`, element reads | Model content through the current MCP view | Can follow a pending copy; does not prove published behavior |
| `getValidationMessages` | Model consistency baseline | Does not prove business rules, runtime authorization, SQL performance or integration behavior |
| Codex CLI `mcp list/get` | Configuration parsed by a fresh CLI process | Does not prove an already-running agent reloaded tool restrictions |
| Service Studio UI Automation | Visible environment label | Did not expose the MCP review setting inside its embedded browser |
| Runtime/browser tests and test harness | NOT RUN / availability UNKNOWN | No runtime testing or Forge installation was requested |

## Feature verification sequence

1. Resolve essential pending setup checks in [setup status](setup-status.md). Identify target, scope, reviewer and recoverable checkpoint.
2. Read affected model elements and current validation. Define acceptance checks and the role matrix before writing.
3. Apply a bounded, authorized model change; read it back and compare validation against the baseline, including affected flow layout.
4. Present validated work through manual Compare and Merge. Record merge outcome separately.
5. Only when deployment is explicitly authorized, establish published version and run meaningful runtime checks. Update evidence without secrets.

For each feature, select normal behavior, invalid input, denied access, relevant boundaries, material duplicate/concurrency cases and affected-caller regressions. Use an existing harness if one is identified; otherwise document reproducible manual steps. Do not invent generic source-code build commands for OML-only work.

## Role matrix template

| Operation | Role / ownership case | Expected allowed or denied result | Actual result / evidence |
| --- | --- | --- | --- |
| First feature: UNKNOWN | UNKNOWN | UNKNOWN | NOT RUN |

## Separate result fields

Report `staged`, `read-back verified`, `validation compared`, `merged`, `published` and `runtime tested` independently. Bootstrap leaves write/merge/publish/runtime checks NOT RUN. A disposable-module smoke edit needs its own explicit request.

## Native-first setup and future UI checks

See the [v1.1 setup report](execution/NATIVE-FIRST-SETUP.report.md). For future UI checks, verify actual native widget/pattern instances and signatures against the accepted [UI contract](../templates/UI_DESIGN_CONTRACT.template.md), then separately check identified runtime theme/font/tokens, served CSS, interaction/focus/disabled/responsive and required access cases. Use existing gates and a representative slice before dependent broad expansion. Metadata, class counts and fixture equality cannot prove native usage or visual/runtime behavior. Reuse evidence only while its foundation and affected contracts remain current.
