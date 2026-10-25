# Tax Documents Preview — implementation and evidence

Current correction: [UI-002 v1.1](specs/UI-002-tax-documents-visual-fidelity.md), [execution report](execution/UI-002.report.md). CompletionTarget RUNTIME_VERIFIED achieved on Development MyApp versionSequence 135 after user manual publish. 34 browser checks passed; 12 corresponding screenshots and an interactive [comparison gallery](../artifacts/ui-002/comparison.html) are available. Scoped blue hierarchy and compact layout are implemented; minor typography/icon/copy differences remain disclosed. Startup and dialog defects resolved; favicon404 tracked separately. Historical roles/lifecycle/publish statements below are superseded by UI-002.

Corrective styling contract, version 1.1 (2026-10-22): [CSS-001 spec](specs/report/O11_CSS_Refactor_and_Project_Rules.md), [execution report](execution/CSS-001.report.md). The initial implementation below is historical. CSS-001 targets the connected MyApp key `5f28b208-ec42-4a32-a28d-c0e74109dfa5`, inherits MyApp typography/primary color, preserves native framework classes, reuses Content/Tag and native Popup inside existing Blocks, and places scoped shared rules in the application theme. It supersedes the initial Screen-only stylesheet decision. Publish and runtime are separately evidenced in the correction report; the reducer error is [DEF-001](defects/DEF-001-tax-preview-reduce.md).

Ngày 22/10/2026, Asia/Saigon. Target: `MyApp` / `31528bde-1c02-46e6-ac4b-2d14a432e584`, Reactive.

Người dùng yêu cầu đọc toàn bộ `D:/Downloads/O11_TaxDocuments_UI_Codex_Prompt.md` và thực hiện trong module kết nối. Đã đọc toàn bộ prompt và xem đủ 12 PNG trong ZIP. Người dùng xác nhận manual Compare and Merge; khi được hỏi điểm khôi phục, trả lời “Không cần thiết”. Không yêu cầu publish.

## Thành phần

- Một Screen mới: `MainFlow/TaxDocumentsPreview`. Chỉ có Registered, không thêm Anonymous hoặc role mới. Hai Screen cũ `Login`, `InvalidPermissions` được giữ nguyên.
- Chín Block mới: `DocumentTypeTabs`, `DocumentYearList`, `DocumentYearCard`, `DocumentStatusBadge`, `DocumentUploadPanel`, `DocumentFileRow`, `DocumentTrackingTimeline`, `ReminderControls`, `YearSelectionDialog`.
- Static Entity mới: `DocumentType` (COR, PEL), `DocumentStatus` (PendingUpload, PendingReview, Accepted, Rejected, NotProvidable, NotProvidableReview). Conditions dùng identifier.
- Structure mới: `DocumentFileVM`, `TrackingEventVM`, `YearOptionVM`, `YearDocumentVM`, `PreviewScenarioVM`, `TaxPreviewStateVM`. Tracking có thêm FileName cho link mẫu độc lập với draft.
- Script nội bộ `TaxDocumentsPrototype` xử lý dữ liệu demo, hỗ trợ native Upload và focus dialog; không render HTML, không network, không storage.
- Dùng các List/widget/Button/Input/Block/Event native. Screen sở hữu state; Block phát RequestCommand, RequestKey, RequestPayload qua event; RequestKey là DocumentKey ổn định. Mở thẻ/Tracking, draft, coverage và reminder được giữ theo key. Không gán vào input Block để lưu thay đổi.
- CSS chỉ nằm trong stylesheet mới của Screen, scope `.tax-documents-preview`. Không thay theme. Lần ghi stylesheet đầu tiên vào một Screen mới có stylesheet rỗng; đã đọc lại model, chưa xác minh CSS được triển khai.
- Không tạo persisted Entity, business CRUD Server Action, integration, migration, reminder hoặc approval thật. Local Server Actions vẫn chỉ có DoLogin/DoLogout. Không refresh reference, reset hoặc publish. Không cần bước Manage Dependencies.

## Preset

| Chọn trong Preview controls | Trạng thái |
| --- | --- |
| All states | Composite showcase: 2024 Not Providable; 2025 Pending Upload; 2026 Pending Review; 2027 Rejected; 2028 Accepted; 2029 Not Providable Review; có cả COR/PEL |
| 021657 | Reviewer, thẻ đóng, năm 2026 suspended |
| 021744 | Reviewer heading, compact Browse, Resume Reminder, Tracking mở |
| 021825 | Rejected đang sửa, file mẫu, chọn năm, Cancel/Submit |
| 021855 | Rejected chỉ đọc, banner, Remove and Resubmit, lịch sử |
| 021920 | Reviewer rejected và Tracking |
| 021939 | Accepted, lịch sử một file cho nhiều năm |
| 022000 | Unavailability rejected trong lịch sử; hiện tại Pending Upload |
| 022019 | Unavailability approved; Not Providable |
| 022033 | Not Providable Review; warning, Reject/Approve |
| 022107 | Pending Review; Tracking đóng, nhiều năm chờ review |
| 022129 | Heading PEL, thẻ 2024–2029 |
| 022146 | Pending Upload, file mẫu, nhiều năm, Clear All/Submit |

Không bỏ preset nào. Thay preset/reset khôi phục fixture có chủ đích; đổi tab giữ state tab kia.

## Hành vi và giới hạn

Browse là native Upload; phần hỗ trợ drop chỉ thao tác input file của Block hiện tại. Kiểm tra pdf/doc/docx/jpg/jpeg/png, file không rỗng và tối đa 10 MiB (10 MB theo nhãn ảnh). Binary Data là biến tạm và được giải phóng sau khi thu metadata. Không giữ nội dung file để tải lại. Thao tác link mẫu/specimen hiện thông báo prototype rõ ràng; không dùng URL hỏng hoặc PDF giả.

