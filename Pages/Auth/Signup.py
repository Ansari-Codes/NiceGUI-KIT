from ui import Card, Row, Col, Input, Button, Label, CardAct, CardSec, navigate, RawCol, RawRow, Div, Password
from Core.pages import per_page, Request
from Classes.Auth import SignupData

async def lblinp(label, model, password=False):
    with RawCol().classes("w-full h-fit p-0.5"):
        with Div().classes("grid grid-cols-2 gap-1 h-fit w-full"):
            label_wdiget = Label(label).classes("capitalize")
            error_wdiget = Label().classes("text-sm items-center text-red-500")
        if password: Password(model=model)
        else: Input(model)
        
async def signup(redirect_to='/'):
    per_page().classes("flex justify-center items-center")
    sdata = SignupData()
    with Card().classes("w-fit h-fit"):
        with CardSec().classes("flex w-full h-fit items-center justify-center"):
            Label("Create Account")
        with CardSec().classes("flex w-full h-fit items-center justify-center"):
            Label("Credentials")
        with CardAct().classes("flex w-full h-fit items-center justify-center"):
            pass

async def create_signup(redirect_to='/'):
    token = None
    if not token: await signup(redirect_to)
    else: navigate(redirect_to)
