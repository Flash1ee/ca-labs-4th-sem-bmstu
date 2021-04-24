from __future__ import annotations
from utils import Point

import numpy as np


class Approximator:
    def __init__(self):
        self.coeffs = []

    def get_coeffs(self, mat: list[list[float]]) -> Approximator:
        self.coeffs = [mat[i][len(mat)] for i in range(len(mat))]

        return self

    def build(self, pl: list[Point]) -> list[Point]:
        dots = []

        for i in np.arange(pl[0].x, pl[-1].x + 0.1, 0.1):
            d = Point(i, 0, 0)

            for j in range(len(self.coeffs)):
                d.y += d.x ** j * self.coeffs[j]

            dots += [d]

        return dots


class SLAU:
    mat: list[list[float]]
    n: int

    def build(self, pl: list[Point], _n: int) -> SLAU:
        self.n = _n
        self.mat = [[0 for i in range(self.n + 2)] for i in range(self.n + 1)]

        for i in range(self.n + 1):
            for j in range(self.n + 1):
                slae_coeffs = 0.0
                expanded_coeff = 0.0
                for k in range(len(pl)):
                    slae_coeffs += pl[k].weight * \
                                   (pl[k].x ** i) * \
                                   (pl[k].x ** j)
                    expanded_coeff += pl[k].weight * pl[k].y * (pl[k].x ** i)

                self.mat[i][j] = slae_coeffs
                self.mat[i][self.n + 1] = expanded_coeff

        return self

    def solve(self) -> list[list[float]]:
        for i in range(self.n + 1):
            for j in range(self.n + 1):
                if i == j:
                    continue

                sub_coeff = self.mat[j][i] / self.mat[i][i]
                for k in range(self.n + 2):
                    self.mat[j][k] -= sub_coeff * self.mat[i][k]

        for i in range(self.n + 1):
            divider = self.mat[i][i]
            for j in range(self.n + 2):
                self.mat[i][j] /= divider

        return self.mat
