# Worker result

Project/task/assignment/role: wht / UI-001 / RV01 / reviewer.

Input revisions and evidence subject: request R1, reference R1, spec 0.2; A01/D01/AR01 contracts; project.json and canonical task package; theme-contract.txt/base-theme-contract.txt; installed O11 skill and typed widget contracts. Proposal only, no pending/live readback supplied. Frozen B01-representative.cs SHA256 **C5B8AEE9A1CFB2AA3FB56478F3C4E017E73ADD45D06B1C27BA5FA8A642397CA8**; generate_b01.py **7E34AE6FAE17ABE075DE912BF31C696B86E1275184995D3B763E317F7A946D5E**; B01-styles.css **AA0C085DA3993184E6CB3C6D45633346451A2B924AAD03BE4CB758E7B32FBE3F**. Builder explicitly froze this version; hashes independently read.

Disposition: FINDINGS. Suitable for primary operator's bounded compilation/model checks, not representative runtime/visual acceptance or merge of the complete feature.

## Severity-ranked findings and evidence gaps

1. **P2 representative accessibility evidence gap: coverage Popup Escape and focus lifecycle are unproven.** B01 cs142-162 initializes the draft and mounts native Popup; cs365-384 opens/closes through Boolean assignments. No explicit Escape handler, stable trigger key or focus restoration exists. Native behavior may supply some of this, so this is not a claimed reproduced runtime defect. Reproduce on identified runtime: keyboard open Select another year, check initial focus/containment, toggle choices, Escape, reopen, Cancel, Confirm, and verify focus returns to the current invoking control each time. D01 accessibility contract and AR01 transition 8 require those outcomes. Keep R13/representative lifecycle NOT_RUN until evidence; add bounded native/scoped behavior only if actual native behavior fails. This gap does not prohibit compilation/readback work.

2. **P2 representative visual mismatch remains in the upload/file region.** generate_b01.py93-101 creates literal Attach a document, native Browse with no inline styling, no centered upload paperclip, and a text Remove button. Reference 022146 and D01 require centered paperclip/inline Browse and compact trailing remove affordance. Source inspection proves the missing upload icon and text Remove variant; actual native Browse appearance and geometry are UNKNOWN until rendered. File-strip success check follows filename directly while margin-left:auto is on Remove, so it is not aligned to the strip's trailing success position in the reference. Correct/calibrate these before V01 visual acceptance. Avoid advertising drop behavior unless implemented. This does not prevent bounded model evaluation.

3. **P3 handoff documentation drift:** B01-apply-contract.md still says binary remains local until reset/disposal and grid y=700/2200/3700. Current source releases Content immediately after Selected trigger (cs58), and computes baseY from existing flow nodes. Update these statements to current behavior before treating the apply contract as exact evidence.

## Resolved during review

- B01-preview2.json recorded unsupported IMobileFlowNode.Name. Current freeze filters collision checks to typed IMobileScreen/IMobileBlock before accessing Name (cs6). Source fix inspected; subsequent compilation remains NOT_RUN in this review.

- Primary-observed parser failure in earlier B01-preview.json corresponded to invalid double-quoted SetTitle/Popup style literals. Current freeze contains escaped expression strings. Source correction confirmed; successful compilation is NOT_RUN by reviewer.
- Instructions now have separate containers; year chevron is trailing and uses aria-expanded to change direction. Earlier fixed-down chevron near the label is corrected in source.
- Current freeze includes short-suffix guards, post-event binary release, COR reset, Document for label, and BFS layout over only newly created actions. These are source findings, not runtime PASS.

## Observed facts and checks executed

| Check | Result at proposal layer | Evidence / limits |
| --- | --- | --- |
| Identity/revisions | PASS | project_id wht, task UI-001/spec0.2, LOCAL/O11_ONLY, RUNTIME_VERIFIED retained |
| Native API shape | PASS for inspected signatures | Typed IUpload file bindings/OnChange, IPopup ShowPopup, ILabel TargetWidget match installed contracts; no live compilation claim |
| Required child inputs/events | PASS by source inspection | inst helper sets every declared feature input; Selected Name/Size, Command Kind, Changed/Confirm Value explicitly mapped through handlers; Tag inputs/placeholder guarded; model expression resolution still NOT_RUN |
| Transient boundary | PASS by source inspection | New Structure, screen locals/client actions, metadata-only file event; no server calls, persistence, aggregates, integration or dependency creation |
| Row/type ownership | PASS by source inspection | Twelve separate locals; explicit per-row handlers; only deliberate submitted coverage propagation changes same-type statuses |
| Coverage Cancel/Clear | PASS by source inspection | Dialog-local Draft; Cancel only closes; Clear restores owning-year coverage; no runtime execution |
| Guards and layout | PASS by source inspection | Exact module name/flow and collision checks; operator envelope owns key/style identity; new actions BFS reachability guarded; no existing flow repositioning |
| CSS containment | PASS by source inspection | Screen stylesheet scopes .wht-ui001 and .wht-ui001-popup; inherited theme untouched; actual theme evidence Manrope/#1068EB and base header2.20.0; served CSS/token rendering NOT_RUN |
| Reference inspection | PASS | Opened actual 022146 PNG; compared source composition to adopted D01 hierarchy |
| Compilation/validation/readback | NOT_RUN | Only earlier failed preview supplied; no current model snapshot reviewed |
| Merge/publication/runtime/visual/access | NOT_RUN | No worker MCP/browser operations, no identified runtime version |

## Later all-12 scope, not newly discovered representative defects

V02-V12 selector/fixtures, rejected edit backup and Cancel restoration, reminder/review/unavailability dialogs and tooltip, richer tracking, compact upload and standalone headings remain explicitly unimplemented. Keep these requirements open; the representative proposal is not the FULL feature. Tab behavior is currently pressed buttons with native keyboard operation, not a complete tab-pattern keyboard implementation; reconcile accepted keyboard contract during complete feature QA.

Files changed: tasks/UI-001/workers/RV01-review.md only. No canonical/source changes, live calls, or subagents. Memory search returned no task-relevant match; no memory facts used.

Assumptions/limitations/blockers: all findings refer only to the exact hashes above. Readback or changed proposal hashes require bounded re-review. Runtime size representation/release, native focus, responsive overflow and denied-access checks remain unknown. No separate compilation or security sandbox was assumed.

Next owner/action: primary operator performs current-proposal dryrun/validation and affected readback, routes concrete failures to builder, then provides exact revision snapshots for independent review. Builder fixes the recorded representative fidelity/handoff gaps. QA executes native lifecycle and visual checks only after authorized publication of an identified version. PREPARED/source checks do not mean applied, merged or published.

