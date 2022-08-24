from src.helper import rng
from src.objects import enchantments
from src.classes.player import Player
from src.objects import items


weapon_enchantments = [
    enchantments.sharp,
    enchantments.reforged,
    enchantments.burning,
    enchantments.lethal,
    enchantments.mythical,
    enchantments.clover
]

weapon_rng = rng.Roulette(
    choices=weapon_enchantments,
    nothing_chance=5
)

armour_enchantments = {
    enchantments.durable,
    enchantments.hardened,
    enchantments.sturdy,
    enchantments.crystalized,
    enchantments.nokia,
    enchantments.synergy,
    enchantments.one_for_all
}

armour_rng = rng.Roulette(
    choices=armour_enchantments,
    nothing_chance=5
)


def broken_w():
    print("YOUR WEAPON HAS BROKEN")
    Player.weapon.pop()


def broken_a():
    print("YOUR ARMOUR HAS BROKEN")
    Player.armor.pop()


name = "enchant"
aliases = ["ench"]
description = "casts a spell upon your gear"


def run(player, args):
    print("---> Magical Stone Tablet <---")

    if args[0] == "sword":
        print("You have *enchanted* your sword:")

        def run(p: player.Player, arg):
            weapon_enchant = weapon_rng.gen()
            print(weapon_enchant)
            Player.weapon.enchantment.append(weapon_enchant)

            if weapon_enchant is None:
                broken_w()

    if args[0] == "armour":
        print("You have *enchanted* your sword:")

        def run(p: player.Player, arg):
            armour_enchant = armour_rng.gen()
            print(armour_enchant)

            if armour_enchant is None:
                broken_a()
