from src.classes.enchantment import Enchantment


class Blessing(Enchantment):
    def __init__(self, id, name, value,
                 description, info, rarity=0,
                 health_mp=1, dmg_mp=1, agility_mp=1, nuelis_mp=1, essence_mp=1,
                 special=False
                 ):

        super().__init__(id=id, name=name, value=value,
                         description=description, info=info, rarity=rarity,
                         health_mp=health_mp, dmg_mp=dmg_mp, agility_mp=agility_mp, nuelis_mp=nuelis_mp, essence_mp=essence_mp,
                         special=special
                         )
