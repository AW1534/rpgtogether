from src.classes.item import Item, Armor
from src.objects import enchantments
import random

stone = Item(
    name="Magical stone",
    description="A mysterious luminescent orb",
    damage=0,
    value=2000,
    rarity=1,
    magic_power=75,
)
rope = Item(
    name="Rope",
    description="Sturdy rope",
    damage=0,
    value=20,
    rarity=25
)
page = Item(
    name="Torn page of a magical book",
    description="I wonder where this page came from...",
    damage=0,
    value=50,
    rarity=9,
    magic_power=5,
)
fabric = Item(
    name="Torn piece of fabric",
    description="Quite dirty, may need a wash",
    damage=0,
    value=125,
    rarity=10
)
book = Item(
    name="Magical book",
    description="Not sure what the cryptic words read, but seems important",
    damage=10,
    value=1500,
    rarity=1,
    recipe=[
        page, page, page, page, page, page, page, page, page, page, page, page, page, page, page, page, page, page,
        page, page,
        rope
    ],
    magic_power=125,
)
rock = Item(
    name="Rock",
    description="A regular rock, nothing special about it...",
    damage=5,
    value=20,
    rarity=30
)
iron = Item(
    name="Chunk of iron",
    description="Obtained from mining, useful for crafting",
    damage=5,
    value=100,
    rarity=15
)
gemstone = Item(
    name="Gemstone",
    description="Obtained from mining, quite a rare find",
    damage=5,
    value=750,
    rarity=1,
    magic_power=100
)

# region utilities

health_pot = Item(
    name="Heal Potion",
    description="A classic potion, smells sweet",
    damage=0,
    value=50,
)
pill = Item(
    name="Suspicious Pill",
    description="A mysterious looking pill, is it safe to eat?",
    damage=-9999,
    value=10001,
    health=random.randint()

)
enchanting_setup = Item(
    name="Enchanting Setup",
    description="Mysterious set of books which possess vast amounts of knowledge",
    damage=0,
    value=11250,
)
# endregion

# region combat


wooly_set = Armor(
    name="Wooly Set",
    description="Cosy set, but not very durable",
    damage=10,
    value=400,
    health=30,
    enchantable=enchantments.all_armor_enchantments,
)
chainmail = Armor(
    name="Chainmail Armor",
    description="Sturdy chainmail armor",
    damage=10,
    health=75,
    value=1000,
    agility=-2,
    enchantable=enchantments.all_armor_enchantments
)
plated = Armor(
    name="Plated Armor",
    description="I can barely move",
    damage=10,
    health=100,
    value=1350,
    agility=-5,
    enchantable=enchantments.all_armor_enchantments,
    recipe=[iron, iron, iron, iron, iron, iron, iron, iron, iron, iron, iron, iron,
            fabric, fabric, fabric, fabric, fabric, fabric, fabric, fabric]
)
rusted_sword = Item(
    name="Rusted Sword",
    description="Sword.. a tiny bit old though",
    damage=20,
    value=250,
    enchantable=enchantments.all_weapon_enchantments
)
sword_regular = Item(
    name="Steel Sword",
    description="A regular sword, forged from steel",
    damage=20,
    value=600,
    enchantable=enchantments.all_weapon_enchantments
)
composite_sword = Item(
    name="Composite Sword",
    description="Forged from many different types of blades",
    damage=35,
    value=1000,
    enchantable=enchantments.all_weapon_enchantments,
    recipe=[iron, iron, iron, iron, iron, iron,
            gemstone,
            fabric]
)

fishing_rod = Item(
    name="Fishing Rod",
    description="Needed to fish",
    damage=5,
    value=500,
)

all_items = [stone, rope, page, book, rock, iron, gemstone, health_pot, enchanting_setup, fishing_rod, rusted_sword,
             sword_regular, composite_sword, wooly_set, chainmail, plated]
all_weapons = [rusted_sword, sword_regular, composite_sword]
all_armor = [wooly_set, chainmail, plated]

# endregion
