"""Utils for math modelling"""

from time import time
from random import randrange
from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import numpy as np


def timer(func):
    """Decorator to track func execution time"""

    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} started working...")
        t1 = time()
        res = func(*args, **kwargs)
        print(f"Function executes {time() - t1} seconds")

        return res
    return wrapper


class Simulation(ABC):
    """Class for experiments simulations"""

    results_map: dict


    @abstractmethod
    def conduct_experiments(self) -> None:
        """Make data for math modelling"""


class ResultVisualization(ABC):
    """Abstract class for parse and visualization data with matplotlib"""

    results: dict

    @abstractmethod
    def show(self) -> None:
        """Show data with matplotlib"""


class RouletteSumilation(Simulation):
    """Roulette math modelling class"""

    path: str
    colors: dict

    def __init__(self, path: str) -> None:
        self.path = path
        self.results_map = {"black": 0, "red": 0, "green": 0}
        self.colors = {"black": {i for i in range(1, 19)},
                       "red": {i for i in range(19, 37)},
                       "green": {37}}

        # clear file
        with open(self.path, 'w', encoding="utf-8") as file:
            file.close()


    @timer
    def conduct_experiments(self) -> None:
        found = 0
        while found < 10000:
            i, prev_spin = 0, None
            while i < 10:

                rand = randrange(1, 38)
                i += 1

                for key, value in self.colors.items():
                    if rand in value:
                        cur_spin = key

                self.results_map[cur_spin] = self.results_map[cur_spin] + 1

                if prev_spin is None:
                    prev_spin = cur_spin
                elif prev_spin != cur_spin:
                    break

            else:
                rand = randrange(1, 38)
                for key, value in self.colors.items():
                    if rand in value:
                        following = key

                self.results_map[following] = self.results_map[following] + 1

                self.save_result(cur_spin, following)
                found += 1


    def save_result(self, ten: str, following: str):
        """Save line in file storing the data"""

        with open(self.path, "a", encoding="utf-8") as file:
            file.write(f"{ten[0]},{following[0]}\n")


class RouletteVisualization(ResultVisualization):
    """Results visualization of roulette math modeling"""

    path: str


    def __init__(self, path: str) -> None:
        self.path = path
        self.results = {"same": 0, "different": 0, "green_1": 0, "green_10": 0, "green_11": 0}


    @timer
    def parse_data(self) -> None:
        """Parse results file for get and save in dict experiments data"""

        with open(self.path, 'r', encoding="utf-8") as file:
            for line in file:
                splited = line.rstrip("\n").split(",")
                if splited[0] == splited[1]:
                    self.results["same"] = self.results["same"] + 1
                else:
                    self.results["different"] = self.results["different"] + 1

                if splited[0] != "g" and splited[1] == "g" :
                    self.results["green_1"] = self.results["green_1"] + 1
                elif splited[0] == "g" and splited[1] != "g":
                    self.results["green_10"] = self.results["green_10"] + 1
                elif splited[0] == "g" and splited[1] == "g":
                    self.results["green_11"] = self.results["green_11"] + 1


    def show(self) -> None:
        """Show visualization of roulette math modelling"""

        print(self.results)
        x = ["same", "different", "green_1", "green_10", "green_11"]
        y = [self.results["same"] - self.results["green_11"],
             self.results["different"] - self.results["green_1"] - self.results["green_10"],
             self.results["green_1"], self.results["green_10"], self.results["green_11"]]
        _, ax = plt.subplots()
        ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
        ax.set(xlim=(0, 1), xticks=np.arange(-1, 6),
               ylim=(0, 100), yticks=np.linspace(0, 7000, 15))
        plt.show()


class BombardmentSimulation(Simulation):
    """Bombardment math modelling class"""

    first_point = None


    def __init__(self) -> None:
        self.results_map = {}


    @timer
    def conduct_experiments(self) -> None:
        found = 0
        while found < 10_000_000:
            x_rand, y_rand = randrange(1, 101), randrange(1, 101)
            point = (x_rand, y_rand)
            if self.first_point is None:
                self.first_point = point

            if point not in self.results_map:
                self.results_map[point] = 1
            else:
                self.results_map[point] = self.results_map[point] + 1

            found += 1

        print(f"first hit is: {self.first_point}")
        print(f"first point hits: {self.results_map[self.first_point]}")

        return self.results_map


class BombardmentVisualization(ResultVisualization):
    """Results visualization of bombardment math modelling"""


    def __init__(self, results: dict) -> None:
        self.results = results


    @timer
    def show(self) -> None:
        """Show visualization of bombardment math modelling"""

        x, y = [], []
        for key, value in self.results.items():
            x += [key[0]] * value
            y += [key[1]] * value

        plt.hist2d(x, y, bins=100)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Bombardment frequencies')
        plt.colorbar()
        plt.show()
