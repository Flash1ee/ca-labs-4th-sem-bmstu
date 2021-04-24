from __future__ import annotations
import matplotlib.pyplot as plt
from utils import Point


def plot_show(points: list[Point], approx: list[tuple(int, list[Point])]) -> None:
    x = [p.x for p in points]
    y = [p.y for p in points]

    plt.title("Аппроксимация методом среднеквадратичного приблжения")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.plot(x, y, 'r+', label='data_from_file')

    for a in approx:
        plt.plot([p.x for p in a[1]], [p.y for p in a[1]], label="p=" + str(a[0]))

    plt.legend()
    plt.show()