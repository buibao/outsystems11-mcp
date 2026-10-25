# Vibe Workflow — Sites + O11, v1.0

Workspace integration: installed locally on 2026-10-23. See [setup report](docs/execution/VIBE-SETUP.report.md) and [first-task guide](docs/VIBEWORKFLOW_QUICKSTART.md) for actual discovery, read-only preflight and remaining limits. The generic kit text below is not an end-to-end verification claim. That setup-time binding is historical; read [project.json](project.json) and the selected task for current identity. Native-first v1.1 integration is documented in the [new setup report](docs/execution/NATIVE-FIRST-SETUP.report.md).

Bộ khởi đầu cho quy trình multi-agent dùng lại giữa nhiều project. Một workflow core, hai adapter thực thi và một profile riêng cho mỗi project. Đây là template đã được kiểm tra cấu trúc, chưa phải một hệ thống đã cài/chạy end-to-end trên máy Windows của bạn.

## Cách dùng

1. Tạo workspace nghiệp vụ riêng cho project mới từ bộ này. Với workspace đang có, so sánh và tích hợp có chọn lọc; không ghi đè AGENTS/config và không sửa upstream distribution.
2. Điền `project.json`: chọn default route `HYBRID_SITES_O11`, `SITES_ONLY` hoặc `O11_ONLY`. Đặt project ID riêng và references/design system/boundaries đúng project. Không đưa credential/token vào profile.
3. Tạo `tasks/<task-id>/` theo các file trong `templates/`. Tạo `task-state.json`, `brief.md`, `spec.md`, `report.md`; các handoff/plans tạo khi giai đoạn đó áp dụng. Điền task-state project ID trùng profile và chọn `delivery_route` của task (có thể O11_ONLY trong project HYBRID). Mọi giá trị chưa biết phải là UNKNOWN/null rõ ràng, không suy đoán.
4. Đọc `SETUP.md` để tích hợp role configs vào Codex local và xác minh discovery. Work dùng cùng role briefs trong `workflow/ROLES.md`; không mặc định Work đọc TOML local.
5. Giao task bằng prompt trong `prompts/START.md`, `WORK_TO_LOCAL.md` hoặc `RESUME.md`. Coordinator chọn các agent cần dùng cho stage hiện tại, không spawn cả đội ngay khi bắt đầu.
6. Chạy `python scripts/check_workspace.py` để kiểm tra cấu trúc; sau khi điền profile/task dùng `python scripts/check_workspace.py --ready --task tasks/<task-id>`. Thêm `--for-o11` trước triển khai O11 để kiểm tra metadata target cần thiết. Đây chỉ là check file/metadata, không xác minh quyền hay model/runtime O11.

## Vai trò của hai môi trường

| Môi trường | Vai trò |
| --- | --- |
| ChatGPT Work + Sites | Làm rõ yêu cầu, thiết kế/prototype, kiểm tra trải nghiệm và xuất gói design handoff có phiên bản |
| Codex local + O11 MCP | Đọc module thật, chuyển contract sang Screen/Block/Structure/Action, thực hiện và kiểm chứng thay đổi O11 |

Sites là implementation web độc lập. Không có bước tự động import HTML/JSX thành OML trong bộ này. Prototype behavior không thay thế runtime behavior của O11.

## Bốn lớp tách biệt

- `workflow/`: quy trình, phân vai, gate, dispatch/handoff contract; không chứa dữ liệu dự án.
- `adapters/`: quy tắc đặc thù Sites và O11; gọi official skill/công cụ hiện hành, không sao chép toàn bộ API contract.
- `project.json`: danh tính và context bền vững của đúng một project.
- `tasks/<task-id>/`: yêu cầu, quyết định, state, report và evidence của đúng task.

Mỗi project một workspace và Work conversation/Site identity riêng khi phù hợp. Không copy session token, Site identity hoặc task state cũ sang project mới.

## Phân vai và concurrency

Primary coordinates, plans and implements, with one independent reviewer at meaningful milestones. Other roles are optional for concrete independent outputs, not a seven-role relay. See [lean workflow](docs/standards/LEAN_UI_WORKFLOW.md) and [native-first](docs/standards/O11_UI_NATIVE_FIRST.md).

O11 operator là primary local session: một operator/module, giữ token trong memory và thực hiện mọi O11 MCP calls. Builder chuẩn bị mutation/code và checklist từ snapshot; reviewer/QA nhận evidence có nhãn pending/live/published. Với Sites, primary Work conversation sở hữu checkout, Site identity, native calls và publication; worker được giao source/assets/review có phạm vi.

Chỉ Coordinator tại `active_surface` cập nhật task state/spec/report chính. Bàn giao Work → local đóng băng revision và bên nhận xác nhận trước khi tiếp tục; một file state copy không tự đồng bộ giữa hai môi trường.

Role instructions không tạo sandbox/tool permission riêng. Không chuyển credential hay token cho worker. Work và local không mặc định chia sẻ memory, filesystem, tools hoặc custom-agent definitions.

## Điều kiện coi bộ setup đã vận hành

- Role configs được discover trên Codex đang cài; worker trả đúng contract.
- Hai bên Work/local mở được cùng phiên bản handoff và nhận diện đúng project/task.
- Một task đại diện đi qua model review/merge/runtime theo CompletionTarget đã chọn.
- Resume sau gián đoạn và chuyển sang project thử nghiệm khác không mang nhầm state/identity.
- Các check chưa chạy vẫn ghi NOT_RUN/BLOCKED. Xem `VERIFICATION.md`.

## Nguồn chính thức

- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://learn.chatgpt.com/docs/config-file/config-reference
- https://learn.chatgpt.com/docs/learn/best-practices
- https://success.outsystems.com/documentation/11/outsystems_mcp/security_and_data_handling/
- https://success.outsystems.com/documentation/11/outsystems_mcp/outsystems_mcp_capabilities/

Role/config syntax đối chiếu tài liệu ngày 23/10/2026. Kiểm tra lại phiên bản/client trước khi áp dụng. Skill Sites đang cài tại thời điểm thực thi quyết định source/preview/publication workflow.
