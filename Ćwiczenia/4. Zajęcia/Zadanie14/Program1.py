"""
Zadanie 14. Dwie liczby naturalne sa zgodne jezeli w zapisie dwójkowym zawieraja te sama liczbe jedynek,
np. 22 = 101102 i 14 = 11102. Dane sa tablice T1[N1][N1] T2[N2][N2], gdzie N2¿N1. Prosze napisac funkcje,
która sprawdza czy istnieje takie połozenie tablicy T1 wewnatrz tablicy T2, przy którym liczba zgodnych
elementów jest wieksza od 33%. Do funkcji nalezy przekazac tablice T1 i T2. Obie oryginalne tablice powinny
pozostac nie zmieniane.
"""

from colorama import Fore, Style
import time
import os
import math


def show_colorized_matrices(small_matrix_bin, big_matrix_bin, start_row_idx, start_col_idx, i, j, found_coords,
                            curr_elements_count, *, sleep=.15):
    print_val = lambda color, value: print(f'{getattr(Fore, color.upper())}{value}{Style.RESET_ALL}', end=' ')

    # Find number of greatest number of digits
    max_small_matrix_val_length = len(str(small_matrix_bin[0][0]))
    for row in small_matrix_bin:
        for val in row:
            val = str(val)
            if len(val) > max_small_matrix_val_length:
                max_small_matrix_val_length = len(val)

    max_big_matrix_val_length = len(str(big_matrix_bin[0][0]))
    for row in big_matrix_bin:
        for val in row:
            val = str(val)
            if len(val) > max_big_matrix_val_length:
                max_big_matrix_val_length = len(val)

    # Print colorized matrices
    os.system('cls')

    print('----- Small matrix: -----')
    for row_idx in range(len(small_matrix_bin)):
        for col_idx in range(len(small_matrix_bin[row_idx])):
            val = str(small_matrix_bin[row_idx][col_idx]).ljust(max_small_matrix_val_length)
            if row_idx == i and col_idx == j:
                print_val('red', val)
            elif (row_idx, col_idx) in found_coords:
                print_val('blue', val)
            else:
                print(val, end=' ')
        print()

    print(f'\n----- Big matrix ({int(curr_elements_count/(len(small_matrix_bin)*len(small_matrix_bin[0]))*100)}%): -----')
    for row_idx in range(len(big_matrix_bin)):
        for col_idx in range(len(big_matrix_bin[row_idx])):
            val = str(big_matrix_bin[row_idx][col_idx]).ljust(max_big_matrix_val_length)
            if row_idx == start_row_idx+i and col_idx == start_col_idx+j:
                print_val('red', val)
            elif (row_idx-start_row_idx, col_idx-start_col_idx) in found_coords:
                print_val('blue', val)
            elif start_row_idx <= row_idx < start_row_idx+len(small_matrix_bin)\
                and start_col_idx <= col_idx < start_col_idx+len(small_matrix_bin[0]):
                print_val('yellow', val)
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


def bin_num_ones_count(num: int) -> int:
    """Returns number of 1 digit in binary representation of the number given"""
    count = 0

    while num > 0:
        count += num % 2
        num //= 2

    return count


def bin_num_ones_count_matrix(matrix: list) -> list:
    """Returns new matrix filled with counts of ones in binary representations
    of appropriate numbers"""
    ones_count_matrix = []
    for row in matrix:
        new_row = []
        for col in row:
            new_row.append(bin_num_ones_count(col))
        ones_count_matrix.append(new_row)
    return ones_count_matrix


def func(big_matrix: 'bigger matrix', small_matrix: 'smaller matrix', searched_ratio: float) -> bool:
    small_matrix_bin = bin_num_ones_count_matrix(small_matrix)
    big_matrix_bin = bin_num_ones_count_matrix(big_matrix)

    searched_elements_count = math.ceil(searched_ratio * len(small_matrix) * len(small_matrix[0]))
    for start_row_idx in range(len(big_matrix) - len(small_matrix) + 1):
        for start_col_idx in range(len(big_matrix[0]) - len(small_matrix[0]) + 1):

            # Count the same elements existing in both matrices on proper fields
            found_coords = set()  # Only for visualisation
            curr_elements_count = 0
            for i in range(len(small_matrix)):
                for j in range(len(small_matrix[0])):
                    if small_matrix_bin[i][j] == big_matrix_bin[start_row_idx+i][start_col_idx+j]:
                        curr_elements_count += 1
                        found_coords.add((i, j))

                        if curr_elements_count >= searched_elements_count:
                            return True

                    show_colorized_matrices(small_matrix_bin, big_matrix_bin, start_row_idx, start_col_idx, i, j,
                                            found_coords, curr_elements_count, sleep=.1)
    return False


if __name__ == '__main__':
    min_ratio = .33
    n1 = int(input('(n1) > '))
    t1 = create_matrix(n1, n1)
    fill_matrix(t1)

    n2 = int(input('(n2) > '))
    t2 = create_matrix(n2, n2)
    fill_matrix(t2)

    print(func(t1, t2, min_ratio))

'''
5
23 1451 542 435 24
25 235 13 124 42
12 314 32 31 422
543 123 431 324 34
4324 53 134 114 34
3
43 14 13
354 31 18
54 213 341


10 
901 309 593 633 710 178 834 874 51 901 
762 505 310 538 960 226 971 897 844 920
620 757 986 576 956 341 24 329 228 823 
472 938 777 806 336 296 761 148 268 151
131 186 77 630 527 599 199 680 771 428 
414 252 88 810 771 449 202 617 442 827 
156 640 361 517 372 951 348 606 135 201 
517 192 607 19 722 982 987 181 603 554 
208 135 973 385 338 351 214 261 121 2 
422 63 241 857 419 740 920 370 931 239 
4
233 8 223 41 
154 346 301 59 
404 338 458 209 
18 215 153 379
'''
