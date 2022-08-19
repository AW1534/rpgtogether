from src.rng import rng
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

roulette = rng.Roulette(
    choices=spawnable_entities,
    nothing_chance=10
)

def run(player, args):
    entity = roulette.gen()
    if entity == None:
        print("Nothing found... better luck next time")
    else:
        print(f"You found {entity.description.lower()}")
