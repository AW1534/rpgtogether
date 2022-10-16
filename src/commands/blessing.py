from src.helper.rendering import Page
from src.helper import hlist, option
from src.objects import blessings


def bless(player, args):
    s_i = []
    for i in player.inventory:
        if i in blessings.all_blessings:
            s_i.append(i.name)
        else:
            continue

    print("Equippable items:\n")

    l_string = hlist.sort_to_string(s_i)
    lst = [f"{i + 1}: {blessing}" for i, blessing in enumerate(l_string)]

    lst.append(f"\nchoose a blessing (1-{len(l_string)}) >> ")

    select = int(input(Page(title="Blessing", text=lst, center_title=False)))

    blessing = player.inventory[select - 1]

    trade = player.trade(
        loses=[blessing]
    )

    player.blessing = blessing

    out = Page(title="Blessing", text=f"{player.name}, you have been blessed with {blessing.name}", center_title=False)


def unbless(player, args):
    state = Page(title="Blessing", text=[f"{player.name}, you are currently blessed with {player.blessing.name}",
                                         "Do you want to remove this blessing? (Y/N)\n>>\t"])
    confirm = input()

    if confirm in option.yes:
        out = Page(title="Blessing", text=f"Removed {player.blessing.name} from {player.name}", center_title=False)
        player.trade(gains=player.blessing)
        player.blessing = None

    if confirm in option.no:
        out = Page(title="Blessing", text="Remove blessing canceled", center_title=False)

    else:
        out = Page(title="Blessing", text="Please enter a valid response next time....", center_title=False)


def run(player, args, rendering):
    if args[0].lower() in ["bless", "b"]:
        bless(player, args)
    if args[0].lower() in ["unbless", "b"]:
        unbless(player, args)
    else:
        print("Invalid Argument")
