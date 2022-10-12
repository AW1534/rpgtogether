from src.helper import rng
from src.classes.player import Player


class Battle_wave:
    def __init__(self, player, waves=None):
        if waves is None:
            waves = []
        self.player = player
        self.waves = waves

    wave = 0

    def next_wave(self):
        total_lose = 0
        self.wave += 1
        for entities in self.waves[self.wave]:  # for each entity in the wave
            lose = rng.Fight(
                teams=[
                    [self.player],
                    entities]
            )
            total_lose += lose
        Player.health -= total_lose

