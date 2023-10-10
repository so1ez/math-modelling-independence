from utils import ResultVisualization


def main() -> None:
    rv = ResultVisualization("src/data/results.txt")
    rv.parse_data()
    print(f"Experiments results: {rv.results}")
    rv.show()


if __name__ == "__main__":
    main()
