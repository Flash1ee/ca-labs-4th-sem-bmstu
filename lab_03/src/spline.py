from __future__ import annotations
from utils import Point


class Spline:
    points: list[Point]

    def __init__(self, _points: list[Point]):
        self.points = _points

    def get_pos(self, p: Point):
        i = 1
        while i < len(self.points) and self.points[i].x < p.x:
            i += 1

        return i - 1

    def solve(self, x: float) -> Point:
        list_x = [p.x for p in self.points]
        list_y = [p.y for p in self.points]

        a = list_y[:-1]

        c = [0 for i in range(len(self.points) - 1)]

        # Нач. данные
        ksi_k, tet_k = [0, 0], [0, 0]

        # Сначала делаем прямой проход и вычисляем прогоночные коеффициенты
        for i in range(2, len(self.points)):
            xhi_1, xhi_2 = list_x[i] - list_x[i - 1], list_x[i - 1] - list_x[i - 2]
            yhi_1, yhi_2 = list_y[i] - list_y[i - 1], list_y[i - 1] - list_y[i - 2]

            phi = 3 * (yhi_1 / xhi_1 - yhi_2 / xhi_2)

            ksi_k.append(-xhi_1 / (xhi_2 * ksi_k[i - 1] + 2 * (xhi_2 + xhi_1)))
            tet_k.append((phi - xhi_2 * tet_k[i - 1]) / (xhi_2 * ksi_k[i - 1] + 2 * (xhi_2 + xhi_1)))

        c[len(self.points) - 2] = tet_k[-1]

        # Обратный проход
        for i in range(len(self.points) - 2, 0, -1):
            c[i - 1] = ksi_k[i] * c[i] + tet_k[i]

        b, d = [], []
        for i in range(1, len(self.points) - 1):
            xhi_1 = list_x[i] - list_x[i - 1]
            yhi_1 = list_y[i] - list_y[i - 1]
            b.append(yhi_1 / xhi_1 - (xhi_1 * (c[i] + 2 * c[i - 1])) / 3)
            d.append((c[i] - c[i - 1]) / (3 * xhi_1))

        b.append((list_y[-1] - list_y[-2]) / (list_x[-1] - list_x[-2]) - ((list_x[-1] - list_x[-2]) * 2 * c[-1]) / 3)
        d.append(-c[len(self.points) - 2] / (3 * list_x[-1] - list_x[-2]))
        pos = self.get_pos(Point(x, 0))

        res = a[pos] + \
              b[pos] * (x - self.points[pos].x) + \
              c[pos] * (x - self.points[pos].x) ** 2 + \
              d[pos] * (x - self.points[pos].x) ** 3


        return Point(x, res)