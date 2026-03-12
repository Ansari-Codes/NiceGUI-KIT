from Core.pages import Request
from Elements.ui import Drawer, Div, Button, Label, RawCol, AddSpace, navigate
from Pages import SESSION_DEL
from Pages.Dashboard.Home import create_home
from Pages.Dashboard.Section import create_section
import app

upper_side_buttons = {
    "Dashboard": {
        "icon": "dashboard",
        "function": create_home
    },
    "A Section": {
        "icon": "image",
        "function": create_section
    },
}
lower_side_buttons = {
    "Settings": {
        "icon": "settings",
        "function": lambda **kwargs: kwargs
    },
    "LogOut": {
        "icon": "exit",
        "function": lambda **kwargs: navigate(SESSION_DEL)
    },
}

async def SideDrawer(**kwargs):
    d = Drawer().classes("bg-primary")
    with d:
        Label("Dashboard").classes("w-full border-b-2 text-4xl text-center")
        with RawCol().classes("w-full h-full gap-1"):
            for btn, kw in upper_side_buttons.items():
                Button(
                    btn,
                    on_click=lambda kw=kw: kw.get("function", lambda **kwargs:())(**kwargs), 
                    config={"icon":kw.get("icon")}
                ).classes("w-full")
            AddSpace()
            for btn, kw in lower_side_buttons.items():
                Button(
                    btn,
                    on_click=lambda kw=kw: kw.get("function", lambda **kwargs:())(**kwargs), 
                    config={"icon":kw.get("icon"), "color": "secondary"}
                ).classes("w-full")
    return d

async def create_dashboard(request: Request):
    await app.context.client.connected()
    token = request.cookies.get("auth_token")
    user_id = request.cookies.get("user_id")
    user_name = request.cookies.get("user_name")
    area = Div()
    drawer = await SideDrawer(area=area, user_id=user_id, user_name=user_name)
    await create_home(area, user_id, user_name)
