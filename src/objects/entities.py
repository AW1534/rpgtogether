import random
from src.classes.entity import Entity

# region scavenge_entities
fire_dragon = Entity(
    name="FIRE-BREATHING DRAGON",
    description=f"A big scary fire-breathing dragon, you should probably run.",
    hp=50,
    damage=35,
    hostile=True,
    rarity=1
)

ogre = Entity(
    name="OGRE",
    description="A goofy looking ogre, doesn't look that dangerous right..?",
    hp=random.randint(20,30),
    damage=random.randint(8,12),
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
    hp=random.randint(7,13),
    damage=random.randint(2,4),
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

beast = Entity(
    name="Hungry beast",
    hostile=True,
    description="Stay near and you're lunch",
    hp=random.randint(20,23),
    damage=random.randint(9,11),
    agility=random.randint(3,5),
    rarity=50
)

hound = Entity(
    name="Bloodhound",
    hostile=True,
    description="Bloodshot eyes, how did they even get that?",
    hp=random.randint(10,13),
    damage=random.randint(9,11),
    agility=random.randint(15,20),
    rarity=50
)

# jus text me on discord man

# endregion