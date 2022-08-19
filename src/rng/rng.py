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
