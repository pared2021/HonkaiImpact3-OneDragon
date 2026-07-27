from PySide6.QtWidgets import QWidget
from qfluentwidgets import SettingCardGroup

from one_dragon_qt.widgets.column import Column
from one_dragon_qt.widgets.vertical_scroll_interface import VerticalScrollInterface
from one_dragon.utils.i18_utils import gt
from hi3_od.context.hi3_context import Hi3Context


class Hi3SettingGameInterface(VerticalScrollInterface):

    def __init__(self, ctx: Hi3Context, parent=None):
        self.ctx: Hi3Context = ctx

        VerticalScrollInterface.__init__(
            self,
            object_name='hi3_setting_game_interface',
            content_widget=None, parent=parent,
            nav_text_cn='游戏设置',
        )

    def get_content_widget(self) -> QWidget:
        content_widget = Column()

        basic_group = SettingCardGroup(gt('游戏基础'))
        content_widget.add_widget(basic_group)
        content_widget.add_stretch(1)

        return content_widget
