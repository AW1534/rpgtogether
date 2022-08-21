import src.helper.list
import entity

class Player(entity.i.ity):
    def __init__(self, name):

        # base stats
        self.base_max_health = 100
        self.base_dmg = 5
        self.base_agility = 10

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
