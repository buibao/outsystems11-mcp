# Worker result

Project/task/assignment/role: `wht / UI-001 / AR01 / architect`

Input revisions and evidence subject: request R1 (full pasted request); A01-requirements.md R1; D01-visual.md R1; current project.json; tasks/UI-001/evidence/data-model.json; Coordinator supplied operator snapshot for WHT_Request Reactive, key 50e8e182-1c94-4c32-bf3b-f4e609f48bda, Development personal-g4et6y1o.outsystemscloud.com, 0 errors/72 baseline warnings. User confirmed manual review and no parallel module editing. This worker did not independently execute MCP. Canonical task-state/brief/spec/report were absent at initial read; no canonical revision is invented. Project profile is DRAFT with project_id wht; request selects O11_ONLY / LOCAL / RUNTIME_VERIFIED.

Disposition: **PREPARED**

## Observed facts and boundary

The supplied data-model snapshot contains referenced WHT business entity signatures and native OutSystemsUI static signatures, including Color, Size, Shape and accordion configuration; it is not a component, action-consumer or theme-CSS snapshot. Operator reports references OutSystemsUI, WHT_TH_Fabric, WHT_CW, STTheme, ReactFilePondUpload_CW, MultipleFileUploadReactive_Lib and backend modules, with referenced themes OutSystemsUI and WHT_Theme_Fabric and no local theme. Resident modules do not prove individual Block availability or safe behavior. Never execute the AddDependency statements in generated read output as a recreation recipe.

Read AGENTS.md, workflow ROLES/CONTRACTS/PROTOCOL, templates/WORKER_RESULT, adapter O11, project setup/context/engineering/verification/recovery and O11 execution protocol. Applied installed official servicestudio-mcp-oml contract and relevant reactive-widget-api, osui-verified-blocks, generated Upload/Popup/event/Screen signatures. Skill catalogue example version 2.27.0 is not evidence of this module's installed OSUI version. Memory lookup for WHT returned no matches; no memory facts used.

All names below are proposed feature-local names, subject to name/consumer collision checks; they do not establish a new project-wide prefix convention. No existing business objects are repurposed. No web source import, new dependency, backend action or persisted Entity is proposed.

## Screen and Block contracts

One new Screen `WHTDocumentsPrototype` in an operator-confirmed suitable local flow owns all committed synthetic state. Keep fixture toolbar and simulation notice outside the comparison panel. Do not modify default route, existing navigation, authentication or business layouts without affected-contract evidence. Prefer an existing safe layout only after its initialization and required inputs are inspected; a local plain feature root is the fallback when layout introduces backend calls.

| Proposed Block | Inputs | Events | Ownership / composition |
| --- | --- | --- | --- |
| PrototypeDocumentHeader | ActiveType Text; HeaderMode Text; DisplayContext Text | TypeSelected(DocumentType Text); SpecimenRequested(DocumentType Text); ReminderRequested(DocumentType Text) | Tabs or standalone heading, instructions and specimen/reminder controls. No data fetch. |
| PrototypeYearCard | YearState PrototypeYear; Events List of PrototypeEvent | ToggleYear(Type Text, Year Integer); ToggleTracking(Type Text, Year Integer); Command(Type Text, Year Integer, Kind Text); FileSelected(Type Text, Year Integer, File PrototypeFile) | Composes native year disclosure, status, upload/file/coverage/tracking/action regions from explicit flags, not status-only guesses. Forwards child events with original Type/Year. |
| PrototypeUpload | Type Text; Year Integer; Mode Text; ResetVersion Integer | Selected(Type Text, Year Integer, File PrototypeFile); InvalidSelection(Message Text) | Owns only temporary native Upload FileContent Binary Data and FileName Text; never passes binary upward or persists it. Large and compact modes. Clear local content after metadata extraction where safe; ResetVersion changes clear widget-local selection. |
| PrototypeFileRow | File PrototypeFile; CanRemove Boolean; Type Text; Year Integer | RemoveRequested(Type Text, Year Integer); OpenRequested(Type Text, Year Integer) | Read-only metadata row and optional remove action. Safe simulated open feedback, no business download action. |
| PrototypeTracking | IsExpanded Boolean; Events List of PrototypeEvent; Type Text; Year Integer | Toggle(Type Text, Year Integer) | Nested disclosure and event list; no parent-toggle bubbling. |
| PrototypeDialogs | IsOpen Boolean; Kind Text; Type Text; Year Integer; Choices List of PrototypeYearChoice; Reason Text; FocusKey Text | Confirm(Kind Text, Type Text, Year Integer, Choices List of PrototypeYearChoice, Reason Text); Cancel() | Permanently mounted native Popup; local draft choices/reason initialized on open/revision, never overwritten on each render. Native checkbox/input and explicit cancel/confirm. |

