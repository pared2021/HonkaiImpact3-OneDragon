from __future__ import annotations

from typing import TYPE_CHECKING

from one_dragon.base.operation.operation_edge import node_from
from one_dragon.base.operation.operation_node import operation_node
from one_dragon.base.operation.operation_round_result import OperationRoundResult
from one_dragon.utils.i18_utils import gt
from hi3_od.application.expedition import expedition_const
from hi3_od.application.hi3_application import Hi3Application

if TYPE_CHECKING:
    from hi3_od.context.hi3_context import Hi3Context


class ExpeditionApp(Hi3Application):
    """远征"""

    def __init__(self, ctx: Hi3Context):
        Hi3Application.__init__(
            self, ctx, expedition_const.APP_ID,
            op_name=gt('远征'),
            run_record=ctx.expedition_run_record,
        )

    @operation_node(name='返回主界面', is_start_node=True)
    def back_to_main(self) -> OperationRoundResult:
        return self.round_success(wait=1)

    @node_from(from_name='返回主界面')
    @operation_node(name='打开远征界面')
    def open_expedition(self) -> OperationRoundResult:
        return self.round_success(wait=1)

    @node_from(from_name='打开远征界面')
    @operation_node(name='收取远征奖励')
    def collect_rewards(self) -> OperationRoundResult:
        return self.round_success(wait=1)

    @node_from(from_name='收取远征奖励')
    @operation_node(name='派遣远征')
    def dispatch(self) -> OperationRoundResult:
        return self.round_success(wait=1)
