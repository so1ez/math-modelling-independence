from time import time
from random import randrange

import matplotlib.pyplot as plt
import numpy as np


def repeat(n: int):
    def outer(func):
        def wrapper(*args, **kwargs):
            print(f"Start repeating {n} times...")
            for _ in range(n):
                func(*args, **kwargs)
            print("Stop repeating")
            
        return wrapper
    return outer


def timer(func):
    def wrapper(*args, **kwargs):
        print("Function started working...")
        t1 = time()
        func(*args, **kwargs)
        print(f"Function executes {time() - t1} seconds")
    
    return wrapper


class RouletteSumilation:
    results_map: dict = {}
    colors: dict = {}
    

    def __init__(self):
        self.results_map = {"black": 0, "red": 0, "green": 0}
        self.colors = {"black": {i for i in range(1, 19)},
                       "red": {i for i in range(19, 37)},
                       "green": {37}}


    @timer
    def roulette_spin(self) -> None:
        found = 0
        while found < 10000:
            i, prev_spin = 0, None
            while i < 10:

                rand = randrange(1, 38)
                i += 1

                for key in self.colors:
                    if rand in self.colors[key]:
                        cur_spin = key

                self.results_map[cur_spin] = self.results_map[cur_spin] + 1

                if prev_spin is None:
                    prev_spin = cur_spin
                elif prev_spin != cur_spin:
                        break
                
            else:
                rand = randrange(1, 38)
                for key in self.colors:
                    if rand in self.colors[key]:
                        following = key
                self.results_map[following] = self.results_map[following] + 1

                self.save_result(cur_spin, following)
                found += 1
    

    def save_result(self, ten: str, following: str):
        with open("src/data/results.txt", "a") as file:
            file.write(f"{ten[0]},{following[0]}\n")


class ResultVisualization:
    path: str
    results: dict


    def __init__(self, path: str) -> None:
        self.path = path
        self.results = {"same": 0, "different": 0, "green_1": 0, "green_10": 0}


    @timer
    def parse_data(self) -> None:
        """parse results file for get experiments data"""
        with open(self.path, 'r') as file:
            for line in file:
                splited = line.rstrip("\n").split(",")
                if splited[0] == splited[1]:
                    self.results["same"] = self.results["same"] + 1
                else:
                    self.results["different"] = self.results["different"] + 1

                if splited[1] == "g":
                    self.results["green_1"] = self.results["green_1"] + 1
                elif splited[0] == "g":
                    self.results["green_10"] = self.results["green_10"] + 1


    def show(self):
        """show visualization of received data"""
        x = ["same", "different", "green_1", "green_10"]
        y = [self.results["same"], self.results["different"],
             self.results["green_1"], self.results["green_10"]]
        fig, ax = plt.subplots()
        ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
        ax.set(xlim=(0, 1), xticks=np.arange(-1, 5),
            ylim=(0, 100), yticks=np.linspace(0, 7000, 15))
        plt.show()
