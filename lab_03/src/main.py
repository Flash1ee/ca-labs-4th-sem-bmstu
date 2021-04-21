from spline import Spline
from polynom import NewtonPolynom
from utils import *

from sys import argv


def main() -> None:
    f = argv[1]
    points = read_points(f)
    print("Table of points\n")
    print_points(points)

    print('\nEntry X for interpolate:\n')
    x = float(input())

    spline_res = Spline(points).solve(x)
    newton_res = NewtonPolynom(points).solve(x)

    print_res(spline_res, newton_res)


if __name__ == "__main__":
    main()
