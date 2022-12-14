from src.classes.enchantment import Enchantment, Weapon, Armour

# region weapon
sharp = Weapon(
    name="Sharpened",
    description="Sharpened and shiny",
    rarity=100,
    special=False,
    value=500,
    dmg_mp=1.5
)

reforged = Weapon(
    name="Reforged",
    description="Been through the smithy once again",
    rarity=80,
    special=False,
    value=650,
    dmg_mp=2
)

burning = Weapon(
    name="Burning",
    description="Hasn't cooled down yet eh?",
    rarity=50,
    special=False,
    value=900,
    dmg_mp=3
)

lethal = Weapon(
    name="Lethal",
    description="Sharpened to the brim",
    rarity="15",
    special=False,
    value=1500,
    dmg_mp=4
)

mythical = Weapon(
    name="Mythical",
    description="Bestowed with the power of a mythical stone",
    rarity="3",
    special=True,
    value=2100,
    info="Extra damage to bosses",
    dmg_mp=5
)

clover = Weapon(
    name="Clover",
    description="Who knows what this can do",
    rarity="3",
    special=True,
    value=2100,
    coins_mp=1.5,
    dmg_mp=5,
    info="Increased coins multiplier during scavenge",

)
# endregion

# region armour

durable = Armour(
    name="Durable",
    description="Extra strong and extra hard",
    rarity=200,
    special=False,
    value=500,
    health_mp=1.5
)

hardened = Armour(
    name="Hardened",
    description="Hard as a rock, but unfortunately rocks aren't the best at moving",
    rarity=160,
    special=False,
    value=500,
    agility=-3,
    health_mp=3
)
sturdy = Armour(
    name="Sturdy",
    description="Lacking a bit of shine for me...",
    rarity=130,
    special=False,
    value=650,
    health_mp=3
)
crystalized = Armour(
    name="Crystalized",
    description="Infested with crystals, maybe it makes the armour stronger?",
    rarity=100,
    special=False,
    value=900,
    health_mp=5
)

nokia = Armour(
    name="NOKIA-3310 PLATING",
    description="Strongest plating of them all, unbreakable",
    rarity=1,
    special=False,
    value=20000,
    health_mp=10
)

synergy = Armour(
    name="Synchronization",
    description="The stronger I get, the higher my health gets. cool.",
    rarity=10,
    special=True,
    value=2100,
    info="50% of your damage is added as health.",
    health_mp=5
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

e_synergy = Armour(
    name="Perfected Synergy",
    description="This power.... I'M INVINCIBLEEE",
    rarity=0,
    special=True,
    value=21420,
    health_mp=7.5,
    info="Adds 75% of attack on to your health points"
)

all_enchantments = [sharp, reforged, burning, lethal, mythical, clover, durable, hardened, crystalized, nokia, synergy,
                    one_for_all, e_synergy]
all_weapon_enchantments = [sharp, reforged, burning, lethal, mythical, clover]
all_armor_enchantments = [durable, hardened, crystalized, nokia, synergy, one_for_all, e_synergy]
