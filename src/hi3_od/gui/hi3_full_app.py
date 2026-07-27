try:
    import sys
    from typing import Tuple
    from PySide6.QtCore import Qt, QThread, Signal
    from PySide6.QtWidgets import QApplication
    from qfluentwidgets import NavigationItemPosition, setTheme, Theme

    from one_dragon.base.operation.one_dragon_context import ContextInstanceEventEnum
    from one_dragon.utils import app_utils
    from one_dragon.utils.i18_utils import gt
    from one_dragon_qt.services.styles_manager import OdQtStyleSheet
    from one_dragon_qt.view.context_event_signal import ContextEventSignal
    from one_dragon_qt.windows.main_app_window_base import MainAppWindowBase
    from one_dragon_qt.windows.window import PhosTitleBar
    from hi3_od.context.hi3_context import Hi3Context

    _init_error = None


    class CtxInitRunner(QThread):

        def __init__(self, ctx: Hi3Context, parent=None):
            super().__init__(parent)
            self.ctx = ctx

        def run(self):
            self.ctx.init()


    class CheckVersionRunner(QThread):

        get = Signal(tuple)

        def __init__(self, ctx: Hi3Context, parent=None):
            super().__init__(parent)
            self.ctx = ctx

        def run(self):
            launcher_version = app_utils.get_launcher_version()
            code_version = self.ctx.git_service.get_current_version()
            versions = (launcher_version, code_version)
            self.get.emit(versions)


    class AppWindow(MainAppWindowBase):
        titleBar: PhosTitleBar

        def __init__(self, ctx: Hi3Context, parent=None):
            self.ctx: Hi3Context = ctx
            MainAppWindowBase.__init__(
                self,
                ctx=ctx,
                win_title='%s %s' % (
                    gt(ctx.project_config.project_name),
                    ctx.one_dragon_config.current_active_instance.name,
                ),
                project_config=ctx.project_config,
                app_icon='logo.ico',
                parent=parent,
            )

            self.ctx.listen_event(ContextInstanceEventEnum.instance_active.value, self._on_instance_active_event)
            self._context_event_signal: ContextEventSignal = ContextEventSignal()
            self._context_event_signal.instance_changed.connect(self._on_instance_active_signal)

            self._check_version_runner = CheckVersionRunner(self.ctx)
            self._check_version_runner.get.connect(self._update_version)

        def init_window(self):
            self.resize(1140, 760)

            screen = QApplication.primaryScreen()
            geometry = screen.availableGeometry()
            w, h = geometry.width(), geometry.height()
            self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

            self.setObjectName('PhosWindow')
            self.navigationInterface.setObjectName('NavigationInterface')
            self.stackedWidget.setObjectName('StackedWidget')
            self.titleBar.setObjectName('TitleBar')

            self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
            self.areaLayout.setContentsMargins(0, 32, 0, 0)
            self.navigationInterface.setContentsMargins(0, 0, 0, 0)

            OdQtStyleSheet.NAVIGATION_INTERFACE.apply(self.navigationInterface)
            OdQtStyleSheet.STACKED_WIDGET.apply(self.stackedWidget)
            OdQtStyleSheet.AREA_WIDGET.apply(self.areaWidget)
            OdQtStyleSheet.TITLE_BAR.apply(self.titleBar)

        def create_sub_interface(self):
            super().create_sub_interface()

            # 主页
            from hi3_od.gui.interface.home.home_interface import HomeInterface
            self.add_sub_interface(HomeInterface(self.ctx, parent=self))

            # 一条龙
            from hi3_od.gui.interface.one_dragon.hi3_one_dragon_interface import Hi3OneDragonInterface
            self.add_sub_interface(Hi3OneDragonInterface(self.ctx, parent=self))

            # 代码同步
            from one_dragon_qt.view.code_interface import CodeInterface
            self.add_sub_interface(
                CodeInterface(self.ctx, parent=self),
                position=NavigationItemPosition.BOTTOM,
            )

            # 设置
            from hi3_od.gui.interface.setting.hi3_setting_interface import Hi3SettingInterface
            self.add_sub_interface(
                Hi3SettingInterface(self.ctx, parent=self),
                position=NavigationItemPosition.BOTTOM,
            )

        def on_ctx_ready(self) -> None:
            if not self.ctx.ready_for_application:
                return
            MainAppWindowBase.on_ctx_ready(self)
            self._check_version_runner.start()

        def _on_instance_active_event(self, event) -> None:
            self._context_event_signal.instance_changed.emit()

        def _on_instance_active_signal(self) -> None:
            self.setWindowTitle('%s %s' % (
                gt(self.ctx.project_config.project_name),
                self.ctx.one_dragon_config.current_active_instance.name,
            ))

        def _update_version(self, versions: Tuple[str, str]) -> None:
            self.titleBar.setLauncherVersion(versions[0])
            self.titleBar.setCodeVersion(versions[1])


except Exception as e:
    import ctypes
    import traceback
    stack_trace = traceback.format_exc()
    _init_error = f'启动一条龙失败，报错信息如下:\n{stack_trace}'


def main() -> None:
    if _init_error is not None:
        ctypes.windll.user32.MessageBoxW(0, _init_error, '错误', 0x10)
        sys.exit(1)

    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    app = QApplication(sys.argv)
    app.setAttribute(Qt.ApplicationAttribute.AA_DontCreateNativeWidgetSiblings)

    _ctx = Hi3Context()

    setTheme(Theme[_ctx.custom_config.theme.upper()])

    w = AppWindow(_ctx)
    w.show()
    w.activateWindow()

    init_runner = CtxInitRunner(_ctx)
    init_runner.finished.connect(w.on_ctx_ready)
    init_runner.start()

    quit_code = app.exec()

    _ctx.after_app_shutdown()
    sys.exit(quit_code)


if __name__ == '__main__':
    main()
