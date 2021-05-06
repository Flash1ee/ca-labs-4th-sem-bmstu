from typing import List, Tuple


filename = "../data/data.txt"


def read_data(filename: str) -> Tuple[List[float], List[float]]:
    x, y = [], []
    with open(filename) as f:
        for line in f:
            x_t, y_t = list(map(float, line.split()[:2]))
            x.append(x_t)
            y.append(y_t)
    return x, y


def main() -> None:
    x, y = read_data(filename)



if __name__ == '__main__':
    main()
