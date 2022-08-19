from src.classes.enchantment import Enchantment, Weapon, Armour

# region weapon
sharp = Weapon(
    name="Sharpened",
    description="Sharpened and shiny",
    rarity=100,
    special=False,
    value=500
)

reforged = Weapon(
    name="Reforged",
    description="Been through the smithy once again",
    rarity=80,
    special=False,
    value=650
)

burning = Weapon(
    name="Burning",
    description="Hasn't cooled down yet eh?",
    rarity=50,
    special=False,
    value=900
)

lethal = Weapon(
    name="Lethal",
    description="Sharpened to the brim",
    rarity="15",
    special=False,
    value=1500
)

mythical = Weapon(
    name="Mythical",
    description="Bestowed with the power of a mythical stone",
    rarity="3",
    special=True,
    value=2100,
    info="Extra damage to bosses"
)

clover = Weapon(
    name="Clover",
    description="Who knows what this can do",
    rarity="3",
    special=True,
    value=2100,
    info="Increased coins multiplier during scavenge"
)
# endregion

# region armour

durable = Armour(
    name="Durable",
    description="Extra strong and extra hard",
    rarity=200,
    special=False,
    value=500
)

hardened = Armour(
    name="Hardened",
    description="Hard as a rock, but unfortunately rocks aren't the best at moving",
    rarity=160,
    special=False,
    value=500,
    agility=-3
)

crystalized = Armour(
    name="Crystalized",
    description="Infested with crystals, maybe it makes the armour stronger?",
    rarity=100,
    special=False,
    value=900
)

nokia = Armour(
    name="NOKIA-3310 PLATING",
    description="Strongest plating of them all, unbreakable",
    rarity=1,
    special=False,
    value=5000,
    info="Adds 2000 defense"
)

synergy = Armour(
    name="Synergization",
    description="The stronger i get, the higher my health gets. cool.",
    rarity=10,
    special=True,
    value=2100,
    info="50% of your damage is added as health."
)

one_for_all = Armour(
    name="One FOR ALL",
    description="A worthy sacrifice",
    rarity=5,
    special=True,
    value=3000,
    agility_mp=-6,
    health_mp=0.7,
    dmg_mp=0.5
)

all_enchantments = [sharp, reforged, burning, lethal, mythical, clover, durable, hardened, crystalized, nokia, synergy, one_for_all]
all_weapon_enchantments = [sharp, reforged, burning, lethal, mythical, clover]
all_armor_enchantments = [durable, hardened, crystalized, nokia, synergy, one_for_all]