from src.classes.enchantment import Enchantment


class Blessing(Enchantment):
    def __init__(self, id, name, value,
                 description, info, rarity,
                 health_mp, dmg_mp, agility_mp, coins_mp,
                 special
                 ):

        super().__init__(id=id, name=name, value=value,
                         description=description, info=info, rarity=rarity,
                         health_mp=health_mp, dmg_mp=dmg_mp, agility_mp=agility_mp, coins_mp=coins_mp,
                         special=special
                         )
