from __future__ import annotations

from typing import TYPE_CHECKING

from one_dragon.base.operation.operation_edge import node_from
from one_dragon.base.operation.operation_node import operation_node
from one_dragon.base.operation.operation_round_result import OperationRoundResult
from one_dragon.utils.i18_utils import gt
from hi3_od.application.reward_collect import reward_collect_const
from hi3_od.application.hi3_application import Hi3Application

if TYPE_CHECKING:
    from hi3_od.context.hi3_context import Hi3Context


class RewardCollectApp(Hi3Application):
    """奖励领取"""

    def __init__(self, ctx: Hi3Context):
        Hi3Application.__init__(
            self, ctx, reward_collect_const.APP_ID,
            op_name=gt('奖励领取'),
            run_record=ctx.reward_collect_run_record,
        )

    @operation_node(name='返回主界面', is_start_node=True)
    def back_to_main(self) -> OperationRoundResult:
        return self.round_success(wait=1)

    @node_from(from_name='返回主界面')
    @operation_node(name='领取邮件奖励')
    def collect_mail(self) -> OperationRoundResult:
        return self.round_success(wait=1)

    @node_from(from_name='领取邮件奖励')
    @operation_node(name='领取活动奖励')
    def collect_activity(self) -> OperationRoundResult:
        return self.round_success(wait=1)
