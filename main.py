"""崩坏三一条龙 - 主入口"""

import sys
from pathlib import Path

# 将 src 目录加入 Python 路径
src_path = Path(__file__).parent / 'src'
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))


def main():
    """主入口"""
    from hi3_od.gui.hi3_full_app import main as gui_main
    gui_main()


if __name__ == '__main__':
    main()
