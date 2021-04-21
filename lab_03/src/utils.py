from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, _x: float, _y: float) -> None:
        self.x = _x
        self.y = _y

    def __lt__(self, other: Point):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    def __str__(self):
        return "{:^8.3f} {:^8.3f}".format(self.x, self.y)


def read_points(fname: str) -> list[Point]:
    points = []

    with open(fname, 'r') as f:
        for line in f.readlines():
            point = Point(*list(map(float, line.split()[:2])))
            points.append(point)

    return points


def print_points(points: list[Point]) -> None:
    print("{:^8} {:^8}".format('X', 'Y'))
    for p in points:
        print(p)

def print_res(spline: Point, newton: Point) -> None:
    print(f"Spline result is {spline}")
    print(f"Newton result is {newton}")