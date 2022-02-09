import random
from pprint import pprint as pp


def random_matrix(rows: int, cols: int, min_val: int, max_val: int) -> [[int]]:
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def last_digit(num: int) -> int:
    return num % 10


def first_digit(num: int) -> int:
    while num > 10:
        num //= 10
    return num


def get_possible_moves(d_row: int, d_col: int) -> tuple:
    if d_row > 0:               # A target point is below
        if abs(d_col) < d_row:  # A target point is below both diagonals
            return 6, 5, 7, 3, 4
        if d_col == d_row:      # A target point is on the top-left bottom-right diagonal
            return 7, 4, 6
        if -d_col == d_row:     # A target point is on the top-right bottom-left diagonal
            return 5, 3, 6
    if d_row < 0:               # A target point is above
        if abs(d_col) < abs(d_row):
            return 1, 0, 2, 3, 4
        if d_col == d_row:      # A target point is on the top-left bottom-right diagonal
            return 0, 3, 1
        if -d_col == d_row:     # A target point is on the top-right bottom-left diagonal
            return 2, 1, 4
    if d_col > 0 and abs(d_row) < d_col:
        return 4, 2, 7, 1, 6    # A target point is on the right side between both diagonals
    else:
        return 3, 0, 5, 1, 6    # A target point is on the left side between both diagonals


def get_move_coordinates(row_idx: int, col_idx: int, move_id: int) -> (int, int):
    """
    0 1 2
    3 ♔ 4
    5 6 7
    """
    if move_id == 0:
        return row_idx-1, col_idx-1
    if move_id == 1:
        return row_idx-1, col_idx
    if move_id == 2:
        return row_idx-1, col_idx+1
    if move_id == 3:
        return row_idx, col_idx-1
    if move_id == 4:
        return row_idx, col_idx+1
    if move_id == 5:
        return row_idx+1, col_idx-1
    if move_id == 6:
        return row_idx+1, col_idx
    if move_id == 7:
        return row_idx+1, col_idx+1


def can_move(matrix, row1: int, col1: int, row2: int, col2: int):
    return 0 <= row2 < len(matrix) and 0 <= col2 < len(matrix[row2])\
           and last_digit(matrix[row1][col1]) < first_digit(matrix[row2][col2])


def get_all_paths(matrix, start_point, target_point) -> list:
    row, col = target_point
    target_point = len(matrix) + row if row < 0 else row, len(matrix[0]) + col if col < 0 else col
    target_row, target_col = target_point

    all_paths = []

    def recur(row_idx, col_idx, moves=(), visited=set()):
        if (row_idx, col_idx) == target_point:
            all_paths.append(moves)
        else:
            for move_id in get_possible_moves(target_row - row_idx, target_col - col_idx):
                next_coords = get_move_coordinates(row_idx, col_idx, move_id)
                if next_coords not in visited:
                    next_row, next_col = next_coords
                    if can_move(matrix, next_row, next_col, next_row, next_col):
                        recur(next_row, next_col, moves + (move_id,), visited.union({next_coords}))

    recur(*start_point, visited={start_point})

    return all_paths


if __name__ == '__main__':
    random.seed(12)
    T = random_matrix(8, 8, 0, 100)
    pp(T)
    print(*get_all_paths(T, (2, 0), (5, 7)), sep='\n')  # The king can go from any starting point to any target point
