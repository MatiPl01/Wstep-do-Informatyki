"""
Zadanie 7. Dane sa dwie tablice mogace pomiescic taka sama liczbe elementów: T1[N][N] i T2[M], gdzie
M=N*N. W kazdym wierszu tablicy T1 znajduja sie uporzadkowane niemalejaco (w obrebie wiersza) liczby
naturalne. Prosze napisac funkcje przepisujaca wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy
T2 były uporzadkowane niemalejaco.
"""

import os
import time
from colorama import Style, Fore


def print_colorized_matrix(source_matrix, target_list, target_elements, pointers, curr_val_row_idx, lowest_val_row_indices, *, sleep=.3):
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
            if row_idx == curr_val_row_idx and col_idx == pointers.get(row_idx):      # Colorize currently checked field
                print_val('red', val)
            elif row_idx in lowest_val_row_indices and col_idx == pointers[row_idx]:  # Colorize fields that have the same value as lowest number
                print_val('blue', val)
            elif row_idx in pointers and pointers[row_idx] == col_idx:                # Colorize positions of pointers
                print_val('yellow', val)
            elif row_idx not in pointers or col_idx < pointers[row_idx]:              # Colorize values that were moved to the target_list
                print_val('LIGHTBLACK_EX', val)
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


def rewrite_values(source_matrix: [[int]], target_list: list):
    """Rewrites values from 'source_matrix' to 'target_matrix' in non-decreasing order.
    Note that all rows in 2-dimensional 'source_matrix' list must be sorted in
    non-decreasing order as well."""
    # Trace position of pointers in each row of 'source_matrix' to move appropriate values
    pointers = dict.fromkeys(range(len(source_matrix)), 0)

    rewritten_elements = 0

    while pointers:
        pointers_iterator = iter(pointers.items())
        row_idx, col_idx = next(pointers_iterator)
        lowest_val = source_matrix[row_idx][col_idx]
        lowest_val_row_indices = {row_idx}

        # Look for the lowest value and store all its occurrences (whe repeated)
        for row_idx, col_idx in pointers_iterator:
            curr_val = source_matrix[row_idx][col_idx]
            if curr_val < lowest_val:
                lowest_val = curr_val
                lowest_val_row_indices = {row_idx}
            elif curr_val == lowest_val:
                lowest_val_row_indices.add(row_idx)

            print_colorized_matrix(source_matrix, target_list, len(source_matrix[0]), pointers, row_idx, lowest_val_row_indices,
                                   sleep=.1)

        # Rewrite the lowest value currently found appropriate number of times corresponding to
        # the number of its occurrences.
        # Move pointers to the right if a value is our 'lowest_val' and remove a pointer
        # if exceeds number of columns.
        for row_idx in lowest_val_row_indices:
            pointers[row_idx] += 1
            if pointers[row_idx] >= len(source_matrix[row_idx]):
                pointers.pop(row_idx)
            target_list[rewritten_elements] = lowest_val
            rewritten_elements += 1


if __name__ == '__main__':
    n = int(input('(n) > '))
    t1 = create_matrix(n, n)
    fill_matrix(t1)
    t2 = [None] * n*n
    rewrite_values(t1, t2)
    print()
    print(t2)
    # print(t2 == sorted(val for row in t1 for val in row))  # Check if works

