"""测试 hi3_od 应用模块结构符合 OneDragon 框架规范"""

import importlib
from pathlib import Path

import pytest

# hi3_od/application 目录
APP_DIR = Path(__file__).parent.parent.parent / 'src' / 'hi3_od' / 'application'

# 需要检查的应用模块（排除非应用模块的文件）
APP_MODULES = [
    'daily_signin',
    'daily_tasks',
    'expedition',
    'reward_collect',
    'battle_assistant',
]


def test_application_modules_exist():
    """每个应用模块目录都存在"""
    for module in APP_MODULES:
        assert (APP_DIR / module).is_dir(), f'缺少应用模块目录: {module}'


def test_const_files_have_required_fields():
    """每个应用的 _const.py 都定义了必需的四个字段"""
    for module in APP_MODULES:
        const_module = importlib.import_module(f'hi3_od.application.{module}.{module}_const')
        assert hasattr(const_module, 'APP_ID'), f'{module}_const 缺少 APP_ID'
        assert hasattr(const_module, 'APP_NAME'), f'{module}_const 缺少 APP_NAME'
        assert hasattr(const_module, 'DEFAULT_GROUP'), f'{module}_const 缺少 DEFAULT_GROUP'
        assert hasattr(const_module, 'NEED_NOTIFY'), f'{module}_const 缺少 NEED_NOTIFY'


def test_factory_files_exist():
    """每个应用都有 _app_factory.py、_app.py、_run_record.py"""
    for module in APP_MODULES:
        module_dir = APP_DIR / module
        assert (module_dir / f'{module}_app.py').is_file(), f'{module} 缺少 _app.py'
        assert (module_dir / f'{module}_app_factory.py').is_file(), f'{module} 缺少 _app_factory.py'
        assert (module_dir / f'{module}_run_record.py').is_file(), f'{module} 缺少 _run_record.py'


def test_factories_are_discoverable():
    """每个应用的工厂类都能被导入且继承 ApplicationFactory"""
    from one_dragon.base.operation.application.application_factory import ApplicationFactory

    for module in APP_MODULES:
        factory_module = importlib.import_module(
            f'hi3_od.application.{module}.{module}_app_factory'
        )
        # 找到模块中的 ApplicationFactory 子类
        factory_classes = [
            obj for name, obj in vars(factory_module).items()
            if isinstance(obj, type) and issubclass(obj, ApplicationFactory)
            and obj is not ApplicationFactory
        ]
        assert len(factory_classes) >= 1, f'{module}_app_factory 中没有 ApplicationFactory 子类'
