from __future__ import annotations


class Point:
    x: float
    y: float
    weight: int

    def __init__(self, _x: float, _y: float, _weight: float) -> None:
        self.x = _x
        self.y = _y
        self.weight = _weight

    def __str__(self):
        return "{:^8.3f} {:^8.3f} {:^8.3f}".format(self.x, self.y, self.weight)


def read_points(fname: str) -> list[Point]:
    points = []

    with open(fname, 'r') as f:
        for line in f.readlines():
            point = Point(*list(map(float, line.split()[:3])))
            points.append(point)

    return points

def print_matrix(matrix: list[list[float]]) -> None:
    for row in matrix:
        print(('[' + ' '.join(["{:8.3f}"] * len(row)) + ' ]').format(*row))

def print_points(points: list[Point]) -> None:
    print("{:^8} {:^8} {:^8}".format('X', 'Y', "Weight"))
    for p in points:
        print(p)
