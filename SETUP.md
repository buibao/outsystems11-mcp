# Setup on local Codex and Work

Local integration evidence (2026-10-23): codex-cli 0.162.0-alpha.17.2 accepted `agents.enabled` and `agents.max_concurrent_threads_per_session` in a strict config/read probe. Only those keys were added to `.codex/config.toml`. User authorized trust for this exact workspace; all other user config and existing MCP/security settings were preserved. A fresh CLI session selected analyst/reviewer by native `agent_type`, and their exact TOML instructions were found in their developer contexts. See [report](docs/execution/VIBE-SETUP.report.md). Work discovery and platform feature flows were not tested by this setup.

## Local Codex

1. Start in the business workspace. Preserve existing AGENTS, config layers and upstream checkout; integrate these files by review rather than blind replacement.
2. Standalone `.codex/agents/*.toml` files define project-scoped custom agents in current Codex documentation. Each has name, description and developer_instructions. They inherit parent model/settings unless explicitly configured; this kit does not pin a model.
3. `.codex/config.example.toml` is an optional configuration fragment, NOT an active config. Merge only supported relevant keys into the existing configuration. Current docs do not require an older experimental multi_agent feature flag. Verify behavior on the installed version, particularly an older/alpha client.
4. Keep working MCP entries in their existing effective config layer. Do not create a second Service Studio server or move user config mechanically. This kit does not change endpoint, tool exclusions, sandbox, approvals or credentials.
5. Start a fresh appropriate session and ask which roles/config/instructions are loaded. Run a bounded docs-only assignment to analyst and reviewer, requesting separate agent threads and contract-shaped results. A TOML parser succeeding is not proof of discovery.
6. Perform read-only O11 preflight when O11 work is requested. Identify module/style/environment, installed skill revision, actual schemas, review mode and current pending state. Reuse valid evidence until the relevant environment/config/revision changes. Resolve only essential blockers for the next operation.

The kit's role files do not set sandbox_mode, approval_policy or mcp_servers: custom-agent files cannot override these parent settings according to current docs. 'Read-only reviewer' is an instruction, not enforcement. Keep live O11 calls with the primary operator so workers never need the MCP token.

## Work + Sites

Use the stage role briefs in `workflow/ROLES.md` and explicitly request subagents. Do not assume local `.codex/agents/` files are installed in hosted Work. Check available capabilities; report unavailable independent-agent execution instead of simulating it silently.

Creating a workflow kit does not create or publish a Site. For a later authorized prototype task, read the current installed Sites skill. The primary Work conversation owns native calls and source workflow. Use provided helpers and preserve project identity/audience for updates. Follow explicit preview/save/deployment scope and tool approvals.

## Existing repo migration

Keep the official O11 skill and its pinned provenance. Keep existing engineering/verification/recovery documents that remain useful; point to them from the O11 adapter instead of copying conflicting rules. Replace project-specific constants in shared process files with profile fields only after reviewing the actual project. Migrate active work as a task package. Removed features do not become required migration work.
