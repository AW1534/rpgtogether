raise Exception
# rendering system is the very first thing to be imported, as it will show the loading screen
import asyncio
import time
import pymongo
import random
import traceback
from pymongo.server_api import ServerApi
from src.helper.rendering import __Renderer, Page
from src.helper import formatting
from src.helper import hlist
from src.commands import blessing, crafting, debug, enchanting, equip, gateway, heal, help, hunt, mine, quit, randevent, \
    scavenge, \
    shop, statue, trader
from src.classes import player
from src.config import config

renderer = __Renderer(
    splash=Page(
        title="RPGTogether is starting up",
        text=[f"If this is taking too long, please contact the creators:",
              f"{formatting.hyperlink('https://github.com/AW1534/rpgtogether', 'Github')}"]
    )
)

print(config)

client = pymongo.MongoClient(config["MONGO"], server_api=ServerApi('1'))
db = client.db
users = db.users

input = renderer.input

r = random.Random()

l = hlist.Unique_generator(
    [
        "Enjoy your stay!",
        "Use help for help on specific commands!",
        "Now begins your new adventure!",
        "You can only have one blessing at a time"
    ]
)

welcome = Page(title="Welcome to RPGTogether", text=l.pick(1), center_title_character="+")
renderer.set_page(welcome)

done = False


def loading_animation(x):
    if done: return 1
    x.set_page(Page(title="Welcome to RPGTogether", text=l.pick(1), center_title_character="+"))


# renderer.animate(loading_animation, interval=0.1)

time.sleep(2)
done = True

p = None

# TODO: try to load player automatically using save data
# TODO: achievements
# TODO: quests


func_loop = asyncio.new_event_loop()
update_loop = asyncio.new_event_loop()


def loop():
    func_loop.run_forever()


# t1 = threading.Thread(target=loop, daemon=True).run()

# update_loop.run_forever()

if p is None:
    p = player.Player(
        name=input("username: ")
    )

active_commands = [blessing, crafting, debug, enchanting, equip, gateway, heal, hunt, mine, quit, scavenge,
                   shop, statue, trader]
passive_commands = [randevent.wandering, randevent.coin_drop]
other_commands = [p.checkbal, p.checkinv, help]

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

        if cmd in ["checkbal", "balance", "bal"]:
            Page(title="wallet", text=p.checkbal())

        if cmd in ["checkinv", "inventory", "inv"]:
            Page(title="inventory", text=p.checkinv())
