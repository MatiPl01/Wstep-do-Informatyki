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


def can_reach(matrix) -> bool:
    possible_moves = ((1, 1), (0, 1), (1, 0), (-1, 1), (1, -1))
    visited = set()

    def recur(row_idx=0, col_idx=0):
        if row_idx == len(matrix)-1 and col_idx == len(matrix)-1:
            return True

        visited.add((row_idx, col_idx))
        for row_move, col_move in possible_moves:
            new_row = row_idx + row_move
            new_col = col_idx + col_move
            if (new_row, new_col) not in visited and 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
                curr_num = matrix[row_idx][col_idx]
                new_num = matrix[new_row][new_col]
                if last_digit(curr_num) < first_digit(new_num) and recur(new_row, new_col):
                    return True
        return False

    return recur()


if __name__ == '__main__':
    random.seed(12)
    T = random_matrix(8, 8, 0, 100)
    pp(T)
    print(can_reach(T))

    # print(get_path(T))


    # i = 0
    # while True:
    #     random.seed(i)
    #     T = random_matrix(8, 8, 0, 100)
    #
    #     if can_reach(T):
    #         print(i)
    #         break
    #
    #     i += 1


# def get_path(matrix) -> list:
#     possible_moves = ((1, 1), (0, 1), (1, 0), (-1, 1), (1, -1))
#     visited = set()
#
#     def recur(row_idx=0, col_idx=0, curr_visited=[]):
#         if row_idx == len(matrix)-1 and col_idx == len(matrix)-1:
#             curr_visited.append((row_idx, col_idx))
#             return curr_visited
#
#         visited.add((row_idx, col_idx))
#         for row_move, col_move in possible_moves:
#             new_row = row_idx + row_move
#             new_col = col_idx + col_move
#             if (new_row, new_col) not in visited and 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
#                 curr_num = matrix[row_idx][col_idx]
#                 new_num = matrix[new_row][new_col]
#                 if last_digit(curr_num) < first_digit(new_num):
#                     res = recur(new_row, new_col, curr_visited + [(row_idx, col_idx)])
#                     if res:
#                         return res
#         return []
#
#     return recur()
