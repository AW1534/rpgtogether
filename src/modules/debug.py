from src.objects.items import all_items


name = "."
aliases = [""]


def run(p, args):
    try:
        print(args)
        if args[0] == "inv":
            print("Items:")
            print(p.inventory)

        if args[0] == "getitem":
            for i in all_items:
                if args[1] == i.name:
                    p.trade(gains=i)

            print(p.inventory)

    except IndexError:
        print("commands: inv")

