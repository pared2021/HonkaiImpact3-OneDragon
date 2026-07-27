import sys

from one_dragon.launcher.application_launcher import ApplicationLauncher
from hi3_od.context.hi3_context import Hi3Context


class Hi3ApplicationLauncher(ApplicationLauncher):
    """崩坏三应用启动器"""

    def __init__(self):
        ApplicationLauncher.__init__(self)

    def create_context(self):
        return Hi3Context()


def main(args: list[str] | None = None) -> None:
    if args is not None:
        sys.argv = [sys.argv[0]] + args
    launcher = Hi3ApplicationLauncher()
    launcher.run()


if __name__ == '__main__':
    main()
