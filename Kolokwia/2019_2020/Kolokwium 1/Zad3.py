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


def recur_init(matrix: list):

    def recur(row_idx: int, start_col_idx: int, curr_sum: int) -> bool:
        # If we've finished searching, return True if sum is equal to 0, else False
        if row_idx == len(matrix)-1:
            return curr_sum == 0
        # Else, start searching recursively
        for col_idx in range(len(matrix[row_idx])):
            # start_col_idx becomes an index of a column occupied by a chess king being in a previous row
            if abs(start_col_idx - col_idx) > 1:  # Only columns fulfilling this condition can be checked
                if recur(row_idx+1, col_idx, curr_sum+matrix[row_idx+1][col_idx]):
                    return True
        return False
    return recur


def check_condition(matrix: list) -> bool:
    if len(matrix) < 3 or len(matrix[0]) < 3:
        return False

    recur = recur_init(matrix)
    # Place a chess king in the first row (check for all columns)
    for start_col_idx in range(len(matrix[0])):
        if recur(0, start_col_idx, 0):
            return True

    return False


if __name__ == '__main__':
    N = int(input('(N) > '))
    t = create_matrix(N, N)
    fill_matrix(t)
    print(check_condition(t))


'''
6
56 -75 39 91 -38 11
98 51 46 -34 -17 13
98 16 -10 -1 -81 27
-64 -36 -78 80 -37 85
48 -75 31 -19 45 70
61 -51 -19 -51 -12 -89
'''
