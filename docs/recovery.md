# Recovery

## Current recovery readiness

- Recoverable pre-change module/version checkpoint: UNKNOWN.
- Organization-approved O11 versioning/rollback procedure and owner: UNKNOWN.
- Database restore, retention and external-side-effect recovery procedures: UNKNOWN.
- A local documentation Git commit is not a live application backup. Temporary MCP snapshots/output are not durable backups.
- Before the first live feature write, identify the relevant existing O11 checkpoint practice and record the checkpoint/version and owner. Do not publish just to create a checkpoint during bootstrap.

## Pending model changes

Read the pinned skill's `reference/mcp-session-pointer.md` and `reference/verb-reference.md` before recovery. Model reads can follow an unmerged host copy. No reset, discard, refresh or merge was performed by bootstrap; unrelated pending-copy state is UNKNOWN.

Do not have two writers modify one module. If the user edits the live module or switches context, re-read relevant state before writing again. Current [product guidance](https://success.outsystems.com/documentation/11/outsystems_mcp/security_and_data_handling/) describes invalidation of a pending copy when the user edits; older distribution design notes differ. Do not assume a stale copy remains mergeable.

Keep the last tool-reported `mutatedOmlPath` and outcome in the session if an authorized future edit creates one. Preserve unresolved output; never edit its contents by hand. A successful merge can consume the output, so do not replay the same merge merely to confirm it. A path from an older, changed or superseded copy may be rejected.

Reset/discard, dependency refresh, merge and publish require authorization for the specific recovery operation. A transport error or unknown outcome does not authorize any of these operations. Do not restart Service Studio while recoverable pending work may exist without first understanding its fate; startup can clean its temporary files. Reloading Codex alone is the setup resume path.

## Failure classification

Observed during the 2026-10-22 Tax Documents feature: the installed MCP tools require explicit startOmlEditSession before writes, and omlMerge does not end that session. After a successful merge, endOmlEditSession removed its working copy; an immediate read then reported a missing temporary `-in.oml` snapshot. A new startOmlEditSession succeeded and supplied a fresh live checkout. Inventory, Screen access and validation were read from it without any mutation, then the verification session ended with discardedChanges=false. Do not replay a successful merge to repair this read-snapshot error. The installed tool schemas take precedence over older skill text about automatic pointer cleanup. Reset, refresh and publish were not used.

| Failure | Response |
| --- | --- |
| Transport / client timeout | Inspect connection and current state; do not blindly replay a write. Reuse the same approved token after reconnecting in the same session. |
| API compilation / argument envelope | Inspect actual schema, required fields and pinned examples. A compile error is not a successful save. |
| Model validation | Compare with the recorded baseline; retain unresolved work and scope the correction. |
| Merge rejection / unknown outcome | Inspect the reported state and available Service Studio dialog; do not repeatedly merge or discard. |
| Runtime / integration failure | Establish published version, affected data and external side effects before planning recovery. |

A model rollback does not restore data or reverse external effects.

## Local bootstrap rollback

The local configuration backup is recorded in [setup status](setup-status.md). To reverse bootstrap configuration, first compare it with the current file and preserve any subsequent user changes; never overwrite unrelated later settings blindly.

The original user skill was moved, unchanged, from `C:\Users\buiba\.agents\skills\servicestudio-mcp-oml` to the project's `.agents/skills/servicestudio-mcp-oml`. It can be moved back after verifying both locations and removing the competing project discovery path. The staged copy inside the vendor checkout was left intact and disabled by an explicit Codex skill-selection entry.

No local Git repository or remote was created for this project. Select the approved repository before committing these documents. The upstream distribution's staged files are user work and must remain untouched.
