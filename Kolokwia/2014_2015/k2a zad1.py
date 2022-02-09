import random


def generate_random_coords(count, min_num, max_num):
    coords = set()
    while len(coords) < count:
        new_coords = tuple(random.randint(min_num, max_num) for _ in range(2))
        if new_coords not in coords:
            coords.add(new_coords)
    return coords


def distance(r1, c1, r2, c2):
    return max(abs(r1 - r2), abs(c1 - c2))


def find_two_kings(board_size, coordinates):
    distances_dct = {}

    center_idx = board_size//2

    for coords in coordinates:
        dist = distance(*coords, center_idx, center_idx)
        if dist in distances_dct:
            return coords, distances_dct[dist]
        else:
            distances_dct[dist] = coords

    return None


if __name__ == '__main__':
    size = 201
    kings_count = 100
    coords = generate_random_coords(kings_count, 0, size-1)
    res = find_two_kings(size, coords)
    if res:
        print(f"Matching kings coordinates:\n{res}.")
    else:
        print("Couldn't have found two kings of the same distance from the board's centre.")
