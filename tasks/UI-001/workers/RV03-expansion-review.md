# Worker result

Project/task/assignment/role: wht / UI-001 / RV03 / reviewer.
Input revisions and evidence subject: request/reference R1, spec0.2, exact B01 pending-model readbacks reviewed in RV02; B02 source/fixtures/styles and apply contract/result. Current canonical identity checked: wht/UI-001/LOCAL/O11_ONLY/spec0.2. This is proposal review only. Latest builder freeze 344014E93609E69B5809BC0C81F15DDD9AFA6619E2968024CD74BA98D47AE97E independently hashed; includes corrected Checkbox expression escaping and latest compact-upload/review-row composition; inspected generated source and CSS.
Disposition: FINDINGS. No remaining identified mutation/contract blocker for bounded primary compilation and readback. Not full visual/runtime acceptance.

## Remaining severity-ranked findings and evidence gaps

1. P2 runtime evidence gap: Popup Escape, Tab containment, initial focus and fallback focus now have explicit scoped JS, but native Popup DOM timing/portal behavior and render event order are untested. In particular the stable DialogHost stores __whtOpen before looking for Popup DOM. If OnRender precedes native Popup DOM creation, initial focus may not be retried when DOM appears. This is a conditional risk, not a reproduced defect. Test repeated open/close, Cancel/Escape/Confirm, each dialog kind, owner controls removed after review, tab/fixture switches, and no stale overlay/listener. No runtime PASS from source review.

## Corrected during review and source verification

- Final freeze places compact Upload and Resume Reminder in the same wht-upload-row flex container; noncompact resume stays in separate footer. Warning/callout and review/resubmit controls share wht-review-row with responsive wrapping. Prior021744 source composition finding is resolved; rendered alignment remains NOT_RUN.

- Removed unconditional WasOpen model assignment from OnRender. New DialogHost DOM property tracks open transitions; no model assignment or extra action event is scheduled by render. Earlier potential rerender-loop concern is removed at source level; no actual loop had been reproduced.
- Approve/Reject confirmation hides ShowReview and removes its trigger. Focus restore now searches exact semantic trigger, then surviving data-wht-year disclosure using explicit FallbackKey. All dialog instances supply the new required input; header dialog supplies empty fallback because its trigger remains mounted.
- 021825 numeric coverage is hidden initially via DisplayCoverageYears=False, and coverage booleans select only2025. 022146 displays2025-2028. Explicit Coverage confirmation reveals selected years; Clear hides list/restores owner-year only. Display flag participates in Cancel backup.
- Empty reminder selection now says No years selected; no changes made. The same per-row match predicate prevents all state/history changes in this case.
- Tooltip Escape sets scoped data-dismissed; CSS hides tooltip despite hover/focus. Focus reentry or mouse reentry re-enables it. No global event listener or style injection added.
-021744 timeline implementation commentary replaced with synthetic event detail; inconsistency explanation belongs in report.
- Latest six Checkbox SetEnabled Coverage string expressions are correctly escaped in C# source. Compiler validation still belongs to primary.

## Executed source/data checks

