import time
from src import rng
from src.objects import items


def run(player, args):
    craftables = [items.sword, items.chainmail]

    try:
        crafting = args[0]
    except IndexError:
        crafting = input(">>Workshop\n What would you like to craft? ")
        for i in craftables:
            print(f"{i.name}:\t{', '.join(i.recipe)}")

    if crafting == "steel sword":
        print("crafting steel sword...will be ready in 10 seconds")
        time.sleep(10)
        #rusted_sword, 3 blocks of iron
    elif crafting == "chainmail":
        print("crafting chainmail...will be ready in 10 seconds")
        time.sleep(10)
        #15 blocks of iron
    elif crafting == "magical book":
        print("crafting magical book...will be ready in 15 seconds")
        time.sleep(15)
        #20 torn pages
    elif crafting == "enchanting setup":
        print("setting up enchanting setup...will be ready in 30 seconds")
        time.sleep(30)
        #5 magical books,
