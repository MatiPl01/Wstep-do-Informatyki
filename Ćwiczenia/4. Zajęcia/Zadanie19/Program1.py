"""
Zadanie 19. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Prosze napisac funkcje, która
zwraca liczbe par elementów, o okreslonym iloczynie, takich ze elementy sa odległe o jeden ruch skoczka
szachowego.
"""

from colorama import Fore, Style
import time
import os


def show_colorized_matrix(matrix, num_coords, fields_to_check, checked_field, searched_product, pairs_found, *, sleep=.2):
    print_val = lambda color, val: print(f'{getattr(Fore, color.upper())}{val}{Style.RESET_ALL}', end=' ')

    # Find greatest-length value
    max_val_length = 0
    for row in matrix:
        for val in row:
            length = len(str(val))
            if length > max_val_length:
                max_val_length = length

    # Print colorized matrix
    os.system('cls')

    print(f'Searched product: {searched_product}')
    print(f'Current product: {matrix[num_coords[0]][num_coords[1]] * matrix[checked_field[0]][checked_field[1]]}')
    print(f'Found matching pairs count: {pairs_found}\n')

    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            val = str(matrix[row_idx][col_idx]).ljust(max_val_length)
            curr_coords = (row_idx, col_idx)
            if curr_coords == num_coords:
                print_val('red', val)     # Current number (position of the chess jumper)
            elif curr_coords == checked_field:
                print_val('blue', val)    # Currently checked available field for the chess jumper
            elif curr_coords in fields_to_check:
                print_val('yellow', val)  # All available fields for chess jumpers that haven't been checked yet
            else:
                print(val, end=' ')       # All the remaining values
        print()

    time.sleep(sleep)


def create_matrix(rows: int, columns: int, *, fill_with=0) -> '2-dimensional list':
    """Creates a 2-dimensional list of a specified number of rows and columns"""
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


def count_pairs_of_specified_product_from_fields_accessible_for_chess_jumper(matrix: list, product: int) -> int:
    """Counts number pairs that product of is equal to the specified 'product'. As a pair of numbers
    we consider the currently checked number and one of the numbers lying one chess jumper's move from
    the currently checked number."""
    pairs_found = 0

    for row_idx in range(len(matrix)-1):
        for col_idx in range(len(matrix[row_idx])):
            curr_num = matrix[row_idx][col_idx]

            if row_idx <= len(matrix)-3:
                if col_idx == 0:
                    fields_to_check = (row_idx+2, col_idx+1), (row_idx+1, col_idx+2)
                elif col_idx == len(matrix[row_idx])-1:
                    fields_to_check = (row_idx+1, col_idx-2), (row_idx+2, col_idx-1)
                elif col_idx == 1:
                    fields_to_check = (row_idx+2, col_idx-1), (row_idx+2, col_idx+1), (row_idx+1, col_idx+2)
                elif col_idx == len(matrix[row_idx])-2:
                    fields_to_check = (row_idx+1, col_idx-2), (row_idx+2, col_idx-1), (row_idx+2, col_idx+1)
                else:
                    fields_to_check = (row_idx+1, col_idx-2), (row_idx+2, col_idx-1), (row_idx+2, col_idx+1), (row_idx+1, col_idx+2)

            elif row_idx == len(matrix)-2:
                if col_idx <= 1:
                    fields_to_check = ((row_idx+1, col_idx+2),)
                elif col_idx >= len(matrix[row_idx])-2:
                    fields_to_check = ((row_idx+1, col_idx-2),)
                else:
                    fields_to_check = (row_idx+1, col_idx-2), (row_idx+1, col_idx+2)

            for i, j in fields_to_check:
                if curr_num * matrix[i][j] == product:
                    pairs_found += 1

                show_colorized_matrix(matrix, (row_idx, col_idx), fields_to_check, (i, j), product, pairs_found, sleep=.3)

    return pairs_found


if __name__ == '__main__':
    k = int(input('(product) > '))
    n = int(input('(n) > '))
    t = create_matrix(n, n)
    fill_matrix(t)
    print(count_pairs_of_specified_product_from_fields_accessible_for_chess_jumper(t, k))

'''
0
8
19 1 9 4 10 20 2 3 
5 8 5 11 8 17 14 13 
14 7 1 10 1 16 0 13 
18 10 14 9 12 18 6 15 
13 4 7 9 6 15 12 1 
1 16 16 13 2 16 13 8 
8 5 14 17 15 13 10 0 
7 18 20 0 17 12 13 9

72
5
12 5  8  9  45
15 2  47 3  6
4  12 22 9  8
12 10 13 6  7 
11 6  9  5  12
'''
