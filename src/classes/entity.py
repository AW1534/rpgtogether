class Entity:
    name = ""
    damage = 0
    base_max_health = 0
    max_health = 0
    base_dmg = 0
    health = 0
    rarity = 0
    hostile = False
    description = ""
    agility = 0
    nuelis = 0
    inventory = None,
    armor = None
    weapon = None
    base_agility = 0


    def __init__(self, name=0, damage=0, health=0, rarity=0, hostile=False, description="", agility=0, nuelis=0, inventory=None,
                 armor=None, weapon=None, base_max_health=0, max_health=0, base_damage=0, base_agility=0):

        if inventory == None:
            inventory = []

        self.health = health
        self.base_max_health = base_max_health
        self.max_health = max_health

        self.base_damage = base_damage
        self.damage = damage

        self.base_agility = base_agility
        self.agility = agility

        self.armour = armor
        self.weapon = weapon
        self.inventory = inventory
