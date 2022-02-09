"""
Zadanie 1. Dana jest tablica T[N][N]. Prosze napisac funkcje wypełniajaca tablice kolejnymi liczbami
naturalnymi po spirali.
"""

import time
import os
from colorama import Fore, Style


# A helper function to show animation of filling matrix with values
def show_matrix(matrix: 'a 2-dimensional iterable', just: int, sleep=.5):
    os.system('cls')
    for row in matrix:
        for v in row:
            val = str(v).ljust(just)
            print(f'{Fore.GREEN}{val}{Style.RESET_ALL}' if v else val, end=' ')
        print()
    time.sleep(sleep)


def create_matrix(rows: int, columns: int, *, fill_with=0):
    return [[fill_with]*columns for _ in range(rows)]


def fill_ints_spiral(matrix: 'a 2-dimensional iterable'):
    row_range = [1, len(matrix)-1]
    col_range = [0, len(matrix[0])-1]
    row = col = 0
    direction = 1  # 1 - right, 2 - down, 3 - left, 4 - up

    max_num = len(matrix) * len(matrix[0])
    for num in range(1, max_num+1):
        matrix[row][col] = num

        if direction in {1, 3}:  # Move horizontally
            if direction == 1:
                if col < col_range[1]:
                    col += 1  # Go right
                else:
                    col_range[1] -= 1
                    direction = 2  # Go down in the next step
                    row += 1
            else:
                if col > col_range[0]:
                    col -= 1  # Go left
                else:
                    col_range[0] += 1
                    direction = 4  # Go up in the next step
                    row -= 1

        else:  # Move vertically
            if direction == 2:
                if row < row_range[1]:
                    row += 1  # Go down
                else:
                    row_range[1] -= 1
                    direction = 3  # Go left in the next step
                    col -= 1
            else:
                if row > row_range[0]:
                    row -= 1  # Go up
                else:
                    row_range[0] += 1
                    direction = 1  # Go right in the next step
                    col += 1

        show_matrix(matrix, len(str(max_num)), sleep=.1)


if __name__ == '__main__':
    n = int(input('(n) > '))
    nums_matrix = create_matrix(n, n)
    fill_ints_spiral(nums_matrix)

    print('[')
    for row in nums_matrix:
        print(f'  {row}')
    print(']')
