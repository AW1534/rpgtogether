class Item:
    name = ""
    damage = 0
    value = 0
    description = ""
    recipe = 0
    rarity = []
    enchantment = None
    enchantable = []
    magic_power = 0
    health = 0

    def __init__(self, id, name, value, damage=0, rarity=0, description="", recipe=None, enchantment=None,
                 enchantable=None, magic_power=0, health=0
                 ):
        if enchantable is None:
            enchantable = []
        if recipe is None:
            recipe = []
        self.name = name
        self.damage = damage
        self.value = value
        self.rarity = rarity
        self.recipe = recipe
        self.description = description
        self.enchantment = enchantment
        self.enchantable = enchantable
        self.magic_power = magic_power
        self.health = health

    def __str__(self):
        return self.name


class Armor(Item):
    health = 0
    agility = 0

    def __init__(self, id, name, damage, value, health, agility=-5, rarity=0, description="", recipe=None, enchantable=None
                 ):
        super().__init__(id, name, damage, value, rarity, description, recipe, enchantable)
        if enchantable is None:
            enchantable = []
        if recipe is None:
            recipe = []
        self.health = health
        self.agility = agility
