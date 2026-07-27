from __future__ import annotations

from typing import TYPE_CHECKING

from one_dragon.base.operation.operation_edge import node_from
from one_dragon.base.operation.operation_node import operation_node
from one_dragon.base.operation.operation_round_result import OperationRoundResult
from one_dragon.utils.i18_utils import gt
from hi3_od.application.daily_tasks import daily_tasks_const
from hi3_od.application.hi3_application import Hi3Application

if TYPE_CHECKING:
    from hi3_od.context.hi3_context import Hi3Context


class DailyTasksApp(Hi3Application):
    """每日任务"""

    def __init__(self, ctx: Hi3Context):
        Hi3Application.__init__(
            self, ctx, daily_tasks_const.APP_ID,
            op_name=gt('每日任务'),
            run_record=ctx.daily_tasks_run_record,
        )

    @operation_node(name='返回主界面', is_start_node=True)
    def back_to_main(self) -> OperationRoundResult:
        return self.round_success(wait=1)

    @node_from(from_name='返回主界面')
    @operation_node(name='打开任务界面')
    def open_tasks(self) -> OperationRoundResult:
        return self.round_success(wait=1)

    @node_from(from_name='打开任务界面')
    @operation_node(name='领取活跃度奖励')
    def collect_rewards(self) -> OperationRoundResult:
        return self.round_success(wait=1)
