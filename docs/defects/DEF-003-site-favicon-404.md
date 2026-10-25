# DEF-003 — site-root favicon returns 404

Status: OPEN, non-blocking for UI-002. Observed 2026-10-22 in Development on published versions133–135.

Chrome requests `https://personal-g4et6y1o.outsystemscloud.com/favicon.ico` and receives404. This is the remaining console resource error; no page JavaScript exception was observed in the final UI suites. The Tax Documents styles, scripts, images and interactions load and execute.

Evidence: `artifacts/ui-002/runtime-checks-135.json` logs include the exact resource location. The error was retained in captures/logs, not suppressed. Root favicon hosting is outside this screen-scoped UI correction; it requires a separately scoped platform/application asset decision. No configuration change was made.
