from src.objects import items
from src.helper import rng
from src.objects import entities
from src import helper

name = "statue"
aliases = ["offer", "offering"]
description = "Toss some stones into the water to restore the statue's magic, and you will receive a reward"
cooldown = 10 * 60
cooldown_warning = "The statue lost all it's power for now, wait {cooldown} seconds"

offerable_items = []
offered_items = []

for i in items.all_items_withcombat:
    if i.magic_power > 0:
        offerable_items.append(i)


def run(p, args):
    offerable_item_names = []
    offerable_obj = []
    for i in p.inventory:
        if i in offerable_items:
            offerable_item_names.append(i.name)
            offerable_obj.append(i)

    print("Items available to offer:\n")

    iteration = 0
    l_string = helper.list.sort_to_string(offerable_item_names)
    for sel in l_string:
        iteration += 1
        print(f"{iteration}: {sel}")

    offering = int(input(f"\nchoose an item (1-{len(l_string)}) >> "))

    item = offerable_obj[offering - 1]

    trade = p.trade(
        loses=[item],
    )

    if trade:
        input("Offered!")
        offered_items.append(item)
    else:
        print("oof, looks like you don't have this item")


# region weak raiders
list_weak_raiders = [
    entities.beast,
    entities.hound,
    entities.goblin
]
number_weak_raiders = [1, 2, 3, 4]
select_weak_raiders = rng.Roulette(
    choices=list_weak_raiders,
    nothing_chance=0
)
amount_weak_raiders = rng.Roulette(
    choices=number_weak_raiders,
    nothing_chance=0
)
# endregion
# region strong raiders
list_strong_raiders = [
    entities.bull,
    entities.boa,
    entities.mutant_bee
]
number_strong_raiders = [3, 4, 5, 6]
select_strong_raiders = rng.Roulette(
    choices=list_strong_raiders,
    nothing_chance=0
)
amount_strong_raiders = rng.Roulette(
    choices=number_strong_raiders,
    nothing_chance=0
)
# endregion
# region invasion
list_invasion_raiders = [
    entities.raider
]
number_invasion_raiders = [15, 17, 19, 23]
select_invasion_raiders = rng.Roulette(
    choices=list_invasion_raiders,
    nothing_chance=0
)
amount_invasion_raiders = rng.Roulette(
    choices=number_invasion_raiders,
    nothing_chance=0
)

# endregion

total_mp = 0
for i in offered_items:
    total_mp += i.magic_power

def battle():
    # weak raid
    if total_mp <= 100:
        present_weak_raider = select_weak_raiders.gen()
        present_amount_weak_raider = amount_weak_raiders.gen()
        print(f"SUDDENLY,  you see {present_amount_weak_raider} {present_weak_raider}s charging towards you")

    # strong raid
    if 100 < total_mp < 200:
        present_strong_raider = select_strong_raiders.gen()
        present_amount_strong_raider = amount_strong_raiders.gen()
        print(f"SUDDENLY, you see {present_amount_strong_raider} {present_strong_raider}s charging towards you")

    # invasion
    if total_mp >= 200:
        present_invasion = select_invasion_raiders.gen()
        present_amount_invasion = amount_invasion_raiders.gen()
        print(f"SUDDENLY, you see {present_invasion} {present_amount_invasion}s rushing towards you")
