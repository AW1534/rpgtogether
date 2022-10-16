class Enchantment:
    id = 0

    name = ""
    description = ""
    rarity = 0
    special = False
    info = ""

    agility = 0
    agility_mp = 1

    health = 0
    health_mp = 1

    dmg = 0
    dmg_mp = 1

    nuelis_mp = 1
    essence_mp = 1

    def __init__(
            self, id, name, value, rarity=0, description="", special=False,
            info="",
            agility=0, agility_mp=1,
            health=0, health_mp=1,
            dmg=0, dmg_mp=1,
            nuelis_mp=1, essence_mp=1
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

        self.nuelis_mp = nuelis_mp
        self.essence_mp = essence_mp


class Weapon(Enchantment):
    def __init__(self, id, name, value, rarity=0, description="", special=False,
                 info="",
                 agility=0, agility_mp=1,
                 health=0, health_mp=1,
                 dmg=0, dmg_mp=1,
                 nuelis_mp=1, essence_mp=1
                 ):
        super().__init__(id=id, name=name, value=value, rarity=rarity, description=description, special=special,
                         info=info,
                         nuelis_mp=nuelis_mp, essence_mp=essence_mp,
                         agility=agility, agility_mp=agility_mp,
                         health=health, health_mp=health_mp,
                         dmg=dmg, dmg_mp=dmg_mp
                         )


class Armour(Enchantment):
    def init(self, id, name, value, rarity=0, description="", special=False,
             info="",
             agility=0, agility_mp=1,
             health=0, health_mp=1,
             dmg=0, dmg_mp=1
             ):
        super().__init__(id=id, name=name, value=value, rarity=rarity, description=description, special=special,
                         info=info,
                         agility=agility, agility_mp=agility_mp,
                         health=health, health_mp=health_mp,
                         dmg=dmg, dmg_mp=dmg_mp
                         )
