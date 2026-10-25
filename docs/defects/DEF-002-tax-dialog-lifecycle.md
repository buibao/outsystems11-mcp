# DEF-002 — Tax Documents dialog lifecycle and return focus

Status: RESOLVED on Development MyApp versionSequence135, 2026-10-22.

On133, closing YearSelectionDialog removed an open native Popup from the tree. The served OutSystemsReactWidgets.js implementation uses its still-true ShowPopup prop during unmount and leaves reactContainer aria-hidden=true. Visible page controls then disappear from the accessibility tree. Evidence: `artifacts/ui-002/aria-diagnostic.json` and runtime-checks-133.json. Follow-on locator failures in that suite were cascading, not independent failures of every workflow.

Fix: keep the block mounted and bind Popup.ShowPopup to DialogKind; do not patch framework DOM attributes. Reset Reason when closed and synchronize the scoped focus helper on parameter changes.

On134, main accessibility recovered, but parent list deserialization replaced the invoking link, so restoring the old DOM node failed. On135, the caller records the command/stable DocumentKey before dispatch; focus returns to the current corresponding control. Tab/Shift+Tab containment, year-toggle focus, request validation/reopening and reminder dialog all pass in `artifacts/ui-002/dialog-135-checks.json`. Mobile360×800 verifies the same close/return behavior. Submit.Enabled was also bound to Files.Length > 0 and verified in runtime-checks-135.json.