Six responsibility-based Blocks plus one Screen are sufficient initially. Keep review/reminder actions inside YearCard/Header and common dialog to avoid a Block for each button. Add a separate status Block only if multiple consumers justify it. All required inputs/events must be wired on every instance; handler input values must be set, not merely event destinations.

## Typed transient structures

Use local Structures (no production identifier types) with these proposed fields; list types are OutSystems typed Structure lists, not JSON strings.

- `PrototypeFile`: Name Text, Extension Text, SizeBytes Long Integer, HasFile Boolean, IsSynthetic Boolean. No URL or Binary field.
- `PrototypeYearChoice`: Year Integer, Selected Boolean, Enabled Boolean.
- `PrototypeEvent`: EventKey Text, DocumentType Text, Year Integer, Sequence Integer, Tone Text, Title Text, Detail Text, DisplayDate Text, ActorLabel Text. Dates/actors are synthetic display text; do not infer production chronology.
- `PrototypeYear`: DocumentType Text, Year Integer, StatusCode Text, IsExpanded Boolean, IsTrackingExpanded Boolean, ReminderSuspended Boolean, PresentationMode Text, ShowUpload Boolean, ShowFile Boolean, ShowCoverage Boolean, ShowReview Boolean, ShowResubmit Boolean, ShowHistory Boolean, IsEditing Boolean, File PrototypeFile, Coverage List of PrototypeYearChoice, Callout Text. Nested list type feasibility must be validated in first structure slice; if awkward in model API, keep Coverage in a separate typed screen list keyed by Type/Year rather than introducing JSON transport.
- `PrototypePreset`: Id Text (reference suffix), Label Text, ActiveType Text, HeaderMode Text, DisplayContext Text.

Screen locals: Presets list; SelectedPreset Text; ActiveType Text; Years List of PrototypeYear; Timeline List of PrototypeEvent; EditBackup PrototypeYear; EditBackupValid Boolean; dialog target/choices/reason/open state; Feedback Text; ResetVersion Integer. A single active edit is a bounded prototype choice; switching Type preserves committed rows and cancels or explicitly preserves that edit by recorded decision, never silently overwrites unrelated rows. Prefer preserving the draft in its Year record, with backup keyed to Type/Year; if multiple simultaneous drafts are allowed, use a typed backup list. Keys are `(DocumentType, Year)`, with event sequence/key scoped to that pair. Never address rows solely by visible index after switching types.

Codes are constrained constants documented in fixture initializer/client actions: type COR/PEL; status PendingUpload/PendingReview/Accepted/Rejected/NotProvidable/NotProvidableReview; header Tabs/Standalone; presentation context Submitter/Reviewer/UnavailabilityReview; upload mode Large/Compact/None. These are presentation codes, not production policy or authorization. Structures suffice; Static Entities are optional and must not reuse production status IDs merely because labels match.

## Client state and action strategy

All actions are local Screen/Block Client Actions. Use native Assign, If, For Each and resident client list operations only after actual API signatures are confirmed. Initialize deterministic fixtures in one feature-local client action or Screen OnInitialize; no Aggregate, Data Action, server call, local storage, session/client persistence, fetch or integration. Keep flows visually arranged and bounded.

