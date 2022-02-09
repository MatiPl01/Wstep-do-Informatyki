"""
Zadanie 4. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Prosze napisac funkcje, która
zwraca wiersz i kolumne dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym lezy
element do sumy elementów wiersza w którym lezy element jest najwieksza.
"""

def create_matrix(rows: int, columns: int, *, fill_with=0) -> '2-dimensional list':
    """Creates a 2-dimensional list of specified number of rows and columns"""
    return [[fill_with]*columns for _ in range(rows)]


def fill_matrix(matrix: list):
    """Fills matrix with values provided by the user"""
    for i in range(len(matrix)):
        while True:
            row = input(f'{i + 1}. row > ').split()
            if len(row) == len(matrix[i]):
                break
            print('Wrong number of values specified. Please try again.')
        for j, val in enumerate(row):
            matrix[i][j] = int(val)


def greatest_column_to_row_sum_ratio_element(matrix: list) -> tuple:
    """Returns a tuple containing row and column index of a number for which
    a sum of elements being in the same column divided by a sum of elements from
    the same row as the checked number is the greatest"""
    cols_sums = []
    rows_sums = []

    for start_idx in range(len(matrix)):  # Works only with square matrices
        rows_sums.append(sum(matrix[start_idx]))
        col_sum = 0
        for row_idx in range(len(matrix)):
            col_sum += matrix[row_idx][start_idx]
        cols_sums.append(col_sum)

    max_col_sum_idx = 0
    for col_idx, col_sum in enumerate(cols_sums):
        if col_sum > cols_sums[max_col_sum_idx]:
            max_col_sum_idx = col_idx

    min_row_sum_idx = 0
    for row_idx, row_sum in enumerate(rows_sums):
        if row_sum < rows_sums[min_row_sum_idx]:
            min_row_sum_idx = row_idx

    print(rows_sums, cols_sums)

    return min_row_sum_idx, max_col_sum_idx


if __name__ == '__main__':
    n = int(input('(n) > '))
    t = create_matrix(n, n)
    fill_matrix(t)
    print(greatest_column_to_row_sum_ratio_element(t))

'''
6
1 32 4 123 24 21
431 123 3412 42 64 34
12 2424 1 42 23 43
42 2143 12 2 342 23
43 451 6 23 532 53
33 643 23 352 53 364
'''
