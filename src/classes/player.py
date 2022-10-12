from src.helper import list, formatting
from src.classes import entity


class Player(entity.Entity):
    def __init__(self, name="", damage=0, rarity=0, hostile=False, description="", agility=10, nuelis=0, inventory=None,
                 armor=None, weapon=None, base_max_health=100, max_health=1000, health=100, base_damage=0,
                 base_agility=10):

        super().__init__(name=name, damage=damage, rarity=rarity, hostile=hostile, description=description, agility=agility, nuelis=nuelis,
                         inventory=inventory,
                         armor=armor, weapon=weapon, base_max_health=base_max_health, max_health=max_health, health=health, base_damage=base_damage,
                         base_agility=base_agility)

    def trade(self, loses: list = None, gains: list = None, loses_nuelis=None, gains_nuelis=None):
        if gains is None:
            gains = []
        if loses is None:
            loses = []
        if loses_nuelis is None:
            loses_nuelis = 0
        if gains_nuelis is None:
            gains_nuelis = 0

        if self.nuelis is None:
            self.nuelis = 0

        if list.contains_items(self.inventory, loses) and self.nuelis >= loses_nuelis:
            for item in loses:
                try:
                    self.inventory.remove(item)
                except ValueError:
                    pass
            self.nuelis -= loses_nuelis

            self.inventory += gains
            self.nuelis += gains_nuelis
            return True
        else:
            return False

    def death(self):
        self.inventory = []
        formatting.add_border("you died", "you lost all items in your inventory")
