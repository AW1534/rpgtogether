from src.objects import items
from src.rng import rng
from src.objects import entities

name = "statue"
aliases = ["offer", "offering"]
description = "Toss some stones into the water to restore the statue's magic, and you will receive a reward"
cooldown = 10 * 60
cooldown_warning = "The statue lost all it's power for now, wait {cooldown} seconds"

offerable_items = []

for item in items.all_items:
    if item.magic_power > 0:
        offerable_items.append(item)


def run(p, args):
    obj_s_i = []
    s_i = []
    for i in p.inventory:
        if i in offerable_items:
            s_i.append(i.name)
            obj_s_i.append(i)

    print("Items available to offer:\n")

    i = 0
    l_string = src.helper.list.sort_to_string(s_i)
    for item in l_string:
        i += 1
        print(f"{i}: {item}")

    offering = int(input(f"\nchoose an item (1-{len(l_string)}) >> "))

    item = obj_s_i[offering - 1]

    trade = p.trade(
        loses=[item],
    )

    if trade:
        input("Offered!")
    else:
        print("oof, looks like you don't have this item")


list_weak_raiders = [
    entities.beast,
    entities.hound,
    entities.goblin
]
select_weak_raiders = rng.Roulette(
    choices=list_weak_raiders,
    nothing_chance=0
)
list_strong_raiders = [
    entities.bull,
    entities.boa,
    entities.mutant_bee
]
select_strong_raiders = rng.Roulette(
    choices=list_strong_raiders,
    nothing_chance=0
)
list_invasion_raiders = [
    entities.raider
]
select_invasion_raiders = rng.Roulette(
    choices=list_invasion_raiders,
    nothing_chance=0
)


def battle():
    def weak_raid():
        for i in obj_s_i[i - 1]:
            if item.magic_power >= 1:
                print("SUDDENLY,  you see {} charging towards you")

    def strong_raid():
        for i in obj_s_i[i - 1]:
            if item.magic_power > 100:
                print("SUDDENLY, you see {} charging towards you")

    def invasion():
        for i in obj_s_i[i - 1]:
            if item.magic_power > 200:
                print("SUDDENLY, you see {} rushing towards you")
