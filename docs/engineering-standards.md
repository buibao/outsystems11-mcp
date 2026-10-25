# Engineering standards

## Status of these rules

The setup/change-control rules in [AGENTS.md](../AGENTS.md) are adopted from the user's bootstrap request. The implementation conventions below are observed facts or PROPOSED review criteria. They are not confirmed business requirements.

## Observed conventions

- The current target is Reactive. Use the Reactive read tools and Model API interfaces.
- `DoLogin` and `DoLogout` are local action names. A single sample does not establish an action naming standard.
- `DoLogin` is non-public, lives in `Authentication`, and delegates to resident `Users.User_Login`. This is not evidence of an authorization policy for future features.
- Existing references include OutSystemsUI, Charts, Maps, System and Users. No new dependency is authorized by their presence.
- Bootstrap returned no locally defined entities. The subsequent Tax Documents prototype adds only Static Entities `DocumentType` and `DocumentStatus`; it establishes no convention for persisted-entity foreign keys, indexes, deletion or concurrency, which remain UNKNOWN.

## PROPOSED criteria to confirm per feature

| Area | Questions / criteria before implementation |
| --- | --- |
| Ownership and architecture | Identify owning module, reviewer, exposed server/service actions and permitted dependency directions. Keep existing boundaries; obtain approval for a new dependency. |
| Data design | Define identifiers, relationships, indexes, delete rules, tenant/record ownership and concurrency behavior. Choose date/time zone semantics and decimal precision when relevant. |
| Authorization | Validate client-supplied identifiers and enforce protected operations on the server. Specify allowed and denied roles and ownership cases. |
| Queries | Define dataset sizes, server filtering, pagination and stable sorting. Parameterize dynamic values and examine relevant performance evidence. |
| Transactions and errors | Define transaction boundary, exception behavior, idempotency/retry limits and diagnostic fields without secrets. |
| UI | Reuse the observed theme and resident blocks after inspection. Specify form validation, loading/empty/error states, keyboard use and responsive behavior. |
| Workflow | Define transitions, initiating roles, rejection/resubmission and audit requirements before implementing a workflow. |
| Timers/integrations | Define schedules, time zones, timeouts, retries, duplicate-processing protection and external side effects as applicable. |

UNKNOWN items are acceptable in bootstrap documentation; they must not be silently converted into feature assumptions.

## Reference map

All paths below were checked in the pinned official skill under `../.agents/skills/servicestudio-mcp-oml/`:

- Contract and failures: `reference/lambda-contract.md`, `reference/verb-reference.md`.
- Element patterns: `reference/patterns-by-element.md`.
- Logic, integrations and BPT: `reference/logic-and-integrations.md`.
- Reactive UI: `reference/reactive-ui-creation.md`, `reference/reactive-widget-api.md`, `reference/osui-verified-blocks.md`.
- Traditional work, if the target changes: `reference/module-style-support.md`, `reference/traditional-ui-creation.md`.

Load the relevant file, not the whole reference corpus. The current skill records revision-specific limitations for adding cross-module dependencies and some screen/block CSS publishing paths. Do not equate refreshing references with adding a dependency; verify delivered assets if an authorized CSS change appears stale.

## Security-source precedence

Use current [OutSystems product security guidance](https://success.outsystems.com/documentation/11/outsystems_mcp/security_and_data_handling/) and observed supported behavior over older upstream design notes. Keep the official skill unchanged; record discrepancies in [setup status](setup-status.md). Never use older notes to justify bypassing restrictions.

Organization approval of the AI account and its data settings is UNKNOWN. Model content can enter the provider request. Leave secret defaults out of module source and use the organization's existing per-environment configuration practice. Do not retrieve Site Property defaults to audit this.

## OutSystems UI and CSS reuse

- Apply the mandatory [native-first standard](standards/O11_UI_NATIVE_FIRST.md), including actual Screen/UI Flow theme/layout and installed public actions before design. The [lean workflow](standards/LEAN_UI_WORKFLOW.md) defines Sites acceptance and representative evidence within existing gates.
- Use the native-first selection ladder: accepted suitable native-based project component; corresponding native widget/OSUI pattern; supported parameters/public actions/classes/tokens; minimal evidenced custom gap; new owned token only for a missing accepted semantic value. Button imitations are not Tabs/Accordion reuse; missing dependencies do not authorize cloning or refresh.
- Preserve required base classes. A custom semantic/modifier class may extend a framework control, but must not replace its foundation with a duplicate button, input, tab, badge or dialog framework.
- Prefer existing widget/pattern parameters over CSS overrides when they express the required behavior or appearance. Do not substitute a visual-only control for a functional accessible pattern.
- Use actual theme tokens for colors, typography, spacing and borders when equivalent tokens exist. Inherit the application font. Do not introduce a second fixed font/color/spacing scale merely to match a screenshot.
- The application theme owns shared defaults. Any deliberately different feature-level design decision must be documented. Keep it scoped to the feature; do not recolor the whole app to match one reference image.
- Keep custom semantic classes for domain-specific layouts such as the document dropzone or tracking timeline where platform patterns/utilities do not express the design. For each remaining custom rule, identify its purpose and why the existing foundation is insufficient.
- Keep reusable custom styles in the application-owned theme or approved shared stylesheet, scoped under the feature root when appropriate. A Screen or Block stylesheet exception must have a concrete reason. Never edit the vendor OutSystemsUI stylesheet.
- Avoid broad element resets, universal selectors, generated-ID selectors, inline CSS, blanket `!important` and JavaScript style injection. Preserve focus, disabled, validation and responsive behavior.
- Inspect generated grid/sibling margins before adding flex gaps or custom spacing. Avoid applying two spacing mechanisms to the same relationship; fix the affected widget configuration rather than globally overriding grid classes.
- Verify both model classes and the served CSS/computed styles. Passing model validation alone does not prove that the correct style layer was published.

These are project policies. They do not prohibit all custom class names or require a framework pattern where it cannot support the feature correctly.