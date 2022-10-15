from src.objects.items import all_items

print = print

name = "."
aliases = [""]


def run(p, args, r):
    print = r.print
    try:
        print(args)
        if args[0] == "inv":
            print("Items:")
            [print(str(i)) for i in p.inventory]

        if args[0] == "get":
            for i in all_items:
                if args[1].lower() == i.name.lower():
                    p.trade(gains=i)

            [print(str(i)) for i in p.inventory]

    except IndexError:
        print("commands: inv")

