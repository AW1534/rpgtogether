from src import helper
from src.classes.item import Armor
from src.objects import items

name = "equip"
aliases = ["eq"]


def run(p, args):
    if args[0].lower() in ["weapon", "w"]:
        weapon(p)
    if args[0].lower() in ["armor", "armour", "a"]:
        armor(p)
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
    l_string = helper.list.sort_to_string(s_i)
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
    l_string = helper.list.sort_to_string(s_i)
    for item in l_string:
        i += 1
        print(f"{i}: {item}")

    selling = int(input(f"\nchoose an item (1-{len(l_string)}) >> "))

    item = obj_s_i[selling - 1]

    trade = p.trade(
        loses=[item]
    )
    p.armour = item
