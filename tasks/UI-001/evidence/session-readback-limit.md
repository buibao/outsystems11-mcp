# Post-merge evidence boundary

Subject: WHT_Request / UI-001 / B02, spec0.2.

Manual Compare and Merge returned merged:true with all agent changes merged (B02-merge.json). No subsequent mutation was executed.

The active tool schema explicitly says omlMerge does not end the edit session or touch its working copy. endOmlEditSession ends the session and deletes the working copy, discarding only unmerged edits; already merged changes remain live.

Post-merge getScreen returned the same exported Screen code as B02 pending. The MCP temp directory still contained only8c7c42181da74bed9df0a6c3ce1e0fa6-out.oml, no fresh in.oml snapshot. Therefore post-merge-screen.json is current-working-copy evidence, not independent accepted-live verification.

The user explicitly forbade reset/discard. The Coordinator requested permission to end this fully merged session before fresh live readback. No end/reset/discard has been called. Durable B02 checkpoint remains available; source and checkpoint hashes are in report.md. This active tool schema takes precedence over the older skill note asserting merge clears its pointer.

## Resolved with explicit authorization

User subsequently authorized ending the fully merged session. end-merged-session.json returned ended:true/discardedChanges:true (working-copy deletion semantics). No post-merge mutation had occurred. Subsequent read generated fresh fb206d14bde54776bf834b5764ef3171-in.oml; the old out.oml was absent. A durable copy is checkpoints/WHT_Request-accepted-live.oml. New live-* readbacks use this fresh accepted-live snapshot. Publication/runtime remain separate.
