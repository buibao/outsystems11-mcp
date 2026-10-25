# DEF-001 — TaxDocumentsPreview reducer namespace failure

Status: RESOLVED by UI-002 on Development versions133–135. Verified 22 October 2026, Asia/Saigon.

Current evidence: `artifacts/ui-002/after-scenarios.json` identifies published135, a loaded reducer function, all12 working presets and no reducer exception. `runtime-checks-135.json` and the additional dialog/file/mobile suites pass. Fix: remove the duplicate early OnInitialize invocation, retain OnReady. No fallback, exception suppression or hidden alert. The remaining site favicon404 is tracked separately as DEF-003. The investigation notes below are historical and superseded by this verified result.

UI-002 follow-up, 2026-10-22: reproduced in a fresh Chrome context on published `versionSequence 132`, token `oEJ0BylI6r+a_wCYBMc3bQ`. Console stack goes through `_initializeDemo$Action` → `_handleIntent$Action` → ReducePreviewState. The live baseline invokes InitializeDemo at both OnInitialize and OnReady; after load `window.TaxDocumentsPrototype.reduce` is a function and all 12 presets operate. Evidence: `artifacts/ui-002/baseline-runtime.json`, `baseline-scenarios.json` and initial screenshot (the alert was retained). The bounded UI-002 fix removes only OnInitialize's duplicated early invocation and retains OnReady. Model readback/merge have passed; runtime retest against the next published version remains **NOT_RUN**. Status remains OPEN / FIX MERGED, AWAITING PUBLISH RETEST, not resolved.

Reported error: `Cannot read properties of undefined (reading 'reduce')`.

Source: [CSS-001 specification, sections 2 and 6](../specs/report/O11_CSS_Refactor_and_Project_Rules.md). The earlier browser observation was on `https://personal-g4et6y1o.outsystemscloud.com/MyApp/TaxDocumentsPreview`. The active preset, exact published version, account, browser console stack and network timing were not supplied; those fields remain UNKNOWN. This refactor did not reproduce that browser session.

Current model evidence: `TaxDocumentsPreview/HandleIntent/ReducePreviewState` calls `window.TaxDocumentsPrototype.reduce(...)`. RequiredScripts includes `TaxDocumentsPrototype` on the Screen, DocumentUploadPanel and YearSelectionDialog. CSS-001 preserved the Screen's non-style statements, action JavaScript, event arguments and state/fixture contracts. These observations establish model references only; they do not establish that the namespace exists at execution time.

Cause: UNCONFIRMED. A script-load/lifecycle problem is a hypothesis to investigate, not an established diagnosis. No suppression, blanket fallback, alert hiding, reducer edit or script-load workaround was introduced by CSS-001.

Reproduction/retest: NOT_RUN. A separate logic-fix scope should identify the published environment/version and active preset, capture the complete stack, inspect script loading and `window.TaxDocumentsPrototype` at the failing action, and verify initialization/reset, COR/PEL changes and subsequent interactions after a separately authorized correction/publish. Functional or visual checks blocked by this exception must not be recorded PASS.

Related work: [CSS-001 execution report](../execution/CSS-001.report.md).
