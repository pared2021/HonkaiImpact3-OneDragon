# AGENTS.md — src/one_dragon

> 全局约束见根目录 [AGENTS.md](../../AGENTS.md)，本文件仅补充模块级指引。

## 模块定位

通用基础框架，提供配置、环境、工具、YOLO 能力等跨项目共用能力。后续目标是转化为独立框架。

## 核心子包

| 子包 | 职责 |
|------|------|
| `base/` | 条件操作引擎、配置体系、上下文、应用系统、Operation 编排 |
| `envs/` | 运行环境与路径管理 |
| `utils/` | 通用工具（图像、时间、文件等） |
| `yolo/` | YOLO 推理封装 |
| `gui/` | 基础 GUI 抽象（非 Qt 实现） |
| `launcher/` | 启动器逻辑 |
| `thread/` | 线程与并发工具 |
| `custom/` | 自定义扩展点 |
| `devtools/` | 开发调试工具 |

## 模块约束

- 本模块是**通用层**，不得引入崩坏3业务逻辑（业务代码在 `src/hi3_od`）。
- `base/conditional_operation/` 是状态机与操作编排核心，修改前务必理解现有状态转换逻辑。
- 配置类继承 `YamlConfig`，新增配置项须有类型注解和默认值。
- GPU/onnx session 调用必须通过 `gpu_executor.submit`，禁止并发直调。

## 关键入口

- 条件操作引擎：`base/conditional_operation/`
- 配置体系：`base/config/`
- 应用系统：`base/operation/`
- YOLO 推理：`yolo/`
