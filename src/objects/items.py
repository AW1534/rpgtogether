from src.classes.item import Item, Armor
from src.objects import enchantments

stone = Item(
    name="Magical stone",
    description="A mysterious luminescent orb",
    damage=0,
    value=2000,
    rarity=1,
    magic_power = 75
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
    magic_power=5
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
    magic_power=125
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
    value=50
)
enchanting_setup = Item(
    name="Enchanting Setup",
    description="Mysterious set of books which possess vast amounts of knowledge",
    damage=0,
    value=11250
)
# endregion

# region combat


leather_set = Armor(
    name="Leather Set",
    description="Cosy set, but not very durable",
    damage=10,
    value=400,
    health=30,
    enchantable=enchantments.all_armor_enchantments
)
chainmail = Armor(
    name="Chainmail Armor",
    description="Heavy chainmail armor",
    damage=10,
    health=75,
    value=1000,
    agility=-5,
    enchantable=enchantments.all_armor_enchantments
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
    description="A regular sword, made from steel",
    damage=20,
    value=600,
    enchantable=enchantments.all_weapon_enchantments
)

fishing_rod = Item(
    name="Fishing Rod",
    description="Needed to fish",
    damage=5,
    value=500,
)

all_items = [stone, rope, page, book, rock, iron, gemstone, health_pot, enchanting_setup, fishing_rod, rusted_sword, leather_set, sword_regular, chainmail]
all_weapons = [rusted_sword, sword_regular]
all_armor = [leather_set, chainmail]

# endregion
