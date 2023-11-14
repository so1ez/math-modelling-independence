"""unit tests main file"""

from src.settings import SETTINGS
from src.utils import (
    RouletteSumilation,
    RouletteVisualization,
    BombardmentSimulation,
    BombardmentVisualization
)


class TestClass:
    """class with test methods"""

    bomb_results = None
    path = "src/data/roulette_results.txt"


    def test_roulette_sim(self):
        """test attributes and methods of roulette simulation class"""

        SETTINGS.path = TestClass.path
        rs = RouletteSumilation(SETTINGS.path)

        assert len(rs.colors) == 3, "В словаре colors неверное число ключей"
        assert list(rs.colors) == ["black", "red", "green"], \
            "В словаре colors неверные ключи"
        assert len(rs.results_map) == 3, "В словаре results_map неверное число ключей"
        assert list(rs.results_map) == ["black", "red", "green"], \
            "В словаре results_map неверные значения"
        assert list(rs.results_map.values()) == [0, 0, 0], \
            "В словаре results_map не нулевые значения результатов"
        assert isinstance(rs.path, str) is True, "Тип переменной пути до файла неверный"
        assert "conduct_experiments" in dir(rs), \
            "В классе не имплементирована функция проведения моделирования"

        rs.conduct_experiments()
        with open(SETTINGS.path, "r", encoding="utf-8") as file:
            assert len(file.readlines()) == 10_000, "Файл с результатами имеет не 10_000 строк"


    def test_roulette_visual(self):
        """test attributes and methods of roulette visualization class"""

        SETTINGS.path = TestClass.path
        rv = RouletteVisualization(SETTINGS.path)
        assert isinstance(rv.path, str) is True, "Тип переменной пути до файла неверный"
        assert list(rv.results) == ["same", "different", "green_1", "green_10", "green_11"], \
            "В словаре results неверные ключи"
        assert list(rv.results.values()) == [0, 0, 0, 0, 0], "В словаре results не нулевые значения"
        assert "parse_data" in dir(rv), "В классе не имплементирована функция парсинга данных"

        rv.parse_data()
        print(f"results: {rv.results.values()}")
        assert rv.results["same"] + rv.results["different"] == 10_000, \
            "Количество всех экспериментов неверное"


    def test_bombardment_sim(self):
        """test attributes and methods of bombardment simulation class"""

        bs = BombardmentSimulation()
        assert bs.first_point is None, "Первая точка не None"
        assert len(bs.results_map) == 0, "Словарь results_map изначально не пуст"
        assert "conduct_experiments" in dir(bs), \
            "В классе не имплементирована функция проведения моделирования"

        TestClass.bomb_results = bs.conduct_experiments()
        assert sum(TestClass.bomb_results.values()) == 10_000_000, \
            "Количество проведенных экспериментов не 10_000_000"
        print(f"max: {max(TestClass.bomb_results.values())}")
        print(f"min: {min(TestClass.bomb_results.values())}")
        assert max(TestClass.bomb_results.values()) - min(TestClass.bomb_results.values()) < 700, \
            "Хьюстон, мы сломали мат статистику. Слишком большой разброс результатов"


    def test_bombardment_visual(self):
        """test attributes and methods of bombardment visualization class"""

        bv = BombardmentVisualization(TestClass.bomb_results)
        assert TestClass.bomb_results == bv.results, \
            "Данные, переданные в класс визуализации, переданы неверно"
        assert "show" in dir(bv), "В классе не имплементирована функция отображения"
