from pprint import pprint as pp
from math import sqrt
import random


def random_points(count: int, max_val, *, dim=2, float_digits=None) -> [(float, float)]:
    points = []
    for _ in range(count):
        points.append(tuple(round(random.choice((-1, 1)) * random.random() * max_val, float_digits) for _ in range(dim)))
    return points


def centre_of_mass(points) -> tuple:
    coords = [0] * len(points[0])
    for point in points:
        for i, val in enumerate(point):
            coords[i] += val
    return tuple(val / len(points) for val in coords)


def vector2D_length(x, y) -> float:
    return sqrt(x**2 + y**2)


def matching_set_exists(seq, max_distance, max_points_count) -> bool:

    def recur(idx=0, points=()):
        if len(points) <= max_points_count and idx < len(seq):
            # If a number of points is a multiplier of 3 and a distance is lower than the max_distance value
            if points and not len(points) % 3 and vector2D_length(*centre_of_mass(points)) < max_distance:
                # print(points, centre_of_mass(points), vector2D_length(*centre_of_mass(points)), sep='\n')
                return True
            else:
                return recur(idx+1, points) or recur(idx+1, points + (seq[idx],))
        else:
            return False

    return recur()


if __name__ == '__main__':
    r = 1.757
    k = 6
    random.seed(0)
    t = random_points(10, 100, float_digits=3)
    pp(t)
    print(matching_set_exists(t, r, k))
