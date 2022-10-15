import time
from src.helper import rng
from src.objects import enchantments
from src.classes.player import Player
from src.objects import items
from src.helper.rendering import Page

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


name = "enchant"
aliases = ["ench"]
description = "casts a spell upon your gear"


def enchant_weapon(player, args):
    a = Page(title="Enchanting - Sword", text="Enchanting sword...", center_title=False)

    weapon_enchant = weapon_rng.gen()
    if weapon_enchant is None:
        a = Page(title="Enchanting - Sword", text="YOUR WEAPON HAS BROKEN", center_title=False)
        player.weapon.pop()

    else:
        enchanted = Page(title="Enchanting - Sword", text=f"You sword has been enchanted with.... \n {weapon_enchant}",
                         center_title=False)
        player.weapon.enchantment.append(weapon_enchant)


def enchant_armour(player, args):
    a = Page(title="Enchanting - Armour", text="Enchanting armour...", center_title=False)

    armour_enchant = armour_rng.gen()
    if armour_enchant is None:
        a = Page(title="Enchanting - Armour", text="YOUR ARMOUR HAS BROKEN", center_title=False)
        player.armour.pop()

    else:
        enchanted = Page(title="Enchanting - Armour", text=f"You armour has been enchanted with.... \n {armour_enchant}",
                         center_title=False)
        player.weapon.enchantment.append(armour_enchant)


def run(player, args, renderer):
    intro = Page(title="---> Magical Stone Tablet <---")

    if args[0].lower() in ["sword", "weapon"]:
        enchant_weapon(player, args)

    if args[0].lower() in ["clothes", "armour", "armor"]:
        enchant_armour(player, args)

    if args[0].lower() in [" ", None]:
        ask = Page(title="Enchanting", text="What would you like to enchant? (Weapon/Armour)")
        inp = input()

        if inp.lower() in ["sword", "weapon"]:
            enchant_weapon(player, args)

        if inp.lower() in ["clothes", "armour", "armor"]:
            enchant_armour(player, args)
    else:
        result = Page(title="Enchanting", text="Invalid Arguments, please try again")
