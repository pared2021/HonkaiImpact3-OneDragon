from __future__ import annotations

from typing import TYPE_CHECKING

from one_dragon.base.operation.operation_edge import node_from
from one_dragon.base.operation.operation_node import operation_node
from one_dragon.base.operation.operation_round_result import OperationRoundResult
from one_dragon.utils.i18_utils import gt
from hi3_od.application.battle_assistant import battle_assistant_const
from hi3_od.application.hi3_application import Hi3Application

if TYPE_CHECKING:
    from hi3_od.context.hi3_context import Hi3Context


class BattleAssistantApp(Hi3Application):
    """战斗辅助 - 深渊/记忆战场"""

    def __init__(self, ctx: Hi3Context):
        Hi3Application.__init__(
            self, ctx, battle_assistant_const.APP_ID,
            op_name=gt('战斗辅助'),
            run_record=ctx.battle_assistant_run_record,
        )

    @operation_node(name='返回主界面', is_start_node=True)
    def back_to_main(self) -> OperationRoundResult:
        return self.round_success(wait=1)

    @node_from(from_name='返回主界面')
    @operation_node(name='进入战斗')
    def enter_battle(self) -> OperationRoundResult:
        return self.round_success(wait=1)

    @node_from(from_name='进入战斗')
    @operation_node(name='战斗循环')
    def battle_loop(self) -> OperationRoundResult:
        return self.round_success(wait=1)

    @node_from(from_name='战斗循环')
    @operation_node(name='检查战斗结果')
    def check_result(self) -> OperationRoundResult:
        return self.round_success(wait=1)
