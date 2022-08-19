class Enchantment:
    name = ""
    description = ""
    rarity = 0
    special = True
    info = ""

    agility = 0
    agility_mp = 0

    health = 0
    health_mp = 0

    dmg = 0
    dmg_mp = 0

    def __init__(self, name, value, rarity=0, description="", special=False, info="", agility=0, agility_mp=0, health=0, health_mp=0, dmg=0, dmg_mp=0):
        self.name = name
        self.value = value
        self.rarity = rarity
        self.description = description
        self.special = special
        self.info = info

        self.agility = agility
        self.agility_mp = agility_mp

        self.health = health
        self.health_mp = health_mp

        self.dmg = dmg
        self.dmg_mp = dmg_mp

class Weapon(Enchantment):
    def __init__(self, name, value, rarity=0, description="", special=False, info=""):
        super().__init__(name, value, rarity=0, description="", special=False, info="")

class Armour(Enchantment):
    def init(self, name, value, rarity=0, description="", special=False, info="", agility=0, health=0, dmg=0):
        super().__init__(name, value, rarity=0, description="", special=False, info="", agility=0, health=0, dmg=0)