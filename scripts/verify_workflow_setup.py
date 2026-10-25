#!/usr/bin/env python3
"""Read-only workspace verification plus disposable metadata fixtures. No platform calls."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    spec = importlib.util.spec_from_file_location('workflow_check', ROOT / 'scripts/check_workspace.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    cases = []

    def record(name, errors, expect_error=None):
        ok = not errors if expect_error is None else any(expect_error in e for e in errors)
        cases.append({'case': name, 'result': 'PASS' if ok else 'FAIL', 'observed': errors})

    record('Installed package and draft metadata', module.check(ROOT)[0])
    record('Draft cannot be ready', module.check(ROOT, ready=True)[0], 'profile_status must be ACTIVE')
    with tempfile.TemporaryDirectory(prefix='vibe-metadata-fixtures-') as tmp:
        target = Path(tmp)
        names = set(module.REQUIRED + ['project.json', 'templates/TASK_STATE.template.json'])
        names.update(str(p.relative_to(ROOT)) for p in (ROOT / '.codex/agents').glob('*.toml'))
        for name in names:
            dst = target / name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / name, dst)
        profile = json.loads((target / 'project.json').read_text(encoding='utf-8'))
        profile.update(project_id='SYNTHETIC-METADATA-ONLY', display_name='Disposable validator fixture', profile_status='ACTIVE')
        profile['o11'].update(environment='SYNTHETIC-NO-ENDPOINT', module='SYNTHETIC-NO-MODULE', module_style='Reactive')
        (target / 'project.json').write_text(json.dumps(profile), encoding='utf-8')
        task_path = target / 'tasks/METADATA-ONLY'
        task_path.mkdir(parents=True)
        for name in ('brief.md', 'spec.md', 'report.md'):
            (task_path / name).write_text('Synthetic validator metadata only. No feature or authorization.', encoding='utf-8')
        state = json.loads((target / 'templates/TASK_STATE.template.json').read_text(encoding='utf-8'))
        state.update(project_id=profile['project_id'], task_id=task_path.name, spec_revision='fixture-1.0', delivery_route='O11_ONLY', active_surface='LOCAL', o11_target='MODEL_REVIEW')

        def run(**kwargs):
            (task_path / 'task-state.json').write_text(json.dumps(state), encoding='utf-8')
            return module.check(target, ready=True, task='tasks/METADATA-ONLY', **kwargs)[0]

        record('Hybrid profile permits O11-only task metadata', run(for_o11=True))
        state['project_id'] = 'WRONG-PROJECT'
        record('Cross-project task rejected', run(), 'Task project_id does not match')
        state['project_id'] = profile['project_id']
        state['o11_target'] = 'INVENTED-TARGET'
        record('Invalid target rejected', run(), 'Invalid O11 target')
        state['o11_target'] = None
        record('O11 implementation requires target', run(for_o11=True), 'Valid O11 target is required')
        state['o11_target'] = 'MODEL_REVIEW'
        state['sites_target'] = 'LOCAL_REVIEW'
        record('O11-only task rejects Sites target', run(), 'Sites target must be null')
        state['sites_target'] = None
        record('Task path outside tasks rejected', module.check(target, task='../outside')[0], 'Task path must be inside')
        shutil.copy2(target / '.codex/agents/analyst.toml', target / '.codex/agents/duplicate.toml')
        record('Duplicate role rejected', module.check(target)[0], 'Duplicate role: analyst')
    print(json.dumps({'subject': 'Package and disposable metadata fixtures; no role discovery/platform behavior', 'cases': cases}, indent=2))
    return int(any(c['result'] != 'PASS' for c in cases))


if __name__ == '__main__':
    raise SystemExit(main())
