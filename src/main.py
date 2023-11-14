"""
Main file for execution
Boytsov V.M.
"""

import os

from settings import SETTINGS
from utils import (
    RouletteSumilation,
    RouletteVisualization,
    BombardmentSimulation,
    BombardmentVisualization
)


def roulette() -> None:
    """Conduct, process and show roulette experiment"""

    # make and save data
    rs = RouletteSumilation(SETTINGS.path)
    rs.conduct_experiments()

    # process data and show results
    rv = RouletteVisualization(SETTINGS.path)
    rv.parse_data()
    rv.show()


def bombardment() -> None:
    """Conduct, process and show bombardment experiment"""

    # make and save data
    bs = BombardmentSimulation()
    results = bs.conduct_experiments()

    # process data and show results
    bv = BombardmentVisualization(results)
    bv.show()


_experiment_map = {
    1: roulette,
    2: bombardment
}


def main() -> None:
    """Main entry-point function"""

    try:
        os.mkdir("src/data")
    except FileExistsError:
        pass

    SETTINGS.path = "src/data/roulette_results.txt"

    choose = None
    while choose not in _experiment_map:
        try:
            choose = int(
                input("1 - Roulette, 2 - Bombardment.\nChoose experiment type: "))
        except ValueError:
            print("Please, write 1 or 2!")

    _experiment_map[choose]()


if __name__ == "__main__":
    main()
