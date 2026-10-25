# Current discovery evidence — 2026-10-24

Primary-operator tool observations (summaries, not fabricated permanent tool logs):

- project.json project_id wht; tasks initially contained README only; no UI-001 spec/report filename existed. User request selected UI-001 and O11_ONLY/LOCAL/RUNTIME_VERIFIED.
- Native listApps: WHT_Request, key 50e8e182-1c94-4c32-bf3b-f4e609f48bda, isOpen true, isReference false, Reactive. Version 0 does not identify a publication.
- Windows UI Automation under ServiceStudio PID23692 read Development - personal-g4et6y1o.outsystemscloud.com and WHT_Request.
- User explicitly confirmed Manual review changes in compare and merge and no concurrent module edits. No setting changed.
- startOmlEditSession returned started:true; primary is sole operator. Checkpoint copied from sole current host input OML; SHA256 A285C8072568F619410DF540EE8061214A2B078E518303AF028AE40352CF67AB. Restore NOT_RUN.
- Baseline all-message getValidationMessages: 0 errors/72 warnings, exact data saved in validation-baseline.json.
- Current read probes: default WHT_Theme_Fabric, base OutSystemsUI; base stylesheet says OutSystems UI 2.20.0. Reference Version/Revision empty. Theme/source excerpts saved, no mutation saved by probes.
- Existing Request_COR_PELetter has real server aggregates, downloads, deletes and upload transaction. Excluded from prototype reuse to prevent business side effects. Existing consumers remain unchanged.
- Current tool catalog has no omlPublish. No publish/refresh/reset/discard/configuration change performed.
- Read query with Themes failed schema validation; corrected by getThemeNames. Read-only probe using BlockSignature.Placeholders failed compile; corrected by reading supported input signatures. Neither saved an OML.

These observations establish discovery/model-view facts only. Published version, runtime behavior and visual comparison NOT_RUN.
