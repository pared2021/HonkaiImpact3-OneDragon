# 开发文档

崩坏三一条龙（HonkaiImpact3-OneDragon）开发文档。

## 目录结构

- `develop/` - 开发相关文档

## 架构说明

项目采用与 ZenlessZoneZero-OneDragon / StarRailOneDragon 一致的三层架构：

```
src/
├── one_dragon/       # 第一层：通用基础框架（Operation引擎、控制器、匹配器、YOLO推理）
├── one_dragon_qt/    # 第二层：PySide6 GUI 框架
└── hi3_od/           # 第三层：崩坏三业务层
    ├── context/      # 上下文（Hi3Context）与控制器
    ├── config/       # 游戏/模型配置
    ├── application/  # 应用模块（每个应用含 const/app/factory/run_record 四件套）
    ├── operations/   # 通用操作
    └── gui/          # GUI 入口与界面
```

## 开发规范

1. 业务逻辑只写在 `src/hi3_od/`，不修改框架层。
2. 新增应用遵循四件套模式，由框架自动发现注册。
3. 配置以 YAML 为主，位于 `config/`。

## 运行

```shell
uv sync --group dev
uv run python main.py
```
