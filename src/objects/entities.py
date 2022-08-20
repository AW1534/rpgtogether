import random
from src.classes.entity import Entity

# region scavenge_entities
fire_dragon = Entity(
    name="FIRE-BREATHING DRAGON",
    description=f"A big scary fire-breathing dragon, you should probably run.",
    hp=random.randint(50, 60),
    damage=random.randint(30, 40),
    hostile=True,
    rarity=1
)

ogre = Entity(
    name="OGRE",
    description="A goofy looking ogre, doesn't look that dangerous right..?",
    hp=random.randint(20, 30),
    damage=random.randint(8, 12),
    hostile=True,
    rarity=12
)

sus = Entity(
    name="Mysterious creature",
    description="???",
    hp=random.randint(10, 75),
    damage=random.randint(5, 30),
    hostile=random.choice([True, False]),
    rarity=3
)

zombie = Entity(
    name="Zombie",
    hostile=True,
    description="A regular zombie rotting away in the sun",
    hp=random.randint(7, 13),
    damage=random.randint(2, 4),
    rarity=14
)

deer = Entity(
    name="Deer",
    hostile=False,
    description="A harmless deer",
    hp=15,
    damage=0,
    rarity=20
)

sheep = Entity(
    name="Sheep",
    hostile=False,
    description="A fluffy sheep",
    hp=10,
    damage=0,
    rarity=20
)

pig = Entity(
    name="Pig",
    hostile=False,
    description="An adorable pig",
    hp=10,
    damage=0,
    rarity=20
)

# endregion

# region raiders

# weak raids

beast = Entity(
    name="Hungry beast",
    hostile=True,
    description="Stay near and you're lunch",
    hp=random.randint(13, 17),
    damage=random.randint(9, 11),
    agility=random.randint(3, 5),
    rarity=2
)

hound = Entity(
    name="Bloodhound",
    hostile=True,
    description="Bloodshot eyes, how did they even get that?",
    hp=random.randint(10, 13),
    damage=random.randint(9, 11),
    agility=random.randint(15, 20),
    rarity=2
)

goblin = Entity(
    name="Goblin",
    hostile=True,
    description="Quickkk, hide your gold!",
    hp=random.randint(16, 20),
    damage=random.randint(9, 11),
    agility=random.randint(7, 9),
    rarity=1
)

# strong raids
bull = Entity(
    name="Raging bull",
    hostile=True,
    description="You better not be waving a red cloth",
    hp=random.randint(17, 21),
    damage=random.randint(13, 15),
    agility=12,
    rarity=2
)
boa = Entity(
    name="Boa",
    hostile=True,
    description="Wait, how did boas get here?!",
    hp=random.randint(14, 18),
    damage=random.randint(13, 15),
    agility=19,
    rarity=1
)
mutant_bee = Entity(
    name="Mutant bumblebee",
    hostile=True,
    description="Do I really smell like honey?",
    hp=random.randint(11, 17),
    damage=random.randint(11, 14),
    agility=21,
    rarity=1
)
# endregion
# region invasions
raider = Entity(
    name="Masked raiders",
    hostile=True,
    description="I'm sure they can wear more fashionable clothes",
    hp=random.randint(7, 11),
    damage=random.randint(11,14),
    agility=(9,11),
    rarity=1
)

# endregion