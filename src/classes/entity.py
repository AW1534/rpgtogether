class Entity:
    name = ""
    description = ""

    base_dmg = 0
    damage = 0

    base_max_health = 0
    max_health = 0
    health = 0

    base_agility = 0
    agility = 0

    rarity = 0
    hostile = False

    nuelis = 0
    inventory = None

    armor = None
    weapon = None

    full_power = 0

    def __init__(self, name=0, damage=0, health=0, rarity=0, hostile=False, description="", agility=0, nuelis=0,
                 inventory=None, armor=None, weapon=None, base_max_health=0, max_health=0, base_damage=0, base_agility=0
                 , full_power=0):

        if inventory is None:
            inventory = []

        self.name = name

        self.health = health
        self.base_max_health = base_max_health
        self.max_health = max_health
        self.full_power = full_power
        self.nuelis = nuelis

        self.rarity = rarity
        self.hostile = hostile
        self.description = description

        self.base_damage = base_damage
        self.damage = damage

        self.base_agility = base_agility
        self.agility = agility

        self.armour = armor
        self.weapon = weapon
        self.inventory = inventory

    @staticmethod
    def get_full_power(entity):
        full_power = entity.health + (entity.damage * 2) + (entity.agility * 0.5)
        if entity.hostile is False:
            full_power /= 4
            return full_power
