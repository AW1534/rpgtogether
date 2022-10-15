from src.classes import player
from src.objects import items

from src.helper import rng

name = "scavenge"
aliases = ["s", "sc", "scv"]
description = "Scavenges for items. Will you strike gold? one way to find out"
cooldown = 1 * 60
cooldown_warning = f"Didn't find anything... try again in {cooldown} seconds"

findable_items = [
    items.stone,
    items.book,
    items.page,
    items.rock,
    items.rope,
    items.fabric
]

roulette = rng.Roulette(
    choices=findable_items,
    nothing_chance=25
)


def run(p: player.Player, arg, r):
    item, = roulette.gen()

    if item is None:
        print("You found nothing")
    else:
        p.trade(
            gains=[item]
        )
        print(f"You found a {item.name.lower()}")
