import time

from src.objects import items
from src.helper import rendering
from src.helper import list


name = "craft"
aliases = ["cft", "make"]
description = "craft an item bruh"

craftables = [x for x in items.all_items if x.recipe is not None or x.recipe is not []]


def run(p, args, renderer: rendering.__Renderer):


    desired = str(args[0]).replace('"', "").replace("'", "").upper()
    amt = 1
    if args[1] is not None and args[1] >= 1:
        amt = args[1]



    item = [x for x in craftables if x.name.upper() == desired][0]



    if item == None:
        return

    page = rendering.Page(title="Crafting", text=[f"Crafting {list.sort_to_string([item.name], False)[0]}"])
    renderer.set_page(page)
    time.sleep(15)
    p.trade(
        loses=item.recipe,
        gains=item
    )
    page.buffer = [
        f"crafted {item.name}",
        f"{item.description}"
    ]

    renderer.set_page(page)