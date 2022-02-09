def create_matrix(rows: int, columns: int, *, fill_with=0) -> '2-dimensional list':
    return [[fill_with]*columns for _ in range(rows)]


def fill_matrix(matrix: list):
    for i in range(len(matrix)):
        while True:
            row = input(f'{i + 1}. row > ').split()
            if len(row) == len(matrix[i]):
                break
            print('Wrong number of values specified. Please try again.')
        for j, val in enumerate(row):
            matrix[i][j] = int(val)


def count_bin_ones(num: int) -> int:
    count = 0
    while num > 0:
        count += num % 2
        num //= 2
    return count


def is_odd(num: int) -> bool:
    return num % 2 == 1


def get_converted_matrix(matrix: list) -> list:
    new_matrix = []
    for row_idx in range(len(matrix)):
        row = []
        for col_idx in range(len(matrix[row_idx])):
            row.append(is_odd(count_bin_ones(matrix[row_idx][col_idx])))
        new_matrix.append(row)
    return new_matrix


def all_values_are_odd(matrix: list, skipped_rows: 'iterable', skipped_columns: 'iterable') -> bool:
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            if row_idx in skipped_rows or col_idx in skipped_columns:
                continue
            if not matrix[row_idx][col_idx]:  # If at least one value is even, return False
                return False
    return True  # Else, return True


def check_condition(matrix: list) -> bool:
    if len(matrix) == 1 or len(matrix[0]) <= 2:
        return False

    converted_matrix = get_converted_matrix(matrix)

    for row_idx in range(len(matrix)):
        for col_1_idx in range(len(matrix[row_idx])):
            for col_2_idx in range(col_1_idx+1, len(matrix[row_idx])):

                if all_values_are_odd(converted_matrix, {row_idx}, {col_1_idx, col_2_idx}):
                    print(row_idx, col_1_idx, col_2_idx)
                    return True
    return False


if __name__ == '__main__':
    N = int(input('(N) > '))
    t = create_matrix(N, N)
    fill_matrix(t)
    print(check_condition(t))


'''
4
91 70 59 22
81 99 37 76
23 65 87 91
35 26 2 99

6
1 2 35 12 52 44
19 52 98 34 37 32
21 74 82 23 89 32
20 93 56 32 19 21
43 94 44 84 22 16
53 69 64 34 79 84
'''
