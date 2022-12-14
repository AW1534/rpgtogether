from src.objects import items
from src.objects import enchantments
from src.helper.rng import Roulette


# region outcomes
list_wandering_outcomes_give = ["Killed", "Repay", "Enchant", "Enchant", "Steal", "Steal", "Attempt", "Attempt",
                                "Attempt"]
list_wandering_outcomes_walk = ["Leave", "Leave", "Leave", "Leave", "Leave", "Die"]
list_wandering_outcomes_attack = ["Slay", "Ambush", "Escape"]
list_attempt_outcome_kill = ["Decap", "Escape"]
list_attempt_outcome_spare = ["Enchant", "Die", "Die"]
# endregion
# region roulettes
random_give = Roulette(
    choices=list_wandering_outcomes_give,
    nothing_chance=0
)
random_walk = Roulette(
    choices=list_wandering_outcomes_walk,
    nothing_chance=0
)
random_attack = Roulette(
    choices=list_wandering_outcomes_attack,
    nothing_chance=0
)
random_kill = Roulette(
    choices=list_attempt_outcome_kill,
    nothing_chance=0
)
random_spare = Roulette(
    choices=list_attempt_outcome_spare,
    nothing_chance=0
)


# endregion
def wandering(Player):
    print("-----------------------------------------------------")
    choice = input(
        "A wanderer walks up to you and begs for food.\nWhat do you do?\t>Give food<\t>Walk away<\t>Attack him<")
    if choice == "give food":
        outcome_give = random_give.gen()
        if outcome_give == "Killed":
            print("The wanderer grabs a KNIFE and STABS you, before running away into the forest")
        if outcome_give == "Repay":
            print(f"The wanderer devours the food and thanks you by handing you a {items.pill.description.upper()}")
            Player.trade(gains=items.pill)
        if outcome_give == "Enchant":
            print(
                f"The wanderer takes off his hood and ENCHANTS your armour with {enchantments.one_for_all.name.upper()}")
        if outcome_give == "Steal":
            print("The wanderer snatches the food out of your hand and runs off, never to be seen again.")
        if outcome_give == "Attempt":
            attempt_choice = input(f"The wanderer grabs a KNIFE and tries to STAB you, but he was so hungry that "
                                   f"he collapsed to the floor. What will you do now?\n>Kill him<\t>Spare him<")
            if attempt_choice == "kill him":
                attempt_outcome_kill = random_kill.gen()
                if attempt_outcome_kill == "Decap":
                    print("You mercilessly decapitate the wanderer.")
                if attempt_outcome_kill == "Escape":
                    print("You swing at the wanderer, but before the sword struck he GRABS your foot and swings you "
                          "around like a madman, before launching you at the wall and running away. He leaves behind a"
                          f"{items.gemstone}")
                    Player.trade(gains=items.gemstone)
            if attempt_choice == "spare him":
                attempt_outcome_spare = random_spare.gen()
                if attempt_outcome_spare == "Enchant":
                    print(f"You spare the wanderer and feed him. He gets up and enchants your armour with "
                          f"{enchantments.e_synergy.name.upper()} out of guilt")
                if attempt_outcome_spare == "Die":
                    print("You spare the wanderer and leave him to die.")

        if choice == "walk away":
            outcome_walk = random_walk.gen()
            if outcome_walk == "Leave":
                print("You ignore the wanderer and walk away, never to be seen again.")
            if outcome_walk == "Die":
                print("You ignore the wanderer and walk away, but the wanderer chases you and stabs you in the back.")
        if choice == "attack him":
            outcome_attack = random_attack.gen()
            if outcome_attack == "Slay":
                print("You mercilessly destroy the wanderer. As you rummage through his belongings, you find a"
                      f" {items.gemstone}")
                Player.trade(gains=items.gemstone)
            if outcome_attack == "Ambush":
                print("You slash at the wanderer, but another sword sinks deep into your spine.")
            if outcome_attack == "Escape":
                print("You swing at the wanderer, but the wanderer dodges your blade and runs off into the distance.")
    print("-----------------------------------------------------")


def coin_drop(Player):
    print("----------------------------------------------------")
    print("WAIT WHAAT?? THERE'S COINS DROPPING OUT OF THE SKY??")
    response = input("Type:`GO AWAY IT'S ALL MINE!!11!`for free coins!")
    print("----------------------------------------------------")
    coins = Player.agility * 7304
    coin = Player.agility * 2489
    if response == "GO AWAY IT'S ALL MINE!!11!":
        print(f"Collected {coins} nuelis")
        Player.trade(gains_nuelis=coins)
    if response == "no":
        print("You walk away... and tripped over a sussy amogus life-size action figure")
        print("Some coins fell out of your pocket and rolled away")
        print(f"You lost {coin}")
        Player.trade(loses_nuelis=coin)
    else:
        print("oops, might want to get a new keyboard lmao")
