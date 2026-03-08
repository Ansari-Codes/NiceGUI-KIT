from ui import Card, Row, Col, Input, Button, Label, CardAct, CardSec, navigate
from Core.pages import per_page, Request
from Classes.Auth import SignupData

async def signup(redirect_to='/'):
    per_page().classes("flex justify-center items-center")
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
