from qfluentwidgets import FluentIcon
from typing import List

from one_dragon_qt.widgets.pivot_navi_interface import PivotNavigatorInterface
from one_dragon_qt.widgets.setting_card.app_run_card import AppRunCard
from hi3_od.context.hi3_context import Hi3Context
from hi3_od.gui.interface.one_dragon.hi3_one_dragon_run_interface import Hi3OneDragonRunInterface


class Hi3OneDragonInterface(PivotNavigatorInterface):

    def __init__(self, ctx: Hi3Context, parent=None):
        self.ctx: Hi3Context = ctx
        PivotNavigatorInterface.__init__(
            self,
            nav_icon=FluentIcon.BUS,
            object_name='one_dragon_interface',
            parent=parent,
            nav_text_cn='一条龙',
        )

        self._app_run_cards: List[AppRunCard] = []

    def create_sub_interface(self):
        self.add_sub_interface(Hi3OneDragonRunInterface(self.ctx))
