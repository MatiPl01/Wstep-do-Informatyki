"""
Zadanie 9. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Prosze napisac funkcje, która w
poszukuje w tablicy kwadratu o liczbie pól bedacej liczba nieparzysta wieksza od 1, którego iloczyn 4 pól
naroznych wynosi k. Do funkcji nalezy przekazac tablice i wartosc k. Funkcja powinna zwrócic informacje
czy udało sie znalezc kwadrat oraz współrzedne (wiersz, kolumna) srodka kwadratu.
"""

import os
import time
from colorama import Fore, Style


def print_colorized_matrix(matrix, start_idx, center_row_idx, center_col_idx, side_length, product, curr_product, *,
                           sleep=.1):
    """Shows colorized current state of square's position searching"""
    print_val = lambda color, val: print(f'{getattr(Fore, color.upper())}{val}{Style.RESET_ALL}', end=' ')

    # Find number of greatest number of digits
    max_val_length = 0
    for row in matrix:
        for val in row:
            val = str(val)
            if len(val) > max_val_length:
                max_val_length = len(val)

    # Print colorized matrix
    os.system('cls')
    corners_coordinates = {
        (center_row_idx - start_idx, center_col_idx - start_idx),
        (center_row_idx - start_idx, center_col_idx + start_idx),
        (center_row_idx + start_idx, center_col_idx - start_idx),
        (center_row_idx + start_idx, center_col_idx + start_idx)
    }

    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            val = str(matrix[row_idx][col_idx]).ljust(max_val_length)
            if row_idx == center_row_idx and col_idx == center_col_idx:                   # Colorize center of the square
                print_val('red', val)
            elif (row_idx, col_idx) in corners_coordinates:                               # Colorize multiplied corners
                print_val('blue', val)
            elif center_row_idx - start_idx <= row_idx <= center_row_idx + start_idx \
                and center_col_idx - start_idx <= col_idx <= center_col_idx + start_idx:  # Colorize the whole square
                print_val('yellow', val)
            else:
                print(val, end=' ')
        print()
    print(f'Searched product of values in corners: {product}')
    print(f'Current product of values in corners: {curr_product}')
    time.sleep(sleep)


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


def search_square(matrix: list, product: int):
    """Returns coordinates of a square (if found) that product of all values lying in its
    corners is equal to the specified value of 'product' parameter. If not found returns None."""
    side_length = 3  # length of the square's side

    # Look for appropriate placement of a square
    while side_length <= min(len(matrix), len(matrix[0])):
        start_idx = side_length // 2

        # Iterate over subsequent possible coordinates of the square's center
        for center_row_idx in range(start_idx, len(matrix)-start_idx):
            for center_col_idx in range(start_idx, len(matrix[center_row_idx])-start_idx):

                # Multiply values that are placed in the corners
                mul = matrix[center_row_idx - start_idx][center_col_idx + start_idx] *\
                      matrix[center_row_idx - start_idx][center_col_idx - start_idx] *\
                      matrix[center_row_idx + start_idx][center_col_idx - start_idx] *\
                      matrix[center_row_idx + start_idx][center_col_idx + start_idx]

                # Show colorized output (not necessary)
                print_colorized_matrix(matrix, start_idx, center_row_idx, center_col_idx, side_length, product, mul)

                # Return coordinates of the square's center if a proper product of values in the corners were found
                if mul == product:
                    return center_row_idx, center_col_idx

        # If couldn't have found any matching square's position, increase its side length
        side_length += 2

    return None  # Return None if no square of any size was found


if __name__ == '__main__':
    k = int(input('(k) > '))
    n = int(input('(n) > '))
    t = create_matrix(n, n)
    fill_matrix(t)
    print(search_square(t, k))

'''
14276737555440
7
12 421 124 124 124 213 2145
1443 412 124 1413 513 141 124
88 532 265 65 346 58 623
252 44 636 457 345 1434 5232
3522 4632 22 25346 4563 2342 435
34134 36436 324 11 25245 6745 4543
4535 43636 23 41 1 6456 567


11964600
12
17 70 94 21 33 14 58 27 27 79 17 97 
32 86 54 46 89 62 43 4 31 96 47 84 
29 29 40 69 20 58 32 25 81 99 37 50 
16 43 79 98 45 69 23 39 15 20 28 85 
73 6 15 74 6 25 17 1 68 47 5 20 
10 38 19 38 88 11 38 68 38 19 32 12 
22 77 46 17 9 73 47 67 90 55 53 87 
7 39 92 58 15 63 3 58 47 85 89 52 
60 68 1 60 78 66 32 86 34 58 51 99 
30 3 20 62 80 60 38 86 20 66 72 34 
69 96 54 11 52 72 62 65 87 17 43 75 
64 51 40 49 12 68 80 63 7 68 30 54 
'''
