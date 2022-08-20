from src.objects import items

name = "shop"
aliases = ["shp", "sh", "sho"]
description = "A place to trade goods"

def run(p, args):
    inp = input("Welcome to the shop, are you buying or selling? (B/S) >> ").lower()
    if inp == "b":
        buy(p, args)
    elif inp == "s":
        sell(p, args)
    else:
        return
buyable_items = [
    items.health_pot,
    items.page,
    items.book,
    items.stone,
    items.rusted_sword,
    items.wooly_set,
    items.fishing_rod,
    items.chainmail
]
sellable_items = [
    items.rock,
    items.stone,
    items.book,
    items.page

]

nln = "\n"

def buy(p, args):
    print(f"Items available to buy:"
          f" {nln.join(buyable_items)}")

    buying = input("choose an item >> ")

    for i in buyable_items:
        if buying.lower() == i.name.lower():
            print(f"bought {i.name}")

def sell(p, args):
    obj_s_i = []
    s_i = []
    for i in p.inventory:
        if i in sellable_items:
            s_i.append(i.name)
            obj_s_i.append(i)

    print("Items available to sell:\n")

    i = 0
    l_string = src.helper.list.sort_to_string(s_i)
    for item in l_string:
        i += 1
        print(f"{i}: {item}")

    selling = int(input(f"\nchoose an item (1-{len(l_string)}) >> "))

    item = obj_s_i[selling-1]

    trade = p.trade(
        loses=[item],
        gains_rupees=item.value
    )

    if trade:
        input(f"Sold {item}... ")
    else:
        print("oof, looks like you don't have this item")