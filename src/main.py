import traceback

from src.modules import scavenge, hunt, shop, debug, mine, statue
from src.classes import player

commands = [scavenge, hunt, shop, debug, mine, statue]

print("----------------------\nWelcome to RPGTogether\n----------------------\n")

p = None

# TODO: try to load player automatically using save file
# TODO: achievements
# TODO: quests
# TODO: magical disguised gambling
# TODO: prestige??
# TODO: random events

if p == None:
    p = player.Player(input("username: "))

while True:
    raw_input = input(">>\t")

    l = raw_input.split(" ")
    cmd = l[0].lower()

    l2 = l
    l2.pop(0)

    for command in commands:
        if cmd in command.aliases or cmd == command.name:
            try:
                command.run(p, l2)
            except Exception as e:
                traceback.print_exc()