| Check | Result / evidence |
| --- | --- |
| Fixture count/identity | PASS: parsed B02-fixtures.json contains exactly12 presets, each12 distinct COR/PEL2024-2029 records |
| Full12 composition flags | PASS by matrix comparison: representative, rejected/reviewer, accepted, unavailability review/history, collapsed reminder, compact upload, replacement edit, pending-review collapsed tracking and standalone PEL match adopted D01 status/expanded/show flags; runtime pixels NOT_RUN |
| Backup consistency | PASS: every Backup* field in021825.COR2025 equals corresponding021855.COR2025 field; zero mismatches. BeginResubmit snapshots same declared fields; Cancel restores them plus reset increment/feedback; backups live in Screen record across tab switches |
| Submit propagation | PASS by source inspection: owning record commits metadata/status/history; selected same-type coverage records receive Pending Review only; transient Submitted command cleared by screen handler; other document type untouched |
| Empty submit | PASS by source inspection: missing file does not set Submitted or Pending Review; gives explicit feedback; no backend operation |
| Reminder/review/unavailability | PASS by source inspection: match predicates constrain type/year; reminder no-choice no-op explicit; Approve/Reject Not Providable Review maps Not Providable/Pending Upload; simulated events only |
| Native controls/events | PASS by source inspection: native Upload/Popup/Checkbox/TextArea/Button/Link/Icon, resident Tag; all newly added dialog/header/upload inputs and forwarded event parameters bound |
| Key guards/deletion boundary | PASS by source inspection: seven supplied B01 UI keys checked before deletion; PrototypeYear checks21 original attribute names/types and unexpanded state; only seven feature objects children rebuilt, top-level UI keys/roles/positions preserved. No external consumer live query performed by reviewer; primary owns that evidence |
| Structure scope | PASS by source inspection: extend existing PrototypeYear; no Delete of structure or business entity. Guard uses exact schema rather than a supplied Structure key, which was not in worker input |
| Security/transient boundary | PASS by source inspection: no server action/aggregate, persistence, network/storage operation, dependency addition, role widening or shared theme change; Registered access inherited unchanged from B01. Presentation reviewer flags are not access control |
| Scoped JS | PASS by source inspection: only own host/header/year DOM listeners and unique semantic focus lookup; no DOM-built UI or injected styles. Browser behavior NOT_RUN |
| Layout | PASS by source inspection: full BFS over rebuilt actions with unreachable guard and explicit positions; existing UI flow positions unchanged |
| Compile/validation/readback/merge/publish/runtime | NOT_RUN in this review; no worker MCP or browser calls |

## Frozen source hashes

- B02-expansion.cs: `344014e93609e69b5809bc0c81f15ddd9afa6619e2968024cd74ba98d47ae97e`
- B02-generate.py: `f400b3ac9358a8e7bfe166e43bdd5c202a238fb7e2558bdc450886600aabb512`
- B02-fixtures.json: `bef0b22a42b637fe208baf584164e227648ee63e30c03396cec16513a48f41d2`
- B02-styles.css: `9729fcd5dc6da582fa5788db44ff7ef63b0f6ea5cc85b062359f3cb8a5b87069`

Files changed: tasks/UI-001/workers/RV03-expansion-review.md only. No source/canonical edits, live operations or subagents. B02 metadata may be updated by builder after source freeze; source hashes above delimit this review.
Next owner/action: primary runs bounded preview, resolves actual errors, saves/readbacks after review, and returns exact snapshots for independent pending-model review. Builder/Coordinator retain runtime calibration checks for corrected composition. QA verifies all12 visual states and dialog/access/responsive behavior only against an identified published runtime. RUNTIME_VERIFIED remains outstanding.

## RV03 preview-warning follow-up

B02-preview.json SHA2566981fe2cc0921575f9c985c095c44fe54fd1342a84c4fb550755ee6fd6f1e522 was inspected: intentional PREVIEW exception, no saved output, zero errors/77 warnings. Two new semantic warnings versus B01 are JSNodeTooLarge on PrototypeDocumentHeader/KeyboardDocumentSelection/ScopedBehavior and PrototypeYearCard/ReminderTooltipLifecycle/ScopedBehavior. Full-field diff also replaces ResetVersion UnusedElement ownerKey because that input is rebuilt; the same ownerPath/rule remains, not a third new semantic warning.

Classification: accepted bounded maintainability/performance heuristics for this proposal, not implementation blockers. Independently inspected source payloads are604 and661 characters respectively: local event delegation for document-selector navigation and tooltip dismissal, not embedded external libraries. Both guard initialization on the owned DOM root; no network/storage, generated UI, model writes in OnRender, unbounded loops or repeated listener installation on the same root. No reason to mutate solely to silence the warnings or introduce a Script dependency. Runtime repeated render/remount/listener behavior and keyboard/access checks remain NOT_RUN; this classification is not a performance/runtime PASS.
