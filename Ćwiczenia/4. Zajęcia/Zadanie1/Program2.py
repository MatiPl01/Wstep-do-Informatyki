"""
Zadanie 1. Dana jest tablica T[N][N]. Prosze napisac funkcje wypełniajaca tablice kolejnymi liczbami
naturalnymi po spirali.
"""

import time
import os
from colorama import Fore, Style


# A helper function to show animation of filling matrix with values
def show_matrix(matrix: 'a 2-dimensional iterable', just: int, sleep=.5, *, colorize=True):
    os.system('cls')
    matrix_cp = [row[:] for row in matrix]
    colors = (Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW)

    colorized = lambda color, v: f'{color}{str(v).ljust(just)}{Style.RESET_ALL}'

    start_idx = 0
    for row_idx in range(start_idx, len(matrix) // 2):
        for col_idx in range(start_idx, len(matrix[row_idx]) - start_idx - 1):
            coords = ((row_idx, col_idx), (col_idx, -row_idx-1), (-row_idx-1, -col_idx-1), (-col_idx-1, row_idx))
            for (row, col), color in zip(coords, colors):
                if colorize and matrix[row][col]:
                    matrix_cp[row][col] = colorized(color, matrix_cp[row][col])
                else:
                    matrix_cp[row][col] = str(matrix_cp[row][col]).ljust(just)
        start_idx += 1

    if len(matrix) % 2 == 1:
        center_idx = len(matrix) // 2
        matrix[center_idx][center_idx] = str(matrix[center_idx][center_idx]).ljust(just)

    for row in matrix_cp:
        for val in row:
            print(val, end=' ')
        print()

    time.sleep(sleep)


def create_matrix(rows: int, columns: int, *, fill_with=0):
    return [[fill_with]*columns for _ in range(rows)]


def fill_ints_spiral(matrix: 'a 2-dimensional square matrix'):
    curr_num = 1
    start_idx = 0  # The same for columns and rows

    for row_idx in range(start_idx, len(matrix)//2):
        # Store current iterations count over the elements in a row in order to fill matrix with proper values
        iterations_count = len(matrix[row_idx]) - start_idx * 2 - 1

        for col_idx in range(start_idx, start_idx + iterations_count):
            matrix[row_idx][col_idx] = curr_num
            matrix[col_idx][-row_idx-1] = curr_num + iterations_count
            matrix[-row_idx-1][-col_idx-1] = curr_num + iterations_count*2
            matrix[-col_idx-1][row_idx] = curr_num + iterations_count*3
            curr_num += 1

            show_matrix(matrix, len(str(len(matrix) ** 2)), sleep=.1)

        curr_num = matrix[-col_idx-1][row_idx]+1
        start_idx += 1

    # Add a center value if odd rows/columns count
    if len(matrix) % 2 == 1:
        center_idx = len(matrix) // 2
        matrix[center_idx][center_idx] = curr_num


if __name__ == '__main__':
    n = int(input('(n) > '))
    nums_matrix = create_matrix(n, n)
    fill_ints_spiral(nums_matrix)

    print('[')
    for row in nums_matrix:
        print(f'  {row}')
    print(']')
