# Worker result

Project/task/assignment/role: `wht / UI-001 / D01 / designer`

Input revisions and evidence subject: request R1 (full UTF-8 `C:/Users/buiba/.codex/attachments/c7a64668-e887-418c-a0a5-bf4cfe9eee28/Pasted text.txt`); ZIP reference R1, 12 extracted PNGs in `tasks/UI-001/references/`. Read `AGENTS.md`, `project.json`, `workflow/ROLES.md`, `workflow/CONTRACTS.md`, `workflow/PROTOCOL.md`, `templates/WORKER_RESULT.template.md`, project context/setup/engineering/verification/recovery documents. At inspection, canonical task-state/brief/spec/report were absent (only references/evidence/workers directories); no canonical revision is invented. `project_id` is `wht`; profile is DRAFT, design-system source UNKNOWN and no live theme snapshot supplied. Historical feature records are not this task's baseline.

Disposition: **PREPARED**

## Observed reference matrix

Each image was opened individually with `view_image`; dimensions below were independently read from PNG metadata. Prefix for each filename is `Screenshot 2026-10-22 ` and suffix `.png`. Display roles are visual personas, not authorization roles. AC identifiers below are proposed design checks for Coordinator reconciliation.

| Image / raster px | Display role | Observed state | Component composition | Proposed acceptance check |
| --- | --- | --- | --- | --- |
| 022146 / 923×586 | Submitter | COR; 2024 Not Providable; 2025 expanded Pending Upload; 2026–2029 Pending Upload | COR/PEL tabs; outlined specimen download; two instruction bullets; upload zone; selected file with green success indicator and remove icon; coverage 2025,2026,2027,2028 + Select another year; Clear All/Submit | V01 representative: all components, alignment and distinct control roles present; selected metadata removable; coverage changes; Clear All and Submit respond in memory |
| 021855 / 888×552 | Submitter | COR 2025 Rejected, non-editing; 2024 Not Providable; later years Pending Upload | File row; red rejection callout + Remove and Resubmit; expanded Tracking Details with red latest event and gray older upload event | V02 rejected view has no large upload zone; resubmit enters editing state; tracking toggles independently |
| 021939 / 833×503 | Reviewer | COR 2025 Accepted; other statuses as above | Review instruction paragraph; Suspend Reminder inline control; file row; tracking with blue accepted event incl. covering 2026,2027,2028, then gray upload event | V03 accepted reviewer state uses green badge and blue event; upload/download instructions absent; reminder control responds |
| 022033 / 845×392 | Unavailability reviewer | COR 2024 expanded Not Providable Review; later visible years Pending Upload | Submitter-style introduction; warning callout; outlined red Reject and solid blue Approve side by side; tracking initial gray request | V04 preserve this mixed visual composition without inferring permissions; review controls simulate outcome; no upload/file row in this state |
| 021657 / 907×386 | Reviewer | COR all six years collapsed; 2024 Not Providable, 2025 Accepted, 2026–2029 Pending Upload; 2026 reminder suspended | Tabs; review instructions; Suspend Reminder; muted-bell marker beside 2026; visible dark tooltip above marker | V05 collapsed row layout and suspended marker; tooltip available on keyboard focus as well as hover |
| 021744 / 907×488 | Reviewer | Standalone COR heading (no tab strip); 2026 expanded, reminder suspended, Pending Upload | Compact upload/browse strip; outlined Resume Reminder at right; blue suspension event in expanded tracking; other years collapsed | V06 standalone heading variant and compact upload must be distinct from large zone; resume removes suspended presentation and gives feedback |
| 021825 / 871×563 | Submitter | COR 2025 Rejected while resubmitting; selected replacement file | Large upload zone; selected file success/remove; multiple-year question + Select another year; Cancel/Submit footer | V07 preserve Rejected badge until simulated submission, Cancel restores fixture snapshot; red annotation rectangle is excluded |
| 021920 / 845×502 | Reviewer | COR 2025 Rejected | Reviewer introduction + Suspend Reminder; file row; red latest review tracking + gray upload event; no resubmit control | V08 distinguish reviewer rejection from submitter V02, retaining correct control visibility |
| 022000 / 842×392 | Submitter/history | COR 2024 expanded Pending Upload after rejected unavailability request | Download/instructions; tracking only: red rejected decision then gray request; no upload zone in this captured state | V09 pending-upload status does not force upload-zone visibility for this preset; preserve history-only composition |
| 022019 / 836×392 | Submitter/history | COR 2024 expanded Not Providable after accepted request | Download/instructions; tracking only: blue accepted decision then gray request | V10 neutral status badge, blue success history; no file/upload controls |
| 022107 / 866×432 | Submitter | COR 2025 expanded Pending Review; 2026–2027 collapsed Pending Review; 2028–2029 Pending Upload; 2024 Not Providable | Tabs/download/instructions; file row; collapsed Tracking Details | V11 pending-review multi-year fixture and nested collapsed tracking are independently selectable/reproducible |
| 022129 / 852×367 | Submitter | Standalone PEL heading (no tab strip); 2024–2029 all collapsed Pending Upload | Heading, download button, two bullets, six year cards | V12 standalone PEL fixture remains available alongside COR/PEL tab navigation and state isolation |

