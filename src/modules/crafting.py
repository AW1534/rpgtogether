import time
from src.objects import items


def run(player, args):
    craftables = [items.sword, items.chainmail]

    try:
        crafting = args[0]
    except IndexError:
        crafting = input(">>Workshop\n What would you like to craft? ")
        for i in craftables:
            print(f"{i.name}:\t{', '.join(i.recipe)}")

    if crafting == "composite sword":
        print("crafting composite sword...will be ready in 10 seconds")
        time.sleep(10)

    elif crafting == "plated armour":
        print("crafting plated armour...will be ready in 10 seconds")
        time.sleep(10)

    elif crafting == "magical book":
        print("crafting magical book...will be ready in 15 seconds")
        time.sleep(15)

    elif crafting == "enchanting setup":
        print("setting up enchanting setup...will be ready in 30 seconds")
        time.sleep(30)

