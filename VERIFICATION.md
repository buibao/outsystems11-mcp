# Kit verification and rollout

Local setup update, 2026-10-23: package/metadata checks, native analyst/reviewer discovery and contract execution, and primary-only read-only O11 preflight have now run. The rollout table below is the original kit's unexecuted baseline; consult [VIBE-SETUP.report.md](docs/execution/VIBE-SETUP.report.md) for current per-check results. Work dispatch, cross-surface handoff and feature implementation/runtime remain NOT_RUN. No setup smoke edit was performed.

## What is checked for this delivery

- File structure, JSON parsing and all standalone role TOML required fields.
- Distinct role names and separation of adapter/native-call ownership.
- Basic readiness validator rejects unfilled profiles, cross-project task identity and invalid targets; task routing can select O11-only work inside a hybrid project.
- No feature-specific artifacts, runtime credentials, copied Site IDs or model identities are supplied.

These are package/static checks, not proof of Codex discovery, Sites connectivity or O11 behavior.

## Required rollout checks — NOT_RUN

| Check | Method | Expected |
| --- | --- | --- |
| Local role discovery | Installed client shows/uses a requested custom role | Actual separate thread returns correct assignment identity |
| Delegation and reconcile | Analyst + reviewer get one bounded docs task | Separate results; Coordinator resolves findings without fabricating PASS |
| Work role dispatch | Explicitly delegate independent design/reference work | Work creates actual workers with available parent tools |
| Cross-surface handoff | Export/reopen one versioned synthetic design package | Same project/task/revision/assets accessible on receiving side |
| O11 preflight | Actual read-only target/schema/validation/session checks | Correct environment/module/style and operation restrictions |
| Representative implementation | One authorized disposable/safe feature | Bounded write/readback/manual merge/runtime per selected target |
| Interrupted work resume | Resume a controlled incomplete task | Re-read state; no duplicate mutation/discard or lost pending work |
| Project switch | Switch between two distinct synthetic profiles | No identity, permission, fixture or state leakage |

Do not run live smoke edits during setup-only verification. Schedule the implementation check as an explicitly scoped feature task. A profile is not access control, a writer field is not a lock, a role instruction is not sandbox enforcement, and passing the local validator does not prove completion.
