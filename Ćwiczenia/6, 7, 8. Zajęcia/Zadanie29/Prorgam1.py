from math import sqrt
from functools import reduce
from pprint import pprint as pp
import random


def random_3D_points(count: int, max_val, *, rounding=None) -> [(float, float, float)]:
    points = []
    for _ in range(count):
        points.append(tuple(round(random.choice((-1, 1)) * random.random() * max_val, rounding) for _ in range(3)))
    return points


def centre_of_mass(points) -> tuple:
    coords_sum = reduce(lambda acc, val: tuple(sum(pair) for pair in zip(acc, val)), points)
    return tuple(v / len(points) for v in coords_sum)


def vector3D_length(x, y, z) -> float:
     return sqrt(x**2 + y**2 + z**2)


def is_centre_of_mass_closer_than_r(T, r) -> bool:

    def recur(idx=-1, points=[]):
        # global count
        # count += 1
        if idx == len(T)-1:
            return len(points) >= 3 and vector3D_length(*centre_of_mass(points)) <= r

        idx += 1
        return recur(idx, points) or recur(idx, points + [T[idx]])

    return recur()


count = 0

if __name__ == '__main__':
    random.seed(0)
    r = .5
    T = random_3D_points(100, 100, rounding=4)
    pp(T)
    print()
    print(is_centre_of_mass_closer_than_r(T, r))
    # print(count)


# r = 10
# T = [(10, 0, 0), (-10, 0, 0), (0, 0, 30)]


# def centre_of_mass(points) -> list:
#     coords = [0] * len(points[0])
#
#     for i in range(len(points)):
#         for j in range(len(points[i])):
#             coords[j] += points[i][j]
#
#     for i in range(len(coords)):
#         coords[i] /= len(points)
#
#     return coords
