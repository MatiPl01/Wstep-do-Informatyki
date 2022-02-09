"""
Zadanie 5. Poprzednie zadanie z tablica wypełniona liczbami całkowitymi.
"""

from colorama import Fore, Style


def print_colorized_result(matrix: list, res_row: int, res_col: int):
    """Shows colorized output (a row and a column that were found)"""
    print_val = lambda color, value: print(f'{getattr(Fore, color.upper())}{value}{Style.RESET_ALL}', end=' ')

    # Find number of greatest number of digits
    max_val_length = len(str(matrix[0][0]))
    for row in matrix:
        for val in row:
            val = str(val)
            if len(val) > max_val_length:
                max_val_length = len(val)

    # Print colorized matrix
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            val = str(matrix[row_idx][col_idx]).ljust(max_val_length)
            if row_idx == res_row and col_idx == res_col:
                print_val('red', val)
            elif col_idx == res_col:
                print_val('yellow', val)
            elif row_idx == res_row:
                print_val('blue', val)
            else:
                print(val, end=' ')
        print()


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
    max_col_sum_idx = 0
    greatest_col_sum = 0
    for col_idx in range(len(matrix[0])):
        curr_sum = 0
        for row_idx in range(len(matrix)):
            curr_sum += matrix[row_idx][col_idx]
        if curr_sum > greatest_col_sum:
            greatest_col_sum = curr_sum
            max_col_sum_idx = col_idx

    min_row_sum_idx = 0
    lowest_row_sum = sum(matrix[0])
    for row_idx in range(1, len(matrix)):
        curr_sum = 0
        for col_idx in range(len(matrix[0])):
            curr_sum += matrix[row_idx][col_idx]
        if curr_sum and curr_sum < lowest_row_sum:
            lowest_row_sum = curr_sum
            min_row_sum_idx = row_idx

    return min_row_sum_idx, max_col_sum_idx


if __name__ == '__main__':
    n = int(input('(n) > '))
    t = create_matrix(n, n)
    fill_matrix(t)
    row_idx, col_idx = greatest_column_to_row_sum_ratio_element(t)
    print('\nRow index:', row_idx, '\nColumn index:', col_idx)
    print_colorized_result(t, row_idx, col_idx)

'''
1 32 -4 123 -24 21 2495
-431 123 -3412 -42 64 34 153
12 -2424 1 42 23 43 -2341
1441 -984 123 638 -2963 1745 0
42 2143 -12 2 -342 23 -41
43 451 6 23 532 53 23 
33 -643 23 -352 53 364 -231
'''
