# Worker assignment

Project/task/assignment ID: UNBOUND-WORKSPACE / VIBE-SETUP / A-DOCS-01
Role and bounded outcome: analyst; derive a concise first-project intake checklist from the installed workflow.
Input spec/handoff/snapshot revision and subject: setup-contract-1.0; local workflow documents only; project.json is DRAFT with UNKNOWN business identity.
Read these sources only as needed: .codex/agents/analyst.toml, workflow/ROLES.md, workflow/CONTRACTS.md, workflow/PROTOCOL.md, templates/WORKER_RESULT.template.md, project.json, prompts/START.md, prompts/WORK_TO_LOCAL.md.
Allowed file writes: NONE.
Allowed tool/test operations: local read/search only for the listed documents and AGENTS.md. Never call O11 MCP, createSessionToken, Sites tools, web services, or read credentials/config/session transcripts. No subagents.
Protected/excluded: all application/model/deployment operations; upstream; all canonical state/spec/report. Do not use old feature context or bind a business target. Setup-only requirements from the current user govern this assignment.
Dependencies: stable installed documentation; no dependency on reviewer output or live preflight.
Return: exact WORKER_RESULT contract; checklist split into Work and Codex local, unknowns, actual document checks and evidence locators. Include actual execution mechanism; reading TOML does not prove native custom-agent discovery.
