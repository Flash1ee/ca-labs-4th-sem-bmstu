from math import cos, sin, exp, pi
from scipy.special import roots_legendre
from typing import Callable as Call, List


class Integral:
    def __init__(self, lm: List[List[float]], n: List[int], fn: List[int]):
        self.lm = lm
        self.n = n
        self.func_one = Integral.simpson if (fn[0]) else Integral.gauss
        self.func_two = Integral.simpson if (fn[1]) else Integral.gauss

    def __call__(self, p: float) -> float:
        f = Integral.__integrated(p)

        inner = lambda x: self.func_two(lambda val_one: f(x, val_one), self.lm[1][0], self.lm[1][1], self.n[1])
        integ = lambda: self.func_one(inner, self.lm[0][0], self.lm[0][1], self.n[0])

        return integ()

    @staticmethod
    def simpson(f: Call[[float], float], a: float, b: float, n: int) -> float:
        if n < 3 or not n % 2 == 0:
            raise Exception("Wrong value n")

        h = (b - a) / (n - 1.0)
        x = a
        res = 0.0
        for i in range((n - 1) // 2):
            res += f(x) + 4 * f(x + h) + f(x + 2 * h)
            x += 2 * h
        return res * h / 3

    @staticmethod
    def gauss(f: Call[[float], float], a: float, b: float, n: int) -> float:
        def pToV(p: float, c: float, d: float) -> float:
            return (d + c) / 2 + (d - c) * p / 2

        x, w = roots_legendre(n)
        return sum([(b - a) / 2 * w[i] * f(pToV(x[i], a, b)) for i in range(n)])

    @staticmethod
    def __integrated(p: float) -> Call[[float, float], float]:
        t = lambda x, y: 2 * cos(x) / (1 - sin(x) ** 2 * cos(y) ** 2)
        return lambda x, y: 4 / pi * (1 - exp(-p * t(x, y))) * cos(x) * sin(x)
