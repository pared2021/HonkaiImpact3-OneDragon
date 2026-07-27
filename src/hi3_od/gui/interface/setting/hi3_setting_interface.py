from qfluentwidgets import FluentIcon

from one_dragon_qt.view.setting.setting_custom_interface import SettingCustomInterface
from one_dragon_qt.view.setting.setting_env_interface import SettingEnvInterface
from one_dragon_qt.widgets.pivot_navi_interface import PivotNavigatorInterface
from hi3_od.context.hi3_context import Hi3Context
from hi3_od.gui.interface.setting.hi3_setting_game_interface import Hi3SettingGameInterface


class Hi3SettingInterface(PivotNavigatorInterface):

    def __init__(self, ctx: Hi3Context, parent=None):
        self.ctx: Hi3Context = ctx
        PivotNavigatorInterface.__init__(self, object_name='hi3_setting_interface', parent=parent,
                                         nav_text_cn='设置', nav_icon=FluentIcon.SETTING)

    def create_sub_interface(self):
        """创建下面的子页面"""
        self.add_sub_interface(Hi3SettingGameInterface(ctx=self.ctx))
        self.add_sub_interface(SettingEnvInterface(ctx=self.ctx))
        self.add_sub_interface(SettingCustomInterface(ctx=self.ctx))
