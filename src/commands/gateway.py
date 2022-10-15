import time
import random
from src.helper import option, formatting
from src.objects import items
from src.classes import player
from src.objects.entities import gateway_dragon

name = "gateway"
aliases = ["g", "end fight", "dungeon"]
description = "Woah.. what's that snoring coming from behind those gates?"
cooldown = 0
cooldown_warning = ""


class Move:
    aliases = []
    dmg = 0
    defence = 0
    heal = 0
    risk = 0

    def __init__(self, aliases=None, dmg=0, defence=0, heal=0, risk=0):
        if aliases is None:
            aliases = []

        self.aliases = aliases
        self.dmg = dmg
        self.defence = defence
        self.heal = heal
        self.risk = risk


slash = Move(
    aliases=["slash", "s", "swing"],
    dmg=40,
    defence=0,
    heal=0,
    risk=7
)
thrust = Move(
    aliases=["thurst", "t", "stab"],
    dmg=60,
    defence=0,
    heal=0,
    risk=20
)
awaken = Move(
    aliases=["awaken", "a"],
    dmg=999999,
    defence=999999,
    heal=999999,
    risk=99
)
block = Move(
    aliases=["block", "b", "shield"],
    dmg=0,
    defence=75,
    heal=0,
    risk=1
)
eat = Move(
    aliases=["eat", "e", "heal"],
    dmg=0,
    defence=20,
    heal=100,
    risk=10
)
escape = Move(
    aliases=["escape", "es", "run"],
    dmg=0,
    defence=0,
    heal=0,
    risk=70
)

turns = 0


def next_turn(p):
    moves = [slash, thrust, awaken, block, eat, escape]

    move_ref = [(slash.aliases, slash),
                (thrust.aliases, thrust),
                (awaken.aliases, awaken),
                (block.aliases, block),
                (eat.aliases, eat),
                (escape.aliases, escape)
                ]

    def ask_for_move(p):
        if turns == 0:
            move = input(formatting.add_border(
                "gateway",
                f"{p}, choose your move:\n"
                f"SLASH\n"
                f"THRUST\n"
                f"BLOCK\n"
                f"EAT\n"
                f"ESCAPE"))

            # checking through aliases for input
            for i in move_ref:
                for j in i:
                    for k in j[0]:
                        if k == move.lower():
                            chosen_move = j
                            # end

                            attack = (chosen_move.dmg / 100) * p.damage
                            defense = (chosen_move.defence / 100) * p.health
                            heal = chosen_move.heal * (p.health / 500)
                            risk = chosen_move.risk - p.agility

                            if risk <= 0:
                                risk = 0

                            if attack > 0:
                                gateway_dragon.health -= attack
                                print(formatting.add_border(
                                    "gateway", f"YOU HIT THE DRAGON FOR {attack} HEALTH!\n"
                                               f"the dragon is on {gateway_dragon.health} hp"))

                            if defense > 0:
                                gateway_dragon.damage -= defense
                                print(formatting.add_border(
                                    "gateway", f"You enter your defensive stance\n"
                                               f"you take {defense} less damage next turn"))
                            if heal > 0:
                                p.health += heal
                                print(formatting.add_border(
                                    "gateway", f"You grab out a random glowing chicken leg and start biting down.\n"
                                               f"you healed {heal} hp, your current health is {p.health}"))
                            safe = 100 - risk
                            lst = []

                            for i in range(risk):
                                lst.append("death")
                            for i in range(safe):
                                lst.append("live")

                            outcome = random.choice(lst)

                            if outcome == "death":
                                p.health = 0
                            else:
                                pass

            else:
                formatting.add_border("move", p + ", please enter a valid move")

        else:
            move = input(formatting.add_border(
                "gateway",
                f"{p}, choose your next move:\n"
                f"SLASH\n"
                f"THRUST\n"
                f"BLOCK\n"
                f"EAT\n"
                f"ESCAPE"))

            # checking through aliases for input
            for i in move_ref:
                for j in i:
                    for k in j[0]:
                        if k == move.lower():
                            chosen_move = j
                            # end

                            attack = (chosen_move.dmg / 100) * p.damage
                            defense = (chosen_move.defence / 100) * p.health
                            heal = chosen_move.heal * (p.health / 500)
                            risk = chosen_move.risk - p.agility
                            if risk <= 0:
                                risk = 0

                            if attack > 0:
                                gateway_dragon.health -= attack
                                print(formatting.add_border(
                                    "gateway", f"YOU HIT THE DRAGON FOR {attack} HEALTH!\n"
                                               f"the dragon is on {gateway_dragon.health} hp"))

                            if defense > 0:
                                gateway_dragon.damage -= defense
                                print(formatting.add_border(
                                    "gateway", f"You enter your defensive stance\n"
                                               f"you take {defense} less damage next turn"))
                            if heal > 0:
                                p.health += heal
                                print(formatting.add_border(
                                    "gateway", f"You grab out a random glowing chicken leg and start biting down.\n"
                                               f"you healed {heal} hp, your current health is {p.health}"))
                            safe = 100 - risk
                            lst = []

                            for i in range(risk):
                                lst.append("death")
                            for i in range(safe):
                                lst.append("live")

                            outcome = random.choice(lst)

                            if outcome == "death":
                                p.health = 0
                            else:
                                pass

            else:
                formatting.add_border("move", p + ", please enter a valid move")

    ask_for_move(p)


game_running = True


def check_win(p):
    if gateway_dragon.health == 0:
        formatting.add_border("gateway", f"YOU HAVE SLAYED THE ALMIGHTY DRAGON")
        global game_running
        game_running = False

    if p.health == 0:
        p.death()
        game_running = False


def open(p):
    print("A giant gateway appears before you. On the side you notice a small tablet\n"
          "engraved into the wall. It seems to be a keyhole and a... square hole?\n"
          "Maybe a cube could fit inside it...?\n")
    x = 0
    if items.key in p.inventory:
        x = 1
    y = 0
    if items.cube in p.inventory:
        y = 1

    opening = ""

    try:
        if x or y == 0:
            print("Looks like you don't have enough items")
        else:
            opening = input(f"You have {x}/1 key and you have {y}/1 cube.\nDo you want to insert them?\n>>\t")
    except TypeError:
        print("Invalid Input")


    if opening == option.no:
        print("Leaving the gates...")
        quit(run(p))

    if opening in option.yes:
        p.trade(loses=items.key)
        p.trade(loses=items.cube)
        print("You insert the glowing cube and the key into the wall...")
        time.sleep(2)
        print("CRAAAANKKK!!")
        time.sleep(0.5)
        print("The gates slowly open, with rays of blinding light beaming out.")


def run(p: player, args, r):
    open(p)

    while game_running is True:
        next_turn(p)
        check_win(p)


