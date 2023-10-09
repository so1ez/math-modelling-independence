import matplotlib.pyplot as plt
import numpy as np

from src.settings import SETTINGS
from src.coin_flipper import CoinFlipper


def main() -> None:
    

    n = int(input("Введите количество повторений броска монеты: "))
    assert n > 0, "Введенное число меньше нуля"
    print(f"Введенное число n = {n}")
    SETTINGS.repeats = n
    
    cf = CoinFlipper()
    cf.coin_flip()
    
    # make bar
    x = ["heads", "tails"]
    y = [cf.results_map["tails"], cf.results_map["heads"]]
    fig, ax = plt.subplots()
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    ax.set(xlim=(0, 1), xticks=np.arange(-1, 3),
           ylim=(0, 100), yticks=np.linspace(0, 600, 13))
    plt.show()

    print("-----------------------------")

if __name__ == "__main__":
    main()