Images 022000/022019/022033 are bottom-cropped after part of the 2027 row; do not infer that 2028/2029 do not exist. Capture edges/checkerboard strips are not application UI. Names, file labels and dates are visual sample content; use safe synthetic fixture metadata and do not infer production workflows from explanatory event text.

## Proposed visual contract

Hierarchy: one synthetic-prototype Screen owns fixture selection outside the comparison region and transient state. Feature panel owns header variant (tabs or standalone title), role-specific instructions, year collection. Each year card owns an unboxed heading trigger, status pill and chevron; expanded content composes upload/file/coverage/callout/tracking/footer as its preset requires. Tracking owns its own disclosure and vertical event list. Separate reusable responsibilities: document header, year card, upload zone, file row, tracking, review/reminder controls and shared dialog host. Exact O11 names/reuse depend on the operator's current snapshot and architect contract.

Panel: white rounded surface against very pale cool-gray page. Thin light-gray borders; no heavy shadows. Year cards have about 8–10 raster-pixel corner radius, narrow vertical gaps, and modest inset content. Text is small neutral sans serif with bold year labels; application typography must be inherited unless a scoped exception is justified from current tokens.

Representative 022146 estimated raster geometry (visual measurements, not CSS values): panel x≈23–915 (width≈892), inner x≈35–903 (width≈868); tab baseline y≈38; first year y≈120–154; expanded year y≈160–399; upload x≈46–892, y≈198–297 (height≈99); file strip y≈308–329; coverage y≈340; footer divider y≈356; actions y≈368–389. Collapsed year heights ≈34–38, gaps ≈6–8. Expanded interiors inset ≈10. Match relative density/alignment, then calibrate against published screenshots. These raster sizes cannot establish source browser viewport, zoom, DPR or original CSS font size.

Tabs: blue active text/bottom underline over a thin full-width divider; inactive tab muted gray. Year headings are neutral bold text with full-row disclosure hit area; status at trailing edge, separate blue chevron. Do not render either as a filled primary button. Preserve native accessible widgets/base classes and map supported pattern parameters first. Buttons: blue solid Submit/Approve/Remove and Resubmit; outlined blue specimen download/Resume Reminder; neutral outlined Clear All/Cancel; red outlined Reject. Inline Browse/Select another year/file names remain blue underlined interactive text. Suspend Reminder is understated dark underlined text in reviewer introduction.

Badges: muted gray Not Providable; pale amber Pending Upload/Pending Review/Not Providable Review; pale green Accepted; pale red Rejected. Their labels convey meaning independent of color. File strip is pale gray, with paperclip at start and underlined filename; editing variants add success check and trailing remove button. Large upload zone is very pale gray with thin border, centered paperclip, Browse and muted extension/size guidance. Compact upload is a single shallow horizontal strip and must remain a separate variant. The reference lists pdf/doc/docx/jpg/jpeg/png and 10 MB as display guidance; Coordinator must distinguish prototype validation from backend enforcement.

Tracking: bordered nested panel; neutral bold title and blue disclosure chevron; left dotted/dashed vertical guide; event marker and multi-line metadata. New success/reminder events blue; rejection red; prior events muted gray. Callout is pale red with warning icon, border and short text; adjacent action controls remain separately focusable. Do not create whole-card color fills based on status.

Custom CSS proposal only after current theme inspection: feature-scoped panel density, year-card inset/border rhythm, upload-zone layout and tracking guide when native patterns/tokens do not express these reference gaps. Application/vendor styling remains untouched. Native token names/version are UNKNOWN to this worker; no claimed native mapping verification.

