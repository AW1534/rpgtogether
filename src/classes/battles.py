from src.helper import rng


class Battle():
    def __init__(self, player, waves=None):
        if waves is None:
            waves = []
        self.player = player
        self.waves = waves

    wave = 0

    def next_wave(self):
        self.wave += 1
        for entities in self.waves[self.wave]:  # for each entity in the wave
            rng.Fight(
                teams=[
                    [self.player],
                    entities]
            )

