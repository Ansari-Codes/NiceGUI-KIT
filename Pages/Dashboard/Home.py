from Elements.ui import Label

async def create_home(area, user_id, user_name):
    area.clear()
    with area:
        Label(f"Hi! {user_name.title()}").classes("w-full font-bold text-9xl text-primary")

