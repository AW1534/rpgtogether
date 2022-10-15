import random
import math
from src.classes.player import Player
from src.objects import items
from src.helper import rng
from src.helper.rendering import Page
from src.objects import entities
from src import helper

name = "statue"
aliases = ["offer", "offering"]
description = "Toss some stones into the water to restore the statue's magic, and you will receive a reward"
cooldown = 10 * 60
cooldown_warning = "The statue lost all it's power for now, wait {cooldown} seconds"

offerable_items = []
offered_items = []

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

# endregion
for i in items.all_items_withcombat:
    if i.magic_power > 0:
        offerable_items.append(i)

total_mp = 0
for i in offered_items:
    total_mp += i.magic_power


def battle(player, rendering):
    # weak raid
    if total_mp <= 100:
        present_weak_raider = select_weak_raiders.gen()
        present_amount_weak_raider = random.randint(1, 4)
        text = Page(title="Statue",
                    text=f"SUDDENLY,  you see {present_amount_weak_raider} {present_weak_raider}s charging towards you"
                    , center_title=False)
        team = [present_weak_raider for i in range(present_amount_weak_raider)]
        weak = rng.Fight(
            teams=team
        )
        result = Page(text=weak.fight(player=player))

    # strong raid
    if 100 < total_mp < 200:
        present_strong_raider = select_strong_raiders.gen()
        present_amount_strong_raider = random.randint(3, 6)
        text = Page(title="Statue",
                    text=f"SUDDENLY, you see {present_amount_strong_raider} {present_strong_raider}s charging towards you",
                    center_title=False)
        team = [present_strong_raider for i in range(present_amount_strong_raider)]
        strong = rng.Fight(
            teams=team
        )
        result = Page(text=strong.fight(player=player))

    # invasion
    if total_mp >= 200:
        present_invasion = select_invasion_raiders.gen()
        present_amount_invasion = random.randint(15, 23)
        text = Page(title="Statue",
                    text=f"SUDDENLY, you see {present_invasion} {present_amount_invasion}s rushing towards you",
                    center_title=False)
        team = [present_invasion for i in range(present_amount_invasion)]
        invade = rng.Fight(
            teams=team
        )
        result = Page(text=invade.fight(player=player))

    essence = math.ceil(total_mp / 10)

    player.trade(gains_essence=essence)

    end = Page(title="Statue", text=f"You gained {essence} magical essence. You currently have {player.essence}")


def run(p, args, r):
    offerable_item_names = []
    offerable_obj = []
    for i in Player.inventory:
        if i in offerable_items:
            offerable_item_names.append(i.name)
            offerable_obj.append(i)

    offer = Page(title="Statue", text="Items available to offer:\n")

    l_string = helper.hlist.sort_to_string(offerable_item_names)
    for i, sel in enumerate(l_string):
        print(f"{i}: {sel}")

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

    battle(p, r)



