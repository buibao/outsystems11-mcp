SETUP_ONLY capability check. User authorizes two real documentation worker tasks.

Use installed native custom agent definitions analyst and reviewer from .codex/agents/*.toml. Verify they are available in your actual agent-spawning interface. Do not simulate separate roles, load their instructions as a replacement for discovery, or register duplicate roles. If unavailable, report exact actual available interface and failure; do not change configuration or enable anything.

Launch precisely two independent custom-agent threads:
- analyst: execute docs/evidence/vibeworkflow-setup/analyst-assignment.md
- reviewer: execute docs/evidence/vibeworkflow-setup/reviewer-assignment.md

Each reads its assignment and only named document inputs and returns the exact WORKER_RESULT contract. These are independent documents tasks; launch together when supported. No recursive spawning. No file writes by workers or coordinator. No O11 MCP calls at all, including token/session/reads, and no Sites native calls. Do not read credentials, user config, auth or other session transcripts. All O11 work belongs to the original primary local session. Do not restore any historical feature. Do not follow links into old feature material.

After both workers finish, inspect both results and return their full contract text plus actual agent thread identities and how roles were selected. Explicitly separate role discovered vs merely TOML installed. State any runtime/tool limitations. Do not claim O11/Sites runtime verified. Keep this probe focused; do not perform other project implementation/setup. The draft profile business identity remains UNKNOWN; assignment identity is UNBOUND-WORKSPACE / VIBE-SETUP / setup-contract-1.0, not a future business project ID.
