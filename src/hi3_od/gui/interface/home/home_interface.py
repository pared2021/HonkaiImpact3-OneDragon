from __future__ import annotations

from typing import TYPE_CHECKING

from qfluentwidgets import FluentIcon

from one_dragon_qt.widgets.base_interface import BaseInterface

if TYPE_CHECKING:
    from hi3_od.context.hi3_context import Hi3Context


class HomeInterface(BaseInterface):
    """主页"""

    def __init__(self, ctx: Hi3Context, parent=None):
        BaseInterface.__init__(
            self,
            object_name='home_interface',
            nav_text_cn='仪表盘',
            nav_icon=FluentIcon.HOME,
            parent=parent,
        )
        self.ctx = ctx