1. `LoadPreset(Id)` initializes 12 typed COR/PEL year rows and their fixture timeline; applies A01/D01 V01-V12 flags exactly. Header variant, role presentation, status and content flags are independent. Resets open dialogs/upload-local state and stale drafts. Default 022146. Fixture selection is reproducible and intentionally resets the prototype dataset.
2. `SelectType(Type)` changes visible rows without rebuilding Years. `ToggleYear` and `ToggleTracking` update only their keyed Boolean. Keep component inputs stable across unrelated updates.
3. `SelectFile(Type,Year,Metadata)` replaces draft metadata only for target row, sets HasFile and visible feedback. Native Upload accepts actual local file selection; discard content without network transmission. Synthetic fixture selection may supplement but not replace operable Browse. If a drop target is advertised, implement and verify local drop or avoid drop wording/affordance. Extension and 10 MB validation are explicit demo constraints, not backend enforcement.
4. `BeginResubmit` copies current row into a keyed backup, exposes large upload, keeps Rejected badge during editing (021825). `ClearAll` clears draft file and restores coverage to owning year only. `CancelEdit` restores backup exactly, including status/file/coverage; clear native upload selection using ResetVersion. `Submit` guards HasFile and valid coverage; commits target row and selected coverage rows as PendingReview for this declared simulated action, closes editing, appends synthetic upload history and feedback. Preset loading remains faithful even where screenshot future-year statuses differ; no automatic reconciliation of preset history.
5. `OpenCoverage` clones draft choices into dialog-local state. Target year is selected/disabled; other 2024-2029 choices are unique and selectable. Confirm updates only target draft; Cancel changes nothing. Do not share dialog draft list references accidentally.
6. `OpenReminder` presents same-document year choices. Confirm sets suspension flags for selected years and appends synthetic reminder events; Resume clears target flag and appends feedback/history. No timers, email or backend reminder service. Tooltip uses focus/hover accessible association.
7. `ReviewApprove` transitions NotProvidableReview to NotProvidable; `ReviewReject` transitions it to PendingUpload with rejected-unavailability history. Other document review fixtures may use Accepted/Rejected demo transitions only where a control is shown. Dialog reason is transient text, not an inferred mandatory business field. `OpenFile` and `DownloadSpecimen` explicitly announce simulated download; no dead anchors or actual confidential file access.
8. `CloseDialog` restores focus to the current trigger located by stable semantic key; do not retain detached DOM nodes across rerenders. Mount Popup outside conditionally removed Year content; toggle ShowPopup. Native focus behavior must be runtime verified, with small scoped behavior script only if needed and after API inspection. Never inject styles or build an independent JS UI tree.

## Native reuse and CSS mapping

| Visual responsibility | First reuse candidate | Bounded fallback / remaining gap |
| --- | --- | --- |
| COR/PEL underline tabs | Existing pure project tabs, then resident OSUI Tabs/TabsHeaderItem/TabsContentItem | Native buttons with tab semantics/keyboard behavior only if resident component unsuitable; no primary-button tab styling. Confirm actual pattern callbacks/active item binding. |
| Year/tracking disclosure | Pure project disclosure, then OSUI Accordion/AccordionItem | Native unboxed disclosure Button with aria-expanded/controls plus conditional region; retain native base classes and narrowly scoped variant. Needed if pattern cannot externally control all fixture states. |
| Status pills | Project status component with no business fetch, then OSUI Content/Tag | Pass supported color/light/size parameters; scoped density only. Snapshot must prove resident Tag, inputs and placeholder. |
| Upload | Pure project upload ONLY with read contract proving no actual upload/server execution | Native IUpload local Binary/FileName bindings, large/compact scoped layout. Existing upload references are not sufficient proof. |
| File actions and footer | Native Link/Button and existing modifiers | Preserve btn/btn-primary etc where applicable; inline Link for Browse/year/file names, neutral year trigger, outlined reject/cancel; no blanket styling. |
| Dialog/choices | Native Popup/Checkbox/Input | No replacement dialog framework. Verify lifecycle and keyboard behavior. |
| Timeline/reminder indicator | Existing pure project timeline/tooltip, then resident OSUI pattern | Scoped list/containers for dotted guide and native icon+accessible tooltip where native pattern does not match density. |

Theme exception: inherited theme appears referenced and must not be changed. Place shared feature-scoped overrides once in the new Screen stylesheet under `.wht-ui001` root, with a separate explicit feature popup root class if native Popup portals outside that root. This is an explicit exception to application-theme placement because there is no reported owned theme and no global change is authorized. Reuse actual inherited font/color/spacing/border variables once read; do not copy catalogue token values as live facts. No inline CSS, generated-ID selectors, blanket !important or vendor edits. Examine grid margins before adding gaps. Native classes remain intact.

