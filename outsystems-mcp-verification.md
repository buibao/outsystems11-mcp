# Xác minh kết nối Codex – OutSystems 11

- MCP server: `servicestudio`
- URL do người dùng xác nhận trong cửa sổ Service Studio: `http://127.0.0.1:41820/mcp`.
- Port 41820 được tiến trình ServiceStudio.exe (PID 19532 tại thời điểm kiểm tra) lắng nghe trên 127.0.0.1.
- Cấu hình: `C:\Users\buiba\.codex\config.toml`; đã đổi tên entry `outsystems` sang `servicestudio`, giữ nguyên các giá trị khác.
- Bản sao lưu: `C:\Users\buiba\.codex\config.toml.backup-20261022-011831`.
- Repository: https://github.com/OutSystems/outsystems11-mcp
- Commit: `80263e4948493847249a62a80b09455889c7b2f0` (đã fetch và khớp origin/main tại lúc cài).
- Skill: `C:\Users\buiba\.agents\skills\servicestudio-mcp-oml`.
- Model được đọc thành công qua kết nối MCP đang hoạt động của phiên hiện tại (namespace cũ `outsystems`). Khởi động phiên Codex mới để nạp tên `servicestudio` và skill vừa cài.
- Chỉ gọi createSessionToken, listApps, getDataModel và getActionNames; không sửa model, merge, refresh hoặc publish.

## Module đang mở

`MyApp` — `Reactive`, `isOpen: true`, `isReference: false`.

## Entities

`getDataModel` trả về 57 Entities tham chiếu; không trả về Entity được định nghĩa cục bộ trong MyApp.

### OutSystemsUI (35)

- `AccordionIconPosition`
- `AccordionIconType`
- `Alert`
- `AnimationType`
- `Autoplay`
- `BooleanTypes`
- `BreakColumns`
- `CarouselDirection`
- `CarouselNavigation`
- `Color`
- `ColumnBreak`
- `DatePickerLanguage`
- `DatePickerTimeFormat`
- `DatePickerWeekDay`
- `DeviceResponsive`
- `Direction`
- `FloatingPosition`
- `Gradient`
- `GutterSize`
- `MenuAction`
- `MessageStatus`
- `Month`
- `Orientation`
- `Position`
- `ScrollbarStyle`
- `Shape`
- `SideMenuBehavior`
- `Size`
- `Space`
- `Speed`
- `StackedCardsPosition`
- `Steps`
- `StepsBehaviour`
- `Trigger`
- `VideoState`

### (System) (9)

- `Activity`
- `Espace`
- `Group`
- `Process`
- `Role`
- `RuntimeKind`
- `Sent_Email`
- `Tenant`
- `User`

### OutSystemsCharts (7)

- `AxisValuesType`
- `HighchartModules`
- `LegendLayout`
- `LegendPosition`
- `SeriesType`
- `StackingType`
- `ValuesType`

### OutSystemsMaps (6)

- `MapErrors`
- `MapEventTriggered`
- `MarkerEventTriggered`
- `Style`
- `Type`
- `Zoom`

## Server Actions

25 action: 2 cục bộ và 23 tham chiếu.

### Cục bộ

- `DoLogin`
- `DoLogout`

### Tham chiếu

- `AbortTransaction`
- `CommitTransaction`
- `GetGoogleMapsServerKey`
- `ListAll`
- `ListAny`
- `ListAppend`
- `ListAppendAll`
- `ListClear`
- `ListDuplicate`
- `ListFilter`
- `ListIndexOf`
- `ListInsert`
- `ListRemove`
- `ListSort`
- `LogMessage`
- `Login`
- `Logout`
- `SetCurrentLocale`
- `User_GetName`
- `User_GetUnifiedLoginUrl`
- `User_GetUnifiedLogoutUrl`
- `User_Login`
- `User_Logout`

## Tiếp tục sau khi khởi động lại

Giữ Service Studio và MyApp mở, MCP Server đang chạy. Mở phiên Codex mới (nếu chưa nạp cấu hình thì reload cửa sổ VS Code), kiểm tra skill servicestudio-mcp-oml và server servicestudio. Có thể yêu cầu: “Dùng servicestudio, chỉ đọc module đang mở và liệt kê Entities, Server Actions; không sửa hoặc publish.”

## Tài liệu

- https://github.com/OutSystems/outsystems11-mcp/blob/main/setup-docs/codex.md
- https://learn.chatgpt.com/docs/extend/mcp?surface=cli
- https://learn.chatgpt.com/docs/build-skills

