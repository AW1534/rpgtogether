import src.helper.list


class Player:
    def __init__(self, name):
        self.name = name
        self.nuelis = 50

        self.max_hunger = 0

        # base stats
        self.base_max_health = 100
        self.base_dmg = 5
        self.base_agility = 10

        # stats
        self.health = self.base_max_health
        self.damage = self.base_dmg
        self.agility = self.base_agility

        self.inventory = []

    def trade(self, loses: list = None, gains: list = None, loses_nuelis=None, gains_nuelis=None):
        if gains is None:
            gains = []
        if loses is None:
            loses = []
        if loses_nuelis is None:
            loses_nuelis = 0
        if gains_nuelis is None:
            gains_nuelis = 0

        if src.helper.list.contains_items(self.inventory, loses) and self.nuelis >= loses_nuelis:
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
