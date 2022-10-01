from src.helper import rng
from src.objects import entities
from src.helper import formatting
from src.classes.player import Player

name = "hunt"
aliases = ["h", "hu", "hun"]
description = "Wandering in the wilderness... I wonder what's there."
cooldown = 5 * 60
cooldown_warning = f"Too tired to hunt... try again in {cooldown} seconds"

spawnable_entities = [
    entities.pig,
    entities.sheep,
    entities.deer,
    entities.sus,
    entities.zombie,
    entities.ogre,
    entities.fire_dragon
]

entity = rng.Roulette(
    choices=spawnable_entities,
    nothing_chance=10
)


def run(player, args):
    hunted = entity.gen()
    if hunted is None:
        formatting.add_border(func=name, string="Nothing found... better luck next time")
    else:
        lose = rng.Fight(
            teams=hunted
        )
        formatting.add_border(func=name, string=f"You found {hunted.description.lower()}!\n"
                                                f"You lost {lose} hp, your current hp is {Player.health}")
        drop = rng.Roulette(
            choices=hunted.inventory,
            nothing_chance=500
        )
        if drop is not None:
            print(f"You took a {drop}")
