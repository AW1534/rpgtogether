import src.helper.list
import entity
from src.objects import items
from src.classes.item import Armor
from src.classes.item import Item

armour_inventory = []
weapon_inventory = []
armour = items.all_armour
weapon = items.all_weapons


class Player(entity):
    base_max_health = 100
    max_health = 100
    base_dmg = 5
    dmg = 5
    base_agility = 10
    agility = 10

    def __init__(self, name, base_max_health=100, max_health=100, base_dmg=5, dmg=5, base_agility=10,
                 agility=10, armour_slot=None, weapon_slot=None, inventory=None):

        self.name = name
        # base stats
        if weapon_slot is None:
            weapon_slot = []
        if armour_slot is None:
            armour_slot = []
        if inventory is None:
            inventory = []

        self.base_max_health = base_max_health
        self.max_health = max_health

        self.base_dmg = base_dmg
        self.dmg = dmg

        self.base_agility = base_agility
        self.agility = agility

        self.armour_slot = armour_slot
        self.weapon_slot = weapon_slot
        self.inventory = inventory

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

    def equip(self):
        for i in self.inventory:
            if i in armour:
                armour_inventory.append(i)
                for itera in armour_inventory:
                    print(itera)
                    a_choice = input("Choose an armour piece to equip")
                    if a_choice == itera.name:
                        print(f"Equipped {a_choice}")
                        self.armour_slot.append(a_choice)
                        if self.armour_slot > 1:
                            self.armour_slot.pop(0)
                            if self.armour_slot is True:
                                self.max_health = self.base_max_health + Armor.health(a_choice)
                    else:
                        print("Invalid Selection")

    def unequip(self):
        self.armour_slot.pop(0)
        print(f"Unequipped {self.armour_slot.name[0]}")

    def hold(self):
        for i in self.inventory:
            if i in weapon:
                weapon_inventory.append(i)
                for itera in weapon_inventory:
                    print(itera)
                    w_choice = input("Choose a weapon to equip")
                    if w_choice == itera.name:
                        print(f"Equipped {w_choice}")
                        self.weapon_slot.append(w_choice)
                        if self.weapon_slot > 1:
                            self.weapon_slot.pop(0)
                            if self.weapon_slot is True:
                                self.dmg = self.base_dmg + Item.damage(w_choice)

    def drop(self):
        self.weapon_slot.pop(0)
        print(f"Unequipped {self.weapon_slot.name(0)}")
