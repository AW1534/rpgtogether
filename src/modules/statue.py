from src.objects import items
from src.rng import rng
from src.objects import entities
from src import helper

name = "statue"
aliases = ["offer", "offering"]
description = "Toss some stones into the water to restore the statue's magic, and you will receive a reward"
cooldown = 10 * 60
cooldown_warning = "The statue lost all it's power for now, wait {cooldown} seconds"

offerable_items = []
offered_items = []

for item in items.all_items:
    if item.magic_power > 0:
        offerable_items.append(item)


def run(p, args):
    n_players_offerable_items = []
    obj_players_offerable_items = []
    for i in p.inventory:
        if i in offerable_items:
            n_players_offerable_items.append(i.name)
            obj_players_offerable_items.append(i)

    print("Items available to offer:\n")

    i = 0
    l_string = helper.list.sort_to_string(n_players_offerable_items)
    for str_item in l_string:
        i += 1
        print(f"{i}: {str_item}")

    offering = int(input(f"\nchoose an item (1-{len(l_string)}) >> "))

    item = obj_players_offerable_items[offering - 1]

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

list_total_magic_power = 0
for i in offered_items:
    list_total_magic_power += i.magic_power


def battle():
    # weak raid
    if list_total_magic_power <= 100:
        present_weak_raider = select_weak_raiders.gen()
        present_amount_weak_raider = amount_weak_raiders.gen()
        print(f"SUDDENLY,  you see {present_amount_weak_raider} {present_weak_raider}s charging towards you")

    # strong raid
    if 100 < list_total_magic_power < 200:
        present_strong_raider = select_strong_raiders.gen()
        present_amount_strong_raider = amount_strong_raiders.gen()
        print(f"SUDDENLY, you see {present_amount_strong_raider} {present_strong_raider}s charging towards you")

    # invasion
    if list_total_magic_power >= 200:
        present_invasion = select_invasion_raiders.gen()
        present_amount_invasion = amount_invasion_raiders.gen()
        print(f"SUDDENLY, you see {present_invasion} {present_amount_invasion}s rushing towards you")