## State, interaction and accessibility contract proposal

- Fixture selector reproducibly selects all V01–V12 states and clearly labels simulation; changing fixture resets only the intended prototype fixture. COR/PEL and year identities scope files, coverage, expansion and tracking to prevent leakage.
- Year and tracking disclosures expose expanded state and controlled region; keyboard Enter/Space toggles; icon-only controls have descriptive accessible labels including year/document type. Toggling nested tracking must not toggle the year.
- Tabs expose active state, labelled panels and supported keyboard navigation. Standalone-heading fixtures intentionally omit tab chrome while the separate fixture selector still permits navigation.
- File selection/removal, Clear All, Cancel and Submit update transient state and provide visible + assistive feedback. Use synthetic filenames in evidence. No apparent download/link control may silently do nothing: provide a safe simulated result or explicit explanatory feedback.
- Year selection, reminder suspension/resumption and review outcome dialogs are proposed to make requested interactions testable; none of the 12 images shows their interior design. Use native accessible Popup/dialog with labelled heading, keyboard containment, Escape/cancel and restoration to the invoking current control. Year choices are checkbox controls, not decorative text. Keep confirmation/action semantics explicit and synthetic.
- Tooltip is available on focus, associated with its muted-bell trigger, and dismissible without losing context. Status updates use restrained live feedback; never rely only on green/red color.
- Focus outline remains visible; control targets must remain operable despite compact visual density. At narrow widths, wrap instruction text, long file names and footer actions; keep badge/chevron visible and avoid horizontal page scrolling. Preserve reading order.

## Viewports and comparison proposal

Reference comparison: capture 022146 first at browser zoom 100%, deviceScaleFactor 1, recording actual viewport and measured panel bounding box. A 960×720 viewport with feature width adjusted to ≈892 CSS px is an initial calibration candidate, NOT a claim about source viewport. Do not shrink fonts to an assumed screenshot scale without evidence. For every reference retain original raster dimensions above, actual runtime viewport, zoom, panel width, selected fixture and expanded states. Compare normalized panel crops only with scaling disclosed; exclude synthetic fixture toolbar, screenshot edges and red annotation. Record font/DPR uncertainty as a limitation, not a PASS.

Proposed usability viewports: 1440×900 desktop, 768×1024 tablet, 390×844 mobile, all 100% zoom; additionally 200% zoom keyboard check on desktop. No mobile reference exists, so narrow-width results establish usability/overflow, not pixel fidelity. Verify all twelve matching states against identified published version; compare control hierarchy, section geometry, density, status color, file-row details, timeline and footer alignment. A full-state visual PASS needs actual runtime captures and documented residuals.

## Checks executed

| Check | Expected | Observed | Result / evidence |
| --- | --- | --- | --- |
| Project identity | wht | project.json project_id wht | PASS, current local file |
| Complete request | Read full UTF-8 request | All six numbered sections inspected | PASS, attachment R1 |
| Reference inventory | 12 PNGs | 12 distinct filenames and raster dimensions | PASS, filesystem metadata |
| Actual image inspection | Open every original image | All twelve opened individually, representative first then required variants | PASS, view_image tool observations reflected in matrix |
| Design-system availability | Current theme/token snapshot | Profile source UNKNOWN; historical docs only | BLOCKED for native-token finalization; independent reference contract PREPARED |
| Runtime visual/access tests | Published environment/version and browser | Not supplied or operated by worker | NOT_RUN |
| Model/merge/publish | Operator evidence | No MCP operations performed | NOT_RUN |

Files changed: only `tasks/UI-001/workers/D01-visual.md`.

Assumptions/limitations/blockers: display-role labels are presentation interpretation; screenshot labels do not establish server authorization/business policy. Actual viewport/zoom/DPR/font and live theme remain unknown. Setup checkpoint/review/pending-state unresolved checks apply to primary live writes, not this read-only analysis. Memory registry lookup was unavailable and no memory-derived fact was used. No source/model/Sites or canonical task files modified.

Next owner/action: Coordinator reconciles V01–V12 with canonical AC and current native theme/component snapshot; architect maps bounded contracts; builder prepares representative 022146 before 021855/021939/022033, then remaining variants. QA executes full matrix only against identified published runtime. **PREPARED does not mean applied, merged, published or runtime verified.**
