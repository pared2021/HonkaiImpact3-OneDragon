# 第三方插件目录

此目录用于放置第三方插件。

## 特性

- **相对导入**：`from .utils import xxx`
- **导入主程序模块**：`from one_dragon.xxx import yyy`, `from hi3_od.xxx import yyy`
- **支持子包**：可以有多层目录结构

## 加载机制

加载插件时，`plugins/` 目录会被添加到 `sys.path`，使每个插件包成为独立的顶级模块。

```python
# 加载过程
sys.path.insert(0, "project_root/plugins")  # 添加一次
# 插件模块名示例
# plugins/my_plugin/my_plugin_factory.py     -> my_plugin.my_plugin_factory
# plugins/my_plugin/sub/sub_factory.py       -> my_plugin.sub.sub_factory
```

## 目录结构示例

```
plugins/                          # 被添加到 sys.path
├── README.md
├── plugin_a/                     # 插件 A
│   ├── __init__.py               # 推荐添加
│   ├── plugin_a_const.py         # 定义 APP_ID, APP_NAME, DEFAULT_GROUP, NEED_NOTIFY
│   ├── plugin_a_factory.py       # 工厂类（必须以 _factory.py 结尾）
│   ├── plugin_a.py               # 应用实现
│   └── utils/                    # 子包
│       ├── __init__.py
│       └── helper.py
└── plugin_b/                     # 插件 B
    ├── __init__.py
    ├── plugin_b_const.py
    └── plugin_b_factory.py
```

## 开发指南

### 1. 创建插件目录

在 `plugins/` 下创建以插件名命名的目录，如 `plugins/my_plugin/`。

### 2. 定义常量文件

创建 `my_plugin_const.py`，定义应用的基本信息：

```python
# plugins/my_plugin/my_plugin_const.py

APP_ID = "my_plugin"
APP_NAME = "我的插件"
DEFAULT_GROUP = True  # True: 显示在一条龙列表，False: 独立工具
NEED_NOTIFY = True    # 是否需要通知

# 插件元数据（可选，用于 GUI 显示）
PLUGIN_AUTHOR = "作者名"
PLUGIN_HOMEPAGE = "https://github.com/author/my_plugin"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "插件功能描述"
```

### 3. 创建工厂类

创建 `my_plugin_factory.py`（**文件名必须以 `_factory.py` 结尾**）：

```python
# plugins/my_plugin/my_plugin_factory.py

from one_dragon.base.operation.application.application_factory import ApplicationFactory
from hi3_od.context.hi3_context import Hi3Context  # 导入主程序模块
from . import my_plugin_const      # 相对导入
from .my_plugin import MyPlugin    # 相对导入


class MyPluginFactory(ApplicationFactory):
    def __init__(self, ctx: Hi3Context):
        ApplicationFactory.__init__(self, my_plugin_const)
        self.ctx = ctx

    def create_application(self, instance_idx, group_id):
        return MyPlugin(self.ctx)
```

### 4. 实现应用逻辑

```python
# plugins/my_plugin/my_plugin.py

from hi3_od.application.hi3_application import Hi3Application
from hi3_od.context.hi3_context import Hi3Context


class MyPlugin(Hi3Application):
    def __init__(self, ctx: Hi3Context):
        Hi3Application.__init__(self, ctx, "my_plugin", node_max_retry_times=3)
```

## 注意事项

1. **文件命名**：工厂文件必须以 `_factory.py` 结尾
2. **必需字段**：const 文件必须定义 `APP_ID`, `APP_NAME`, `DEFAULT_GROUP`, `NEED_NOTIFY`
3. **`__init__.py`**：建议添加以支持相对导入
4. **模块名唯一**：插件包名（目录名）应该唯一，避免与其他插件或主程序模块冲突
5. **热重载**：刷新应用时会卸载整个插件包并重新加载
6. **嵌套目录**：支持在插件包内任意深度放置 `_factory.py` 文件
