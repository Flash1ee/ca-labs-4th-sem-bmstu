from __future__ import annotations
import numpy as np

from utils import Point


class NewtonPolynom:
    x_list: list[float]
    y_list: list[float]

    def __init__(self, points: list[Point]):
        self.x_list = [p.x for p in points]
        self.y_list = [p.y for p in points]

    def solve(self, x: float) -> Point:
        a = self.make_diff_table()
        n = len(self.x_list) - 1  # Degree of polynomial
        p = a[n]

        for k in range(1, n + 1):
            p = a[n - k] + (x - self.x_list[n - k]) * p

        return Point(x, p)

    def make_diff_table(self) -> np.ndarray[float]:
        m = len(self.x_list)

        x = np.copy(self.x_list)
        a = np.copy(self.y_list)
        for k in range(1, m):
            a[k:m] = (a[k:m] - a[k - 1]) / (x[k:m] - x[k - 1])

        return a
