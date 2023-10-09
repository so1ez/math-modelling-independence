import random

from .decorators import repeat, timer
from .settings import SETTINGS


class CoinFlipper:
    results_map: dict = {}

    def __init__(self):
        self.results_map = {"heads": 0, "tails": 0}

    @timer
    @repeat(SETTINGS.repeats)
    def coin_flip(self) -> None:
        if random.randrange(2):
            self.results_map["tails"] += 1
        else:
            self.results_map["heads"] += 1
