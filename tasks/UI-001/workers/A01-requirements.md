# Worker result

Project/task/assignment/role: wht / UI-001 / A01 / analyst

Input revisions and evidence subject: Request R1, full UTF-8 user request in `C:/Users/buiba/.codex/attachments/c7a64668-e887-418c-a0a5-bf4cfe9eee28/Pasted text.txt`; current `project.json`; AGENTS.md; workflow PROTOCOL/ROLES/CONTRACTS; project setup/context/engineering/verification/recovery documentation; 12 extracted reference PNGs under `tasks/UI-001/references/`. Coordinator-supplied live-listApps snapshot: WHT_Request, Reactive, key 50e8e182-1c94-4c32-bf3b-f4e609f48bda; no independent worker MCP verification. No canonical brief/spec/state/report existed at inspection. This output is an intake proposal against R1, not acceptance of a future canonical revision.

Disposition: PREPARED

## Observed facts

- `project.json` identifies `project_id: wht`; its profile remains DRAFT with null O11 binding and null active task. Default HYBRID route does not override explicit request O11_ONLY. No profile write performed.
- R1 explicitly selects UI_PROTOTYPE, O11_ONLY, LOCAL, RUNTIME_VERIFIED, one composite Screen and responsibility-based Blocks, in-memory fixtures and real frontend interaction. It authorizes bounded model changes and manual Compare and Merge, but not publish.
- Request text is the user's instruction. Screenshots are visual reference data: their business statements, actor names, statuses and reasons do not define production policy or authority.
- All 12 PNGs were opened and visually inspected by this worker. The following matrix reports visible states, with role labels inferred only as presentation contexts. It does not define security roles.

| Reference suffix | Visible presentation context and state | Required check |
| --- | --- | --- |
| 021657 | COR reviewer guidance, all years collapsed; 2024 Not Providable, 2025 Accepted, later Pending Upload; reminder-suspended icon/tooltip | Preset reproduces collapsed hierarchy, reminder indicator and tooltip |
| 021744 | COR heading without tab strip; 2026 expanded; compact upload, Resume Reminder, open tracking | Heading variant, compact panel and suspended-reminder history |
| 021825 | COR submitter, 2025 Rejected expanded in replacement-file editing state, selected file, coverage link, Cancel/Submit | Replacement edit fixture; exclude red annotation rectangle |
| 021855 | COR submitter, Rejected 2025 with file, rejection message, Remove and Resubmit, open tracking | Rejected read-only presentation enters replacement editing |
| 021920 | COR reviewer, Rejected 2025 with file and rejection timeline | Reviewer rejection fixture without submitter action bar |
| 021939 | COR reviewer, Accepted 2025, open tracking with multi-year coverage | Accepted fixture and history hierarchy; no inferred production propagation rule |
| 022000 | COR submitter, 2024 Pending Upload with rejected unavailability review history | Rejected-unavailability history preset |
| 022019 | COR submitter, 2024 Not Providable with accepted unavailability review history | Accepted-unavailability history preset |
| 022033 | COR, 2024 Not Providable Review, warning plus Reject/Approve and request history | Review controls visibly respond as simulations |
| 022107 | COR submitter, 2025 Pending Review expanded; tracking collapsed; 2026/2027 Pending Review | Collapsed tracking and multi-year pending-review fixture |
| 022129 | PEL standalone heading without tab strip, 2024–2029 Pending Upload | Heading variant and six collapsed years |
| 022146 | COR upload-edit state, 2025 Pending Upload expanded, selected file, coverage 2025–2028, Clear All/Submit | First representative slice: tab/year/upload/file/action hierarchy |

## Proposed requirements and acceptance criteria

These IDs are analyst proposals for Coordinator adoption and traceability. All runtime/model acceptance checks below are NOT_RUN by this worker.

