import random
from pprint import pprint as pp


def random_matrix(rows: int, columns: int, min_num: int, max_num: int) -> [[int]]:
    return [[random.randint(min_num, max_num) for _ in range(rows)] for _ in range(columns)]


def lowest_king_move_cost(matrix, start_col=0) -> int:

    def recur(row_idx, col_idx, curr_sum=0):
        if row_idx == len(matrix)-1:
            return curr_sum

        sums = []
        row_idx += 1
        for i in range(max(0, col_idx-1), min(col_idx+2, len(matrix[row_idx]))):
            sums.append(recur(row_idx, i, curr_sum + matrix[row_idx][i]))

        return min(sums)

    return recur(-1, start_col, matrix[0][start_col])


def lowest_king_move_cost_columns(matrix, start_col=0) -> list:
    min_cost = 0
    for i in range(len(matrix)):
        min_cost += matrix[i][start_col]
    min_cost_indices = []

    def recur(row_idx, col_idx, curr_sum=0, indices=[]):
        nonlocal min_cost, min_cost_indices

        if row_idx == len(matrix)-1:
            if curr_sum < min_cost:
                min_cost = curr_sum
                min_cost_indices = indices
            return curr_sum

        sums = []
        row_idx += 1
        for i in range(max(0, col_idx - 1), min(col_idx + 2, len(matrix[row_idx]))):
            sums.append(recur(row_idx, i, curr_sum + matrix[row_idx][i], indices + [i]))

        return min(sums)

    recur(0, start_col, matrix[0][start_col], [start_col])
    return min_cost_indices


if __name__ == '__main__':
    # k = int(input('(k) > '))
    # t = create_matrix(8, 8)
    # fill_matrix(t)

    k = 2
    random.seed(0)
    t = random_matrix(8, 8, 0, 1000)
    pp(t)
    print()
    print(lowest_king_move_cost(t, k))
    print(lowest_king_move_cost_columns(t, k))
