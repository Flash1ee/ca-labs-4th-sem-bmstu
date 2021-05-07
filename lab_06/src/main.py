from typing import List, Tuple
from differ import Differ

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

    h = 1.0

    Differ.print_init("X              :", x)
    Differ.print_init("Y              :", y)
    Differ.print_res("Onesided       :", Differ.left(y, h))
    Differ.print_res("Center         :",
                             Differ.center(y, h))
    Differ.print_res("Second Range   :",
                             Differ.second_runge(y, h, 1))
    Differ.print_res("Aligned params :",
                             Differ.aligned_coeffs(x, y))
    Differ.print_res("Second oneSided:",
                             Differ.second_left(y, h))


if __name__ == '__main__':
    main()
