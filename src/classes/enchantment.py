class Enchantment:
    id = 0

    name = ""
    description = ""
    rarity = 0
    special = False
    info = ""

    agility = 0
    agility_mp = 0

    health = 0
    health_mp = 0

    dmg = 0
    dmg_mp = 0

    coins_mp = 0

    def __init__(
            self, id, name, value, rarity=0, description="", special=False, info="", agility=0, agility_mp=0, health=0,
            health_mp=0, dmg=0, dmg_mp=0, coins_mp=0
    ):
        self.id = id
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

        self.coins_mp = coins_mp


class Weapon(Enchantment):
    def __init__(self, id, name, value, rarity=0, description="", special=False, info="", agility=0, agility_mp=0, health=0,
             health_mp=0, dmg=0, dmg_mp=0, coins_mp=0):
        super().__init__(id, name, value, rarity=0, description="", special=False, info="", coins_mp=0, agility=0,
                         agility_mp=0, health=0, health_mp=0, dmg=0, dmg_mp=0)


class Armour(Enchantment):
    def init(self, id, name, value, rarity=0, description="", special=False, info="", agility=0, agility_mp=0, health=0,
             health_mp=0, dmg=0, dmg_mp=0):
        super().__init__(id, name, value, rarity=0, description="", special=False, info="", agility=0, agility_mp=0,
                         health=0, health_mp=0, dmg=0, dmg_mp=0)