Clear All chỉ xóa file/coverage draft của tài liệu đó; năm chính luôn được giữ. Cancel phục hồi snapshot trước sửa. Submit giả lập Pending Review. Resubmit giữ lịch sử. Popup coverage giữ draft chưa submit; Cancel không đổi coverage. Suspend/Resume và request/review chỉ đổi state trong bộ nhớ. Lịch sử là fixture, không phải audit thật.

Popup chọn năm, form reason, focus trap và composite showcase là phần bổ sung theo prompt, không phải thiết kế được chứng minh trong ảnh. Văn bản nhỏ, ngày giờ và tên file là sample gần đúng. Không tái tạo khung đỏ, viền đen hoặc capture edges.

## Verification

| Kiểm tra | Kết quả / bằng chứng |
| --- | --- |
| Đọc prompt và 12 ảnh | PASS; ảnh được extract có kiểm tra path dưới `artifacts/tax-documents/reference` |
| Readback model | PASS; getScreen/getWebBlock/runQuery đọc lại Screen, Card, Upload, Tracking, inventory và event arguments |
| Inventory | PASS; đúng một MobileScreen thêm vào MainFlow, 9 MobileBlock, 2 StaticEntity và 6 Structure |
| Validation | 0 lỗi, 3 warning; baseline 0 lỗi/2 warning |
| Warning mới | Missing roles ở TaxDocumentsPreview, cùng rule với hai Screen cũ. Readback có Registered và AnonymousAccess=false. Skill patterns-by-element ghi nhận warning này trong module không có app role riêng. Không mở Anonymous hoặc tạo role để xóa warning |
| Logic demo | PASS: `node artifacts/tax-documents/check-reducer.cjs` — 13 scenario, hai tab độc lập, keyed edits, invalid extensions/size, primary-year protection, Confirm/Cancel, submit/resubmit/history, request/review, reminder và deterministic reset |
| JavaScript syntax | PASS: `node --check artifacts/tax-documents/TaxDocumentsPrototype.js` |
| Flow layout | PASS model: BFS toàn bộ action mới, kiểm tra connector/đích và node reachable; đặt tọa độ từng tầng. Không chạy Server Action |
| UI events/file picker/drop | Đã nối và đọc lại model; browser end-to-end NOT RUN |
| Responsive / keyboard / focus / tooltip | Đã tạo CSS/attributes/focus handlers; runtime NOT RUN |
| So sánh pixel với ảnh | NOT RUN; chưa publish/chưa có runtime phiên bản mới |
| Allowed/denied screen access | Model có Registered, không Anonymous; runtime allowed/denied NOT RUN |
| Merge | PASS — `merged: true`, “All of the agent's changes were merged.” |
| Live readback sau merge | PASS — checkout mới từ module live, không mutation; inventory đúng, Registered và AnonymousAccess=false, CSS scoped, vẫn 0 lỗi/3 warning. Sau đó đã end session với discardedChanges=false |
| Native Script references sau merge | PASS — đọc typed Model API xác nhận TaxDocumentsPrototype tồn tại và nằm trong RequiredScripts của Screen, Upload panel và Dialog; probe chỉ đọc, mutatedOmlPath rỗng |
| Publish | NOT RUN, không được yêu cầu; omlPublish không có trong catalog hiện tại |

Kết quả kiểm tra hàm JavaScript cục bộ không thay thế kiểm thử trong browser của OutSystems. Model validation không chứng minh hành vi runtime hoặc độ giống ảnh. Evidence: [bản làm việc trước merge](evidence/tax-documents-model.json), [bản live sau merge](evidence/tax-documents-live.json).

MCP đã báo thiếu snapshot tạm ở lần đọc ngay sau end phiên triển khai. Không replay merge; mở một edit session mới để checkout từ live, chỉ đọc kiểm chứng, rồi end với discardedChanges=false. Không thay đổi model trong phiên kiểm chứng này.

## Preview sau khi developer publish

1. Chấp nhận diff Compare and Merge nếu phù hợp. Chỉ publish thủ công khi được phép.
2. Trong Service Studio, chọn `MainFlow/TaxDocumentsPreview`, mở Screen trong browser và đăng nhập bằng tài khoản sẵn có. Không đổi default/home Screen.
3. Dùng Preview controls để chọn All states hoặc từng suffix ảnh ở bảng trên. Mở nhiều thẻ năm, mở/đóng Tracking độc lập; đổi COR/PEL rồi trở lại để kiểm tra state.
4. Kiểm tra upload file hợp lệ, file sai đuôi, file quá 10 MB, Browse và drop; remove, Clear All, Cancel; chọn năm và bảo vệ năm chính; submit, resubmit và lịch sử.
5. Kiểm tra Suspend/Resume, request reason/years và Reject/Approve ở preset 022033. Kiểm tra Reset demo trở về fixture ban đầu.
6. So ảnh ở khoảng 900 px, màn rộng và màn hẹp; kiểm tra wrap filename/buttons, Tab/Shift+Tab, focus dialog và truy cập cho tài khoản đăng nhập/không đăng nhập. Ghi nhận actual result, không đánh dấu các bước chưa chạy là pass.

Build scripts, reducer checks và nguồn mẫu nằm ở `artifacts/tax-documents/`. Các file C# là các giai đoạn tạo model có thứ tự, không phải build pipeline cho OML và không nên replay lên module đã có các đối tượng đó. Upstream `outsystems11-mcp` không được sửa.
