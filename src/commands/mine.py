from src.helper import rng
from src.objects import items

name = "mine"
aliases = ["m","mi","min","mine"]
description = "A trip down the mine.. I wonder if there's anything valuable"
cooldown = 10 * 60
cooldown_warning = f"Too tired to mine right now... wait {cooldown} seconds"

minerals = [
    items.rock,
    items.gemstone,
    items.iron
]

r = rng.Roulette(
    choices = minerals,
    nothing_chance = 80
)


def run(player, args, r):
    res = []
    for i in range(200):
        res = r.gen()

    print(f"you found {', '.join(res)}.")


