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


# Finds a destination where a tower should be placed
def get_target_field(matrix):
    # Look for a row in which there is no tower placed
    non_tower_row = None
    for idx, row in enumerate(matrix):
        for val in row:
            if val:
                break
        else:  # If loop was not broken, store this row index as we know there is no tower in th row
            non_tower_row = idx  # The first one is enough and we don't have to look for antorher one
            break

    # Do the same for columns
    non_tower_col = None
    for col_idx in range(len(matrix[0])):
        for row_idx in range(len(matrix)):
            if matrix[row_idx][col_idx]:
                break
        else:  # If loop was not broken, store this row index as we know there is no tower in th row
            non_tower_col = col_idx  # The first one is enough and we don't have to look for antorher one
            break

    return non_tower_row, non_tower_col


def get_source_field(matrix):
    # Look for a row in which there is more than one tower placed
    more_than_one_tower_row = None
    for idx, row in enumerate(matrix):
        found_tower_in_row = False
        for val in row:
            if val:
                if found_tower_in_row:
                    more_than_one_tower_row = idx
                    break
                found_tower_in_row = True
        else:
            continue  # If loop was not broken
        break  # If inner loop was broken break the outer one

    # Do the same for columns
    # Look for a row in which there is more than one tower placed
    more_than_one_tower_col = None
    for col_idx in range(len(matrix[0])):
        found_tower_in_col = False
        for row_idx in range(len(matrix)):
            if matrix[row_idx][col_idx]:
                if found_tower_in_col:
                    more_than_one_tower_col = col_idx
                    break
                found_tower_in_col = True
        else:
            continue  # If loop was not broken
        break  # If inner loop was broken break the outer one

    return more_than_one_tower_row, more_than_one_tower_col


if __name__ == '__main__':
    board = [
        [0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1]
    ]
    print(f"{get_source_field(board)} -> {get_target_field(board)}")
