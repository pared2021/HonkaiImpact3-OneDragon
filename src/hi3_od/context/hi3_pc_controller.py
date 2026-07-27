from __future__ import annotations

from one_dragon.base.controller.pc_controller_base import PcControllerBase
from hi3_od.config.game_config import GameConfig


class Hi3PcController(PcControllerBase):
    """崩坏三 PC 端控制器"""

    def __init__(self, game_config: GameConfig,
                 screenshot_method: str,
                 standard_width: int = 1920,
                 standard_height: int = 1080):
        PcControllerBase.__init__(self,
                                  screenshot_method=screenshot_method,
                                  standard_width=standard_width,
                                  standard_height=standard_height)
        self.game_config: GameConfig = game_config

    def esc(self) -> bool:
        """按下ESC键"""
        self.btn_tap(self.game_config.key_esc)
        return True
