# WHT UI-001 specification
Project/task/spec: wht / UI-001 / 0.2. Progress: see [current report](report.md) and [task state](task-state.json). Mode UI_PROTOTYPE, FULL. Route O11_ONLY, LOCAL. O11 target RUNTIME_VERIFIED; Sites N/A.

## Outcome and boundaries
One new isolated prototype Screen and cohesive Blocks; preserve existing WHT_Request business screens and consumers. Synthetic in-memory state only. Request R1 is authoritative. No restoration of historical MyApp features.
All R01–R15 requirements and acceptance criteria in [A01](workers/A01-requirements.md) are adopted; all twelve reference matrix rows V01–V12 and visual hierarchy in [D01](workers/D01-visual.md) are adopted. These documents are part of spec 0.1; their proposals do not claim implementation.

## Contracts and Visual Contract
Blue underline tabs, neutral unboxed year disclosures, inline links, distinct action styles, muted status pills, compact/large upload variants, file metadata strips and nested tracking. Exclude red annotations and capture edges. Presets reproduce inconsistent screenshot history/status independently; no inferred policy.
Use actual resident theme/native contracts after inspection. Screen-specific scoped CSS exception is proposed because only referenced themes are listed; never edit shared/vendor theme.
Viewport checks: 1440x900, 768x1024, 390x844 at 100%; desktop 200% zoom. Initial visual calibration 960x720, panel approximately 892 CSS px; original zoom/DPR/font unknown, disclose comparison scaling.
AR01 Screen/Block responsibilities and explicit simulation transitions are adopted, with this bounded implementation adjustment: twelve fixed typed year locals (COR/PEL x 2024–2029) and six Boolean coverage fields replace mutable year/coverage lists. This preserves keyed isolation without extra business dependencies. Per-row backup/draft state must survive tab switching; Cancel restores only the target row. Preset selection resets all prototype state.
New Screen WHTDocumentsPrototype belongs to TestComponent; six feature Blocks remain private. Registered access follows current ExportRequest/TestDuplicate role readback; Anonymous access is not added. Existing routes/layout consumers remain untouched. Use native Upload without server calls, native mounted Popup, native Button/Link and resident Tag where suitable. Unboxed disclosure/tab variants retain native semantics and classes; deterministic preset control is the reason for scoped native disclosure presentation rather than stateful AccordionItem (StartsExpanded only).
Current read-only Model API probes confirm WHT_Theme_Fabric -> OutSystemsUI, inherited Manrope, primary #1068EB; base stylesheet header identifies OutSystems UI 2.20.0. Reference version/revision fields are blank, so theme evidence is explicitly the stylesheet header, not a platform package-version claim. Full source excerpts are evidence/theme-contract.txt and evidence/base-theme-contract.txt. Screen-owned scoped CSS is approved for this feature because both themes are references. It must reuse observed tokens and preserve native classes. Served CSS verification is mandatory after manual publish.

## Target, baseline and authority
Observed live WHT_Request, Reactive, key 50e8e182-1c94-4c32-bf3b-f4e609f48bda. Service Studio UI: Development - personal-g4et6y1o.outsystemscloud.com. listApps version 0 is not published version.
MCP current-view baseline: 0 errors/72 warnings, full identities in evidence/validation-baseline.json. Themes listed OutSystemsUI and WHT_Theme_Fabric, both references. User confirmed Manual review and no concurrent module edits in this conversation.
Checkpoint/pending session: startOmlEditSession returned started:true; durable prewrite copy checkpoints/WHT_Request-prewrite.oml SHA256 A285C8072568F619410DF540EE8061214A2B078E518303AF028AE40352CF67AB. Only one host input OML was present at copy time; no saved mutation yet. Read-only throw probes returned empty mutatedOmlPath. Restore itself NOT_RUN. Primary local operator owns all MCP calls.
Installed skill .agents/skills/servicestudio-mcp-oml, no upgrade. Publishing disabled in active catalog; do not enable.

## Checks and execution
R01 discovery -> representative V01/022146 -> V02,V03,V04 -> remaining V05–V12 -> independent proposal/readback review -> manual merge + accepted-live readback -> user DEV publish -> identified-version runtime/visual QA.
Check file selection/removal, Clear/Cancel/Submit, year selection, COR/PEL isolation, nested expansion, reminder/review simulation, dialog lifecycle/focus, keyboard and responsive behavior. Full cases in A01/D01.
No backend operations added, so transaction/migration tests N/A; screen access and no accidental backend invocation still require verification.
Before each slice inspect guards/contracts. After each slice readback and exact validation delta; preserve existing warning identities. Unknown write outcome requires inspection, never blind repeat.

## Progress reference and preserved constraints
Current stage, completed checks and remaining actions are maintained in the [report](report.md) and [task state](task-state.json). Do not replay completed merge/readback based on superseded progress text in this spec. Existing Request_COR_PELetter is rejected for reuse because inspected code performs server aggregates/download/delete/upload transactions (evidence/existing-cor-block.json). Do not alter its existing consumers. Publication and runtime QA remain later-stage dependencies, not permission to lower the target.
