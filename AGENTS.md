# AGENTS.md

本文件是项目与 AI 编码协作的入口，只保留会直接影响实现落点与提交流程的约束。

## 项目概述

- 项目：崩坏三一条龙（HonkaiImpact3-OneDragon），面向 Windows 的崩坏三自动化工具。
- 语言与环境：Python 3.11、uv、PySide6。
- 代码布局：`src-layout`，源码在 `src/`，运行时配置在 `config/`，资源在 `assets/`，开发文档在 `docs/develop/`。
- 运行基准：1080p；配置以 YAML 为主。
- 架构对齐 ZenlessZoneZero-OneDragon / StarRailOneDragon 的三层结构：
  - `src/one_dragon/`：通用基础框架（不改动）
  - `src/one_dragon_qt/`：PySide6 GUI 框架（不改动）
  - `src/hi3_od/`：崩坏三业务层（只改这里）

## 常用命令

```shell
uv sync --group dev
uv run python main.py
uv run pytest tests/
uv run ruff check src/hi3_od/
uv run ruff check --fix src/hi3_od/
```

## 核心约束

1. **三层架构**：业务逻辑只写在 `src/hi3_od/`，不修改 `one_dragon/` 和 `one_dragon_qt/`。
2. **应用模块四件套**：每个应用包含 `_const.py`（APP_ID/APP_NAME/DEFAULT_GROUP/NEED_NOTIFY）、`_app.py`（继承 Hi3Application，用 `@operation_node`/`@node_from` 装饰器）、`_app_factory.py`（继承 ApplicationFactory）、`_run_record.py`（继承 AppRunRecord）。
3. **应用自动发现**：应用工厂由框架扫描 `src/hi3_od/application/` 下的 `*_factory.py` 自动注册，不要在 Context 中手动 register。
4. **GUI 界面**：继承正确基类并传 `object_name`/`nav_text_cn`/`nav_icon`（如 PivotNavigatorInterface、VerticalScrollInterface）。
5. **不添加框架外功能**：严格对齐参考项目，不添加抽卡模拟器、数据助手等参考项目中不存在的功能。
