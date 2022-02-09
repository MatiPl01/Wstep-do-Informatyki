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


def fill_ints_spiral(matrix: 'a 2-dimensional square matrix'):
    curr_num = 1
    i, j = 0, -1

    def fill_num(row, col):
        nonlocal curr_num
        matrix[row][col] = curr_num
        curr_num += 1
        show_matrix(matrix, just=len(str(len(matrix)**2)), sleep=.05)

    steps = len(matrix)
    curr_step = 1
    move_vertically = False

    while steps > 0:
        if move_vertically:
            for _ in range(steps):
                i += curr_step
                fill_num(i, j)
            curr_step *= -1
        else:
            for _ in range(steps):
                j += curr_step
                fill_num(i, j)
            steps -= 1

        move_vertically = not move_vertically


if __name__ == '__main__':
    n = int(input('(n) > '))
    nums_matrix = create_matrix(n, n)
    fill_ints_spiral(nums_matrix)

    print('[')
    for row in nums_matrix:
        print(f'  {row}')
    print(']')
