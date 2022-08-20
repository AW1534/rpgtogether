from src.objects import items
from src.objects import enchantments

list_wandering_outcomes_give = ["Killed", "Repay", "Enchant", "Enchant", "Steal", "Steal", "Attempt", "Attempt",
                                "Attempt"]
list_wandering_outcomes_walk = ["Leave", "Leave", "Leave", "Leave", "Leave", "Die"]
list_wandering_outcomes_attack = ["Slay", "Ambush", "Escape"]
list_attempt_outcome_kill = ["Decap", "Escape"]
list_attempt_outcome_spare = ["Enchant", "Die", "Die"]

def wandering():
    choice = input(
        "A wanderer walks up to you and begs for food\nWhat do you do?\t>Give food<\t>Walk away<\t>Attack him<")
    if choice == "give food":
        outcome_give = list_wandering_outcomes_give.gen()
        if outcome_give == "Killed":
            print("The wanderer grabs a KNIFE and STABS you, before running away into the forest")
        if outcome_give == "Repay":
            print(f"The wanderer devours the food and thanks you by handing you a {items.pill.description.upper()}")
        if outcome_give == "Enchant":
            print(
                f"The wanderer takes off his hood and ENCHANTS your armour with {enchantments.one_for_all.name.upper()}")
        if outcome_give == "Steal":
            print("The wanderer snatches the food out of your hand and runs off, never to be seen again.")
        if outcome_give == "Attempt":
            attempt_choice = input(f"The wanderer grabs a KNIFE and tries to STAB you, but he was so hungry that "
                                   f"he collapsed to the floor. What will you do now?\n>Kill him<\t>Spare him<")
            if attempt_choice == "kill him":
                attempt_outcome_kill = list_attempt_outcome_kill.gen()
                if attempt_outcome_kill == "Decap":
                    print("You mercilessly decapitate the wanderer.")
                if attempt_outcome_kill == "Escape":
                    print("You swing at the wanderer, but before the sword struck he GRABS your foot and swings you "
                          "around like a madman, before launching you at the wall and running away. He leaves behind a"
                          f"{items.gemstone}")
            if attempt_choice == "spare him":
                attempt_outcome_spare = list_attempt_outcome_spare.gen()
                if attempt_outcome_spare == "Enchant":
                    print(f"You spare the wanderer and feed him. He gets up and enchants your armour with "
                          f"{enchantments.e_synergy.name.upper()} out of guilt")
                if attempt_outcome_spare == "Die":
                    print("You spare the wanderer and leave him to die.")

        if choice == "walk away":
            outcome_walk = list_wandering_outcomes_walk.gen()
            if outcome_walk == "Leave":
                print("You ignore the wanderer and walk away, never to be seen again.")
            if outcome_walk == "Die":
                print("You ignore the wanderer and walk away, but the wanderer chases you and stabs you in the back.")
        if choice == "attack him":
            outcome_attack = list_wandering_outcomes_attack.gen()
            if outcome_attack == "Slay":
                print("You mercilessly destroy the wanderer. As you rummage through his belongings, you find a"
                      f" {items.gemstone}")
            if outcome_attack == "Ambush":
                print("You slash at the wanderer, but another sword sinks deep into your spine.")
            if outcome_attack == "Escape":
                print("You swing at the wanderer, but the wanderer dodges your blade and runs off into the distance.")



