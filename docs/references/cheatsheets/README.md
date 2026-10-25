# CheatSheet source index

Observed 2026-10-25. These are candidate-discovery references, not evidence of installed contracts, availability, version compatibility or runtime behavior. Follow the [native-first standard](../../standards/O11_UI_NATIVE_FIRST.md). No live O11 discovery was performed for this index.

| Source ID | Source / locator | Purpose and scoped entry points | Observed version/date | Limits |
| --- | --- | --- | --- | --- |
| DEV-CS | [OutSystems Developer Cheat Sheet](OutSystems-Developer-Cheat-Sheet.pdf) | General IDE and language concepts. p1: IDE, screens, structures, variables/actions; p2: calls, data/queries/integrations; p3: UI Flow, Screen/Block/widget candidates and logic; p4: logic, integrations, security and data. | Footer v0.8; 4 pages. PDF CreationDate and ModDate: 2023-12-21 20:20:34 UTC. | File metadata is not a release date or installed platform version. Overview spans concepts/styles; no installed widget/public-action signature or UI token registry. Examples involving publish/data/security are reference content, not operation authorization. |
| UI-CS | [OutSystems UI CheatSheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet) | UI pattern, class and CSS-variable candidate lookup. Observed sections include UI Patterns, Borders, Buttons and Colors; examples include Tabs, Accordion, Tag and Tooltip, button variants and border utilities/variables. | Browser title: OutSystems UI / CheatSheet; accessed 2026-10-25. Release/version and publication date UNKNOWN. | Mutable JavaScript-rendered reference. Basic web fetch returned JavaScript required; browser read succeeded. Website values and names do not establish resident package version, supported signatures or actual target theme. |

PDF provenance: user-supplied D:/Downloads/OutSystems-Developer-Cheat-Sheet.pdf; copied byte-for-byte, 247616 bytes. SHA-256: `b74f8288a77e3c32cf88ac5c963e3dead8818881b820c885b881cc36b2110e9c`.

## Candidate-to-evidence use

Use DEV-CS for general concept/widget candidates and UI-CS for pattern/class/token candidates. Record source ID plus page/section for only the feature's relevant candidates. For example, DEV-CS p3 can suggest a Screen/Block or Upload; UI-CS UI Patterns can suggest Tabs/Accordion. These examples remain candidates, not WHT mapping decisions.

Primary local alone verifies relevant installed signatures, inputs/events/public actions, utility classes and token values through scoped read-only O11 discovery under the official skill and actual schemas. Record target/actual Screen/UI Flow theme/layout, availability, version evidence, evidence subject/locator and foundation revision separately from reference provenance. Never promote a website or PDF claim into installed evidence. Missing dependency/public-action evidence remains Unverified where critical; no clone or refresh workaround.

Reuse the focused [foundation catalog](../../../templates/UI_FOUNDATION.template.json) revision while relevant target/theme/dependency/skill/contracts remain valid; recheck only affected entries after changes or conflicting evidence. Assign workers source IDs/page/section, relevant verified excerpts, UI IDs and revision/delta locators. Do not reread the whole PDF/site or dump the whole theme into each worker. This source index is not a generated feature catalog.
