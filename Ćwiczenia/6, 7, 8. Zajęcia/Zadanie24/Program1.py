from pprint import pprint as pp
from math import sqrt
import random


def random_points(count: int, max_val, *, dim=2, rounding=None) -> [(float, float)]:
    points = []
    for _ in range(count):
        points.append(tuple(round(random.choice((-1, 1)) * random.random() * max_val, rounding) for _ in range(dim)))
    return points


def centre_of_mass(points) -> tuple:
    coords = [0] * len(points[0])
    for point in points:
        for i, val in enumerate(point):
            coords[i] += val
    return tuple(val / len(points) for val in coords)


def distance_between_points(pt1, pt2) -> float:
    return sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)


def shortest_distance(points) -> float:
    random_dist = distance_between_points(points[0], points[1])

    def recur(idx=-1, set1=(), set2=()):
        if idx == len(points)-1:
            if set1 and set2:
                set1_centre = centre_of_mass(set1)
                set2_centre = centre_of_mass(set2)
                return distance_between_points(set1_centre, set2_centre)
            return random_dist

        idx += 1
        new_point = (points[idx],)
        return min(recur(idx, set1, set2),
                   recur(idx, set1 + new_point, set2),
                   recur(idx, set1, set2 + new_point))
    return recur()


if __name__ == '__main__':
    random.seed(0)
    T = random_points(10, 10000, rounding=3)
    pp(T)
    print(shortest_distance(T))

    # print(*shortest_distance_points(T), sep='\n')


# def shortest_distance(points):
#     min_distance = None
#
#     def recur(idx=-1, set1=(), set2=()):
#         if idx == len(points)-1:
#             if set1 and set2:
#                 nonlocal min_distance
#                 set1_centre = centre_of_mass(set1)
#                 set2_centre = centre_of_mass(set2)
#                 distance = distance_between_points(set1_centre, set2_centre)
#                 if min_distance is None:
#                     min_distance = distance
#                 if distance < min_distance:
#                     min_distance = distance
#             return
#         else:
#             idx += 1
#             new_point = (points[idx],)
#             recur(idx, set1, set2)
#             recur(idx, set1 + new_point, set2)
#             recur(idx, set1, set2 + new_point)
#     recur()
#
#     return min_distance


# def shortest_distance_points(points) -> (tuple, tuple):
#     min_distance = None
#     min_distance_sets = ()
#
#     def recur(idx=-1, set1=(), set2=()):
#         if idx == len(points)-1:
#             if set1 and set2:
#                 nonlocal min_distance, min_distance_sets
#                 set1_centre = centre_of_mass(set1)
#                 set2_centre = centre_of_mass(set2)
#                 distance = distance_between_points(set1_centre, set2_centre)
#                 if min_distance is None:
#                     min_distance = distance
#                 if distance < min_distance:
#                     min_distance = distance
#                     min_distance_sets = set1, set2
#             return
#         else:
#             idx += 1
#             new_point = (points[idx],)
#             recur(idx, set1, set2)
#             recur(idx, set1 + new_point, set2)
#             recur(idx, set1, set2 + new_point)
#     recur()
#
#     return min_distance_sets
