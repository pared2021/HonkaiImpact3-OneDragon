from __future__ import annotations

from one_dragon.base.config.yaml_config import YamlConfig


class GameConfig(YamlConfig):
    """崩坏三游戏配置"""

    def __init__(self, instance_idx: int):
        YamlConfig.__init__(self, module_name='game', instance_idx=instance_idx)

    @property
    def win_title(self) -> str:
        return self.get('win_title', '崩坏3')

    @property
    def key_esc(self) -> str:
        return self.get('key_esc', 'esc')

    @property
    def lang(self) -> str:
        return self.get('lang', 'cn')