'''
10
0 7 14 17 28 35 59 79 81 98
13 22 37 40 42 54 54 54 62 97
16 31 72 76 77 81 83 89 96 99
13 38 43 54 58 71 78 84 93 96
11 26 31 34 47 48 48 49 65 97
0 13 20 49 54 61 79 81 96 99
19 21 26 44 53 62 84 85 92 100
17 17 25 34 41 42 64 75 80 90
1 11 34 54 61 63 66 78 80 100
41 52 61 72 73 78 93 94 94 95

20
43 55 131 192 196 208 238 248 257 447 649 750 792 803 884 905 920 925 949 992
47 69 75 193 308 415 442 478 546 611 693 704 755 782 785 790 884 894 962 987
48 76 124 127 186 198 263 280 322 327 494 549 584 656 663 794 896 960 972 977
30 38 142 148 156 159 204 278 359 405 452 456 653 675 690 727 754 771 860 927
73 254 291 470 482 528 542 543 692 694 710 724 729 754 804 844 903 907 945 987
9 32 38 46 47 48 246 247 248 349 496 549 654 671 723 748 771 819 880 950
73 147 188 252 276 293 350 409 438 451 535 654 750 800 806 849 909 933 948 968
4 53 182 218 320 331 381 386 432 456 520 524 542 570 594 627 649 719 860 976
26 57 100 164 172 202 289 437 501 545 762 789 809 817 818 846 887 891 913 961
60 111 205 221 232 233 314 365 456 469 495 523 561 579 655 752 825 829 836 851
91 123 137 181 218 287 309 325 395 500 519 661 686 765 792 911 920 975 985 996
30 126 144 188 196 203 288 327 366 469 486 546 574 612 621 637 717 718 721 841
16 71 116 130 143 148 204 270 326 346 429 438 563 679 704 823 888 931 967 991
18 89 101 207 265 332 390 392 513 546 556 563 576 583 691 762 805 824 824 896
83 112 140 172 254 256 260 319 346 389 405 515 685 741 773 801 807 810 839 931
4 71 122 132 193 200 253 305 349 415 444 471 501 695 717 809 817 845 964 976
41 166 385 393 441 448 464 545 584 606 610 649 650 680 694 807 861 872 891 894
30 31 43 92 118 149 205 206 299 332 470 472 592 594 714 751 751 902 925 987
325 437 516 524 559 560 629 646 648 667 775 824 849 867 894 922 939 974 991 993
36 137 149 215 282 324 389 445 456 489 574 644 717 740 744 816 907 911 926 958

25
0 0 1 2 2 2 2 2 2 4 4 4 4 4 5 5 5 6 6 6 7 8 9 9 9
0 0 0 1 1 3 3 3 3 4 4 4 4 6 6 6 6 8 8 8 9 9 9 9 9
0 0 0 0 1 4 4 5 5 5 5 6 6 6 7 7 7 8 9 9 9 9 9 10 10
0 0 1 1 1 2 2 3 3 3 4 4 4 4 5 5 5 6 7 7 7 8 10 10 10
0 0 0 1 1 2 3 3 3 3 3 3 3 4 4 5 5 7 7 7 8 8 9 10 10
0 0 0 1 1 2 2 3 4 4 4 5 6 6 6 6 6 6 7 8 9 9 10 10 10
0 1 1 1 2 2 2 3 3 3 3 4 4 5 5 5 6 6 7 7 7 8 8 9 9
0 0 0 0 1 1 1 2 3 3 4 4 5 5 5 5 5 6 6 7 8 9 10 10 10
0 1 1 1 2 2 3 3 4 4 4 5 6 6 7 7 7 8 8 9 9 9 10 10 10
0 1 1 1 2 2 3 3 4 4 4 5 5 5 6 6 6 6 7 7 8 10 10 10 10
0 0 1 1 1 2 2 3 4 4 4 7 7 7 8 9 9 9 9 10 10 10 10 10 10
0 0 0 1 1 1 1 1 2 3 6 6 7 7 8 8 8 8 9 9 9 9 10 10 10
0 0 0 0 2 2 2 3 3 3 4 4 4 5 5 6 6 6 7 7 8 9 10 10 10
2 2 2 3 3 3 4 4 5 5 5 6 6 6 6 7 7 7 8 8 8 8 9 10 10
1 3 3 3 4 5 5 6 6 6 7 7 7 8 8 8 8 9 9 9 9 10 10 10 10
0 0 0 0 0 1 1 2 2 4 5 5 5 5 6 6 7 7 8 8 9 10 10 10 10
1 1 1 1 2 3 3 4 5 5 5 5 6 6 6 7 8 8 9 9 9 9 9 10 10
0 1 2 3 3 3 4 4 4 5 5 5 5 5 6 6 6 7 7 7 8 8 9 10 10
0 1 2 2 2 2 2 2 3 4 4 4 5 6 6 6 6 7 7 8 8 9 10 10 10
1 1 2 3 3 3 4 4 5 5 5 5 7 7 7 8 8 8 9 9 9 10 10 10 10
0 0 1 1 1 1 1 2 3 3 4 4 4 5 6 6 7 8 8 8 9 9 10 10 10
0 0 0 1 1 1 1 2 3 3 3 4 5 6 6 7 7 7 7 7 8 8 9 10 10
0 0 0 1 2 2 3 4 4 5 5 5 5 5 6 6 7 8 8 8 8 9 9 10 10
0 0 0 1 1 2 2 2 3 3 3 5 5 5 5 6 7 7 7 9 9 9 10 10 10
0 0 1 1 2 2 3 4 4 4 5 5 5 6 6 6 7 7 7 7 8 8 9 9 10
'''
