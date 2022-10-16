from src.helper.rendering import Page
from src.objects.blessings import all_blessings


nln = "\n"


def run(player, args, renderer):
    start = Page(title="Trader", text="Welcome to the trader")
    if args[0] in [" ", None]:
        buy = Page(title="Trader", text=f"Items available to buy:{nln.join(all_blessings)}", center_title=False)

        buying = input("choose an item >> ")

        for i in all_blessings:
            if buying.lower() == i.name.lower():
                output = Page(title="Trader", text=f"Bought {i.name} for {i.value * 1.5}", center_title=False)

                player.trade(gains=i, loses_nuelis=i.value * 1.5)
        else:
            output = Page(title="Trader", text="Please enter a valid item", center_title=False)

    if args[0] is not None:
        for i in all_blessings:
            if args[0].lower() == i.name.lower():
                output = Page(title="Trader", text=f"Bought {i.name} for {i.value * 1.5}", center_title=False)

                player.trade(gains=i, loses_nuelis=i.value * 1.5)
        else:
            output = Page(title="Trader", text="Please enter a valid item", center_title=False)
