# rendering system is the very first thing to be imported, as it will show the loading screen
import asyncio
import time

import pymongo
from pymongo.server_api import ServerApi

from src.helper.rendering import __Renderer, Page
from src.helper import formatting

renderer = __Renderer(
    splash=Page(
        title="RPGTogether is starting up",
        text=[f"If this is taking too long, please contact the creators:",
              f"{formatting.hyperlink('https://github.com/AW1534/rpgtogether', 'Github')}"]
    )
)

from src.helper import hlist

import random

import traceback

from src.commands import scavenge, hunt, shop, debug, mine, statue, gateway, quit, randevent
from src.classes import player

from src.config import config

import threading

print(config)

client = pymongo.MongoClient(config["MONGO"], server_api=ServerApi('1'))
db = client.db
users = db.users

input = renderer.input

active_commands = [scavenge, hunt, shop, debug, mine, statue, gateway, quit]
passive_commands = [randevent.wandering, randevent.coin_drop]

r = random.Random()

l = hlist.Unique_generator(
    [
        "Enjoy your stay!",
        "Use help for help on specific commands!",
        "Now begins your new adventure!",
        "i like men"
    ]
)

welcome = Page(title="Welcome to RPGTogether", text=l.pick(1), center_title_character="+")
renderer.set_page(welcome)

done = False


def loading_animation(x):
    if done: return 1
    x.set_page(Page(title="Welcome to RPGTogether", text=l.pick(1), center_title_character="+"))


#renderer.animate(loading_animation, interval=0.1)

time.sleep(2)  # poopoo
done = True

p = None

# TODO: try to load player automatically using save data
# TODO: achievements
# TODO: quests
# TODO: prestige??

func_loop = asyncio.new_event_loop()
update_loop = asyncio.new_event_loop()


def loop():
    func_loop.run_forever()


#t1 = threading.Thread(target=loop, daemon=True).run()

#update_loop.run_forever()

if p is None:
    p = player.Player(
        name=input("username: ")
    )

while True:
    raw_input = input(">>\t")

    l = raw_input.split(" ")
    cmd = l[0].lower()

    l2 = l
    l2.pop(0)  # list of args

    for active in active_commands:
        if cmd in active.aliases or cmd == active.name:
            try:
                active.run(p, l2, renderer)

            except Exception as e:
                traceback.print_exc()
