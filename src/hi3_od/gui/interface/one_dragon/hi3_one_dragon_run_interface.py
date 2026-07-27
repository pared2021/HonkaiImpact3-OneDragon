from one_dragon.base.operation.one_dragon_app import OneDragonApp
from one_dragon_qt.view.one_dragon.one_dragon_run_interface import OneDragonRunInterface
from hi3_od.application.one_dragon_app.hi3_one_dragon_app import Hi3OneDragonApp
from hi3_od.context.hi3_context import Hi3Context


class Hi3OneDragonRunInterface(OneDragonRunInterface):

    def __init__(self, ctx: Hi3Context, parent=None):
        self.ctx: Hi3Context = ctx
        OneDragonRunInterface.__init__(
            self,
            ctx=ctx,
            parent=parent,
            help_url='',
        )

    def get_one_dragon_app(self) -> OneDragonApp:
        return Hi3OneDragonApp(self.ctx)
