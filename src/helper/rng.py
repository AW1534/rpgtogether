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

    def gen(self, player):
        loses_hp = 0

        for team in self.teams:
            player_total = 0
            enemy_total = 0
            cnt = 0

            for entity in team:
                cnt += 1
                power = 0

                if entity.hostile:
                    power += entity.damage * 3
                    power += entity.agility
                    power += entity.health
                    enemy_total += power
                else:
                    power += random.randint(-10, 30)

            player_total += player.damage * 3
            player_total += player.agility
            player_total += player.health
            player_total += random.randint(-20, 20)

            enemy_total += random.randint(-20, 20)

            loses_hp += player_total - enemy_total

            if loses_hp >= 0:
                loses_hp = 0

        player.health -= loses_hp
        return loses_hp
