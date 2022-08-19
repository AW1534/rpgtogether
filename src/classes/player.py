import src.helper.list


class Player:
    def __init__(self, name):
        self.name = name
        self.rupees = 50

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

    def trade(self, loses: list = None, gains: list = None, loses_rupees=None, gains_rupees=None):
        if gains is None:
            gains = []
        if loses is None:
            loses = []
        if loses_rupees is None:
            loses_rupees = 0
        if gains_rupees is None:
            gains_rupees = 0

        if src.helper.list.contains_items(self.inventory, loses) and self.rupees >= loses_rupees:
            for item in loses:
                try:
                    self.inventory.remove(item)
                except ValueError:
                    pass
            self.rupees -= loses_rupees

            self.inventory += gains
            self.rupees += gains_rupees
            return True
        else:
            return False
