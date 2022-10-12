# rendering system is the very first thing to be imported, as it will show the loading screen
import time

from src.helper.rendering import renderer, Page

import random

import traceback

from src.modules import scavenge, hunt, shop, debug, mine, statue, gateway, quit
from src.classes import player

input = renderer.input

commands = [scavenge, hunt, shop, debug, mine, statue, gateway, quit]

r = random.Random()

tips = [
    "Enjoy your stay!",
    "Use help for help on specific commands!",
    "Now begins your new adventure!"
        ]

welcome = Page(title="Welcome to RPGTogether", text=[r.choice(tips)], center_title_character="+")
renderer.set_page(welcome)
cox = Page(title="I love cok", text=["d"], center_title_character="+")
renderer.set_page(cox)

done = False

def loading_animation(x):
    if done: return 1
    x.buffer[2] = r.choice(tips)


#renderer.animate(loading_animation, interval=3)

time.sleep(2)
done = True

p = None

# TODO: try to load player automatically using save data
# TODO: achievements
# TODO: quests
# TODO: magical disguised gambling
# TODO: prestige??

if p is None:
    p = player.Player(
        name=input("username: ")
    )

while True:
    raw_input = input(">>\t")

    l = raw_input.split(" ")
    cmd = l[0].lower()

    l2 = l
    l2.pop(0) # list of args

    for command in commands:
        if cmd in command.aliases or cmd == command.name:
            try:
                command.run(p, l2, renderer)
            except Exception as e:
                traceback.print_exc()
