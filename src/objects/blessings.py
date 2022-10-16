from src.classes.blessing import Blessing


gigantism = Blessing(
    id=800,
    name="Gigantism",
    value=50,
    description="Did I just gain a few inches?",
    info="Gains 200% Health",
    rarity=50,
    health_mp=2,
    special=False
)

strengthen = Blessing(
    id=801,
    name="Strengthen",
    value=50,
    description="Weights? What's that?",
    info="Gains 200% Damage",
    rarity=50,
    dmg_mp=2,
    special=False
)

swiftness = Blessing(
    id=802,
    name="Swiftness",
    value=150,
    description="One with the wind",
    info="1000% Faster",
    rarity=25,
    agility_mp=10,
    special=False
)

duplication = Blessing(
    id=810,
    name="Duplication",
    value=500,
    description="Wait... UNLIMITED DINO NUGGIES?",
    info="125% more nuelis and more essence",
    rarity=5,
    nuelis_mp=1.5,
    essence_mp=1.5,
    special=True
)

all_blessings = [gigantism, strengthen, swiftness, duplication]
blessings = [gigantism, strengthen, swiftness]
special = [duplication]
