from __future__ import annotations
from sys import argv

from utils import *
from rms_approx import *
from graphics import *

def cmp(points: list[Point], points_sec: list[Point], n:list[int]) -> None:
    approxs = []

    for deg in n:
        slau = SLAU().build(points, deg)

        print("\nSLAU to solve\n")
        print_matrix(slau.mat)

        slau = slau.solve()

        print("\nSolved SLAE\n")
        print_matrix(slau)
        print()

        approxs.append((deg, Approximator().get_coeffs(slau).build(points)))
    for deg in n:
        slau = SLAU().build(points_sec, deg)

        print("\nSLAU to solve\n")
        print_matrix(slau.mat)

        slau = slau.solve()

        print("\nSolved SLAE\n")
        print_matrix(slau)
        print()

        approxs.append((deg, Approximator().get_coeffs(slau).build(points_sec)))


    plot_show(points, approxs)

def main():
    f = argv[1]
    points = read_points(f)

    print("Source table:")
    print_points(points)

    if len(argv) > 2 and argv[2] == 'test':
        n = [i for i in range(0, 9, 2)]
        n[0] = 1
    else:
        print("Entry degree of polynom")
        n = [*map(int, input().split())]
        if len(argv) == 4 and argv[3] == 'cmp':
            points_cmp = read_points(argv[2])
            cmp(points, points_cmp, n)

    approxs = []
    for deg in n:
        slau = SLAU().build(points, deg)

        print("\nSLAU to solve\n")
        print_matrix(slau.mat)

        slau = slau.solve()

        print("\nSolved SLAE\n")
        print_matrix(slau)
        print()

        approxs.append((deg, Approximator().get_coeffs(slau).build(points)))

    plot_show(points, approxs)

if __name__ == '__main__':
    main()
