# Execution report — <FEATURE-ID>

Standard version: 1.0. Create this for one actual implementation; do not mark checks passed in advance. Link the exact feature spec/version and read the protocol.

## 1. Current status

| Field | Observed value |
| --- | --- |
| Spec path / version | <path/version> |
| CompletionTarget | <target> |
| Work status | NOT_STARTED / IN_PROGRESS / BLOCKED / PARTIAL / TARGET_ACHIEVED |
| Achieved stage | NONE / MODEL_READY / MERGED / RUNTIME_VERIFIED |
| Application / module / environment | <actual identities; UNKNOWN if not observed> |
| Last updated | <actual timestamp/timezone> |
| Next action | <concrete restartable action and owner> |

| Stage | Status | Evidence / reason |
| --- | --- | --- |
| Model verification | NOT_RUN | <evidence/reason> |
| Merge | NOT_REQUESTED | <requested/pending/accepted/rejected/failed/unknown outcome> |
| Publish | NOT_REQUESTED | <environment/version/result or reason> |
| Runtime verification | NOT_RUN | <version/check result or reason> |

## 2. Baseline and changed objects

Baseline/checkpoint: <observed errors/warnings, relevant pending state and actual checkpoint identity>.

| Object / module | Created / reused / modified | Req IDs | Observed change | Evidence IDs |
| --- | --- | --- | --- | --- |
| <object> | <operation> | <IDs> | <actual result> | <EV-IDs> |

## 3. Progress and gates

| Milestone | Status: NOT_STARTED / IN_PROGRESS / COMPLETE / BLOCKED / NOT_IN_SCOPE | Work completed / remaining | Gate and evidence |
| --- | --- | --- | --- |
| <M-ID> | <status> | <details> | <G-ID/EV-IDs> |

Do not mark a milestone COMPLETE while a required exit check is failed, blocked or unexecuted. A skipped phase needs NOT_IN_SCOPE and the actual authorization/scope source.

## 4. Requirement coverage and checks

| Req ID | Implemented object | AC ID | TC ID | Result | Evidence / gap |
| --- | --- | --- | --- | --- | --- |
| <Req-ID> | <object> | <AC-ID> | <TC-ID> | NOT_RUN | <EV-ID or reason> |

| Check ID | Actual preconditions / version / fixture | Expected | Observed | Result | Evidence IDs |
| --- | --- | --- | --- | --- | --- |
| <TC-ID> | <actual state> | <expected> | <actual observation> | NOT_RUN | <IDs/reason> |

Allowed results: PASS / FAIL / NOT_RUN / BLOCKED / N/A. PASS requires evidence. N/A requires a legitimate applicability reason and must not contradict the spec. If a check has several relevant modes/roles/states, record the cases separately.

## 5. Evidence register

| Evidence ID | Captured time/timezone | Subject: snapshot / live model / published runtime | Method and actual observation | Version / artifact or tool-result reference |
| --- | --- | --- | --- | --- |
| EV-001 | <actual time> | <subject> | <concise observed fact> | <real locator or “session observation; no persistent log ID”> |

Store only evidence needed to assess the change. Do not copy tokens, credentials or personal data. Evidence of mutation success alone cannot pass a visual/behavioral test.

## 6. Discoveries, deviations and decisions

| Item | Observation / deviation | Impacted IDs | Resolution / linked spec decision |
| --- | --- | --- | --- |
| <item> | <fact> | <IDs> | <resolution/DEC-ID> |

Record material spec changes in the spec's version/decision log too. Keep assumptions labeled; successful implementation does not confirm a business rule.

## 7. Recovery and resume

Current pending-work disposition: <none/staged/merge pending/unknown; evidence>.

Recoverable checkpoint/artifacts: <actual references; no tokens>.

Resume procedure: <current target, source versions, completed milestones, next safe operation, required re-reads>.

## 8. Handoff

Selected target achieved? <YES / NO with gate/check evidence>.

Delivered: <actual objects/artifacts>.

Unmet MUST requirements/checks: <IDs or NONE, justified by coverage>.

Remaining untested behavior: <checks/reasons>.

Next user/agent action: <minimal concrete step>.

Outcome and lesson: <short factual conclusion, improvement to carry forward>.

## UI contract evidence (when applicable)

Link the single canonical UI contract, foundation revision and actual design acceptance. Report native mapping/instances separately from served theme/font/token, behavior/access and visual checks on an identified runtime. Metadata PASS proves none of these. Reuse valid evidence by locator and record changed deltas only.
