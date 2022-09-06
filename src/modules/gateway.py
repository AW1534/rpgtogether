import time
from src.helper import option
from src.objects import items
from src.classes import player


def run(p: player):
    print("A giant gateway appears before you. On the side you notice a small tablet\n"
          "engraved into the wall. It seems to be a keyhole and a... square hole?\n"
          "Maybe a cube could fit inside it...?\n")
    x = 0
    if items.key in p.inventory:
        x = 1
    y = 0
    if items.cube in p.inventory:
        y = 1

    opening = ""

    try:
        if x or y == 0:
            print("Looks like you don't have enough items")
        else:
            opening = input(f"You have {x}/1 key and you have {y}/1 cube.\nDo you want to insert them?\n>>\t")
    except TypeError:
        print("Invalid Input")
        quit(run(p))

    if opening == option.no:
        print("Leaving the gates...")
        quit(run(p))

    if opening in option.yes:
        p.trade(loses=items.key)
        p.trade(loses=items.cube)
        print("You insert the glowing cube and the key into the wall...")
        time.sleep(2)
        print("CRAAAANKKK!!")
        time.sleep(0.5)
        print("The gates slowly open, with rays of blinding light beaming out.")



