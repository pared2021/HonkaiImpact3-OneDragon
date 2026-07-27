# AGENTS.md — src/one_dragon_qt

> 全局约束见根目录 [AGENTS.md](../../AGENTS.md)，本文件仅补充模块级指引。

## 模块定位

通用 Qt GUI 框架与公共组件，基于 PySide6 + pyside6-fluent-widgets，提供 Fluent Design 风格的桌面 UI 能力。

## 核心子包

| 子包 | 职责 |
|------|------|
| `view/` | 页面视图组件 |
| `widgets/` | 可复用 UI 控件 |
| `windows/` | 窗口定义 |
| `services/` | GUI 服务（主题、设置管理等） |
| `overlay/` | 游戏内覆盖层（HUD、日志面板等） |
| `logic/` | 图像分析等 GUI 关联逻辑 |
| `mixins/` | 视图 Mixin（如历史导航） |
| `app/` | 应用入口与开发工具 |
| `utils/` | GUI 工具函数 |
| `_rc/` | 资源文件（QSS 样式、图标等） |

## 模块约束

- GUI 优先复用 `pyside6-fluent-widgets` 与现有项目组件，保持 Fluent Design 风格。
- 本模块是**通用 GUI 层**，不得引入崩坏3业务逻辑（业务界面在 `src/hi3_od/gui/`）。
- 新设置界面优先沿用 setting card、`YamlConfigAdapter`、`AdapterInitMixin` 模式。
- QSS 样式修改在 `_rc/qss/` 对应主题目录下进行，修改后需重新打包资源：`pyside6-rcc resource.qrc -o resource.py`。
- Overlay 相关修改注意 Win32 窗口层级与透明窗口的平台兼容性。

## 关键入口

- 页面视图：`view/`
- 可复用控件：`widgets/`
- 窗口定义：`windows/`
- QSS 样式：`_rc/qss/`
