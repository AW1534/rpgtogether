import random
from src.helper import rng
from src.objects import items
from src.helper.rendering import Page
from src.helper.hlist import sort_to_string

name = "mine"
aliases = ["m", "mi", "min", "mine"]
description = "A trip down the mine.. I wonder if there's anything valuable"
cooldown = 10 * 60
cooldown_warning = f"Too tired to mine right now... wait {cooldown} seconds"

minerals = [
    items.rock,
    items.gemstone,
    items.iron
]

loot = rng.Roulette(
    choices=minerals,
    nothing_chance=80
)


def run(player, args, r):
    res = []
    for i in range(random.randint(2, 5)):
        res.append(loot.gen())

    l_string = sort_to_string(res)
    Page(title="Mine", text=["You found..."] + [i for i in l_string])
    player.trade(gains=[i for i in res])

