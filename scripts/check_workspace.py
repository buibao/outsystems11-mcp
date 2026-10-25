#!/usr/bin/env python3
"""Read-only package/metadata check. Never connects to a platform or grants authority."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import tomllib


ROUTES = {"HYBRID_SITES_O11", "SITES_ONLY", "O11_ONLY"}
SITES_TARGETS = {"LOCAL_REVIEW", "SAVED_VERSION", "DEPLOYED_VERIFIED"}
O11_TARGETS = {"MODEL_REVIEW", "MERGED", "RUNTIME_VERIFIED"}
ROLES = {"analyst", "designer", "architect", "planner", "builder", "reviewer", "qa"}
REQUIRED = [
    "AGENTS.md", "README.md", "SETUP.md", "VERIFICATION.md", "TEMPLATES.md",
    "workflow/PROTOCOL.md", "workflow/ROLES.md", "workflow/CONTRACTS.md",
    "workflow/PROJECT_SWITCH.md", "adapters/SITES.md", "adapters/O11.md",
    "templates/BRIEF.template.md", "templates/TASK_SPEC.template.md",
    "templates/DESIGN_HANDOFF.template.md", "templates/O11_PLAN.template.md",
    "templates/WORKER_ASSIGNMENT.template.md", "templates/WORKER_RESULT.template.md",
    "templates/EXECUTION_REPORT.template.md", "templates/TASK_STATE.template.json",
    "prompts/START.md", "prompts/WORK_TO_LOCAL.md", "prompts/RESUME.md",
    ".codex/config.example.toml",
]


def filled(value):
    return isinstance(value, str) and value.strip() not in {"", "UNKNOWN", "REPLACE_ME"}


def check(root: Path, ready=False, task=None, for_o11=False):
    errors, notes = [], []

    def read_json(path):
        try:
            value = json.loads(path.read_text(encoding="utf-8-sig"))
            if not isinstance(value, dict):
                raise ValueError("expected JSON object")
            return value
        except (OSError, ValueError) as ex:
            errors.append(f"{path}: {ex}")
            return {}

    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f"Missing kit file: {name}")
    profile = read_json(root / "project.json")
    read_json(root / "templates/TASK_STATE.template.json")
    route = profile.get("default_delivery_route")
    if route not in ROUTES:
        errors.append("Unsupported default_delivery_route")
    names = set()
    for path in sorted((root / ".codex/agents").glob("*.toml")):
        try:
            cfg = tomllib.loads(path.read_text(encoding="utf-8"))
            for key in ("name", "description", "developer_instructions"):
                if not filled(cfg.get(key)):
                    errors.append(f"{path.name}: missing required {key}")
            name = cfg.get("name")
            if name in names:
                errors.append(f"Duplicate role: {name}")
            names.add(name)
            for key in ("sandbox_mode", "approval_policy", "mcp_servers"):
                if key in cfg:
                    errors.append(f"{path.name}: parent-session setting {key} in role file")
        except (OSError, ValueError, TypeError) as ex:
            errors.append(f"{path.name}: {ex}")
    if names != ROLES:
        errors.append(f"Role set differs: {sorted(str(x) for x in names)}")
    try:
        tomllib.loads((root / ".codex/config.example.toml").read_text(encoding="utf-8"))
    except (OSError, ValueError) as ex:
        errors.append(f"Config example: {ex}")
    if ready:
        for key in ("project_id", "display_name"):
            if not filled(profile.get(key)):
                errors.append(f"Unfilled project {key}")
        if profile.get("profile_status") != "ACTIVE":
            errors.append("profile_status must be ACTIVE for metadata readiness")
        if task is None:
            errors.append("--ready requires --task tasks/<task-id>")
    if task is not None:
        candidate = Path(task)
        task_path = (candidate if candidate.is_absolute() else root / candidate).resolve()
        try:
            task_path.relative_to((root / "tasks").resolve())
        except ValueError:
            errors.append("Task path must be inside this workspace's tasks directory")
            return errors, notes
        state = read_json(task_path / "task-state.json")
        route = state.get("delivery_route")
        if route not in ROUTES:
            errors.append("Task delivery_route must be explicitly selected")
        if state.get("active_surface") not in {"WORK", "LOCAL", "UNASSIGNED"}:
            errors.append("Invalid active_surface")
        if not filled(state.get("project_id")) or state.get("project_id") != profile.get("project_id"):
            errors.append("Task project_id does not match the filled project profile")
        if not filled(state.get("task_id")) or state.get("task_id") != task_path.name:
            errors.append("Task task_id must match its directory name")
        if not filled(state.get("spec_revision")):
            errors.append("Task spec_revision is missing")
        for name in ("brief.md", "spec.md", "report.md"):
            if not (task_path / name).is_file():
                errors.append(f"Missing task file: {name}")
        st, ot = state.get("sites_target"), state.get("o11_target")
        if route in {"SITES_ONLY", "HYBRID_SITES_O11"}:
            if st is not None and st not in SITES_TARGETS:
                errors.append("Invalid Sites target")
            elif st is None:
                notes.append("Sites target not selected: resolve before dependent implementation/integration.")
        if route in {"O11_ONLY", "HYBRID_SITES_O11"}:
            if ot is not None and ot not in O11_TARGETS:
                errors.append("Invalid O11 target")
            elif ot is None:
                notes.append("O11 target not selected: independent design may proceed, O11 implementation is not ready.")
            if for_o11 and ot not in O11_TARGETS:
                errors.append("Valid O11 target is required for O11 implementation metadata")
        if route == "SITES_ONLY" and ot is not None:
            errors.append("O11 target must be null for SITES_ONLY")
        if route == "O11_ONLY" and st is not None:
            errors.append("Sites target must be null for O11_ONLY")
    if for_o11:
        if task is None:
            errors.append("--for-o11 requires --task tasks/<task-id>")
        if route == "SITES_ONLY":
            errors.append("O11 metadata check requested for SITES_ONLY route")
        o11 = profile.get("o11", {})
        if not isinstance(o11, dict):
            errors.append("o11 must be an object")
            o11 = {}
        for key in ("environment", "module", "module_style"):
            if not filled(o11.get(key)):
                errors.append(f"Missing O11 {key} for implementation metadata")
        if o11.get("module_style") not in {"Reactive", "Traditional", "Mobile"}:
            errors.append("O11 style must be an explicitly identified supported style")
    if not ready and profile.get("profile_status") == "TEMPLATE":
        notes.append("Template profile is expected to be unfilled; not ready for a live task.")
    notes.append("Checks cover package/metadata only: not role discovery, authorization, source semantics, evidence truth, or platform behavior.")
    return errors, notes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--ready", action="store_true")
    parser.add_argument("--task")
    parser.add_argument("--for-o11", action="store_true")
    args = parser.parse_args()
    errors, notes = check(args.root.resolve(), args.ready, args.task, args.for_o11)
    for note in notes:
        print("NOTE:", note)
    for error in errors:
        print("FAIL:", error)
    print("PACKAGE/METADATA:", "FAIL" if errors else "PASS")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
