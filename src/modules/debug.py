name = "."
aliases = [""]

def run(p, args):
    print(args)
    if args[0] == "inv":
        print("Items:")
        print(p.inventory)