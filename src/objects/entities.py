import random
from src.classes.entity import Entity
from src.objects import items
# region randevent entities
# endregion
# region scavenge entities
fire_dragon = Entity(
    name="FIRE-BREATHING DRAGON",
    description=f"A big scary fire-breathing dragon, you should probably run.",
    base_max_health=random.randint(50, 60),
    base_damage=random.randint(30, 40),
    hostile=True,
    rarity=1,
    inventory=[items.dragon_wing, items.dragon_scale]
)

ogre = Entity(
    name="OGRE",
    description="A goofy looking ogre, doesn't look that dangerous right..?",
    base_max_health=random.randint(20, 30),
    base_damage=random.randint(8, 12),
    hostile=True,
    rarity=12
)

sus = Entity(
    name="Mysterious creature",
    description="???",
    base_max_health=random.randint(10, 75),
    base_damage=random.randint(5, 30),
    hostile=random.choice([True, False]),
    rarity=3,
    inventory=[items.all_items]
)

zombie = Entity(
    name="Zombie",
    hostile=True,
    description="A regular zombie rotting away in the sun",
    base_max_health=random.randint(7, 13),
    base_damage=random.randint(2, 4),
    rarity=14,
    inventory=[items.nails]
)

deer = Entity(
    name="Deer",
    hostile=False,
    description="A harmless deer",
    base_max_health=15,
    base_damage=0,
    rarity=20,
    inventory=[items.fabric]
)

sheep = Entity(
    name="Sheep",
    hostile=False,
    description="A fluffy sheep",
    base_max_health=10,
    base_damage=0,
    rarity=20,
    inventory=[items.fabric]
)

pig = Entity(
    name="Pig",
    hostile=False,
    description="An adorable pig",
    base_max_health=10,
    base_damage=0,
    rarity=20
)

# endregion

# region raiders

# weak raids

beast = Entity(
    name="Hungry beast",
    hostile=True,
    description="Stay near and you're lunch",
    base_max_health=random.randint(13, 17),
    base_damage=random.randint(9, 11),
    agility=random.randint(3, 5),
    rarity=2
)

hound = Entity(
    name="Bloodhound",
    hostile=True,
    description="Bloodshot eyes, how did they even get that?",
    base_max_health=random.randint(10, 13),
    base_damage=random.randint(9, 11),
    agility=random.randint(15, 20),
    rarity=2
)

goblin = Entity(
    name="Goblin",
    hostile=True,
    description="A goblin, quick, hide your gold!",
    base_max_health=random.randint(16, 20),
    base_damage=random.randint(9, 11),
    agility=random.randint(7, 9),
    rarity=1
)

# strong raids
bull = Entity(
    name="Raging bull",
    hostile=True,
    description="You see the sheer anger in it's eyes.",
    base_max_health=random.randint(17, 21),
    base_damage=random.randint(13, 15),
    agility=12,
    rarity=2
)
boa = Entity(
    name="Boa",
    hostile=True,
    description="Wait, how did boas get here?!",
    base_max_health=random.randint(14, 18),
    base_damage=random.randint(13, 15),
    agility=19,
    rarity=1
)
mutant_bee = Entity(
    name="Mutant bumblebee",
    hostile=True,
    description="Do I really smell like honey?",
    base_max_health=random.randint(11, 17),
    base_damage=random.randint(11, 14),
    agility=21,
    rarity=1
)
# endregion
# region invasions
raider = Entity(
    name="Masked raiders",
    hostile=True,
    description="I'm sure they can wear more fashionable clothes",
    base_max_health=random.randint(7, 11),
    base_damage=random.randint(11,14),
    agility=(9,11),
    rarity=1
)
# endregion

