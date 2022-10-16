import time
from src.helper import rng
from src.objects import enchantments
from src.helper.rendering import Page
from src.helper import option

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


def disenchant(player):
    disenchanting = input(Page(title="Enchanting - Disenchanting", text=f"What would you like to disenchant, {player.name}?\n>> (Armour/Weapon)\t"))

    if disenchanting.lower() in ["sword", "weapon", "w"]:
        confirm = input(
            Page(title="Enchanting - Disenchanting - Weapon", text=f"You are about to disenchant {player.weapon.name}.\n"
                                                                   f"Enchant: {player.weapon.enchantment.name}"
                                                                   "this will cost 1000 nuelis.\n"
                                                                   "Confirm? (Y/N)",
                 center_title=False
                 ))

        if confirm in option.yes:
            res = Page(title="Enchanting - Disenchanting - Weapon", text="Disenchanting your weapon...",
                       center_title=False)
            time.sleep(1)
            player.trade(loses_nuelis=1000)
            player.weapon.enchantment = None
            out = Page(title="Enchanting - Disenchanting - Weapon", text="Your weapon has been disenchanted", center_title=False)

        elif confirm in option.no:
            out = Page(title="Enchanting - Disenchanting - Weapon", text="Cancelled disenchanting", center_title=False)

        else:
            out = Page(title="Enchanting - Disenchanting - Weapon", text="Please enter a valid response next time....",
                       center_title=False)

    if disenchanting.lower() in ["armour", "armor", "a"]:
        confirm = input(
            Page(title="Enchanting - Disenchanting - Armour", text=f"You are about to disenchant {player.armour.name}.\n"
                                                                   f"Enchant: {player.armour.enchantment.name}"
                                                                   "this will cost 1000 nuelis.\n"
                                                                   "Confirm? (Y/N)",
                 center_title=False
                 ))

        if confirm in option.yes:
            res = Page(title="Enchanting - Disenchanting - Armour", text="Disenchanting your armour...",
                       center_title=False)
            time.sleep(1)
            player.trade(loses_nuelis=1000)
            player.armour.enchantment = None
            out = Page(title="Enchanting - Disenchanting - Armour", text="Your armour has been disenchanted",
                       center_title=False)

        elif confirm in option.no:
            out = Page(title="Enchanting - Disenchanting - Armour", text="Cancelled disenchanting", center_title=False)

        else:
            out = Page(title="Enchanting - Disenchanting - Armour", text="Please enter a valid response next time....",
                       center_title=False)
    else:
        Page(title="Enchanting - Disenchanting", text="Please enter a valid item type next time....")


def enchant_weapon(player):
    a = Page(title="Enchanting - Sword", text="Enchanting sword...", center_title=False)

    weapon_enchant = weapon_rng.gen()
    if weapon_enchant is None:
        a = Page(title="Enchanting - Sword", text="YOUR WEAPON HAS BROKEN", center_title=False)
        player.weapon.pop()

    else:
        enchanted = Page(title="Enchanting - Sword", text=f"You sword has been enchanted with.... \n {weapon_enchant}",
                         center_title=False)
        player.weapon.enchantment.append(weapon_enchant)


def enchant_armour(player):
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

    if args[0].lower() in ["disenchant", "unenchant", "grind", "d"]:
        disenchant(player)

    if args[0].lower() in ["enchant", "cast", "e", "spell"]:

        if args[1].lower() in ["sword", "weapon"]:
            enchant_weapon(player)

        if args[1].lower() in ["clothes", "armour", "armor"]:
            enchant_armour(player)

        if args[1].lower() in [" ", None]:
            ask = Page(title="Enchanting", text="What would you like to enchant? (Weapon/Armour)")
            inp = input()

            if inp.lower() in ["sword", "weapon"]:
                enchant_weapon(player)

            if inp.lower() in ["clothes", "armour", "armor"]:
                enchant_armour(player)

            else:
                result = Page(title="Enchanting", text="Invalid Arguments, please try again")

        else:
            result = Page(title="Enchanting", text="Invalid Arguments, please try again")

    if args[0] in [" ", None]:
        ask = Page(title="Enchanting", text="What would you like to do? (Enchant/Disenchant)")
        inp = input()

        if inp.lower() in ["disenchant", "unenchant", "grind", "d"]:
            disenchant(player)

        if inp.lower() in ["enchant", "cast", "e", "spell"]:
            ask = Page(title="Enchanting", text="What would you like to enchant? (Weapon/Armour)")
            inp = input()

            if inp.lower() in ["sword", "weapon"]:
                enchant_weapon(player)

            if inp.lower() in ["clothes", "armour", "armor"]:
                enchant_armour(player)

            else:
                result = Page(title="Enchanting", text="Invalid Arguments, please try again")

        else:
            result = Page(title="Enchanting", text="Invalid Arguments, please try again")

    else:
        result = Page(title="Enchanting", text="Invalid Arguments, please try again")

