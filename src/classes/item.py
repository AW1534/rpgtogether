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
                 enchantable=None, magic_power=0, health=0, agility=0, coins_potential=1, essence_potential=1
                 ):

        if enchantable is None:
            enchantable = []
        if recipe is None:
            recipe = []
        self.id = id
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
        self.agility = agility

        self.coins_potential = coins_potential
        self.essence_potential = essence_potential

        if self.enchantment is not None:
            self.health = self.health * self.enchantment.health_mp
            self.damage = self.damage * self.enchantment.dmg_mp
            self.agility = self.agility * self.enchantment.agility_mp
            self.coins_potential = self.coins_potential
            self.essence_potential = self.essence_potential

    def __str__(self):
        return self.name


class Armor(Item):
    health = 0
    agility = 0

    def __init__(self, id, name, damage, value, health, agility=-5, rarity=0, description="", recipe=None, enchantable=None
                 ):
        super().__init__(id=id, name=name, damage=damage, value=value, rarity=rarity, description=description
                         , recipe=recipe, enchantable=enchantable
                         )
        if enchantable is None:
            enchantable = []
        if recipe is None:
            recipe = []
        self.health = health
        self.agility = agility

        if self.enchantment is not None:
            self.health = self.health * self.enchantment.health_mp
            self.damage = self.damage * self.enchantment.dmg_mp
            self.agility = self.agility * self.enchantment.agility_mp
            self.coins_potential = self.coins_potential
            self.essence_potential = self.essence_potential
