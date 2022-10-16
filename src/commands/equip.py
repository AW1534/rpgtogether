from src import helper
from src.classes.item import Armor
from src.objects import items
from src.helper.rendering import Page


name = "equip"
aliases = ["eq"]


def run(p, *args, r):
    if args[0].lower() in ["equip", "e"]:
        if args[1].lower() in ["weapon", "w"]:
            weapon(p)
        if args[1].lower() in ["armor", "armour", "a"]:
            armor(p)
        else:
            print("Invalid Argument")
    if args[0].lower() in ["unequip", "u"]:
        unequip(p, args)
    else:
        print("Invalid Argument")


def weapon(p):
    s_i = []
    for i in p.inventory:
        if i in items.all_weapons:
            s_i.append(i.name)
        else:
            continue

    print("Equippable items:\n")

    i = 0
    l_string = helper.hlist.sort_to_string(s_i)
    for item in l_string:
        i += 1
        print(f"{i}: {item}")

    selling = int(input(f"\nchoose an item (1-{len(l_string)}) >> "))

    item = p.inventory[selling - 1]

    trade = p.trade(
        loses=[item]
    )
    p.weapon = item


def armor(p):
    obj_s_i = []
    s_i = []
    for i in p.inventory:
        if type(i) is Armor:
            s_i.append(i.name)
            obj_s_i.append(i)

    print("Equippable items:\n")

    i = 0
    l_string = helper.hlist.sort_to_string(s_i)
    for item in l_string:
        i += 1
        print(f"{i}: {item}")

    selling = int(input(f"\nchoose an item (1-{len(l_string)}) >> "))

    item = obj_s_i[selling - 1]

    trade = p.trade(
        loses=[item]
    )
    p.armour = item


def unequip(player, *args):
    if args[1] in ["armour", "armor", "a"]:
        out = Page(title="Equip - Unequip", text=f"Unequipped {player.armour}")
        player.trade(gains=player.armour)
        player.armour = None

    if args[1] in ["weapon", "sword", "w"]:
        out = Page(title="Equip - Unequip", text=f"Unequipped {player.weapon}")
        player.trade(gains=player.weapon)
        player.weapon = None

    if args[1] in [" ", None]:
        select = input(Page(title="Equip - Unequip", text="What are you unequipping?", center_title=False))

        if select.lower() in ["armour", "armor", "a"]:
            out = Page(title="Equip - Unequip", text=f"Unequipped {player.armour}")
            player.trade(gains=player.armour)
            player.armour = None

        if select.lower() in ["weapon", "sword", "w"]:
            out = Page(title="Equip - Unequip", text=f"Unequipped {player.weapon}")
            player.trade(gains=player.weapon)
            player.weapon = None

        else:
            out = Page(title="Equip - Unequip", text="Please enter a valid response next time....", center_title=False)

    else:
        out = Page(title="Equip - Unequip", text="Please enter a valid response next time....", center_title=False)



