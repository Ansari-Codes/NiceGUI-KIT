from Elements.ui import Label

async def create_section(area, user_id, user_name):
    area.clear()
    with area:
        Label(f"this is simple section")

