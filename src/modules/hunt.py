from src.helper import rng
from src.objects import entities

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
        print("Nothing found... better luck next time")
    else:
        print(f"You found {hunted.description.lower()}")
        drop = rng.Roulette(
            choices=hunted.inventory,
            nothing_chance=500
        )
        if drop is None:
            print(f"You didn't find anything valuable that the {hunted.name} had. Better luck next time")
        else:
            print(f"You took a {drop}")
