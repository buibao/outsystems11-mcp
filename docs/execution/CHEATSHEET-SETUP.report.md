# CHEATSHEET-SETUP execution report

Revision 1, 2026-10-25. Documentation/template/prompt task authorized by current request. Status: integrated; local metadata/reference/syntax/preservation checks executed. No WHT task or CompletionTarget change. No O11 or Sites operations.

## Deliverables and changes

- Stored user PDF byte-for-byte and added [source index](../references/cheatsheets/README.md), including purpose, scoped page/section navigation, observed v0.8/metadata date, web URL/access date, provenance and limits.
- General Developer reference and UI pattern/class/token reference are distinct candidate sources. Installed signatures/public actions/utilities/tokens require primary-local read-only discovery. Reuse scoped foundation revisions and give workers relevant excerpts/deltas only.
- One canonical component map lives in the UI design contract. Every row includes UI ID, region, classification, exact widget/pattern/module, availability/version evidence, inputs/events/public actions, classes/tokens, custom gap, rationale and acceptance. Candidate provenance and criticality/evidence resolution are explicit.
- Sites App and Review views correlate the same stable UI IDs. Review consumes/references the canonical map and linked token/exception sections. Generated projections pin revision/hash and verify ID/field drift, rather than maintaining independent editable tables. Sites web simulation stays distinct from proposed O11 classification.
- Reviewer rejects unjustified Button/Container substitutions, redundant CSS where utilities/tokens exist, missing evidence and prototype/map drift. Critical Unverified blocks dependent writes. Existing gates, primary plus one reviewer, operational authorization and safeguards remain unchanged.

Modified files:

- [adapters/SITES.md](../../adapters/SITES.md)
- [prompts/O11_UI_APPLY.md](../../prompts/O11_UI_APPLY.md)
- [prompts/UI_DESIGN_START.md](../../prompts/UI_DESIGN_START.md)
- [templates/UI_DESIGN_CONTRACT.template.md](../../templates/UI_DESIGN_CONTRACT.template.md)
- [templates/UI_FOUNDATION.template.json](../../templates/UI_FOUNDATION.template.json)
- [.codex/agents/architect.toml](../../.codex/agents/architect.toml)
- [.codex/agents/builder.toml](../../.codex/agents/builder.toml)
- [.codex/agents/designer.toml](../../.codex/agents/designer.toml)
- [.codex/agents/reviewer.toml](../../.codex/agents/reviewer.toml)
- [docs/catalogs/README.md](../../docs/catalogs/README.md)
- [docs/standards/O11_UI_NATIVE_FIRST.md](../../docs/standards/O11_UI_NATIVE_FIRST.md)

## Actual checks and evidence

| Check | Result | Evidence / limitation |
| --- | --- | --- |
| PDF copy, metadata and page/footer extraction | PASS | [Source evidence](../evidence/cheatsheet-setup/sources.json); source SHA-256 equals stored PDF |
| UI website read | PASS | Basic web fetch needed JavaScript; browser read succeeded. Only reference content observed; no installed-version assertion |
| Existing package checker for current WHT task | PASS | [Metadata output](../evidence/cheatsheet-setup/metadata.json); no business/native/runtime validation |
| Changed/new Markdown local links and JSON/TOML | PASS | [Local checks](../evidence/cheatsheet-setup/local-checks.json); external URLs/placeholder paths excluded from local-link pass |
| Preservation / final diff | PASS | [Local checks](../evidence/cheatsheet-setup/local-checks.json) and [diff](../evidence/cheatsheet-setup/integration.diff); baseline includes current prior setup changes |
| Independent milestone review | PASS, no actionable findings | [Review](../evidence/cheatsheet-setup/review.md) |

## Not verified / next dependent operations

O11 discovery, actual installed/native usage, public-action signatures, theme/token applicability, design acceptance, Sites App/Review implementation, generated mapping consumption, UI-ID navigation and runtime/visual/access QA: NOT_RUN. No real feature catalog or WHT mapping has been invented. No Sites skill execution was needed to edit these instructions; a future prototype task must read and use the installed skill.

In the next authorized feature/design task, primary local performs missing scoped read-only discovery, records evidence/foundation revision and resolves critical Unverified. A Sites prototype then consumes/references the canonical contract and demonstrates App/Review UI-ID correspondence before acceptance. No new gate or automatic enforcement was installed. Metadata PASS does not establish native usage, runtime or visual QA.
