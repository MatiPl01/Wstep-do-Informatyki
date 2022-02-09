"""
Zadanie 6. Dane sa dwie tablice mogace pomiescic taka sama liczbe elementów: T1[N][N] i T2[M], gdzie
M=N*N. W kazdym wierszu tablicy T1 znajduja sie uporzadkowane rosnaco (w obrebie wiersza) liczby
naturalne. Prosze napisac funkcje przepisujaca wszystkie singletony (liczby wystepujace dokładnie raz) z
tablicy T1 do T2, tak aby liczby w tablicy T2 były uporzadkowane rosnaco. Pozostałe elementy tablicy T2
powinny zawierac zera.
"""

import os
import time
from colorama import Style, Fore


def print_colorized_matrix(source_matrix, target_list, target_elements, pointers, curr_val_row_idx, excluded_values, *, sleep=.3):
    print_val = lambda color, val: print(f'{getattr(Fore, color.upper())}{val}{Style.RESET_ALL}', end=' ')

    # Find number of greatest number of digits in source_matrix
    max_source_matrix_val_length = len(str(source_matrix[0][0]))
    for row in source_matrix:
        for val in row:
            val = str(val)
            if len(val) > max_source_matrix_val_length:
                max_source_matrix_val_length = len(val)

    os.system('cls')

    # Find start index of target_matrix representation
    end_idx = 0
    for end_idx, val in enumerate(target_list):
        if val is None:
            break
    start_idx = max(0, end_idx-target_elements)

    # Print target_list
    print('----- Source matrix: -----')
    for row_idx in range(len(source_matrix)):
        for col_idx in range(len(source_matrix[row_idx])):
            val = str(source_matrix[row_idx][col_idx]).ljust(max_source_matrix_val_length)
            if row_idx == curr_val_row_idx and col_idx == pointers.get(row_idx):  # Colorize currently checked field
                print_val('red', val)
            elif row_idx in pointers and pointers[row_idx] == col_idx:            # Colorize positions of pointers
                print_val('yellow', val)
            elif source_matrix[row_idx][col_idx] in excluded_values:              # Colorize excluded fields
                print_val('LIGHTBLACK_EX', val)
            elif row_idx not in pointers or col_idx < pointers[row_idx]:          # Colorize values that were moved to the target_list
                print_val('LIGHTCYAN_EX', val)
            else:
                print(val, end=' ')
        print()

    # Print target_list
    print(f'\n----- Target list (last {target_elements} elements): -----')
    for idx in range(start_idx, start_idx + target_elements):
        val = target_list[idx]
        if val is not None:
            print_val('green', val)
        else:
            print(val, end=' ')
    print()

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


def rewrite_singletons(source_matrix: [[int]], target_list: list):
    """Rewrites singleton values from 'source_matrix' to 'target_matrix' in an increasing order.
    Note that all rows in 2-dimensional 'source_matrix' list must be sorted in an increasing
    order as well."""
    # Store information about values that appear more than once in the 'source_matrix'
    checked_values = set()
    excluded_values = set()
    for row_idx in range(len(source_matrix)):
        for col_idx in range(len(source_matrix[row_idx])):
            val = source_matrix[row_idx][col_idx]
            if val in checked_values:
                excluded_values.add(val)
            else:
                checked_values.add(val)
    del checked_values

    # Trace position of pointers in each row of 'source_matrix' to move appropriate values
    pointers = dict.fromkeys(range(len(source_matrix)), 0)

    rewritten_elements = 0

    while pointers:
        lowest_val = lowest_val_row_idx = None
        pointers_to_remove = []

        # Look for the lowest value and store all its occurrences (whe repeated)
        for row_idx in pointers.keys():
            while source_matrix[row_idx][pointers[row_idx]] in excluded_values:
                pointers[row_idx] += 1
                if pointers[row_idx] >= len(source_matrix[row_idx]):
                    pointers_to_remove.append(row_idx)
                    break
            else:
                curr_val = source_matrix[row_idx][pointers[row_idx]]
                if not lowest_val or curr_val < lowest_val:
                    lowest_val = curr_val
                    lowest_val_row_idx = row_idx

            print_colorized_matrix(source_matrix, target_list, 15, pointers, row_idx, excluded_values, sleep=.5)

        # Save lowest value found in the target list
        target_list[rewritten_elements] = lowest_val
        rewritten_elements += 1
        pointers[lowest_val_row_idx] += 1
        if pointers[lowest_val_row_idx] >= len(source_matrix[lowest_val_row_idx]):
            pointers_to_remove.append(lowest_val_row_idx)

        # Remove useless pointers
        for pointer in pointers_to_remove:
            pointers.pop(pointer)


if __name__ == '__main__':
    n = int(input('(n) > '))
    t1 = create_matrix(n, n)
    fill_matrix(t1)
    t2 = [None] * n*n
    rewrite_singletons(t1, t2)
    print(t1, t2, sep='\n')


'''
6
1 431 515 634 744 2535
16 34 65 634 1234 9064
1 2 3 4 5 6
231 543 765 765 943 1234
6 98 712 819 6542 12334
1 654 3421 7523 9783 43212

10
2 22 40 68 77 77 86 92 94 100
47 48 49 52 67 68 79 85 90 100
2 23 24 28 52 90 91 95 100 100
2 5 14 28 47 48 50 56 70 71
1 7 9 18 21 32 33 62 63 90
34 52 56 57 68 80 85 86 96 100
2 8 17 38 39 39 43 43 66 89
13 21 26 49 53 59 90 93 96 99
2 6 13 15 34 64 70 72 72 91
32 40 50 63 69 70 75 75 79 91
'''
