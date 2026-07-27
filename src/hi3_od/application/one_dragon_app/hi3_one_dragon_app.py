from one_dragon.base.operation.application import application_const
from one_dragon.base.operation.one_dragon_app import OneDragonApp
from hi3_od.application.hi3_application import Hi3Application
from hi3_od.context.hi3_context import Hi3Context


class Hi3OneDragonApp(OneDragonApp, Hi3Application):
    """崩坏三一键一条龙"""

    def __init__(self, ctx: Hi3Context):
        Hi3Application.__init__(
            self,
            ctx=ctx,
            app_id=application_const.ONE_DRAGON_APP_ID,
        )
        OneDragonApp.__init__(
            self,
            ctx=ctx,
            op_to_enter_game=None,
            op_to_switch_account=None,
        )
