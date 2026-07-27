from __future__ import annotations

from typing import Optional

from one_dragon.base.config.game_account_config import GameAccountConfig
from one_dragon.base.operation.one_dragon_context import OneDragonContext
from one_dragon.utils import i18_utils
from hi3_od.context.hi3_pc_controller import Hi3PcController


class Hi3Context(OneDragonContext):
    """崩坏三全局上下文"""

    def __init__(self):
        OneDragonContext.__init__(self)

        self.controller: Optional[Hi3PcController] = None

        # 共用配置
        from hi3_od.config.model_config import ModelConfig
        self.model_config: ModelConfig = ModelConfig()

        # 实例独有的配置
        self.reload_instance_config()

    def register_application_factory(self) -> None:
        OneDragonContext.register_application_factory(self)
        self.app_group_manager.set_default_apps(self.run_context.default_group_apps)
        self.app_group_manager.clear_config_cache()

        from one_dragon.base.config.notify_config import NotifyConfig
        self.notify_config = NotifyConfig(self.current_instance_idx, self.run_context.notify_app_map)

    def init_by_config(self) -> None:
        """根据配置进行初始化"""
        self.init()

    def init_controller(self) -> None:
        i18_utils.update_default_lang(self.game_config.lang)

        if self.controller is not None:
            self.controller.cleanup_after_app_shutdown()

        self.controller = Hi3PcController(
            game_config=self.game_config,
            screenshot_method=self.env_config.screenshot_method,
            standard_width=self.project_config.screen_standard_width,
            standard_height=self.project_config.screen_standard_height
        )
        self.controller.set_window_title(self._get_win_title())

    def _get_win_title(self) -> str:
        if self.game_account_config.use_custom_win_title:
            return self.game_account_config.custom_win_title
        return self.game_config.win_title

    def load_instance_config(self) -> None:
        self.reload_instance_config()

    def reload_instance_config(self) -> None:
        OneDragonContext.reload_instance_config(self)

        from hi3_od.config.game_config import GameConfig
        self.game_config: GameConfig = GameConfig(self.current_instance_idx)

        from one_dragon.base.config.game_account_config import GameAccountConfig
        self.game_account_config: GameAccountConfig = GameAccountConfig(self.current_instance_idx)

        from one_dragon.base.config.notify_config import NotifyConfig
        self.notify_config: NotifyConfig = NotifyConfig(self.current_instance_idx, self.run_context.notify_app_map)

        game_refresh_hour_offset = self.game_account_config.game_refresh_hour_offset

        from hi3_od.application.daily_signin.daily_signin_run_record import DailySigninRunRecord
        self.daily_signin_run_record: DailySigninRunRecord = DailySigninRunRecord(
            self.current_instance_idx, game_refresh_hour_offset)

        from hi3_od.application.daily_tasks.daily_tasks_run_record import DailyTasksRunRecord
        self.daily_tasks_run_record: DailyTasksRunRecord = DailyTasksRunRecord(
            self.current_instance_idx, game_refresh_hour_offset)

        from hi3_od.application.expedition.expedition_run_record import ExpeditionRunRecord
        self.expedition_run_record: ExpeditionRunRecord = ExpeditionRunRecord(
            self.current_instance_idx, game_refresh_hour_offset)

        from hi3_od.application.reward_collect.reward_collect_run_record import RewardCollectRunRecord
        self.reward_collect_run_record: RewardCollectRunRecord = RewardCollectRunRecord(
            self.current_instance_idx, game_refresh_hour_offset)

        from hi3_od.application.battle_assistant.battle_assistant_run_record import BattleAssistantRunRecord
        self.battle_assistant_run_record: BattleAssistantRunRecord = BattleAssistantRunRecord(
            self.current_instance_idx, game_refresh_hour_offset)

    def on_switch_instance(self) -> None:
        self.init_controller()