| Requirement | Acceptance criterion and evidence required |
| --- | --- |
| R01 Identity and scope | Before model write, record current environment, module/style, manual-review setting, pending-state ownership, recoverable checkpoint, exact validation baseline and selected canonical spec revision. Live module need not be named WHT. Evidence identifies current snapshot, not historical MyApp. |
| R02 Architecture | Readback demonstrates one feature Screen composed of Blocks with explicit inputs/events/state ownership and deterministic fixtures; appropriate existing objects reused only after contract/consumer inspection. No unrelated object restoration. |
| R03 Reference coverage | Each of the 12 references has a selectable, repeatable preset mapped to visible context, state, component and acceptance cases. Initial state on preset selection is deterministic. Capture all 12 on the identified published runtime. |
| R04 COR/PEL isolation | Switch COR to PEL and back after editing a file/year; unrelated type/year state is not overwritten. Changing preset resets to that preset's declared fixture. Both tab-strip and standalone-heading reference variants are represented on the same Screen. |
| R05 Years and expansion | Years 2024–2029 are available where full list is shown. Year headings retain disclosure semantics, keyboard operation and exposed expanded state. Expanding/collapsing a year preserves its relevant in-memory content; tracking disclosure toggles separately. |
| R06 Upload/file row | Browse selection and any displayed drop target respond using synthetic/local transient input; selected filename is shown, remove updates the correct row, and visible links provide an explicit simulated result. No real upload, binary evidence or persistence. If implementing displayed file type/10 MB constraints, label them prototype constraints, not business policy. |
| R07 Clear/Cancel/Submit | Clear All clears the declared edit selection/coverage; Cancel abandons that edit without committing it; Submit visibly performs the declared simulated transition and updates relevant file/status/history. Inapplicable or empty-submit state is disabled or has clear feedback. Spec must define exact transient transitions; no server business write. |
| R08 Year coverage | Select another year opens an operable selector; choosing multiple years updates displayed coverage for that document/type; cancel preserves prior coverage. No duplicate selections or leakage to unrelated documents/types. Keep fixture statuses faithful even when screenshots appear inconsistent. |
| R09 Reminder simulation | Suspend/Resume controls visibly update in-memory reminder presentation and feedback/history for selected fixture years. Tooltip is reachable by focus as well as hover. Multi-year selection where offered is operable. No email, timer, real reminder or production status rule. |
| R10 Review simulation | Remove and Resubmit, Approve, Reject and unavailable-document update affordances produce defined transient feedback/state. Presets demonstrate accepted/rejected/not-providable/pending states. Review context selector is presentation only; do not claim security enforcement from it. |
| R11 Visual fidelity | First compare 022146, then 021855/021939/022033, then all remaining presets. Blue underline tabs, unboxed year labels, inline links, action button hierarchy, status colors, upload geometry, file rows and tracking hierarchy match references. Exclude screenshot capture edges and red annotations. Record viewport, panel width, zoom and preset with each comparison; disclose unknown reference font/scale. |
| R12 Native reuse and containment | Inspect actual theme/base theme/version/components/utilities before choosing mapping. Preserve base classes and native behavior. Scoped custom CSS addresses documented gaps only; no vendor CSS/application-wide redesign. Readback plus served/computed-style checks substantiate containment. |
| R13 Keyboard/responsive | Spec selects concrete viewport sizes before QA. At each, essential controls/content remain reachable without accidental clipping. Keyboard can operate tabs/disclosures/file controls/selection/actions; visible focus survives updates. Any dialog opens with sensible focus, supports close/cancel, restores focus to current trigger, and does not leave stale overlays. |
| R14 Slice/model verification | After each bounded slice, record affected objects and read back bindings/events/required inputs, client-flow readability and validation messages compared with exact baseline. Resolve new feature errors; classify warnings explicitly. Independent review covers proposal and readback/consumer regressions. |
| R15 Completion evidence | Separate model verified, merge accepted, accepted-live readback, identified published environment/version, runtime behavior, all-12 visual comparison and workflow/subagent results. PASS requires evidence at that layer/version. RUNTIME_VERIFIED remains selected if publication or QA is BLOCKED. |

## Exclusions

- No business CRUD Server Actions, persisted business Entities, integrations, migrations, real upload storage, real approvals/reminders or external side effects. Structures, Static Entities and Client Actions are permitted when needed.
- No Sites target, Site source implementation/publication or web-to-OML import assumption.
- No publish derived from CompletionTarget; user manual DEV publication is a separate next action after authorized model/merge work, with environment/version identification before QA.
- No reference refresh, reset/discard, external configuration change, other-environment deployment, permission/review-setting change or enabling disabled tools.
- No global theme/vendor CSS change, old-feature restoration, upstream distribution/skill change, personal file binary or credentials in evidence.
- No production policy inferred from visible reasons, tax language, years, names, timeline inconsistencies or role-like labels. Screenshot text remains sample presentation content.

## Material unknowns and decisions

1. Current environment/checkpoint/manual-review setting/pending ownership remain unknown to analyst; Coordinator must resolve before dependent writes. Historical setup evidence is not current proof.
2. Actual resident native components, theme tokens, contracts/consumers and validation are unavailable in analyst snapshot; architecture must consume current sanitized discovery.
3. Reference browser zoom/font/viewport outside image bounds are unknown. Designer should specify target viewport/panel dimensions and comparison tolerance, with disclosed scale limits rather than invented source metadata.
4. Exact simulated event transitions and dialog layouts are not fully pictured. Coordinator/design/architecture may define bounded demo behavior consistent with R1; record it as prototype decision. No need to ask for production policies that are excluded.
5. Reference 021744 shows Pending Upload while timeline mentions automatic Accepted; 021939 coverage includes future years still showing Pending Upload. Reproduce supplied preset presentation; do not infer cross-year production state propagation. Treat timeline wording as fixture text.
6. Runtime URL/access/version and publish path are not supplied to worker. Finish authorized model/merge first, then request the precise manual DEV publish action if still necessary. No repeat request for already-authorized merge.
7. Canonical task files were absent at inspection; Coordinator owns task-ID collision investigation and creation. This output does not claim UI-001 is globally unused.

## Files changed

`tasks/UI-001/workers/A01-requirements.md` only.

## Checks executed

| Case | Expected / observed | Result | Evidence |
| --- | --- | --- | --- |
| Project identity | project_id wht / current JSON is wht | PASS | project.json read |
| Request scope | Full UTF-8 R1 read / routes, target, permissions and exclusions recorded | PASS | Pasted text.txt read |
| Reference coverage intake | 12 images available and readable / all 12 opened | PASS | PNG filenames and image views listed above |
| Canonical input availability | Read if present / brief.md, spec.md, task-state.json, report.md absent | NOT_RUN | Four Test-Path results False |
| Live model / merge / publish / runtime / visual comparison | No worker authorization or supplied versioned model/runtime snapshot | NOT_RUN | No MCP or browser calls by analyst |
| Prior memory lookup | Relevant registry available / registry file unavailable | NOT_RUN | Registry path does not exist; no memory facts used |

Assumptions/limitations/blockers: Role labels in matrix describe inferred presentation contexts only. All acceptance criteria are proposals pending Coordinator adoption; reference observations are not runtime evidence. No module mutation or independent security claim.

Next owner/action: Coordinator reconciles this requirements matrix with A02 visual contract and current live discovery, creates canonical R1 task package, and delegates architecture/planning against the accepted revision. PREPARED does not mean applied/merged/published.