Installed skill warns modifications to nonempty Screen/Block CSS can be accepted live but serve stale CSS after publish. Initial empty Screen CSS is the best bounded placement available; later changes require served-CSS/hash and computed-style verification on identified published version. Do not invent a reset/publish workaround. If stale, prepare exact CSS for user's normal editor/manual publication while preserving task scope.

## Security and dependency contract

The feature never invokes protected business operations; therefore new server authorization action is N/A, not a reason to add fake client authorization. DisplayContext is presentation only. Preserve existing page access policy based on a relevant safe local Screen snapshot; do not add Anonymous access or alter shared role mappings without a concrete decision. Authenticated allowed and unauthenticated/denied page access checks remain required where applicable. Model and runtime network inspection must confirm no new business calls, writes, upload endpoints or external sends.

Read any reused Block lifecycle actions and nested consumers for side effects before adoption. Leave WHT backend/entity references unused. Existing FileMetadata and business TaxDocumentType signatures are not appropriate transient prototype storage. No reference addition/refresh authorized.

## Missing evidence and API risks

- Before builder finalization, operator needs bounded snapshot: candidate flow/screens/roles and collision inventory; actual project layout/tab/accordion/tag/tooltip Block signatures and initialization/consumer behavior; actual theme/base chain and relevant token/class excerpts/version; checkpoint and pending state. No worker claim of live native feasibility is made before this arrives.
- Generated API supports IMobileFlow.CreateBlock, IUpload.SetFileContent/SetFileName and OnChange, native Popup.SetShowPopup, IBlock.CreateEvent and instance EventHandlers. Builder must inspect exact trigger-event node type, event input/handler binding methods and actual required parameters. Destination-only wiring can leave required arguments invalid.
- Use screen.ScreenActions, fully-qualified NRWidgets.IExpression, typed IList/If/Block interfaces. Avoid dynamic, reflection, Func factories returning model objects, recursively walking leaf Widgets, fetched attribute special getters and referenced static Records enumeration. Block margins use scoped classes rather than crash-prone setters or prohibited inline-style workaround.
- Read actual names after creation (silent suffixes), clear only default children of newly created widgets where needed, assert collision/identity guards and input types. Preserve existing objects and consumers.
- Representative slice should prove 022146 native upload, event forwarding, typed lists, reset and Popup lifecycle before broad fixture expansion. Then 021855, 021939, 022033; finally remaining eight variants. Model validation is insufficient for upload/drop/access/focus/CSS behavior.

## Checks executed

| Case | Expected / observed | Result / evidence |
| --- | --- | --- |
| Project identity | wht / project.json wht | PASS, direct file read |
| R1 scope alignment | One Screen, Blocks, transient data, 12 presets, O11_ONLY / mapped above | PASS for proposal traceability only; request + A01/D01 reads |
| API availability in installed docs | Native upload/popup/event/structure interfaces / signatures present | PASS for documentation presence only; generated API files |
| Current component/theme feasibility | Live candidate signatures/token/version/consumers / absent from supplied snapshot | BLOCKED for final reuse selection; data-model.json is entity signatures only |
| Model / merge / published runtime / visual comparison | Worker has no live authority or published version / not performed | NOT_RUN |

Files changed: `tasks/UI-001/workers/AR01-architecture.md` only.

Assumptions/limitations/blockers: This is a bounded architecture proposal against request/A01/D01 R1, not accepted canonical spec. The state transition choices above are explicit simulation design decisions for Coordinator reconciliation. Screen access and actual component contracts remain unresolved; checkpoint evidence must be handled by operator before material writes. No MCP/session operation, upstream edit, canonical change or subagent spawn performed.

Next owner/action: Coordinator reconciles architecture with canonical R1 and supplies sanitized component/theme/access snapshot; planner sequences guarded structure/representative UI/event slices; builder validates exact event APIs and returns bounded lambdas. Primary operator alone applies/readbacks/merges; QA waits for identified published version. **PREPARED does not mean applied, merged, published or runtime verified.**
