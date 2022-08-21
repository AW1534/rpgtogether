class Entity:
    name = ""
    damage = 0
    hp = 0
    description = ""
    hostile = False
    chance = 0
    agility = 0
    nuelis = 0
    inventory = []

    def __init__(self, name, damage, hp, rarity, hostile=False, description="", agility=0, nuelis = 0, inventory = []):
        self.name = name
        self.damage = damage
        self.hp = hp
        self.description = description
        self.hostile = hostile
        self.rarity = rarity
        self.agility = agility
        self.nuelis = nuelis
        self.inventory = inventory
