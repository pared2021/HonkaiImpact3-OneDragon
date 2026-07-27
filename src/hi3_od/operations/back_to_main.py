from __future__ import annotations

from one_dragon.base.operation.operation import Operation
from one_dragon.base.operation.operation_round_result import OperationRoundResult


class BackToMain(Operation):
    """返回主界面操作"""

    def __init__(self, ctx):
        Operation.__init__(self, ctx, op_name='返回主界面')

    def handle_init(self) -> None:
        Operation.handle_init(self)

    def execute(self):
        # TODO: 实现返回主界面逻辑
        return self.round_success()
