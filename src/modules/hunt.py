import math

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
    print(hunted)
    if len(hunted) <= 0:
        formatting.add_border(func=name, strings="Nothing found... better luck next time")
    else:
        lose = rng.Fight(
            teams=[hunted]
        )

        txt = [f"You found a {x.name.lower()}: {x.description.lower():>15}" for x in hunted].append(
            f"You lost {abs(lose.gen(player=player))} hp, your current hp is {player.health}"
        )

        formatting.add_border(func=name, strings=txt)

        drop = rng.Roulette(
            choices=hunted[0].inventory,
            nothing_chance=500,
        ).gen()

        if len(drop) > 0:
            formatting.add_bot_border("Rewards", [f"You took a {drop}"])
            player.trade(gains=drop)
        else:
            formatting.add_bot_border("Rewards",
                formatting.delta_time(
                    seconds=cooldown,
                    m_format_string="You didn't find anything. Try again in {m} minutes and {s} seconds",
                    s_format_string="You didn't find anything. Try again in {m} minutes"
                )
            )
