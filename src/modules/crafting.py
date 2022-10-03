import time
from src.objects import items
from src.helper import formatting


def run(player, args):
    global crafting_recipe
    craftables = [items.composite_sword, items.plated_armour, items.book.recipe, items.enchanting_setup
                  ]

    craftables_recipe = [("composite sword", items.composite_sword.recipe),
                         ("plated armor", items.plated_armour.recipe),
                         ("book", items.book.recipe),
                         ("enchanting setup", items.enchanting_setup.recipe)
                         ]
    ready = []

    try:
        crafting = args[0]
    except IndexError:
        crafting = input(">>Workshop\n What would you like to craft? ")
        for i in craftables:
            print(f"{i.name}:\t{', '.join(i.recipe)}")

    for i in craftables_recipe:
        if i == crafting:
            crafting_recipe = i[1]

    for i in crafting_recipe:
        if i not in player.inventory:
            formatting.add_border("crafting", "You do not have enough items to craft this item")
            ready = []
        else:
            ready.append(i)


