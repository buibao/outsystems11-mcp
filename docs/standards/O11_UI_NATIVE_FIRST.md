# Native-first O11 UI standard v1.1

Project process; installed O11 skill/tool schemas remain authoritative for APIs. Applicable to new UI and material UI redesigns. Existing approved designs can be reused when their foundation, scope and evidence are current. A small maintenance fix need not regenerate Sites; record the unchanged accepted design revision and affected delta.

## Foundation before design

Primary O11 operator performs focused read-only discovery. Record module identity/style, actual target Screen and UI Flow, theme and base chain, layout Block, installed dependency signatures, relevant public actions, utility classes and token excerpts. Module default alone is insufficient. A CSS header is version evidence of that asset, not necessarily the installed package revision.

Create one versioned `docs/catalogs/<foundation-id>.json` from `templates/UI_FOUNDATION.template.json`. Store only relevant contracts and source locators, never tokens, Site Properties inventory, business records or full CSS in worker context. Invalidate affected entries when module, theme, dependency/skill revision, consumer behavior or relevant evidence changes. A different company/on-prem environment requires discovery or exact verified equivalence; Personal Cloud is not proof of its version.

## Selection ladder

1. Approved project component, if its implementation retains native foundations and its data/lifecycle side effects fit the requested scope.
2. O11 native widget or the supported OutSystems UI pattern appropriate to the responsibility.
3. Supported pattern parameters/variants/placeholders/public actions, then existing utility classes and tokens.
4. Narrowly scoped custom presentation using existing tokens for an evidenced design gap.
5. A new owned semantic token only for a missing approved value, with reuse/ownership documented. Custom interaction/component replacement is a separate exception, never the default fallback.

Native widgets include Button, Link, Upload and Popup. OutSystems UI patterns include Tabs, Accordion, Tag and Tooltip. A native Button plus `btn` and custom JS still does not constitute the Tabs pattern. Copying pattern classes into Containers does not instantiate a pattern.

Cheat Sheet and official O11 documentation identify candidates; the installed module's signatures establish availability and supported contracts. Check current public actions before concluding that an initialization parameter cannot support a use case. `StartsExpanded` being initialization-only is not evidence that Accordion cannot be controlled. Do not assume current web documentation exactly matches an older installed version.

If a pattern is absent, classify dependency state: resident / available but not referenced / unavailable / unknown. Record the exact required addition and owner decision. Do not refresh/add dependencies or create a clone merely because dependencies were excluded from the original task. Continue independent work.

## CSS and token decisions

Use utility classes directly for equivalent layout/spacing/typography. When a selector is necessary, reuse observed CSS variables rather than writing their literal values again. Do not quantize an approved exact design value to a different scale silently; propose the difference during design review.

For example, if the installed foundation contains `--color-error`, `--color-error-light`, `--space-s`, use those for equivalent semantic intent. An approved design may require a distinct semantic value; record that exception rather than declaring any hexadecimal color categorically invalid.

Use supported small/cancel/error button variants if present. Preserve native base classes and accessibility. Do not reset `.btn` and reconstruct all its sizing/interaction rules merely to obtain tabs or disclosures. Each intentional size/density deviation belongs in the design contract.

Keep styles in the approved application-owned theme/shared stylesheet, or a justified Screen/Block scope when ownership and constraints require it. Never modify vendor CSS. Never change application-wide defaults for one feature without explicit scope. Necessary feature classes are allowed; their count is not the quality criterion.

## Reviewable design contract

Use `templates/UI_DESIGN_CONTRACT.template.md`. For each visible component record exact native candidate, availability, signature locator, parameters/events/public actions, utilities/tokens, custom gap and evidence. UNKNOWN does not become approved by filling in a name.

Sites prototype must show the intended layout/states plus a review view listing component mapping, typography/tokens and exceptions. Its app view should remain clean. Prefer verified official assets when suitable and available. If Sites simulates a pattern with web code, label simulation; do not imply the actual O11 pattern was tested. Never copy production runtime cookies/credentials/assets indiscriminately into a hosted preview.

Record actual user acceptance of the version/reference. Acceptance is not publication, dependency refresh, migration or deployment authority. Existing acceptance within the same scope is reusable. A changed component mapping, theme, material behavior or visual exception reopens only affected design decisions.

## Application and evidence

Before broad implementation, implement one approved representative native slice under existing live-write prerequisites. Verify generated model pattern instances and contracts, actual served theme/font/tokens, visible default/expanded/disabled states and required interaction. If runtime access/publication is blocked, prepare remaining plans independently; do not repeat broad speculative UI construction. Proceed with a known runtime gap only when the task explicitly authorizes that risk, and retain NOT_RUN/BLOCKED labels.

Native is not automatically bug-free or accessible for every version. Add a bounded behavior fix only for an observed failure or applicable version-specific official guidance, with relevant verification; do not preemptively build a second focus/keyboard/tooltip framework.

Reviewer blocks unexplained pattern substitutions, copied default styling, unresolved critical mappings and design drift even when compilation succeeds. Model/readback, manual merge, published version and runtime each retain their existing evidence rules. No new automatic enforcement mechanism is claimed.

## Reference provenance and canonical component mapping

Use the [CheatSheet source index](../references/cheatsheets/README.md): Developer Cheat Sheet supplies general IDE/language/widget candidates; UI CheatSheet supplies UI pattern/class/token candidates. Neither proves installed contracts. Primary local verifies only relevant signatures, public actions, utilities and tokens through read-only O11 discovery, using current foundation revision and evidence locators. Workers receive scoped source sections/excerpts and deltas, not repeated full PDF/site/theme dumps.

The native component map in the single UI design contract is the canonical mapping source. Every component row must contain: stable UI ID; UI region; classification; exact O11 widget/pattern and module (or explicit none/unknown); availability/version evidence; inputs/events/public actions; classes/tokens; custom gap; rationale; acceptance status with decision locator. Keep candidate provenance and installed evidence distinct. Use exactly Native / Native + custom CSS / Native + custom behavior / Fully custom / Unverified. These classify the proposed O11 implementation, never prove that a Sites web simulation is native. If both CSS and behavior extensions exist, classify Native + custom behavior and describe both. Fully custom requires evidenced alternatives/gap and explicit acceptance; it does not waive native-first. Missing material foundation/contract evidence is Unverified, regardless of visual similarity or design acceptance.

Sites must provide an App view for UI review and a Review view matching every UI region to its canonical UI ID, classification, component contract, tokens and exceptions. Use a review overlay/selection highlight, anchor or equivalent stable UI-ID navigation between the views, including conditional states. Keep normal App view clean. Label web simulations explicitly. The Review view reads or references the canonical contract map and its linked token/exception sections; do not maintain a second editable table. A generated projection must identify the source path/revision/hash, be regenerated after changes and be checked for missing/extra IDs and field drift before review. Freeze the same revision for prototype, contract acceptance and handoff.

Reviewer compares prototype regions/states and IDs with the canonical mapping, checks source revision and token/exception links, and flags unexplained Button/Container pattern substitutions, CSS duplicating existing utilities/tokens, missing installed evidence and prototype/mapping drift. Critical Unverified entries block dependent O11 writes until resolved with evidence; continue independent discovery/documentation. These conditions refine existing G1-G3, not a new gate system. Primary plus one milestone reviewer remains the default.
