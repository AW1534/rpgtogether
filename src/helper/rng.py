import random
from src.classes import item


class Roulette:
    def __init__(self, choices, nothing_chance=0):
        self.choices = []
        for choice in choices:
            for i in range(item.Item.rarity(choice)):
                self.choices.append(choice)
        for i in range(nothing_chance):
            self.choices.append(None)

    def gen(self):
        return random.choice(self.choices)


class Fight:
    def __init__(self, teams: list):
        self.teams = teams

    def gen(self):
        team_avgs = {

        }

        for team in self.teams:
            total = 0
            cnt = 0
            for entity in team:
                cnt += 1
                pow = 0
                if entity.hostile:
                    pow += entity.damage * 2
                    pow += entity.agility
                    pow += entity.health
                pow += random.randint(-40, 40)

            team_avgs[team] = total

        return max(team_avgs, key=team_avgs.get)
