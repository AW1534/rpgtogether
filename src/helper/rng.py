import random


class Roulette:
    def __init__(self, choices, nothing_chance=0):
        self.choices = []
        for choice in choices:
            for i in range(choice.rarity):
                self.choices.append(choice)
        for i in range(nothing_chance):
            self.choices.append(None)

    def gen(self):
        return random.choice(self.choices)


class Fight:
    def __init__(self, teams: list):
        self.teams = teams

    def gen(self):
        loses_hp = 0
        for team in self.teams:
            total = 0
            cnt = 0

            for entity in team:
                cnt += 1
                pow = 0

                if entity.hostile:
                    pow += entity.damage * 3
                    pow += entity.agility
                    pow += entity.health
                    total += pow
                else:
                    pow += random.randint(-10, 30)

            total += random.randint(-40, 40)

            loses_hp += total / 10

        return loses_hp
