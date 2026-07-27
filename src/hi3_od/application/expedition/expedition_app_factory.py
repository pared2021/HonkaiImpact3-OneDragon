from __future__ import annotations

from typing import TYPE_CHECKING

from one_dragon.base.config.game_account_config import GameAccountConfig
from one_dragon.base.operation.application.application_factory import ApplicationFactory
from one_dragon.base.operation.application_base import Application
from one_dragon.base.operation.application_run_record import AppRunRecord
from hi3_od.application.expedition import expedition_const
from hi3_od.application.expedition.expedition_app import ExpeditionApp
from hi3_od.application.expedition.expedition_run_record import ExpeditionRunRecord

if TYPE_CHECKING:
    from hi3_od.context.hi3_context import Hi3Context


class ExpeditionAppFactory(ApplicationFactory):

    def __init__(self, ctx: Hi3Context):
        ApplicationFactory.__init__(self, expedition_const)
        self.ctx: Hi3Context = ctx

    def create_application(self, instance_idx: int, group_id: str) -> Application:
        return ExpeditionApp(self.ctx)

    def create_run_record(self, instance_idx: int) -> AppRunRecord:
        return ExpeditionRunRecord(
            instance_idx,
            GameAccountConfig(instance_idx).game_refresh_hour_offset,
        )
