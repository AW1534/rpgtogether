from src.helper import list
from src.classes import entity


class Player(entity.Entity):
    def __init__(self, name="", damage=0, rarity=0, hostile=False, description="", agility=0, nuelis=0, inventory=None,
                 armour=None, weapon=None, base_max_health=0, max_health=0, base_damage=0, base_agility=0, player=True):
        self.player = player

        super().__init__(name, damage, rarity, hostile, description, agility, nuelis, inventory,
                         armour, weapon, base_max_health, max_health, base_damage, base_agility)

    def trade(self, loses: list = None, gains: list = None, loses_nuelis=None, gains_nuelis=None):
        if gains is None:
            gains = []
        if loses is None:
            loses = []
        if loses_nuelis is None:
            loses_nuelis = 0
        if gains_nuelis is None:
            gains_nuelis = 0

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




